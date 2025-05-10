import json
import re

from google.genai import types

from react_agent.state import State

from react_agent.prompt import (
    ARCHITECTURE_ANALYSIS_TEMPLATE, ARCHITECTURE_RESPONSE_CONFIG, 
    ASSESSMENT_TEMPLATE, ASSESSMENT_CONFIG, 
    ARCHITECTURE_CORRECTION_TEMPLATE, ARCHITECTURE_CORRECTION_CONFIG, 
    THREAT_ANALYSIS_CONFIG,
    CHECKLIST_CONFIG
)

from react_agent.variables import (
    architecture_analysis,
    components_map,
    actors_map,
    assets_map,
    data_flows_map,
    trust_boundaries_map,
    behaviors_map,
    model,
    client,
    FEEDBACK_LOOP_COUNT
)

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

def generate_llm_response(state: State) -> str:
    """generate llm response"""
    
    # first architecture analysis node
    if state.initial_architecture_analysis and not state.assessment_analysis:
        
        target_docs = load_file(state.target_docs_path)
        
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
        return response
    
    elif state.assessment_analysis and state.feedback_architecture_analysis < FEEDBACK_LOOP_COUNT:
        
        target_docs = load_file(state.target_docs_path)
    
        # read architecture_analysis 
        analysis_json = load_file("results/architecture_analysis.json")
        
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
        return response
    
    # feedback loop architecture analysis node
    elif state.feedback_architecture_analysis and not state.threat_analysis:
        
        target_docs = load_file(state.target_docs_path)
        analysis_json = load_file("results/architecture_analysis.json")
        # read assessment file
        assessment_json = load_file("results/assessment.json")
            
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
        return response
    
    # threat analysis node
    elif state.threat_analysis and not state.checklist_analysis:
        
        prompt = state.threat_prompt
        
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
        return response
    
    elif state.checklist_analysis:
        
        prompt = state.checklist_prompt
        
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