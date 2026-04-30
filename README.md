# Eticas AI Risk Taxonomy

A unified, machine-readable AI risk taxonomy for use across [Eticas](https://eticas.ai) audit methodologies, assessment frameworks, and reporting outputs.

**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**Version:** 0.3.0 · [What's new →](CHANGELOG.md)  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## About

This repository contains Eticas' canonical definitions of AI risk categories and subcategories, formally linked to ten major international frameworks: NIST AI RMF (AI 100-1), NIST AI 600-1 (Generative AI Profile), EU AI Act (Regulation 2024/1689), MIT AI Risk Repository V4, OECD AI Principles (2024 update), ISO/IEC 42001:2023, W3C Data Privacy Vocabulary v2.3, AIUC-1, AIR 2024, and the IBM AI Risk Atlas.

Each concept has a stable URI (e.g., `https://taxonomy.eticas.ai/risk/bias-fairness`), a definition, alternative labels, lifecycle stage applicability, and cross-references to equivalent concepts in external frameworks. Mappings are organised in three buckets — compliance (regulations and certifiable standards), reference (policy frameworks and principles), and taxonomy (academic and vocabulary frameworks) — making it straightforward to demonstrate adherence to obligations separately from conceptual interoperability.

## Documentation

### For Eticas team and contributors
- **[Introduction for the team](docs/intro-for-team.md)** — what we're building and why it matters
- **[Implementation details](docs/implementation.md)** — architecture, build pipeline, and technical decisions
- **[How to edit the taxonomy](docs/editing-guide.md)** — step-by-step guides for adding and modifying entries
- **[Decision tracker](TRACKER.md)** — structural decisions, rationale, and open items
- **[Framework mapping verification](docs/external-framework-mapping-verification.md)** — research record behind the v0.3 mapping refresh: framework-by-framework verification across 10 frameworks, citations, and gap analysis. The decisions captured here were applied to the YAML during the Phase 5 work
- **[v0.2 → v0.3 concept mapping](docs/v0.2-to-v0.3-mapping.md)** — concept-by-concept record of every move (kept, renamed, retired, absorbed, preserved as operationalisation)
- **[Changelog](CHANGELOG.md)** — version history of taxonomy changes

### External
- **[Taxonomy description](TAXONOMY.md)** — full list of categories, subcategories, definitions, and external mappings
- **[External framework alignment](docs/external-framework-alignment.md)** — how Eticas categories align with each framework, where they diverge, and where Eticas extends what existing frameworks cover

## Risk categories

- [Bias & Fairness](risk/bias-fairness.md) — established
- [Privacy & Confidentiality](risk/privacy-confidentiality.md) — established
- [Reliability](risk/reliability.md) — established
- [Governance](risk/governance.md) — established
- [Security & Misuse](risk/security-misuse.md) — established
- [Environmental Impact](risk/environmental-impact.md) — established
- [Transparency & Explainability](risk/transparency-explainability.md) — established
- [Autonomy & Agency](risk/autonomy-agency.md) — emerging
- [Organisational Readiness](risk/organisational-readiness.md) — emerging

## Outputs

The build pipeline produces both an internal version (full taxonomy with all subcategories) and a public version (categories and sub-groups only, established maturity, mappings without match-type qualifiers). Both are regenerated automatically on every merge to `main`.

| Format | Path | Audience | Description |
|--------|------|----------|-------------|
| YAML source | [`src/taxonomy.yaml`](src/taxonomy.yaml) | Internal | Human-editable source of truth |
| Framework definitions | [`src/mappings.yaml`](src/mappings.yaml) | Internal | External framework metadata and `type` classification |
| SKOS Turtle (full) | [`dist/taxonomy.ttl`](dist/taxonomy.ttl) | Internal | Machine-readable RDF, full taxonomy |
| SKOS JSON-LD (full) | [`dist/taxonomy.jsonld`](dist/taxonomy.jsonld) | Internal | Machine-readable linked data, full taxonomy |
| SKOS Turtle (public) | [`dist/taxonomy-public.ttl`](dist/taxonomy-public.ttl) | Public | Filtered: categories + sub-groups, established maturity |
| SKOS JSON-LD (public) | [`dist/taxonomy-public.jsonld`](dist/taxonomy-public.jsonld) | Public | Filtered: categories + sub-groups, established maturity |
| Browsable pages (full) | [`risk-internal/`](risk-internal/) | Internal | Full per-concept pages with match types |
| Browsable pages (public) | [`risk/`](risk/) | Public | Categories and sub-groups, no match-type qualifiers |

## Contributing

Edit [`src/taxonomy.yaml`](src/taxonomy.yaml) and open a pull request. The CI validates your changes automatically and regenerates all outputs on merge.

See the **[editing guide](docs/editing-guide.md)** for step-by-step instructions, including copy-paste templates for common tasks.

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.3.0).
https://taxonomy.eticas.ai/risk/
```
