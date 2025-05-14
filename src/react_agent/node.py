"""Utility & helper functions."""
import json

# state
from react_agent.state import State
# utils
from react_agent.llm_utils import (
    init_state,
    json_str_to_dict, 
    save_json, 
    load_file,
    map_update,
    generate_llm_response,
    build_llm_chunk,
    _init_db,
    _code_binding,
    _verify_checklist,
    _verify_checklist_with_code
)

# import variables
from react_agent.variables import (
    components_map,
    actors_map,
    assets_map,
    data_flows_map,
    trust_boundaries_map,
    behaviors_map,
    threats_list,
    threat_count,
    checklist_count
)

from react_agent.prompt import THREAT_ANALYSIS_TEMPLATE, CHECKLIST_TEMPLATE
from time import sleep

# architecture analysis node
def analyze_architecture(state: State) -> State:
    """architecture analysis node"""
    # not feedback loop
    if state.architecture_feedback_loop_count == 0:
        print("completed initializing state")
        state = init_state(state)
        print("first architecture analysis ...")
        state.is_initial_architecture_analysis = True
        # generate llm response
        response = generate_llm_response(state)
        # parsing response and save to file
        response_dict = json_str_to_dict(response.text)
        # save architecture_analysis
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed first architecture analysis")
        
        return {"is_initial_architecture_analysis": False}
    else:
        print("feedback loop architecture analysis ...")
        state.is_feedback_architecture_analysis = True
        # load architecture_analysis
        response = generate_llm_response(state)
        
        map_update(json.loads(response.text), state)
        
        response_dict = json_str_to_dict(response.text)
        # parsing response and save to file
        save_json(response_dict, "results/architecture_analysis.json")
        print("completed feedback loop architecture analysis")
        
        return {"is_feedback_architecture_analysis": False}
    
# assessment node
def assess_architecture(state: State) -> State:
    """architecture assessment node"""
    state.is_assessment_analysis = True
    # generate llm response
    response = generate_llm_response(state)
    
    # parsing json and save to file
    response_dict = json_str_to_dict(response.text)
    save_json(response_dict, "results/assessment.json")
    print("completed assessing architecture")
    
    return {
        "is_assessment_analysis": False, 
        "architecture_feedback_loop_count": state.architecture_feedback_loop_count+1
        }

def analyze_threats(state: State) -> State:
    print("analyzing threats ...")
    state.is_threat_analysis = True
    id_weight = 1
    
    response = generate_llm_response(state)
    # parsing response and save to file
    response_dict = json_str_to_dict(response.text)
    for i in response_dict["threats"]:
        i["id"] = id_weight
        id_weight += 1
        
    threats_list.append(response_dict["threats"])
    
    save_json(response_dict["threats"], f'results/actors/threats_actor_{state.current_actor_id+1}.json')
    print(f"Saved threats for actor {state.current_actor_id+1}")
    
    global threat_count
    threat_count += 1
    
    if threat_count == len(actors_map):
        save_json({ "threats": threats_list }, 'results/all_threats.json')
        print("Saved all threats in 'all_threats.json'")
        print("completed analyzing threats")
        print("sleep 60 seconds ... ")
        sleep(60)
        print("sleep 60 seconds ... done")
        
    return {"is_threat_analysis": False}

def generate_checklist(state: State) -> State:
    
    print("[+] generating checklist ...")
    state.is_initial_checklist_analysis = True
        
    id_weight = 1
    checklist_items = []
    theats_list_copy = threats_list.copy()
    
    context = []
    prev_threat = []
    for threat in theats_list_copy[state.current_actor_id]:
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
        
    if state.checklist_feedback_loop_count == 0:
        state.is_initial_checklist_analysis = True
        response = generate_llm_response(state)
    else:
        state.is_feedback_checklist_analysis = True
        response = generate_llm_response(state)
        
    # parsing response and save to file
    response_dict = json_str_to_dict(response.text)
    for checklist_item in response_dict['checklist_items']:
        checklist_item['id'] = id_weight
        id_weight = id_weight+1
        # append each checklist item extracted from the current actor
        checklist_items.append(checklist_item)
    print(state.current_actor_id, "번째 actor의 checklist prompt end. 햔재까지 checklist : ", len(checklist_items), "개")
    
    checklist_count += 1
    
    if checklist_count == len(actors_map):
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
        print("Saved checklist in 'results/checklist.json'")
        print("completed generating checklist")
    
    return {"is_initial_checklist_analysis": False, "is_feedback_checklist_analysis": False}

def verify_checklist(state: State) -> State:
    print("verifying checklist ...")
    state.is_verify_checklist = True
    
    _verify_checklist(state)
    
    print("completed verifying checklist")
    
    return {"is_verify_checklist": False, "checklist_feedback_loop_count": state.checklist_feedback_loop_count+1}

def init_db(state: State) -> State:
    print("initializing vector db ...")
    state.is_init_db = True
    _init_db()
    
    print("completed initializing vector db")
    
    state.is_init_db = False
    
def code_binding(state: State) -> State:
    
    # 피드백 루프를 구분하는 분기문 필요
    
    print("code binding ...")
    state.is_code_binding = True
    
    _code_binding(state)
    
    print("completed code binding")
    
    return {"is_code_binding": False}

def verify_checklist_with_code(state: State) -> State:
    state.is_verify_checklist_with_code = True
    
    _verify_checklist_with_code(state)
    
    return {
        "is_verify_checklist_with_code": False, 
        "checklist_with_code_feedback_loop_count": state.checklist_with_code_feedback_loop_count+1
        }
