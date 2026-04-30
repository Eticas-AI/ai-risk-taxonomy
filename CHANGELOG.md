# Changelog

All notable changes to the Eticas AI Risk Taxonomy are documented here.

The taxonomy follows [Semantic Versioning](https://semver.org/):
- **Major** (X.0.0) — breaking changes: categories removed or fundamentally redefined
- **Minor** (0.X.0) — new categories or subcategories added, structural changes, new external mappings
- **Patch** (0.0.X) — definition refinements, typo fixes, additional alternative labels

Change types use the following categories, inspired by the [AIUC-1 changelog model](https://www.aiuc-1.com/changelog):
- **Addition** — new concept introduced
- **Revision** — substantive change to an existing concept
- **Clarification** — wording improved without changing meaning
- **Specification** — scope or applicability refined
- **Retired** — concept removed or merged into another

---

## [0.3.0] — 2026-05-01

Refinement based on Usman's review (April 29, 2026) and Gemma's email-thread proposals. The structural simplification reduces categories from 10 to 9, introduces a separation between *risks* and the *mechanisms* through which they manifest, splits framework mappings into compliance / reference / taxonomy buckets, and dramatically expands the external framework mappings (316 new entries, 10 frameworks total). The full rationale for each structural decision is recorded in [TRACKER.md](TRACKER.md).

### Summary

- Categories: **10 → 9** (Incident Reporting & Redress dissolved into Governance and Transparency)
- Sub-groups: **21 → 18**
- Active subcategories: **77 → 70** (some retired or absorbed as operationalisation; new ones added)
- Retired concepts: **0 → 20** (preserved with `status: retired` for institutional memory)
- New `operationalisation` field on parent risks (mechanisms preserved, not retired)
- New `status` field on every concept (`active` / `retired`)
- Public/private split: filtered SKOS files for the public site (`taxonomy-public.ttl`, ~22 pages) alongside the full internal version (`taxonomy.ttl`, ~97 pages)
- External framework mappings: **316 new entries** added; **10 total frameworks** (added AIUC-1, AIR 2024, IBM AI Risk Atlas; removed AIRO and VAIR after their incorporation into DPV v2.3)
- Mappings now grouped on rendered pages by framework type (compliance / reference / taxonomy) per Gemma's request

### Structure

| Change | Type | Affected concepts | Notes |
|--------|------|-------------------|-------|
| Restructured Bias & Fairness | Revision | bias-fairness | Three new sub-groups: Outcome disparities, Representational harm, Dynamic & Systemic bias. The previous sub-groups (Data & representation, Output quality, Performance disparities) were dissolved. Concepts that described mechanisms (dataset bias, proxy discrimination, allocation of opportunity, accessibility barriers, intersectional unfairness, quality of service disparity) are preserved as `operationalisation` entries on `disparate-impact-protected-groups` and `performance-equity` rather than as standalone subcategories |
| Added `homogenization-output-across-groups` subcategory | Addition | bias-representational-harm | New subcategory under Representational harm. ExactMatch with NIST 600-1 #6 homogenization clause |
| Dissolved Incident Reporting & Redress | Retired | incident-reporting-redress | The category and its three subcategories (`absence-of-appeal`, `ineffective-communication`, `unclear-remediation`) are dissolved. The first two are absorbed into the new `right-to-explanation-contestation` subcategory under Transparency; `unclear-remediation` becomes an operationalisation of `failure-remediation-gaps` under Governance / Compliance & process. EU AI Act Art. 73 obligations on serious incident reporting are now covered by `incident-response-gaps` under Governance |
| Restructured Reliability | Revision | reliability | Two active sub-groups (Output quality, Resilience). Monitoring & remediation moved entirely to Governance / Compliance & process. Manipulation & misinformation moved to Security & Misuse / Harmful Misuse |
| Dissolved Governance / Data & oversight | Retired | governance-data-oversight | `human-oversight-control` moved to Governance / Accountability; `data-governance` moved to Governance / Compliance & process. Oversight is fundamentally an accountability concern; data governance fits cleanly under compliance |
| Restructured Security & Misuse | Revision | security-misuse | New "Harmful Misuse" sub-group introduced, absorbing `behavioural-manipulation`, `synthetic-media-abuse`, and `misuse-beyond-intended-purpose`. Security operational sub-group dissolved. AI-specific attacks expanded with `model-extraction` and `data-poisoning` |
| Added `right-to-explanation-contestation` | Addition | transparency-explainability-group | New subcategory absorbing the dissolved Incident Reporting concepts. ExactMatch with EU AI Act Art. 86 |
| Renamed `transparency-explainability-group` content | Revision | system-explainability, prompt-transparency | `prompt-transparency` retired as standalone subcategory and preserved as `operationalisation` of `system-explainability` |
| Renamed `transparency-communication` content | Revision | stakeholder-communication, model-card-completeness | `model-card-completeness` retired as standalone subcategory and preserved as `operationalisation` of `poor-documentation` (Governance / Documentation) |

### New fields

| Field | Purpose | Notes |
|-------|---------|-------|
| `status` | Lifecycle of a concept (`active` / `retired`) | Retired concepts remain in the YAML for institutional memory but do not generate pages or appear in public outputs |
| `operationalisation` | List of mechanisms, indicators, or aids used to assess a parent risk | Each entry has `id`, `label`, and `description`. Used to preserve concepts that describe *causes* rather than risks themselves (dataset bias, proxy discrimination, etc.) without losing them from the YAML. Will eventually carry metrics, methods, and evidence pointers (Gemma's proposed methodology layer) |
| `retirement_note` | Free-text explanation of why a concept was retired and where its content went | Required when `status: retired` |
| `type` (in `mappings.yaml`) | Framework classification (`compliance` / `reference` / `taxonomy`) | Used for grouped rendering on pages and for separating compliance obligations from methodological references |

### Pipeline

| Change | Type | Notes |
|--------|------|-------|
| Public/private filter | Addition | `convert.py` and `generate_pages.py` now produce two outputs: a full internal version (`taxonomy.ttl`, all categories + sub-groups + subcategories, all maturities) and a filtered public version (`taxonomy-public.ttl`, only categories and sub-groups, only `established` maturity). Two parallel directories (`risk/` and `risk-internal/`) are generated |
| Match types removed from public pages | Revision | The `Relationship` column showing exactMatch / closeMatch / etc. is now hidden from public pages. Preserved on internal pages and in SKOS output for internal use |
| Mapping tables grouped by framework type | Addition | On every concept page, mappings are now rendered in three sections: Compliance, Reference frameworks, Taxonomies & vocabularies. The grouping is driven by the `type` field on each framework definition in `mappings.yaml` |
| Framework reference validation | Addition | `check_yaml.py` now validates that every `framework:` value in mapping entries refers to a framework actually defined in `mappings.yaml` |

### External framework mappings

| Change | Type | Notes |
|--------|------|-------|
| Added AIUC-1 | Addition | Q2-2026 release of the AI Underwriting Company Standard. Six domains (A. Data & Privacy, B. Security, C. Safety, D. Reliability, E. Accountability, F. Society) and ~55 controls. Classified as `compliance` |
| Added AIR 2024 / AIR-Bench 2024 | Addition | Zeng et al. academic taxonomy. Four Level-1 categories, 16 Level-2, 45 Level-3, and 314 Level-4 risks derived from 8 government regulations and 16 corporate policies. Classified as `taxonomy` |
| Added IBM AI Risk Atlas | Addition | Lifecycle-based vendor taxonomy (Input / Inference / Output / Non-technical). Classified as `taxonomy` |
| Removed AIRO | Retired | No Eticas concept ever mapped to AIRO directly. The vocabulary was formally incorporated into W3C DPV v2.3 (February 2026); future mappings should target `dpv_ai` |
| Removed VAIR | Retired | Same rationale as AIRO. The standalone URIs remain resolvable for citation |
| 316 new mapping entries applied | Addition | Across 70 active subcategories, 18 sub-groups, and 9 categories. Driven by the verification document at [docs/external-framework-mapping-verification.md](docs/external-framework-mapping-verification.md) |

**Notable exact matches added:**

| Eticas concept | Framework | Concept |
|----------------|-----------|---------|
| `right-to-explanation-contestation` | EU AI Act | Article 86 — Right to explanation of individual decision-making |
| `right-to-explanation-contestation` | DPV | `dpv:RightToExplanation` |
| `data-poisoning` | DPV | `ai:DataPoisoning` |
| `data-poisoning` | EU AI Act | Recital 76 — data poisoning (cybersecurity) |
| `data-poisoning` | IBM AI Risk Atlas | Input → Data poisoning |
| `model-extraction` | IBM AI Risk Atlas | Inference → Extraction attack |
| `homogenization-output-across-groups` | NIST AI 600-1 | #6 Harmful Bias or Homogenization (homogenization clause) |
| `human-oversight-control` | EU AI Act | Article 14 — Human oversight |
| `ai-interaction-disclosure` | EU AI Act | Article 50 — Transparency obligations for AI interacting with natural persons |
| `incident-response-gaps` | EU AI Act | Article 73 — Reporting of serious incidents |
| `pii-leakage` | DPV | `ai:UnauthorisedDataDisclosure` (closeMatch); IBM Output→Personal information (exactMatch); AIUC-1 A.6 (exactMatch); MIT 2.1 (exactMatch); AIR Privacy×PII (exactMatch) |
| `hallucination` | NIST AI 600-1 | #2 Confabulation; IBM hallucination; AIUC-1 D.1+D.2 |
| `automation-bias` | DPV | `ai:AutomationBias` |
| `over-reliance` | MIT | Subdomain 5.1 — Overreliance and unsafe use |
| `loss-of-human-control` | MIT | Subdomain 5.2 — Loss of human agency and autonomy |
| `prompt-injection` | DPV | `ai:PromptInjection` |
| `adversarial-attacks` | DPV | `ai:AdversarialAttack` |
| `behavioural-manipulation` | EU AI Act | Article 5(1)(a) — subliminal/manipulative techniques (prohibited) |
| `re-identification` | DPV | `risk:Reidentification` |
| `membership-inference` | DPV | `ai:MembershipInferenceAttack` |
| `environmental-impact` (category) | MIT, NIST 600-1, OECD, IBM | All four exactMatch — best-aligned category in the taxonomy |
| `organisational-readiness` (category) | ISO 42001 | A.4.2 Resources + A.4.3 Tooling + A.3 Internal organization |
| `transparency-explainability` (category) | ISO 42001 | A.8 Information for interested parties + A.6.2.8 documentation |
| `transparency-explainability` (category) | IBM AI Risk Atlas | Output → Explainability + Non-technical → Transparency |
| `governance` (category) | ISO 42001 | A.2 Policies + A.3 Internal organization |
| `governance` (category) | IBM AI Risk Atlas | Non-technical → Governance dimension |
| `privacy-confidentiality` (category) | AIUC-1 | A — Data & Privacy domain |
| `reliability` (category) | AIUC-1 | D — Reliability domain |

**SKOS triples:** 1085 (post-restructuring) → 1615 (after full mapping refresh).

### Documentation

| Change | Type | Notes |
|--------|------|-------|
| Added `docs/external-framework-mapping-verification.md` | Addition | Complete framework-by-framework verification and mapping research generated up front. Records the reasoning behind every mapping decision applied during Phase 5 |
| Added `docs/v0.2-to-v0.3-mapping.md` | Addition | Concept-by-concept mapping showing where every v0.2 entity moved to in v0.3 (kept, renamed, retired, absorbed, preserved as operationalisation) |
| Updated `docs/external-framework-alignment.md` | Revision | Updated category alignment table to reflect 9-category structure; added AIUC-1, AIR 2024, IBM AI Risk Atlas; corrected and expanded the gaps section based on Phase 5 verification findings |
| Updated `README.md`, `TAXONOMY.md` | Revision | Version bumped to 0.3.0; counts and category lists refreshed; AIUC-1, AIR 2024, IBM Risk Atlas listed as alignment targets |
| Updated `TRACKER.md` | Addition | Phase 5 completion section added with cumulative mapping statistics by framework and notes on application decisions |

---

## [0.2.0] — 2026-04-23

Major restructuring following team review. Reduced the number of top-level categories, introduced an intermediate grouping level, simplified the classification dimensions, and enriched external framework mappings. The full rationale is documented in [TRACKER.md](TRACKER.md).

### Summary

- Categories: **13 → 10**
- Classification dimensions: **3 → 1** (only `maturity` visible; `perspective` retained as internal metadata)
- Structural levels: **2 → 3** (category → sub-group → subcategory)
- Sub-groups introduced: **21**
- Subcategories: **67 → 77**
- External framework mappings: **significantly expanded, including at sub-group level**

### Structure

| Change | Type | Affected concepts | Notes |
|--------|------|-------------------|-------|
| Introduced `subgroup` concept type | Addition | All categories with ≥5 subcategories | Intermediate navigable level between categories and subcategories |
| Merged `autonomy` + `agentic-risks` → `autonomy-agency` | Revision | Autonomy & Human Agency, Agentic Risks | Both dealt with insufficient human control over AI systems |
| `manipulation-misinformation` → `reliability-manipulation` (sub-group) | Revision | Reliability | Moved from standalone category to sub-group under Reliability, consistent with existing Eticas audit practice |
| `resilience` → `reliability-resilience` (sub-group) | Revision | Reliability | Moved from proposed standalone category to sub-group under Reliability |
| `responsibility-redress` → `incident-reporting-redress` | Revision | Incident Reporting & Redress | Renamed to emphasise incident handling rather than who is responsible; aligns with EU AI Act Art. 73 |
| `integration-readiness` → `organisational-readiness` | Revision | Organisational Readiness | Renamed; foregrounds organisational factors as the primary locus of deployment failure |
| Merged `task-success` into `fitness-for-purpose` | Retired | Governance | Combined into "Fitness for purpose and task effectiveness" to cover both ex ante and ex post validation |

### Classification dimensions

| Change | Type | Notes |
|--------|------|-------|
| Removed `inclusion` dimension | Retired | Inclusion always depends on engagement contract; not a stable property of the category |
| Simplified `maturity` to two levels | Revision | Collapsed `established / developing / provisional / proposed` → `established / emerging` |
| Moved `perspective` from page display to internal metadata only | Revision | Field retained in YAML/SKOS for programmatic queries (e.g., client-facing grouping); hidden from browsable pages |

### New subcategories

| Category / Sub-group | Subcategory | Type | Source |
|----------------------|-------------|------|--------|
| Reliability / Manipulation & misinformation | Disinformation generation | Addition | Unified Risk Taxonomy original sub-risks |
| Reliability / Manipulation & misinformation | Behavioural manipulation | Addition | Unified Risk Taxonomy original sub-risks |
| Reliability / Manipulation & misinformation | Synthetic media abuse | Addition | Unified Risk Taxonomy original sub-risks |
| Autonomy & Agency / Human agency | Automation bias | Addition | MIT AI Risk Repository Domain 5 |
| Autonomy & Agency / Human agency | Trust calibration | Addition | MIT AI Risk Repository Domain 5 |
| Autonomy & Agency / Human agency | Deskilling | Addition | MIT AI Risk Repository Domain 5 |
| Autonomy & Agency / Human agency | Over-reliance on AI | Addition | MIT AI Risk Repository Domain 5 |
| Autonomy & Agency / System autonomy | Multi-step autonomous actions | Addition | MIT 7.6 (Multi-agent risks) |
| Autonomy & Agency / System autonomy | Tool use risks | Addition | Emerging agentic AI literature |
| Autonomy & Agency / System autonomy | Emergent behaviour | Addition | Emerging agentic AI literature |
| Autonomy & Agency / System autonomy | Loss of meaningful human control | Addition | EU AI Act Art. 14 |

### Definitions

| Concept | Change | Type | Notes |
|---------|--------|------|-------|
| `security-misuse` | Reframed as AI-specific security (adversarial inputs, prompt injection, model extraction) rather than traditional IT security | Specification | Positions Eticas's assessment as complementary to standard IT security audits |
| `fitness-for-purpose` | Renamed to "Fitness for purpose and task effectiveness", absorbs `task-success` | Revision | Combines ex ante (was this designed for this problem?) and ex post (does it actually work?) questions |

### External framework mappings

| Concept | Change | Type | Notes |
|---------|--------|------|-------|
| All 21 sub-groups | Added external framework mappings at sub-group level | Addition | Mappings to NIST, EU AI Act, MIT, DPV, ISO, OECD added where applicable |
| `incident-reporting-redress` | EU AI Act Article 62 → Article 73 | Clarification | Article was renumbered during trilogue; 73 is the final adopted text |
| `reliability` | Expanded to cover Manipulation (MIT Domain 3, NIST 600-1 #8) and Resilience (NIST "Secure & Resilient", EU AI Act Art. 15(4)) | Revision | Reflects the new sub-groups under Reliability |
| `autonomy-agency` | Added MIT Domain 5, NIST 600-1 #7, DPV Human Oversight, EU AI Act Art. 14 | Addition | New merged category needed its own mappings |
| AIRO / VAIR references | Updated to note formal incorporation into W3C DPV v2.3 | Clarification | AIRO/VAIR are now part of DPV's AI and EU AI Act extensions |

### Documentation

| Change | Type | Notes |
|--------|------|-------|
| External framework alignment document fully rewritten | Revision | Updated for 10-category structure; verified claims against current framework state (MIT V4, DPV v2.3, NIST AI 100-2 E2025, ISO 42005/42006/12792:2025) |
| Added TRACKER.md | Addition | Captures structural decisions and their rationale; public institutional memory |
| Rewrote editing guides (add-category, add-subcategory, edit-existing) | Revision | Reflect new 3-level structure and simplified maturity |
| Simplified category pages to show sub-groups only | Revision | Subcategories now listed on their respective sub-group pages, reducing visual clutter on category pages |

---

## [0.1.0] — 2026-04-10

### Addition

- Initial taxonomy consolidated from 6 Eticas source documents: Unified Risk Taxonomy (URT), RAIA Guide, LLM audit methodology, ADM audit methodology, Career Scoops audit, HR&A project taxonomy
- 11 categories, 57 subcategories (expanded to 13 and 67 respectively through the v0.1.x series)
- SKOS vocabulary published on GitHub with automated build pipeline (YAML → Turtle / JSON-LD / browsable pages)
- External framework alignment with NIST AI RMF, NIST AI 600-1, EU AI Act, MIT AI Risk Repository, OECD AI Principles, ISO/IEC 42001, W3C DPV
- Namespace: `https://taxonomy.eticas.ai/risk/` (pending DNS configuration)
- Published site: `https://eticas-foundation.github.io/ai-risk-taxonomy/risk/` (later moved to `https://eticas-ai.github.io/ai-risk-taxonomy/risk/`)
- Editing workflow: GitHub pull requests with automated YAML validation and SKOS regeneration

---

## How to contribute changes

Changes are proposed via GitHub pull requests:

1. Edit `src/taxonomy.yaml` (add, revise, or retire concepts)
2. Update this CHANGELOG under an `## [Unreleased]` heading
3. Open a pull request
4. CI validates the YAML and regenerates SKOS and pages automatically
5. Team review and merge

Releases are tagged in Git. Each release produces a timestamped snapshot of all output formats (Turtle, JSON-LD, HTML).
