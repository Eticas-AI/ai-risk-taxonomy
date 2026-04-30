# Eticas AI Risk Taxonomy

**Version:** 0.3.0  
**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**License:** CC BY 4.0  
**Maintained by:** [Eticas](https://eticas.ai)

## About this taxonomy

This is Eticas' unified AI risk taxonomy — a structured, machine-readable vocabulary of risk categories used across all of Eticas' audit methodologies, assessment frameworks, and reporting outputs.

Each concept in the taxonomy has a stable URI, a canonical definition, and formal links to equivalent or related concepts in major international frameworks. The taxonomy is published as a SKOS (Simple Knowledge Organization System) vocabulary, making it interoperable with knowledge graphs, linked data systems, and semantic web tools.

## Taxonomy structure

The taxonomy is organised in three levels:

- **Categories** — top-level risk areas (e.g., Bias & Fairness, Reliability)
- **Sub-groups** — intermediate groupings within a category (e.g., "Output quality" within Reliability)
- **Subcategories** — specific risk types (e.g., Hallucination, Output drift)

Not every category has sub-groups. Categories with few subcategories (e.g., Environmental Impact, Organisational Readiness) keep a flat structure.

Each concept carries the following metadata:

| Field | Description |
|-------|-------------|
| `id` | Stable identifier (e.g., `bias-fairness`, `hallucination`) |
| `uri` | Persistent URI under `https://taxonomy.eticas.ai/risk/` |
| `label` | Canonical English label |
| `alt_labels` | Alternative labels / synonyms used in Eticas documents |
| `definition` | Prose definition |
| `scope` | Applicability: `ADM`, `LLM`, or `ALL` |
| `maturity` | How developed the concept is: `established` or `emerging` |
| `status` | `active` or `retired` (retired concepts are preserved for institutional memory but not rendered) |
| `perspective` | (Categories only) Which client concern the category addresses |
| `lifecycle_stages` | Where in the AI lifecycle this risk manifests |
| `operationalisation` | List of mechanisms or aids used to assess the risk (will eventually carry metrics and methods) |
| `mappings` | External equivalences to ten frameworks across compliance, reference, and taxonomy buckets |

## Maturity

Each category and subcategory is classified as either **established** or **emerging**:

**Established** — Stable definition, well-developed subcategories, proven assessment methods, and strong mappings to external frameworks. Changes are made carefully.

**Emerging** — Recognised as important, but definitions may evolve, subcategories are being refined, and assessment methods are still developing. Findings referencing emerging concepts should note this status.

An emerging concept becomes established as definitions stabilise, assessment methods are tested in audits, and the profession develops shared practice. These are team decisions documented in the changelog.

## Risks vs mechanisms

A core distinction in v0.3 is between *risks* (what can go wrong) and *mechanisms* (how a risk arises or is observed). Mechanisms — such as dataset bias, proxy discrimination, model card incompleteness, or absence of an appeal process — are not standalone subcategories in the taxonomy. They live as `operationalisation` entries on the parent risk concept they help assess. This keeps the risk hierarchy clean and creates a designated home for the methodology layer (metrics, methods, evidence pointers) being developed in parallel.

## Client perspective

When presenting the taxonomy to clients, categories can be grouped by the concern they address:

| Perspective | Question it answers | Categories |
|-------------|-------------------|------------|
| Rights & ethics | Does the system respect people? | Bias & Fairness, Privacy & Confidentiality, Autonomy & Agency |
| Technical soundness | Does the system work correctly and safely? | Reliability, Security & Misuse, Environmental Impact |
| Governance & compliance | Is it properly managed and legally compliant? | Governance, Transparency & Explainability |
| Operational viability | Will it deliver value in context? | Organisational Readiness |

This grouping is a presentation aid, not a formal classification. Categories may be grouped differently for specific clients or sectors.

## Risk categories

Each category links to a detailed page with sub-groups, subcategories, definitions, and mappings to external frameworks. Browse all categories at the [taxonomy site](https://eticas-ai.github.io/ai-risk-taxonomy/risk/).

**[Bias & Fairness](risk/bias-fairness.md)** — The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes. *(3 sub-groups, 8 subcategories)*

**[Privacy & Confidentiality](risk/privacy-confidentiality.md)** — The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data, or that sensitive information is exposed without authorization. *(3 sub-groups, 8 subcategories)*

**[Reliability](risk/reliability.md)** — The risk that an AI system produces unreliable, fabricated, or out-of-distribution outputs, or cannot recover from disruption. *(2 sub-groups, 9 subcategories)*

**[Governance](risk/governance.md)** — The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use. *(3 sub-groups, 15 subcategories)*

**[Security & Misuse](risk/security-misuse.md)** — The risk that an AI system is exposed to AI-specific vulnerabilities, attacks, or deliberate misuse. Covers risks beyond traditional IT security, including adversarial inputs, prompt injection, model extraction, data poisoning, behavioural manipulation, and synthetic media abuse. *(3 sub-groups, 10 subcategories)*

**[Environmental Impact](risk/environmental-impact.md)** — The risk that an AI system's development, deployment, or use causes negative environmental effects. *(3 subcategories)*

**[Transparency & Explainability](risk/transparency-explainability.md)** — The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs. Includes the right to explanation and contestation for affected individuals. *(2 sub-groups, 4 subcategories)*

**[Autonomy & Agency](risk/autonomy-agency.md)** — The risk that an AI system undermines human agency or operates with insufficient human control. Includes both human-side risks (automation bias, over-reliance) and system-side risks (multi-step actions, tool use, emergent behaviour). *(2 sub-groups, 8 subcategories)*

**[Organisational Readiness](risk/organisational-readiness.md)** — The risk that an AI system fails to deliver value because it does not fit the organisational, technical, or human context into which it is deployed. *(5 subcategories)*

---

## Alignment with external frameworks

The taxonomy is formally linked to ten major international frameworks using SKOS mapping properties (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`). Mappings are organised in three buckets:

| Bucket | Frameworks | Purpose |
|--------|------------|---------|
| **Compliance** | EU AI Act, ISO/IEC 42001, AIUC-1 | Legally binding regulations or directly certifiable standards. Used to demonstrate adherence to obligations |
| **Reference** | NIST AI RMF, NIST AI 600-1, OECD AI Principles | Policy frameworks and principles; soft-law but commonly cited by regulators and clients |
| **Taxonomy** | MIT AI Risk Repository V4, AIR 2024, IBM AI Risk Atlas, W3C DPV v2.3 | Academic taxonomies, vendor research, and SKOS/OWL vocabularies. Used for conceptual interoperability |

Each category page lists its mappings grouped by bucket. For a detailed analysis of how each Eticas category aligns with, diverges from, and extends these frameworks — including coverage gaps and areas where Eticas addresses risks that existing frameworks miss — see **[External framework alignment](docs/external-framework-alignment.md)**. The full research record behind v0.3's mappings is in **[External framework mapping verification](docs/external-framework-mapping-verification.md)**.

---

## Versioning and governance

The taxonomy follows [Semantic Versioning](https://semver.org/):

- **Major** (X.0.0): Breaking changes — categories removed or fundamentally redefined
- **Minor** (0.X.0): New categories or subcategories added; maturity changes; new external mappings
- **Patch** (0.0.X): Definition refinements, typo fixes, additional alternative labels

Changes are proposed via GitHub Issues, discussed with the team, and merged via pull requests. Every release is tagged and produces a timestamped snapshot of all output formats (Turtle, JSON-LD, HTML).

---

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.3.0).
https://taxonomy.eticas.ai/risk/
```

---

*This taxonomy is maintained by Eticas and published under CC BY 4.0. Contributions and alignment suggestions are welcome via GitHub Issues.*
