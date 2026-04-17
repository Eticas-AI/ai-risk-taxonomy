# Taxonomy decision tracker

This document records structural decisions made about the Eticas AI Risk Taxonomy, their rationale, and any open questions. It serves as institutional memory so future contributors understand *why* the taxonomy is shaped the way it is.

---

## v0.2.0 — Restructuring (April 2026)

### Context

The initial taxonomy (v0.1.0) was synthesised from six Eticas source documents (Unified Risk Taxonomy, RAIA Guide, LLM/ADM methodologies, Career Scoops audit, HR&A project taxonomy) and published with 13 categories, 67 subcategories, and three classification dimensions (inclusion, maturity, perspective). Team review identified several structural issues: too many top-level categories with overlapping scope, classification dimensions that were overly granular, and a flat structure that jumped from category to subcategory without intermediate grouping.

### Decisions made

#### 1. Reduced categories from 13 to 10

**Merged Autonomy & Human Agency + Agentic Risks → Autonomy & Agency.**
Rationale: both deal with AI acting with insufficient human control. The distinction between "the system undermines human agency" and "the system acts autonomously in risky ways" is real but subtle, and maintaining two separate categories — neither of which had subcategories — was not justified. The merged category has two sub-groups (Human agency, System autonomy) that preserve the distinction without top-level fragmentation.

**Moved Manipulation & Misinformation under Reliability as a sub-group.**
Rationale: in existing Eticas audit practice (LLM methodology, Career Scoops audit), manipulation was already assessed alongside reliability under the combined label "Reliability & Manipulation". The framing is that unreliable outputs exist on a spectrum — from hallucination (unintentionally wrong) to manipulation (systematically misleading). There was also concern about overlap with Security & Misuse (intentional manipulation) and Autonomy (manipulative design). Placing it under Reliability with its own sub-group preserves visibility while reducing category count.

**Moved Resilience under Reliability as a sub-group.**
Rationale: resilience was proposed as a standalone category to cover AI deployed in conflict/crisis contexts. However, once organisational readiness was separated into its own category (see below), the remaining resilience subcategories (graceful degradation, recovery, infrastructure dependency, offline operability) were all technical properties of the system — closely related to reliability. The intermediate sub-group level allows resilience to remain a named, findable concept without being top-level.

**Renamed Responsibility & Redress → Incident Reporting & Redress.**
Rationale: the old name overlapped with Governance (which also covers responsibility and accountability). The rename shifts emphasis from "who is responsible" to "what happens when things go wrong" — reporting, escalation, remediation, appeal. This is more actionable and more distinct from Governance. Also aligns with EU AI Act incident reporting requirements.

**Renamed Integration Readiness → Organisational Readiness.**
Rationale: analysis of the subcategories showed that only one (technical interoperability) was purely technical — the rest (workflow compatibility, deployment sustainability, institutional capacity) are fundamentally about the organisation. The new name foregrounds where most AI deployment failures actually happen: organisational factors, not model performance. Technical interoperability is retained as a subcategory since in practice it's driven by organisational decisions (procurement, IT strategy).

#### 2. Added intermediate sub-group level

Rationale: the jump from "Bias & Fairness" (category) to "Sentiment fairness across groups" (subcategory) was too steep. Sub-groups provide navigable intermediate structure — for example, Bias & Fairness now has "Data & representation", "Output quality across groups", and "Performance disparities". This mirrors how other taxonomies handle granularity (MIT AI Risk Repository uses domains → subdomains → risks). Implemented as a new `type: subgroup` in the YAML, rendered as H3 sections on category pages. Not every category needs sub-groups — Environmental Impact (3 subcategories) and Incident Reporting & Redress (3 subcategories) stay flat.

#### 3. Removed inclusion dimension

The v0.1.0 taxonomy classified each category as either `required` (assessed in every audit) or `audit-dependent` (included based on scope). This was removed because in practice, which categories are assessed always depends on the engagement contract. A client requesting a resilience audit won't necessarily want bias assessment included. The distinction was misleading — it suggested a fixed protocol when the reality is always negotiated. Categories can still be presented as "core" vs "extended" in proposals, but this is a presentation choice, not a data property.

#### 4. Simplified maturity to two levels

v0.1.0 had four maturity levels (established, developing, provisional, proposed). This was too fine-grained — the distinction between "developing" and "provisional" required knowing the provenance of each concept (which source document it came from), which is implementation detail rather than useful classification. Simplified to:

- **Established** — clear methods, shared across the profession, used in multiple audits
- **Emerging** — important but methods still developing

The old maturity assignments mapped as: established → established; developing, provisional, proposed → emerging.

#### 5. Kept perspective as metadata, removed from page display

The `perspective` field (rights & ethics, technical soundness, governance & compliance, operational viability) was introduced to address a question about how to frame risk categories for clients. It was removed from the browsable site's badge display because it added visual clutter alongside the maturity badge, and because the grouping may need to vary by client or sector. The field remains in the YAML and SKOS output so it can be queried programmatically — for example, when generating a proposal that groups categories by client concern. TAXONOMY.md includes a "Client perspective" table showing the grouping as a presentation aid.

#### 6. Reframed Security & Misuse as AI-specific

The Security & Misuse category definition was updated to make explicit that it covers AI-specific security risks (adversarial inputs, prompt injection, model extraction, jailbreaking, AI supply-chain risks) rather than traditional IT security (penetration testing, access controls, encryption). This positions Eticas's assessment as complementary to standard IT security audits rather than competing with them.

#### 7. Added Human-AI interaction subcategories

The merged Autonomy & Agency category includes new subcategories for risks at the human-AI interface: automation bias, trust calibration, deskilling, and over-reliance. These were identified as a gap — the MIT AI Risk Repository covers them under Domain 5 (Human-Computer Interaction), but the v0.1.0 Eticas taxonomy had no home for them. They sit under a "Human agency" sub-group alongside the "System autonomy" sub-group (multi-step actions, tool use, emergent behaviour, loss of human control).

#### 8. Added Manipulation & Misinformation subcategories

The v0.1.0 Manipulation & Misinformation category had no subcategories. Now that it's a sub-group under Reliability, three subcategories were added: disinformation generation, behavioural manipulation, and synthetic media abuse. These are drawn from the Unified Risk Taxonomy's original sub-risks list.

### Open items

- **Public/private layer for SKOS files**: if the repo is made private, filtered SKOS files (categories + sub-groups only) should be generated and served alongside the public pages on GitHub Pages (`risk/taxonomy.ttl`, `risk/taxonomy.jsonld`). The `dist/` folder in the private repo keeps the full internal version with all subcategories. Same build pipeline, two outputs: `generate_pages.py` already filters what pages are generated; the SKOS generation in `convert.py` needs a similar filter that produces a `taxonomy-public.ttl` with only category and subgroup concepts. The public SKOS files are the ones that would eventually be served via content negotiation on `taxonomy.eticas.ai`.
- **References field**: agreed to add a `references` field for key papers, benchmarks, and regulatory sources per concept. YAML structure designed but not yet populated. Will be filled as part of the coordination with the methodology team.
- **Automated literature scanning**: agreed in principle to implement a monthly GitHub Action that searches for recent publications relevant to each category and opens a pull request adding the candidates as `references` entries in the YAML. The team reviews the PR, removes irrelevant entries, and merges — deleting what you don't want is easier than adding what you do. The CI validates the YAML before merge so nothing breaks. Implement after the references field is populated with an initial manual pass.
- **External framework alignment document**: needs updating to reflect the 10-category structure and the new sub-groups. The W3C DPV Risk Extension's organisational and societal risk sections should be explored for mapping to Organisational Readiness and Resilience subcategories.
- **Sub-group definitions**: some sub-group definitions are placeholder-quality and need refinement by the methodology team.
- **Governance sub-groups**: resolved — merged "task success" into "fitness for purpose", now called "Fitness for purpose and task effectiveness" under Compliance & process. The merged concept covers both the ex ante question (was this designed for this problem?) and the ex post question (does it actually work?). Governance now has 12 subcategories across 4 sub-groups. "Data & oversight" sub-group has 2 items (data governance, human oversight and control).

---

## v0.1.0 — Initial publication (April 2026)

### Context

Risk categories existed across multiple Eticas documents with inconsistent names and definitions. The taxonomy project consolidated them into a single source of truth.

### Key decisions

- **Source consolidation**: categories extracted from 6 documents, with naming discrepancies recorded as `alt_labels` (e.g., "Fairness" in the URT became an alias of "Bias & Fairness")
- **SKOS as the data model**: chosen for interoperability with the W3C DPV and other AI risk vocabularies being published as linked data
- **GitHub as the platform**: version control, pull request review, automated CI/CD, and GitHub Pages for the browsable site
- **YAML as the source format**: human-editable, with automated conversion to SKOS Turtle and JSON-LD
- **Maturity based on provenance**: concepts from the URT (used across multiple documents) were tagged as established; concepts from the RAIA Guide or validated in Career Scoops as developing; concepts from the HR&A taxonomy only as provisional
- **Namespace**: `https://taxonomy.eticas.ai/risk/` on a domain Eticas controls, so URIs survive hosting changes
