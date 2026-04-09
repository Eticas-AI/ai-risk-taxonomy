# Eticas AI Risk Taxonomy

A unified, machine-readable AI risk taxonomy for use across [Eticas](https://eticas.ai) audit methodologies, assessment frameworks, and reporting outputs.

**Namespace:** `https://taxonomy.eticas.ai/risk/`  
**Version:** 0.1.0  
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## About

This repository contains Eticas' canonical definitions of AI risk categories and subcategories, formally linked to major international frameworks including the NIST AI RMF, EU AI Act, MIT AI Risk Repository, OECD AI Principles, ISO/IEC 42001, and the W3C Data Privacy Vocabulary.

Each concept has a stable URI (e.g., `https://taxonomy.eticas.ai/risk/bias-fairness`), a definition, alternative labels, lifecycle stage applicability, and cross-references to equivalent concepts in external frameworks.

## Documentation

### For Eticas team and contributors

- **[Introduction for the team](docs/intro-for-team.md)** — what we're building and why it matters
- **[Implementation details](docs/implementation.md)** — architecture, build pipeline, and technical decisions
- **[How to edit the taxonomy](docs/editing-guide.md)** — step-by-step guides for adding and modifying entries

### External

- **[Taxonomy description](TAXONOMY.md)** — full list of categories, subcategories, definitions, and external mappings
- **[External framework alignment](docs/external-framework-alignment.md)** — how Eticas categories map to NIST, MIT, EU AI Act, OECD, ISO, and W3C DPV

## Risk categories

- [Bias & Fairness](risk/bias-fairness.md) — required · established · rights & ethics
- [Privacy & Confidentiality](risk/privacy-confidentiality.md) — required · established · rights & ethics
- [Reliability](risk/reliability.md) — required · established · technical soundness
- [Governance](risk/governance.md) — required · established · governance & compliance
- [Security & Misuse](risk/security-misuse.md) — required · established · technical soundness
- [Transparency & Explainability](risk/transparency-explainability.md) — required · established · governance & compliance
- [Environmental Impact](risk/environmental-impact.md) — audit-dependent · established · technical soundness
- [Responsibility & Redress](risk/responsibility-redress.md) — audit-dependent · developing · rights & ethics
- [Autonomy & Human Agency](risk/autonomy.md) — audit-dependent · provisional · rights & ethics
- [Agentic Risks](risk/agentic-risks.md) — audit-dependent · provisional · technical soundness
- [Manipulation & Misinformation](risk/manipulation-misinformation.md) — audit-dependent · provisional · rights & ethics

## Outputs

| Format | Path | Description |
|--------|------|-------------|
| YAML source | [`src/taxonomy.yaml`](src/taxonomy.yaml) | Human-editable source of truth |
| SKOS Turtle | [`dist/taxonomy.ttl`](dist/taxonomy.ttl) | Machine-readable RDF |
| SKOS JSON-LD | [`dist/taxonomy.jsonld`](dist/taxonomy.jsonld) | Machine-readable linked data |
| Browsable pages | [`risk/`](risk/) | One page per concept |

## Contributing

Edit [`src/taxonomy.yaml`](src/taxonomy.yaml) and open a pull request. The CI validates your changes automatically and regenerates all outputs on merge.

See the **[editing guide](docs/editing-guide.md)** for step-by-step instructions, including copy-paste templates for common tasks.

## How to cite

```
Eticas. (2026). Eticas AI Risk Taxonomy (Version 0.1.0).
https://taxonomy.eticas.ai/risk/
```
