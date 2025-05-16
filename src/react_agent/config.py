from google.genai import types
from google import genai

ARCHITECTURE_RESPONSE_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required = ["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
        properties = {
            "actors": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "name", "type", "capabilities"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "name": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "type": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            enum = ["External User", "Internal Service", "Partner System"],
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "capabilities": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        ),
                    },
                ),
            ),
            "assets": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "name", "type", "sensitivity"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "name": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "type": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "sensitivity": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            enum = ["High", "Medium", "Low"],
                        ),
                    },
                ),
            ),
            "components": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "name", "assets_managed"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "name": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "trust_level": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            enum = ["High", "Medium", "Low"],
                        ),
                        "assets_managed": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                        ),
                    },
                ),
            ),
            "data_flows": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "source_id", "destination_id", "data", "security_properties"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "source_id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "destination_id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "data": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "security_properties": genai.types.Schema(
                            type = genai.types.Type.OBJECT,
                            required = ["confidentiality_required", "integrity_required", "availability_required"],
                            properties = {
                                "confidentiality_required": genai.types.Schema(
                                    type = genai.types.Type.BOOLEAN,
                                ),
                                "integrity_required": genai.types.Schema(
                                    type = genai.types.Type.BOOLEAN,
                                ),
                                "availability_required": genai.types.Schema(
                                    type = genai.types.Type.BOOLEAN,
                                ),
                            },
                        ),
                    },
                ),
            ),
            "trust_boundaries": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "name", "between_ids", "validation_required"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "name": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "between_ids": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "validation_required": genai.types.Schema(
                            type = genai.types.Type.BOOLEAN,
                        ),
                    },
                ),
            ),
            "behaviors": genai.types.Schema(
                type = genai.types.Type.ARRAY,
                items = genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["id", "name", "initiator_type", "initiator_id", "target_id", "action"],
                    properties = {
                        "id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "name": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "initiator_type": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            enum = ["Actor", "Component"],
                        ),
                        "initiator_id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "target_id": genai.types.Schema(
                            type = genai.types.Type.INTEGER,
                        ),
                        "action": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "risk_level": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            enum = ["High", "Medium", "Low"],
                        ),
                    },
                ),
            ),
        },
    ),
)

ARCHITECTURE_ASSESSMENT_CONFIG = types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0,
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["evaluation_summary", "findings"],
            properties = {
                "evaluation_summary": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
                    properties = {
                        "actors": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "assets": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "components": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "data_flows": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "trust_boundaries": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "behaviors": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                    },
                ),
                "findings": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["category", "type", "id", "description"],
                        properties = {
                            "category": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
                            ),
                            "type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["missing", "hallucinated", "invalid_reference", "schema_error", "inconsistent"],
                            ),
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                                nullable = "True",
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
    )

ARCHITECTURE_CORRECTION_CONFIG = types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0,
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["actors", "assets", "components", "data_flows", "trust_boundaries", "behaviors"],
            properties = {
                "actors": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "name", "type", "capabilities"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["External User", "Internal Service", "Partner System"],
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "capabilities": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                        },
                    ),
                ),
                "assets": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "name", "type", "sensitivity"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "sensitivity": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["High", "Medium", "Low"],
                            ),
                        },
                    ),
                ),
                "components": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "name", "assets_managed"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "trust_level": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["High", "Medium", "Low"],
                            ),
                            "assets_managed": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.INTEGER,
                                ),
                            ),
                        },
                    ),
                ),
                "data_flows": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "source_id", "destination_id", "data", "security_properties"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "source_id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "destination_id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "data": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "security_properties": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["confidentiality_required", "integrity_required", "availability_required"],
                                properties = {
                                    "confidentiality_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "integrity_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "availability_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                },
                            ),
                        },
                    ),
                ),
                "trust_boundaries": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "name", "between_ids", "validation_required"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "between_ids": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.INTEGER,
                                ),
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "validation_required": genai.types.Schema(
                                type = genai.types.Type.BOOLEAN,
                            ),
                        },
                    ),
                ),
                "behaviors": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "name", "initiator_type", "initiator_id", "target_id", "action"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "initiator_type": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Actor", "Component"],
                            ),
                            "initiator_id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "target_id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "action": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "risk_level": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["High", "Medium", "Low"],
                            ),
                        },
                    ),
                ),
            },
        ),
    )

THREAT_ANALYSIS_CONFIG = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["threats"],
            properties = {
                "threats": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "stride_category", "origin", "threat_target", "attack_surface", "trust_boundary_risk", "security_gap", "actor_risk", "behavioral_risk", "assumptions", "mitigation", "description", "trace_source"],
                        properties = {
                            "id": genai.types.Schema(
                                type = genai.types.Type.INTEGER,
                            ),
                            "stride_category": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                enum = ["Spoofing", "Tampering", "Repudiation", "Information Disclosure", "Denial of Service", "Elevation of Privilege"],
                            ),
                            "origin": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["from_chunk", "actor_id", "behavior_id", "capability_match"],
                                properties = {
                                    "from_chunk": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "actor_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "behavior_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "capability_match": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                            "threat_target": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["component_id", "asset_ids"],
                                properties = {
                                    "component_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "asset_ids": genai.types.Schema(
                                        type = genai.types.Type.ARRAY,
                                        items = genai.types.Schema(
                                            type = genai.types.Type.INTEGER,
                                        ),
                                    ),
                                },
                            ),
                            "attack_surface": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["behavior_id", "data_flow_id", "data_description"],
                                properties = {
                                    "behavior_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "data_flow_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "data_description": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                            "trust_boundary_risk": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["boundary_id", "boundary_name", "between_component_ids"],
                                properties = {
                                    "boundary_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "boundary_name": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                    "between_component_ids": genai.types.Schema(
                                        type = genai.types.Type.ARRAY,
                                        items = genai.types.Schema(
                                            type = genai.types.Type.INTEGER,
                                        ),
                                    ),
                                },
                            ),
                            "security_gap": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["confidentiality_required", "integrity_required", "availability_required", "gap_description"],
                                properties = {
                                    "confidentiality_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "integrity_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "availability_required": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "gap_description": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                            "actor_risk": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["actor_id", "type", "overprivileged", "description"],
                                properties = {
                                    "actor_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "type": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                        enum = ["External User", "Internal Service", "Partner System"],
                                    ),
                                    "overprivileged": genai.types.Schema(
                                        type = genai.types.Type.BOOLEAN,
                                    ),
                                    "description": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                            "behavioral_risk": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["behavior_id", "risk_level", "rationale"],
                                properties = {
                                    "behavior_id": genai.types.Schema(
                                        type = genai.types.Type.INTEGER,
                                    ),
                                    "risk_level": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                        enum = ["High", "Medium", "Low"],
                                    ),
                                    "rationale": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                            "assumptions": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                            "mitigation": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["strategy", "type", "priority"],
                                properties = {
                                    "strategy": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                    "type": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                        enum = ["Technical Control", "Process Control", "Policy"],
                                    ),
                                    "priority": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                        enum = ["High", "Medium", "Low"],
                                    ),
                                },
                            ),
                            "description": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "trace_source": genai.types.Schema(
                                type = genai.types.Type.OBJECT,
                                required = ["doc_reference", "matched_capability"],
                                properties = {
                                    "doc_reference": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                    "matched_capability": genai.types.Schema(
                                        type = genai.types.Type.STRING,
                                    ),
                                },
                            ),
                        },
                    ),
                ),
            },
        ),
    )

CHECKLIST_CONFIG = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["checklist_items"],
            properties = {
                "checklist_items": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["id", "title", "description", "linked_threat_id", "category", "check_type", "target_entity", "target_type", "security_property", "priority", "assumption_ref", "mitigation_ref", "evidence_required", "automatable", "status", "owner"],
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
                            "last_checked": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Timestamp of last validation",
                                format = "date-time",
                                nullable = "True",
                            ),
                            "owner": genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Team or person responsible",
                            ),
                        },
                    ),
                ),
            },
        ),
    )

CHECKLIST_CORRECTION_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required=["checklist_items"],
        properties={
            "checklist_items": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=[
                        "id", "title", "description", "linked_threat_id", "category",
                        "check_type", "target_entity", "target_type", "security_property",
                        "priority", "assumption_ref", "mitigation_ref", "evidence_required",
                        "automatable", "status", "owner"
                    ],
                    properties={
                        "id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                        ),
                        "title": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "linked_threat_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                        ),
                        "category": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "check_type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "target_entity": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                        ),
                        "target_type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "security_property": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "priority": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "assumption_ref": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "mitigation_ref": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "evidence_required": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "automatable": genai.types.Schema(
                            type=genai.types.Type.BOOLEAN,
                        ),
                        "status": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                        "last_checked": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ), 
                        "owner": genai.types.Schema(
                            type=genai.types.Type.STRING,
                        ),
                    }
                )
            )
        }
    )
)

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
                    required=["category", "type", "id", "description"],
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
                        "id": genai.types.Schema(
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

CODE_BINDING_ASSESSMENT_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    temperature=0,
    response_schema=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        required=["summary", "findings"],
        properties={
            "summary": genai.types.Schema(
                type=genai.types.Type.STRING
            ),
            "findings": genai.types.Schema(
                type=genai.types.Type.ARRAY,
                items=genai.types.Schema(
                    type=genai.types.Type.OBJECT,
                    required=["type", "description"],
                    properties={
                        "type": genai.types.Schema(
                            type=genai.types.Type.STRING,
                            enum=[
                                "missing_binding",
                                "invalid_reference",
                                "irrelevant_binding",
                                "schema_error"
                            ]
                        ),
                        "threat_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            nullable="True"
                        ),
                        "checklist_id": genai.types.Schema(
                            type=genai.types.Type.INTEGER,
                            nullable="True"
                        ),
                        "description": genai.types.Schema(
                            type=genai.types.Type.STRING
                        ),
                    },
                ),
            ),
        },
    )
)