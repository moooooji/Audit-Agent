from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.node import (
    analyze_architecture, 
    assess_architecture,
    route_threats,
    generate_batch_threats,
    generate_parallel_threats, 
    map_get_assessment_checklist,
    generate_parallel_checklist,
    route_checklist,
    init_db,
    code_binding,
    assess_checklist,
    assess_code_binding,
    feedback_loop_checklist
)

# dataset/hyperlane-monorepo_docs_merged.md
from react_agent.variables import (
    ARCHITECTURE_FEEDBACK_LOOP_COUNT, 
    CHECKLIST_FEEDBACK_LOOP_COUNT, 
    CODE_BINDING_FEEDBACK_LOOP_COUNT
    )

import react_agent.variables
react_agent.variables.actors_map

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
        return "feedback_loop_checklist"
    else:
        return "code_binding"

def checklist_with_code_feedback_loop_edge(state: State):
    if state["code_binding_feedback_loop_count"]  < CODE_BINDING_FEEDBACK_LOOP_COUNT:
        return "assess_code_binding"
    else:
        return "__end__"
    
def parallel_threats_processing(state: State):
    
    return [Send("generate_parallel_threats", State(
        target_docs_path=state["target_docs_path"],
        current_actor_id=i,
    )) for i in range(len(react_agent.variables.actors_map))]
    
# define a new graph
builder = StateGraph(State, input=InputState)

# define node
builder.add_node(analyze_architecture)
builder.add_node(assess_architecture)
builder.add_node(route_threats)
builder.add_node(generate_parallel_threats)
builder.add_node(init_db)
builder.add_node(code_binding)
builder.add_node(assess_checklist)
builder.add_node(assess_code_binding)
builder.add_node(generate_parallel_checklist)
builder.add_node(route_checklist)
builder.add_node(feedback_loop_checklist)

# define edges
builder.add_edge("__start__", "analyze_architecture")

# jump based on feedback loop count
builder.add_conditional_edges("analyze_architecture", architecture_feedback_loop_edge, ["assess_architecture", "route_threats"])
builder.add_edge("assess_architecture", "analyze_architecture")

# parallel edges
builder.add_conditional_edges("route_threats", generate_batch_threats, ["generate_parallel_threats", "route_checklist"])
builder.add_edge("route_threats", "init_db")
builder.add_edge("generate_parallel_threats", "route_threats")


builder.add_edge("generate_parallel_checklist", "route_checklist")
builder.add_conditional_edges("assess_checklist", checklist_feedback_loop_edge, ["feedback_loop_checklist", "code_binding"])
builder.add_edge("feedback_loop_checklist", "assess_checklist")

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
builder.add_edge("init_db", "__end__")

# # set memory
# memory = MemorySaver()

# # Compile the builder into an executable graph
# graph = builder.compile(name="Audit Agent", checkpointer=memory)

graph = builder.compile(name="Audit Agent")