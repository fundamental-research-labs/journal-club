# Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents

**Authors:** Haochen Sun, Shuwen Zhang, Lujie Niu, Lei Ren, Hao Xu, Hao Fu, Fangkun Zhao, Caixia Yuan, Xiaojie Wang
**arXiv:** 2502.20073
**Venue:** Preprint
**Date:** September 2025

## Problem
LLM-based multi-agent systems are often evaluated with end-to-end task success, but many benchmarks do not force collaboration or explain whether agents failed to ask for help, respond to help, or maintain coordination over time. The paper targets this gap for interactive, process-specific tasks where collaboration is required rather than optional.

## Method
Collab-Overcooked extends Overcooked-AI/ProAgent into a two-agent kitchen benchmark with resource isolation and asymmetric task knowledge. Agent Bob and Agent Alice have different action spaces, exchange resources through counters, and coordinate through natural-language communication. The benchmark contains 30 sequential tasks across 6 complexity levels, annotated with Referential Action Trajectories (RATs). It evaluates both end-to-end and process behavior using TES/ITES-derived metrics: Progress Completeness (PC), Initiating Capability (IC), and Responding Capability (RC). Experiments use a shared in-context agent baseline with memory, reflection, error handling, and communication across 13 LLMs, plus human comparison and attention analyses.

## Key Findings
- The benchmark is designed to make collaboration necessary through resource isolation and asymmetric task knowledge, rather than relying only on nominally collaborative goals.
- Model success drops sharply as task complexity increases. Claude Sonnet 4 is the strongest overall model in Table 2, while DeepSeek-R1 is the strongest open-source model but uses substantially more tokens than GPT-4o in the reported setup.
- Process metrics show that many models are better at responding to collaboration requests than initiating them; initiating collaboration is identified as a primary bottleneck.
- Human participants remain much more stable across complexity levels under time constraints, suggesting the tasks are tractable but current LLM-MAS agents lack robust procedural abstraction and adaptation.
- Failure analysis links degradation to later-step collaboration, positional dependence, and attention misalignment: agents over-attend to task execution details or partner instructions while under-attending to collaboration rules and environmental state.

## Tags
`LLM-agents`, `multi-agent`, `collaboration`, `benchmark`, `Overcooked-AI`, `process-evaluation`, `attention-analysis`

## Connections
- Complements **CooperBench** by studying collaborative agents in an embodied/game environment rather than software repositories, while similarly questioning whether multiple agents coordinate reliably.
- Related to **WhyMultiAgentFail** and other failure-taxonomy work: Collab-Overcooked provides a controlled setting for measuring how failures evolve across collaboration steps.
- Builds on Overcooked-AI and ProAgent, but changes the environment so resource isolation and asymmetric knowledge make agent-agent collaboration structurally necessary.
- Useful alongside RocoBench, CuisineWorld, VillagerBench, LLMARENA, and MultiAgentBench as a benchmark emphasizing process-oriented collaboration metrics rather than only final success.
