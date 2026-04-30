---
layout: concept
title: "PII leakage through model outputs"
id: pii-leakage
uri: https://taxonomy.eticas.ai/risk/pii-leakage
type: subcategory
maturity: established
scope: LLM
broader: privacy-model-level
---

# PII leakage through model outputs

`https://taxonomy.eticas.ai/risk/pii-leakage`

**Maturity:** <span class="badge badge-established">established</span>

Personal data present in training data surfacing in model outputs, either through memorisation or through responses that reveal sensitive information about individuals.

**Also known as:** PII leakage rate · Privacy leakage

**Applies to:** LLM  
**Lifecycle stages:** In Processing, Post Processing

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 15(5) — cybersecurity (confidentiality attacks) | narrow match |
| [AIUC-1 — AI Underwriting Company Standard](https://www.aiuc-1.com) | Prevent PII leakage | exact match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Data Privacy (leakage clause) | close match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Compromise of privacy by leaking or inferring sensitive information | exact match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | [Unauthorised Data Disclosure](https://w3c.github.io/dpv/2.3/risk/#UnauthorisedDataDisclosure) | close match |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | Privacy → Unauthorized Privacy Violations × PII | exact match |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Output → Revealing personal information in output | exact match |

*Source: HRA project taxonomy*
