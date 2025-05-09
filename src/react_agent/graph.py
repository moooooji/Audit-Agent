from langgraph.graph import StateGraph
from react_agent.state import InputState, State
from react_agent.utils import (
    analyze_architecture, 
    assess_architecture, 
    analyze_threats, 
    generate_checklist
)


def feedback_loop_edge(state: State):
    if state.feedback_loop_count < 1:
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

# define edges
builder.add_edge("__start__", "analyze_architecture")
# feedback loop count에 따라 분기
builder.add_conditional_edges("analyze_architecture", feedback_loop_edge)
builder.add_edge("assess_architecture", "analyze_architecture")
builder.add_edge("analyze_threats", "generate_checklist")
builder.add_edge("generate_checklist", "__end__")

# Compile the builder into an executable graph
graph = builder.compile(name="Audit Agent")