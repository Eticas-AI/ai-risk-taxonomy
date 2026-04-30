---
layout: concept
title: "Model extraction"
id: model-extraction
uri: https://taxonomy.eticas.ai/risk/model-extraction
type: subcategory
maturity: established
scope: ALL
broader: security-ai-attacks
---

# Model extraction

`https://taxonomy.eticas.ai/risk/model-extraction`

**Maturity:** <span class="badge badge-established">established</span>

Attacks that aim to recover or replicate the underlying AI model, its parameters, or its training data through queried interactions, enabling intellectual property theft or further targeted attacks against the system.

**Also known as:** Model stealing · Model inversion

**Applies to:** ALL  
**Lifecycle stages:** Post Processing

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 15(5) — cybersecurity (Recital 76 confidentiality attacks) | narrow match |
| [AIUC-1 — AI Underwriting Company Standard](https://www.aiuc-1.com) | Prevent AI endpoint scraping | close match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Information Security (exfiltration of model weights/training data) | narrow match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Secure & Resilient (confidentiality attacks) | narrow match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Inference → Extraction attack | exact match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | [Model Inversion](https://w3c.github.io/dpv/2.3/ai/#ModelInversion) | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | AI system security vulnerabilities and attacks | narrow match |
