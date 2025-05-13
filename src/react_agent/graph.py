from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.node import (
    analyze_architecture, 
    assess_architecture, 
    analyze_threats, 
    generate_checklist,
    init_db,
    code_binding
)
# dataset/berachain_docs_merged.md
from react_agent.variables import FEEDBACK_LOOP_COUNT

def feedback_loop_edge(state: State):
    print(state)
    if state.feedback_loop_count  < FEEDBACK_LOOP_COUNT:
        return "assess_architecture"
    else:
        return "analyze_threats"

# define a new graph
builder = StateGraph(State, input=InputState)

# define node
builder.add_node(analyze_architecture)
builder.add_node(assess_architecture)
builder.add_node(analyze_threats)
builder.add_node(generate_checklist)
builder.add_node(init_db)
builder.add_node(code_binding)

# define edges
builder.add_edge("__start__", "analyze_architecture")

# jump based on feedback loop count
builder.add_conditional_edges("analyze_architecture", feedback_loop_edge, ["assess_architecture", "analyze_threats"])
builder.add_edge("assess_architecture", "analyze_architecture")
# parallel edges
builder.add_edge("analyze_threats", "init_db")
builder.add_edge("init_db", "__end__")
builder.add_edge("analyze_threats", "generate_checklist")
builder.add_edge("generate_checklist", "code_binding")
builder.add_edge("code_binding", "__end__")

# Compile the builder into an executable graph
graph = builder.compile(name="Audit Agent")