# External framework alignment

This document maps the Eticas AI Risk Taxonomy (v0.3) against the ten major international AI risk frameworks, standards, and academic taxonomies it links to. It describes where Eticas categories align, where they diverge, and where Eticas addresses risk areas that existing frameworks miss. For per-concept mapping detail, see the framework-by-framework verification at [docs/external-framework-mapping-verification.md](external-framework-mapping-verification.md). For the application history, see [TRACKER.md](../TRACKER.md).

## Frameworks covered

Eticas v0.3 links to ten frameworks, organised into three buckets reflecting their function in the AI governance landscape:

### Compliance — legally binding or directly certifiable

| Framework | Scope | Machine-readable |
|-----------|-------|------------------|
| [EU AI Act](https://artificialintelligenceact.eu) (Regulation 2024/1689) | Risk tiers, prohibited practices (Art. 5), high-risk AI requirements (Arts. 9–15), transparency obligations (Art. 50), GPAI/systemic-risk obligations (Arts. 51–55), post-market monitoring & incident reporting (Arts. 72–73), Right to explanation (Art. 86) | Via [W3C DPV EU AI Act extension](https://w3c.github.io/dpv/2.3/legal/eu/aiact/) |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | AI Management System Standard, 38 controls across 9 control objectives (A.2–A.10). Companions: ISO/IEC 42005:2025 (AI impact assessment), ISO/IEC 42006:2025 (certification body requirements), ISO/IEC 12792:2025 (transparency taxonomy) | Paid standard, no vocabulary |
| [AIUC-1](https://www.aiuc-1.com) | Q2-2026 release. Certifiable standard for AI agents with six core domains (A. Data & Privacy, B. Security, C. Safety, D. Reliability, E. Accountability, F. Society) and ~55 controls | URIs minted by Eticas referencing lettered control identifiers |

### Reference — soft-law principles and policy frameworks

| Framework | Scope | Machine-readable |
|-----------|-------|------------------|
| [NIST AI RMF (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | January 2023. Four functions (Govern, Map, Measure, Manage) and seven characteristics of trustworthy AI | PDF only |
| [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | July 2024 Generative AI Risk Profile. 12 risk categories unique to or exacerbated by generative AI | PDF only |
| [OECD AI Principles](https://oecd.ai) | 2024 update. Five values-based principles (1.1–1.5) and five recommendations (2.1–2.5) | PDF only |

### Taxonomy & vocabulary — academic, vendor, and semantic

| Framework | Scope | Machine-readable |
|-----------|-------|------------------|
| [MIT AI Risk Repository V4](https://airisk.mit.edu) | December 2025. 1,725 risks across 7 domains and 24 subdomains, derived from 74 frameworks | CSV/Sheets (CC BY 4.0) |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | Zeng et al. Four Level-1 categories, 16 Level-2, 45 Level-3, and 314 Level-4 risks derived from 8 government regulations and 16 corporate policies | Paper only |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | 2024–2025 (integrated into IBM Risk Atlas Nexus). Lifecycle-based taxonomy organising risks across Input / Inference / Output / Non-technical stages | URIs minted by Eticas |
| [W3C DPV v2.3](https://w3c.github.io/dpv/) | February 2026 Final Community Group Report. Vocabulary family with AI Extension, Risk Extension, EU AI Act Extension, Privacy core. The only framework in this set with production-ready SKOS concept URIs | RDF (Turtle, JSON-LD, RDF/XML, N3) |

**Notes on the W3C DPV.** The Data Privacy Vocabulary is broader than its name suggests. Version 2.3 (February 2026) contains 9,982 concepts across multiple extensions: a core privacy vocabulary, an [AI extension](https://w3c.github.io/dpv/2.3/ai/) covering bias types, security attacks, and AI lifecycle, a [Risk extension](https://w3c.github.io/dpv/2.3/risk/) covering risk management and a full risk/impact taxonomy, and an [EU AI Act extension](https://w3c.github.io/dpv/2.3/legal/eu/aiact/) encoding the regulation's concepts in RDF. The AIRO and VAIR ontologies (Golpayegani, Pandit, Lewis; ADAPT Centre, Trinity College Dublin) have been formally incorporated into DPV's AI and EU AI Act extensions. **DPV is the only framework in this set that provides production-ready SKOS concept URIs** suitable for formal linking. It is a W3C Community Group Final Specification, not a full W3C Recommendation.

**Notes on NIST.** Both AI 100-1 (RMF) and AI 600-1 (GenAI Profile) are under directed revision following the July 2025 White House AI Action Plan, but no revised versions have been published. The companion NIST AI 100-2 E2025 (Adversarial ML Taxonomy, March 2025) is the most significant NIST taxonomy update since AI 600-1.

**Notes on AIUC-1.** AIUC-1 is the most agent-focused framework in this set, with explicit controls for tool-call safety, AI endpoint scraping, and unauthorized agent actions. It is also the only certifiable standard targeted at AI agents (rather than AI management systems generally). It has weaknesses in fairness/bias coverage, environmental impact, and socioeconomic risks — these gaps are flagged in mappings as absent rather than papered over with weak matches.

## Category-level alignment

The table below shows how each of Eticas' 9 categories maps to its closest equivalent in each framework. Cells indicate the strength of alignment using SKOS terminology. Where a category contains sub-groups or subcategories with their own distinct mappings, the mapping shown is for the category itself; per-concept detail is in the verification document and in the YAML.

| Eticas category | EU AI Act | ISO 42001 | AIUC-1 | NIST RMF | NIST 600-1 | OECD | MIT V4 | AIR 2024 | IBM Atlas | W3C DPV |
|---|---|---|---|---|---|---|---|---|---|---|
| **Bias & Fairness** | close — Art. 10 | narrow — A.7.4 | related — C.5 | close — Fair w/ Harmful Bias Managed | broad — #6 | broad — Pr. 1.2 | close — Domain 1 | broad — L1 Discrim. & Bias | close — Output Fairness | close — `ai:AIBias` |
| **Privacy & Confidentiality** | broad — Art. 10 | close — A.7.5 | **exact — A** | close — Privacy-Enhanced | broad — #4 | close — Pr. 1.2 | broad — Domain 2 | broad — L2 Privacy | close — Privacy lifecycle | close — `dpv:PersonalDataHandling` |
| **Reliability** | close — Art. 15 | close — A.6.2.4 | **exact — D** | close — Valid & Reliable | close — #2 + #8 | close — Pr. 1.4 | close — 7.3 | close — Operational Misuses | close — Output Robustness | broad — `ai:ModelRisk` |
| **Governance** | close — Art. 17 + 9 | **exact — A.2 + A.3** | close — E (Accountability) | close — Govern function | narrow — #12 | close — Pr. 1.5 | broad — 6.5 | broad — implicit | **exact — Governance dim.** | close — `dpv:Governance` |
| **Security & Misuse** | close — Art. 15(5) + Art. 5 | close — A.6.2.5 + A.10 | close — B + F | close — Secure & Resilient | broad — #9 + #1 | close — Pr. 1.4 | close — 2.2 + Domain 4 | close — Security + Manipulation | close — Inference + Misuse | close — `ai:SecurityAttack` |
| **Environmental Impact** | related — Art. 95 | close — A.5.2 | — *(gap)* | — | **exact — #5** | **exact — Pr. 1.1** | **exact — 6.6** | related — 6.6 | **exact — Env. impact** | close — Risk env. impact |
| **Transparency & Explainability** | close — Art. 13 | **exact — A.8** | close — E.16 + E.17 | close — Explainable & Interpretable | close — #8 | close — Pr. 1.3 | close — 7.5 | related — Deception | **exact — Output Expl. + Non-tech Trans.** | broad — `ai:Transparency` |
| **Autonomy & Agency** | broad — Art. 14 | close — A.6.2.7 | close — B.6 + C.7 | related — Govern 3 | close — #7 | close — Pr. 1.2 (added 2024) | close — Domain 5 | close — Autonomous Unsafe Op | close — Value Alignment | broad — `ai:HumanOversight` |
| **Organisational Readiness** | close — Art. 4 + 26 | **exact — A.4.2 + A.4.3 + A.3** | close — E.4 + E.10 + E.12 | broad — Govern 2 + 4 | related — implicit | close — Rec. 2.4 | related — implicit | — | close — Skill gaps + Vendor risk | close — `dpv:OrganisationalMeasure` |

**Reading the table.** Cells in **bold** are exact matches — the framework concept and the Eticas concept are equivalent in scope and meaning. The categories with the strongest cross-framework alignment are **Environmental Impact** (4 exact matches), **Transparency & Explainability** (3 exact matches at category level), and **Privacy & Confidentiality**, **Reliability**, **Organisational Readiness** (each with one exact match anchoring it firmly in a major framework).

## Where Eticas aligns with the consensus

The core categories — Bias & Fairness, Privacy & Confidentiality, Reliability, Governance, Security & Misuse — are well-established across all major frameworks. Every framework addresses them, though with varying granularity and naming. The main variations are structural rather than substantive:

**Naming differences are the primary source of friction.** NIST uses compound names ("Secure & Resilient", "Fair with Harmful Bias Managed"), the MIT Repository uses domain-level labels that don't map 1:1 to Eticas categories ("Discrimination & Toxicity" bundles bias with toxic content), and the EU AI Act distributes requirements across articles rather than naming risk categories. The taxonomy's `alt_labels` and SKOS mapping links address this by documenting every name variant and its formal equivalent.

**Granularity varies significantly.** Where Eticas defines 8 subcategories under Bias & Fairness (organised into 3 sub-groups), NIST 600-1 has a single category ("Harmful Bias & Homogenization"), the MIT Repository has 3 subdomains, and AIR 2024 decomposes "Discrimination & Bias" into 60 Level-4 risks (20 protected characteristics × 3 discriminatory activities). Conversely, NIST's governance structure (the Govern function alone has 17 subcategories) is more detailed than Eticas's Governance category. This is appropriate — Eticas is an audit taxonomy, not a process framework, and not a per-policy enumeration of harms.

**The W3C DPV is the strongest alignment target for formal linking.** It is the only framework that provides concept-level URIs in RDF, covers nearly every Eticas category across its AI, Risk, and EU AI Act extensions, and is actively maintained. v0.3 mapped six Eticas concepts to formal DPV IRIs as `exactMatch`: `data-poisoning` ↔ `ai:DataPoisoning`, `prompt-injection` ↔ `ai:PromptInjection`, `adversarial-attacks` ↔ `ai:AdversarialAttack`, `automation-bias` ↔ `ai:AutomationBias`, `re-identification` ↔ `risk:Reidentification`, `membership-inference` ↔ `ai:MembershipInferenceAttack`, plus `right-to-explanation-contestation` ↔ `dpv:RightToExplanation` (DPV core / GDPR extension).

**The EU AI Act anchors specific Eticas concepts to specific articles.** v0.3 mapped four concepts as `exactMatch` to specific articles: `right-to-explanation-contestation` ↔ Art. 86, `human-oversight-control` ↔ Art. 14, `ai-interaction-disclosure` ↔ Art. 50, `incident-response-gaps` ↔ Art. 73, plus `behavioural-manipulation` ↔ Art. 5(1)(a) (subliminal/manipulative techniques). These anchors make it straightforward to demonstrate adherence to specific Articles when conducting audits in the EU.

## Where Eticas diverges from or extends existing frameworks

### Risks vs mechanisms

A core distinction in v0.3 is the separation between *risks* (what can go wrong) and *mechanisms* (how a risk arises or is observed). Concepts like dataset bias, proxy discrimination, model card incompleteness, or absence of an appeal process — which earlier versions of the taxonomy treated as standalone subcategories — are not standalone in v0.3. They live as `operationalisation` entries on the parent risk concept they help assess. No surveyed framework makes this distinction explicit; most flatten risks and mechanisms into a single list. The Eticas approach keeps the risk hierarchy clean and provides the structural hook for the methodology layer (metrics, methods, evidence pointers) being built in parallel.

### Three-level hierarchy with sub-groups

Most frameworks use either a flat list (NIST 600-1: 12 categories) or a two-level hierarchy (MIT: 7 domains → 24 subdomains; AIUC-1: 6 domains → ~55 controls). Eticas uses three levels: categories → sub-groups → subcategories. This allows fine-grained risk types to be navigable without flattening them into an unstructured list. For example, Bias & Fairness contains three sub-groups (Outcome disparities, Representational harm, Dynamic & Systemic bias) — each with its own set of subcategories and distinct external framework mappings.

### Lifecycle-stage tagging

Eticas tags every subcategory with the lifecycle stages where it manifests (pre-processing, in-processing, post-processing). Most frameworks either organise by lifecycle stage (NIST MAP/MEASURE/MANAGE; IBM Risk Atlas Input/Inference/Output) or by risk domain (MIT, NIST 600-1, AIR 2024) but not both. The dual tagging allows the same taxonomy to serve both a risk-domain view (for reporting) and a lifecycle view (for audit execution).

### Audit-oriented granularity

Existing frameworks tend toward either very high-level principles (OECD: 5 principles) or very fine-grained risk inventories (MIT: 1,725 entries; AIR 2024: 314 risk types). Eticas targets the middle ground — 9 categories, 18 sub-groups, 70 active subcategories, structured at a granularity where each subcategory is auditable (you can write assessment checks for it) but not so granular that the taxonomy becomes an encyclopaedia.

### Compliance / reference / taxonomy split on every concept page

Every concept page renders its mappings in three sections — Compliance, Reference frameworks, Taxonomies & vocabularies — corresponding to the framework `type` classification. This means a reader can go to any concept and see at a glance: which legal obligations apply (compliance), which policy frameworks reference it (reference), which conceptual or vocabulary equivalents exist (taxonomy). No surveyed framework structures its cross-references this way.

## How Eticas addresses gaps in existing frameworks

### Resilience as a named sub-group under Reliability

The concept of resilience — the ability to absorb disruption, degrade gracefully, and recover — is fragmented across existing frameworks rather than treated as a coherent assessment area. The EU AI Act's Article 15 uses "resilient" in two places: for robustness (Art. 15(4), "as resilient as possible regarding errors, faults or inconsistencies") and for cybersecurity (Art. 15(5), "resilient against attempts by unauthorised third parties"). NIST pairs resilience with security as a single trustworthiness characteristic ("Secure & Resilient"). ISO 22989 defines it separately from robustness and reliability as the "ability to recover operational condition quickly following an incident."

Eticas addresses this by placing resilience as a named sub-group within Reliability, with five specific subcategories: graceful degradation, edge/offline operability, recovery capability, infrastructure dependency, and contextual/ethical resilience. The key conceptual distinction:

| Property | Focus | Question it answers |
|----------|-------|-------------------|
| Reliability | Consistency under normal conditions | "Does it work correctly?" |
| Robustness | Performance under varied conditions | "Does it still work when conditions change?" |
| Resilience | Recovery after disruption | "What happens when it breaks, and can it come back?" |

This is particularly important for AI deployed in conflict zones, humanitarian operations, or critical infrastructure — contexts where standard assumptions about operating conditions do not hold. The five subcategories under `reliability-resilience` were left without subcategory-level external mappings during the v0.3 mapping refresh, deliberately: no clean equivalents exist in the surveyed frameworks. This is the gap the Eticas treatment addresses.

### Organisational Readiness as a standalone category

Between 70 and 85% of AI initiatives fail to meet their objectives — and the primary causes are organisational and integration factors, not model performance. No major AI risk taxonomy treats this as a standalone risk domain. The MIT Repository catalogues what can go wrong with AI systems but not what goes wrong when AI meets organisations. NIST's MAP function acknowledges deployment context but doesn't formalise it as a risk type. ISO 42001 mentions interoperability and resources within lifecycle management. AIR 2024 has no equivalent.

Eticas addresses this with Organisational Readiness as a standalone category covering five dimensions: organisational preparedness (governance maturity, staff competency, change management), workflow compatibility (alert fatigue, end-user involvement), deployment sustainability (ongoing maintenance, vendor dependency), institutional absorptive capacity (digital infrastructure, data literacy), and technical interoperability (legacy systems, data pipelines, API conformance).

The strongest external anchor is ISO 42001 A.4.2 (Resources — human / competence) + A.4.3 (Tooling) + A.3 (Internal organization) — mapped as `exactMatch`. The evidence base includes well-documented failures where technically capable systems failed in organisational context: IBM Watson for Oncology, the Epic Sepsis Model, FEMA's AI damage assessment tools.

### Right to explanation and contestation

The dissolved Incident Reporting & Redress category had `absence-of-appeal` and `ineffective-communication` as standalone subcategories. v0.3 absorbs them into a new `right-to-explanation-contestation` subcategory under Transparency, with two strong anchors:

- EU AI Act **Article 86** — Right to explanation of individual decision-making (`exactMatch`)
- W3C DPV `dpv:RightToExplanation` (DPV core / GDPR extension) (`exactMatch`)

This makes the concept a first-class member of the Transparency hierarchy with formal links to both regulatory obligation and SKOS vocabulary, rather than a subcategory of a niche category that few audits triggered.

### Autonomy & Agency dual coverage

Autonomy & Agency merges two dimensions that frameworks treat inconsistently. The human side (automation bias, over-reliance, deskilling, trust calibration) is addressed by MIT's Domain 5 and NIST 600-1 #7. The system side (multi-step actions, tool use, emergent behaviour, loss of human control) is more sparsely covered: MIT added a multi-agent subdomain in V3/V4, AIUC-1 added explicit agentic-action controls (B.6 "Prevent unauthorized AI agent actions") in its Q2-2026 release. Eticas's merged category with two sub-groups treats both dimensions as parts of the same risk: the relationship between human control and AI autonomy.

## Gaps in current Eticas coverage that future versions could address

The verification work in [external-framework-mapping-verification.md](external-framework-mapping-verification.md) identified concepts that appear in multiple external frameworks but have no Eticas counterpart. These are candidates for v0.4 consideration, in rough priority order:

1. **Socioeconomic and labour-market impacts** — the largest gap. MIT V4 Domain 6 (six subdomains: power centralisation, increased inequality, economic and cultural devaluation, competitive dynamics, governance failure, environmental harm) and OECD recommendation 2.4 are entirely uncovered. Could be a new top-level "Socioeconomic Impact" category or an expansion of Organisational Readiness.

2. **Sector-specific or prohibited use-case risks** — AIUC-1 is weak here, but the EU AI Act (Art. 5 prohibitions, Annex III high-risk lists) and AIR 2024 (advice in heavily regulated industries) name them. A cross-cutting "Prohibited or restricted use cases" sub-group, or sector tags applicable across all categories, would help.

3. **Content-safety harms not captured by Harmful Misuse** — CSAM, non-consensual intimate imagery, self-harm content, defamation, and election integrity are Level-2 categories in AIR 2024 and are named risks in NIST 600-1, EU AI Act, and most corporate policies.

4. **Information integrity / content provenance** — NIST 600-1 #8 and OECD 1.4 (2024 update) both elevate this. Currently only weakly mapped through transparency and reliability.

5. **Multi-agent and emergent risks** — a newly added subdomain in MIT V3/V4. With AIUC-1's focus on agents, this is becoming central.

6. **Value chain / third-party AI** — NIST 600-1 #12, EU AI Act Art. 25, AIUC-1 vendor due-diligence, and ISO/IEC 42001 A.10 all converge here. Currently implicit in Eticas Governance.

7. **AI welfare / rights and competitive dynamics** — speculative but increasingly cited. Treat as candidates for a future "Frontier risks" sub-group rather than core inclusion.

---

*This document is part of the [Eticas AI Risk Taxonomy](../README.md). For the full category definitions, see [TAXONOMY.md](../TAXONOMY.md). For implementation details, see [docs/implementation.md](implementation.md).*
