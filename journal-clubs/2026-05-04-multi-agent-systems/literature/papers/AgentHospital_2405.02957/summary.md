# Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents

**Authors:** Junkai Li, Yunghwei Lai, Weitao Li, Jingyi Ren, Meng Zhang, Xinhui Kang, Siyu Wang, Peng Li, Ya-Qin Zhang, Weizhi Ma, Yang Liu
**arXiv:** 2405.02957
**Venue:** Preprint
**Date:** May 2024; local PDF is arXiv v3 dated January 17, 2025

## Problem
Medical LLMs can encode textbook knowledge, but they do not directly model the long practice phase through which clinicians gain hospital experience. Existing medical-agent work largely studies reasoning or multi-agent consultation, leaving open how doctor agents can improve through repeated patient treatment without manually labeled training data.

## Method
Agent Hospital is a hospital simulacrum populated by LLM-powered patient, nurse, and doctor agents. It simulates a closed treatment loop: disease onset, triage, registration, consultation, medical examination, diagnosis, medicine dispensing, convalescence, and follow-up. The paper's SEAL paradigm builds the simulacrum by coupling LLMs with medical knowledge bases, then evolves agents inside it.

The concrete training method, MedAgent-Zero, generates patient agents from disease knowledge, demographics, medical history, symptoms, and examination reports. Doctor agents make examination, diagnosis, and treatment decisions using a medical case base of successful cases and an experience base of validated reflections from failures; both are retrieved with RAG during later decisions. The evaluated Agent Hospital covers 32 departments, including 21 clinical departments and 339 diseases.

## Key Findings
- In the virtual hospital, doctor agents improve after treating synthetic patients. Across 21 clinical departments, Table 3 reports overall examination accuracy rising from 66.14% to 98.76% and diagnosis accuracy from 76.98% to 95.31% after evolution on 20,000 virtual patients per department, tested on separate synthetic patients.
- The paper reports scaling-like behavior as doctor agents treat more virtual patients: respiratory diagnosis improves over 50,000 cases in Figure 5b, and cardiology/nephrology trends in Figure 9 generally rise over 20,000 cases, though the curves are not perfectly monotonic.
- On MedQA, MedAgent-Zero outperforms the listed Direct, CoT, MedAgents, and Medprompt baselines for each reported base model in Table 4 without using MedQA training labels in the non-hybrid setting; for GPT-4o, it reports 92.22% versus 91.52% for Medprompt and 90.42% for CoT.
- Ablations in Figure 12 suggest that both the medical case base and the experience base contribute to MedAgent-Zero, and adding real-world Q&A pairs in the hybrid variant improves further in most settings.
- The authors explicitly limit the current system: the base model is frozen, AI doctors recommend only high-level treatment plans, and the simulation lacks interdepartment doctor consultation.

## Tags
`medical-agents`, `simulacrum`, `synthetic-data`, `agent-evolution`, `healthcare-ai`, `rag`, `MedQA`, `virtual-patients`

## Connections
- Extends the Smallville/generative-agent idea from social simulation to a task-specific hospital environment with medical workflows and synthetic patients.
- Uses an AlphaGo Zero-style framing: agents improve through an accelerated virtual environment rather than manually labeled target-benchmark data.
- Related to MedAgents and Medprompt as medical-agent/reasoning baselines on MedQA, but emphasizes case memory and failure-derived experience rather than only prompting or consultation.
- Useful alongside work on synthetic data, world models, and agent memory because it ties generated experience to retrieval-time behavior.
- Important cautionary companion for healthcare-agent work: the results are benchmark and simulation results, not evidence of clinical deployment readiness.
