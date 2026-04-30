---
layout: concept
title: "Model-level privacy"
id: privacy-model-level
uri: https://taxonomy.eticas.ai/risk/privacy-model-level
type: subgroup
scope: ALL
broader: privacy-confidentiality
---

# Model-level privacy

`https://taxonomy.eticas.ai/risk/privacy-model-level`

Risks from AI models leaking or exposing private information through their outputs or structure.

## Subcategories

- [PII leakage through model outputs](pii-leakage.md)
- [Membership inference risk](membership-inference.md)

## Mappings to external frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Compromise of privacy by obtaining, leaking or inferring sensitive information | close match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | [Membership Inference Attack](https://w3c.github.io/dpv/2.3/ai/#MembershipInferenceAttack) | close match |

## References

- **[OpenAI Privacy Filter](https://github.com/openai/privacy-filter)** <sub>[tool]</sub>
  Open-source tool for detecting and filtering personally identifiable information in LLM inputs and outputs.
