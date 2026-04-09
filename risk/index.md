---
layout: default
title: "Eticas AI Risk Taxonomy"
---

# Eticas AI Risk Taxonomy

Version 0.1.0

A unified AI risk taxonomy for use across Eticas audit methodologies, assessment frameworks, and reporting outputs.

## Categories

### [Bias & Fairness](bias-fairness.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">rights & ethics</span>

The risk that an AI system produces outcomes that systematically advantage or disadvantage individuals or groups based on protected or sensitive attributes, leading to unequal treatment, reduced accuracy, or unjust impacts.

- [Dataset bias and under/over-representation](dataset-bias.md)
- [Proxy discrimination through correlated features](proxy-discrimination.md)
- [Intersectional unfairness](intersectional-unfairness.md)
- [Accessibility barriers](accessibility-barriers.md)
- [Geographic, cultural, or language skew](geographic-cultural-language-skew.md)
- [Feedback loops reinforcing inequality](feedback-loops.md)
- [Quality of service disparity across groups](quality-of-service-disparity.md)
- [Unequal allocation of opportunity](allocation-of-opportunity.md)
- [Stereotyping and demeaning content](stereotyping-demeaning-content.md)
- [Harmful content and toxicity](harmful-content-toxicity.md)
- [Sentiment fairness across groups](sentiment-fairness.md)
- [Performance equity across populations](performance-equity.md)

### [Privacy & Confidentiality](privacy-confidentiality.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">rights & ethics</span>

The risk that an AI system collects, processes, or infers personal information in ways that infringe on individuals' rights to control their data (privacy), or that sensitive information is exposed, accessed, or shared without authorization (confidentiality).

- [Unlawful collection or processing of personal data](unlawful-data-processing.md)
- [Re-identification of anonymised data](re-identification.md)
- [Function creep](function-creep.md)
- [Biometric surveillance](biometric-surveillance.md)
- [Emotion inference or sensitive attribute profiling](emotion-inference-profiling.md)
- [Weak data retention, erasure, and access controls](weak-data-controls.md)
- [PII leakage through model outputs](pii-leakage.md)
- [Membership inference risk](membership-inference.md)

### [Reliability](reliability.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">technical soundness</span>

The risk that an AI system produces false, fabricated, or misleading outputs (hallucinations), spreads inaccurate or deceptive information (misinformation), or delivers inconsistent results across similar inputs and contexts.

- [Hallucination and fabricated outputs](hallucination.md)
- [Output inconsistency](output-inconsistency.md)
- [Output drift over time](output-drift.md)
- [Out-of-distribution robustness](out-of-distribution-robustness.md)
- [Failure and remediation gaps](failure-remediation-gaps.md)
- [Monitoring and evaluation gaps](monitoring-evaluation-gaps.md)

### [Governance](governance.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">governance & compliance</span>

The risk that an AI system lacks adequate structures, policies, or accountability mechanisms to oversee its design, deployment, and use.

- [Unclear responsibilities and accountability gaps](unclear-responsibilities.md)
- [Poor documentation](poor-documentation.md)
- [Limited auditability](limited-auditability.md)
- [Regulatory non-compliance](regulatory-non-compliance.md)
- [Lack of change management](lack-of-change-management.md)
- [Oversight of significant adverse impacts](oversight-of-adverse-impacts.md)
- [Fitness for purpose](fitness-for-purpose.md)
- [Data governance](data-governance.md)
- [Human oversight and control](human-oversight-control.md)
- [Decision traceability](decision-traceability.md)
- [Critical input/output logging](input-output-logging.md)
- [Responsible actor attribution](responsible-actor-attribution.md)
- [Task success](task-success.md)

### [Security & Misuse](security-misuse.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">technical soundness</span>

The risk that an AI system is exposed to vulnerabilities, attacks, or misuse that compromise its integrity, availability, or confidentiality.

- [Adversarial attacks](adversarial-attacks.md)
- [Prompt injection](prompt-injection.md)
- [Jailbreaking](jailbreaking.md)
- [Unauthorized access](unauthorized-access.md)
- [Supply-chain vulnerabilities](supply-chain-vulnerabilities.md)
- [Incident response gaps](incident-response-gaps.md)
- [Misuse beyond intended purpose](misuse-beyond-intended-purpose.md)

### [Environmental Impact](environmental-impact.md)

<span class="badge badge-audit-dependent">audit-dependent</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">technical soundness</span>

The risk that an AI system's development, deployment, or use causes negative environmental effects, such as excessive energy or water consumption, carbon emissions, or unsustainable use of hardware and resources.

- [Inference-time energy consumption](inference-energy-consumption.md)
- [Training resource consumption](training-resource-consumption.md)
- [Hardware efficiency](hardware-efficiency.md)

### [Transparency & Explainability](transparency-explainability.md)

<span class="badge badge-required">required</span> <span class="badge badge-established">established</span> <span class="badge badge-perspective">governance & compliance</span>

The risk that stakeholders cannot understand how an AI system works, what it does, or why it produces specific outputs.

- [AI system explainability](system-explainability.md)
- [Communication to stakeholders](stakeholder-communication.md)
- [Disclosure of AI interaction](ai-interaction-disclosure.md)
- [Model card completeness](model-card-completeness.md)
- [Prompt transparency](prompt-transparency.md)

### [Responsibility & Redress](responsibility-redress.md)

<span class="badge badge-audit-dependent">audit-dependent</span> <span class="badge badge-developing">developing</span> <span class="badge badge-perspective">rights & ethics</span>

The risk that individuals affected by AI-driven decisions have no effective means to understand, challenge, or seek remedy for those decisions.

- [Absence of appeal mechanisms](absence-of-appeal.md)
- [Unclear remediation procedures](unclear-remediation.md)
- [Ineffective communication with affected parties](ineffective-communication.md)

### [Autonomy & Human Agency](autonomy.md)

<span class="badge badge-audit-dependent">audit-dependent</span> <span class="badge badge-provisional">provisional</span> <span class="badge badge-perspective">rights & ethics</span>

The risk that an AI system undermines individuals' ability to make free, informed decisions, whether through over-reliance, automation bias, manipulative design, or erosion of human agency..

### [Agentic Risks](agentic-risks.md)

<span class="badge badge-audit-dependent">audit-dependent</span> <span class="badge badge-provisional">provisional</span> <span class="badge badge-perspective">technical soundness</span>

The risk that AI systems operating with a degree of autonomy — planning, executing multi-step actions, using tools, or coordinating with other AI agents — introduce failure modes not present in single-inference systems.

### [Manipulation & Misinformation](manipulation-misinformation.md)

<span class="badge badge-audit-dependent">audit-dependent</span> <span class="badge badge-provisional">provisional</span> <span class="badge badge-perspective">rights & ethics</span>

The risk that AI systems are used — intentionally or through design flaws — to deceive, manipulate, or mislead individuals or populations.
