---
layout: concept
title: "Differential performance across populations"
id: performance-equity
uri: https://taxonomy.eticas.ai/risk/performance-equity
type: subcategory
maturity: emerging
scope: ALL
broader: bias-outcome-disparities
---

# Differential performance across populations

`https://taxonomy.eticas.ai/risk/performance-equity`

**Maturity:** <span class="badge badge-emerging">emerging</span>

The AI system performs systematically worse for some demographic groups than others — through higher error rates, lower accuracy, or reduced reliability — leading to unequal quality of service even when access is the same.

> **This subcategory is emerging.** It has not yet been validated through established assessment methods.

**Also known as:** Group-wise error rate · Performance equity across populations

**Applies to:** ALL  
**Lifecycle stages:** In Processing, Post Processing

## Mappings to external frameworks

| Framework | Concept | Relationship |
|-----------|---------|-------------|
| [MIT AI Risk Repository](https://airisk.mit.edu) | Unequal performance across groups | close match |

## How this risk manifests

The mechanisms below describe *how* this risk arises in practice. They are operationalisation aids, not risks in themselves — useful when designing assessment methods.

**Dataset bias and under/over-representation**  
Training or evaluation data that does not adequately represent all relevant population groups, leading to systematic performance differences or exclusion of certain groups.

**Proxy discrimination through correlated features**  
Discrimination through features that correlate with protected attributes (e.g., postcode as proxy for ethnicity), even when protected attributes are not directly used.

*Source: HRA project taxonomy*
