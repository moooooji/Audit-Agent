from typing import Annotated, Any, TypedDict, Optional, List, Literal
from google.generativeai import types as genai_types # google.generativeai.types에 대한 별칭 사용
from google import genai # genai.types.Schema 접근을 위해 유지
# from openai import OpenAI # 현재 코드에서는 사용되지 않으므로 주석 처리 또는 제거 가능
from pydantic import BaseModel, Field # Field는 ChecklistItem에서 사용될 수 있으므로 유지
from enum import Enum # ChecklistItem의 Enum들을 위해 추가
from typing import Optional, List, Dict, Any # Dict, Any 추가
from datetime import datetime # ChecklistItem에서 사용
from google.genai import types
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

def set_gemini_config(config_name: str):
    if config_name == "ARCHITECTURE_RESPONSE_CONFIG":
        ARCHITECTURE_RESPONSE_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        description="Describes the overall architecture of the Web3 system or smart contract(s) under audit, based on the provided documentation (e.g., whitepaper).",
        required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors", "Architectural Analysis Judgment Basis"],
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
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER, 
                            description="Asset ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset name."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset description."
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset type (e.g., Token, Data)."
                        ),
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
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Component ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Component name."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Component description."
                        ),
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
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Data flow ID."
                        ),
                        "source_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="ID of the source actor or component."
                        ),
                        "destination_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="ID of the destination actor or component."
                        ),
                        "data": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Description of the data transferred."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Purpose of the data flow."
                        ),
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
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Trust boundary ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Trust boundary name."
                        ),
                        "between_ids": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            description="IDs of entities this boundary separates.",
                            items=genai.types.Schema(type=genai.types.Type.INTEGER, description="ID of an entity."),
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Trust boundary explanation."
                        ),
                        "validation_required": genai.types.Schema(
                            type=genai.types.Type.BOOLEAN,
                            description="Validation required when crossing."
                        ),
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
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Behavior ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Behavior name."
                        ),
                        "initiator_type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["Actor", "Component"],
                            description="Type of initiator.",
                        ),
                        "initiator_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Initiator ID."
                        ),
                        "target_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER, 
                            description="Target component ID."
                        ),
                        "action": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Action performed."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Behavior purpose."
                        ),
                        "risk_level": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Inherent risk level.",
                        ),
                    },
                ),
            ),
            "Architectural Analysis Judgment Basis": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Structured rationale explaining the judgment basis for architectural analysis decisions.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    properties={
                        "actors_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for actor identification."
                        ),
                        "assets_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for asset categorization."
                        ),
                        "components_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for component identification."
                        ),
                        "data_flows_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for data flow mapping."
                        ),
                        "trust_boundaries_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for trust boundary establishment."
                        ),
                        "behaviors_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for behavior extraction."
                        ),
                    },
                ),
            ),
        },
    ),
)
        return ARCHITECTURE_RESPONSE_CONFIG
        
    elif config_name == "ARCHITECTURE_ASSESSMENT_CONFIG":
        ARCHITECTURE_ASSESSMENT_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        description="Assessment of the extracted architecture.",
        required=["evaluation_summary", "findings"],
        properties={
            "evaluation_summary": genai.types.Schema(
                type=genai.types.Type.OBJECT,
                description="High-level summary of the assessment.",
                required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
                properties={
                    "actors": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for actors."
                    ),
                    "assets": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for assets."
                    ),
                    "components": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for components."
                    ),
                    "data_flows": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for data flows."
                    ),
                    "trust_boundaries": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for trust boundaries."
                    ),
                    "behaviors": genai.types.Schema(
                        type=genai.types.Type.STRING,
                        description="Summary for behaviors."
                    ),
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
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Detailed description of the finding."
                        ),
                    },
                ),
            ),
        },
    ),
)
        return ARCHITECTURE_ASSESSMENT_CONFIG
        

    elif config_name == "ARCHITECTURE_CORRECTION_CONFIG":
        ARCHITECTURE_CORRECTION_CONFIG = types.GenerateContentConfig(
    temperature=0,
    response_mime_type="application/json",
    response_schema=genai.types.Schema( # ARCHITECTURE_RESPONSE_SCHEMA와 구조 동일
        type=genai.types.Type.OBJECT,
        description="Corrected or refined version of the system architecture.",
        required=["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors", "Architectural Analysis Judgment Basis"],
        properties={ # 상세 설명은 ARCHITECTURE_RESPONSE_SCHEMA 참고, 여기서는 간략히
            "actors": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected actors.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "type", "capabilities"],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Actor ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Actor name."
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=SMART_CONTRACT_ACTOR_TYPES_EN,
                            description="Actor type."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Actor description."
                        ),
                        "capabilities": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            items=genai.types.Schema(
                                type=genai.types.Type.STRING
                            ),
                            description="Actor capabilities."),
                    },),),
            "assets": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected assets.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "type", "sensitivity"],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Asset ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset name."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset description."
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Asset type."
                        ),
                        "sensitivity": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Asset sensitivity."
                        ),
                    },
                ),
            ),
            "components": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected components.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "name", "assets_managed"],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Component ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Component name."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Component description."
                        ),
                        "trust_level": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Component trust level."
                        ),
                        "assets_managed": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            items=genai.types.Schema(
                                type=genai.types.Type.INTEGER
                            ),
                            description="Assets managed."
                        ),
                    },
                ),
            ),
            "data_flows": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected data flows.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=["id", "source_id", "destination_id", "data", "security_properties"],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Data flow ID."
                        ),
                        "source_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Source ID."
                        ),
                        "destination_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Destination ID."
                        ),
                        "data": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Data transferred."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Data flow purpose."
                        ),
                        "security_properties": genai.types.Schema(
                            type=genai.types.Type.OBJECT, required=[
                                "confidentiality_required", "integrity_required", "availability_required"
                            ],
                            properties={
                                "confidentiality_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Confidentiality."
                                ),
                                "integrity_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Integrity."
                                ),
                                "availability_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Availability."
                                ),
                            },
                        ),
                    },
                ),
            ),
            "trust_boundaries": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected trust boundaries.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=[
                        "id", "name", "between_ids", "validation_required"
                    ],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Boundary ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Boundary name."
                        ),
                        "between_ids": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            items=genai.types.Schema(
                                type=genai.types.Type.INTEGER
                            ),
                            description="Entity IDs."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Boundary description."
                        ),
                        "validation_required": genai.types.Schema(
                            type=genai.types.Type.BOOLEAN,
                            description="Validation required."
                        ),
                    },
                ),
            ),
            "behaviors": genai.types.Schema(
                type=genai.types.Type.ARRAY, description="Corrected behaviors.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT, required=[
                        "id", "name", "initiator_type", "initiator_id", "target_id", "action"
                    ],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Behavior ID."
                        ),
                        "name": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Behavior name."
                        ),
                        "initiator_type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["Actor", "Component"],
                            description="Initiator type."
                        ),
                        "initiator_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Initiator ID."
                        ),
                        "target_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            description="Target ID."
                        ),
                        "action": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Action."
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Behavior purpose."
                        ),
                        "risk_level": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["High", "Medium", "Low"],
                            description="Risk level."
                        ),
                    },
                ),
            ),
            "Architectural Analysis Judgment Basis": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Structured rationale explaining the judgment basis for architectural analysis decisions.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    properties={
                        "actors_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for actor identification."
                        ),
                        "assets_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for asset categorization."
                        ),
                        "components_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for component identification."
                        ),
                        "data_flows_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for data flow mapping."
                        ),
                        "trust_boundaries_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for trust boundary establishment."
                        ),
                        "behaviors_description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Source references, extraction logic, risk assessment basis, scope decisions, and assumptions for behavior extraction."
                        ),
                    },
                ),
            ),
        }
    ),
)
        return ARCHITECTURE_CORRECTION_CONFIG
    
    elif config_name == "THREAT_ANALYSIS_CONFIG":
        THREAT_ANALYSIS_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        description="Analysis of potential threats to the system.",
        required=["threats", "Threat_Analysis_Judgment_Basis"],
        properties={
            "threats": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="List of potential threats identified.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=[
                        "id", "stride_category", "origin", "threat_target",
                        "attack_surface", "trust_boundary_risk", "security_gap",
                        "actor_risk", "behavioral_risk", "assumptions",
                        "mitigation", "description", "trace_source"
                    ],
                    properties={
                        "id": genai.types.Schema(type=genai.types.Type.INTEGER, description="Threat ID."),
                        "stride_category": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=[
                                "Spoofing", "Tampering", "Repudiation",
                                "Information Disclosure", "Denial of Service",
                                "Elevation of Privilege"
                            ],
                            description="STRIDE category.",
                        ),
                        "origin": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Threat origin.",
                            required=["from_chunk", "actor_id", "behavior_id", "capability_match"],
                            properties={
                                "from_chunk": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Identified from document chunk."
                                ),
                                "actor_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Originating actor ID."
                                ),
                                "behavior_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Related behavior ID."
                                ),
                                "capability_match": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    nullable=True,
                                    description="Matching capability."
                                ),
                            },
                        ),
                        "threat_target": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Threat target.",
                            required=["component_id", "asset_ids"],
                            properties={
                                "component_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Targeted component ID."
                                ),
                                "asset_ids": genai.types.Schema(
                                    type=genai.types.Type.ARRAY,
                                    items=genai.types.Schema(
                                        type=genai.types.Type.INTEGER
                                    ),
                                    description="Targeted asset IDs."),
                            },
                        ),
                        "attack_surface": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Attack surface.",
                            required=["behavior_id", "data_flow_id", "data_description"],
                            properties={
                                "behavior_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Exposing behavior ID."
                                ),
                                "data_flow_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Involved data flow ID."
                                ),
                                "data_description": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    description="Data/input description."
                                ),
                            },
                        ),
                        "trust_boundary_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Trust boundary risk.",
                            required=["boundary_id", "boundary_name", "between_component_ids"],
                            properties={
                                "boundary_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Involved boundary ID."
                                ),
                                "boundary_name": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    nullable=True,
                                    description="Boundary name."
                                ),
                                "between_component_ids": genai.types.Schema(
                                    type=genai.types.Type.ARRAY,
                                    items=genai.types.Schema(
                                        type=genai.types.Type.INTEGER
                                    ),
                                    description="Component IDs across boundary."
                                ),
                            },
                        ),
                        "security_gap": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Security gap.",
                            required=[
                                "confidentiality_required", "integrity_required",
                                "availability_required", "gap_description"
                            ],
                            properties={
                                "confidentiality_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Confidentiality gap."
                                ),
                                "integrity_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Integrity gap."
                                ),
                                "availability_required": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Availability gap."
                                ),
                                "gap_description": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    description="Gap description."
                                ),
                            },
                        ),
                        "actor_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Actor risk.",
                            required=["actor_id", "type", "overprivileged", "description"],
                            properties={
                                "actor_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Actor ID."
                                ),
                                "type": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    enum=SMART_CONTRACT_ACTOR_TYPES_EN,
                                    nullable=True,
                                    description="Actor type."
                                ), # 스마트 컨트랙트용 Enum
                                "overprivileged": genai.types.Schema(
                                    type=genai.types.Type.BOOLEAN,
                                    description="Actor overprivileged."
                                ),
                                "description": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    description="Actor risk description."
                                ),
                            },
                        ),
                        "behavioral_risk": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Behavioral risk.",
                            required=["behavior_id", "risk_level", "rationale"],
                            properties={
                                "behavior_id": genai.types.Schema(
                                    type=genai.types.Type.INTEGER,
                                    nullable=True,
                                    description="Behavior ID."
                                ),
                                "risk_level": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    enum=["High", "Medium", "Low"]
                                    , description="Risk level."
                                ),
                                "rationale": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    description="Risk rationale."
                                ),
                            },
                        ),
                        "assumptions": genai.types.Schema(
                            type=genai.types.Type.ARRAY,
                            description="Assumptions made.",
                            items=genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="An assumption."
                            ),
                        ),
                        "mitigation": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Mitigation measures.",
                            required=["strategy", "type", "priority"],
                            properties={
                                "strategy": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    description="Mitigation strategy."
                                ),
                                "type": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    enum=[
                                        "Technical Control", "Process Control",
                                        "Policy", "Monitoring Control", "Architectural Change"
                                    ],
                                    description="Mitigation type."
                                ), # 확장된 Enum
                                "priority": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    enum=["High", "Medium", "Low"],
                                    description="Mitigation priority."
                                ),
                            },
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Comprehensive threat description."
                        ),
                        "trace_source": genai.types.Schema(
                            type=genai.types.Type.OBJECT, description="Trace to source document.",
                            required=["doc_reference", "matched_capability"],
                            properties={
                                "doc_reference": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    nullable=True,
                                    description="Document reference."
                                ),
                                "matched_capability": genai.types.Schema(
                                    type=genai.types.Type.STRING,
                                    nullable=True,
                                    description="Matched capability from document."
                                ),
                            },
                        ),
                    },
                ),
            ),
            "Threat_Analysis_Judgment_Basis": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                description="Structured rationale explaining the judgment basis for threat analysis decisions.",
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    properties={
                        "threat_identification_logic": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Why each STRIDE threat was identified for the specific behavior/component combination and systematic application methodology."
                        ),
                        "risk_level_justification": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="What factors from the architecture analysis or documentation justified the assigned risk levels and impact assessments."
                        ),
                        "attack_vector_analysis": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="How the identified attack surfaces and trust boundary vulnerabilities support the threat scenarios and entry point analysis."
                        ),
                        "mitigation_reasoning": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Why the proposed mitigation strategies are appropriate for the identified security gaps and implementation considerations."
                        ),
                        "scope_coverage": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="How comprehensively the STRIDE categories were applied to the chunk entities and completeness verification."
                        ),
                        "documentation_traceability": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            description="Which specific architectural elements or documentation references support each threat identification and validation process."
                        ),
                    },
                ),
            ),
        }
    ),
)
        return THREAT_ANALYSIS_CONFIG
    
    elif config_name == "CHECKLIST_CONFIG":
        CHECKLIST_CONFIG = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["checklist_items", "Checklist_Generation_Judgment_Basis"],
            properties = {
                "checklist_items": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "title", "description", "linked_threat_id", "category", "check_type", "target_entity", "target_type", "security_property", "priority", "assumption_ref", "mitigation_ref", "evidence_required", "automatable", "status", "need_code_binding", "last_checked", "owner"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                                description = "Unique ID for the check item",
                            ),
                            "title": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Short, clear, and actionable title",
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Explanation of what needs to be checked and why",
                            ),
                            "linked_threat_id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                                description = "Threat ID this check is associated with",
                            ),
                            "category": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Authentication", "Authorization", "Input Validation", "Configuration", "UX Verification", "Logging", "Monitoring", "Policy"],
                            ),
                            "check_type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Technical", "Procedural", "Manual Review", "Automated Test"],
                            ),
                            "target_entity": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                                description = "ID of the component or asset being verified",
                            ),
                            "target_type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Type of the target entity",
                                enum = ["Component", "Asset", "Behavior", "TrustBoundary"],
                            ),
                            "security_property": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Integrity", "Confidentiality", "Availability"],
                            ),
                            "priority": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["High", "Medium", "Low"],
                            ),
                            "assumption_ref": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Assumption that motivates this check",
                            ),
                            "mitigation_ref": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Mitigation action related to this check",
                            ),
                            "evidence_required": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Evidence needed to prove the check",
                            ),
                            "automatable": genai.types.Schema(
                                type = genai.types.Type.BOOLEAN,
                                description = "Whether this check can be automated",
                            ),
                            "status": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Not Started", "In Progress", "Completed", "Blocked"],
                            ),
                            "need_code_binding": genai.types.Schema(
                                type = genai.types.Type.BOOLEAN,
                                description = "Whether this check needs smart contract code binding",
                            ),
                            "last_checked": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Timestamp of last validation",
                                format = "date-time",
                                nullable = "True",
                            ),
                            "owner": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Team or person responsible",
                            )
                        },
                    ),
                ),
                "Checklist Generation Judgment Basis": genai.types.Schema(
                    type=genai.types.Type.ARRAY,
                    description="Structured rationale explaining the judgment basis for checklist generation decisions.",
                    items=genai.types.Schema(
                        type=genai.types.Type.OBJECT,
                        properties={
                            "item_selection_logic": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="Why each checklist item was generated from the threat analysis and what specific threat aspects it addresses."
                            ),
                            "priority_assignment_reasoning": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="What factors determined the priority levels (High/Medium/Low) for each checklist item and impact considerations."
                            ),
                            "category_mapping_justification": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="How STRIDE threat categories were mapped to checklist categories and why those mappings are appropriate."
                            ),
                            "code_binding_assessment": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="Which items require code-level verification and why, based on the technical nature of the threats."
                            ),
                            "evidence_requirements_analysis": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="Why specific evidence types were chosen for each item and how they validate the security controls."
                            ),
                            "actionability_verification": genai.types.Schema(
                                type=genai.types.Type.STRING,
                                description="How each item provides clear, executable steps for security verification rather than vague guidelines."
                            ),
                        },
                    ),
                ),
            },
        ),
    )
        return CHECKLIST_CONFIG
    
    elif config_name == "CHECKLIST_ASSESSMENT_CONFIG":
        CHECKLIST_ASSESSMENT_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        required=["evaluation_summary", "findings"],
        properties={
            "evaluation_summary": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="A concise overall evaluation summary of the checklist_items section"
            ),
            "findings": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["category", "type", "checklist_id", "description"],
                    properties={
                        "category": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=["checklist_items"],
                        ),
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=[
                                "missing",          # 명백히 빠진 항목
                                "hallucinated",     # 존재하지 않는 내용 생성
                                "schema_error",     # 필드 누락이나 포맷 오류
                                "clarity_issue"     # 모호하거나 비실용적인 표현
                            ],
                        ),
                        "checklist_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            nullable="True",
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                    },
                ),
            ),
        },
    )
)
        return CHECKLIST_ASSESSMENT_CONFIG
  
  
# --- 아래는 THREAT_ANALYSIS_CONFIG에 해당하는 Pydantic 모델들 ---

class ThreatSchemaOrigin(BaseModel):
    from_chunk: bool = Field(description="Identified from document chunk.")
    actor_id: Optional[int] = Field(description="Originating actor ID.")
    behavior_id: Optional[int] = Field(description="Related behavior ID.")
    capability_match: Optional[str] = Field(description="Matching capability.")

class ThreatSchemaThreatTarget(BaseModel):
    component_id: Optional[int] = Field(description="Targeted component ID.")
    asset_ids: List[int] = Field(description="Targeted asset IDs.")

class ThreatSchemaAttackSurface(BaseModel):
    behavior_id: Optional[int] = Field(description="Exposing behavior ID.")
    data_flow_id: Optional[int] = Field(description="Involved data flow ID.")
    data_description: str = Field(description="Data/input description.")

class ThreatSchemaTrustBoundaryRisk(BaseModel):
    boundary_id: Optional[int] = Field(description="Involved boundary ID.")
    boundary_name: Optional[str] = Field(description="Boundary name.")
    between_component_ids: List[int] = Field(description="Component IDs across boundary.")

class ThreatSchemaSecurityGap(BaseModel):
    confidentiality_required: bool = Field(description="Confidentiality gap.")
    integrity_required: bool = Field(description="Integrity gap.")
    availability_required: bool = Field(description="Availability gap.")
    gap_description: str = Field(description="Gap description.")

class ThreatSchemaActorRisk(BaseModel):
    actor_id: Optional[int] = Field(description="Actor ID.")
    # SMART_CONTRACT_ACTOR_TYPES_EN의 실제 Enum 값을 알 수 없어 str로 정의합니다.
    # 필요시 Literal[SMART_CONTRACT_ACTOR_TYPES_EN_VALUES...] 형태로 수정하세요.
    type: Optional[str] = Field(description="Actor type.")
    overprivileged: bool = Field(description="Actor overprivileged.")
    description: str = Field(description="Actor risk description.")

class ThreatSchemaBehavioralRisk(BaseModel):
    behavior_id: Optional[int] = Field(description="Behavior ID.")
    risk_level: Literal["High", "Medium", "Low"] = Field(description="Risk level.")
    rationale: str = Field(description="Risk rationale.")

class ThreatSchemaMitigation(BaseModel):
    strategy: str = Field(description="Mitigation strategy.")
    type: Literal[
        "Technical Control", "Process Control",
        "Policy", "Monitoring Control", "Architectural Change"
    ] = Field(description="Mitigation type.")
    priority: Literal["High", "Medium", "Low"] = Field(description="Mitigation priority.")

class ThreatSchemaTraceSource(BaseModel):
    doc_reference: Optional[str] = Field(description="Document reference.")
    matched_capability: Optional[str] = Field(description="Matched capability from document.")

class ThreatSchemaItem(BaseModel):
    id: int = Field(description="Threat ID.")
    stride_category: Literal[
        "Spoofing", "Tampering", "Repudiation",
        "Information Disclosure", "Denial of Service",
        "Elevation of Privilege"
    ] = Field(description="STRIDE category.")
    origin: ThreatSchemaOrigin = Field(description="Threat origin.")
    threat_target: ThreatSchemaThreatTarget = Field(description="Threat target.")
    attack_surface: ThreatSchemaAttackSurface = Field(description="Attack surface.")
    trust_boundary_risk: ThreatSchemaTrustBoundaryRisk = Field(description="Trust boundary risk.")
    security_gap: ThreatSchemaSecurityGap = Field(description="Security gap.")
    actor_risk: ThreatSchemaActorRisk = Field(description="Actor risk.")
    behavioral_risk: ThreatSchemaBehavioralRisk = Field(description="Behavioral risk.")
    assumptions: List[str] = Field(description="Assumptions made.")
    mitigation: ThreatSchemaMitigation = Field(description="Mitigation measures.")
    description: str = Field(description="Comprehensive threat description.")
    trace_source: ThreatSchemaTraceSource = Field(description="Trace to source document.")

class ThreatJudgmentBasis(BaseModel):
    threat_id: int = Field(description="The unique identifier of the threat being analyzed.")
    threat_identification_logic: str = Field(description="Why this specific STRIDE threat was identified for the particular behavior/component combination.")
    risk_level_justification: str = Field(description="What specific factors from the architecture analysis or documentation justified the assigned risk level for this threat.")
    attack_vector_analysis: str = Field(description="How the identified attack surfaces and trust boundary vulnerabilities specifically support this threat scenario.")
    mitigation_reasoning: str = Field(description="Why the proposed mitigation strategy is appropriate for this specific threat's security gaps.")
    documentation_traceability: str = Field(description="Which specific architectural elements or documentation references support this individual threat identification.")

class ThreatAnalysisOutput(BaseModel):
    threats: List[ThreatSchemaItem] = Field(description="List of potential threats identified.")
    Threat_Analysis_Judgment_Basis: List[ThreatJudgmentBasis] = Field(description="Structured rationale explaining the judgment basis for threat analysis decisions.")      

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

class ChecklistJudgmentBasis(BaseModel):
    checklist_item_id: int = Field(description="The unique identifier of the checklist item being analyzed.")
    item_selection_logic: str = Field(description="Why this specific checklist item was generated from the threat analysis and what specific threat aspects it addresses.")
    priority_assignment_reasoning: str = Field(description="What factors determined the priority level (High/Medium/Low) for this specific checklist item.")
    category_mapping_justification: str = Field(description="How the STRIDE threat category was mapped to this checklist category and why that mapping is appropriate.")
    code_binding_assessment: str = Field(description="Whether this item requires code-level verification and why, based on the technical nature of the specific threat.")
    evidence_requirements_analysis: str = Field(description="Why the specific evidence type was chosen for this item and how it validates the security control.")
    actionability_verification: str = Field(description="How this item provides clear, executable steps for security verification rather than vague guidelines.")

class Checklist(BaseModel):
    checklist_items: list[ChecklistItem]
    Checklist_Generation_Judgment_Basis: List[ChecklistJudgmentBasis] = Field(description="Structured rationale explaining the judgment basis for checklist generation decisions.")
        
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

    need_code_binding: bool = Field(..., description="Whether this check needs smart contract code binding")

    last_checked: Optional[str] = Field(
        None,
        description="Timestamp of last validation (nullable, ISO 8601 format)"
    )
    owner: Optional[str] = Field(None, description="Team or person responsible, if assigned")
    notes: Optional[str] = Field(None, description="Additional notes or observations for this checklist item.")


class ChecklistConfig(BaseModel):
    checklist_items: List[ChecklistItem]
    Checklist_Correction_Judgment_Basis: List[ChecklistJudgmentBasis] = Field(description="Structured rationale explaining the judgment basis for checklist correction decisions.")

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