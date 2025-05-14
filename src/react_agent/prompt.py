"""
위협 모델링 관련 프롬프트 템플릿
이 모듈은 블록체인 시스템의 위협 모델링을 위한 다양한 프롬프트 템플릿을 포함합니다.
"""

from google.genai import types
from google import genai

# ===== 아키텍처 분석 프롬프트 =====
ARCHITECTURE_ANALYSIS_TEMPLATE = """
System: You are an expert threat-modeling assistant.

Context:  
Here is the system documentation:

Content:  
{DOCS}

Task:
1. Extract all **actors** mentioned in the documentation. For each actor include:
    - `id`: unique integer 
    - `name`: actor name (e.g., "External User", "Admin Service") 
    - `type`: actor category (e.g., "External User", "Internal Service", "Partner System")
    - `description`: short description if given
    - `capabilities`: list of actions or permissions the actor has (e.g., "can submit requests", "has database write access")    
2. Extract all **assets** mentioned in the documentation.
3. Extract all **components**, with their `trust_level` if given, and list of managed asset IDs.
4. Extract all **data_flows** between components, referencing by IDs.
5. Extract all **trust_boundaries** and which components they separate, referencing by IDs.
6. Extract all **behaviors** describing actions initiated by an actor or component toward another component.
    

After extraction, **validate each item** against the source text:
- If an entry is inaccurate or attributes are wrong, **correct** it.
- If it is already accurate, **leave it unchanged**.

Output Requirements:
- Return **only** valid JSON (no extra text).
- Use this schema exactly:
    

{
  "actors": [
    {
      "id": 1,
      "name": "Actor Name",
      "type": "External User|Internal Service|Partner System",
      "description": "Short description",
      "capabilities": ["Capability A", "Capability B"]
    }
    // …
  ],
  "assets": [
    {
      "id": 1,
      "name": "Asset Name",
      "description": "Short description",
      "type": "Token|NFT|Key|Voting Power|…",
      "sensitivity": "High|Medium|Low"
    }
    // …
  ],
  "components": [
    {
      "id": 1,
      "name": "Component Name",
      "description": "Short description",
      "trust_level": "High|Medium|Low",
      "assets_managed": [1,2]
    }
    // …
  ],
  "data_flows": [
    {
      "id": 1,
      "source_id": 2,
      "destination_id": 3,
      "data": "What data moves",
      "description": "Short description",
      "security_properties": {
        "confidentiality_required": true,
        "integrity_required": true,
        "availability_required": false
      }
    }
    // …
  ],
  "trust_boundaries": [
    {
      "id": 1,
      "name": "Boundary Name",
      "between_ids": [2,4],
      "description": "What is protected",
      "validation_required": true
    }
    // …
  ],
  "behaviors": [
    {
      "id": 1,
      "name": "Behavior Name",
      "initiator_type": "Actor|Component",
      "initiator_id": 5,
      "target_id": 3,
      "action": "call|send|fetch|…",
      "description": "Short description",
      "risk_level": "High|Medium|Low"
    }
    // …
  ]
}


Strict Requirements:
- Only extract information **explicitly** stated in the documentation.
- Do **not** infer or assume beyond the text.
- If a field is not clearly provided, **omit** that field.
- Do **not** hallucinate any element.
- Ensure every entry can be traced to specific evidence in `{DOCS}`.

Begin JSON output now.
"""

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

# ===== 평가 프롬프트 =====
ASSESSMENT_TEMPLATE = """
**System:** You are an Expert Panel for Threat Modeling Output Verification.

**Context:**
- A system documentation.
    

{docs}

- A structured JSON output was generated according to the following schema: **actors**, assets, components, data_flows, trust_boundaries, and behaviors.

{json}

**Task:**  
You will perform a comprehensive panel review of the extracted output to evaluate the following:

1. **Traceability** – Is each extracted item **explicitly** supported by the documentation? Flag any hallucinated or unsupported entries.
    
2. **Completeness** – Are there any **missing** entries that are clearly present in the documentation but were **not extracted**?
    
3. **Schema Compliance** – Does each item conform to the **required JSON schema** and allowed field values (e.g., types, ID uniqueness, structure)?
    
4. **Consistency** – Are IDs, cross-references (e.g., `assets_managed`, `initiator_id`, `between_ids`), and values such as `trust_level` or `risk_level` used **correctly and uniformly**?
    

**Instructions:**
- For each category (`actors`, `assets`, `components`, `data_flows`, `trust_boundaries`, `behaviors`), provide a short **evaluation summary**.
- Then, return a list of **validation findings** in the following schema:
    
{
  "findings": [
    {
      "category": "actors",
      "type": "missing",
      "id": null,
      "description": "Actor `X` is mentioned in the documentation but was not extracted."
    },
    {
      "category": "components",
      "type": "invalid_reference",
      "id": 3,
      "description": "`assets_managed` refers to an asset ID not found in the assets list."
    },
    {
      "category": "assets",
      "type": "hallucinated",
      "id": 5,
      "description": "Asset `Y` is not mentioned anywhere in the documentation."
    }
  ]
}

**Strict Review Principles:**

- Do **not** infer beyond what is written in the documentation.
    
- If a field or item is **not explicitly stated**, it must be flagged as hallucinated or omitted.
    
- **All items must be verifiable** within `{docs}`.
"""

ASSESSMENT_CONFIG = types.GenerateContentConfig(
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

# ===== 아키텍처 수정 프롬프트 =====
ARCHITECTURE_CORRECTION_TEMPLATE = """
**System:** You are a Senior Threat Modeling Analyst responsible for generating the **final, validated** analysis result.

**Context:**

You are given:

1. **System Documentation** – The authoritative source that describes the actual architecture and design.
   `{docs}`

2. **Initial Draft Output** – A structured JSON generated by an LLM from the system documentation, using the following schema: `actors`, `assets`, `components`, `data_flows`, `trust_boundaries`, and `behaviors`.
   `{initial_json}`

3. **Panel Validation Findings** – Expert feedback identifying hallucinations, missing elements, incorrect references, or schema violations in the draft output.
   `{findings}`

---

**Task:**
Generate a **final, corrected JSON output** that:

1. **Fixes or removes** all hallucinated, incorrect, or schema-violating items from the initial output based on the validation findings.
2. **Adds** any **missing items** that are explicitly present in the documentation and noted in the findings.
3. Ensures all items are:

   * Traceable to the documentation
   * Schema-compliant
   * Internally consistent (IDs, references, types)

---

**Strict Requirements:**

* Do **not** invent or infer information not directly supported by `{docs}`.
* Every item must be **justified by the documentation** and **not flagged** in `{findings}`, or must have been corrected based on that feedback.
* Follow the schema **exactly**:


{
  "actors": [ ... ],
  "assets": [ ... ],
  "components": [ ... ],
  "data_flows": [ ... ],
  "trust_boundaries": [ ... ],
  "behaviors": [ ... ]
}


* IDs must be **unique integers**, and all **cross-references must be valid**.
* If an item from the initial output is valid and unflagged, it may be retained.
* All modifications must result in a complete and clean JSON that could be used for downstream analysis or visualization.

---

**Output:**
Return only the final JSON output. Do not include any explanation, commentary, or intermediate notes.

**Begin your final structured JSON output now.**
"""

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



# ===== 위협 분석 프롬프트 =====
THREAT_ANALYSIS_TEMPLATE = """
**System:**
You are a STRIDE-based threat modeling assistant with expertise in analyzing actor-driven behaviors and identifying security risks based on specific architectural context.

**Context:**
You are provided with the following:

1. **Complete System Model**
   Includes `actors`, `components`, `assets`, `data_flows`, `trust_boundaries`, and `behaviors`.

`{model}`

2. **Focused Analysis Chunk**
   A filtered subset of the system model centered on a single `actor` and all related:

   * Behaviors they initiate
   * Target components
   * Managed assets
   * Relevant data flows
   * Applicable trust boundaries

`{chunk}`

3. **Reference Documentation**
   Contains technical descriptions and intended behaviors for components and actors.
   
`{docs}`   

4. **ID Reference Guide**  
   Use the following rules to interpret ID references within the system:

	- `actors[].id` → unique actor ID
	- `assets[].id` → unique asset ID
	- `components[].id` → unique component ID
	- `components[].assets_managed` → references asset IDs
	- `data_flows[].source_id` / `destination_id` → reference component IDs
	- `trust_boundaries[].between_ids` → references component IDs
	- `behaviors[].initiator_id` → references either an actor ID or component ID
	- `behaviors[].target_id` → references a component ID

---

**Task:**

Based **only on the entities within the chunk**, identify all plausible security threats by applying the STRIDE framework:

* S: Spoofing
* T: Tampering
* R: Repudiation
* I: Information Disclosure
* D: Denial of Service
* E: Elevation of Privilege

---

For each identified threat, generate a JSON object including:

{
  "id": 1,
  "stride_category": "Spoofing",
  "origin": {
    "from_chunk": true,
    "actor_id": 1,
    "behavior_id": 5,
    "capability_match": "Vote on Proposal"
  },
  "threat_target": {
    "component_id": 9,
    "asset_ids": [4]
  },
  "attack_surface": {
    "behavior_id": 5,
    "data_flow_id": 11,
    "data_description": "vote selection + signature"
  },
  "trust_boundary_risk": {
    "boundary_id": 2,
    "boundary_name": "User to Contract",
    "between_component_ids": [1, 9]
  },
  "security_gap": {
    "confidentiality_required": false,
    "integrity_required": true,
    "availability_required": true,
    "gap_description": "Vote input may be spoofed without signature verification."
  },
  "actor_risk": {
    "actor_id": 1,
    "type": "External User",
    "overprivileged": false,
    "description": "The actor is unauthenticated and can perform governance actions."
  },
  "behavioral_risk": {
    "behavior_id": 5,
    "risk_level": "High",
    "rationale": "The system accepts unsigned votes from external actors."
  },
  "assumptions": [
    "The governance contract does not enforce signature verification for vote messages.",
    "The actor is able to access the voting interface without authentication."
  ],
  "mitigation": {
    "strategy": "Require signature-based vote authentication and role validation.",
    "type": "Technical Control",
    "priority": "High"
  },
  "description": "An attacker may impersonate a user and submit fraudulent votes to the governance contract.",
  "trace_source": {
    "doc_reference": "governance/voting.md#vote-process",
    "matched_capability": "Vote on Proposal"
  }
}


---

**Instructions:**

* Output a **JSON array** named `threats`, each object matching the schema above.
* Do **not include threats unrelated to the current chunk**.
* Use exact `id` references from the chunk when filling `actor_id`, `component_id`, `asset_ids`, etc.
* Be specific and concise in each field.
* You may output multiple STRIDE threats for a single behavior if applicable.
* For each threat, include a `"assumptions"` field: an array of short, concrete statements describing the conditions assumed in order for the threat to exist.

---

**End your output with:**

{
  "threats": [ ... ]
}
"""

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


# ===== 체크리스트 프롬프트 =====
CHECKLIST_TEMPLATE = """
**System**:
You are a threat modeling and security checklist generation expert.
You receive structured STRIDE-based threat descriptions and convert them into high-quality, traceable, and actionable security checklist items.
Each item should help ensure that the threat is effectively mitigated or controlled in practice.

---

**Input**:
1. **Complete System Model**
   Includes context for checklist generation
   
   `{context}`
   
2. **Focused Analysis Threats**
You are given a JSON object that contains one or more `threats`, following this schema:

* `stride_category`
* `description`
* `assumptions`
* `attack_surface`
* `security_gap`
* `mitigation`
* `threat_target`
* `behavioral_risk`
* `actor_risk`
* `origin`
* `trust_boundary_risk`
* `trace_source`

`{Threat}`

---

**Task**:

For each threat:

* Generate **only the security checklist items that are meaningful, relevant, and actionable**.
* You are **not required to produce a fixed number of items**.
* **Do not generate checklist items that are trivial, vague, or redundant**.
* Each checklist item should clearly trace back to:

  * A security assumption or mitigation strategy
  * A STRIDE category (mapped to a checklist category)
  * A component or asset (from the threat_target)

---

**Checklist Item Output Format**:

```json
{
  "id": "1",
  "title": "Ensure forum account is tied to on-chain identity",
  "description": "Check if forum users submitting RFRVs are verified through on-chain identity.",
  "linked_threat_id": 1,
  "category": "Authentication",
  "check_type": "Technical",
  "target_entity": 22,
  "target_type": "Component",
  "security_property": "Integrity",
  "priority": "High",
  "assumption_ref": "The Governance Forum lacks strong authentication mechanisms to verify the identity of the user submitting the RFRV.",
  "mitigation_ref": "Implement strong authentication (e.g., linking forum account to on-chain identity, SSO)",
  "evidence_required": "Screenshot or audit log showing linked on-chain identity at login.",
  "automatable": false,
  "status": "Not Started",
  "last_checked": null,
  "owner": "Security Engineering Team"
}
```

---

**Guidelines**:

* **Quality > Quantity**: Prefer 1 strong checklist item over 3 weak ones.
* **Be specific**: "Verify authentication" is vague. Instead say "Verify that forum requires wallet-based login for RFRV submitters."
* **Trace everything**: Each checklist item must quote an assumption or mitigation as its justification.
* **Use judgment**: If the mitigation is trivial (e.g., "add logging") but doesn't align with the actual threat, do not generate an item.

---

**Expected Output**:

Return a JSON array of checklist items. The number may vary based on how many meaningful items can be derived from the input.
"""

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

ASSESSMENT_CHECKLIST_TEMPLATE = """
**System**:
You are a security engineer.
You are given a JSON object that contains one or more `threats`, following this schema:

`{Checklist}`
"""

ASSESSMENT_CHECKLIST_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required = ["checklist_items"],
    ),
)


ASSESSMENT_CHECKLIST_WITH_CODE_TEMPLATE = """
**System**:
You are a security engineer.
You are given a JSON object that contains one or more `threats`, following this schema:

`{Checklist}`
"""

ASSESSMENT_CHECKLIST_WITH_CODE_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required = ["checklist_items"],
    ),
)

CODE_BINDING_TEMPLATE = """
**System**:
You are a security engineer.
You are given a JSON object that contains one or more `threats`, following this schema:

`{Checklist}`
"""

CODE_BINDING_CONFIG = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=genai.types.Schema(
        type = genai.types.Type.OBJECT,
        required = ["code_binding"],
    ),
)