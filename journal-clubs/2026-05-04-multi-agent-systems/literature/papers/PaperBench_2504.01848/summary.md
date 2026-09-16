# PaperBench: Evaluating AI's Ability to Replicate AI Research

**Authors:** Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Chan Jun Shern, Leon Maksin, Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, Tejal Patwardhan
**arXiv:** 2504.01848
**Venue:** Preprint
**Date:** April 2025

## Problem
Most coding and ML-agent benchmarks do not test the full workflow required to replicate a modern AI research paper from scratch: understanding the paper, building the implementation, running experiments, and producing evidence that results were reproduced. PaperBench targets this longer-horizon ML R&D capability, which is relevant both for scientific acceleration and for monitoring autonomous AI capabilities.

## Method
PaperBench gives an agent a research paper and clarifying addendum, then asks it to create a repository with a root `reproduce.sh` that can reproduce the paper's empirical contributions. The benchmark contains 20 ICML 2024 Spotlight and Oral papers selected for suitability across multiple ML topics. Original authors' code and known replications are blacklisted so the task measures from-scratch replication rather than code reuse.

Submissions are run in a fresh Ubuntu 24.04 environment with an A10 GPU before grading. Each paper has an author-reviewed hierarchical rubric whose weighted leaf nodes cover code development, execution evidence, and result matching. Across the benchmark there are 8,316 individually gradable leaf nodes. The authors also build SimpleJudge, an LLM-based grading scaffold, and JudgeEval, a human-labeled auxiliary benchmark for measuring judge accuracy. PaperBench Code-Dev is a lighter variant that grades only code-development rubric nodes without the reproduction run.

## Key Findings
- In the main BasicAgent setup, the best tested agent, Claude 3.5 Sonnet (New), reaches an average PaperBench Replication Score of 21.0%; o1 reaches 13.2%, and the other tested models score below 10%.
- Prompting and scaffolding matter: IterativeAgent raises o1 to 24.4% and o3-mini to 8.5%, but lowers Claude 3.5 Sonnet to 16.1%, showing that model comparisons are scaffold-sensitive.
- On the human baseline subset, ML PhD participants eventually outperform the evaluated AI agent: best-of-3 humans score 41.4% after 48 hours on the reported 3-paper subset, versus 26.6% for o1 on the same subset.
- SimpleJudge with o3-mini achieves 0.83 F1 on JudgeEval, making automated grading plausible for scale, but the paper explicitly treats the judge as imperfect and less reliable than expert human grading.
- PaperBench Code-Dev is cheaper and easier to run, and o1 with IterativeAgent scores 43.4% on it, but the authors describe it as less robust and only weakly correlated with full PaperBench.

## Tags
`AI-research-agents`, `ML-R&D`, `benchmark`, `paper-replication`, `rubric-grading`, `LLM-as-judge`, `long-horizon-agents`, `reproducibility`

## Connections
- A key benchmark for papers on software and research agents, including CAID-style multi-agent systems that use PaperBench as a long-horizon evaluation target.
- Complements CooperBench: CooperBench isolates collaborative coding coordination failures, while PaperBench tests whether agents can complete an end-to-end ML research replication.
- Related to CORE-Bench, MLE-bench, MLAgentBench, DSBench, and RE-Bench, but differs by requiring from-scratch paper replication against author-reviewed rubrics rather than using existing repositories, Kaggle-style tasks, or narrow scoring functions.
- Useful for discussions of LLM-as-judge infrastructure because PaperBench pairs a complex rubric benchmark with JudgeEval for validating automated graders.
