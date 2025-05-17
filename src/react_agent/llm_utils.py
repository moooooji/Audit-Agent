import json
import re

from google.genai import types

from react_agent.state import State
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
    ARCHITECTURE_RESPONSE_CONFIG, 
    ARCHITECTURE_ASSESSMENT_CONFIG,
    ARCHITECTURE_CORRECTION_CONFIG,
    THREAT_ANALYSIS_CONFIG,
    ChecklistConfig,
    ChecklistAssessmentConfig,
    CodeBindingAssessmentConfig
)
from react_agent.Utils.FunctionParser import FunctionParser
from react_agent.Utils.RedisUtil import RedisUtil
from react_agent.Utils.AnalyzeSolidity import AnalyzeSolidity
from react_agent.variables import (
    architecture_analysis,
    components_map,
    actors_map,
    assets_map,
    data_flows_map,
    trust_boundaries_map,
    behaviors_map,
    gemini_model,
    gemini_client,
    chatgpt_model,
    chatgpt_client,
    threats_list,
    ARCHITECTURE_FEEDBACK_LOOP_COUNT,
    CHECKLIST_FEEDBACK_LOOP_COUNT,
    CODE_BINDING_FEEDBACK_LOOP_COUNT
)

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


def generate_llm_response(state: State) -> str:
    """generate llm response"""
    
    # first architecture analysis node
    if state.is_initial_architecture_analysis:
        print("=============initial architecture analysis node=============")
        target_docs = load_file(state.target_docs_path)
        
        prompt = ARCHITECTURE_ANALYSIS_TEMPLATE.replace("{target_docs}", target_docs)
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        response = gemini_client.models.generate_content(
            model=gemini_model,
            contents=contents,
            config=ARCHITECTURE_RESPONSE_CONFIG,
        )
        return response
    
    elif state.is_assessment_analysis and state.architecture_feedback_loop_count < ARCHITECTURE_FEEDBACK_LOOP_COUNT:
        print("=============assessment analysis node=============")
        target_docs = load_file(state.target_docs_path)
    
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
        
        response = gemini_client.models.generate_content(
            model=gemini_model,
            contents=contents,
            config=ARCHITECTURE_ASSESSMENT_CONFIG,
        )
        return response
    
    # feedback loop architecture analysis node
    elif state.is_feedback_architecture_analysis:
        print("=============feedback architecture analysis node=============")
        target_docs = load_file(state.target_docs_path)
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
        
        response = gemini_client.models.generate_content(
            model=gemini_model,
            contents=contents,
            config=ARCHITECTURE_CORRECTION_CONFIG,
        )
        
        return response
    
    # threat analysis node
    elif state.is_threat_analysis:
        print("=============threat analysis node=============")
        target_docs = load_file(state.target_docs_path)
        # read architecture_correction file
        architecture_analysis = load_file("results/architecture_analysis.json")
        
        cur_actor = build_llm_chunk(architecture_analysis, state.current_actor_id + 1)
        
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

        response = gemini_client.models.generate_content(
            model=gemini_model,
            contents=contents,
            config=THREAT_ANALYSIS_CONFIG,
        )
        return response
    
    elif state.is_initial_checklist_analysis:
        print("=============checklist analysis node=============")
        
        threats_list_copy = threats_list.copy()
        
        context = []
        
        for i in range(len(threats_list)):
            actor_id = threats_list_copy[i]["actor_risk"]["actor_id"]
            threats_list_copy[i]["actor_risk"]["actor_details"] = actors_map.get(actor_id, {})
            
            # Add threat target component and assets
            threats_list_copy[i]["threat_target"]["component_details"] = components_map.get(threats_list_copy[i]["threat_target"]["component_id"], {})
            threats_list_copy[i]["threat_target"]["asset_details"] = [assets_map.get(aid, {}) for aid in threats_list_copy[i]["threat_target"]["asset_ids"]]

            # Add behavior context
            behavior_id = threats_list_copy[i]["attack_surface"]["behavior_id"]
            threats_list_copy[i]["attack_surface"]["behavior_details"] = behaviors_map.get(behavior_id, {})

            # Add data flow context
            df_id = threats_list_copy[i]["attack_surface"]["data_flow_id"]
            threats_list_copy[i]["attack_surface"]["data_flow_details"] = data_flows_map.get(df_id, {})

            # Add trust boundary context
            tb_id = threats_list_copy[i]["trust_boundary_risk"]["boundary_id"]
            threats_list_copy[i]["trust_boundary_risk"]["boundary_details"] = trust_boundaries_map.get(tb_id, {})
            
            context.append(threats_list_copy[i])
        
        target_docs = load_file(state.target_docs_path)
        threat_analysis = load_file("results/all_threats.json")
        prompt = CHECKLIST_TEMPLATE.replace(
            "{context}", json.dumps(context)
            ).replace(
                "{threat_analysis}", threat_analysis
            )
        
        contents = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = chatgpt_client.beta.chat.completions.parse(
            model=chatgpt_model,
            messages=contents,
            response_format=ChecklistConfig
        )
        return response
    
    elif state.is_feedback_checklist_analysis:
        print("=============feedback checklist analysis node=============")
        
        threats_list_copy = threats_list.copy()
        
        context = []
        
        for i in range(len(threats_list)):
            actor_id = threats_list_copy[i]["actor_risk"]["actor_id"]
            threats_list_copy[i]["actor_risk"]["actor_details"] = actors_map.get(actor_id, {})
            
            # Add threat target component and assets
            threats_list_copy[i]["threat_target"]["component_details"] = components_map.get(threats_list_copy[i]["threat_target"]["component_id"], {})
            threats_list_copy[i]["threat_target"]["asset_details"] = [assets_map.get(aid, {}) for aid in threats_list_copy[i]["threat_target"]["asset_ids"]]

            # Add behavior context
            behavior_id = threats_list_copy[i]["attack_surface"]["behavior_id"]
            threats_list_copy[i]["attack_surface"]["behavior_details"] = behaviors_map.get(behavior_id, {})

            # Add data flow context
            df_id = threats_list_copy[i]["attack_surface"]["data_flow_id"]
            threats_list_copy[i]["attack_surface"]["data_flow_details"] = data_flows_map.get(df_id, {})

            # Add trust boundary context
            tb_id = threats_list_copy[i]["trust_boundary_risk"]["boundary_id"]
            threats_list_copy[i]["trust_boundary_risk"]["boundary_details"] = trust_boundaries_map.get(tb_id, {})
                
        context.append(threats_list_copy[i])
        
        initial_checklist = load_file("results/checklist.json")
        assessment_checklist_json = load_file("results/assessment_checklist.json")
        prompt = CHECKLIST_CORRECTION_TEMPLATE.replace(
            "{context}", json.dumps(context)
            ).replace(
                "{initial_checklist}", initial_checklist
            ).replace(
                "{assessment_checklist}", assessment_checklist_json
            )
        
        contents = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = chatgpt_client.beta.chat.completions.parse(
            model=chatgpt_model,
            messages=contents,
            response_format=ChecklistConfig
        )
        return response
    
    # verify checklist node
    elif state.is_assessment_checklist and state.checklist_feedback_loop_count < CHECKLIST_FEEDBACK_LOOP_COUNT:
        print("=============assess checklist node=============")
        
        threat_analysis = load_file("results/all_threats.json")
        initial_checklist = load_file("results/checklist.json")
        
        prompt = CHECKLIST_ASSESSMENT_TEMPLATE.replace(
            "{threat_analysis}", threat_analysis
            ).replace(
                "{initial_checklist}", initial_checklist
            )
        
        contents = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = chatgpt_client.beta.chat.completions.parse(
            model=chatgpt_model,
            messages=contents,
            response_format=ChecklistAssessmentConfig
        )
        
        return response
        
    # feedback loop verify checklist with code
    elif state.is_assessment_code_binding and state.code_binding_feedback_loop_count < CODE_BINDING_FEEDBACK_LOOP_COUNT:
        print("=============assess checklist with code node=============")
        
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
        
        response = chatgpt_client.beta.chat.completions.parse(
            model=chatgpt_model,
            messages=contents,
            response_format=CodeBindingAssessmentConfig
        )
        
        return response
    
def map_update(response_dict: dict, state: State):
    """map update"""
    print("updating map...")
    
    try:
        target_docs = load_file(state.target_docs_path)
        # map update
        components_map.update({comp["id"]: comp for comp in response_dict.get("components", [])})
        actors_map.update({actor["id"]: actor for actor in response_dict.get("actors", [])})
        assets_map.update({asset["id"]: asset for asset in response_dict.get("assets", [])})
        data_flows_map.update({flow["id"]: flow for flow in response_dict.get("data_flows", [])})
        trust_boundaries_map.update({tb["id"]: tb for tb in response_dict.get("trust_boundaries", [])})
        behaviors_map.update({behavior["id"]: behavior for behavior in response_dict.get("behaviors", [])})

        architecture_analysis["system_context"]["docs"]["overview"] = target_docs
        architecture_analysis["system_context"]["docs"]["pol"] = target_docs
        
        # save result
        with open("results/enriched_architecture_analysis.json", "w") as f:
            json.dump(architecture_analysis, f, indent=2)

        print("✅ 아키텍처 분석이 완료되었습니다.")
        print(f"- 컴포넌트: {len(components_map)}개")
        print(f"- 액터: {len(actors_map)}개") 
        print(f"- 자산: {len(assets_map)}개")
        print(f"- 데이터 흐름: {len(data_flows_map)}개")
        print(f"- 신뢰 경계: {len(trust_boundaries_map)}개")
        print(f"- 행동: {len(behaviors_map)}개")

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

    