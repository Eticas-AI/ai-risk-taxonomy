---
layout: concept
title: "Security & Misuse"
id: security-misuse
uri: https://taxonomy.eticas.ai/risk/security-misuse
type: category
maturity: established
scope: ALL
---

# Security & Misuse

`https://taxonomy.eticas.ai/risk/security-misuse`

**Maturity:** <span class="badge badge-established">established</span>

The risk that an AI system is exposed to AI-specific vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality. This covers risks beyond traditional IT security, including adversarial inputs, prompt injection, model extraction, jailbreaking, and supply-chain risks specific to AI components. It is intended to complement, not replace, standard IT security assessments.

**Also known as:** Safety, Security & Misuse · Security · Safety

**Applies to:** ALL  
**Lifecycle stages:** Pre Processing, In Processing, Post Processing

## Risk groups

- [AI-specific attacks](security-ai-attacks.md) — Attack vectors specific to AI systems that exploit model behaviour or training processes.
- [System security](security-system.md) — Risks related to access control and integrity of the AI system and its supply chain.
- [Harmful Misuse](security-harmful-misuse.md) — Risks from deliberate misuse of the AI system to generate harmful content, manipulate users, or operate beyond its intended purpose. These risks involve human intent — distinguishing them from unintentional system failures (which belong under Reliability).

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 15(5) — cybersecurity (resilience against attacks) | close match |
| [AIUC-1 — AI Underwriting Company Standard](https://www.aiuc-1.com) | Security domain (and Society domain F for misuse) | close match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Information Security | close match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Secure & Resilient | close match |
| [OECD AI Principles](https://oecd.ai) | Robustness, security & safety | broad match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | AI system security vulnerabilities & attacks | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | Malicious Actors & Misuse | close match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | Security Attack | broad match |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | System & Operational Risks (Security + Operational Misuses) | close match |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Inference → Adversarial robustness + Non-technical → Misuse | close match |
