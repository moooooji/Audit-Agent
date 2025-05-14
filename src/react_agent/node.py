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
)

# import variables
from react_agent.variables import (
    actors_map,
    threats_list,
)

threat_count = 0
checklist_count = 0

from time import sleep
from react_agent.Utils.RedisUtil import RedisUtil
from react_agent.Utils.AnalyzeSolidity import AnalyzeSolidity
# architecture analysis node
def analyze_architecture(state: State) -> State:
    """architecture analysis node"""
    # not feedback loop
    if state.architecture_feedback_loop_count == 0:
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
        threats_list.append(i)
        save_json(i, f'results/actors/threats_actor_{state.current_actor_id+1}.json')
    
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
    
    state.is_initial_checklist_analysis = True
        
    id_weight = 1
    checklist_items = []
        
    if state.checklist_feedback_loop_count == 0:
        print("initial checklist analysis ...")
        state.is_initial_checklist_analysis = True
        response = generate_llm_response(state)
        print("completed initial checklist analysis")
    else:
        print("feedback loop checklist analysis ...")
        state.is_feedback_checklist_analysis = True
        response = generate_llm_response(state)
        print("completed feedback loop checklist analysis")
        
    # parsing response and save to file
    response_dict = json_str_to_dict(response.text)
    for checklist_item in response_dict['checklist_items']:
        checklist_item['id'] = id_weight
        id_weight = id_weight+1
        # append each checklist item extracted from the current actor
        checklist_items.append(checklist_item)
    print(state.current_actor_id, "번째 actor의 checklist prompt end. 햔재까지 checklist : ", len(checklist_items), "개")
    
    global checklist_count
    checklist_count += 1
    
    if checklist_count == len(actors_map):
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
        print("Saved checklist in 'results/checklist.json'")
        print("completed generating checklist")
    
    return {"is_initial_checklist_analysis": False, "is_feedback_checklist_analysis": False}

def assess_checklist(state: State) -> State:
    print("verifying checklist ...")
    state.is_assessment_checklist = True
    
    generate_llm_response(state)
    
    print("completed verifying checklist")
    
    return {"is_assessment_checklist": False, "checklist_feedback_loop_count": state.checklist_feedback_loop_count+1}

def init_db(state: State) -> State:
    print("initializing vector db ...")
    state.is_init_db = True
    _init_db()
    
    print("completed initializing vector db")
    
    state.is_init_db = False
    
def code_binding(state: State) -> State:
    if state.checklist_with_code_feedback_loop_count == 0:
        print("initial code binding ...")
        
        with open("results/checklist.json", "r") as f:
            checklist = json.load(f)
        
        similar_functions_list = []
        for item in checklist["checklist_items"]:
            function_description = item["description"]
            similar_functions = AnalyzeSolidity.search(function_description, 3)
            similar_functions_list.append(similar_functions)
        print("[+] similar_functions_list: ", similar_functions_list)
        print("[+] similar_functions_length: ", len(similar_functions_list))
        
        function_codes = {}
        # parsing contract names and function names
        for i, similar_functions in enumerate(similar_functions_list):
            print(f"\n[+] Processing checklist item {i+1}:")
            function_codes[i] = {
                "checklist_item_id": i,
                "similar_functions": []
            }
            for doc in similar_functions:
                # Parse metadata
                contract_name = doc.metadata['contract']
                function_name = doc.metadata['function']
                function_code = RedisUtil.get_function_code(f"{contract_name}.{function_name}")
                # Store the function code with its metadata
                function_codes[i]["similar_functions"].append({
                    "contract_name": contract_name,
                    "function_name": function_name,
                    "code": function_code
                })
                print(f"[+] Added function code for {contract_name}.{function_name}")
        
        print("[+] Saving function codes to code_binding.json...")
        with open("results/code_binding.json", "w") as f:
            json.dump({ "function_codes": function_codes }, f, ensure_ascii=False, indent=2)
        state.is_initial_code_binding = True
        response = generate_llm_response(state)
        print("completed initial code binding")
    else:
        print("feedback loop code binding ...")
        state.is_feedback_code_binding = True
        response = generate_llm_response(state)
        print("completed feedback loop code binding")
    
    return {"is_initial_code_binding": False, "is_feedback_code_binding": False}

def assess_checklist_with_code(state: State) -> State:
    print("assessing checklist with code ...")
    state.is_assessment_checklist_with_code = True
    
    generate_llm_response(state)
    
    print("completed assessing checklist with code")
    
    return {
        "is_assessment_checklist_with_code": False, 
        "checklist_with_code_feedback_loop_count": state.checklist_with_code_feedback_loop_count+1
        }
