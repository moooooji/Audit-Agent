from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.node import (
    analyze_architecture, 
    assess_architecture, 
    analyze_threats, 
    generate_checklist,
    init_db,
    code_binding,
    verify_checklist,
    verify_checklist_with_code
)
# dataset/berachain_docs_merged.md
from react_agent.variables import ARCHITECTURE_FEEDBACK_LOOP_COUNT, CHECKLIST_FEEDBACK_LOOP_COUNT, CHECKLIST_WITH_CODE_FEEDBACK_LOOP_COUNT

def architecture_feedback_loop_edge(state: State):
    print(state)
    if state.architecture_feedback_loop_count  < ARCHITECTURE_FEEDBACK_LOOP_COUNT:
        return "assess_architecture"
    else:
        return "analyze_threats"
    
def checklist_feedback_loop_edge(state: State):
    if state.checklist_feedback_loop_count  < CHECKLIST_FEEDBACK_LOOP_COUNT:
        return "verify_checklist"
    else:
        return "code_binding"

def checklist_with_code_feedback_loop_edge(state: State):
    if state.checklist_with_code_feedback_loop_count  < CHECKLIST_WITH_CODE_FEEDBACK_LOOP_COUNT:
        return "verify_checklist_with_code"
    else:
        return "__end__"

# define a new graph
builder = StateGraph(State, input=InputState)

# define node
builder.add_node(analyze_architecture)
builder.add_node(assess_architecture)
builder.add_node(analyze_threats)
builder.add_node(generate_checklist)
builder.add_node(init_db)
builder.add_node(code_binding)
builder.add_node(verify_checklist)
builder.add_node(verify_checklist_with_code)

# define edges
builder.add_edge("__start__", "analyze_architecture")

# jump based on feedback loop count
builder.add_conditional_edges("analyze_architecture", architecture_feedback_loop_edge, ["assess_architecture", "analyze_threats"])
builder.add_edge("assess_architecture", "analyze_architecture")
# parallel edges
builder.add_edge("analyze_threats", "init_db")
builder.add_edge("analyze_threats", "generate_checklist")
builder.add_conditional_edges("generate_checklist", checklist_feedback_loop_edge, ["verify_checklist", "code_binding"])
builder.add_edge("verify_checklist", "generate_checklist")
builder.add_conditional_edges("code_binding", checklist_with_code_feedback_loop_edge, ["verify_checklist_with_code", "__end__"])
builder.add_edge("verify_checklist_with_code", "code_binding")
builder.add_edge("init_db", "__end__")

# Compile the builder into an executable graph
graph = builder.compile(name="Audit Agent")