"""Define the state structures for the agent."""

from __future__ import annotations
from typing import Annotated, Any, TypedDict
import operator


    
def parallel_handler(a, b):
    """parallel handler for state"""
    
def last_value_reducer(previous_value: Any, new_value: Any) -> Any:
    """Keeps the last value written to the field."""
    if new_value is None:
        return previous_value
    return new_value

def previous_value_reducer(previous_value: Any, new_value: Any) -> Any:
    """Keeps the last value written to the field."""
    return previous_value
    


from pydantic import BaseModel, Field   
class ChecklistItem(BaseModel): 
        id: int = Field(description="Unique ID for the check item")
        title: str = Field(description="Short, clear, and actionable title")
        description: str = Field(description="Explanation of what needs to be checked and why")
        linked_threat_id: int = Field(description="Threat ID this check is associated with")
        category: str = Field(description="Category of the check")
        check_type: str = Field(description="Type of the check")
        target_entity: int = Field(description="ID of the component or asset being verified")
        target_type: str = Field(description="Type of the target entity")
        security_property: str = Field(description="Security property being verified")
        priority: str = Field(description="Priority of the check")
        assumption_ref: str = Field(description="Assumption that motivates this check")
        mitigation_ref: str = Field(description="Mitigation action related to this check")
        evidence_required: str = Field(description="Evidence needed to prove the check")
        automatable: bool = Field(description="Whether this check can be automated")
        status: str = Field(description="Status of the check")
        need_code_binding: bool = Field(description="Whether this check needs smart contract code binding")
        last_checked: str = Field(description="Timestamp of last validation")
        owner: str = Field(description="Team or person responsible")

class Checklist(BaseModel):
    checklist_items: list[ChecklistItem]
    
class InputState(TypedDict):
    target_docs_path: str

class State(InputState):
    # feedback loop count
    architecture_feedback_loop_count: int
    checklist_feedback_loop_count: Annotated[int, parallel_handler]
    code_binding_feedback_loop_count: int
    
    # node flag
    is_initial_architecture_analysis: bool
    is_assessment_analysis: bool
    is_feedback_architecture_analysis: bool
    is_threat_analysis: Annotated[bool, parallel_handler]
    is_initial_checklist_analysis: Annotated[bool, last_value_reducer]
    is_feedback_checklist_analysis: Annotated[bool, parallel_handler]
    is_init_db: bool
    is_initial_code_binding: bool
    is_feedback_code_binding: bool
    is_assessment_checklist: bool
    is_assessment_code_binding: bool
    threat_list_length: Annotated[int, last_value_reducer]
    current_threat_count: Annotated[int, last_value_reducer]
    
    # node info
    current_actor_id: int
    current_threat_id: int

    #tmp for parallel
    tmp_checklist: Annotated[list[ChecklistItem], operator.add]