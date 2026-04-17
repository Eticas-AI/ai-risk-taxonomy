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

### Output quality

Risks related to the correctness, consistency, and robustness of system outputs.

- [Hallucination and fabricated outputs](hallucination.md)
- [Output inconsistency](output-inconsistency.md)
- [Output drift over time](output-drift.md)
- [Out-of-distribution robustness](out-of-distribution-robustness.md)

### Monitoring & remediation

Risks from inadequate monitoring, evaluation, and failure response.

- [Failure and remediation gaps](failure-remediation-gaps.md)
- [Monitoring and evaluation gaps](monitoring-evaluation-gaps.md)

### Manipulation & misinformation

Risks that the system produces or facilitates deceptive, manipulative, or misleading content, whether through design flaws or intentional misuse.

- [Disinformation generation](disinformation-generation.md)
- [Behavioural manipulation](behavioural-manipulation.md)
- [Synthetic media abuse](synthetic-media-abuse.md)

### Resilience

Risks related to the system's ability to absorb disruption, degrade gracefully, and recover. Particularly critical for AI deployed in conflict zones, humanitarian operations, or critical infrastructure.

- [Graceful degradation](graceful-degradation.md)
- [Edge and offline operability](edge-offline-operability.md)
- [Recovery capability](recovery-capability.md)
- [Infrastructure dependency](infrastructure-dependency.md)
- [Contextual and ethical resilience](contextual-resilience.md)

## Mappings to external frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Lack of capability or robustness | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | Misinformation | broad match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Confabulation | close match |
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Information Integrity | broad match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Valid & Reliable | close match |
| [OECD AI Principles](https://oecd.ai) | Robustness, security & safety | broad match |
