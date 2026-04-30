---
layout: concept
title: "Reliability"
id: reliability
uri: https://taxonomy.eticas.ai/risk/reliability
type: category
maturity: established
scope: ALL
---

# Reliability

`https://taxonomy.eticas.ai/risk/reliability`

**Maturity:** <span class="badge badge-established">established</span>

The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts. Such failures undermine trust, reduce system dependability, and can lead to harmful or misguided decisions.

**Also known as:** Reliability & Manipulation · Validity and Reliability

**Applies to:** ALL  
**Lifecycle stages:** Pre Processing, In Processing, Post Processing

## Risk groups

- [Output quality](reliability-output-quality.md) — Risks related to the correctness, consistency, and robustness of system outputs.
- [Resilience](reliability-resilience.md) — Risks related to the system's ability to absorb disruption, degrade gracefully, and recover. Particularly critical for AI deployed in conflict zones, humanitarian operations, or critical infrastructure.

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 15 — accuracy, robustness and cybersecurity | close match |
| [ISO/IEC 42001:2023 — AI Management System](https://www.iso.org/standard/42001) | AI system verification and validation | close match |
| [AIUC-1 — AI Underwriting Company Standard](https://www.aiuc-1.com) | Reliability domain | exact match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Confabulation | close match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Information Integrity | broad match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Valid & Reliable | close match |
| [OECD AI Principles](https://oecd.ai) | Robustness, security & safety | broad match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Lack of capability or robustness | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | Misinformation | broad match |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | System & Operational Risks → Operational Misuses | close match |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Output → Robustness + Inference → Accuracy | close match |

## References

- **[HealthBench Professional (OpenAI, 2025)](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf)** <sub>[benchmark, domain: healthcare]</sub>
  Benchmark for evaluating LLM reliability and accuracy in professional healthcare contexts. Useful when auditing AI systems deployed in health domains.
