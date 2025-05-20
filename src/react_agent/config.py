from google.generativeai import types as genai_types # google.generativeai.types에 대한 별칭 사용
from google import genai # genai.types.Schema 접근을 위해 유지
# from openai import OpenAI # 현재 코드에서는 사용되지 않으므로 주석 처리 또는 제거 가능
from pydantic import BaseModel, Field # Field는 ChecklistItem에서 사용될 수 있으므로 유지
from enum import Enum # ChecklistItem의 Enum들을 위해 추가
from typing import Optional, List, Dict, Any # Dict, Any 추가
from datetime import datetime # ChecklistItem에서 사용

# ---------------------------------------------------------------------------
# ENUM Values (Smart Contract Audit Specific)
# ---------------------------------------------------------------------------
SMART_CONTRACT_ACTOR_TYPES_EN = [
    "EOA (Externally Owned Account)",
    "Smart Contract",
    "Oracle",
    "DAO Participant/Token Holder",
    "Privileged Role (e.g., Owner, Admin, Minter)",
    "Off-chain Service/Bot"
]

# ---------------------------------------------------------------------------
# ARCHITECTURE_RESPONSE_CONFIG (딕셔너리 형태로 변경)
# ---------------------------------------------------------------------------
ARCHITECTURE_RESPONSE_CONFIG: Dict[str, Any] = {
    "temperature": 0,
    "response_mime_type": "application/json", # 이 필드는 generate_content 호출 시점에 사용
    "response_schema": genai.types.Schema( # genai.types.Schema는 그대로 사용
        type=genai.types.Type.OBJECT,
        description="Describes the overall architecture of the Web3 system or smart contract(s) under audit, based on the provided documentation (e.g., whitepaper).",
        required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
        properties={
            "actors": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Entities (users, contracts, or external systems) that interact with or within the smart contract system.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "name", "type", "capabilities"],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Unique identifier for the actor.",
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Name of the actor.",
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=SMART_CONTRACT_ACTOR_TYPES_EN, # 스마트 컨트랙트용 Enum
                            description="Type of the actor.",
                        ),
                        "description": genai.types.Schema( # 이 필드는 원래 있었음
                            type=genai.types.Type.STRING,
                            description="Brief explanation of the actor's role.",
                        ),
                        "capabilities": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            description="List of actor's capabilities.",
                            items=genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="A specific capability.",
                            ),
                        ),
                    },
                ),
            ),
            "assets": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Valuable resources managed by the system.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "name", "type", "sensitivity"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Asset ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Asset name."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Asset description."),
                        "type": genai.types.Schema(type=genai.types.Type.STRING, description="Asset type (e.g., Token, Data)."),
                        "sensitivity": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Sensitivity level of the asset.",
                        ),
                    },
                ),
            ),
            "components": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Logical or functional units of the system (e.g., smart contracts).",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "name", "assets_managed"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Component ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Component name."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Component description."),
                        "trust_level": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Assumed trust level of the component.",
                        ),
                        "assets_managed": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            description="List of asset IDs managed by this component.",
                            items=genai.types.Schema(type=genai.types.Type.INTEGER, description="ID of a managed asset."),
                        ),
                    },
                ),
            ),
            "data_flows": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Interactions or data exchanges between actors and/or components.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "source_id", "destination_id", "data", "security_properties"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Data flow ID."),
                        "source_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="ID of the source actor or component."),
                        "destination_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="ID of the destination actor or component."),
                        "data": genai.types.Schema(type=genai.types.Type.STRING, description="Description of the data transferred."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Purpose of the data flow."),
                        "security_properties": genai.types.Schema(
                            type=genai.types.Type.OBJECT,
                            description="Security requirements of the data flow.",
                            required=["confidentiality_required", "integrity_required", "availability_required"],
                            properties={
                                "confidentiality_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Confidentiality required."),
                                "integrity_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Integrity required."),
                                "availability_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Availability required."),
                            },
                        ),
                    },
                ),
            ),
            "trust_boundaries": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Interfaces where the level of trust changes.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "name", "between_ids", "validation_required"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Trust boundary ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Trust boundary name."),
                        "between_ids": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            description="IDs of entities this boundary separates.",
                            items=genai.types.Schema(type=genai.types.Type.INTEGER, description="ID of an entity."),
                        ),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Trust boundary explanation."),
                        "validation_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Validation required when crossing."),
                    },
                ),
            ),
            "behaviors": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Specific actions or operations within the system.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "name", "initiator_type", "initiator_id", "target_id", "action"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Behavior ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Behavior name."),
                        "initiator_type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["Actor", "Component"],
                            description="Type of initiator.",
                        ),
                        "initiator_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Initiator ID."),
                        "target_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Target component ID."),
                        "action": genai.types.Schema(type=genai.types.Type.STRING, description="Action performed."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Behavior purpose."),
                        "risk_level": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Inherent risk level.",
                        ),
                    },
                ),
            ),
        },
    )
}

# ---------------------------------------------------------------------------
# ARCHITECTURE_ASSESSMENT_CONFIG (딕셔너리 형태로 변경)
# ---------------------------------------------------------------------------
ARCHITECTURE_ASSESSMENT_CONFIG: Dict[str, Any] = {
    "temperature": 0,
    "response_mime_type": "application/json",
    "response_schema": genai.types.Schema(
        type=genai.types.Type.OBJECT,
        description="Assessment of the extracted architecture.",
        required=["evaluation_summary", "findings"],
        properties={
            "evaluation_summary": genai.types.Schema(
                type=genai.types.Type.OBJECT,
                description="High-level summary of the assessment.",
                required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
                properties={
                    "actors": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for actors."),
                    "assets": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for assets."),
                    "components": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for components."),
                    "data_flows": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for data flows."),
                    "trust_boundaries": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for trust boundaries."),
                    "behaviors": genai.types.Schema(type=genai.types.Type.STRING, description="Summary for behaviors."),
                },
            ),
            "findings": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Specific issues identified.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["category", "type", "id", "description"],
                    properties={
                        "category": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
                            description="Architectural category of the finding.",
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["missing", "hallucinated", "invalid_reference", "schema_error", "inconsistent", "ambiguous_description", "potential_concern"], # 확장된 Enum
                            description="Type of issue identified.",
                        ),
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            nullable=True, # Boolean으로 수정
                            description="ID of the related element, if applicable.",
                        ),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Detailed description of the finding."),
                    },
                ),
            ),
        },
    )
}

# ---------------------------------------------------------------------------
# ARCHITECTURE_CORRECTION_CONFIG (딕셔너리 형태로 변경)
# ---------------------------------------------------------------------------
ARCHITECTURE_CORRECTION_CONFIG: Dict[str, Any] = {
    "temperature": 0,
    "response_mime_type": "application/json",
    "response_schema": genai.types.Schema( # ARCHITECTURE_RESPONSE_SCHEMA와 구조 동일
        type=genai.types.Type.OBJECT,
        description="Corrected or refined version of the system architecture.",
        required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
        properties={ # 상세 설명은 ARCHITECTURE_RESPONSE_SCHEMA 참고, 여기서는 간략히
            "actors": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected actors.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "type", "capabilities"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Actor ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Actor name."),
                        "type": genai.types.Schema(type=genai.types.Type.STRING, enum=SMART_CONTRACT_ACTOR_TYPES_EN, description="Actor type."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Actor description."),
                        "capabilities": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.STRING), description="Actor capabilities."),
                    },),),
            "assets": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected assets.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "type", "sensitivity"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Asset ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Asset name."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Asset description."),
                        "type": genai.types.Schema(type=genai.types.Type.STRING, description="Asset type."),
                        "sensitivity": genai.types.Schema(type=genai.types.Type.STRING, enum=["High", "Medium", "Low"], description="Asset sensitivity."),
                    },),),
            "components": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected components.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "assets_managed"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Component ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Component name."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Component description."),
                        "trust_level": genai.types.Schema(type=genai.types.Type.STRING, enum=["High", "Medium", "Low"], description="Component trust level."),
                        "assets_managed": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.INTEGER), description="Assets managed."),
                    },),),
            "data_flows": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected data flows.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "source_id", "destination_id", "data", "security_properties"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Data flow ID."),
                        "source_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Source ID."),
                        "destination_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Destination ID."),
                        "data": genai.types.Schema(type=genai.types.Type.STRING, description="Data transferred."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Data flow purpose."),
                        "security_properties": genai.types.Schema(
                            type=genai.types.Type.OBJECT, required=["confidentiality_required", "integrity_required", "availability_required"],
                            properties={
                                "confidentiality_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Confidentiality."),
                                "integrity_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Integrity."),
                                "availability_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Availability."),
                            },),
                    },),),
            "trust_boundaries": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected trust boundaries.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "between_ids", "validation_required"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Boundary ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Boundary name."),
                        "between_ids": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.INTEGER), description="Entity IDs."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Boundary description."),
                        "validation_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Validation required."),
                    },),),
            "behaviors": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected behaviors.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "initiator_type", "initiator_id", "target_id", "action"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Behavior ID."),
                        "name": genai.types.Schema(type=genai.types.Type.STRING, description="Behavior name."),
                        "initiator_type": genai.types.Schema(type=genai.types.Type.STRING, enum=["Actor", "Component"], description="Initiator type."),
                        "initiator_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Initiator ID."),
                        "target_id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Target ID."),
                        "action": genai.types.Schema(type=genai.types.Type.STRING, description="Action."),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Behavior purpose."),
                        "risk_level": genai.types.Schema(type=genai.types.Type.STRING, enum=["High", "Medium", "Low"], description="Risk level."),
                    },),),
        }
    )
}

# ---------------------------------------------------------------------------
# THREAT_ANALYSIS_CONFIG (딕셔너리 형태로 변경)
# ---------------------------------------------------------------------------
THREAT_ANALYSIS_CONFIG: Dict[str, Any] = {
    # "temperature"는 여기에 포함되지 않을 수 있음. generate_content 호출 시점에 결정.
    "response_mime_type": "application/json",
    "response_schema": genai.types.Schema(
        type=genai.types.Type.OBJECT,
        description="Analysis of potential threats to the system.",
        required=["threats"],
        properties={
            "threats": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="List of potential threats identified.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["id", "stride_category", "origin", "threat_target", "attack_surface", "trust_boundary_risk", "security_gap", "actor_risk", "behavioral_risk", "assumptions", "mitigation", "description", "trace_source"],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Threat ID."),
                        "stride_category": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["Spoofing", "Tampering", "Repudiation", "Information Disclosure", "Denial of Service", "Elevation of Privilege"],
                            description="STRIDE category.",
                        ),
                        "origin": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Threat origin.",
                            required=["from_chunk", "actor_id", "behavior_id", "capability_match"],
                            properties={
                                "from_chunk": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Identified from document chunk."),
                                "actor_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Originating actor ID."),
                                "behavior_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Related behavior ID."),
                                "capability_match": genai.types.Schema(type=genai.types.Type.STRING, nullable=True, description="Matching capability."),
                            },),
                        "threat_target": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Threat target.",
                            required=["component_id", "asset_ids"],
                            properties={
                                "component_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Targeted component ID."),
                                "asset_ids": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.INTEGER), description="Targeted asset IDs."),
                            },),
                        "attack_surface": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Attack surface.",
                            required=["behavior_id", "data_flow_id", "data_description"],
                            properties={
                                "behavior_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Exposing behavior ID."),
                                "data_flow_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Involved data flow ID."),
                                "data_description": genai.types.Schema(type=genai.types.Type.STRING, description="Data/input description."),
                            },),
                        "trust_boundary_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Trust boundary risk.",
                            required=["boundary_id", "boundary_name", "between_component_ids"],
                            properties={
                                "boundary_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Involved boundary ID."),
                                "boundary_name": genai.types.Schema(type=genai.types.Type.STRING, nullable=True, description="Boundary name."),
                                "between_component_ids": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.INTEGER), description="Component IDs across boundary."),
                            },),
                        "security_gap": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Security gap.",
                            required=["confidentiality_required", "integrity_required", "availability_required", "gap_description"],
                            properties={
                                "confidentiality_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Confidentiality gap."),
                                "integrity_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Integrity gap."),
                                "availability_required": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Availability gap."),
                                "gap_description": genai.types.Schema(type=genai.types.Type.STRING, description="Gap description."),
                            },),
                        "actor_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Actor risk.",
                            required=["actor_id", "type", "overprivileged", "description"],
                            properties={
                                "actor_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Actor ID."),
                                "type": genai.types.Schema(type=genai.types.Type.STRING, enum=SMART_CONTRACT_ACTOR_TYPES_EN, nullable=True, description="Actor type."), # 스마트 컨트랙트용 Enum
                                "overprivileged": genai.types.Schema(type=genai.types.Type.BOOLEAN, description="Actor overprivileged."),
                                "description": genai.types.Schema(type=genai.types.Type.STRING, description="Actor risk description."),
                            },),
                        "behavioral_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Behavioral risk.",
                            required=["behavior_id", "risk_level", "rationale"],
                            properties={
                                "behavior_id": genai.types.Schema(type=genai.types.Type.INTEGER, nullable=True, description="Behavior ID."),
                                "risk_level": genai.types.Schema(type=genai.types.Type.STRING, enum=["High", "Medium", "Low"], description="Risk level."),
                                "rationale": genai.types.Schema(type=genai.types.Type.STRING, description="Risk rationale."),
                            },),
                        "assumptions": genai.types.Schema(
                            type=genai.types.Type.ARRAY, description="Assumptions made.",
                            items=genai.types.Schema(type=genai.types.Type.STRING, description="An assumption."),),
                        "mitigation": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Mitigation measures.",
                            required=["strategy", "type", "priority"],
                            properties={
                                "strategy": genai.types.Schema(type=genai.types.Type.STRING, description="Mitigation strategy."),
                                "type": genai.types.Schema(type=genai.types.Type.STRING, enum=["Technical Control", "Process Control", "Policy", "Monitoring Control", "Architectural Change"], description="Mitigation type."), # 확장된 Enum
                                "priority": genai.types.Schema(type=genai.types.Type.STRING, enum=["High", "Medium", "Low"], description="Mitigation priority."),
                            },),
                        "description": genai.types.Schema(type=genai.types.Type.STRING, description="Comprehensive threat description."),
                        "trace_source": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Trace to source document.",
                            required=["doc_reference", "matched_capability"],
                            properties={
                                "doc_reference": genai.types.Schema(type=genai.types.Type.STRING, nullable=True, description="Document reference."),
                                "matched_capability": genai.types.Schema(type=genai.types.Type.STRING, nullable=True, description="Matched capability from document."),
                            },),
                    },
                ),
            ),
        }
    )
}


# ───────────── ENUM 정의 (스마트 컨트랙트 감사에 맞게 확장/조정된 버전 사용) ─────────────
class CategoryEnum(str, Enum):
    AUTHENTICATION = "Authentication"
    AUTHORIZATION = "Authorization"
    ACCESS_CONTROL = "Access Control"
    INPUT_VALIDATION = "Input Validation"
    STATE_MANAGEMENT = "State Management"
    ARITHMETIC_ISSUES = "Arithmetic Issues"
    REENTRANCY = "Reentrancy"
    EXTERNAL_CALLS = "External Calls"
    GAS_OPTIMIZATION = "Gas Optimization"
    TOKENOMICS = "Tokenomics"
    UPGRADEABILITY = "Upgradeability"
    ERROR_HANDLING = "Error Handling"
    LOGGING = "Logging"
    MONITORING = "Monitoring"
    CONFIGURATION = "Configuration"
    UX_VERIFICATION = "UX Verification"
    POLICY = "Policy"
    TESTING_COVERAGE = "Testing Coverage"
    DENIAL_OF_SERVICE = "Denial of Service"
    FRONT_RUNNING_MEV = "Front-running/MEV"
    TIMESTAMP_DEPENDENCE = "Timestamp Dependence"
    SIGNATURE_MALLEABILITY = "Signature Malleability"
    SHORT_ADDRESS_ATTACK = "Short Address Attack"

class CheckTypeEnum(str, Enum):
    TECHNICAL = "Technical"
    PROCEDURAL = "Procedural"
    MANUAL_REVIEW = "Manual Review"
    CONTRACT_REVIEW = "Contract Review"
    AUTOMATED_TEST = "Automated Test"
    FORMAL_VERIFICATION = "Formal Verification"
    ECONOMIC_MODEL_REVIEW = "Economic Model Review"
    ARCHITECTURAL_REVIEW = "Architectural Review"

class TargetTypeEnum(str, Enum):
    COMPONENT = "Component"
    FUNCTION = "Function"
    VARIABLE = "Variable"
    EVENT = "Event"
    MODIFIER = "Modifier"
    ASSET = "Asset"
    BEHAVIOR = "Behavior"
    TRUST_BOUNDARY = "TrustBoundary"
    SYSTEM_WIDE = "System-Wide"
    EXTERNAL_INTERACTION = "External Interaction"

class SecurityPropertyEnum(str, Enum):
    INTEGRITY = "Integrity"
    CONFIDENTIALITY = "Confidentiality"
    AVAILABILITY = "Availability"
    CORRECTNESS = "Correctness"
    NON_REPUDIATION = "Non-Repudiation"
    ACCESS_CONTROL_EFFECTIVENESS = "Access Control Effectiveness"
    ERROR_HANDLING_ROBUSTNESS = "Error Handling Robustness"
    RESILIENCE_TO_KNOWN_ATTACKS = "Resilience to Known Attacks"

class PriorityEnum(str, Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    INFORMATIONAL = "Informational"

class StatusEnum(str, Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"
    NOT_APPLICABLE = "Not Applicable"
    NEEDS_DISCUSSION = "Needs Discussion"
    MITIGATED = "Mitigated"
    PENDING_VERIFICATION = "Pending Verification"

# ───────────── Checklist Item 정의 (Pydantic 모델) ─────────────
class ChecklistItem(BaseModel):
    id: int = Field(..., description="Unique ID for the check item")
    title: str = Field(..., description="Short, clear, and actionable title")
    description: str = Field(..., description="Explanation of what needs to be checked and why")
    linked_threat_id: Optional[int] = Field(None, description="Threat ID this check is associated with, if any")

    category: str = Field(..., description="Security category of the check")
    check_type: str = Field(..., description="Type of check (e.g., Technical, Manual Review)")

    target_entity: Optional[int] = Field(None, description="ID of the component or asset being verified, if applicable")
    target_type: str = Field(..., description="Type of target (e.g., Component, Function)")

    security_property: str = Field(..., description="Security property being verified")
    priority: str = Field(..., description="Priority level of the check")

    assumption_ref: Optional[str] = Field(None, description="Assumption that motivates this check, if any")
    mitigation_ref: Optional[str] = Field(None, description="Mitigation action related to this check, if any")
    evidence_required: str = Field(..., description="Evidence needed to prove the check")

    automatable: bool = Field(..., description="Whether this check can be automated")
    status: str = Field("Not Started", description="Current status of this check item")

    last_checked: Optional[str] = Field(
        None,
        description="Timestamp of last validation (nullable, ISO 8601 format)"
    )
    owner: Optional[str] = Field(None, description="Team or person responsible, if assigned")
    notes: Optional[str] = Field(None, description="Additional notes or observations for this checklist item.")


class ChecklistConfig(BaseModel):
    checklist_items: List[ChecklistItem]

class ChecklistAssessmentFinding(BaseModel):
    category: str = Field(..., description="Category of the finding")
    type: str = Field(..., description="Type of finding")
    checklist_id: int = Field(..., description="ID of related checklist item")
    description: str = Field(..., description="Detailed description of the finding")
    severity: Optional[str] = Field(None, description="Severity level of the finding")
    recommendation: Optional[str] = Field(None, description="Recommended action")
    status: Optional[str] = Field("Not Started", description="Current status of this finding")

class ChecklistAssessmentConfig(BaseModel):
    summary: str = Field(..., description="Overall summary of the assessment")
    findings: List[ChecklistAssessmentFinding] = Field(..., description="List of findings from the assessment")

class CodeBindingAssessmentFinding(BaseModel):
    type: str = Field(..., description="Type of the code binding finding")
    checklist_id: int = Field(..., description="ID of related checklist item")
    description: str = Field(..., description="Description of the finding")
    code_reference: Optional[str] = Field(None, description="Specific reference to code location")

class CodeBindingAssessmentConfig(BaseModel):
    summary: str = Field(..., description="Summary of the code binding assessment")
    findings: List[CodeBindingAssessmentFinding] = Field(..., description="List of code binding findings")