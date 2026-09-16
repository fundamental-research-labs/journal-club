# Why Do Multi-Agent LLM Systems Fail?

**Authors:** Mert Cemri, Melissa Z. Pan, Shuyi Yang, Lakshya A Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Dan Klein, Kannan Ramchandran, Matei Zaharia, Joseph E. Gonzalez, Ion Stoica
**arXiv:** 2503.13657
**Venue:** NeurIPS 2025 (Datasets & Benchmarks Track)
**Date:** March 2025

## Problem
Multi-agent LLM systems (MAS) show minimal performance gains over single-agent baselines on popular benchmarks, with observed failure rates of 41% to 86.7% across state-of-the-art open-source MAS. There is no principled understanding of why these systems fail or a standardized framework for classifying their failures.

## Method
The authors build MAST (Multi-Agent System Failure Taxonomy), the first empirically grounded taxonomy of MAS failures, using Grounded Theory analysis on 150+ execution traces from 5 MAS frameworks annotated by 6 human experts. They validate MAST through inter-annotator agreement studies (Cohen's kappa = 0.88) and develop an LLM-as-a-Judge annotation pipeline (using OpenAI o1 with few-shot examples, achieving kappa = 0.77 with humans). Using this pipeline, they construct MAST-Data, a dataset of 1642 annotated traces from 7 MAS frameworks (ChatDev, MetaGPT, HyperAgent, AppWorld, AG2, Magentic-One, OpenManus) across coding, math, and general agent tasks with 4 model families (GPT-4, Claude 3, Qwen2.5, CodeLlama).

## Key Findings
- MAST identifies 14 failure modes in 3 categories: (1) System Design Issues (e.g., disobey task spec 11.8%, step repetition 15.7%, not recognizing task completion 12.4%), (2) Inter-Agent Misalignment (e.g., wrong assumptions 6.8%, task derailment 7.4%, reasoning-action mismatch 13.2%), (3) Task Verification (e.g., premature termination 6.2%, incomplete verification 8.2%, incorrect verification 9.1%)
- Failure distributions differ by MAS architecture: AppWorld suffers from premature termination, OpenManus from step repetition, HyperAgent from step repetition and incorrect verification
- Systems with explicit verifiers (MetaGPT, ChatDev) show fewer total failures, but verification alone is insufficient -- ChatDev achieves only 33.33% correctness on ProgramDev
- Improving agent role specifications in ChatDev yielded +9.4% success rate with the same model
- Adding high-level task verification to ChatDev yielded +15.6% improvement on ProgramDev
- Many failures stem from system design and agent coordination, not just LLM limitations -- better MAS organization with the same underlying model produces measurable gains
- GPT-4o shows 39% fewer System Design Issues than Claude 3.7 Sonnet in MetaGPT; MetaGPT has 60-68% fewer FC1/FC2 failures than ChatDev but 1.56x more verification failures

## Tags
`multi-agent-failures`, `taxonomy`, `failure-analysis`, `benchmark`, `dataset`, `verification`, `agent-coordination`, `system-design`

## Connections
- Directly complements **SingleAgentOutperforms** -- both papers question MAS value, but this one provides a structured taxonomy explaining *why* MAS underperform rather than just showing single agents win
- Relevant to **AgentScalingDiversity** -- the finding that failure distributions are architecture-dependent connects to questions about how agent diversity and scaling affect outcomes
- The verification failures (FC3) relate to **SlopCodeBench** -- superficial code checks passing while deeper correctness fails mirrors concerns about code quality in agent-generated software
- The inter-agent misalignment category (FC2) connects to **CooperBench** and **DELEGATE-52** -- both study multi-agent cooperation, and this paper's taxonomy provides a vocabulary for classifying cooperation failures
- Relates to **MaAS** -- the finding that system design matters more than model capability informs how multi-agent-as-a-service architectures should be structured
- The "theory of mind" collapse finding (FC2) connects to **AI_Scientists_Dont_Reason** -- failures in agent reasoning and communication parallel concerns about shallow reasoning in AI scientific agents
- Relevant to **ScienceOfScaling** -- the paper argues that scaling model capability alone won't fix MAS failures, suggesting organizational design is an orthogonal axis to model scaling
- **MemMA** addresses memory in multi-agent systems, which directly relates to FC1 failures around context loss (FM-1.4) identified here
