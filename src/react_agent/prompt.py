"""
위협 모델링 관련 프롬프트 템플릿
이 모듈은 블록체인 시스템의 위협 모델링을 위한 다양한 프롬프트 템플릿을 포함합니다.
"""



# ===== 아키텍처 분석 프롬프트 =====
ARCHITECTURE_ANALYSIS_TEMPLATE = """
System: You are an expert threat-modeling assistant.

Context:  
Here is the system documentation:

Content:  
{target_docs}

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
- Ensure every entry can be traced to specific evidence in `{target_docs}`.

Begin JSON output now.
"""



# ===== 평가 프롬프트 =====
ARCHITECTURE_ASSESSMENT_TEMPLATE = """
**System:** You are an Expert Panel for Threat Modeling Output Verification.

**Context:**
- A system documentation.
    

{target_docs}

- A structured JSON output was generated according to the following schema: **actors**, assets, components, data_flows, trust_boundaries, and behaviors.

{initial_architecture_analysis}

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
    
- **All items must be verifiable** within `{target_docs}`.
"""



# ===== 아키텍처 수정 프롬프트 =====
ARCHITECTURE_CORRECTION_TEMPLATE = """
**System:** You are a Senior Threat Modeling Analyst responsible for generating the **final, validated** analysis result.

**Context:**

You are given:

1. **System Documentation** – The authoritative source that describes the actual architecture and design.
   `{target_docs}`

2. **Initial Draft Output** – A structured JSON generated by an LLM from the system documentation, using the following schema: `actors`, `assets`, `components`, `data_flows`, `trust_boundaries`, and `behaviors`.
   `{initial_architecture_analysis}`

3. **Panel Validation Findings** – Expert feedback identifying hallucinations, missing elements, incorrect references, or schema violations in the draft output.
   `{assessment_architecture}`

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





# ===== 위협 분석 프롬프트 =====
THREAT_ANALYSIS_TEMPLATE = """
**System:**
You are a STRIDE-based threat modeling assistant with expertise in analyzing actor-driven behaviors and identifying security risks based on specific architectural context.

**Context:**
You are provided with the following:

1. **Complete System Model**
   Includes `actors`, `components`, `assets`, `data_flows`, `trust_boundaries`, and `behaviors`.

`{architecture_analysis}`

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
   
`{target_docs}`   

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
   
   `{target_docs}`
   
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

`{threat_analysis}`

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



# ===== 체크리스트 수정 프롬프트 =====
CHECKLIST_CORRECTION_TEMPLATE = """
**System:** You are a Senior Threat Modeling Analyst responsible for generating the **final, validated** checklist output.

**Context:**

You are given:

1. **System Documentation** – The authoritative source describing system architecture, threats, and security concerns.
   {target_docs}

2. **Initial Draft Checklist** – A structured JSON generated by an LLM based on the documentation, using the following schema: checklist_items. Each item includes fields like `id`, `title`, `description`, `linked_threat_id`, `category`, `check_type`, `target_entity`, `target_type`, and `security_property`.
   {initial_checklist}

3. **Panel Validation Findings** – Expert review that identifies hallucinations, missing checks, schema violations, or ambiguous entries in the draft checklist.
   {assessment_checklist}

---

**Task:**
Generate a **final, corrected JSON checklist** that:

1. **Removes or corrects** all hallucinated, ambiguous, or schema-invalid items from the initial checklist, based on the findings.
2. **Adds** any **missing but justified** checklist items that are clearly supported by the system documentation and mentioned in the findings.
3. Ensures all items are:

   * Directly traceable to the documentation
   * Fully schema-compliant
   * Consistent in fields like ID, references, categories, and technical accuracy

---

**Strict Requirements:**

* Do **not** invent or infer items that are not clearly supported by {target_docs}.
* You may retain items that were not flagged in {findings}, as long as they are valid and traceable.
* Follow this schema exactly:

{
  "checklist_items": [
    {
      "id": 1,
      "title": "...",
      "description": "...",
      "linked_threat_id": 1,
      "category": "...",
      "check_type": "...",
      "target_entity": 1,
      "target_type": "...",
      "security_property": "...",
      "priority": "...",
      "assumption_ref": "...",
      "mitigation_ref": "...",
      "evidence_required": "...",
      "automatable": true,
      "status": "...",
      "last_checked": null,
      "owner": "..."
    }
  ]
}

* IDs must be **unique integers**.
* All references (like `linked_threat_id`, `target_entity`) must point to valid elements described in the documentation.
* Final output must be **clean JSON only**, suitable for automated post-processing and validation.

---

**Output:**
Return only the final corrected JSON object. Do **not** include any explanation, commentary, or extra formatting.

**Begin your final structured checklist JSON output now.**
"""




CHECKLIST_ASSESSMENT_TEMPLATE = """
**System:** You are an Expert Panel for Security Checklist Validation.

**Context:**
- Below is the original threat analysis that identifies risks within the system:

{threat_analysis}

- Based on this threat analysis, an initial set of security checklist items was generated in structured JSON format. These items include fields such as `id`, `title`, `description`, `linked_threat_id`, `category`, `check_type`, `target_entity`, `target_type`, and `security_property`.

Initial checklist to review:

{initial_checklist}

**Task:**  
You are to review the generated **initial checklist** with the goal of validating its correctness, traceability to the threat model, and usefulness as a security review tool. Please assess the following:

1. **Traceability** – Is each checklist item clearly linked to a relevant threat in the analysis? Flag any hallucinated or unsupported items.
    
2. **Completeness** – Are there any important checks missing based on the threat analysis or known security practices?
    
3. **Schema Compliance** – Does each item conform to the expected structure (e.g., required fields present, ID uniqueness)?
    
4. **Relevance & Clarity** – Is each item specific, technically actionable, and clearly written?

**Instructions:**
- Provide a brief evaluation summary of the `checklist_items` overall.
- Then return a list of **validation findings** in the following format:

{
  "findings": [
    {
      "category": "checklist_items",
      "type": "missing",
      "id": null,
      "description": "Checklist missing for input validation on governance proposal submission, which is mentioned as a risk in the threat model."
    },
    {
      "category": "checklist_items",
      "type": "hallucinated",
      "id": 2,
      "description": "Checklist references biometric authentication, but this is not mentioned in the threat analysis."
    },
    {
      "category": "checklist_items",
      "type": "schema_error",
      "id": 3,
      "description": "`target_type` is missing or invalid."
    },
    {
      "category": "checklist_items",
      "type": "clarity_issue",
      "id": 1,
      "description": "Checklist title is too vague; needs to specify what identity checks are being verified."
    }
  ]
}

**Strict Review Principles:**

- Base all judgments strictly on what is written in `{threat_analysis}` and found in `{initial_checklist}`.
- If a checklist item is not clearly supported by the threat context, it must be flagged.
- Each item should be practical, traceable, and clearly contribute to mitigating a specific threat.
"""




CODE_BINDING_ASSESSMENT_TEMPLATE = """
**System:** You are a Security Engineer responsible for validating the correctness and completeness of a threat-to-code binding process.

**Context:**

You are given:

1. **Code Binding Output** – A JSON array of one or more `threats` that have been mapped to relevant source code locations or evidence (e.g., files, functions, or lines).
   {code_binding}

2. **Checklist Items** – A structured list of checklist items that were originally generated to mitigate or detect these threats. Each checklist item includes `id`, `description`, `linked_threat_id`, and additional metadata.
   {checklist_items}

---

**Task:**

Evaluate the **code binding output** in relation to the checklist items and documentation. You must verify:

1. **Traceability** – For each threat, does the mapped code artifact clearly correspond to the **linked checklist item**? Is the evidence valid and well-supported?

2. **Completeness** – Are there any threats or checklist items that are **not covered** by any code binding? Flag if a threat has no corresponding implementation or test.

3. **Relevance & Accuracy** – Is the bound code artifact actually relevant to the security concern? Are the file paths, functions, or logic well-scoped and justified?

4. **Schema Compliance** – Does the code binding object include the required fields: `threat_id`, `checklist_id`, `file_path`, `function`, `reason`?

---

**Instructions:**

- Provide a concise **summary** of the overall validation.
- Then return a list of findings in this schema:

```json
{
  "findings": [
    {
      "type": "missing_binding",
      "checklist_id": 2,
      "description": "Checklist item 2 is not bound to any code artifact."
    },
    {
      "type": "invalid_reference",
      "threat_id": 5,
      "description": "Threat 5 is mapped to a file path that does not exist in the source repository."
    },
    {
      "type": "irrelevant_binding",
      "checklist_id": 7,
      "description": "The code bound to checklist item 7 does not handle the risk described in its threat."
    },
    {
      "type": "schema_error",
      "checklist_id": 3,
      "description": "Missing required field `file_path` in code binding object."
    }
  ]
}
```
"""

