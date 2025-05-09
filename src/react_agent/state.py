"""Define the state structures for the agent."""

from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class InputState:
    target_docs_path: str = field(default="")

@dataclass
class State(InputState):
    target_architecture_analysis_path: str = field(default="")
    target_assessment_path: str = field(default="")
    target_threat_analysis_path: str = field(default="")
    target_checklist_path: str = field(default="")
    feedback_loop_count: int = field(default=0)
