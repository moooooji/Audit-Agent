"""Define the state structures for the agent."""

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class InputState:
    target_docs_path: str = field(default="")

@dataclass
class State(InputState):
    feedback_loop_count: int = field(default=0)
    initial_architecture_analysis: bool = field(default=False)
    assessment_analysis: bool = field(default=False)
    feedback_architecture_analysis: bool = field(default=False)
    threat_analysis: bool = field(default=False)
    checklist_analysis: bool = field(default=False)
    threat_prompt: str = field(default="")
    checklist_prompt: str = field(default="")
