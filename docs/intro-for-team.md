# Eticas AI Risk Taxonomy: what we're building and why it matters

## The problem we're solving

Eticas uses risk categories — Bias & Fairness, Privacy & Confidentiality, Reliability, and others — across everything we do: audit methodologies (LLM and ADM), the RAIA Guide, the Leaflet, audit reports. But these categories are not currently defined in a single authoritative place, and there are inconsistencies across documents:

- The LLM Methodology uses "Reliability & Manipulation" as a combined category; the Unified Risk Taxonomy separates them.
- Some documents say "Safety, Security & Misuse"; others just "Security & Misuse".
- The RAIA Guide adds "Transparency & Explainability" and "Responsibility & Redress" as separate categories, but only at the Post-Processing stage.
- The HR&A taxonomy includes subcategories (like "Jailbreakability" or "Hallucination prevention") that don't appear in other documents.

This is manageable today, but it becomes a real problem as we grow, take on more clients, and need audit results to be comparable across engagements.

## What we're doing

We're creating a **unified, formal AI risk taxonomy** — a structured catalogue where every risk category and subcategory has:

- A **canonical name** and a **clear definition**
- A **unique identifier** (a URL) that allows unambiguous referencing
- **Synonyms and equivalences** to major international frameworks (NIST, EU AI Act, MIT AI Risk Repository, OECD, ISO, W3C DPV)
- Indication of which **system types** it applies to (LLM, ADM, both) and which **lifecycle stages** are relevant
- A **maturity level** and an **inclusion rule** — reflecting both how developed the category is and whether it's part of every audit

Not every risk category is at the same level of development. The taxonomy tracks **maturity** as a single dimension with two values: **established** (stable definition, well-developed subcategories, proven assessment methods, strong mappings to external frameworks) and **emerging** (recognised as important, but definitions may evolve and assessment methods are still developing). Whether a particular category is included in a given audit depends on the engagement contract — that is a presentation choice rather than a property of the category. Categories move from emerging to established as definitions stabilise, assessment methods are tested in audits, and the profession develops shared practice. Each change is an explicit team decision documented in the changelog.

The taxonomy will live as a GitHub repository and will be automatically published as a browsable reference site.

## What "linked taxonomy" means in practice

The core idea: **when Eticas says "Bias & Fairness", we want to formally state that this is the same thing as (or closely related to) what NIST calls "Fair with Harmful Bias Managed", what the MIT AI Risk Repository classifies as "Discrimination & Toxicity", and what the EU AI Act regulates through its non-discrimination requirements.**

This is done through SKOS (Simple Knowledge Organization System) — a W3C standard for expressing relationships between concepts across vocabularies. It's the same approach used by the EU Publications Office for EuroVoc, by national libraries for subject headings, and by the W3C Data Privacy Vocabulary group for linking privacy and AI concepts across jurisdictions.

The practical result is that our taxonomy is **connected** to the international AI risk standards ecosystem rather than existing in isolation.

## Why not just a spreadsheet?

A well-maintained Excel file could solve the consistency problem. You could list categories, definitions, and even add columns mapping to NIST, MIT, and others. This is roughly what the HR&A taxonomy does today. The question is what you gain by going further.

The difference is between a document that **describes** relationships and a structure that **encodes** them in a way software can act on. A few concrete examples of what becomes possible:

**Automated regulatory mapping.** A client asks which of our audit findings are relevant under the EU AI Act. If the taxonomy is machine-readable and linked to the W3C DPV's AI Act extension, a script can answer this directly: it can traverse the links from our risk categories to the Act's requirements and generate a compliance mapping table — without anyone manually building it each time.

**Tooling integration.** The Leaflet needs to know which risk categories to score and how they relate to the RAIA Guide scorecard checks. If the taxonomy is structured data, the Leaflet can read it directly as a configuration source rather than requiring someone to manually keep the two in sync. The same applies to any future dashboard, reporting template, or client portal.

**Cross-audit analytics.** If audit findings reference taxonomy URIs rather than free-text category names, it becomes straightforward to aggregate findings across audits — e.g., "across all audits in 2026, which subcategories had the highest severity scores?" This kind of query is difficult when categories are text strings that vary slightly between documents.

**Interoperability with external systems.** Clients, regulators, and partner organisations increasingly work with structured data. If a client's GRC platform imports NIST AI RMF categories, and our taxonomy formally declares equivalences to those categories, integration becomes a data operation rather than a consulting exercise.

**Discoverability.** When the taxonomy is published with resolvable URIs (each concept has a URL that returns its definition, hierarchy, and cross-references), anyone — a regulator, a researcher, a potential client — can navigate from a reference to our taxonomy to understand exactly what we mean and how it relates to frameworks they already know. A spreadsheet shared on request doesn't provide this.

None of this requires Eticas to build complex infrastructure today. The point is that encoding the taxonomy in a standard format — SKOS — keeps these options open at very low marginal cost, whereas a spreadsheet forecloses them. The effort to maintain a YAML source file is comparable to maintaining a spreadsheet; the difference is in what the outputs enable.

**Where SKOS fits in:** SKOS is the specific standard that makes the encoding work. It provides a small, well-defined vocabulary for saying things like "concept A is broader than concept B", "concept A in our taxonomy is equivalent to concept X in NIST's taxonomy", and "concept A has this definition in English". Because SKOS is a W3C standard used by hundreds of organisations, any tool that works with linked data or knowledge graphs can consume it without custom integration. We don't interact with SKOS directly — we edit YAML and the build pipeline handles the conversion — but SKOS is the reason the outputs are interoperable rather than just structured.

## Why this matters for Eticas

### Immediate practical benefits

**Consistency across our work.** When an auditor opens the LLM methodology, the RAIA Guide, or the Leaflet, the risk categories are the same. When someone new joins, there's a single reference point for what each category means.

**Comparability across audits.** If a client commissions two audits over time, or audits of different systems, the results are comparable because they use exactly the same vocabulary.

**Easy to extend.** When a new risk type emerges (e.g., "Agentic Risks" for autonomous agent systems), it gets added to the taxonomy with its definition and equivalences, and is immediately available across all methodologies.

**Regulatory mapping built in.** When a client asks "how does your audit relate to the EU AI Act?" or "how does this map to NIST?", the answer is already in the taxonomy: each of our categories indicates which regulatory requirement it corresponds to.

### Positioning benefits

**Eticas as a contributor, not just a consumer.** There is a convergence moment right now: MIT, the W3C, NIST, and the OECD are all publishing AI risk taxonomies and vocabularies. But none offers a complete, linked, audit-practice-oriented taxonomy. If Eticas publishes ours as an open, linked vocabulary:

- We position ourselves as a technical reference in the field
- Other auditors and organisations can cite and link to our definitions
- We demonstrate the level of rigour and systematisation behind our work

**Credibility with clients and regulators.** Being able to say "our risk taxonomy is formally aligned with the NIST AI RMF, the EU AI Act, and ISO standards" is both a sales argument and a credibility signal. This isn't a table of equivalences in a PDF — these are verifiable, navigable cross-references.

**Foundation for future products.** A structured taxonomy is the base layer for tools like the Leaflet (which needs to know exactly which categories to score), cross-audit comparison dashboards, or a future audit results API.

## How this affects day-to-day work

The change to daily workflow is minimal. The taxonomy is edited in a YAML file — a structured, readable text format. No programming required. A simplified example of what it looks like:

```yaml
- id: bias-fairness
  label: "Bias & Fairness"
  definition: >
    The risk that an AI system produces outcomes that systematically
    advantage or disadvantage individuals or groups based on protected
    or sensitive attributes.
  applies_to: [ADM, LLM]
  equivalent_to:
    - nist: "Fair with Harmful Bias Managed"
    - mit: "Domain 1: Discrimination & Toxicity"
    - eu_ai_act: "Non-discrimination requirements"
  subcategories:
    - id: dataset-bias
      label: "Dataset bias and under/over-representation"
    - id: proxy-discrimination
      label: "Proxy discrimination through correlated features"
```

What was previously a definition scattered across several documents becomes a single structured entry that feeds everything else.

## What happens next

1. **Consolidation:** We extract all categories and subcategories currently used across Eticas documents and unify them.
2. **Integration of the HR&A taxonomy:** Subcategories from the HR&A project that add value are incorporated into the base taxonomy.
3. **External linking:** For each category, we document equivalences with NIST, MIT, EU AI Act, OECD, ISO, and W3C DPV.
4. **Publication:** The repository is set up on GitHub with automatic generation of the reference site.
5. **Progressive adoption:** Eticas methodologies and documents begin referencing the taxonomy as their canonical source.

---

*Prepared as part of the Eticas risk taxonomy standardisation project, April 2026.*
