---
layout: concept
title: "Disparate impact on protected groups"
id: disparate-impact-protected-groups
uri: https://taxonomy.eticas.ai/risk/disparate-impact-protected-groups
type: subcategory
maturity: established
scope: ALL
broader: bias-outcome-disparities
---

# Disparate impact on protected groups

`https://taxonomy.eticas.ai/risk/disparate-impact-protected-groups`

**Maturity:** <span class="badge badge-established">established</span>

The system produces systematically different — typically worse — outcomes for individuals belonging to protected groups, including across multiple intersecting attributes (race, gender, age, disability, etc.). Encompasses unequal allocation of opportunity, quality of service disparities, intersectional unfairness, and accessibility barriers.

**Also known as:** Disparate impact · Quality of service disparity · Allocation of opportunity · Intersectional unfairness · Accessibility barriers

**Applies to:** ALL  
**Lifecycle stages:** Post Processing

## Mappings to external frameworks

### Compliance

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 5(1)(c) — prohibited social scoring | close match |
| [EU AI Act (Regulation 2024/1689)](https://artificialintelligenceact.eu) | Article 10 — data and data governance | close match |
| [ISO/IEC 42001:2023 — AI Management System](https://www.iso.org/standard/42001) | AI system impact assessment | close match |

### Reference frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [NIST AI 600-1 — Generative AI Risk Profile](https://doi.org/10.6028/NIST.AI.600-1) | Harmful Bias & Homogenization | broad match |
| [NIST AI Risk Management Framework (AI 100-1)](https://www.nist.gov/itl/ai-risk-management-framework) | Harmful bias / disparate performance | close match |

### Taxonomies & vocabularies

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Unfair discrimination and misrepresentation | close match |
| [MIT AI Risk Repository](https://airisk.mit.edu) | Unequal performance across groups | close match |
| [W3C Data Privacy Vocabulary — AI Extension](https://w3c.github.io/dpv/2.3/ai/) | [Discrimination](https://w3c.github.io/dpv/2.3/risk/#Discrimination) | close match |
| [AIR 2024 / AIR-Bench 2024](https://arxiv.org/abs/2406.17864) | Discrimination & Bias × Protected Characteristics (60 Level-4 risks) | close match |
| [IBM AI Risk Atlas](https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas) | Output → Fairness dimension | close match |

## How this risk manifests

The mechanisms below describe *how* this risk arises in practice. They are operationalisation aids, not risks in themselves — useful when designing assessment methods.

**Intersectional unfairness**  
Compounded disadvantage affecting individuals at the intersection of multiple protected characteristics (e.g., gender and ethnicity together producing worse outcomes than either alone).

**Accessibility barriers**  
System design that excludes or disadvantages people with disabilities, including inaccessible interfaces, outputs, or interaction modes.

**Quality of service disparity across groups**  
Inconsistent service quality across demographic groups, leading to systematically better performance for some groups over others.

**Unequal allocation of opportunity**  
AI system outputs that lead to the uneven allocation of opportunities (e.g., jobs, credit, services) across demographic groups.
