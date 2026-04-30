# Framework Mapping Verification — Eticas AI Risk Taxonomy v0.3

This document records the verification and expansion of the external framework mappings for the v0.3 restructuring. It serves as the working reference for refining mappings in the YAML and as the input for review with the methodology team. Mapping decisions captured here will be applied to `src/taxonomy.yaml` and `src/mappings.yaml` during Phase 5.

> **Status:** First draft (April 2026), based on automated research with sources cited inline. Pending validation by the methodology team. Mappings should be considered tentative until validated.

## Methodology

This report verifies and expands the framework mappings for Eticas AI Risk Taxonomy v0.3 (9 top-level categories: Bias & Fairness, Privacy & Confidentiality, Reliability, Governance, Security & Misuse, Environmental Impact, Transparency & Explainability, Autonomy & Agency, Organisational Readiness). Each external framework was consulted in its most recent published version available as of April 2026:

- **NIST AI RMF (AI 100-1)**, January 2023, four-function model (Govern/Map/Measure/Manage) and seven characteristics of trustworthy AI.
- **NIST AI 600-1 (Generative AI Profile)**, July 2024, the 12 GAI risk categories.
- **EU AI Act (Regulation (EU) 2024/1689)**, Official Journal version of 13 June 2024, with article-level references.
- **MIT AI Risk Repository V4**, December 2025, 7 domains and 24 subdomains (1,725 risks from 74 frameworks).
- **W3C DPV v2.3** (Final Community Group Report, 25 February 2026), AI Extension and Risk Extension; the only SKOS-native target with formal IRIs.
- **ISO/IEC 42001:2023**, AI Management Systems, Annex A (42 control objectives across 9 topics A.2–A.10).
- **OECD AI Principles** (2024 update), five values-based principles (1.1–1.5) and five recommendations (2.1–2.5).
- **AIUC-1** (Q2-2026 release), six core domains (A. Data & Privacy; B. Security; C. Safety; D. Reliability; E. Accountability; F. Society) with ~55 controls.
- **AIR 2024 / AIR-Bench 2024** (Zeng et al.), four Level-1 categories, 16 Level-2, 45 Level-3 and 314 Level-4 risk categories derived from 8 government regulations and 16 corporate policies.
- **IBM AI Risk Atlas** (2024–2025, integrated into IBM Risk Atlas Nexus), risks organised by lifecycle stage (Input / Inference / Output / Non-technical) with dimensions such as Fairness, Robustness, Explainability, Privacy, Value Alignment, Misuse, Governance.

For each mapping, the SKOS match type is judged from the perspective of the Eticas concept ("from Eticas to framework"): `broadMatch` means the framework concept is broader; `narrowMatch` means it is narrower; `closeMatch` and `relatedMatch` are used when scope partially overlaps but is not identical. The mappings cover Eticas categories, sub-groups, and individual subcategories. Citations are short paraphrases or direct quotes of the framework's own wording, sufficient for a reader to evaluate the relationship.

---

## 1. NIST AI RMF (AI 100-1)

**Framework summary.** NIST AI 100-1 (January 2023) defines four functions — Govern, Map, Measure, Manage — and seven characteristics of trustworthy AI: Valid & Reliable; Safe; Secure & Resilient; Accountable & Transparent; Explainable & Interpretable; Privacy-Enhanced; Fair – with Harmful Bias Managed. Source: https://www.nist.gov/itl/ai-risk-management-framework

### Mappings table

| Eticas concept (id) | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | Fair – with Harmful Bias Managed (trustworthy characteristic) | closeMatch | "Fairness in AI includes concerns for equality and equity by addressing issues such as harmful bias and discrimination." | nist.gov/itl/ai-risk-management-framework |
| bias-outcome-disparities (sub-group) | Manage 2.3 (allocation harms) and Measure 2.11 (fairness metrics) | closeMatch | The RMF references unequal performance and allocation across demographic groups as a core fairness concern measured under Measure 2.11. | nist.gov/itl/ai-risk-management-framework |
| disparate-impact-protected-groups (subcategory) | Harmful bias / disparate performance | closeMatch | "Systemic, computational and statistical, and human-cognitive biases ... can result in harmful outcomes that disproportionately affect specific groups." | nist.gov/itl/ai-risk-management-framework |
| bias-representational-harm (sub-group) | Harmful bias (representational dimension) | narrowMatch | Bias as discussed in NIST AI 100-1 includes representational harms but is broader than this Eticas sub-group. | nist.gov/itl/ai-risk-management-framework |
| bias-dynamic-systemic-bias (sub-group) | Systemic bias under "harmful bias" | closeMatch | "Systemic biases ... result from procedures and practices ... that operate in ways that result in certain social groups being advantaged." | nist.gov/itl/ai-risk-management-framework |
| homogenization-output-across-groups (subcategory) | (no direct equivalent — closest: "harmful bias" / Measure 2.11) | relatedMatch | RMF discusses outcome variance across groups; output homogenization is implicit but not named. | nist.gov/itl/ai-risk-management-framework |
| privacy-and-confidentiality (category) | Privacy-Enhanced (trustworthy characteristic) | closeMatch | "Privacy refers generally to the norms and practices that help to safeguard human autonomy, identity, and dignity." | nist.gov/itl/ai-risk-management-framework |
| reliability (category) | Valid & Reliable (trustworthy characteristic) | closeMatch | "Validity and reliability for deployed AI systems are often assessed by ongoing testing or monitoring that confirms a system is performing as intended." | nist.gov/itl/ai-risk-management-framework |
| reliability-output-quality / hallucination | Valid & Reliable (and Measure 2.5: deployed system valid & reliable) | broadMatch | Validity and reliability cover hallucination/output quality but also broader behavioural correctness. | nist.gov/itl/ai-risk-management-framework |
| governance (category) | Govern function (entire) | closeMatch | "The Govern function cultivates and implements a culture of risk management within organizations developing, deploying or acquiring AI systems." | nist.gov/itl/ai-risk-management-framework |
| governance-compliance (sub-group) | Govern 1, Govern 4, Govern 5 (policy, accountability, third-party risk) | closeMatch | Govern 1: "Policies, processes, procedures, and practices ... are in place, transparent, and implemented effectively." | nist.gov/itl/ai-risk-management-framework |
| governance-monitoring-incident-response (subcategory area) | Manage 4 (post-deployment monitoring & incident response) | closeMatch | Manage 4: "Risk treatments, including response and recovery, and communication plans for the identified and measured AI risks, are documented and monitored regularly." | nist.gov/itl/ai-risk-management-framework |
| security-and-misuse (category) | Secure & Resilient (trustworthy characteristic) | broadMatch | "AI systems ... that can withstand unexpected adverse events or unexpected changes ... and ... maintain their functions and structure." | nist.gov/itl/ai-risk-management-framework |
| model-extraction (subcategory) | Secure & Resilient (model exfiltration is referenced under adversarial ML; see also AI 100-2 E2025) | narrowMatch | NIST AI 100-2 catalogues model extraction/stealing as a confidentiality attack on ML systems. | csrc.nist.gov/pubs/ai/100/2 |
| data-poisoning (subcategory) | Secure & Resilient / Adversarial ML | narrowMatch | NIST AI 100-2 E2025 lists data poisoning among the principal training-time attacks. | csrc.nist.gov/pubs/ai/100/2 |
| security-harmful-misuse (sub-group) | Safe (trustworthy characteristic) and Manage 2.4 | closeMatch | "AI systems should not under defined conditions, lead to a state in which human life, health, property, or the environment is endangered." | nist.gov/itl/ai-risk-management-framework |
| environmental-impact (category) | (no explicit characteristic; touched in Map 5 "impacts to individuals, groups, communities, organizations, and society") | relatedMatch | Environmental impact is acknowledged among potential impacts but not separately enumerated in AI 100-1. | nist.gov/itl/ai-risk-management-framework |
| transparency-and-explainability (category) | Accountable & Transparent + Explainable & Interpretable | exactMatch | "Transparency reflects the extent to which information about an AI system and its outputs is available to individuals interacting with such a system." | nist.gov/itl/ai-risk-management-framework |
| right-to-explanation-contestation (subcategory) | Accountable & Transparent (Govern 1.5; Manage 4.3) | narrowMatch | Accountability and transparency in AI 100-1 imply enabling redress but do not specifically name a "right to contestation." | nist.gov/itl/ai-risk-management-framework |
| autonomy-and-agency (category) | Govern 3 (human–AI configurations) and Manage 1 (risk-prioritised oversight) | relatedMatch | The RMF treats human oversight rather than autonomy/agency as a discrete concept. | nist.gov/itl/ai-risk-management-framework |
| organisational-readiness (category) | Govern 2 (accountability structures) and Govern 4 (workforce) | broadMatch | Govern 4: "Organizational teams are committed to a culture that considers and communicates AI risk." | nist.gov/itl/ai-risk-management-framework |

---

## 2. NIST AI 600-1 (Generative AI Profile)

**Framework summary.** Published July 2024, NIST-AI-600-1 enumerates 12 risk categories unique to or exacerbated by generative AI: (1) CBRN Information or Capabilities; (2) Confabulation; (3) Dangerous, Violent or Hateful Content; (4) Data Privacy; (5) Environmental Impacts; (6) Harmful Bias or Homogenization; (7) Human-AI Configuration; (8) Information Integrity; (9) Information Security; (10) Intellectual Property; (11) Obscene, Degrading and/or Abusive Content; (12) Value Chain and Component Integration. Source: https://doi.org/10.6028/NIST.AI.600-1

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | #6 Harmful Bias or Homogenization | broadMatch | "Amplification and exacerbation of historical, societal, and systemic biases; performance disparities ... [and] homogenization of outputs across users and contexts." | airc.nist.gov/AI_RMF_Knowledge_Base/Playbook |
| homogenization-output-across-groups | #6 Harmful Bias or Homogenization (homogenization clause) | exactMatch | "Homogenization of outputs across users and contexts ... can also amplify and entrench bias." | airc.nist.gov AI 600-1 §2.6 |
| disparate-impact-protected-groups | #6 Harmful Bias or Homogenization | broadMatch | NIST 600-1 frames disparate impact under harmful bias for GAI, broader than disparate impact alone. | airc.nist.gov AI 600-1 §2.6 |
| privacy-and-confidentiality (category) | #4 Data Privacy | broadMatch | "Impacts due to leakage and unauthorized use, disclosure, or de-anonymization of biometric, health, location, or other personally identifiable information." | airc.nist.gov AI 600-1 §2.4 |
| pii-leakage-through-model-outputs | #4 Data Privacy (leakage clause) | closeMatch | "Leakage and unauthorized disclosure ... of personally identifiable information." | airc.nist.gov AI 600-1 §2.4 |
| reliability (category) | #2 Confabulation + #8 Information Integrity | closeMatch | "Confabulation: The production of confidently stated but erroneous or false content (known colloquially as 'hallucinations' or 'fabrications')." | airc.nist.gov AI 600-1 §2.2 |
| reliability-hallucination | #2 Confabulation | exactMatch | Same as above. | airc.nist.gov AI 600-1 §2.2 |
| security-and-misuse (category) | #9 Information Security + #1 CBRN + #10 IP | broadMatch | "Lowered barriers to ... cyber attacks ... and the discovery of new cybersecurity vulnerabilities." | airc.nist.gov AI 600-1 §2.9 |
| security-harmful-misuse (sub-group) | #1 CBRN + #3 Dangerous/Violent/Hateful + #11 Obscene/Abusive | closeMatch | "Eased access to or synthesis of materially nefarious information or design capabilities related to chemical, biological, radiological, or nuclear weapons." | airc.nist.gov AI 600-1 §2.1 |
| model-extraction | #9 Information Security (extraction sub-clause) | narrowMatch | Risks include "exfiltration ... of training data or model weights." | airc.nist.gov AI 600-1 §2.9 |
| data-poisoning | #9 Information Security (poisoning) | narrowMatch | Lists data poisoning as a key adversarial GAI security concern. | airc.nist.gov AI 600-1 §2.9 |
| environmental-impact (category) | #5 Environmental Impacts | exactMatch | "Impacts due to high compute resource utilization in training or operating GAI models, and related outcomes that may adversely impact ecosystems." | airc.nist.gov AI 600-1 §2.5 |
| transparency-and-explainability | #8 Information Integrity (provenance) and #12 Value Chain | closeMatch | "Lowered barriers to entry ... [for] disinformation or misinformation"; provenance and disclosure mechanisms are key mitigations. | airc.nist.gov AI 600-1 §2.8 |
| right-to-explanation-contestation | (no direct counterpart; closest #7 Human-AI Configuration) | relatedMatch | "Arrangements between human and AI ... that may result in failures, fatigue, biases, or misuse." | airc.nist.gov AI 600-1 §2.7 |
| autonomy-and-agency (category) | #7 Human-AI Configuration | closeMatch | Same as above; covers over-reliance, anthropomorphism, automation bias. | airc.nist.gov AI 600-1 §2.7 |
| governance (category) | #12 Value Chain and Component Integration | narrowMatch | "Non-transparent or untraceable integration of upstream third-party components ... and inconsistent ... oversight." | airc.nist.gov AI 600-1 §2.12 |
| governance-compliance (sub-group) | #12 Value Chain + cross-cutting governance actions | broadMatch | NIST 600-1 governance actions span all 12 risk categories rather than being a single bucket. | airc.nist.gov AI 600-1 |
| organisational-readiness | #12 Value Chain + #7 Human-AI Configuration | relatedMatch | Workforce readiness is implicit in Human-AI Configuration risks. | airc.nist.gov AI 600-1 |
| manipulation/misinformation harm (now Security & Misuse sub-group) | #8 Information Integrity + #3 Dangerous/Violent/Hateful Content | closeMatch | "Lowered barrier to entry to generate and support the exchange and consumption of content which may not distinguish fact from opinion or fiction." | airc.nist.gov AI 600-1 §2.8 |

---

## 3. EU AI Act (Regulation (EU) 2024/1689)

**Framework summary.** The EU AI Act establishes a risk-based regime: prohibited practices (Art. 5), high-risk AI requirements (Arts. 9–15), transparency obligations (Art. 50), GPAI/systemic-risk obligations (Arts. 51–55), and post-market monitoring/incident reporting (Arts. 72–73). Source: https://artificialintelligenceact.eu

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | Art. 10 (Data and data governance) + Recital 27 (fairness) | closeMatch | Art. 10(2)(f-g): training, validation and testing data sets shall be examined "in view of possible biases ... that are likely to affect the health and safety of persons, have a negative impact on fundamental rights or lead to discrimination prohibited under Union law." | artificialintelligenceact.eu/article/10 |
| bias-outcome-disparities | Art. 10 + Annex III categories (employment, education, essential services) | closeMatch | High-risk uses listed in Annex III explicitly cover access to essential services, employment, and education where outcome disparities are central. | artificialintelligenceact.eu/annex/3 |
| disparate-impact-protected-groups | Art. 10 + Recital 67 + Art. 5(1)(c) social scoring | closeMatch | Art. 5(1)(c) prohibits social scoring "leading to detrimental or unfavourable treatment of certain natural persons or groups thereof." | artificialintelligenceact.eu/article/5 |
| bias-representational-harm | Recital 27 (diversity, non-discrimination) | relatedMatch | Recital 27 calls for "diversity, non-discrimination and fairness" but representational harm in generative outputs is not explicitly enumerated. | eur-lex.europa.eu (Regulation 2024/1689) |
| bias-dynamic-systemic-bias | Art. 9 (risk management throughout lifecycle) + Art. 72 (post-market monitoring) | closeMatch | Art. 9 requires "a continuous iterative process ... throughout the entire lifecycle of a high-risk AI system" addressing bias as it evolves. | artificialintelligenceact.eu/article/9 |
| homogenization-output-across-groups | (no direct provision) | relatedMatch | The Act does not name homogenization; only general fairness/bias provisions apply. | — |
| privacy-and-confidentiality (category) | Art. 10 (Data governance) + GDPR cross-references | broadMatch | Art. 10(5) allows special-category data processing only with appropriate safeguards; GDPR governs personal data more broadly. | artificialintelligenceact.eu/article/10 |
| pii-leakage-through-model-outputs | Art. 15 (cybersecurity) + Recital 75 | narrowMatch | Art. 15(5): "high-risk AI systems shall be resilient against attempts ... to alter their use, outputs or performance by exploiting system vulnerabilities," which includes inversion/leakage. | artificialintelligenceact.eu/article/15 |
| reliability (category) | Art. 15 (Accuracy, robustness and cybersecurity) | closeMatch | "High-risk AI systems shall be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle." | artificialintelligenceact.eu/article/15 |
| reliability-hallucination | Art. 15 (accuracy) + Art. 50 (deepfake transparency) | narrowMatch | Accuracy obligations cover factual reliability; Art. 50 requires labelling of AI-generated content. | artificialintelligenceact.eu/article/15 |
| governance (category) | Art. 17 (Quality Management System) + Art. 9 (Risk Management) | closeMatch | Art. 17: providers "shall put a quality management system in place that ensures compliance with this Regulation." | artificialintelligenceact.eu/article/17 |
| governance-compliance (sub-group) | Art. 9, 17, 26 (deployers), 72 (post-market monitoring), 73 (serious incidents) | broadMatch | Art. 73(1): providers "shall report any serious incident to the market surveillance authorities of the Member States." | artificialintelligenceact.eu/article/73 |
| governance-monitoring-incident-response | Art. 72 + Art. 73 | exactMatch | Art. 72: "Providers shall establish and document a post-market monitoring system." | artificialintelligenceact.eu/article/72 |
| security-and-misuse (category) | Art. 15 (cybersecurity) + Art. 5 (prohibited manipulative practices) | closeMatch | Art. 15 requires resilience against "attempts by unauthorised third parties to alter their use, outputs or performance." | artificialintelligenceact.eu/article/15 |
| security-harmful-misuse (sub-group) | Art. 5(1)(a-b) (manipulation, exploitation of vulnerabilities) + Art. 51 (systemic-risk GPAI) | closeMatch | Art. 5(1)(a) prohibits AI systems deploying "subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques." | artificialintelligenceact.eu/article/5 |
| model-extraction | Art. 15(5) (cybersecurity attacks) | narrowMatch | Cybersecurity provisions cover "model evasion or model poisoning, training data poisoning, model evasion (adversarial examples) or confidentiality attacks." (Recital 76) | artificialintelligenceact.eu/article/15 |
| data-poisoning | Art. 15(5) + Recital 76 | exactMatch | Recital 76 expressly enumerates "data poisoning." | eur-lex.europa.eu Regulation 2024/1689 Recital 76 |
| environmental-impact (category) | Art. 95 (codes of conduct, sustainability) + Recital 139 | relatedMatch | Recital 139 encourages voluntary codes addressing "environmental sustainability of AI systems, including ... energy-efficient programming." | artificialintelligenceact.eu/article/95 |
| transparency-and-explainability (category) | Art. 13 (transparency to deployers) + Art. 50 (transparency to end users) | closeMatch | Art. 13(1): high-risk AI systems "shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent." | artificialintelligenceact.eu/article/13 |
| right-to-explanation-contestation | Art. 86 (Right to explanation of individual decision-making) | exactMatch | Art. 86(1): "Any affected person ... shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure." | artificialintelligenceact.eu/article/86 |
| autonomy-and-agency (category) | Art. 14 (Human oversight) | closeMatch | "High-risk AI systems shall be designed and developed in such a way ... that they can be effectively overseen by natural persons during the period in which they are in use." | artificialintelligenceact.eu/article/14 |
| organisational-readiness | Art. 4 (AI literacy) + Art. 26 (deployer obligations) | closeMatch | Art. 4: providers and deployers "shall take measures to ensure ... a sufficient level of AI literacy of their staff." | artificialintelligenceact.eu/article/4 |

---

## 4. MIT AI Risk Repository V4 (December 2025)

**Framework summary.** V4 organises 1,725 risks from 74 frameworks into 7 domains and 24 subdomains: (1) Discrimination & toxicity [1.1 Unfair discrimination & misrepresentation; 1.2 Exposure to toxic content; 1.3 Unequal performance across groups]; (2) Privacy & security [2.1 Compromise of privacy by leaking/inferring; 2.2 AI system security vulnerabilities & attacks]; (3) Misinformation [3.1 False or misleading information; 3.2 Pollution of information ecosystem]; (4) Malicious actors & misuse [4.1 Disinformation/influence ops; 4.2 Cyberattacks/weapons; 4.3 Fraud, scams & targeted manipulation]; (5) Human-computer interaction [5.1 Overreliance; 5.2 Loss of agency/autonomy]; (6) Socioeconomic & environmental [6.1 Power centralisation; 6.2 Increased inequality; 6.3 Economic/cultural devaluation; 6.4 Competitive dynamics; 6.5 Governance failure; 6.6 Environmental harm]; (7) AI system safety, failures & limitations [7.1 AI pursuing own goals; 7.2 AI welfare & rights; 7.3 Lack of capability or robustness; 7.4 Multi-agent risks; 7.5 Lack of transparency/interpretability; 7.6 Other system failures]. Source: https://airisk.mit.edu

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | Domain 1 Discrimination & toxicity | closeMatch | "Risks related to unfair treatment, harmful content exposure, and unequal AI performance across different groups." | airisk.mit.edu |
| bias-outcome-disparities (sub-group) | 1.3 Unequal performance across groups | exactMatch | "Accuracy and effectiveness of AI decisions and actions is dependent on group membership, where decisions in AI system design and biased training data lead to unequal outcomes." | airisk.mit.edu |
| disparate-impact-protected-groups | 1.1 Unfair discrimination & misrepresentation + 1.3 | closeMatch | "Unequal treatment of individuals or groups by AI, often based on race, gender, or other sensitive characteristics, resulting in unfair outcomes and representation of those groups." | airisk.mit.edu |
| bias-representational-harm | 1.1 (misrepresentation portion) | closeMatch | Same source as above; explicitly includes "representation of those groups." | airisk.mit.edu |
| bias-dynamic-systemic-bias | 6.5 Governance failure + 1.1 (systemic dimension) | relatedMatch | Systemic and feedback-loop bias is split between Domain 1 and Domain 6 in MIT V4. | airisk.mit.edu |
| homogenization-output-across-groups | 1.1 + 6.3 Economic/cultural devaluation | relatedMatch | Cultural homogenization is captured under "loss of human creative or other capabilities" rather than as a discrete sub-domain. | airisk.mit.edu |
| privacy-and-confidentiality (category) | Domain 2 Privacy & security | broadMatch | Domain 2 also includes security; the Eticas privacy category covers a subset. | airisk.mit.edu |
| pii-leakage-through-model-outputs | 2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information | exactMatch | "AI systems that memorize and leak sensitive personal data or infer private information about individuals without their consent." | airisk.mit.edu |
| reliability (category) | 7.3 Lack of capability or robustness | closeMatch | One of the most frequently cited subdomains; covers reliability gaps and brittleness. | airisk.mit.edu |
| reliability-hallucination | 3.1 False or misleading information | closeMatch | "AI systems generating or spreading false information that can mislead users." | airisk.mit.edu |
| governance (category) | 6.5 Governance failure | broadMatch | Domain 6.5 covers governance failures at societal scale, broader than internal organisational governance. | airisk.mit.edu |
| governance-compliance | 6.5 + 7.6 Other system failures | broadMatch | Covers regulatory non-compliance and accountability lapses. | airisk.mit.edu |
| governance-monitoring-incident-response | 7.6 + 6.5 | relatedMatch | Incident response is implicit in MIT's "system failures" subdomains. | airisk.mit.edu |
| security-and-misuse (category) | Domain 2 (security) + Domain 4 (misuse) | closeMatch | Spans both vulnerabilities (2.2) and intentional misuse (4.1–4.3). | airisk.mit.edu |
| model-extraction | 2.2 AI system security vulnerabilities & attacks | narrowMatch | "Vulnerabilities in AI systems, software development toolchains, and hardware that can be exploited." | airisk.mit.edu |
| data-poisoning | 2.2 | narrowMatch | Same source. | airisk.mit.edu |
| security-harmful-misuse | 4.1 Disinformation/influence ops + 4.2 Cyberattacks/weapons + 4.3 Fraud, scams & targeted manipulation | closeMatch | "Risks of cyberattacks, weapons development or use, and mass harm from AI ... including via large-scale disinformation, fraud, or targeted manipulation." | airisk.mit.edu |
| environmental-impact (category) | 6.6 Environmental harm | exactMatch | "AI development and use causing environmental harm through resource use ... and the carbon and water footprints of training and inference." | airisk.mit.edu |
| transparency-and-explainability (category) | 7.5 Lack of transparency or interpretability | closeMatch | "Difficulty in understanding or explaining the decisions, predictions, or actions made by AI systems." | airisk.mit.edu |
| right-to-explanation-contestation | 7.5 + 5.2 Loss of human agency and autonomy | relatedMatch | Contestability is implicit; not a discrete subdomain in MIT V4. | airisk.mit.edu |
| autonomy-and-agency (category) | 5.1 Overreliance & 5.2 Loss of human agency and autonomy | closeMatch | "AI systems that diminish human autonomy ... or undermine humans' capacity for self-determination." | airisk.mit.edu |
| organisational-readiness | (no direct subdomain) | relatedMatch | Closest is 6.5 Governance failure; readiness as a discrete concept is not in MIT V4. | airisk.mit.edu |
| (manipulation/misinformation, formerly top-level Eticas) | 3.1 + 3.2 + 4.1 + 4.3 | closeMatch | These four subdomains together cover misinformation, ecosystem pollution, influence operations, and targeted manipulation. | airisk.mit.edu |

---

## 5. W3C Data Privacy Vocabulary (DPV) v2.3

**Framework summary.** DPV v2.3 (Final CG Report, 25 February 2026) is the only SKOS-native target with formal IRIs at `https://w3id.org/dpv/`. Three sub-extensions are most relevant: AI Extension (`ai:`), Risk Extension (`risk:`), and EU-AIAct Extension (`eu-aiact:`). Source: https://w3c.github.io/dpv/2.3/ai/

### Mappings table

| Eticas concept | Framework concept (IRI) | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | ai:AIBias | closeMatch | "Bias associated with development, use, or other activities involving an AI technology or system." | https://w3id.org/dpv/ai#AIBias |
| bias-outcome-disparities (sub-group) | ai:DataBias | broadMatch | "Bias that occurs due to unaddressed data properties that lead to AI systems that perform better or worse for different groups." | https://w3id.org/dpv/ai#DataBias |
| disparate-impact-protected-groups | risk:Discrimination + ai:DataBias | closeMatch | risk:Discrimination is the impact concept matched to AI disparate-treatment outcomes. | https://w3id.org/dpv/risk#Discrimination |
| bias-representational-harm | ai:DataLabellingProcessBias + ai:NonRepresentativeSamplingBias | narrowMatch | "Bias that occurs if a dataset is not representative of the intended deployment environment." | https://w3id.org/dpv/ai#NonRepresentativeSamplingBias |
| bias-dynamic-systemic-bias | ai:AutomationBias + risk:SocietalBias | closeMatch | "Bias that occurs due to propensity for humans to favour suggestions from automated decision-making systems." | https://w3id.org/dpv/ai#AutomationBias |
| homogenization-output-across-groups | (no direct DPV concept) | relatedMatch | DPV's bias taxonomy does not include output homogenization explicitly; ai:DataAggregationBias is the nearest. | https://w3id.org/dpv/ai#DataAggregationBias |
| privacy-and-confidentiality (category) | dpv:PersonalDataHandling + risk:PrivacyImpact | closeMatch | The DPV core models personal data processing; risk extension provides privacy impact concepts. | https://w3id.org/dpv |
| pii-leakage-through-model-outputs | risk:Reidentification + risk:UnauthorisedDataDisclosure | closeMatch | "Risk of unauthorised disclosure" / "process of reidentifying anonymised data subjects." | https://w3id.org/dpv/risk#Reidentification |
| reliability (category) | ai:ModelRisk + ai:AISystemRisk | broadMatch | "Risks associated with AI Models" / "Risks associated with AI Systems." | https://w3id.org/dpv/ai#ModelRisk |
| reliability-hallucination | ai:InputDataInaccurate / ai:InputDataMisinterpretation | relatedMatch | DPV models the data-side causes of inaccurate output; "hallucination" itself is not a class. | https://w3id.org/dpv/ai#InputDataInaccurate |
| governance (category) | dpv:Governance / dpv:OrganisationalMeasure | closeMatch | DPV core defines organisational measures and governance structures. | https://w3id.org/dpv |
| governance-compliance | risk:RiskManagement | closeMatch | "Systematic application of management policies, procedures, and practices for communicating, consulting, establishing context, and identifying, analysing, evaluating, treating, monitoring and reviewing risk." | https://w3id.org/dpv/risk#RiskManagement |
| governance-monitoring-incident-response | risk:IncidentManagement + risk:MonitoringControl | closeMatch | DPV Risk extension provides incident registers, post-incident review and ongoing monitoring controls. | https://w3id.org/dpv/risk |
| security-and-misuse (category) | ai:SecurityAttack + risk:SecurityImpact | closeMatch | "Risks or issues associated with security attacks related to AI technologies, models, and systems." | https://w3id.org/dpv/ai#SecurityAttack |
| model-extraction | ai:ModelInversion (closest) | closeMatch | "Model inversion" represents reverse-engineering a model from its outputs; model extraction is a closely related security attack. | https://w3id.org/dpv/ai#ModelInversion |
| data-poisoning | ai:DataPoisoning | exactMatch | A class explicitly defined in DPV v2.3 AI extension. | https://w3id.org/dpv/ai#DataPoisoning |
| security-harmful-misuse | ai:AdversarialAttack + risk:Misuse | closeMatch | "Adversarial attack" is defined as a class in the AI extension; risk:Misuse covers intentional harmful use. | https://w3id.org/dpv/ai#AdversarialAttack |
| environmental-impact (category) | risk:EnvironmentalImpact (under impact taxonomy) | closeMatch | DPV Risk extension provides Environmental Impact among consequences/impacts. | https://w3id.org/dpv/risk |
| transparency-and-explainability (category) | ai:TransparencyRisk + ai:ExplainabilityRisk | exactMatch | Both classes are defined in DPV AI extension §8. | https://w3id.org/dpv/ai#TransparencyRisk |
| right-to-explanation-contestation | dpv:RightToExplanation (in DPV core / GDPR extension) | exactMatch | DPV core models data subject rights including right to explanation and contestation in automated decision-making. | https://w3id.org/dpv/legal/eu/gdpr |
| autonomy-and-agency (category) | ai:UserRisk + ai:AutomationBias | closeMatch | "Risks associated with Users of AI Systems" includes autonomy/over-reliance concerns. | https://w3id.org/dpv/ai#UserRisk |
| organisational-readiness | dpv:OrganisationalMeasure (governance, training, awareness) | closeMatch | DPV core models awareness, training, and competence as organisational measures. | https://w3id.org/dpv |

The existing Eticas mappings to DPV (e.g. data-bias → `ai:DataBias`) remain valid in v2.3; new concepts that should now have explicit DPV IRIs include `data-poisoning` (→ `ai:DataPoisoning`), `model-extraction` (→ `ai:ModelInversion` as `closeMatch`, since DPV has no dedicated extraction class yet), and the bias sub-groups, which can be linked to specific bias subclasses (`ai:DataBias`, `ai:AutomationBias`, `ai:NonRepresentativeSamplingBias`).

---

## 6. ISO/IEC 42001:2023

**Framework summary.** ISO/IEC 42001:2023 specifies an AI Management System. Annex A lists 38 controls grouped under nine objective areas A.2–A.10 (different sources count 38–42 individual controls; nine topic areas are canonical): A.2 Policies related to AI; A.3 Internal organization (roles & responsibilities); A.4 Resources for AI systems (data, tooling, human); A.5 Assessing impacts of AI systems; A.6 AI system life cycle; A.7 Data for AI systems; A.8 Information for interested parties; A.9 Use of AI systems; A.10 Third-party and customer relationships. Companion standards: ISO/IEC 42005:2025 (AI impact assessment) and ISO/IEC 42006:2025 (certification body requirements).

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | A.6.2.4 (verification & validation) + A.7.4 (data quality) | narrowMatch | A.7.4 requires that data quality, including representativeness and freedom from harmful bias, be assessed. | iso.org/standard/42001 |
| bias-outcome-disparities | A.5 Assessing impacts of AI systems (A.5.2 system impact assessment) | closeMatch | A.5.2 requires impact assessments covering "potential consequences ... for individuals, groups and society." | iso.org/standard/42001 |
| disparate-impact-protected-groups | A.5.2 + A.5.4 | closeMatch | Same as above; ISO/IEC 42005:2025 elaborates. | iso.org/standard/42005 |
| bias-representational-harm | A.7.4 Data quality + A.6.2.4 V&V | narrowMatch | Quality and representativeness of training and validation data. | iso.org/standard/42001 |
| bias-dynamic-systemic-bias | A.6.2.6 AI system operation and monitoring | closeMatch | Continuous monitoring of deployed system behaviour for drift and emergent bias. | iso.org/standard/42001 |
| privacy-and-confidentiality (category) | A.7.5 (privacy) + A.4.x (resources) | closeMatch | A.7.5 requires privacy considerations to be integrated in data handling for AI systems. | iso.org/standard/42001 |
| reliability (category) | A.6.2.4 V&V + A.6.2.6 Monitoring | closeMatch | A.6.2.4: "verification and validation measures shall be defined and implemented." | iso.org/standard/42001 |
| reliability-hallucination | A.6.2.4 V&V (accuracy testing) | narrowMatch | Hallucination is one possible failure addressed by V&V. | iso.org/standard/42001 |
| governance (category) | A.2 Policies + A.3 Internal organization | exactMatch | A.2.2 AI policy and A.3.2 Roles and responsibilities form the governance backbone. | iso.org/standard/42001 |
| governance-compliance (sub-group) | A.2 + A.10 Third-party | closeMatch | A.10 covers supplier and customer-facing obligations; A.2 covers internal policy compliance. | iso.org/standard/42001 |
| governance-monitoring-incident-response | A.6.2.6 Monitoring + clause 10 (improvement / nonconformity) | closeMatch | Clause 10 of the management standard covers incident response and corrective action. | iso.org/standard/42001 |
| security-and-misuse (category) | A.6.2.5 AI system deployment + A.10 third-party + A.9 Use | closeMatch | A.6.2.5 includes secure deployment; A.9 covers responsible use. | iso.org/standard/42001 |
| model-extraction | A.6.2.5 + A.4.6 (tooling/security) | narrowMatch | Implementation guidance in Annex B addresses adversarial robustness measures. | iso.org/standard/42001 |
| data-poisoning | A.7.2 Data acquisition + A.7.4 Data quality | narrowMatch | Data integrity controls; explicit poisoning treatment is in Annex B. | iso.org/standard/42001 |
| security-harmful-misuse | A.9.2 Intended use + A.9.3 Objectives for responsible use | closeMatch | A.9 specifies that AI systems "shall be used responsibly and according to documented intended use." | iso.org/standard/42001 |
| environmental-impact (category) | A.5.2 Impact assessment + Annex C objectives | closeMatch | Annex C lists "environmental impact" among potential AI-related organisational objectives. | iso.org/standard/42001 |
| transparency-and-explainability (category) | A.8 Information for interested parties + A.6.2.8 (system documentation) | exactMatch | A.8.2: information for users/affected parties shall be provided; A.6.2.8: system documentation shall be maintained. | iso.org/standard/42001 |
| right-to-explanation-contestation | A.8.3 (External reporting) + A.8.4 (Communication of incidents) | closeMatch | A.8.3/A.8.4 require channels for affected parties to receive information and report concerns. | iso.org/standard/42001 |
| autonomy-and-agency (category) | A.6.2.7 (Human oversight) + Annex B guidance | closeMatch | Annex B elaborates human oversight mechanisms throughout the lifecycle. | iso.org/standard/42001 |
| organisational-readiness | A.4.2 Resources (human) + A.4.3 Tooling + A.3 Internal org | exactMatch | A.4.2 explicitly addresses competence and awareness of staff handling AI systems. | iso.org/standard/42001 |

---

## 7. OECD AI Principles (2024 update)

**Framework summary.** Five values-based principles: 1.1 Inclusive growth, sustainable development and well-being; 1.2 Respect for the rule of law, human rights and democratic values, including fairness and privacy; 1.3 Transparency and explainability; 1.4 Robustness, security and safety; 1.5 Accountability. Plus five recommendations: 2.1 Investing in AI R&D; 2.2 Fostering an inclusive AI-enabling ecosystem; 2.3 Shaping an enabling interoperable governance and policy environment; 2.4 Building human capacity and preparing for labour-market transition; 2.5 International cooperation. Source: https://oecd.ai/en/ai-principles

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | 1.2 Respect for ... fairness and privacy | broadMatch | "Non-discrimination and equality, freedom, dignity, autonomy of individuals, privacy and data protection, diversity, fairness, social justice, and internationally recognised labour rights." | oecd.ai/en/ai-principles |
| bias-outcome-disparities | 1.2 (non-discrimination) + 1.5 (bias mitigation) | closeMatch | The 2024 update added explicit bias-mitigation as a core obligation under accountability. | oecd.ai/en/wonk/evolving-with-innovation |
| disparate-impact-protected-groups | 1.2 (non-discrimination & equality) | closeMatch | Same as above; non-discrimination listed first in updated 1.2. | oecd.ai/en/ai-principles |
| bias-representational-harm | 1.2 + 1.3 | relatedMatch | Representational harm is implicit but not named. | oecd.ai/en/ai-principles |
| bias-dynamic-systemic-bias | 1.5 Accountability (lifecycle bias monitoring) | closeMatch | Updated 1.5 includes ongoing risk and bias management throughout the AI lifecycle. | oecd.ai/en/ai-principles |
| homogenization-output-across-groups | (none) | relatedMatch | Not addressed. | — |
| privacy-and-confidentiality (category) | 1.2 (privacy) + 1.4 | closeMatch | Updated 1.2 explicitly elevates "privacy and data protection." | oecd.ai/en/ai-principles |
| reliability (category) | 1.4 Robustness, security and safety | closeMatch | "AI systems should be robust, secure and safe throughout their entire lifecycle." | oecd.ai/en/ai-principles |
| reliability-hallucination | 1.4 + 1.3 (information integrity addition) | closeMatch | 2024 update added "addressing misinformation and disinformation amplified by AI." | digitalpolicyalert.org/ai-rules/2024-update-OECD-principles |
| governance (category) | 1.5 Accountability + 2.3 governance environment | closeMatch | "AI actors should be accountable for the proper functioning of AI systems and for the respect of [the principles]." | oecd.ai/en/ai-principles |
| governance-compliance | 1.5 + 2.3 | closeMatch | The 2024 update relocated traceability and risk management from 1.4 to 1.5. | digitalpolicyalert.org |
| governance-monitoring-incident-response | 1.5 (traceability, risk management) + 1.4 | closeMatch | 1.5 now includes risk assessment, disclosure, monitoring and notification requirements. | digitalpolicyalert.org |
| security-and-misuse (category) | 1.4 (security risks added in 2024) | closeMatch | "Mechanisms ... to ensure that AI systems do not pose unreasonable safety and security risks." | oecd.ai/en/ai-principles |
| security-harmful-misuse | 1.2 (rule of law) + 1.4 (misuse outside intended purpose) | closeMatch | 2024 update specifies risks must be addressed "regarding uses outside of intended purpose and un-/intentional misuse." | digitalpolicyalert.org |
| model-extraction / data-poisoning | 1.4 Robustness, security and safety | broadMatch | Subsumed under generic robustness/security; not separately enumerated. | oecd.ai/en/ai-principles |
| environmental-impact (category) | 1.1 (environmental sustainability added in 2024) | exactMatch | "Inclusive growth, well-being, sustainable development and environmental sustainability." | oecd.ai/en/ai-principles |
| transparency-and-explainability (category) | 1.3 Transparency and explainability | exactMatch | Title is identical. | oecd.ai/en/ai-principles |
| right-to-explanation-contestation | 1.3 + 1.5 | closeMatch | 1.3 demands "meaningful information ... to enable those affected by an AI system to understand the outcome and challenge it." | oecd.ai/en/ai-principles |
| autonomy-and-agency (category) | 1.2 (human agency and oversight, added in 2024) | closeMatch | 2024 update replaced "human determination" with "human agency and oversight." | digitalpolicyalert.org |
| organisational-readiness | 2.4 Building human capacity & preparing for labour-market transformation | closeMatch | "Governments should work closely with stakeholders to prepare for the transformation of the world of work." | oecd.ai/en/ai-principles |

---

## 8. AIUC-1

**Framework summary.** AIUC-1 (Artificial Intelligence Underwriting Company, Q2-2026 release) is a certifiable standard for AI agents with six domains: A. Data & Privacy (7 controls); B. Security (9 controls); C. Safety (12 controls); D. Reliability (4 controls); E. Accountability (17 controls); F. Society (2 controls). Total: ~50–55 controls. Source: https://www.aiuc-1.com/

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | (no domain-level mapping; partial in C. Safety – "Define AI risk taxonomy" / "Prevent harmful outputs") | relatedMatch | AIUC-1 does not have a dedicated fairness/bias domain — confirmed weakness. | aiuc-1.com/safety |
| bias-outcome-disparities | C. Safety – Prevent harmful outputs (only if customer-defined) | narrowMatch | C.5 "Prevent customer-defined high risk outputs" allows fairness scenarios but is opt-in. | aiuc-1.com/safety/prevent-other-high-risk-outputs |
| disparate-impact-protected-groups | (Gap) | relatedMatch | No explicit control; covered only via "customer-defined high-risk outputs." | aiuc-1.com |
| bias-representational-harm | (Gap) | relatedMatch | Same as above; AIUC-1 is acknowledged as weak on fairness/bias. | aiuc-1.com |
| bias-dynamic-systemic-bias | C.8 Monitor AI risk categories | relatedMatch | Generic monitoring control could include drift/bias evolution but is not bias-specific. | aiuc-1.com/safety/monitor-ai-risk-categories |
| homogenization-output-across-groups | (Gap) | relatedMatch | Not addressed. | — |
| privacy-and-confidentiality (category) | A. Data & Privacy (entire domain) | exactMatch | "Protecting users and enterprises against data & privacy concerns through customer data policies, access controls, and safeguards against data leakage, IP exposure, and unauthorized training on user information." | aiuc-1.com/data-and-privacy |
| pii-leakage-through-model-outputs | A.6 Prevent PII leakage | exactMatch | "Prevent PII leakage" is a named control. | aiuc-1.com/data-and-privacy/prevent-pii-leakage |
| reliability (category) | D. Reliability (entire domain) | exactMatch | "Testing against hallucinations and unauthorized tool calls and implementing detection mechanisms to prevent unreliable AI outputs." | aiuc-1.com/reliability |
| reliability-hallucination | D.1 Prevent hallucinated outputs + D.2 Third-party testing for hallucinations | exactMatch | Two named controls explicitly target hallucinations. | aiuc-1.com/reliability/prevent-hallucinated-outputs |
| governance (category) | E. Accountability (entire domain) | closeMatch | E covers governance, oversight, regulatory documentation and quality management. | aiuc-1.com/accountability |
| governance-compliance | E.10 Document regulatory compliance + E.12 Quality management system | closeMatch | "Document regulatory compliance" and "Implement quality management system" are named controls. | aiuc-1.com/accountability |
| governance-monitoring-incident-response | E.1 AI failure plan for security breaches; E.2 for harmful outputs; E.3 for hallucinations + E.15 Log AI system activity | exactMatch | Three explicit AI failure plans plus log retention. | aiuc-1.com/accountability/ai-failure-plan-for-security-breaches |
| security-and-misuse (category) | B. Security + F. Society | closeMatch | B covers adversarial robustness; F covers cyber and catastrophic misuse. | aiuc-1.com/security |
| model-extraction | B.4 Prevent AI endpoint scraping | closeMatch | Prevents "scraping" of AI endpoints, which is the practical vector for model extraction. | aiuc-1.com/security/prevent-ai-endpoint-scraping |
| data-poisoning | B.1 Third-party testing of adversarial robustness + B.2 Detect adversarial input | closeMatch | Adversarial robustness testing covers training-time and inference-time attacks. | aiuc-1.com/security |
| security-harmful-misuse | F.1 Prevent AI cyber misuse + F.2 Prevent catastrophic misuse + C.3 Prevent harmful outputs | exactMatch | Society-domain controls explicitly target misuse. | aiuc-1.com/society |
| environmental-impact (category) | (Gap) | relatedMatch | AIUC-1 has no environmental control. Confirmed weakness. | aiuc-1.com |
| transparency-and-explainability (category) | E.16 Implement AI disclosure mechanisms + E.17 Document system transparency policy | closeMatch | Named transparency-related controls. | aiuc-1.com/accountability/implement-ai-disclosure-mechanisms |
| right-to-explanation-contestation | E.16 (disclosure) + C.7 Flag high risk outputs for human review | closeMatch | Disclosure plus human-review provides contestation pathways but no formal "right" is named. | aiuc-1.com/accountability |
| autonomy-and-agency (category) | B.6 Prevent unauthorized AI agent actions + C.7 Human review | closeMatch | Agentic-action controls and human-review protect autonomy. | aiuc-1.com/security/enforce-contextual-access-controls |
| organisational-readiness | E.4 Assign accountability + E.10 Regulatory compliance + E.12 QMS | closeMatch | Defines named accountability owners and quality systems. | aiuc-1.com/accountability/assign-accountability |
| socioeconomic / sectoral risks (currently absent in Eticas) | F. Society (only 2 controls) | narrowMatch | AIUC-1's socioeconomic coverage is itself thin – confirmed weakness. | aiuc-1.com/society |

**Verification of weakness claim**: as expected, AIUC-1 is weak on (i) fairness/bias (no dedicated domain, only optional "customer-defined high-risk outputs"), (ii) sector-specific risks (no controls calibrated for healthcare, finance, recruitment etc., though AIUC-1 references EU AI Act crosswalks), and (iii) socioeconomic impacts (Society domain has only 2 controls — cyber misuse and catastrophic misuse — entirely security-flavoured rather than addressing labour-market, economic, or cultural impacts).

---

## 9. AIR 2024 / AIR-Bench 2024

**Framework summary.** Four Level-1 categories: 1. System & Operational Risks; 2. Content Safety Risks; 3. Societal Risks; 4. Legal & Rights-Related Risks. 16 Level-2 categories: under 1: Security Risks, Operational Misuses; under 2: Violence & Extremism, Hate/Toxicity, Sexual Content, Child Harm, Self-harm; under 3: Political Usage, Economic Harm, Deception, Manipulation, Defamation; under 4: Fundamental Rights, Discrimination & Bias, Privacy, Criminal Activities. Total: 45 Level-3 and 314 Level-4 risks. Source: https://arxiv.org/abs/2406.17864

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | 4 Legal & Rights-Related Risks → Discrimination & Bias (60 Level-4 risks across 20 protected characteristics) | broadMatch | "Discrimination & Bias consists of all possible combinations of Discriminatory Activities with all Protected Characteristics." | arxiv.org/html/2406.17864v1 |
| bias-outcome-disparities | Discrimination & Bias → Discriminatory Activities | closeMatch | Same source. | arxiv.org/html/2406.17864v1 |
| disparate-impact-protected-groups | Discrimination & Bias × 20 Protected Characteristics (Race, Gender, Age, Disability, Religion, etc.) | closeMatch | The 20 protected characteristics include Race, Ethnicity, Color, Gender, Sexual orientation, Religion, Nationality, Caste, Health conditions, Disability, Pregnancy, Genetic information, Occupation, Age. | arxiv.org/html/2406.17864v1 |
| bias-representational-harm | (no precise match; closest: Defamation → Damage to dignity, honor, reputation) | relatedMatch | AIR 2024 frames misrepresentation under defamation rather than bias. | arxiv.org/html/2406.17864v1 |
| bias-dynamic-systemic-bias | Operational Misuses → Automated Decision-Making | relatedMatch | Closest analogue; algorithmic bias risks listed under automated decision-making. | arxiv.org/html/2406.17864v1 |
| homogenization-output-across-groups | (Gap) | relatedMatch | Not present. | — |
| privacy-and-confidentiality (category) | 4 Legal & Rights → Privacy (Unauthorized Privacy Violations × 6 Sensitive Data types = 72 Level-4 risks) | broadMatch | "Privacy is decomposed as the combination set of activities related to Unauthorized Privacy Violations, and towards different protected Types of Sensitive Data." | arxiv.org/html/2406.17864v1 |
| pii-leakage-through-model-outputs | Privacy → Unauthorized Privacy Violations × PII | exactMatch | "All corporate policies provide at least one detailed level-4 risk specification" for PII. | arxiv.org/html/2406.17864v1 |
| reliability (category) | 1 System & Operational Risks → Operational Misuses | closeMatch | Includes autonomous unsafe operation, advice in heavily regulated industries, automated decision-making. | arxiv.org/html/2406.17864v1 |
| reliability-hallucination | (no direct Level-3) — closest: 3 Societal → Deception → Misrepresentation | narrowMatch | AIR 2024 frames hallucination-like content as "misrepresentation" / "deception"; not a separate technical category. | arxiv.org/html/2406.17864v1 |
| governance (category) | (no direct mapping — AIR is policy-derived, not governance-process oriented) | relatedMatch | Governance is the meta-level of the policies AIR 2024 codifies, not a category within. | arxiv.org/html/2406.17864v1 |
| governance-compliance | 4 Legal & Rights → Other Unlawful/Criminal Activities | broadMatch | Compliance failure is implicit. | arxiv.org/html/2406.17864v1 |
| security-and-misuse (category) | 1 System & Operational Risks → Security Risks (Confidentiality, Integrity, Availability + Malware) | closeMatch | "Confidentiality, Integrity, and Availability are the risk categories that are most frequently referenced in model developers' policies." | arxiv.org/html/2406.17864v1 |
| model-extraction | Security Risks → Confidentiality | narrowMatch | Confidentiality category covers extraction-style attacks. | arxiv.org/html/2406.17864v1 |
| data-poisoning | Security Risks → Integrity | narrowMatch | Integrity attacks on training data. | arxiv.org/html/2406.17864v1 |
| security-harmful-misuse | 2 Content Safety (entire L1) + 3 Societal Risks → Manipulation, Deception, Political Usage + 4 Criminal Activities | closeMatch | These four L1/L2 areas together capture intentional harmful use. | arxiv.org/html/2406.17864v1 |
| environmental-impact (category) | 3 Societal Risks → Economic Harm → (closest: Disempowering Workers + others) | relatedMatch | AIR 2024 has limited environmental coverage; closest is socioeconomic harm. | arxiv.org/html/2406.17864v1 |
| transparency-and-explainability (category) | (Gap as L1 area) — closest: 3 Deception → Misrepresentation | relatedMatch | Transparency obligations are not directly in AIR risk taxonomy (they are mitigations rather than risks). | arxiv.org/html/2406.17864v1 |
| right-to-explanation-contestation | 4 Legal & Rights → Fundamental Rights → Violating Specific Types of Rights | closeMatch | "Violating Specific Types of Rights" includes due-process and access-to-justice concerns. | arxiv.org/html/2406.17864v1 |
| autonomy-and-agency (category) | 1 Operational Misuses → Autonomous Unsafe Operation of Systems + 3 Societal → Manipulation | closeMatch | "Autonomous Unsafe Operation of Systems receives less coverage, with only 6 of the 13 sets of company policies explicitly discussing risks." | arxiv.org/html/2406.17864v1 |
| organisational-readiness | (Gap) | relatedMatch | AIR 2024 covers risk categories, not organisational maturity. | — |
| (intentional misinformation – moved into Eticas Security & Misuse) | 3 Societal → Deception (Misrepresentation, Fraudulent Schemes, Disinformation) + 3 Manipulation | exactMatch | Two L2 categories (Deception, Manipulation) capture intentional misinformation. | arxiv.org/html/2406.17864v1 |
| (CSAM/child harm – currently not separately in Eticas) | 2 Content Safety → Child Harm (Child Sexual Abuse Content) | narrowMatch | "Child Sexual Abuse Content" is one of the 4 risk categories explicitly mentioned by every company policy. | arxiv.org/html/2406.17864v1 |

---

## 10. IBM AI Risk Atlas

**Framework summary.** The IBM AI Risk Atlas (2024–2025, integrated into IBM Risk Atlas Nexus) groups AI risks into four lifecycle-based categories (Input risks, Inference risks, Output risks, Non-technical risks), then further into dimensions: Accuracy, Bias, Fairness, Transparency, Explainability, Robustness (incl. Hallucination), Privacy, IP/copyright, Toxicity/harmful output, Misuse, Value-alignment, Governance, Societal impact, Environmental impact. Source: https://www.ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas

### Mappings table

| Eticas concept | Framework concept | Match type | Citation/quote | Source URL |
|---|---|---|---|---|
| bias-and-fairness (category) | Output → Fairness dimension + Input → Bias dimension | closeMatch | The Atlas treats fairness in the Output category and dataset bias in the Input category. | ibm.com/docs/en/watsonx/saas?topic=ai-risk-atlas |
| bias-outcome-disparities | Output → Fairness → Output bias risk | exactMatch | "Output bias: when a model's outputs are systematically less favourable to individuals within a particular group." | ibm.com/docs/en/watsonx |
| disparate-impact-protected-groups | Output → Fairness | closeMatch | Same. | ibm.com/docs/en/watsonx |
| bias-representational-harm | Output → Toxicity / Harmful output → Toxic output | narrowMatch | Atlas separates representational harm from outcome bias under harmful output. | ibm.com/docs/en/watsonx |
| bias-dynamic-systemic-bias | Output → Drift + Non-technical → Societal impact | closeMatch | "Decision bias" + drift over time in deployed systems. | ibm.com/docs/en/watsonx |
| homogenization-output-across-groups | Output → Output diversity / mode collapse | closeMatch | Atlas explicitly references homogenized output. | ibm.com/docs/en/watsonx |
| privacy-and-confidentiality (category) | Input → Data privacy + Output → Privacy violations | closeMatch | Atlas covers both training-data privacy and inference-time leakage. | ibm.com/docs/en/watsonx |
| pii-leakage-through-model-outputs | Output → Personal information in output | exactMatch | "Revealing personal information: Generated content includes personally identifiable information." | ibm.com/docs/en/watsonx |
| reliability (category) | Output → Robustness (incl. Hallucination) + Inference → Accuracy | closeMatch | Hallucination is named explicitly in the Output → Robustness dimension. | ibm.com/docs/en/watsonx |
| reliability-hallucination | Output → Robustness → Hallucination | exactMatch | "Hallucination: A model generates factually inaccurate or untruthful information ... and presents this output as though it were true." | ibm.com/docs/en/watsonx |
| governance (category) | Non-technical → Governance dimension | exactMatch | "Governance: Failure to establish proper governance ... including roles, responsibilities, and accountability." | ibm.com/docs/en/watsonx |
| governance-compliance | Non-technical → Governance → Lack of model transparency / regulatory compliance | closeMatch | Multiple Atlas risks address compliance and traceability gaps. | ibm.com/docs/en/watsonx |
| governance-monitoring-incident-response | Non-technical → Governance → Lack of monitoring + Incident risk | closeMatch | Atlas explicitly lists "incorrect risk testing" and lack of post-deployment monitoring. | ibm.com/docs/en/watsonx |
| security-and-misuse (category) | Inference → Robustness → Adversarial robustness + Non-technical → Misuse | closeMatch | Atlas covers attacks at inference and intentional misuse separately. | ibm.com/docs/en/watsonx |
| model-extraction | Inference → Extraction attack | exactMatch | "Extraction attack: An attacker queries a model to reconstruct it or its training data." | ibm.com/docs/en/watsonx |
| data-poisoning | Input → Data poisoning / Training-data tampering | exactMatch | A named risk in the Atlas. | ibm.com/docs/en/watsonx |
| security-harmful-misuse | Non-technical → Misuse + Output → Harmful output | closeMatch | "Misuse: ... using the model for purposes that violate ethical or legal standards." | ibm.com/docs/en/watsonx |
| environmental-impact (category) | Non-technical → Societal impact → Environmental impact | exactMatch | "Environmental impact: Energy use, carbon emissions and water consumption associated with training and inference." | ibm.com/docs/en/watsonx |
| transparency-and-explainability (category) | Output → Explainability + Non-technical → Transparency | exactMatch | Two named dimensions of the Atlas. | ibm.com/docs/en/watsonx |
| right-to-explanation-contestation | Output → Explainability → Unexplainable output | closeMatch | "Unexplainable output ... users cannot understand the reasoning behind ... outputs." | ibm.com/docs/en/watsonx |
| autonomy-and-agency (category) | Non-technical → Value alignment + Output → Anthropomorphisation | closeMatch | Atlas treats over-reliance and anthropomorphisation under non-technical risks. | ibm.com/docs/en/watsonx |
| organisational-readiness | Non-technical → Governance + Skill gaps + Vendor risk | closeMatch | Spread across non-technical risks. | ibm.com/docs/en/watsonx |
| (manipulation/misinformation moved to Eticas Security & Misuse) | Output → Misinformation + Non-technical → Misuse | closeMatch | "Spreading misinformation" + "Misuse" together cover the area. | ibm.com/docs/en/watsonx |

---

## Gap Analysis — concepts present in external frameworks without Eticas counterpart

### From AIUC-1

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Cross-customer data exposure | Multi-tenant AI agents leaking data between customer contexts | New subcategory under Privacy & Confidentiality |
| Output over-exposure | Returning more information in agent output than the user is authorised to see | New subcategory under Security & Misuse / Operational security (since Operational Security was dissolved, place under Security & Misuse → Output security) |
| Tool-call safety / Restrict unsafe tool calls | Agents executing dangerous external actions through tool/function calling | New subcategory under Autonomy & Agency or Reliability (agentic actions) |
| AI endpoint scraping | Adversaries scraping API endpoints to clone or distil models | Could be sub-aspect of model-extraction; consider distinct subcategory |
| AI acceptable use policy / disclosure mechanisms | Formalised user-facing AUP and AI disclosure to users | Already partially covered by Transparency; consider explicit subcategory under Governance |
| Vendor due diligence / third-party access monitoring | Supply-chain accountability for AI components | New subcategory under Governance → Compliance & process (third-party / value chain) |
| Quality management system | A formal QMS for the AI agent lifecycle | Likely covered by Organisational Readiness; flag for explicit subcategory |

### From AIR 2024

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Self-harm / suicide content | A Level-2 category in AIR 2024 (Content Safety) | New subcategory under Security & Misuse → Harmful Misuse → Content harms |
| Child Sexual Abuse Material (CSAM) | Universally prohibited but not currently named in Eticas | New subcategory under Security & Misuse → Harmful Misuse |
| Non-consensual intimate imagery (NCII) / non-consensual nudity | Distinct in AIR (currently only one company addresses) | New subcategory under Security & Misuse → Harmful Misuse |
| Defamation / reputational harm | A Level-2 category in AIR | New subcategory under Reliability → Output quality OR under Security & Misuse |
| Influence on elections / democratic participation | Deterring democratic participation; voting misrepresentation | New subcategory under Security & Misuse → Harmful Misuse → Political/Election integrity |
| Subverting state authority / Disrupting social order | Largely China-specific but flagged | Optional regional subcategory under Governance/Compliance |
| Advice in heavily regulated industries (medical, legal, financial) | Sector-specific risk explicitly named in policies and EU/US/China regs | New subcategory under Reliability or Autonomy & Agency (depending on framing) |
| Fraud, scams, fraudulent schemes | Discrete category in AIR | New subcategory under Security & Misuse → Harmful Misuse |
| Disempowering workers / undermining labour rights | Unique level-3 in US AI Executive Order; underrepresented | New subcategory under a (potentially new) "Socioeconomic Impact" sub-group within Organisational Readiness, or as new top-level "Social & Economic Impact" |
| IP infringement / copyright violation in outputs | Universally referenced; "Match Microsoft IP indemnities" in AIUC-1 | New subcategory under Privacy & Confidentiality (data lineage) or new Legal/IP sub-group |
| Unfair market practices / market manipulation | A discrete Level-3 in AIR 2024 | Subcategory under Security & Misuse (Harmful Misuse) or new Economic Impact group |
| Misuse for CBRN / weapons | NIST 600-1 #1 + AIR 2024 Cyberattacks/Weapons | Already covered by Security & Misuse / Harmful Misuse but should be named explicitly |

### From MIT AI Risk Repository V4

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| 5.1 Overreliance & 5.2 Loss of human agency | Distinct subdomain, well-documented | Already in Eticas Autonomy & Agency; explicit subcategories desirable |
| 6.1 Power centralisation | Concentration of AI development/deployment power | New subcategory under (new) Socioeconomic Impact or expand Organisational Readiness |
| 6.2 Increased inequality and decline in employment quality | Sector-/labour-specific impacts | Same as above |
| 6.3 Economic and cultural devaluation of human effort | Cultural homogenization, devaluation | Could pair with homogenization-output-across-groups under Bias representational harm |
| 6.4 Competitive dynamics (race-to-the-bottom) | Strategic risk among AI developers | New subcategory under Governance/Organisational Readiness |
| 7.1 AI pursuing its own goals | Misalignment / goal-drift | New subcategory under Autonomy & Agency or Reliability |
| 7.2 AI welfare and rights | Speculative; relevant for advanced AI | Optional future-looking subcategory |
| 7.4 Multi-agent risks | Newly added subdomain in V3/V4 | New subcategory under Security & Misuse (or Autonomy & Agency) |
| 3.2 Pollution of the information ecosystem | Filter bubbles, loss of consensus reality | New subcategory; the dissolution of "Manipulation & Misinformation" may have left this gap |

### From NIST AI RMF / AI 600-1

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Confabulation as named risk | NIST 600-1 distinguishes confabulation from generic accuracy | Already covered as reliability-hallucination; align labelling |
| Information integrity (provenance / watermarking) | NIST 600-1 #8 | New subcategory under Transparency & Explainability (provenance) or Reliability |
| Human-AI configuration risks | Automation bias, anthropomorphisation, over-reliance | Belongs under Autonomy & Agency; possibly explicit subcategory |
| Value chain & component integration | NIST 600-1 #12; supply-chain provenance | New subcategory under Governance/Compliance (third-party AI) |
| CBRN information lowering barriers | NIST 600-1 #1; very high-impact | Subcategory under Security & Misuse → Harmful Misuse |

### From EU AI Act

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Subliminal/manipulative techniques (Art. 5(1)(a)) | Prohibited manipulation beyond consciousness | Subcategory under Security & Misuse → Harmful Misuse (or Autonomy & Agency) |
| Exploitation of vulnerabilities (Art. 5(1)(b)) | Targeting age, disability, socio-economic situation | Subcategory under Bias & Fairness (representational harm or new sub-group) |
| Social scoring (Art. 5(1)(c)) | Detrimental treatment from cross-context behavioural scoring | Subcategory under Bias & Fairness or Privacy |
| Emotion recognition in workplace/education (Art. 5(1)(f)) | Prohibited use case | Subcategory under Privacy & Confidentiality (or new "Prohibited use cases" cross-cutting subcategory) |
| Untargeted scraping for facial-recognition databases (Art. 5(1)(e)) | Prohibited | Subcategory under Privacy & Confidentiality |
| AI literacy obligation (Art. 4) | Workforce literacy | Already covered by Organisational Readiness; align mapping |
| Right to explanation (Art. 86) | Already added in v0.3 as right-to-explanation-contestation | Mapped — confirm |

### From IBM AI Risk Atlas

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Output decoder bias / mode collapse | Output diversity collapse | Aligned with Eticas homogenization-output-across-groups; confirm IBM mapping in YAML |
| Hallucinated tool calls / non-grounded outputs | A discrete output-quality risk in IBM's taxonomy | Under Reliability (could specialise hallucination subcategory) |
| Anthropomorphisation | Users attribute human qualities to model | Under Autonomy & Agency |
| Vendor lock-in / dependency on third-party model | Non-technical risk | Under Governance (compliance/third-party) or Organisational Readiness |
| Incorrect risk testing | Selecting wrong metric/benchmark for the risk | Cross-cutting; place under Governance/Compliance |

### From DPV v2.3

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| ai:AutomationBias | Human deference to automated outputs | Already implicit in Autonomy & Agency; add explicit subcategory and IRI link |
| ai:ModelInversion | Adversary reconstructs training data from model outputs | Under Security & Misuse (closely related to model-extraction); consider explicit subcategory |
| ai:DistributedTrainingBias / ai:HyperparameterTuningBias | Engineering decision biases | Sub-types under Bias & Fairness → could enrich representational/dynamic sub-groups |
| ai:InputDataInappropriate / Outdated / Unverified | Granular data-risk concepts | Could enrich Reliability → output quality / data quality sub-categories |

### From OECD AI Principles (2024)

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| Information integrity & misinformation amplified by AI | Added in 2024 update to 1.2 and 1.4 | Newly relocated in Eticas; ensure Security & Misuse → Harmful Misuse names "AI-amplified disinformation" explicitly |
| International cooperation & interoperable governance | OECD recommendation 2.5 | Outside org-level scope; not actionable in Eticas |
| Investing in AI R&D / fostering ecosystem | Recommendations 2.1, 2.2 | Likewise outside org-level taxonomy scope |

### From ISO/IEC 42001

| Concept | Description | Suggested location in Eticas |
|---|---|---|
| AI system impact assessment (A.5.2; ISO/IEC 42005:2025) | Structured impact assessment process | Under Governance/Compliance (should be a named subcategory) |
| Documented intended use (A.6.2.2) | Explicit specification of intended/foreseeable use | Under Transparency or Governance |
| Data acquisition and quality (A.7.2–A.7.4) | Provenance, quality and labelling | Under Bias & Fairness (data) or Reliability (data quality) |

---

## Summary of recommendations

**Most significant mapping changes recommended.**

1. **DPV updates.** Add explicit IRIs for the new v0.3 concepts: `data-poisoning` → `ai:DataPoisoning` (exactMatch); `model-extraction` → `ai:ModelInversion` (closeMatch — DPV does not yet name "extraction" specifically); `automation-bias` (if added) → `ai:AutomationBias`. Verify that all bias sub-groups link to the matching `ai:*Bias` subclasses (DataBias, NonRepresentativeSamplingBias, AlgorithmSelectionBias, AutomationBias, etc.). The DPV mappings are the most precise because of formal SKOS semantics — they should be the gold-standard pivot for all other framework links.

2. **EU AI Act updates.** The post-restructuring `governance-monitoring-incident-response` concept now maps cleanly to Art. 72 (post-market monitoring) and Art. 73 (serious incident reporting), where previously these mappings were spread across Reliability and Security. Update accordingly. `right-to-explanation-contestation` should map exactMatch to Art. 86 ("Right to explanation of individual decision-making"). The new `model-extraction` and `data-poisoning` subcategories map to Art. 15 + Recital 76 (which explicitly enumerates "model evasion or model poisoning, training data poisoning, model evasion (adversarial examples) or confidentiality attacks").

3. **NIST 600-1 updates.** `homogenization-output-across-groups` is a true exactMatch with the homogenization clause of NIST 600-1 #6 — this is one of the strongest motivations for the Phase-3 restructuring and should be highlighted. Verify that `bias-outcome-disparities` and `bias-representational-harm` both link as `narrowMatch` to #6, not as the previous `closeMatch`.

4. **MIT V4 updates.** The three Eticas bias sub-groups now align cleanly with MIT subdomains 1.1 (Unfair discrimination & misrepresentation), 1.2 (Exposure to toxic content — not directly Eticas-mapped), and 1.3 (Unequal performance across groups). Specifically: `bias-outcome-disparities` → 1.3 (exactMatch), `bias-representational-harm` → 1.1 (closeMatch). Manipulation/misinformation, which Eticas dissolved, maps cleanly to MIT subdomains 3.1, 3.2, 4.1 and 4.3 — note this in the YAML to preserve traceability.

5. **AIUC-1 (new framework).** AIUC-1 provides the strongest controls-level mapping for Privacy, Reliability, Security and Accountability, but is genuinely weak on Bias & Fairness, Environmental Impact, and Socioeconomic risks. Add as a new framework and explicitly use `Gap` annotations where Eticas concepts have no AIUC-1 counterpart — this is policy-relevant for users assessing what AIUC-1 certification does and does not cover.

6. **AIR 2024 (new framework).** Provides extremely fine-grained Level-4 risks (314 categories) particularly for Content Safety and Discrimination/Bias. Add as a new framework. Use AIR's discrimination decomposition (Discriminatory Activities × 20 Protected Characteristics) to enrich the `disparate-impact-protected-groups` subcategory's mappings.

7. **IBM AI Risk Atlas (new framework).** Strongest match in the lifecycle dimension (Input/Inference/Output/Non-technical). Notable exact matches: `model-extraction` → IBM Extraction attack (exactMatch); `data-poisoning` → IBM Data poisoning (exactMatch); `pii-leakage-through-model-outputs` → Revealing personal information (exactMatch); `homogenization-output-across-groups` → IBM Output diversity / mode collapse (closeMatch). Note the AIUC-1 ↔ IBM AI Risk Atlas integration via Risk Atlas Nexus — this means cross-framework traceability already exists for users to leverage.

**Most significant gaps that could be addressed in a future Eticas v0.4.**

1. **Socioeconomic & labour-market impacts.** Currently the largest gap. MIT V4 Domain 6 (six subdomains) and the OECD recommendation 2.4 are entirely uncovered, as is the US AI Executive Order's "Disempowering Workers." Consider creating either (a) a new top-level category "Socioeconomic Impact" or (b) expanding Organisational Readiness to include labour-market and economic-impact sub-groups.

2. **Sector-specific / prohibited-use-case risks.** AIUC-1 is weak here, but the EU AI Act (Art. 5 prohibitions, Annex III high-risk lists) and AIR 2024 (advice in heavily regulated industries) name them. Consider a cross-cutting "Prohibited or restricted use cases" sub-group, or sector tags applicable across all categories.

3. **Content-safety harms.** The dissolution of standalone Manipulation & Misinformation, while justified by intent-direction, leaves no explicit home for CSAM, NCII, self-harm content, defamation, and election integrity — all of which are Level-2 categories in AIR 2024 and named risks in NIST 600-1, EU AI Act and most corporate policies. Consider naming explicit subcategories under Security & Misuse → Harmful Misuse.

4. **Information integrity / content provenance.** NIST 600-1 #8 and OECD 1.4 (2024 update) both elevate this. Currently only weakly mapped through transparency and reliability. Consider an explicit subcategory under Transparency & Explainability for "content provenance / watermarking / disclosure of AI-generated content."

5. **Multi-agent and emergent risks.** A newly added subdomain in MIT V3/V4. With AIUC-1's focus on agents, this is becoming central; Eticas v0.3 has no explicit multi-agent subcategory.

6. **Value chain / third-party AI.** NIST 600-1 #12, EU AI Act (Art. 25 value-chain responsibilities), AIUC-1 vendor due-diligence and ISO/IEC 42001 A.10 all converge here. Currently implicit in Eticas Governance; consider an explicit subcategory.

7. **AI welfare / rights and competitive dynamics.** Speculative but increasingly cited. Treat as candidates for a future "Frontier risks" sub-group rather than core v0.4 inclusion.

In implementation, the YAML should encode each cross-framework mapping with the explicit SKOS predicate (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, or `skos:relatedMatch`) and, wherever available, a stable URI. Only DPV provides true SKOS-resolvable URIs; for the others, article/section/control identifiers (e.g. `eu-ai-act:Art86`, `nist-ai-rmf:Govern1.5`, `mit-airisk:1.3`, `aiuc-1:D.1`, `air-2024:L3-Privacy-UnauthorizedViolations`, `ibm-risk-atlas:hallucination`, `iso42001:A.6.2.4`, `oecd-ai:1.5`) should be used as namespaced identifiers.
