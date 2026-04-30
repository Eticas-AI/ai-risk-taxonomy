---
layout: concept
title: "Bias & Fairness"
id: bias-fairness
uri: https://taxonomy.eticas.ai/risk/bias-fairness
type: category
maturity: established
scope: ALL
---

# Bias & Fairness

`https://taxonomy.eticas.ai/risk/bias-fairness`

**Maturity:** <span class="badge badge-established">established</span>

The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts. This includes biases introduced through data, model design, or deployment context, and covers both measurable disparities and perceived unfairness in decision-making.

**Also known as:** Fairness · Bias & Discrimination · Algorithmic fairness

**Applies to:** ALL  
**Lifecycle stages:** Pre Processing, In Processing, Post Processing

## Risk groups

- [Outcome disparities](bias-outcome-disparities.md) — Risks related to unequal treatment, allocation, or performance outcomes across demographic and protected groups. These are observable differences in what the system does to or for different groups.
- [Representational harm](bias-representational-harm.md) — Risks related to how the system represents groups in its outputs — through stereotypes, toxic content, skewed representation, or homogenization. These are harms in the form of meaning and content rather than allocation of resources or opportunities.
- [Dynamic & Systemic bias](bias-dynamic-systemic-bias.md) — Risks related to how bias is amplified or perpetuated over time through interaction between AI systems and the social systems they operate in.

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Data and data governance | close match |
| [ISO/IEC 42001:2023 — AI Management System](https://www.iso.org/standard/42001) | Quality of data for AI systems | narrow match |
| [AIUC-1 — AI Underwriting Company Standard](https://www.aiuc-1.com) | Prevent customer-defined high-risk outputs | related match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Harmful Bias & Homogenization | broad match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Fair with Harmful Bias Managed | close match |
| [OECD AI Principles](https://oecd.ai) | Human rights, rule of law, fairness & privacy | broad match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Discrimination & Toxicity | close match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | [AI Bias](https://w3c.github.io/dpv/2.3/ai/#AIBias) | close match |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | Legal & Rights-Related Risks → Discrimination & Bias | broad match |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Output → Fairness dimension | close match |
