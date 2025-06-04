import json
import re
import time
from typing import Any, Callable

from google.genai import types
from google.api_core import exceptions as google_exceptions
from openai import OpenAIError

from react_agent.state import State

from react_agent.Utils.FunctionParser import FunctionParser
from react_agent.Utils.RedisUtil import RedisUtil
from react_agent.Utils.AnalyzeSolidity import AnalyzeSolidity
from react_agent.variables import (
    architecture_analysis,
    gemini_model,
    gemini_client,
    chatgpt_model,
    chatgpt_client,
)

import react_agent.variables

react_agent.variables.threats_list
react_agent.variables.actors_map
react_agent.variables.components_map
react_agent.variables.assets_map
react_agent.variables.data_flows_map
react_agent.variables.trust_boundaries_map
react_agent.variables.behaviors_map

# cache storage
_cache_storage: dict = {}

def init_state(state: State) -> State:
    """initialize state"""
    state.is_threat_analysis = False
    state.is_checklist_analysis = False
    state.is_code_binding = False
    state.is_init_db = False
    state.feedback_loop_count = 0
    state.threat_prompt = ""
    state.checklist_prompt = ""
    return state

def json_str_to_dict(raw: str) -> dict:
    """
    코드펜스(```` … ```​`)가 포함될 수도 있는 JSON 문자열을
    깨끗이 정리한 뒤 dict 로 변환한다.
    """
    s = raw.strip()

    # remove ```json … ``` or ``` … ```
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s)   # remove ```json … ``` or ``` … ```
        s = re.sub(r"\s*```$", "", s)            # remove ```

    return json.loads(s)

def save_json(data: dict, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        
def load_file(path: str) -> dict:
    with open(path, "r") as f:
        return f.read()
    
def build_llm_chunk(data: dict, actor_id: int) -> dict:
    # Parse the data if it's a string
    if isinstance(data, str):
        data = json.loads(data)
        
    # 실제 actor_id를 얻는 방법 변경
    # 인덱스 대신 실제 액터의 ID를 가져오도록 수정
    actual_actors = data["actors"]
    if actor_id > len(actual_actors):
        raise ValueError(f"Actor index {actor_id} out of range (total actors: {len(actual_actors)})")
    
    # 인덱스를 사용하여 액터 가져오기 (0부터 시작)
    actor_index = actor_id - 1
    actor = actual_actors[actor_index]
    actual_actor_id = actor["id"]  # 실제 JSON에 있는 액터 ID (예: 101, 102 등)
    
    # 1. related behaviors
    behaviors = [
        b for b in data["behaviors"]
        if b["initiator_type"] == "Actor" and b["initiator_id"] == actual_actor_id
    ]

    # 2. related components (target of behaviors)
    component_ids = {b["target_id"] for b in behaviors}
    components = [c for c in data["components"] if c["id"] in component_ids]

    # 3. related assets (from components' assets_managed)
    asset_ids = {aid for comp in components for aid in comp.get("assets_managed", [])}
    assets = [a for a in data["assets"] if a["id"] in asset_ids]

    # 4. related data_flows (actor or related component involved)
    data_flows = [
        df for df in data["data_flows"]
        if df["source_id"] == actual_actor_id or df["destination_id"] in component_ids
    ]

    # 5. related trust boundaries
    all_component_ids = {c["id"] for c in components}
    trust_boundaries = [
        tb for tb in data["trust_boundaries"]
        if any(cid in all_component_ids for cid in tb["between_ids"])
    ]

    # 6. combine results
    chunk = {
        "actor": actor,
        "behaviors": behaviors,
        "components": components,
        "assets": assets,
        "data_flows": data_flows,
        "trust_boundaries": trust_boundaries,
    }

    return chunk

def retry_on_error(max_retries: int = 3, sleep_time: int = 60) -> Callable:
    """API 호출 실패 시 재시도하는 데코레이터"""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    # 응답이 None이거나 빈 문자열인 경우도 에러로 처리
                    if result is None or (isinstance(result, str) and not result.strip()):
                        raise ValueError("Empty response received")
                    return result
                except (google_exceptions.ServiceUnavailable, 
                        google_exceptions.InternalServerError,
                        google_exceptions.BadRequest,
                        OpenAIError,
                        ValueError) as e:
                    retries += 1
                    if retries == max_retries:
                        raise e
                    print(f"\n⚠️ API 호출 실패 (시도 {retries}/{max_retries}): {str(e)}")
                    print(f"⏳ {sleep_time}초 후 재시도합니다...")
                    time.sleep(sleep_time)
            return None
        return wrapper
    return decorator

@retry_on_error()
def call_gemini_api(contents: list, config: dict) -> Any:
    """Gemini API 호출"""
    return gemini_client.models.generate_content(
        model=gemini_model,
        contents=contents,
        config=config,
    )

@retry_on_error()
def call_chatgpt_api(messages: list, response_format: dict) -> Any:
    """ChatGPT API 호출"""
    return chatgpt_client.beta.chat.completions.parse(
        model=chatgpt_model,
        messages=messages,
        response_format=response_format
    )
    
def create_cache(display_name: str, content: str, ttl: str = "3600s"):
    """
    캐시를 생성하고 반환합니다.
    - 이미 존재하는 캐시가 있으면 해당 캐시를 재사용합니다.
    - 캐시가 없으면 새로 생성합니다.
    """
    # 이름을 직접 키로 사용
    cache_key = display_name
    
    # 이미 저장된 캐시가 있는지 확인
    if cache_key in _cache_storage:
        print(f"[*] 기존 캐시 사용: {cache_key}")
        return _cache_storage[cache_key]
    
    # 새 캐시 생성 시도
    try:
        # 최소 토큰 수 요구사항으로 인한 에러 방지를 위해 콘텐츠 길이 확인
        # 대략적으로 4 바이트 = 1 토큰으로 가정
        estimated_tokens = len(content) / 4
        
        if estimated_tokens < 4000:
            print(f"[!] 콘텐츠가 최소 토큰 요구사항(4096)을 충족하지 않을 수 있습니다. 예상 토큰: {estimated_tokens:.0f}")
            # 토큰이 부족하면 None 반환하고 캐시 없이 진행
            return None
        # 캐시 생성 시도
        cache = gemini_client.caches.create(
            model=gemini_model,
            config=types.CreateCachedContentConfig(
                display_name=display_name,
                ttl=ttl,
                system_instruction=content
            )
        )
        
        # 성공하면 저장소에 저장
        _cache_storage[cache_key] = cache
        print(f"[+] 캐시 생성 완료: {cache_key}")
        return cache
    except Exception as e:
        print(f"⚠️ 캐시 생성 실패: {str(e)}")
        return None

def map_update(response_dict: dict, state: State):
    """map update"""
    print("updating map...")
    
    try:
        target_docs = load_file(state["target_docs_path"])
        # map update
        react_agent.variables.components_map.update({comp["id"]: comp for comp in response_dict.get("components", [])})
        react_agent.variables.actors_map.update({actor["id"]: actor for actor in response_dict.get("actors", [])})
        react_agent.variables.assets_map.update({asset["id"]: asset for asset in response_dict.get("assets", [])})
        react_agent.variables.data_flows_map.update({flow["id"]: flow for flow in response_dict.get("data_flows", [])})
        react_agent.variables.trust_boundaries_map.update({tb["id"]: tb for tb in response_dict.get("trust_boundaries", [])})
        react_agent.variables.behaviors_map.update({behavior["id"]: behavior for behavior in response_dict.get("behaviors", [])})

        architecture_analysis["system_context"]["docs"]["overview"] = target_docs
        architecture_analysis["system_context"]["docs"]["pol"] = target_docs
        
        # save result
        with open("results/enriched_architecture_analysis.json", "w") as f:
            json.dump(architecture_analysis, f, indent=2)

        print("✅ 아키텍처 분석이 완료되었습니다.")
        print(f"- 컴포넌트: {len(react_agent.variables.components_map)}개")
        print(f"- 액터: {len(react_agent.variables.actors_map)}개") 
        print(f"- 자산: {len(react_agent.variables.assets_map)}개")
        print(f"- 데이터 흐름: {len(react_agent.variables.data_flows_map)}개")
        print(f"- 신뢰 경계: {len(react_agent.variables.trust_boundaries_map)}개")
        print(f"- 행동: {len(react_agent.variables.behaviors_map)}개")

    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        
    print("completed updating map")
    
def _init_db():
    """initialize vector db && redis"""
    print("initializing vector db && redis ...")
    
    with open("./src/react_agent/Utils/final_analysis_results.json", "r") as f:
        functions = json.load(f)
        
    # embedding functions
    print("embedding functions ...")
    vector_db = AnalyzeSolidity.store_db(functions)
    print("[+] vector db: ", vector_db)
    print("completed embedding functions")
    
    # set redis
    print("setting functions in Redis ...")
    functions = FunctionParser.process_directory("./src/react_agent/Utils/contracts/src")
    RedisUtil.set_function_codes_from_json(functions)
    print("[+] test: ", RedisUtil.get_function_code("BeaconRootsHelper.setZeroValidatorPubkeyGIndex"))
    
    print("completed setting functions in Redis")
    
    print("Stored functions in Redis")
    
    return

    