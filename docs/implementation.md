# Eticas AI Risk Taxonomy — Implementation guide

## Overview

This document describes the technical architecture for building and maintaining Eticas' AI risk taxonomy as a GitHub-hosted, machine-readable vocabulary. The design prioritises **low maintenance overhead** (a team of 5–10 people, none of whom need to be ontology specialists) while producing **standards-compliant outputs** suitable for knowledge graphs, regulatory mapping, and interoperability with the broader AI governance ecosystem.

## Architecture: the dual-layer approach

The core design principle is **simple source, generated complexity**. The team edits human-friendly YAML files. An automated pipeline converts these into formal SKOS (Turtle and JSON-LD) and a browsable documentation site. No one needs to write RDF by hand.

```
┌─────────────────────────────────────────────────────────┐
│                    Source layer (human)                  │
│                                                         │
│   src/taxonomy.yaml          ← team edits this          │
│   src/mappings.yaml          ← external equivalences    │
│                                                         │
├───────────────────── GitHub Actions ────────────────────┤
│                                                         │
│   1. convert.py (RDFLib)     → SKOS Turtle + JSON-LD    │
│   2. validate.py (Skosify)   → consistency checks       │
│   3. generate_pages.py       → Markdown per concept     │
│                                                         │
├───────────────────── Jekyll (GitHub Pages) ─────────────┤
│                                                         │
│   Markdown → HTML            (automatic, zero config)   │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    Output layer (machine + human)        │
│                                                         │
│   dist/taxonomy.ttl          ← SKOS Turtle              │
│   dist/taxonomy.jsonld       ← JSON-LD                  │
│   risk/bias-fairness.md      → served as HTML by Jekyll  │
│   risk/privacy.md            → served as HTML by Jekyll  │
│   ...                                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

Every push to `main` triggers the pipeline. The published site and formal vocabulary files are always in sync with the source.

## Namespace and concept URIs

### What a namespace is

Every concept in the taxonomy needs a **persistent, globally unique identifier**. In the linked data world, these identifiers are URLs — not because someone necessarily visits them in a browser (though they can), but because URLs are the only identifier scheme that is globally unique, owned by the organisation, and resolvable.

The namespace is the base URL from which all concept identifiers are derived. For example, with a namespace of `https://taxonomy.eticas.ai/risk/`, the "Bias & Fairness" category gets the identifier:

```
https://taxonomy.eticas.ai/risk/bias-fairness
```

This URI serves three purposes simultaneously:

1. **As an identifier** — when another system, document, or vocabulary refers to Eticas' "Bias & Fairness" concept, it uses this URI. There is no ambiguity about which definition of "fairness" is meant.
2. **As a documentation URL** — visiting the URI in a browser returns a human-readable page with the definition, hierarchy, and cross-references.
3. **As a data endpoint** — a machine requesting the URI with the appropriate content-type header (e.g., `Accept: application/ld+json`) receives the structured SKOS data instead of HTML.

This is standard practice for published vocabularies. The W3C DPV uses `https://w3id.org/dpv/`, Schema.org uses `https://schema.org/`, and EuroVoc uses `http://eurovoc.europa.eu/`. The pattern is always the same: a domain the organisation controls, serving both human and machine representations of each concept.

### Why not use GitHub URLs

The repository will be hosted at `github.com/eticas-ai/ai-risk-taxonomy`, and GitHub Pages will initially serve the site at `eticas-ai.github.io/ai-risk-taxonomy/`. It would be tempting to use these as concept URIs directly. This is a bad idea for one reason: **URIs are permanent, but hosting is not**.

If Eticas ever moves the repository to a different GitHub organisation, switches to GitLab, or hosts the documentation elsewhere, every URI breaks — and every external system or document that references those URIs now points to nothing. In linked data, broken URIs are the equivalent of broken contracts.

By using `https://taxonomy.eticas.ai/risk/` as the namespace and configuring it as a custom domain for GitHub Pages, the URI layer is decoupled from the hosting layer. The DNS record for `taxonomy.eticas.ai` can be pointed at GitHub Pages today and at any other hosting tomorrow, without changing a single URI. External references to `https://taxonomy.eticas.ai/risk/bias-fairness` continue to work regardless of where the content is served from.

### Chosen namespace

```
https://taxonomy.eticas.ai/risk/
```

This uses a subdomain of `eticas.ai` (the company domain), which Eticas controls. The `/risk/` path scopes the namespace to the risk taxonomy specifically, leaving room for other vocabularies under the same subdomain in the future (e.g., `https://taxonomy.eticas.ai/controls/`, `https://taxonomy.eticas.ai/lifecycle/`).

Concept URIs follow the pattern:

| Concept | URI |
|---------|-----|
| Bias & Fairness (category) | `https://taxonomy.eticas.ai/risk/bias-fairness` |
| Dataset bias (subcategory) | `https://taxonomy.eticas.ai/risk/dataset-bias` |
| Prompt injection (subcategory) | `https://taxonomy.eticas.ai/risk/prompt-injection` |

### Setup required

Configuring the custom domain requires one DNS record and one GitHub Pages setting:

1. **DNS:** Add a CNAME record pointing `taxonomy.eticas.ai` to `eticas-ai.github.io`
2. **GitHub Pages:** In the repository settings, set `taxonomy.eticas.ai` as the custom domain and enable HTTPS

This is a one-time configuration. Once done, GitHub Pages serves the site under the custom domain, and all concept URIs resolve correctly.

## Repository structure

```
eticas-ai/ai-risk-taxonomy/        # github.com/eticas-ai/ai-risk-taxonomy
│
├── README.md                          # Overview and quick start
├── TAXONOMY.md                        # Full taxonomy description (document 2)
├── CHANGELOG.md                       # Version history
├── LICENSE                            # CC BY 4.0
├── _config.yml                        # Jekyll configuration
│
├── src/
│   ├── taxonomy.yaml                  # Source of truth — risk categories
│   ├── mappings.yaml                  # External framework alignments
│   └── config.yaml                    # Namespace, versioning metadata
│
├── risk/                              # Generated Markdown — one page per concept
│   ├── bias-fairness.md               #   (also readable directly on GitHub)
│   ├── privacy-confidentiality.md
│   ├── dataset-bias.md
│   └── ...
│
├── dist/                              # Generated machine-readable outputs
│   ├── taxonomy.ttl                   # SKOS in Turtle format
│   └── taxonomy.jsonld                # SKOS in JSON-LD
│
├── build/
│   ├── convert.py                     # YAML → SKOS RDF (Python/RDFLib)
│   ├── validate.py                    # SKOS validation (Skosify)
│   ├── generate_pages.py             # YAML → Markdown concept pages
│   └── requirements.txt              # Python dependencies
│
├── .github/
│   └── workflows/
│       └── build-and-publish.yml      # CI/CD pipeline
│
└── docs/
    ├── intro-for-team.md              # Non-technical introduction (document 1)
    └── implementation.md              # This document
```

## Source format: YAML

The YAML source file is designed to be readable and editable without any specialised tools. A concept entry looks like this:

```yaml
# src/taxonomy.yaml

scheme:
  id: eticas-ai-risk-taxonomy
  title: "Eticas AI Risk Taxonomy"
  version: "0.1.0"
  namespace: "https://taxonomy.eticas.ai/risk/"
  description: >
    A unified AI risk taxonomy for use across Eticas audit
    methodologies, assessment frameworks, and reporting outputs.

concepts:

  - id: bias-fairness
    type: category          # category | subgroup | subcategory
    label: "Bias & Fairness"
    alt_labels:
      - "Fairness"
      - "Bias & Discrimination"
      - "Algorithmic fairness"
    definition: >
      The risk that an AI system produces outcomes that systematically
      advantage or disadvantage individuals or groups based on protected
      or sensitive attributes, leading to unequal treatment, reduced
      accuracy, or unjust impacts.
    scope: ALL              # ADM | LLM | ALL
    lifecycle_stages:
      - pre-processing
      - in-processing
      - post-processing
    maturity: established   # established | emerging
    perspective: rights & ethics
    status: active          # active | retired (default: active)
    mappings:
      - framework: mit
        target_id: domain-1
        target_label: "Discrimination & Toxicity"
        relation: closeMatch
      - framework: dpv_ai
        target_id: AIBias
        target_label: "AI Bias"
        target_url: https://w3c.github.io/dpv/2.3/ai/#AIBias
        relation: closeMatch

  - id: disparate-impact-protected-groups
    type: subcategory
    broader: bias-outcome-disparities   # points to a sub-group, not the category
    label: "Disparate impact on protected groups"
    definition: >
      AI system outputs that produce systematically different outcomes
      for individuals based on protected characteristics such as race,
      gender, age, disability, or religion.
    scope: ALL
    lifecycle_stages:
      - in-processing
      - post-processing
    operationalisation:
      - id: dataset-bias
        label: "Dataset bias and under/over-representation"
        description: >
          Training or evaluation data that does not adequately represent
          all relevant population groups. Used as a mechanism to detect
          and assess the parent risk, not as a risk in itself.
    # ... mappings ...
```

Key design decisions:

- **One file for the taxonomy** — at this scale (~100 concepts), a single file is simpler than one-file-per-concept. If the taxonomy grows significantly, splitting by category is straightforward.
- **Mappings in a separate file** — `mappings.yaml` defines the external framework definitions including a `type` field (`compliance` / `reference` / `taxonomy`) used to group rendered mappings on each concept page.
- **Alt labels capture naming variations** — every name variant used across Eticas documents (e.g., "Reliability & Manipulation" for what the taxonomy calls "Reliability") is recorded as an `alt_label`, ensuring backward discoverability.
- **Risks vs mechanisms** — concepts that describe how a risk is detected or measured (rather than the risk itself) live as `operationalisation` entries on the parent risk concept. This keeps the risk hierarchy clean and provides a hook for the methodology layer.
- **Status field** — concepts no longer recognised as risks but kept for institutional memory carry `status: retired` plus a `retirement_note`. The pipeline filters them from all generated outputs.

## The build pipeline

### Step 1: Convert (YAML → SKOS RDF)

A Python script (~150 lines) using [RDFLib](https://rdflib.readthedocs.io/) reads the YAML source and produces SKOS Turtle and JSON-LD files.

For each concept, the script generates:

```turtle
eticas:bias-fairness a skos:Concept ;
    skos:inScheme eticas:scheme ;
    skos:prefLabel "Bias & Fairness"@en ;
    skos:altLabel "Fairness"@en, "Bias & Discrimination"@en ;
    skos:definition "The risk that an AI system..."@en ;
    skos:topConceptOf eticas:scheme ;
    skos:closeMatch <https://airisk.mit.edu/domain/1> ;
    skos:closeMatch <https://nist.gov/ai-600-1/harmful-bias> ;
    skos:broadMatch <https://w3id.org/dpv/ai#AIBias> ;
    eticas:scope "ALL" ;
    eticas:status "core" .

eticas:dataset-bias a skos:Concept ;
    skos:inScheme eticas:scheme ;
    skos:prefLabel "Dataset bias and under/over-representation"@en ;
    skos:broader eticas:bias-fairness ;
    skos:definition "Training or evaluation data..."@en .
```

### Step 2: Validate (Skosify)

[Skosify](https://github.com/NatLibFi/Skosify) is run as a validation and enrichment step. It:

- Checks SKOS structural integrity (no orphan concepts, no cyclic broader/narrower)
- Infers inverse relationships (if A `skos:broader` B, then B `skos:narrower` A)
- Fills in `skos:hasTopConcept` from the hierarchy
- Reports warnings for missing labels or definitions

This runs as a CI check — a pull request with an invalid taxonomy change fails the build.

### Step 3: Generate concept pages (Markdown)

A Python script reads the YAML source and generates one Markdown file per concept in the `risk/` directory. Each file includes a YAML front matter block (which Jekyll uses for layout and metadata) and a structured body. A generated page looks like this:

```markdown
---
layout: concept
title: "Bias & Fairness"
id: bias-fairness
uri: https://taxonomy.eticas.ai/risk/bias-fairness
maturity: established
scope: ALL
---

# Bias & Fairness

The risk that an AI system produces outcomes that systematically
advantage or disadvantage individuals or groups based on protected
or sensitive attributes, leading to unequal treatment, reduced
accuracy, or unjust impacts.

**Also known as:** Fairness · Bias & Discrimination · Algorithmic fairness

**Applies to:** ADM, LLM
**Lifecycle stages:** Pre-processing, In-processing, Post-processing

## Subcategories

- [Dataset bias and under/over-representation](dataset-bias)
- [Proxy discrimination](proxy-discrimination)
- [Intersectional unfairness](intersectional-unfairness)
- ...

## Mappings to external frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| MIT AI Risk Repository | Domain 1: Discrimination & Toxicity | closeMatch |
| NIST AI 600-1 | #6 Harmful Bias & Homogenization | closeMatch |
| NIST AI RMF | Fair with Harmful Bias Managed | closeMatch |
| W3C DPV | ai:AIBias | broadMatch |
```

This approach has three advantages over generating HTML directly (e.g., via pyLODE):

**Readable in the repo.** Anyone browsing `github.com/eticas-ai/ai-risk-taxonomy/blob/main/risk/bias-fairness.md` sees a rendered page with the definition, hierarchy, and mappings — without needing to visit the published site.

**Reviewable in PRs.** When the build regenerates concept pages after a YAML change, the diff shows meaningful Markdown rather than opaque HTML. Reviewers can see exactly what changed in the published content.

**Rendered by Jekyll for free.** GitHub Pages has Jekyll built in. Any `.md` file with YAML front matter gets rendered as HTML automatically, with whatever layout template you define. No extra build step, no additional tooling.

The `_config.yml` at the repo root configures Jekyll — theme, navigation, the base URL. A simple `_layouts/concept.html` template controls how concept pages are styled. This is standard GitHub Pages usage.

### CI/CD: GitHub Actions

The pipeline runs in a single GitHub Actions workflow:

```yaml
# .github/workflows/build-and-publish.yml

name: Build and publish taxonomy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r build/requirements.txt

      - name: Convert YAML to SKOS
        run: python build/convert.py

      - name: Validate SKOS
        run: python build/validate.py

      - name: Generate concept pages
        run: python build/generate_pages.py

      - name: Commit generated files
        if: github.ref == 'refs/heads/main'
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add risk/ dist/
          git diff --staged --quiet || git commit -m "Regenerate taxonomy outputs"
          git push
```

On pull requests, the pipeline runs convert + validate to check the change is well-formed. On merge to `main`, it regenerates the concept pages and SKOS files and commits them back to the repo. GitHub Pages then picks up the changes automatically — no separate deployment step needed.

Note: an alternative is to use the `peaceiris/actions-gh-pages` action to deploy to a separate `gh-pages` branch, keeping generated files out of `main`. Either pattern works; committing to `main` is simpler and keeps everything in one place.

## Tools and dependencies

All tools are Python-based and open source. The full dependency list:

| Tool | Purpose | Install |
|------|---------|---------|
| [RDFLib](https://rdflib.readthedocs.io/) | YAML → RDF conversion, SKOS graph manipulation | `pip install rdflib` |
| [Skosify](https://github.com/NatLibFi/Skosify) | SKOS validation and enrichment | `pip install skosify` |
| [PyYAML](https://pyyaml.org/) | YAML parsing | `pip install pyyaml` |
| [Jinja2](https://jinja.palletsprojects.com/) | Markdown page templating (optional) | `pip install jinja2` |

Total: three required packages, one optional. Jekyll is provided by GitHub Pages — nothing to install. If richer auto-generated documentation is needed later (class diagrams, full property tables), [pyLODE](https://github.com/RDFLib/pyLODE) can be added as a supplementary tool.

## Workflow for the team

### Adding a new subcategory

1. Open `src/taxonomy.yaml`
2. Add a new entry under the appropriate category:
   ```yaml
   - id: automation-bias
     type: subcategory
     broader: autonomy
     label: "Automation bias"
     definition: >
       The tendency of humans to over-rely on automated outputs,
       accepting AI recommendations without sufficient scrutiny.
     scope: ALL
     lifecycle_stages:
       - post-processing
   ```
3. Commit, push, open a PR
4. CI validates the change; a colleague reviews and merges
5. The site updates automatically

### Adding a mapping to an external framework

1. Open `src/mappings.yaml` to check the framework prefix exists (or add it)
2. In `src/taxonomy.yaml`, add a mapping entry to the relevant concept:
   ```yaml
   mappings:
     - target: "nist600:human-ai-configuration"
       relation: closeMatch
       label: "Human-AI Configuration"
   ```
3. Same commit/PR/review flow

### Changing a category's inclusion

When the team decides a category should be assessed in every audit (or vice versa):

1. Change `inclusion: audit-dependent` to `inclusion: required` (or the reverse) in the YAML
2. Document the rationale in the PR description and in CHANGELOG.md
3. Bump the minor version in `src/config.yaml`

This is a significant decision — it changes what every audit must cover. The PR should include agreement from the team.

### Changing a category's maturity

As a category's definitions stabilise and assessment methods are tested in practice:

1. Change `maturity: emerging` to `maturity: established`
2. For promotion to established: ensure the definition is stable, subcategories are complete, and external mappings are in place
3. Document the change in CHANGELOG.md
4. Bump the minor version in `src/config.yaml`

Maturity is now a single dimension with two values (`established`, `emerging`). The earlier `inclusion` dimension (whether a category is required or audit-dependent) was removed in v0.2 because in practice, what is assessed always depends on the engagement contract.

## Benefits of this approach

### For Eticas' internal work

**Single source of truth.** Every methodology, scorecard, leaflet, and audit report can reference a canonical definition by its URI. When a definition changes, it changes everywhere.

**Traceability.** Every change to the taxonomy is tracked in Git with commit messages, authorship, timestamps, and review records. This is auditable — important for a company that audits others.

**Low friction.** The team edits YAML, which reads like a structured outline. No RDF, no ontology editors, no special training. Review happens through the same pull request workflow already used for other projects.

**Extensibility.** Adding a new risk category, subcategory, or external mapping is a 5-minute YAML edit, not a document revision across multiple files.

### For interoperability and positioning

**Machine-readable outputs.** The generated SKOS Turtle and JSON-LD files can be consumed by knowledge graph systems, SPARQL endpoints, or any tool that understands linked data. This enables future applications like automated regulatory mapping or cross-audit analytics.

**Resolvable URIs.** Every concept has a URL that returns both human-readable documentation (HTML) and machine-readable data (RDF via content negotiation or link headers). This is the standard for published vocabularies.

**Formal cross-references.** Using `skos:exactMatch` and `skos:closeMatch` to link to W3C DPV, MIT, NIST, and other vocabularies makes Eticas' taxonomy part of the emerging web of AI governance vocabularies — not an island.

**Standards compliance.** SKOS is a W3C Recommendation (since 2009), widely adopted by libraries, governments, and standards bodies. Using it positions Eticas alongside institutions like the EU Publications Office, the Library of Congress, and the W3C DPVCG.

### Compared to alternatives

| Approach | Pros | Cons |
|----------|------|------|
| **Spreadsheet (current state)** | Easy to edit | No versioning, no URIs, no machine-readable output, no links to external frameworks |
| **Word/PDF document** | Rich formatting | Same limitations, plus harder to extract structured data |
| **Full ontology editor (VocBench, Protégé)** | Powerful for complex ontologies | Heavy infrastructure, steep learning curve, overkill for ~80 concepts |
| **YAML + build pipeline (proposed)** | Low barrier, full standards compliance, Git-native | Requires initial setup of build scripts |

## Implementation roadmap

### Phase 1: Foundation (weeks 1–2)

- Set up the GitHub repository with the structure described above
- Write the `convert.py` script (YAML → SKOS Turtle + JSON-LD)
- Populate `taxonomy.yaml` with the core 5 categories and their subcategories from the Unified Risk Taxonomy
- Add basic CI validation

### Phase 2: Consolidation (weeks 3–4)

- Integrate subcategories from the HRA taxonomy (Excel) that add value and don't conflict
- Add extended categories (Environmental Impact, Transparency & Explainability, Responsibility & Redress)
- Document naming variations across LLM methodology, ADM methodology, RAIA Guide, and Career Scoops as `alt_labels`
- Set up Markdown concept page generation, Jekyll layout, and GitHub Pages deployment with custom domain (`taxonomy.eticas.ai`)

### Phase 3: External linking (weeks 5–6)

- Add mappings to W3C DPV AI extension (concept-level URIs)
- Add mappings to MIT AI Risk Repository domains/subdomains
- Add mappings to NIST AI 600-1 risk categories and AI RMF trustworthiness characteristics
- Add reference-level mappings to OECD principles and ISO standards

### Phase 4: Adoption (ongoing)

- Update methodology documents to reference taxonomy URIs
- Integrate taxonomy categories into the Leaflet scoring system
- Incorporate into new audit scoping and reporting workflows

---

*This document describes the implementation plan for Eticas' AI risk taxonomy repository. For the non-technical introduction, see `intro-for-team.md`. For the full taxonomy description, see `TAXONOMY.md`.*
