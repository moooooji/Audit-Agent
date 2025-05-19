import asyncio
import json
from src.react_agent.graph import graph
from src.react_agent.state import InputState

def main():
    """
    Main function to run the Audit Agent graph.
    """
    initial_input_path = "dataset/berachain_docs_merged.md"
    
    initial_input = InputState(target_docs_path=initial_input_path)

    print(f"Invoking Audit Agent graph with input: {{'target_docs_path': '{initial_input_path}'}}")

    try:
        # Invoke the graph asynchronously
        graph.invoke(initial_input)


    except Exception as e:
        print(f"An error occurred during graph execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()