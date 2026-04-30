# Taxonomy decision tracker

This document records structural decisions made about the Eticas AI Risk Taxonomy, their rationale, and any open questions. It serves as institutional memory so future contributors understand *why* the taxonomy is shaped the way it is.

---

## v0.3.0 — Refinement based on Usman's review (April–May 2026)

### Context

Usman did a detailed review of the v0.2.0 taxonomy (April 29, 2026). Main feedback: (1) some subcategories describe *mechanisms* or *causes* rather than *risks* — e.g., "dataset bias" explains how disparate impact occurs but is not a risk in itself; (2) cross-cutting overlaps remain between categories; (3) several structural moves proposed. Gemma responded with general agreement and one specific pushback on Manipulation & Misinformation placement.

📋 **Concept-by-concept mapping from v0.2 to v0.3:** [docs/v0.2-to-v0.3-mapping.md](docs/v0.2-to-v0.3-mapping.md)

📋 **External framework mapping verification (Phase 5 working document):** [docs/external-framework-mapping-verification.md](docs/external-framework-mapping-verification.md) — comprehensive review of mappings across 10 frameworks (NIST RMF, NIST 600-1, EU AI Act, MIT V4, W3C DPV, ISO 42001, OECD, plus newly added AIUC-1, AIR 2024, IBM Risk Atlas) with gap analysis. Draft for team review before applying to YAML.

### Decisions

#### Adopt Usman's restructured taxonomy as the base

After review, the team agreed to adopt Usman's proposal as the base for v0.3, with a few specific adjustments documented below. The mapping document captures all the concept-by-concept changes; this section records the rationale for the structural choices.

#### Distinguish risks from mechanisms

Several v0.2 concepts (most notably under Bias & Fairness) described how a risk happens rather than the risk itself. With LLMs in particular, "dataset bias" cannot be measured directly — what is observed is its effect (disparate impact). The decision was to:

- Restructure Bias & Fairness around three sub-groups (Outcome disparities, Representational harm, Dynamic & Systemic bias) that describe risks, not causes.
- Preserve mechanism-level concepts (dataset bias, proxy discrimination, etc.) by moving them to a new `operationalisation` field on the parent risk concept. This field will later be enriched with metrics, methods, etc. (Gemma's proposed methodology layer).
- Distinguish this from concepts that are simply being eliminated (no longer recognised as risks), which will be marked `status: retired` so they remain in the YAML for institutional memory but do not generate pages or appear in outputs.

#### Manipulation & Misinformation: distinguish intent from output

Usman proposed moving the entire Manipulation & Misinformation sub-group to Security & Misuse (renamed "Harmful and Malicious Misuse"). Gemma pushed back: she sees misinformation as often resulting from hallucination, not adversarial engagement.

The key distinction is *who causes the harmful output*:
- **Misuse** — a human actor deliberately uses the model for a harmful purpose. The model works correctly; the problem is who uses it and for what.
- **Hallucination** — the model produces false information on its own, without anyone seeking it. The problem is what the system produces.

The non-adversarial case Gemma describes is already covered by `hallucination` under Reliability / Output quality. The remaining subcategories (behavioural manipulation, synthetic media abuse) all imply intent and therefore belong in Security & Misuse. `disinformation-generation` is dropped as a subcategory — it is redundant with hallucination when non-intentional, and falls under misuse when intentional.

#### Dissolve Incident Reporting & Redress

The category is dissolved. Each of its three subcategories has a natural home elsewhere: `absence-of-appeal` and `ineffective-communication` are absorbed into the new "Right to explanation & contestation" subcategory in Transparency; `unclear-remediation` is absorbed into `failure-remediation-gaps` under Governance / Compliance & process. EU AI Act Art. 73 obligations on serious incident reporting are covered by `incident-response-gaps` under Governance.

This contradicts an earlier decision (the rename from "Responsibility & Redress" to "Incident Reporting & Redress" was Gemma's suggestion in v0.2), but Gemma agreed with Usman's revised proposal. The reason for keeping it earlier was that no clear destinations existed for its subcategories — once Usman provided coherent destinations across Governance and Transparency, the case for keeping it as a standalone category became weaker.

#### Other structural changes

- **Monitoring & remediation** moves entirely from Reliability to Governance / Compliance & process. Reliability focuses on technical aspects of the system; monitoring and remediation are governance processes about how the organisation watches the system over time.
- **Governance / Data & oversight** is dissolved: `human-oversight-control` moves to Accountability, `data-governance` moves to Compliance & process.
- **Security & Misuse** gains a new "Harmful Misuse" sub-group (absorbing the moved Manipulation subcategories and `misuse-beyond-intended-purpose`), and adds `model-extraction` and `data-poisoning` to AI-specific attacks.
- **Transparency / Explainability** gains a new "Right to explanation & contestation" subcategory (covering GDPR Art. 22 and EU AI Act Art. 13). `prompt-transparency` and `model-card-completeness` are dropped as risks — the team agreed they are documentation requirements rather than risks per se.

### Other agreed changes (from Gemma's email thread)

#### Separate compliance mappings from taxonomy mappings

Gemma asked for framework mappings to be split: regulatory/compliance frameworks (EU AI Act, ISO 42001, NIST, OECD) separate from taxonomy/vocabulary frameworks (W3C DPV, MIT AI Risk Repository). This makes it clearer for the client-facing use case ("this audit covers Section X of ISO 42001"). Implement as either two separate tables on pages, or a categorisation field on each mapping entry in the YAML.

#### Remove match types from public pages

Usman proposed removing "broad match" / "close match" etc. from the public GitHub Pages. Keep them in the YAML/SKOS for internal use. Aligns with the public/private split already planned.

### Open items for implementation

See [docs/v0.2-to-v0.3-mapping.md](docs/v0.2-to-v0.3-mapping.md) for the full list of items requiring work during implementation (definitions to update, new subcategory definitions, operationalisation field design, retired status implementation, external framework mappings review).

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
- **External framework alignment document**: resolved — fully rewritten for 10-category structure. Factual corrections applied: EU AI Act serious incident reporting is Article 73 (not 62, which was the draft-stage number); MIT Repository updated to V4 (December 2025); AIRO/VAIR formally incorporated into W3C DPV v2.3 (February 2026); OECD "information integrity" clarified as sub-provisions in Principles 1.2 and 1.4, not a new principle; DPV noted as Community Group Final Specification (not a full W3C Recommendation). Added references to NIST AI 100-2 E2025 (Adversarial ML Taxonomy), ISO/IEC 42005/42006/12792:2025, and Digital Omnibus timeline implications.
- **Mapping corrections in YAML**: Article 62 → Article 73 fixed in incident-reporting-redress mappings. MIT Domain 5 label corrected for autonomy-agency.
- **DPV Risk Extension deep mapping**: the DPV Risk Extension's organisational and societal risk concept hierarchies should be explored for detailed subcategory-level mapping to Organisational Readiness and Resilience sub-groups. This is an opportunity for the coordination with the methodology team.
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
