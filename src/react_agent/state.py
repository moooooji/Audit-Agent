"""Define the state structures for the agent."""

from __future__ import annotations
from typing import TypedDict, Annotated, NotRequired
from dataclasses import dataclass, field
import operator
from langgraph.prebuilt import ToolNode
    
def parallel_handler(a, b):
    """parallel handler for state"""
    
@dataclass
class InputState():
    target_docs_path: str = field(default="")

@dataclass
class State(InputState):
    # feedback loop count
    architecture_feedback_loop_count: int = field(default=0)
    checklist_feedback_loop_count: int = field(default=0)
    checklist_with_code_feedback_loop_count: int = field(default=0)
    
    # node flag
    is_initial_architecture_analysis: bool = field(default=False)
    is_assessment_analysis: bool = field(default=False)
    is_feedback_architecture_analysis: bool = field(default=False)
    is_threat_analysis: Annotated[bool, parallel_handler] = field(default=False)
    is_initial_checklist_analysis: Annotated[bool, parallel_handler] = field(default=False)
    is_feedback_checklist_analysis: Annotated[bool, parallel_handler] = field(default=False)
    is_init_db: bool = field(default=False)
    is_initial_code_binding: bool = field(default=False)
    is_feedback_code_binding: bool = field(default=False)
    is_assessment_checklist: bool = field(default=False)
    is_assessment_checklist_with_code: bool = field(default=False)
    
    # node info
    current_actor_id: int = field(default=0)