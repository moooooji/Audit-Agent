"""Utility & helper functions."""
import json
import threading
from langgraph.types import Send

from react_agent.state import State
from react_agent.llm_utils import (
    json_str_to_dict, 
    save_json, 
    map_update,
    _init_db,
    load_file,
    call_gemini_api,
    set_gemini_config,
    call_chatgpt_api,
    build_llm_chunk
)

from react_agent.prompt import (
    ARCHITECTURE_ANALYSIS_TEMPLATE, 
    ARCHITECTURE_ASSESSMENT_TEMPLATE,
    ARCHITECTURE_CORRECTION_TEMPLATE,
    THREAT_ANALYSIS_TEMPLATE,
    CHECKLIST_TEMPLATE,
    CHECKLIST_CORRECTION_TEMPLATE,
    CHECKLIST_ASSESSMENT_TEMPLATE,
    CODE_BINDING_ASSESSMENT_TEMPLATE,
)
from react_agent.config import (
    set_gemini_config,
    CodeBindingAssessmentConfig
)

from google.genai import types

# import variables
import react_agent.variables

react_agent.variables.threats_list
react_agent.variables.actors_map

threat_count = 0
checklist_count = 0
BATCH_SIZE = 10

# 병렬 처리를 위한 세마포어 변수 추가
api_semaphore = threading.Semaphore(1)  # 한 번에 하나의 스레드만 API 대기 로직 실행
processed_threats_batches = 0  # 처리된 위협 배치 수 추적
processed_checklist_batches = 0  # 처리된 체크리스트 배치 수 추적

from time import sleep
from react_agent.Utils.RedisUtil import RedisUtil
from react_agent.Utils.AnalyzeSolidity import AnalyzeSolidity
# architecture analysis node
def analyze_architecture(state: State) -> State:
    """architecture analysis node"""
    
    # not feedback loop
    if state.get("architecture_feedback_loop_count", 0) == 0:
        print("first architecture analysis ...")
        state["is_initial_architecture_analysis"] = True
        # generate llm response
        target_docs = load_file(state["target_docs_path"])
        
        prompt = ARCHITECTURE_ANALYSIS_TEMPLATE.replace(
            "{target_docs}", target_docs
        )
        
        # 프롬프트 템플릿만 사용
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        response = call_gemini_api(contents, set_gemini_config("ARCHITECTURE_RESPONSE_CONFIG"))
        # parsing response and save to file
        response_dict = json_str_to_dict(response.text)
        # save architecture_analysis
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed first architecture analysis")
        
        return {
            "is_initial_architecture_analysis": False,
            "architecture_feedback_loop_count": state.get("architecture_feedback_loop_count", 0)
            }
    else:
        print("feedback loop architecture analysis ...")
        state["is_feedback_architecture_analysis"] = True
        # load architecture_analysis
        target_docs = load_file(state["target_docs_path"])
        analysis_json = load_file("results/architecture_analysis.json")
        # read assessment file
        assessment_architecture_json = load_file("results/assessment_architecture.json")
            
        prompt = ARCHITECTURE_CORRECTION_TEMPLATE.replace(
            "{target_docs}", target_docs
        ).replace(
            "{initial_architecture_analysis}", analysis_json
        ).replace(
            "{assessment_architecture}", assessment_architecture_json
        )
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        response = call_gemini_api(contents, set_gemini_config("ARCHITECTURE_CORRECTION_CONFIG"))
        
        map_update(json.loads(response.text), state)
        
        response_dict = json_str_to_dict(response.text)
        # parsing response and save to file
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed feedback loop architecture analysis")
        
        return {"is_feedback_architecture_analysis": False}
    
# assessment node
def assess_architecture(state: State) -> State:
    """architecture assessment node"""
    state["is_assessment_analysis"] = True
    # generate llm response
    target_docs = load_file(state["target_docs_path"])
    
    # read architecture_analysis 
    analysis_json = load_file("results/architecture_analysis.json")
    
    prompt = ARCHITECTURE_ASSESSMENT_TEMPLATE.replace(
        "{target_docs}", target_docs
    ).replace(
        "{initial_architecture_analysis}", analysis_json
    )
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]
    
    response = call_gemini_api(contents, set_gemini_config("ARCHITECTURE_ASSESSMENT_CONFIG"))
    
    # parsing json and save to file
    response_dict = json_str_to_dict(response.text)
    save_json(response_dict, "results/assessment_architecture.json")
    print("completed assessing architecture")
    
    return {
        "is_assessment_analysis": False, 
        "architecture_feedback_loop_count": state["architecture_feedback_loop_count"]+1
        }

def analyze_threats(state: State) -> State:
    print("analyzing threats ...")
    state["is_threat_analysis"] = True
    id_weight = 1

    global threat_count
    global processed_threats_batches
    
    # prevent race condition
    with api_semaphore:
        # for google gemini api RPM limit
        current_batch = (threat_count - 1) // BATCH_SIZE
        if current_batch > processed_threats_batches:
            processed_threats_batches = current_batch
            print("gemini api initializing for threats batch ", current_batch, " ...")
            sleep(60)
            print("gemini api initialized for threats batch ", current_batch)

    target_docs = load_file(state["target_docs_path"])
    # read architecture_correction file
    architecture_analysis = load_file("results/architecture_analysis.json")
    
    cur_actor = build_llm_chunk(architecture_analysis, state["current_actor_id"] + 1)
    
    prompt = THREAT_ANALYSIS_TEMPLATE.replace(
        "{target_docs}", target_docs
    ).replace(
        "{chunk}", json.dumps(cur_actor)
    ).replace(
        "{architecture_analysis}", architecture_analysis
    )
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    response = call_gemini_api(contents, set_gemini_config("THREAT_ANALYSIS_CONFIG"))
    # parsing response and save to file
    response_dict = json_str_to_dict(response.text)
    
    print(f"[+] Processing actor {state["current_actor_id"]+1}...")
    print(f"[+] Threats count: {len(response_dict['threats'])}")
    for threat in response_dict["threats"]:
        react_agent.variables.threats_list.append(threat)

        save_json(threat, f'results/actors/threats_actor_{state["current_actor_id"]+1}.json')
    
    with api_semaphore:
    
        threat_count += 1
        print(f"Saved threats for actor {state["current_actor_id"]+1}")
        
        print(f"threat_count : {threat_count}")
        print(f"len(react_agent.variables.actors_map) : {len(react_agent.variables.actors_map)}")
    
        if threat_count == len(react_agent.variables.actors_map):
            # for all threats, assign sequential id weights
            threat_count = 0
            
            for threat in react_agent.variables.threats_list:
                threat["id"] = id_weight
                id_weight += 1
            
            print("threats_list : ", len(react_agent.variables.threats_list))
                
            save_json({ "threats": react_agent.variables.threats_list }, 'results/all_threats.json')
            print("Saved all threats in 'all_threats.json'")
            print("completed analyzing threats")
            
            print("gemini api initializing ...")
            sleep(60)
            print("gemini api initialized")
            
            return {
                    "is_threat_analysis": False,
                    "is_initial_checklist_analysis": True,
                    "threat_list_length": len(react_agent.variables.threats_list),
                    "current_threat_count": id_weight-1,
                    }
            
def map_get_assessment_checklist(state: State) -> State:
    if state["is_initial_checklist_analysis"] == True:
        batch_sends = []
        with open("results/all_threats.json", "r") as f:
            threats_data = json.load(f)
        threats = threats_data["threats"]
        for threat in threats:
            threat_id = threat["id"]
            print(f"Processing threat ID: {threat_id}")
            actor_id = threat["actor_risk"]["actor_id"]
            actor_details = None
            if actor_id is not None:
                actor_details = react_agent.variables.actors_map.get(actor_id, {})
            component_id = threat["threat_target"]["component_id"]
            component_details = None
            if component_id is not None:
                component_details = react_agent.variables.components_map.get(component_id, {})
            asset_ids = threat["threat_target"]["asset_ids"]
            asset_details = [
                react_agent.variables.assets_map.get(asset_id, {}) 
                for asset_id in asset_ids
            ]
            behavior_id = threat["attack_surface"]["behavior_id"]
            behavior_details = None
            if behavior_id is not None:
                behavior_details = react_agent.variables.behaviors_map.get(behavior_id, {})
            data_flow_id = threat["attack_surface"]["data_flow_id"]
            data_flow_details = None
            if data_flow_id is not None:
                data_flow_details = react_agent.variables.data_flows_map.get(data_flow_id, {})
            boundary_id = threat["trust_boundary_risk"]["boundary_id"]
            boundary_details = None
            if boundary_id is not None:
                boundary_details = react_agent.variables.trust_boundaries_map.get(boundary_id, {})
            threat_with_context = {
                "threat": threat,
                "related_entities": {
                    "actor": actor_details,
                    "component": component_details,
                    "assets": asset_details,
                    "behavior": behavior_details,
                    "data_flow": data_flow_details,
                    "trust_boundary": boundary_details
                }
            }
            batch_sends.append(Send("generate_parallel_checklist", {
                "threat_with_context": threat_with_context, 
            }))
        print("batch_sends : ", len(batch_sends))
        
        return batch_sends
    else:
        return "assess_checklist"
    
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
import os
if not os.path.exists("cache"):
    os.makedirs("cache")
set_llm_cache(SQLiteCache(database_path="./cache/llm_cache.db"))

async def generate_parallel_checklist(state: State) -> State:
    threat_with_context = state["threat_with_context"]
    threat = threat_with_context["threat"]
    

    from react_agent.prompt import CHECKLIST_TEMPLATE
    from google.genai import types

    prompt = CHECKLIST_TEMPLATE.replace(
        "{context}", json.dumps(threat_with_context["related_entities"])
    ).replace(
        "{threat_analysis}", json.dumps({"threats": [threat]})  # 단일 위협을 배열로 감싸서 템플릿 형식 유지
    )
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    from langchain_google_genai import ChatGoogleGenerativeAI
    from dotenv import load_dotenv
    from pydantic import BaseModel

    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17",
        temperature=0
    )
    from react_agent.state import Checklist
    structured_llm = llm.with_structured_output(Checklist)
    response = await structured_llm.ainvoke(prompt)
    json_data = response.model_dump()
    print(f"in parallel, generated {len(json_data)}, inside length : {len(json_data['checklist_items'])}")
    return {
        "tmp_checklist": json_data["checklist_items"],
        "is_initial_checklist_analysis": False,
        }

def route_checklist(state: State):
    from react_agent.variables import CHECKLIST_FEEDBACK_LOOP_COUNT
    tmp_checklist = state["tmp_checklist"]
    print(f"in route_checklist, generated {len(tmp_checklist)} checklist items")
    
    print(f"is_initial_checklist_analysis : {state["is_initial_checklist_analysis"]}")
    
    if state["is_initial_checklist_analysis"] == True:
        return {"is_initial_checklist_analysis": True}
    else:
        # 여기서 생성된 체크리스트들 전부 모일테니, unique id 다시 재 부여할 필요가있을거같음
        print(f"여길 들어오나?")
        checklist_items = tmp_checklist
        index = 0
        for item in checklist_items:
            item["id"] = index
            index += 1
            # TODO 중복체크 여기서 처리하는 로직 넣으면 될듯.
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
        return {
            "is_feedback_checklist_analysis": False,
        }
    


def generate_checklist(state: State) -> State:
    
    global checklist_count
    global processed_checklist_batches
    
    if state["checklist_feedback_loop_count"] == 0:
        print("initial checklist analysis ...")
        state["is_initial_checklist_analysis"] = True
        
        response = generate_llm_response(state)
        
        # 초기 생성 시 response는 리스트 (개별 처리 결과들)
        checklist_items = []
        for threat_response in response:
            if 'checklist_items' in threat_response:
                checklist_items.extend(threat_response['checklist_items'])
        
        print(f"받은 checklist_items 개수: {len(checklist_items)}개")
        
        # 중복 제거: title과 description이 같은 항목 제거
        unique_items = []
        seen = set()
        for item in checklist_items:
            # title과 description을 기준으로 중복 체크
            item_key = (item.get('title', ''), item.get('description', ''))
            if item_key not in seen:
                seen.add(item_key)
                unique_items.append(item)
        
        checklist_items = unique_items
        print(f"중복 제거 후 checklist_items : {len(checklist_items)}개")
                    
        print("completed initial checklist analysis")
        
        id_weight = 1
        
        for item in checklist_items:
            item['id'] = id_weight
            id_weight = id_weight+1
            
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
            
        print("checklist_items : ", len(checklist_items))
        checklist_items.clear()  # 더 확실한 초기화 방법
        
        print("Saved checklist in 'results/checklist.json'")
        print("completed generating checklist")
        
        print("gemini api initializing ...")
        sleep(60)
        print("gemini api initialized")
        
        return {"is_initial_checklist_analysis": False, "is_feedback_checklist_analysis": False}
        
    else:
        print("feedback loop checklist analysis ...")
        state["is_feedback_checklist_analysis"] = True
        
        response = generate_llm_response(state)
        
        # 피드백 시 response는 딕셔너리 (전체 처리 결과)
        checklist_items = response.get('checklist_items', [])
        
        print(f"받은 checklist_items 개수: {len(checklist_items)}개")
        
        # 중복 제거: title과 description이 같은 항목 제거
        unique_items = []
        seen = set()
        for item in checklist_items:
            # title과 description을 기준으로 중복 체크
            item_key = (item.get('title', ''), item.get('description', ''))
            if item_key not in seen:
                seen.add(item_key)
                unique_items.append(item)
        
        checklist_items = unique_items
        print(f"중복 제거 후 checklist_items : {len(checklist_items)}개")
            
        print("completed feedback loop checklist analysis")
        
        id_weight = 1
        
        for item in checklist_items:
            item['id'] = id_weight
            id_weight = id_weight+1
            
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
            
        print("checklist_items : ", len(checklist_items))
        checklist_items.clear()  # 더 확실한 초기화 방법
        
        print("Saved checklist in 'results/checklist.json'")
        print("completed generating checklist")
        
        print("gemini api initializing ...")
        sleep(60)
        print("gemini api initialized")
        
        return {"is_initial_checklist_analysis": False, "is_feedback_checklist_analysis": False}
        

def assess_checklist(state: State) -> State:
    print("verifying checklist ...")
    state["is_assessment_checklist"] = True
    
    threat_analysis = load_file("results/all_threats.json")
    initial_checklist = load_file("results/checklist.json")
    
    prompt = CHECKLIST_ASSESSMENT_TEMPLATE.replace(
        "{threat_analysis}", threat_analysis
        ).replace(
            "{initial_checklist}", initial_checklist
        )
    
    contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    response = call_gemini_api(contents, set_gemini_config("CHECKLIST_ASSESSMENT_CONFIG"))
    response = json_str_to_dict(response.text)
    
    save_json(response, "results/assessment_checklist.json")
    
    print("completed verifying checklist")
    
    return {"is_assessment_checklist": False, "checklist_feedback_loop_count": state["checklist_feedback_loop_count"]+1}

def init_db(state: State) -> State:
    print("initializing vector db ...")
    state["is_init_db"] = True
    _init_db()
    
    print("completed initializing vector db")
    
    state["is_init_db"] = False
    
def code_binding(state: State) -> State:
    if state.get("code_binding_feedback_loop_count", 0) == 0:
        print("initial code binding ...")

        with open("results/checklist.json", "r") as f:
            checklist = json.load(f)

        similar_functions_list = []
        filtered_items = [item for item in checklist["checklist_items"]
                  if item.get("need_code_binding") is True]

        function_codes = {}

        for item in filtered_items:
            item_id = item["id"]          # ← 1부터 시작하는 고유 ID 사용
            desc = item["description"]
            similar_funcs = AnalyzeSolidity.search(desc, k=3)

            function_codes[item_id] = {   # 키도, 내부 표시도 모두 같은 ID
                "checklist_item_id": item_id,
                "similar_functions": [
                    {
                        "contract_name": d.metadata["contract"],
                        "function_name": d.metadata["function"],
                        "code": RedisUtil.get_function_code(
                            f"{d.metadata['contract']}.{d.metadata['function']}"
                        )
                    }
                    for d in similar_funcs
                ],
            }
            #print(f"[+] Added function code for {contract_name}.{function_name}")

        print("[+] Saving function codes to code_binding.json...")
        with open("results/code_binding.json", "w") as f:
            json.dump({"function_codes": function_codes}, f, ensure_ascii=False, indent=2)

        state["is_initial_code_binding"] = True
        print("completed initial code binding")

    else:
        print("feedback loop code binding ...")
        state["is_feedback_code_binding"] = True
        print("completed feedback loop code binding")

    return {
        "is_initial_code_binding": False, 
        "is_feedback_code_binding": False,
        "code_binding_feedback_loop_count": state.get("code_binding_feedback_loop_count", 0)
        }


def assess_code_binding(state: State) -> State:
    print("assessing code binding ...")
    state["is_assessment_code_binding"] = True
    
    code_binding = load_file("results/code_binding.json")
    checklist_items = load_file("results/checklist.json")
    
    prompt = CODE_BINDING_ASSESSMENT_TEMPLATE.replace(
        "{code_binding}", code_binding,
    ).replace(
        "{checklist_items}", checklist_items
    )
    
    contents = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    response = call_chatgpt_api(contents, CodeBindingAssessmentConfig)
    
    response_dict = json_str_to_dict(response.choices[0].message.content)
    save_json(response_dict, "results/assessment_code_binding.json")
    
    print("completed assessing code binding")
    
    initialize_state(state)
    
    return {
        "is_assessment_code_binding": False, 
        "code_binding_feedback_loop_count": state["code_binding_feedback_loop_count"]+1
        }

def initialize_state(state: State) -> State:
    state["architecture_feedback_loop_count"] = 0
    state["checklist_feedback_loop_count"] = 0
    state["code_binding_feedback_loop_count"] = 0
    
    state["is_initial_architecture_analysis"] = False
    state["is_feedback_architecture_analysis"] = False
    state["is_assessment_analysis"] = False
    state["is_assessment_checklist"] = False
    state["is_assessment_code_binding"] = False
    state["is_init_db"] = False
    state["is_initial_checklist_analysis"] = False
    state["is_feedback_checklist_analysis"] = False
    state["is_initial_code_binding"] = False
    state["is_feedback_code_binding"] = False
    state["is_threat_analysis"] = False
    
    state["current_actor_id"] = 0