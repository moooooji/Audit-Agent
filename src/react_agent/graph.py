from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.node import (
    analyze_architecture, 
    assess_architecture, 
    analyze_threats, 
    map_get_assessment_checklist,
    generate_parallel_checklist,
    route_checklist,
    init_db,
    code_binding,
    assess_checklist,
    assess_code_binding
)

# dataset/hyperlane-monorepo_docs_merged.md
from react_agent.variables import (
    ARCHITECTURE_FEEDBACK_LOOP_COUNT, 
    CHECKLIST_FEEDBACK_LOOP_COUNT, 
    CODE_BINDING_FEEDBACK_LOOP_COUNT
    )

import react_agent.variables
react_agent.variables.actors_map
react_agent.variables.threats_list

from langgraph.types import Send
from langgraph.checkpoint.memory import MemorySaver

def architecture_feedback_loop_edge(state: State):
    if state["architecture_feedback_loop_count"] < ARCHITECTURE_FEEDBACK_LOOP_COUNT:
        return "assess_architecture"
    else:
        # parallel processing
        return parallel_threats_processing(state)

def checklist_feedback_loop_edge(state: State):
    if state["checklist_feedback_loop_count"]  < CHECKLIST_FEEDBACK_LOOP_COUNT:
        return "assess_checklist"
    else:
        return "code_binding"

def checklist_with_code_feedback_loop_edge(state: State):
    if state["code_binding_feedback_loop_count"]  < CODE_BINDING_FEEDBACK_LOOP_COUNT:
        return "assess_code_binding"
    else:
        return "__end__"
    
def parallel_threats_processing(state: State):
    
    return [Send("analyze_threats", State(
        target_docs_path=state["target_docs_path"],
        current_actor_id=i,
        is_threat_analysis=state["is_threat_analysis"],
        architecture_feedback_loop_count=state["architecture_feedback_loop_count"],
        checklist_feedback_loop_count=state["checklist_feedback_loop_count"],
    )) for i in range(len(react_agent.variables.actors_map))]
    
# define a new graph
builder = StateGraph(State, input=InputState)

# define node
builder.add_node(analyze_architecture)
builder.add_node(assess_architecture)
builder.add_node(analyze_threats, defer=True)
# builder.add_node(init_db)
builder.add_node(code_binding)
builder.add_node(assess_checklist)
builder.add_node(assess_code_binding)
builder.add_node(generate_parallel_checklist)
builder.add_node(route_checklist)

# define edges
builder.add_edge("__start__", "analyze_architecture")

# jump based on feedback loop count
builder.add_conditional_edges("analyze_architecture", architecture_feedback_loop_edge, ["assess_architecture", "analyze_threats"])
builder.add_edge("assess_architecture", "analyze_architecture")

# parallel edges
# builder.add_edge("analyze_threats", "init_db")


builder.add_edge("analyze_threats", "route_checklist")
builder.add_edge("generate_parallel_checklist", "route_checklist")
builder.add_edge("assess_checklist", "code_binding")

builder.add_conditional_edges(
    "route_checklist",
    map_get_assessment_checklist,
    [
        "generate_parallel_checklist",
        "assess_checklist"
    ]
)

builder.add_conditional_edges("code_binding", checklist_with_code_feedback_loop_edge, ["assess_code_binding", "__end__"])
builder.add_edge("assess_code_binding", "code_binding")
# builder.add_edge("init_db", "__end__")

# # set memory
# memory = MemorySaver()

# # Compile the builder into an executable graph
# graph = builder.compile(name="Audit Agent", checkpointer=memory)

graph = builder.compile(name="Audit Agent")