# External framework alignment

This document maps the Eticas AI Risk Taxonomy against major international AI risk frameworks, standards, and academic taxonomies. It describes where Eticas categories align, where they diverge, and where Eticas addresses risk areas that existing frameworks miss.

## Frameworks covered

| Framework | Type | Scope | Machine-readable |
|-----------|------|-------|-----------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Academic database | 1,725 risks across 7 domains, 24 subdomains | CSV/Sheets (CC BY 4.0) |
| [NIST AI RMF (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Government framework | 7 trustworthiness characteristics, 4 functions, 66 subcategories | PDF only |
| [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) | Government framework | 12 GenAI-specific risk categories | PDF only |
| [EU AI Act](https://artificialintelligenceact.eu) | Regulation | Risk tiers, requirements for high-risk AI | Via [W3C DPV extension](https://w3c.github.io/dpv/legal/eu/aiact/) |
| [OECD AI Principles](https://oecd.ai) | International principles | 5 principles, classification framework, incident taxonomy | PDF only |
| [ISO/IEC 42001](https://www.iso.org/standard/81230.html) | Management system standard | 39 controls across 10 domains | Paid standard, no vocabulary |
| [ISO/IEC 23894](https://www.iso.org/standard/77304.html) | Risk management standard | AI-specific risk management guidance | Paid standard, no vocabulary |
| [W3C DPV AI Extension](https://w3c.github.io/dpv/2.3/ai/) | Vocabulary | SKOS/RDFS concepts for AI risks, lifecycle, attacks | RDF (Turtle, JSON-LD) |
| [AIRO / VAIR](https://w3id.org/airo) | Ontology / vocabulary | OWL ontology + SKOS vocabulary for AI risks | OWL, SKOS |
| [AIR 2024](https://arxiv.org/abs/2406.17864) (Zeng et al.) | Academic taxonomy | 4 levels, 314 specific risk types | Paper only |

## Category-level alignment

The table below shows how each Eticas category maps to its closest equivalent in each framework. Cells indicate the strength of alignment: **exact** (same concept, same scope), **close** (same concept, different scope or granularity), **partial** (related but structurally different), or **—** (not addressed).

| Eticas category | MIT AI Risk Repository | NIST AI 600-1 | NIST AI RMF | EU AI Act | OECD | ISO 42001/23894 | W3C DPV |
|---|---|---|---|---|---|---|---|
| **Bias & Fairness** | Close — Domain 1 (Discrimination & Toxicity) covers bias but bundles it with toxic content | Close — #6 Harmful Bias & Homogenization | Close — "Fair with Harmful Bias Managed" | Partial — non-discrimination via external EU law; no standalone fairness requirement | Close — Principle 1.2 (fairness) | Close — Annex A.8 (impact assessment) | Close — `ai:AIBias` hierarchy |
| **Privacy & Confidentiality** | Close — Subdomain 2.1 (Compromise of privacy) | Close — #4 Data Privacy | Close — "Privacy-Enhanced" | Partial — defers to GDPR | Close — Principle 1.2 (privacy) | Close — Annex A.7 (data management) | Exact — core DPV focus |
| **Reliability** | Close — Subdomain 7.3 (Lack of capability/robustness) | Close — #2 Confabulation (narrower, LLM-specific) | Close — "Valid & Reliable" | Exact — Art. 15 (accuracy) | Close — Principle 1.4 (robustness) | Partial — general lifecycle testing | Close — `ai:Reliability` |
| **Governance** | Partial — Subdomain 6.5 (Governance failure, societal focus) | Partial — #12 Value Chain Integration (narrower) | Close — "Accountable & Transparent" + Govern function | Close — QMS, documentation, oversight requirements | Close — Principle 1.5 (accountability) | Exact — core standard focus | Partial — `dpv:GovernanceProcedures` |
| **Security & Misuse** | Close — Subdomain 2.2 + Domain 4 (split across two domains) | Close — #9 Information Security | Close — "Secure & Resilient" | Close — Art. 15(5) cybersecurity | Close — Principle 1.4 (security) | Close — Annex A.6 (information security) | Close — `ai:SecurityAttack` |
| **Environmental Impact** | Close — Subdomain 6.6 (Environmental harm) | Close — #5 Environmental Impacts | — not addressed | Partial — Art. 112 mentions future scope | Partial — Principle 1.1 (sustainable development) | — not addressed | — not addressed |
| **Transparency & Explainability** | Close — Subdomain 7.4 (Lack of transparency) | — no standalone category | Close — "Explainable & Interpretable" | Close — chatbot/deepfake disclosure, user info | Close — Principle 1.3 | Partial — Annex A.5 (documentation) | Close — `ai:Transparency` |
| **Responsibility & Redress** | — not a standalone domain | — | Partial — within "Accountable & Transparent" | Close — consumer redress in Colorado AI Act | Close — Principle 1.5 (accountability) | Partial — general stakeholder management | Partial — `dpv:RightToRemedy` |
| **Autonomy & Human Agency** | Close — Subdomain 5.2 (Loss of agency) | Close — #7 Human-AI Configuration | — | Partial — Art. 14 human oversight | — | Partial — human-AI interaction in Annex C | Partial — `ai:HumanOversight` |
| **Agentic Risks** | Close — Subdomain 7.6 (Multi-agent, added April 2025) | — | — | — | — | — | — |
| **Manipulation & Misinformation** | Close — Domain 3 (Misinformation) + Subdomain 4.1 | Close — #8 Information Integrity | — | Partial — subliminal manipulation banned; deepfake disclosure | Partial — 2024 update added information integrity | — | Close — `ai:Misinformation` |
| **Resilience** *(proposed)* | — | — (embedded in "Secure & Resilient") | Partial — within "Secure & Resilient" | Partial — Art. 15(4) "as resilient as possible" | — (embedded in incident taxonomy) | — | — |
| **Integration Readiness** *(proposed)* | — | — | Partial — MAP function mentions deployment context | — | Partial — classification framework covers context | Partial — lifecycle management | — |

## Where Eticas aligns with the consensus

The core five categories — Bias & Fairness, Privacy & Confidentiality, Reliability, Governance, Security & Misuse — are well-established across all major frameworks. Every framework addresses them, though with varying granularity and naming. The main variations are structural rather than substantive:

**Naming differences are the primary source of friction.** NIST uses compound names ("Secure & Resilient", "Fair with Harmful Bias Managed"), the MIT Repository uses domain-level labels that don't map 1:1 to Eticas categories (e.g., "Discrimination & Toxicity" bundles bias with toxic content), and the EU AI Act distributes requirements across articles rather than naming risk categories. The taxonomy's `alt_labels` and `skos:closeMatch` links address this by documenting every name variant and its formal equivalent.

**Granularity varies significantly.** Where Eticas defines ~12 subcategories under Bias & Fairness, NIST 600-1 has a single category ("Harmful Bias & Homogenization") and the MIT Repository has 3 subdomains. Conversely, NIST's governance structure (the Govern function alone has 17 subcategories) is more detailed than Eticas's current Governance subcategories. This is appropriate — Eticas is an audit taxonomy, not a process framework.

**The W3C DPV AI Extension is the strongest alignment target** for formal linking. It is the only framework that provides concept-level URIs in RDF, covers nearly every Eticas category, and is actively maintained by a standards body. DPV's AI extension includes concepts for specific bias types (algorithmic selection bias, data aggregation bias, automation bias), security attacks (data poisoning, prompt injection, model inversion), and lifecycle stages that map directly to Eticas's pre/in/post-processing structure.

## Where Eticas diverges from or extends existing frameworks

### Categories that most frameworks underserve

**Environmental Impact** is addressed explicitly only by the MIT Repository (Subdomain 6.6) and NIST 600-1 (#5). The EU AI Act mentions it only as a future consideration (Art. 112). ISO standards do not address it. OECD treats it under "sustainable development" at the principle level without operationalising it. Eticas's inclusion of this as an established category with specific subcategories (inference energy, training consumption, hardware efficiency) goes beyond what most frameworks offer.

**Responsibility & Redress** has no direct equivalent as a standalone risk category in any of the major frameworks. NIST and OECD address it under accountability. The EU AI Act's strongest treatment is in the Colorado AI Act, not the EU Act itself. The RAIA Guide's decision to include it as a separate post-processing category is a distinctive design choice.

**Agentic Risks** is the newest and most sparsely covered category. MIT added a multi-agent subdomain only in April 2025. NIST announced an AI Agent Standards Initiative in February 2026 but has not published guidance. No other framework addresses compound AI system risks, multi-step autonomous action, or tool-use chains as a distinct risk domain. Eticas's early inclusion — even as provisional — positions the taxonomy ahead of the field.

### Structural differences in Eticas's approach

**Lifecycle-stage tagging.** Eticas tags every subcategory with the lifecycle stages where it manifests (pre-processing, in-processing, post-processing). This is unusual — most frameworks either organise by lifecycle stage (RAIA Guide, NIST MAP/MEASURE/MANAGE) or by risk domain (MIT, NIST 600-1) but not both simultaneously. The dual tagging allows the same taxonomy to serve both a risk-domain view (for reporting) and a lifecycle view (for audit execution).

**Audit-oriented granularity.** Existing frameworks tend toward either very high-level principles (OECD: 5 principles) or very fine-grained risk inventories (MIT: 1,725 entries, AIR 2024: 314 risk types). Eticas targets the middle ground — ~70 concepts structured at a granularity where each subcategory is auditable (you can write assessment checks for it) but not so granular that the taxonomy becomes an encyclopaedia. This "audit-ready" level of abstraction is a deliberate design choice.

**Two-dimensional classification (inclusion × maturity).** No external framework classifies its own risk categories by both whether they must be assessed and how mature they are. This is an Eticas-specific feature that reflects the reality of a growing taxonomy used in production audits.

## Two gaps that no framework addresses adequately

### Resilience as a unified audit dimension

The concept of resilience — the ability to absorb disruption, degrade gracefully, and recover — is fragmented across existing frameworks rather than treated as a coherent risk category.

The EU AI Act's Article 15 uses "resilient" in two places: for robustness (Art. 15(4), "as resilient as possible regarding errors, faults or inconsistencies") and for cybersecurity (Art. 15(5), "resilient against attempts by unauthorised third parties"). NIST pairs resilience with security as a single trustworthiness characteristic ("Secure & Resilient"), defining it as the ability to "maintain functions and structure in the face of internal and external change and degrade safely and gracefully." ISO 22989 defines it separately from robustness and reliability as the "ability to recover operational condition quickly following an incident."

Despite these definitions, no framework offers a unified resilience category with auditable subcategories. This matters particularly for AI deployed in conflict zones, humanitarian operations, or critical infrastructure — contexts where standard assumptions about operating conditions (reliable connectivity, stable infrastructure, cooperative environments) do not hold. The ICRC's work on AI in armed conflict, the Rohingya biometric data scandal, and military AI stress-testing frameworks all demonstrate that resilience failures in these contexts can have life-or-death consequences.

The key conceptual distinction that an audit framework needs:

| Property | Focus | Question it answers |
|----------|-------|-------------------|
| Reliability | Consistency under normal conditions | "Does it work correctly?" |
| Robustness | Performance under varied conditions | "Does it still work when conditions change?" |
| Resilience | Recovery after disruption | "What happens when it breaks, and can it come back?" |

Eticas's existing Reliability category covers the first and partly the second. A Resilience category would cover the third — including graceful degradation, fallback mechanisms, recovery procedures, infrastructure dependency, and safeguards against function creep or weaponisation.

### Integration readiness as an operational risk dimension

Between 70 and 85% of AI initiatives fail to meet their objectives — and the primary causes are organisational and integration factors, not model performance. No major AI risk taxonomy treats this as a standalone risk domain. The MIT Repository catalogues what can go wrong with AI systems but not what goes wrong when AI meets organisations. NIST's MAP function acknowledges deployment context but doesn't formalise integration risk. ISO 42001 mentions interoperability challenges but embeds them within lifecycle management.

The evidence base for this gap is extensive:

**IBM Watson for Oncology** spent an estimated $4–5 billion and failed primarily because it was trained on US-centric guidelines that didn't transfer to India, Thailand, or South Korea; because it used hypothetical rather than real patient data; and because clinicians distrusted its opaque reasoning. The technology worked — the integration didn't.

**The Epic Sepsis Model** achieved 76–83% accuracy in development but only 0.63 AUC in external validation, with 88% false positive rates creating alert fatigue that degraded rather than improved clinical care. The model's performance was secondary to its integration failure — it didn't fit clinical workflows.

**FEMA's AI damage assessment tools** failed in smaller counties lacking modern data infrastructure or trained personnel — technically capable systems deployed into contexts without the capacity to absorb them.

Implementation science — developed over decades in health services research — provides validated frameworks for assessing exactly this kind of risk (NASSS, CFIR, RE-AIM), yet these are almost entirely absent from AI governance discussions. A 2022 analysis found that 85.6% of AI evaluations focus on model capability, while only 5.3% assess human interaction and 9.1% examine systemic factors.

An Integration Readiness category would cover organisational preparedness (governance maturity, staff competency, change management), technical integration (legacy system compatibility, data interoperability, monitoring infrastructure), sociotechnical fit (workflow compatibility, end-user adoption, context transferability), and deployment sustainability (maintenance capacity, vendor dependency, cost-effectiveness).

## Implications for the taxonomy

Both resilience and integration readiness represent risk areas where Eticas's practical audit experience — particularly in humanitarian, health, and crisis contexts — can inform categories that the broader AI governance ecosystem has not yet formalised. Including them as emerging/provisional categories would position the taxonomy ahead of NIST, ISO, and the EU AI Act on two of the most consequential sources of real-world AI failure.

The formal SKOS links to existing frameworks documented in the [category-level mapping table](../TAXONOMY.md#category-level-mapping-table) ensure that where Eticas's categories align with established concepts, the alignment is explicit and machine-readable. Where they don't — as with resilience and integration readiness — the taxonomy documents the gap itself, serving as both an audit tool and a contribution to the evolving international vocabulary of AI risk.

---

*This document is part of the [Eticas AI Risk Taxonomy](../README.md). For the full category definitions, see [TAXONOMY.md](../TAXONOMY.md). For implementation details, see [docs/implementation.md](implementation.md).*
