# External framework alignment

This document maps the Eticas AI Risk Taxonomy against major international AI risk frameworks, standards, and academic taxonomies. It describes where Eticas categories align, where they diverge, and where Eticas addresses risk areas that existing frameworks miss.

## Frameworks covered

| Framework | Type | Scope | Machine-readable |
|-----------|------|-------|-----------------|
| [MIT AI Risk Repository V4](https://airisk.mit.edu) | Academic database | 1,700+ risks across 7 domains, 24 subdomains (Dec 2025) | CSV/Sheets (CC BY 4.0) |
| [NIST AI RMF (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Government framework | 7 trustworthiness characteristics, 4 functions (Jan 2023; revision directed but not published) | PDF only |
| [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Government framework | 12 GenAI-specific risk categories (Jul 2024; revision directed but not published) | PDF only |
| [NIST AI 100-2 E2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) | Government taxonomy | Adversarial ML threat taxonomy (Mar 2025) | PDF only |
| [EU AI Act](https://artificialintelligenceact.eu) | Regulation | Risk tiers, requirements for high-risk AI (Reg. 2024/1689) | Via [W3C DPV extension](https://w3c.github.io/dpv/legal/eu/aiact/) |
| [OECD AI Principles](https://oecd.ai) | International principles | 5 principles (updated May 2024), classification framework, incident monitor | PDF only |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | Management system standard | 38 controls across 9 control objectives | Paid standard, no vocabulary |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | Risk management standard | AI-specific risk management guidance | Paid standard, no vocabulary |
| [W3C DPV v2.3](https://w3c.github.io/dpv/) | Vocabulary family | SKOS/RDFS concepts across AI, Risk, Privacy, EU AI Act (Feb 2026) | RDF (Turtle, JSON-LD, RDF/XML, N3) |
| [AIR 2024](https://arxiv.org/abs/2406.17864) (Zeng et al.) | Academic taxonomy | 4 levels, 314 specific risk types | Paper only |

**Notes on the W3C DPV:** The Data Privacy Vocabulary is broader than its name suggests. Version 2.3 (February 2026) contains 9,982 concepts across multiple extensions: a core privacy vocabulary, an [AI extension](https://w3c.github.io/dpv/2.3/ai/) covering bias types, security attacks, and AI lifecycle, a [Risk extension](https://w3c.github.io/dpv/2.3/risk/) covering risk management, assessment, and a full risk/impact taxonomy (technical, organisational, societal, legal), and an [EU AI Act extension](https://w3c.github.io/dpv/legal/eu/aiact/) encoding the regulation's concepts in RDF. The AIRO and VAIR ontologies (Golpayegani, Pandit, Lewis; ADAPT Centre, Trinity College Dublin) have been formally incorporated into DPV's AI and EU AI Act extensions. **DPV is the only framework in this set that provides production-ready SKOS concept URIs** suitable for formal linking. It is a W3C Community Group Final Specification, not a full W3C Recommendation.

**Notes on NIST:** Both AI 100-1 (RMF) and AI 600-1 (GenAI Profile) are under directed revision following the July 2025 White House AI Action Plan, but no revised versions have been published. The companion NIST AI 100-2 E2025 (Adversarial ML Taxonomy, March 2025) is the most significant NIST taxonomy update since AI 600-1.

**Notes on ISO:** ISO/IEC 42001:2023 has not been revised, but several companion standards were published in 2025: ISO/IEC 42005 (AI impact assessment), ISO/IEC 42006 (requirements for bodies auditing AI management systems), and ISO/IEC 12792 (transparency taxonomy of AI systems). All remain paid, PDF-only, with no machine-readable vocabulary.

## Category-level alignment

The table below shows how each of Eticas's 10 categories maps to its closest equivalent in each framework. Cells indicate the strength of alignment: **close** (same concept, possibly different scope or granularity), **partial** (related but structurally different), or **—** (not addressed). Where a category now contains sub-groups that have their own distinct mappings, these are noted.

| Eticas category | MIT AI Risk Repository | NIST AI 600-1 | NIST AI RMF | EU AI Act | OECD | ISO 42001 | W3C DPV |
|---|---|---|---|---|---|---|---|
| **Bias & Fairness** | Close — Domain 1 (Discrimination & Toxicity) | Close — #6 Harmful Bias & Homogenization | Close — "Fair with Harmful Bias Managed" | Partial — non-discrimination via EU law | Close — Principle 1.2 | Close — A.8 (impact assessment) | Close — `ai:AIBias` |
| **Privacy & Confidentiality** | Close — Subdomain 2.1 | Close — #4 Data Privacy | Close — "Privacy-Enhanced" | Partial — defers to GDPR | Close — Principle 1.2 | Close — A.7 (data management) | Exact — core DPV focus |
| **Reliability** *(now includes Manipulation and Resilience sub-groups)* | Close — Subdomain 7.3 + Domain 3 (Misinformation) | Close — #2 Confabulation + #8 Information Integrity | Close — "Valid & Reliable" + "Secure & Resilient" (resilience part) | Close — Art. 15 (accuracy, resilience) | Close — Principle 1.4 | Partial — lifecycle testing | Close — `ai:Reliability` + `ai:Misinformation` |
| **Governance** | Partial — Subdomain 6.5 | Partial — #12 Value Chain Integration | Close — "Accountable & Transparent" + Govern function | Close — QMS, documentation, oversight | Close — Principle 1.5 | Close — core standard focus | Partial — `dpv:GovernanceProcedures` |
| **Security & Misuse** *(AI-specific, not traditional IT)* | Close — Subdomain 2.2 + Domain 4 | Close — #9 Information Security | Close — "Secure & Resilient" (security part) | Close — Art. 15(5) cybersecurity | Close — Principle 1.4 | Close — A.6 (information security) | Close — `ai:SecurityAttack` |
| **Environmental Impact** | Close — Subdomain 6.6 | Close — #5 Environmental Impacts | — | Partial — Art. 112 (future scope) | Partial — Principle 1.1 (sustainable development) | — | — |
| **Transparency & Explainability** | Close — Subdomain 7.4 | — | Close — "Explainable & Interpretable" | Close — disclosure, user information | Close — Principle 1.3 | Partial — A.5 (documentation) | Close — `ai:Transparency` |
| **Incident Reporting & Redress** | — | — | Partial — within "Accountable & Transparent" | Close — Art. 73 (serious incident reporting) | Close — Principle 1.5 | Partial — stakeholder management | Partial — `dpv:RightToRemedy` |
| **Autonomy & Agency** *(merged; includes Human agency and System autonomy sub-groups)* | Close — Domain 5 (Human-Computer Interaction) + Subdomain 7.6 (Multi-agent) | Close — #7 Human-AI Configuration | — | Close — Art. 14 (human oversight) | — | Partial — Annex C | Close — `ai:HumanOversight` |
| **Organisational Readiness** | — | — | Partial — MAP function (deployment context) | — | Partial — classification framework | Partial — lifecycle management | Partial — Risk ext. (organisational risks) |

## Where Eticas aligns with the consensus

The core categories — Bias & Fairness, Privacy & Confidentiality, Reliability, Governance, Security & Misuse — are well-established across all major frameworks. Every framework addresses them, though with varying granularity and naming. The main variations are structural rather than substantive:

**Naming differences are the primary source of friction.** NIST uses compound names ("Secure & Resilient", "Fair with Harmful Bias Managed"), the MIT Repository uses domain-level labels that don't map 1:1 to Eticas categories (e.g., "Discrimination & Toxicity" bundles bias with toxic content), and the EU AI Act distributes requirements across articles rather than naming risk categories. The taxonomy's `alt_labels` and `skos:closeMatch` links address this by documenting every name variant and its formal equivalent.

**Granularity varies significantly.** Where Eticas defines 12 subcategories under Bias & Fairness (organised into 3 sub-groups), NIST 600-1 has a single category ("Harmful Bias & Homogenization") and the MIT Repository has 3 subdomains. Conversely, NIST's governance structure (the Govern function alone has 17 subcategories) is more detailed than Eticas's Governance category. This is appropriate — Eticas is an audit taxonomy, not a process framework.

**The W3C DPV is the strongest alignment target** for formal linking. It is the only framework that provides concept-level URIs in RDF, covers nearly every Eticas category across its AI, Risk, and EU AI Act extensions, and is actively maintained. DPV's Risk extension includes organisational and societal risk concepts that map to Eticas's Organisational Readiness and Resilience sub-groups — an alignment opportunity that should be explored in detail.

## Where Eticas diverges from or extends existing frameworks

### Categories that most frameworks underserve

**Environmental Impact** is addressed explicitly only by the MIT Repository (Subdomain 6.6) and NIST 600-1 (#5). The EU AI Act mentions it only as a future consideration (Art. 112). ISO standards do not address it. OECD treats it under "sustainable development" at the principle level without operationalising it. Eticas's treatment as an established category with specific subcategories (inference energy, training consumption, hardware efficiency) goes beyond what most frameworks offer.

**Incident Reporting & Redress** (renamed from Responsibility & Redress) has no direct equivalent as a standalone risk category in most frameworks. NIST and OECD address it under accountability. The EU AI Act's Article 73 requires reporting of serious incidents for high-risk systems, but this is a compliance obligation rather than a risk category. Eticas's separation of incident response from governance reflects the operational reality that reporting and remediation processes require distinct assessment.

**Autonomy & Agency** merges two dimensions that frameworks treat inconsistently. The human side (automation bias, over-reliance, deskilling) is addressed by MIT's Domain 5 (Human-Computer Interaction) and NIST 600-1 #7 (Human-AI Configuration), while the system side (multi-step actions, tool use, emergent behaviour) is only sparsely covered — MIT added a multi-agent subdomain in April 2025, and NIST launched an AI Agent Standards Initiative in February 2026 but has not published guidance. Eticas's merged category with two sub-groups (Human agency and System autonomy) treats both dimensions as parts of the same risk: the relationship between human control and AI autonomy.

### Structural differences in Eticas's approach

**Three-level hierarchy with sub-groups.** Most frameworks use either a flat list (NIST 600-1: 12 categories) or a two-level hierarchy (MIT: 7 domains → 24 subdomains). Eticas uses three levels: categories → sub-groups → subcategories. This allows fine-grained risk types to be navigable without flattening them into an unstructured list. For example, Reliability contains four sub-groups (output quality, monitoring & remediation, manipulation & misinformation, resilience) — each with its own set of subcategories and distinct external framework mappings.

**Lifecycle-stage tagging.** Eticas tags every subcategory with the lifecycle stages where it manifests (pre-processing, in-processing, post-processing). Most frameworks either organise by lifecycle stage (NIST MAP/MEASURE/MANAGE) or by risk domain (MIT, NIST 600-1) but not both. The dual tagging allows the same taxonomy to serve both a risk-domain view (for reporting) and a lifecycle view (for audit execution).

**Audit-oriented granularity.** Existing frameworks tend toward either very high-level principles (OECD: 5 principles) or very fine-grained risk inventories (MIT: 1,700+ entries, AIR 2024: 314 risk types). Eticas targets the middle ground — 108 concepts structured at a granularity where each subcategory is auditable (you can write assessment checks for it) but not so granular that the taxonomy becomes an encyclopaedia.

## How Eticas addresses gaps in existing frameworks

### Resilience as a named sub-group under Reliability

The concept of resilience — the ability to absorb disruption, degrade gracefully, and recover — is fragmented across existing frameworks rather than treated as a coherent assessment area.

The EU AI Act's Article 15 uses "resilient" in two places: for robustness (Art. 15(4), "as resilient as possible regarding errors, faults or inconsistencies") and for cybersecurity (Art. 15(5), "resilient against attempts by unauthorised third parties"). NIST pairs resilience with security as a single trustworthiness characteristic ("Secure & Resilient"), defining it as the ability to "maintain functions and structure in the face of internal and external change and degrade safely and gracefully." ISO 22989 defines it separately from robustness and reliability as the "ability to recover operational condition quickly following an incident."

Eticas addresses this by placing resilience as a named sub-group within Reliability, with five specific subcategories: graceful degradation, edge/offline operability, recovery capability, infrastructure dependency, and contextual/ethical resilience. The key conceptual distinction:

| Property | Focus | Question it answers |
|----------|-------|-------------------|
| Reliability | Consistency under normal conditions | "Does it work correctly?" |
| Robustness | Performance under varied conditions | "Does it still work when conditions change?" |
| Resilience | Recovery after disruption | "What happens when it breaks, and can it come back?" |

This is particularly important for AI deployed in conflict zones, humanitarian operations, or critical infrastructure — contexts where standard assumptions about operating conditions do not hold.

### Organisational Readiness as a standalone category

Between 70 and 85% of AI initiatives fail to meet their objectives — and the primary causes are organisational and integration factors, not model performance. No major AI risk taxonomy treats this as a standalone risk domain. The MIT Repository catalogues what can go wrong with AI systems but not what goes wrong when AI meets organisations. NIST's MAP function acknowledges deployment context but doesn't formalise it as a risk type. ISO 42001 mentions interoperability challenges but embeds them within lifecycle management.

Eticas addresses this with Organisational Readiness as a standalone category covering five dimensions: organisational preparedness (governance maturity, staff competency, change management), workflow compatibility (alert fatigue, end-user involvement), deployment sustainability (ongoing maintenance, vendor dependency), institutional absorptive capacity (digital infrastructure, data literacy), and technical interoperability (legacy systems, data pipelines, API conformance).

The evidence base includes well-documented failures where technically capable systems failed in organisational context: IBM Watson for Oncology (US-centric guidelines that didn't transfer internationally), the Epic Sepsis Model (88% false positive rate creating alert fatigue in clinical workflows), and FEMA's AI damage assessment tools (failed in counties lacking data infrastructure). Implementation science frameworks (NASSS, CFIR, RE-AIM) provide validated assessment methods for exactly this kind of risk, yet are almost entirely absent from AI governance discussions.

---

*This document is part of the [Eticas AI Risk Taxonomy](../README.md). For the full category definitions, see [TAXONOMY.md](../TAXONOMY.md). For implementation details, see [docs/implementation.md](implementation.md).*
