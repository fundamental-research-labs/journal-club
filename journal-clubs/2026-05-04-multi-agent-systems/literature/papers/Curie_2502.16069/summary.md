# Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents

**Authors:** Patrick Tser Jern Kon, Jiachen Liu, Qiuyi Ding, Yiming Qiu, Zhenning Yang, Yibo Huang, Jayanth Srinivasa, Myungjin Lee, Mosharaf Chowdhury, Ang Chen
**arXiv:** 2502.16069
**Venue:** ICML 2025
**Date:** February 2025

## Problem
LLMs can assist with literature review, ideation, coding, and data analysis, but rigorous scientific experimentation requires more than ad hoc prompting. Agents must formulate hypotheses, design controlled experiments, execute and validate setups, track intermediate results, and draw reproducible conclusions without cascading hallucinations or undocumented state.

## Method
Curie is a multi-agent experimentation framework built around an Experimental Rigor Engine. An Architect Agent proposes and refines experimental plans, while Technician Agents implement and execute controlled experiments. The Intra-Agent Rigor Module validates each agent step for reliability, including setup alignment and clean execution checks. The Inter-Agent Rigor Module partitions plans, enforces valid workflow transitions, and schedules work. The Experiment Knowledge Module records plans, states, results, and provenance in a structured "time machine" so agents can read and update experiment state consistently.

## Key Findings
- The paper introduces an Experimentation Benchmark of 46 computer-science research tasks across LLM reasoning, vector indexing, cloud computing, and ML training.
- On the benchmark, Curie reports higher weighted average scores than OpenHands and Microsoft Magentic-One across experiment design, execution setup, implementation alignment, and conclusion correctness.
- Table 2 reports Curie at 36.1% conclusion correctness, compared with 10.5% for OpenHands and 2.3% for Magentic-One; the abstract summarizes this as a 3.4x improvement over the strongest tested baseline on correctly answering experimental questions.
- The largest gains are in execution setup and downstream conclusion quality, which the authors attribute to stepwise validation, methodical task transitions, and structured experiment records.
- Performance drops as task complexity increases, but Figure 8 shows Curie staying above the baselines across the reported complexity dimensions.

## Tags
`AI-agents`, `scientific-experimentation`, `agent-frameworks`, `experimental-rigor`, `multi-agent-systems`, `benchmark`, `LLM-for-science`

## Connections
- Complements **AI Scientist** and other automated-science systems by focusing on the rigor of experimentation rather than end-to-end paper generation.
- Related to **ScienceAgentBench** and **MLAgentBench** as an evaluation effort, but Curie's benchmark stresses full experimental workflows and conclusion validity rather than only task completion.
- Useful alongside multi-agent coordination papers such as **CAID** and **CooperBench** because Curie makes coordination constraints explicit through workflow states, partitioning, and controlled writes.
- Relevant to work on process supervision and provenance: Curie applies stepwise validation and structured state histories to scientific agent workflows.
