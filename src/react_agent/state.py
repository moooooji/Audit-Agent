"""Define the state structures for the agent."""

from __future__ import annotations
from typing import Annotated, Any, TypedDict, Optional, List, Literal
import operator
from pydantic import BaseModel, Field   
from react_agent.config import ChecklistItem, ThreatAnalysisOutput

def parallel_handler(a, b):
    """parallel handler for state"""
    
def last_value_reducer(previous_value: Any, new_value: Any) -> Any:
    """Keeps the last value written to the field."""
    if new_value is None:
        return previous_value
    return new_value

class InputState(TypedDict):
    target_docs_path: str

class State(InputState):
    # feedback loop count
    architecture_feedback_loop_count: int
    checklist_feedback_loop_count: int
    code_binding_feedback_loop_count: int
    
    # node flag
    is_threat_analysis: Annotated[bool, last_value_reducer]
    is_initial_checklist_analysis: Annotated[bool, last_value_reducer]
    
    # node info
    current_actor_id: int

    #tmp for parallel
    tmp_threats: Annotated[list[ThreatAnalysisOutput], operator.add]
    tmp_checklist: Annotated[list[ChecklistItem], operator.add]