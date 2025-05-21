import asyncio
import json
from src.react_agent.graph import graph
from src.react_agent.state import InputState
from src.react_agent.variables import graph_config


def main():
    """
    Main function to run the Audit Agent graph.
    """
    initial_input_path = "dataset/berachain_docs_merged.md"
    
    # 그래프의 첫 번째 입력입니다.
    # InputState를 사용하거나, State에 직접 매핑될 수 있는 딕셔너리를 사용할 수 있습니다.
    # 여기서는 초기 입력을 딕셔너리 형태로 설정합니다.
    input_: dict | None = {"target_docs_path": initial_input_path}

    print(f"Starting Audit Agent graph with input: {input_}")

    # config에 thread_id가 포함되어 있어야 인터럽트 후 상태를 기억하고 재개할 수 있습니다.
    # from src.react_agent.variables import config 에서 가져온 config가 이를 담당합니다.
    # 예: config = {"configurable": {"thread_id": "user_session_123"}}

    while True:
        print(f"\nStarting Audit Agent graph ...")
        
        # 지정된 노드 중 하나가 완료된 후 인터럽트합니다.
        interrupt_nodes = [
            "analyze_architecture", "assess_architecture", 
            "analyze_threats", 
            "generate_checklist", "assess_checklist", 
            "code_binding", "assess_code_binding"
        ] 
        
        # stream_mode="events"로 설정하여 각 단계의 상세한 이벤트를 받습니다.
        for event in graph.stream(
            input=input_, 
            config=graph_config, 
            stream_mode="events", 
            interrupt_after=interrupt_nodes
        ):
            for key, value in event.items():
                print(f"{key} : {value}")
                
        try:
            current_graph_state_snapshot = graph.get_state(config=graph_config) 
        except Exception as e:
            print(f"Error getting graph state: {e}. Assuming graph has ended or critical error.")
            break

        print(f"\nSnapshot - Current state values: {current_graph_state_snapshot.values}")
        print(f"Snapshot - Next node(s) to execute: {current_graph_state_snapshot.next}")
        
        # 그래프가 완전히 종료되었는지 확인합니다.
        if not current_graph_state_snapshot.next:
            print("\nGraph has completed.")
            break
        else:
            # .next가 비어있지 않으면 그래프가 일시 중지된 상태입니다.
            print(f"\nGraph execution paused. Next node(s) to execute: {current_graph_state_snapshot.next}")
            
            
            user_response = input("Type 'resume' to continue, or 'quit' to exit: ")
            if user_response.lower() == 'quit':
                print("Exiting.")
                break
            elif user_response.lower() == 'resume':
                print("Resuming graph execution...")
                # 실행을 재개할 때는 input으로 None을 전달하여 저장된 상태에서 계속하도록 합니다.
                input_ = None 
    
    print("\nAudit Agent graph finished.")

if __name__ == "__main__":
    main()