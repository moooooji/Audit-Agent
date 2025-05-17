from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.node import (
    analyze_architecture, 
    assess_architecture, 
    analyze_threats, 
    generate_checklist,
    init_db,
    code_binding,
    assess_checklist,
    assess_code_binding
)

threat_count = 0
# dataset/berachain_docs_merged.md
from react_agent.variables import (
    ARCHITECTURE_FEEDBACK_LOOP_COUNT, 
    CHECKLIST_FEEDBACK_LOOP_COUNT, 
    CODE_BINDING_FEEDBACK_LOOP_COUNT,
    actors_map,
    )

from langgraph.types import Send

def architecture_feedback_loop_edge(state: State):
    if state.architecture_feedback_loop_count < ARCHITECTURE_FEEDBACK_LOOP_COUNT:
        return "assess_architecture"
    else:
        # parallel processing
        return parallel_threats_processing(state)

def checklist_feedback_loop_edge(state: State):
    if state.checklist_feedback_loop_count  < CHECKLIST_FEEDBACK_LOOP_COUNT:
        return "assess_checklist"
    else:
        return "code_binding"

def checklist_with_code_feedback_loop_edge(state: State):
    if state.code_binding_feedback_loop_count  < CODE_BINDING_FEEDBACK_LOOP_COUNT:
        return "assess_code_binding"
    else:
        return "__end__"
    
def parallel_threats_processing(state: State):
    
    return [Send("analyze_threats", State(
        target_docs_path=state.target_docs_path,
        current_actor_id=i,
        is_threat_analysis=state.is_threat_analysis,
        architecture_feedback_loop_count=state.architecture_feedback_loop_count,
        checklist_feedback_loop_count=state.checklist_feedback_loop_count,
        code_binding_feedback_loop_count=state.code_binding_feedback_loop_count,
        is_initial_architecture_analysis=state.is_initial_architecture_analysis,
        is_assessment_analysis=state.is_assessment_analysis,
        is_feedback_architecture_analysis=state.is_feedback_architecture_analysis,
        is_initial_checklist_analysis=state.is_initial_checklist_analysis,
        is_feedback_checklist_analysis=state.is_feedback_checklist_analysis,
        is_initial_code_binding=state.is_initial_code_binding,
        is_feedback_code_binding=state.is_feedback_code_binding,
        is_init_db=state.is_init_db,
        is_assessment_checklist=state.is_assessment_checklist,
        is_assessment_code_binding=state.is_assessment_code_binding,
        threat_list_length=state.threat_list_length,
        current_threat_count=state.current_threat_count,
        checklist_list_length=state.checklist_list_length,
    )) for i in range(len(actors_map))]
    
def parallel_checklist_processing(state: State):
    
    print("state.current_threat_count : ", state.current_threat_count)
    print("threats_list : ", state.threat_list_length)
    
    if state.current_threat_count == state.threat_list_length:
        
        threat_count = 0
        return [Send("generate_checklist", State(
            target_docs_path=state.target_docs_path,
            current_actor_id=i,
            is_threat_analysis=state.is_threat_analysis,
            architecture_feedback_loop_count=state.architecture_feedback_loop_count,
            checklist_feedback_loop_count=state.checklist_feedback_loop_count,
            code_binding_feedback_loop_count=state.code_binding_feedback_loop_count,
            is_initial_architecture_analysis=state.is_initial_architecture_analysis,
            is_assessment_analysis=state.is_assessment_analysis,
            is_feedback_architecture_analysis=state.is_feedback_architecture_analysis,
            is_initial_checklist_analysis=state.is_initial_checklist_analysis,
            is_feedback_checklist_analysis=state.is_feedback_checklist_analysis,
            is_initial_code_binding=state.is_initial_code_binding,
            is_feedback_code_binding=state.is_feedback_code_binding,
            is_init_db=state.is_init_db,
            is_assessment_checklist=state.is_assessment_checklist,
            is_assessment_code_binding=state.is_assessment_code_binding,
            threat_list_length=state.threat_list_length,
            current_threat_count=state.current_threat_count,
            checklist_list_length=state.checklist_list_length,
        )) for i in range(state.threat_list_length)]
    else:
        print("state.current_threat_count : ", state.current_threat_count)
        return "__end__"

def parallel_feedback_checklist_processing(state: State):
    return [Send("generate_checklist", State(
        target_docs_path=state.target_docs_path,
        current_actor_id=i,
        is_threat_analysis=state.is_threat_analysis,
        architecture_feedback_loop_count=state.architecture_feedback_loop_count,
        checklist_feedback_loop_count=state.checklist_feedback_loop_count,
        code_binding_feedback_loop_count=state.code_binding_feedback_loop_count,
        is_initial_architecture_analysis=state.is_initial_architecture_analysis,
        is_assessment_analysis=state.is_assessment_analysis,
        is_feedback_architecture_analysis=state.is_feedback_architecture_analysis,
        is_initial_checklist_analysis=state.is_initial_checklist_analysis,
        is_feedback_checklist_analysis=state.is_feedback_checklist_analysis,
        is_initial_code_binding=state.is_initial_code_binding,
        is_feedback_code_binding=state.is_feedback_code_binding,
        is_init_db=state.is_init_db,
        is_assessment_checklist=state.is_assessment_checklist,
        is_assessment_code_binding=state.is_assessment_code_binding,
        threat_list_length=state.threat_list_length,
        current_threat_count=state.current_threat_count,
        checklist_list_length=state.checklist_list_length,
    )) for i in range(state.checklist_list_length)]

# define a new graph
builder = StateGraph(State, input=InputState)

# define node
builder.add_node(analyze_architecture)
builder.add_node(assess_architecture)
builder.add_node(analyze_threats)
builder.add_node(generate_checklist)
builder.add_node(init_db)
builder.add_node(code_binding)
# builder.add_node(assess_checklist)
builder.add_node(assess_code_binding)

# define edges
builder.add_edge("__start__", "analyze_architecture")

# jump based on feedback loop count
builder.add_conditional_edges("analyze_architecture", architecture_feedback_loop_edge, ["assess_architecture", "analyze_threats"])
builder.add_edge("assess_architecture", "analyze_architecture")

# parallel edges
builder.add_edge("analyze_threats", "init_db")

builder.add_conditional_edges("analyze_threats", parallel_checklist_processing, ["generate_checklist", "__end__"])
builder.add_edge("generate_checklist", "code_binding")
# builder.add_conditional_edges("assess_checklist", parallel_feedback_checklist_processing, ["generate_checklist", "__end__"])
builder.add_conditional_edges("code_binding", checklist_with_code_feedback_loop_edge, ["assess_code_binding", "__end__"])
builder.add_edge("assess_code_binding", "code_binding")
builder.add_edge("init_db", "__end__")

# Compile the builder into an executable graph
graph = builder.compile(name="Audit Agent")