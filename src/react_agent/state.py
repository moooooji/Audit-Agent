"""Define the state structures for the agent."""

from __future__ import annotations
from typing import TypedDict, Annotated, NotRequired
from dataclasses import dataclass, field
import operator
    
@dataclass
class InputState():
    target_docs_path: str = field(default="")

@dataclass
class State(InputState):
    architecture_feedback_loop_count: int = field(default=0)
    checklist_feedback_loop_count: int = field(default=0)
    checklist_with_code_feedback_loop_count: int = field(default=0)
    is_initial_architecture_analysis: bool = field(default=False)
    is_assessment_analysis: bool = field(default=False)
    is_feedback_architecture_analysis: bool = field(default=False)
    is_threat_analysis: bool = field(default=False)
    is_checklist_analysis: bool = field(default=False)
    is_init_db: bool = field(default=False)
    is_code_binding: bool = field(default=False)
    is_verify_checklist: bool = field(default=False)
    is_verify_checklist_with_code: bool = field(default=False)
    threat_prompt: str = field(default="")
    checklist_prompt: str = field(default="")
    