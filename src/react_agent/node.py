"""Utility & helper functions."""
import json

from react_agent.state import State
from react_agent.llm_utils import (
    json_str_to_dict, 
    save_json, 
    map_update,
    generate_llm_response,
    _init_db,
)

# import variables
from react_agent.variables import (
    actors_map,
    
)

threats_list = []
checklist_items = []

threat_count = 0
checklist_count = 0
BATCH_SIZE = 10


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
        
        # input("\n아키텍처 분석이 완료되었습니다. 계속하려면 Enter를 누르세요...")
        
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
        
        # input("\n피드백 루프 아키텍처 분석이 완료되었습니다. 계속하려면 Enter를 누르세요...")
        
        return {"is_feedback_architecture_analysis": False}
    
# assessment node
def assess_architecture(state: State) -> State:
    """architecture assessment node"""
    state.is_assessment_analysis = True
    # generate llm response
    response = generate_llm_response(state)
    
    # parsing json and save to file
    response_dict = json_str_to_dict(response.text)
    save_json(response_dict, "results/assessment_architecture.json")
    print("completed assessing architecture")
    
    # input("\n아키텍처 평가가 완료되었습니다. 계속하려면 Enter를 누르세요...")
    
    return {
        "is_assessment_analysis": False, 
        "architecture_feedback_loop_count": state.architecture_feedback_loop_count+1
        }
    
# 병렬 처리를 위한 세마포어 변수 추가
import threading
api_semaphore = threading.Semaphore(1)  # 한 번에 하나의 스레드만 API 대기 로직 실행
processed_threats_batches = 0  # 처리된 위협 배치 수 추적
processed_checklist_batches = 0  # 처리된 체크리스트 배치 수 추적

def analyze_threats(state: State) -> State:
    print("analyzing threats ...")
    state.is_threat_analysis = True
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

    response = generate_llm_response(state)
    # parsing response and save to file
    response_dict = json_str_to_dict(response.text)
    
    print(f"[+] Processing actor {state.current_actor_id+1}...")
    print(f"[+] Threats count: {len(response_dict['threats'])}")
    for threat in response_dict["threats"]:
        threats_list.append(threat)
        
        save_json(threat, f'results/actors/threats_actor_{state.current_actor_id+1}.json')
    threat_count += 1
    print(f"Saved threats for actor {state.current_actor_id+1}")
    
    if threat_count == len(actors_map):
        # for all threats, assign sequential id weights
        threat_count = 0
        
        for threat in threats_list:
            threat["id"] = id_weight
            id_weight += 1
        
        print("threats_list : ", len(threats_list))
            
        save_json({ "threats": threats_list }, 'results/all_threats.json')
        print("Saved all threats in 'all_threats.json'")
        print("completed analyzing threats")
        
        print("gemini api initializing ...")
        sleep(60)
        print("gemini api initialized")
        
        # input("\n위협 분석이 완료되었습니다. 계속하려면 Enter를 누르세요...")
    return {
            "is_threat_analysis": False,
            "threat_list_length": len(threats_list),
            "current_threat_count": id_weight-1,
            }

def generate_checklist(state: State) -> State:
    
    global checklist_count
    global processed_checklist_batches
    global checklist_items
    
    # prevent race condition
    with api_semaphore:
        # for google gemini api RPM limit
        current_batch = (checklist_count - 1) // BATCH_SIZE
        if current_batch > processed_checklist_batches:
            processed_checklist_batches = current_batch
            print("gemini api initializing for checklist batch ", current_batch, " ...")
            sleep(60)
            print("gemini api initialized for checklist batch ", current_batch)
    
    if state.checklist_feedback_loop_count == 0:
        print("initial checklist analysis ...")
        state.is_initial_checklist_analysis = True
        response = generate_llm_response(state)
        
        response_dict = json_str_to_dict(response.choices[0].message.content)
        for checklist_item in response_dict['checklist_items']:
            # append each checklist item extracted from the current actor
            checklist_items.append(checklist_item)
            
        print(state.current_threat_id, "번째 threat의 checklist prompt end. 햔재까지 checklist : ", len(checklist_items), "개")
        
        print("completed initial checklist analysis")
        
        # input("\n체크리스트 분석이 완료되었습니다. 계속하려면 Enter를 누르세요...")
    else:
        print("feedback loop checklist analysis ...")
        state.is_feedback_checklist_analysis = True
        response = generate_llm_response(state)
        
        response_dict = json_str_to_dict(response.choices[0].message.content)
        for checklist_item in response_dict['checklist_items']:
            # append each checklist item extracted from the current actor
            checklist_items.append(checklist_item)
            
        print(state.current_threat_id, "번째 threat의 checklist prompt end. 햔재까지 checklist : ", len(checklist_items), "개")
        
        print("completed feedback loop checklist analysis")
        
        # input("\n피드백 루프 체크리스트 분석이 완료되었습니다. 계속하려면 Enter를 누르세요...")
        
    checklist_count += 1
    
    if checklist_count == len(threats_list):
        
        id_weight = 1
        
        for item in checklist_items:
            item['id'] = id_weight
            id_weight = id_weight+1
        
        checklist_count = 0
        with open("results/checklist.json", "w") as f:
            json.dump({ "checklist_items": checklist_items }, f, ensure_ascii=False, indent=2)
        
        print("checklist_items : ", len(checklist_items))
        checklist_items = []
        
        print("Saved checklist in 'results/checklist.json'")
        print("completed generating checklist")
        
        print("gemini api initializing ...")
        sleep(60)
        print("gemini api initialized")
    
    return {"is_initial_checklist_analysis": False, "is_feedback_checklist_analysis": False}

def assess_checklist(state: State) -> State:
    print("verifying checklist ...")
    state.is_assessment_checklist = True
    
    response = generate_llm_response(state)
    
    response_dict = json_str_to_dict(response.choices[0].message.content)
    save_json(response_dict, "results/assessment_checklist.json")
    
    print("completed verifying checklist")
    
    return {"is_assessment_checklist": False, "checklist_feedback_loop_count": state.checklist_feedback_loop_count+1}

def init_db(state: State) -> State:
    print("initializing vector db ...")
    state.is_init_db = True
    _init_db()
    
    print("completed initializing vector db")
    
    state.is_init_db = False
    
def code_binding(state: State) -> State:
    if state.code_binding_feedback_loop_count == 0:
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

        state.is_initial_code_binding = True
        print("completed initial code binding")

    else:
        print("feedback loop code binding ...")
        state.is_feedback_code_binding = True
        print("completed feedback loop code binding")

    return {"is_initial_code_binding": False, "is_feedback_code_binding": False}


def assess_code_binding(state: State) -> State:
    print("assessing code binding ...")
    state.is_assessment_code_binding = True
    
    response = generate_llm_response(state)
    
    response_dict = json_str_to_dict(response.choices[0].message.content)
    save_json(response_dict, "results/assessment_code_binding.json")
    
    print("completed assessing code binding")
    
    initialize_state(state)
    
    return {
        "is_assessment_code_binding": False, 
        "code_binding_feedback_loop_count": state.code_binding_feedback_loop_count+1
        }

def initialize_state(state: State) -> State:
    state.architecture_feedback_loop_count = 0
    state.checklist_feedback_loop_count = 0
    state.code_binding_feedback_loop_count = 0
    
    state.is_initial_architecture_analysis = False
    state.is_feedback_architecture_analysis = False
    state.is_assessment_analysis = False
    state.is_assessment_checklist = False
    state.is_assessment_code_binding = False
    state.is_init_db = False
    state.is_initial_checklist_analysis = False
    state.is_feedback_checklist_analysis = False
    state.is_initial_code_binding = False
    state.is_feedback_code_binding = False
    state.is_threat_analysis = False
    
    
    state.current_actor_id = 0
