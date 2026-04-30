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

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Lack of capability or robustness | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | Misinformation | broad match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Confabulation | close match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Information Integrity | broad match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Valid & Reliable | close match |
| [OECD AI Principles](https://oecd.ai) | Robustness, security & safety | broad match |

## References

- **[HealthBench Professional (OpenAI, 2025)](https://cdn.openai.com/dd128428-0184-4e25-b155-3a7686c7d744/HealthBench-Professional.pdf)** <sub>[benchmark, domain: healthcare]</sub>
  Benchmark for evaluating LLM reliability and accuracy in professional healthcare contexts. Useful when auditing AI systems deployed in health domains.
