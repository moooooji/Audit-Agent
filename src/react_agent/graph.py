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
from react_agent.variables import (
    ARCHITECTURE_FEEDBACK_LOOP_COUNT, 
    CHECKLIST_FEEDBACK_LOOP_COUNT, 
    CHECKLIST_WITH_CODE_FEEDBACK_LOOP_COUNT,
    actors_map
    )

from langgraph.types import Send

def architecture_feedback_loop_edge(state: State):
    print(state)
    if state.architecture_feedback_loop_count < ARCHITECTURE_FEEDBACK_LOOP_COUNT:
        return "assess_architecture"
    else:
        # 피드백 루프가 끝나면 병렬 처리 시작
        return parallel_threats_processing(state)

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
    
def parallel_threats_processing(state: State):
    # update current_actor_id
    return [Send("analyze_threats", State(
        target_docs_path=state.target_docs_path,
        current_actor_id=i,
        is_threat_analysis=True,
        architecture_feedback_loop_count=state.architecture_feedback_loop_count,
        checklist_feedback_loop_count=state.checklist_feedback_loop_count,
        checklist_with_code_feedback_loop_count=state.checklist_with_code_feedback_loop_count,
        is_initial_architecture_analysis=state.is_initial_architecture_analysis,
        is_assessment_analysis=state.is_assessment_analysis,
        is_feedback_architecture_analysis=state.is_feedback_architecture_analysis,
        is_checklist_analysis=state.is_checklist_analysis,
        is_code_binding=state.is_code_binding,
        is_init_db=state.is_init_db,
        is_verify_checklist=state.is_verify_checklist,
        is_verify_checklist_with_code=state.is_verify_checklist_with_code,
        threat_prompt=state.threat_prompt,
        checklist_prompt=state.checklist_prompt
    )) for i in range(len(actors_map))]

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