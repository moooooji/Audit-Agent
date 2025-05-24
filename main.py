import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

import asyncio
import json
from src.react_agent.graph import graph
from src.react_agent.state import InputState
from src.react_agent.variables import graph_config

DATASET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset')

def main():
    """
    Main function to run the Audit Agent graph.
    """
    initial_input_path = os.path.join(DATASET_DIR, 'hyperlane-monorepo_docs_merged.md')
    print(f"Current working directory: {os.getcwd()}")
    
    input_: dict | None = {"target_docs_path": initial_input_path}

    print(f"Starting Audit Agent graph with input: {input_}")
    # input("[*input*](yes/no/quit) An error occurred. Try to resume from checkpoint? (yes/no/quit): ")
    while True:
        try:
            print(f"\nStarting/Resuming Audit Agent graph with input: {input_}")
            
            # interrupt node
            interrupt_nodes = [
                "analyze_architecture", "assess_architecture", 
                "analyze_threats", 
                "generate_checklist", "assess_checklist", 
                "code_binding", "assess_code_binding"
            ] 
            
            for event in graph.stream(
                input=input_, 
                config=graph_config, 
                stream_mode="events", 
                interrupt_after=interrupt_nodes
            ):
                for key, value in event.items():
                    print(f"{key} : {value}")
                    
            current_graph_state_snapshot = graph.get_state(config=graph_config) 
            print(f"\nSnapshot - Current state values: {current_graph_state_snapshot.values}")
            print(f"Snapshot - Next node(s) to execute: {current_graph_state_snapshot.next}")
            
            if not current_graph_state_snapshot.next:
                print("\nGraph has completed.")
                break
            else:
                # print(f"\nGraph execution paused. Next node(s) to execute: {current_graph_state_snapshot.next}")
                
                # if current_graph_state_snapshot.next == "analyze_threats":
                #     user_response = input("output: architecture_analysis.json [*input*](resume/quit) Type 'resume' to continue, or 'quit' to exit: ").lower()
                    
                # elif current_graph_state_snapshot.next == "generate_checklist":
                #     user_response = input("output: all_threats.json [*input*](resume/quit) Type 'resume' to continue, or 'quit' to exit: ").lower()
                    
                # elif current_graph_state_snapshot.next == "code_binding":
                #     user_response = input("output: checklist.json [*input*](resume/quit) Type 'resume' to continue, or 'quit' to exit: ").lower()
                # else:    
                #     user_response = input("[*input*](resume/quit) Type 'resume' to continue, or 'quit' to exit: ").lower()
                    
                # if user_response == 'quit':
                #     print("Exiting.")
                #     break
                # elif user_response == 'resume':
                #     print("Resuming graph execution...")
                #     input_ = None 
                # else:
                #     print("Invalid input. Defaulting to resume.")
                input_ = None


        except Exception as e:
            print(f"\n--- ERROR DURING GRAPH EXECUTION ---")
            print(f"Error details: {e}")
            import traceback
            traceback.print_exc()

            while True:
                user_response_on_error = input("[*input*](yes/no/quit) An error occurred. Try to resume from checkpoint? (yes/no/quit): ").lower()
                if user_response_on_error == 'yes':
                    print("Attempting to resume from the last checkpoint...")
                    input_ = None
                    break
                elif user_response_on_error in ['no', 'quit']:
                    print("Exiting due to error.")
                    print("\nAudit Agent graph finished.")
                    return
                else:
                    print("Invalid input. Please type 'yes', 'no', or 'quit'.")
    
    print("\nAudit Agent graph finished.")

if __name__ == "__main__":
    main()