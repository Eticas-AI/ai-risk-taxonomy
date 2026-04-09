# Eticas AI Risk Taxonomy

**Version:** 0.1.0-draft  
**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**License:** CC BY 4.0  
**Maintained by:** [Eticas](https://eticas.ai)

## About this taxonomy

This is Eticas' unified AI risk taxonomy — a structured, machine-readable vocabulary of risk categories used across all of Eticas' audit methodologies, assessment frameworks, and reporting outputs.

Each concept in the taxonomy has a stable URI, a canonical definition, and formal links to equivalent or related concepts in major international frameworks. The taxonomy is published as a SKOS (Simple Knowledge Organization System) vocabulary, making it interoperable with knowledge graphs, linked data systems, and semantic web tools.

The taxonomy is designed to be:

- **Authoritative** — the single source of truth for risk category definitions across Eticas
- **Interoperable** — formally linked to NIST, EU AI Act, MIT AI Risk Repository, OECD, ISO, and W3C DPV vocabularies
- **Extensible** — new categories and subcategories can be added without breaking existing references
- **Human-readable and machine-readable** — source files are editable YAML; build outputs include browsable HTML, SKOS Turtle, and JSON-LD

## Taxonomy structure

The taxonomy is organised in three levels: **risk categories** (top level), **subcategories** (specific risk types), and **indicators** (observable manifestations, linked to assessment checks in Eticas methodologies).

Each concept carries the following metadata:

| Field | Description |
|-------|-------------|
| `id` | Stable identifier (e.g., `bias-fairness`, `privacy-pii-leakage`) |
| `uri` | Persistent URI under `https://taxonomy.eticas.ai/risk/` |
| `prefLabel` | Canonical English label |
| `altLabel` | Alternative labels / synonyms used in Eticas documents |
| `definition` | Prose definition |
| `scope` | Applicability: `ADM`, `LLM`, or `ALL` |
| `inclusion` | Whether this category is part of every audit: `required` or `audit-dependent` |
| `maturity` | How developed the category is: `established`, `developing`, `provisional`, or `proposed` |
| `perspective` | Which client concern the category addresses: `rights & ethics`, `technical soundness`, `governance & compliance`, or `operational viability` |
| `lifecycle_stages` | Where in the AI lifecycle this risk manifests: `pre-processing`, `in-processing`, `post-processing` |
| `mappings` | External equivalences (see Alignment section below) |

---

## Category classification

Each risk category is classified along three independent dimensions: **inclusion** (whether it is part of every audit), **maturity** (how developed the category is), and **perspective** (which client concern it addresses).

### Inclusion: required vs. audit-dependent

**Required** — Assessed in every Eticas audit regardless of system type or engagement scope. These categories represent risks that are relevant to any AI system.

**Audit-dependent** — Assessed based on the engagement scope, system type, and regulatory context. Their exclusion from a specific audit is a scoping decision that should be documented and justified.

### Maturity: how developed the category is

**Established** — Stable definition, well-developed subcategories, proven assessment methods, and strong mappings to external frameworks. Changes to established categories are made carefully.

**Developing** — The definition is solid, but subcategories and assessment methods are being refined through use in audits. External mappings may be partial.

**Provisional** — Recognised as important, but definitions may change, subcategories are incomplete, and assessment methods are not yet proven. Findings referencing provisional categories should note the provisional status.

**Proposed** — Suggested but not yet validated by the team. Included in the taxonomy to show how the category would integrate. Definitions, subcategories, and scope are subject to discussion.

### Perspective: which client concern the category addresses

**Rights & ethics** — Does the system respect people's rights and treat them fairly?

**Technical soundness** — Does the system work correctly and safely?

**Governance & compliance** — Is the system properly managed and legally compliant?

**Operational viability** — Will the system actually deliver value in context?

### Current classification

| Category | Inclusion | Maturity | Perspective |
|----------|-----------|----------|-------------|
| Bias & Fairness | required | established | rights & ethics |
| Privacy & Confidentiality | required | established | rights & ethics |
| Reliability | required | established | technical soundness |
| Governance | required | established | governance & compliance |
| Security & Misuse | required | established | technical soundness |
| Transparency & Explainability | required | established | governance & compliance |
| Environmental Impact | audit-dependent | established | technical soundness |
| Responsibility & Redress | audit-dependent | developing | rights & ethics |
| Autonomy & Human Agency | audit-dependent | provisional | rights & ethics |
| Agentic Risks | audit-dependent | provisional | technical soundness |
| Manipulation & Misinformation | audit-dependent | provisional | rights & ethics |
| Resilience | audit-dependent | proposed | operational viability |
| Integration Readiness | audit-dependent | proposed | operational viability |

All three dimensions can change independently. An audit-dependent category can be promoted to required as practice evolves. A proposed category becomes provisional once validated by the team, then developing and established as methods mature. These are team decisions documented in the changelog.

---

## Risk categories

### Required categories

These categories are assessed in every Eticas audit.

#### 1. Bias & Fairness
`https://taxonomy.eticas.ai/risk/bias-fairness`

The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts. This includes biases introduced through data, model design, or deployment context, and covers both measurable disparities and perceived unfairness in decision-making.

**Subcategories:**
- **Dataset bias and under/over-representation** — Training or evaluation data that does not adequately represent all relevant population groups
- **Proxy discrimination** — Discrimination through correlated features that serve as proxies for protected attributes
- **Intersectional unfairness** — Compounded disadvantage affecting individuals at the intersection of multiple protected characteristics
- **Accessibility barriers** — System design that excludes or disadvantages people with disabilities
- **Geographic, cultural, or language skew** — Systematic performance differences across geographies, cultures, or languages
- **Feedback loops reinforcing inequality** — System outputs that, when fed back into the system or its context, amplify existing biases
- **Quality of service disparities** — Inconsistent service quality across demographic groups
- **Stereotyping and demeaning content** — Outputs that reinforce, erase, or demean demographic groups
- **Harmful content and toxicity** — Offensive or harmful outputs that damage user well-being
- **Sentiment fairness across groups** — Unequal emotional tone in outputs across groups
- **Performance equity across populations** — Higher error rates for specific groups

#### 2. Privacy & Confidentiality
`https://taxonomy.eticas.ai/risk/privacy-confidentiality`

The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality). This includes risks from data leakage, re-identification, unauthorized use, or insufficient safeguards.

**Subcategories:**
- **Unlawful collection or processing of personal data**
- **Re-identification of anonymised data**
- **Function creep** — Repurposing data beyond original intent
- **Biometric surveillance** — Mass biometric data collection and processing
- **Emotion inference or sensitive attribute profiling**
- **Weak data retention/erasure and access controls**
- **PII leakage** — Personal data present in training data leaking through model outputs
- **Membership inference risk** — Ability to determine whether specific individuals were in training data

#### 3. Reliability
`https://taxonomy.eticas.ai/risk/reliability`

The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts. Such failures undermine trust, reduce system dependability, and can lead to harmful or misguided decisions.

**Subcategories:**
- **Hallucination and fabricated outputs** — Generation of false or misleading information that appears credible
- **Output inconsistency** — Inconsistent results across similar inputs and contexts
- **Output drift over time** — Degradation of output quality or accuracy as conditions change
- **Out-of-distribution robustness** — Unpredictable behaviour when exposed to unfamiliar data
- **Failure and remediation gaps** — Lack of remediation plans for predictable or unknown failures
- **Monitoring and evaluation gaps** — Lack of monitoring rendering datasets obsolete and outputs unreliable

#### 4. Governance
`https://taxonomy.eticas.ai/risk/governance`

The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use. Weak governance can lead to unclear responsibilities, poor documentation, limited auditability, and failure to align with legal, ethical, or organizational standards.

**Subcategories:**
- **Unclear responsibilities and accountability gaps** — Missing or ambiguous role assignments
- **Poor documentation** — Incomplete or outdated system documentation
- **Limited auditability** — Insufficient logging, versioning, or traceability for external review
- **Regulatory non-compliance** — Failure to align with applicable legal or ethical standards
- **Lack of change management** — Absence of controlled processes for system modifications
- **Oversight of adverse impacts** — Missing processes for identifying and escalating harmful outcomes
- **Fitness for purpose** — System not validated against the problem it is intended to solve
- **Data governance** — Inadequate labelling, tagging, approval, or appropriateness assessment of data
- **Human oversight and control** — Lack of defined intervention points or override capabilities
- **Decision traceability** — Inability to trace decisions back to specific inputs and processes
- **Critical input/output logging** — Failure to log inputs and outputs systematically
- **Responsible actor attribution** — Unclear attribution of responsibility across developers, deployers, and reviewers
- **Task success** — Low or uneven task success across subpopulations or input types

#### 5. Security & Misuse
`https://taxonomy.eticas.ai/risk/security-misuse`

The risk that an AI system is exposed to vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality. This includes adversarial inputs, model inversion, data poisoning, prompt injection, and unauthorized access, which can lead to manipulation of outputs, data breaches, or system failure.

**Subcategories:**
- **Adversarial attacks** — Evasion, poisoning, and extraction attacks
- **Prompt injection** (LLM) — Malicious inputs that subvert system intent
- **Jailbreaking** (LLM) — Bypass of safety controls to trigger prohibited behaviours
- **Unauthorized access** — Exploitation of access control weaknesses
- **Supply-chain vulnerabilities** — Risks from third-party components, data sources, or model providers
- **Incident response gaps** — Insufficient detection, logging, or response capabilities
- **Misuse beyond intended purpose** — Use of the system for purposes it was not designed for

#### 6. Transparency & Explainability
`https://taxonomy.eticas.ai/risk/transparency-explainability`

The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs. Lack of transparency undermines informed consent, impedes oversight, and erodes trust.

**Subcategories:**
- **AI system explainability** — Stakeholders misinterpret or misunderstand system purpose or outputs
- **Communication to stakeholders** — Stakeholders not aware of system limitations or settings
- **Disclosure of AI interaction** — Users interacting with AI under the assumption it is human
- **Model card completeness** — Incomplete documentation of model purpose, performance, or limitations
- **Prompt transparency** (LLM) — Inconsistent outputs to semantically similar inputs reducing trust

### Audit-dependent categories

These categories are assessed based on engagement scope and system type.

#### 7. Environmental Impact
`https://taxonomy.eticas.ai/risk/environmental-impact`

The risk that an AI system's development, deployment, or use causes negative environmental effects, such as excessive energy or water consumption, carbon emissions, or unsustainable use of hardware and resources. This includes hidden impacts across the system's lifecycle, from model training to long-term operation.

**Subcategories:**
- **Inference-time energy consumption** — High energy use during deployment
- **Training resource consumption** — Significant carbon emissions from model training
- **Hardware efficiency** — Poor hardware utilisation increasing costs and environmental impact

#### 8. Responsibility & Redress
`https://taxonomy.eticas.ai/risk/responsibility-redress`

The risk that individuals affected by AI-driven decisions have no effective means to understand, challenge, or seek remedy for those decisions. This includes absence of appeal mechanisms, unclear remediation procedures, and failure to communicate with affected parties.

**Subcategories:**
- **Absence of appeal mechanisms**
- **Unclear remediation procedures**
- **Ineffective communication with affected parties**

#### 9. Autonomy & Human Agency
`https://taxonomy.eticas.ai/risk/autonomy`

The risk that an AI system undermines individuals' ability to make free, informed decisions, whether through over-reliance, automation bias, manipulative design, or erosion of human agency.

#### 10. Agentic Risks
`https://taxonomy.eticas.ai/risk/agentic-risks`

The risk that AI systems operating with a degree of autonomy — planning, executing multi-step actions, using tools, or coordinating with other AI agents — introduce failure modes not present in single-inference systems. This includes cascading errors across agent chains, unintended emergent behaviour, and loss of meaningful human control over compound actions.

#### 11. Manipulation & Misinformation
`https://taxonomy.eticas.ai/risk/manipulation-misinformation`

The risk that AI systems are used — intentionally or through design flaws — to deceive, manipulate, or mislead individuals or populations. This includes generation of disinformation at scale, deepfakes, subliminal manipulation, and pollution of the information ecosystem.

### Proposed categories

These categories have been suggested but not yet validated by the team. They are included to show how they would integrate into the taxonomy.

#### 12. Resilience
`https://taxonomy.eticas.ai/risk/resilience`

The risk that an AI system cannot absorb disruption, degrade gracefully, or recover when faced with adverse events, attacks, infrastructure failures, or environmental changes. This goes beyond reliability (consistent performance under normal conditions) and robustness (performance under varied conditions) to address what happens when the system is genuinely disrupted and must recover or continue operating in degraded mode. Particularly critical for AI deployed in conflict zones, humanitarian operations, or critical infrastructure.

**Subcategories:**
- **Graceful degradation** — Absence of defined degradation pathways for partial function under component failure
- **Edge and offline operability** — System inability to function without continuous cloud access or connectivity
- **Recovery capability** — Lack of tested recovery procedures or rollback mechanisms
- **Infrastructure dependency** — Unmapped dependencies on external infrastructure whose failure would disable the system
- **Contextual and ethical resilience** — Absence of safeguards against function creep, weaponisation, or repurposing against served populations

#### 13. Integration Readiness
`https://taxonomy.eticas.ai/risk/integration-readiness`

The risk that an AI system fails to deliver value not because of model performance issues but because it does not fit the organisational, technical, or human context into which it is deployed. This includes interoperability failures with existing systems, insufficient organisational capacity to absorb the technology, workflow incompatibility, and lack of sustainable maintenance capability.

**Subcategories:**
- **Organisational readiness** — Insufficient governance maturity, leadership engagement, change management, or staff competency
- **Technical interoperability** — Inability to integrate with existing infrastructure, legacy systems, or data standards
- **Workflow compatibility** — System outputs or interfaces that don't fit existing human workflows, causing alert fatigue or abandonment
- **Deployment sustainability** — Lack of capacity for ongoing operation, maintenance, and monitoring after deployment
- **Institutional absorptive capacity** — Broader context lacking foundational capabilities (infrastructure, literacy, regulatory frameworks) for viable AI deployment

---

## Alignment with external frameworks

The taxonomy is formally linked to major international frameworks using SKOS mapping properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`). Each category page lists its specific mappings to the MIT AI Risk Repository, NIST AI RMF, NIST AI 600-1, OECD AI Principles, W3C DPV, ISO 42001, and the EU AI Act.

For a detailed analysis of how each Eticas category aligns with, diverges from, and extends these frameworks — including coverage gaps and areas where Eticas addresses risks that existing frameworks miss — see **[External framework alignment](docs/external-framework-alignment.md)**.

---

## Versioning and governance

The taxonomy follows [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): Breaking changes — categories removed or fundamentally redefined
- **Minor** (0.X.0): New categories or subcategories added; inclusion or maturity changes; new external mappings
- **Patch** (0.0.X): Definition refinements, typo fixes, additional alternative labels

Changes are proposed via GitHub Issues, discussed with the team, and merged via pull requests. Every release is tagged and produces a timestamped snapshot of all output formats (Turtle, JSON-LD, HTML).

---

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.1.0).
https://taxonomy.eticas.ai/risk/
```

---

*This taxonomy is maintained by Eticas and published under CC BY 4.0. Contributions and alignment suggestions are welcome via GitHub Issues.*
