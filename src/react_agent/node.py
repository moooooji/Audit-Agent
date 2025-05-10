"""Utility & helper functions."""
import json

# state
from react_agent.state import State
# utils
from react_agent.utils import (
    json_str_to_dict, 
    save_json, 
    load_file,
    map_update,
    generate_llm_response,
    build_llm_chunk,
)

from react_agent.variables import (
    components_map,
    actors_map,
    assets_map,
    data_flows_map,
    trust_boundaries_map,
    behaviors_map,
    all_threats,
    threats_list
)

from react_agent.prompt import THREAT_ANALYSIS_TEMPLATE, CHECKLIST_TEMPLATE

# dataset/berachain_docs_merged.md

# architecture analysis node
def analyze_architecture(state: State) -> State:
    """architecture analysis node"""
    # not feedback loop
    if state.feedback_loop_count == 0:
        print("first architecture analysis ...")
        state.initial_architecture_analysis = True
        # generate llm response
        response = generate_llm_response(state)
        # parsing response and save to file
        response_dict = json_str_to_dict(response.text)
        # save architecture_analysis
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed first architecture analysis")
        
        return state
    else:
        print("feedback loop architecture analysis ...")
        state.feedback_architecture_analysis = True
        # load architecture_analysis
        response = generate_llm_response(state)
        
        map_update(json.loads(response.text), state)
        
        response_dict = json_str_to_dict(response.text)
        # parsing response and save to file
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed feedback loop architecture analysis")
        return state
    
# assessment node
def assess_architecture(state: State) -> State:
    """architecture assessment node"""
    state.assessment_analysis = True
    print("assessing architecture ...")
    
    # generate llm response
    response = generate_llm_response(state)
    
    # parsing json and save to file
    response_dict = json_str_to_dict(response.text)
    save_json(response_dict, "results/assessment.json")
    print("completed assessing architecture")
    
    # feedback loop count
    state.feedback_loop_count += 1
    
    return state

def analyze_threats(state: State) -> State:
    print("analyzing threats ...")
    state.threat_analysis = True
    id_weight = 1
    # read target docs file
    target_docs = load_file(state.target_docs_path)
    # read architecture_correction file
    architecture_correction = load_file("results/architecture_analysis.json")
        
    for actor_number in range(len(actors_map)):
        cur_actor = build_llm_chunk(architecture_correction, actor_number + 1)

        prompt = THREAT_ANALYSIS_TEMPLATE.replace("{docs}", target_docs).replace("{chuck}", json.dumps(cur_actor)).replace("{json}", architecture_correction)
        state.threat_prompt = prompt

        response = generate_llm_response(state)
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
    print("completed analyzing threats")
    return state

def generate_checklist(state: State) -> State:
    print("generating checklist ...")
    state.checklist_analysis = True
    # read target docs file
    with open(state.target_docs_path, "r") as f:
        target_docs = f.read()
    
    # read threat_analysis file
    with open("results/all_threats.json", "r") as f:
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
        state.checklist_prompt = prompt
        
        response = generate_llm_response(state)

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
    print("completed generating checklist")
    
    return state
        