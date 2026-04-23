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
