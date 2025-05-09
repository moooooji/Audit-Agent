"""Utility & helper functions."""
import json
import re
import os
from dotenv import load_dotenv

# google genai
from google import genai
from google.genai import types

# state
from react_agent.state import State

load_dotenv()

model = "gemini-1.5-flash"

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

from react_agent.prompt import (
    ARCHITECTURE_ANALYSIS_TEMPLATE, ARCHITECTURE_RESPONSE_CONFIG, 
    ASSESSMENT_TEMPLATE, ASSESSMENT_CONFIG, 
    ARCHITECTURE_CORRECTION_TEMPLATE, ARCHITECTURE_CORRECTION_CONFIG, 
    THREAT_ANALYSIS_TEMPLATE, THREAT_ANALYSIS_CONFIG,
    CHECKLIST_TEMPLATE, CHECKLIST_CONFIG
)

# 빈 맵 초기화
actors_map = {}
assets_map = {}
components_map = {}
data_flows_map = {}
trust_boundaries_map = {}
behaviors_map = {}

# 아키텍처 분석을 위한 프롬프트 호출
architecture_analysis = {
    "system_context": {
        "docs": {
            "overview": "",
            "pol": "",
            "tokens": "",
            "governance": "",
            "dapps": ""
        },
        "components": components_map,
        "actors": actors_map,
        "assets": assets_map
    }
}

# all threats list
all_threats = []

# threats list
threats_list = []

# dataset/berachain_docs_merged.md

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

def build_llm_chunk(data: dict, actor_id: int) -> dict:
    # Parse the data if it's a string
    if isinstance(data, str):
        data = json.loads(data)
        
    actor = next((a for a in data["actors"] if a["id"] == actor_id), None)
    if not actor:
        raise ValueError(f"Actor with id {actor_id} not found")

    # 1. related behaviors
    behaviors = [
        b for b in data["behaviors"]
        if b["initiator_type"] == "Actor" and b["initiator_id"] == actor_id
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
        if df["source_id"] == actor_id or df["destination_id"] in component_ids
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

def save_json(data: dict, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        
def load_file(path: str) -> dict:
    with open(path, "r") as f:
        return f.read()

# architecture analysis node
def analyze_architecture(state: State) -> State:
    """architecture analysis node"""
    # load target docs
    target_docs = load_file(state.target_docs_path)
        
    # not feedback loop
    if state.feedback_loop_count == 0:
    
        prompt = ARCHITECTURE_ANALYSIS_TEMPLATE.replace("{DOCS}", target_docs)
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=ARCHITECTURE_RESPONSE_CONFIG,
        )
        
        response_dict = json_str_to_dict(response.text)
        # save architecture_analysis
        save_json(response_dict, "results/architecture_analysis.json")
        
        # save architecture_analysis file path
        state.target_architecture_analysis_path = "results/architecture_analysis.json"
        return state
    else:
        # load architecture_analysis
        analysis_json = load_file(state.target_architecture_analysis_path)
        # read assessment file
        assessment_json = load_file(state.target_assessment_path)
            
        prompt = ARCHITECTURE_CORRECTION_TEMPLATE.replace(
        "{docs}", target_docs
        ).replace(
            "{initial_json}", analysis_json
        ).replace(
            "{findings}", assessment_json
        )
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]
        
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=ARCHITECTURE_CORRECTION_CONFIG,
        )
        
        try:
            analysis_result = json.loads(response.text)

            # map update
            components_map.update({comp["id"]: comp for comp in analysis_result.get("components", [])})
            actors_map.update({actor["id"]: actor for actor in analysis_result.get("actors", [])})
            assets_map.update({asset["id"]: asset for asset in analysis_result.get("assets", [])})
            data_flows_map.update({flow["id"]: flow for flow in analysis_result.get("data_flows", [])})
            trust_boundaries_map.update({tb["id"]: tb for tb in analysis_result.get("trust_boundaries", [])})
            behaviors_map.update({behavior["id"]: behavior for behavior in analysis_result.get("behaviors", [])})

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
        # read initial_architecture_analysis file
        analysis_json = load_file(state.target_architecture_analysis_path)
        
        response_dict = json_str_to_dict(response.text)
        # parsing response and save to file
        save_json(response_dict, "results/architecture_analysis.json")
        
        # save result to state
        state.target_architecture_analysis_path = "results/architecture_analysis.json"
        return state
    
# assessment node
def assess_architecture(state: State) -> State:
    """architecture assessment node"""
    target_docs = load_file(state.target_docs_path)
    
    # read architecture_analysis 
    analysis_json = load_file(state.target_architecture_analysis_path)
    
    prompt = ASSESSMENT_TEMPLATE.replace("{docs}", target_docs).replace(
        "{json}", analysis_json
    )
    
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]
    
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=ASSESSMENT_CONFIG,
    )
    
    # parsing json and save to file
    response_dict = json_str_to_dict(response.text)
    save_json(response_dict, "results/assessment.json")
    
    # feedback loop count
    state.feedback_loop_count += 1
    # save assessment file path
    state.target_assessment_path = "results/assessment.json"
    return state

def analyze_threats(state: State) -> State:
    id_weight = 1
    # read target docs file
    target_docs = load_file(state.target_docs_path)
    # read architecture_correction file
    architecture_correction = load_file(state.target_architecture_analysis_path)
        
    for actor_number in range(len(actors_map)):
        cur_actor = build_llm_chunk(architecture_correction, actor_number + 1)

        prompt = THREAT_ANALYSIS_TEMPLATE.replace("{docs}", target_docs).replace("{chuck}", json.dumps(cur_actor)).replace("{json}", architecture_correction)

        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]

        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=THREAT_ANALYSIS_CONFIG,
        )
        # parsing response and save to file
        response_dict = json_str_to_dict(response.text)
        for i in response_dict["threats"]:
            i["id"] = id_weight
            id_weight += 1
            
        threats_list.append(response_dict["threats"])
        print(f"{actor_number}번 actor의 threats {len(response_dict['threats'])}건 추출 완료. 총 {id_weight}개")
    print(f"총 actor {len(threats_list)}명의 threat {id_weight}개 추출 완료")
    
    for i, actor_threat in enumerate(threats_list):
        # save actors' threats
        save_json(actor_threat, f'results/actors/threats_actor_{i+1}.json')
        print(f"Saved threats for actor {i+1}")
        
        # append to all threats list actor_threat
        all_threats.extend(actor_threat)
        
    save_json({ "threats": all_threats }, 'results/all_threats.json')
    print("Saved all threats in 'all_threats.json'")

    # save result to state
    state.target_threat_analysis_path = "results/all_threats.json"
    return state

def generate_checklist(state: State) -> State:
    # read target docs file
    with open(state.target_docs_path, "r") as f:
        target_docs = f.read()
    
    # read threat_analysis file
    with open(state.target_threat_analysis_path, "r") as f:
        threat_analysis = f.read()
        
    id_weight = 1
    checklist_items = []
    theats_list_copy = threats_list.copy()
    
    for i in range(len(threats_list)):
        context = []
        prev_threat = []
        for threat in theats_list_copy[i]:
            prev_threat.append(threat.copy())
            actor_id = threat["actor_risk"]["actor_id"]
            threat["actor_risk"]["actor_details"] = actors_map.get(actor_id, {})
            
            # Add threat target component and assets
            threat["threat_target"]["component_details"] = components_map.get(threat["threat_target"]["component_id"], {})
            threat["threat_target"]["asset_details"] = [assets_map.get(aid, {}) for aid in threat["threat_target"]["asset_ids"]]

            # Add behavior context
            behavior_id = threat["attack_surface"]["behavior_id"]
            threat["attack_surface"]["behavior_details"] = behaviors_map.get(behavior_id, {})

            # Add data flow context
            df_id = threat["attack_surface"]["data_flow_id"]
            threat["attack_surface"]["data_flow_details"] = data_flows_map.get(df_id, {})

            # Add trust boundary context
            tb_id = threat["trust_boundary_risk"]["boundary_id"]
            threat["trust_boundary_risk"]["boundary_details"] = trust_boundaries_map.get(tb_id, {})
            
            context.append(threat)
    
        prompt = CHECKLIST_TEMPLATE.replace("{docs}", target_docs).replace("{json}", threat_analysis)
        
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)],
            ),
        ]

        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=CHECKLIST_CONFIG,
        )

        # parsing response and save to file
        response_dict = json_str_to_dict(response.text)
        for checklist_item in response_dict['checklist_items']:
            checklist_item['id'] = id_weight
            id_weight = id_weight+1
            # append each checklist item extracted from the current actor
            checklist_items.append(checklist_item)
        print(i, "번째 actor의 checklist prompt end. 햔재까지 checklist : ", len(checklist_items), "개")
        
    with open("results/checklist.json", "w") as f:
        json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
    print("Saved checklist in 'results/checklist.json'")
    
    # save result to state
    state.target_checklist_path = "results/checklist.json"
    return state
        