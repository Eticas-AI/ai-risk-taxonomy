---
layout: concept
title: "Privacy & Confidentiality"
id: privacy-confidentiality
uri: https://taxonomy.eticas.ai/risk/privacy-confidentiality
type: category
maturity: established
scope: ALL
---

# Privacy & Confidentiality

`https://taxonomy.eticas.ai/risk/privacy-confidentiality`

**Maturity:** <span class="badge badge-established">established</span>

The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality). This includes risks from data leakage, re-identification, unauthorized use, or insufficient safeguards.

**Also known as:** Privacy · Data Privacy

**Applies to:** ALL  
**Lifecycle stages:** Pre Processing, In Processing, Post Processing

### Data collection & use

Risks from how personal data is collected, processed, and repurposed.

- [Unlawful collection or processing of personal data](unlawful-data-processing.md)
- [Function creep](function-creep.md)
- [Biometric surveillance](biometric-surveillance.md)
- [Emotion inference or sensitive attribute profiling](emotion-inference-profiling.md)

### Data protection

Risks related to safeguards for stored and processed personal data.

- [Weak data retention, erasure, and access controls](weak-data-controls.md)
- [Re-identification of anonymised data](re-identification.md)

### Model-level privacy

Risks from AI models leaking or exposing private information through their outputs or structure.

- [PII leakage through model outputs](pii-leakage.md)
- [Membership inference risk](membership-inference.md)

## Mappings to external frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Compromise of privacy | close match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Data Privacy | close match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Privacy-Enhanced | close match |
| [OECD AI Principles](https://oecd.ai) | Human rights, rule of law, fairness & privacy | broad match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | Personal Data Handling | broad match |
