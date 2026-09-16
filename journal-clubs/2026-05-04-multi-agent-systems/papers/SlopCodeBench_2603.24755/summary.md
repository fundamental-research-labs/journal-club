# SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks

**Authors:** Gabriel Orlanski, Devjeet Roy, Alexander Yun, Changho Shin, Alex Gu, Albert Ge, Dyah Adila, Frederic Sala, Aws Albarghouthi
**arXiv:** 2603.24755
**Venue:** NeurIPS 2026 (submitted)
**Date:** March 2025

## Problem
Existing coding-agent benchmarks evaluate single-shot solutions against complete specifications, missing the fact that agent-generated code becomes progressively harder to extend under repeated modification. Pass-rate benchmarks cannot detect structural decay because test suites do not measure code quality over time.

## Method
SlopCodeBench (SCBench) is a language-agnostic benchmark of 20 problems spanning 93 checkpoints, where agents repeatedly extend their own prior code under evolving specifications. Specifications constrain only external behavior (CLI/API), not internal structure, and the test suite is hidden. The agent's workspace carries forward between checkpoints, so early architectural decisions compound. The paper introduces two trajectory-level quality metrics: (1) structural erosion -- the fraction of total complexity mass concentrated in high-cyclomatic-complexity functions (CC > 10), and (2) verbosity -- the fraction of code that is redundant or duplicated, measured via 137 AST-Grep rules plus clone detection. These are calibrated against 48 maintained open-source Python repositories. A prompt-intervention study tests whether "anti-slop" or "plan-first" prompts can suppress degradation.

## Key Findings
- No agent solves any problem end-to-end across 11 models; the highest checkpoint solve rate is 17.2% (Opus 4.6)
- Structural erosion rises in 80% of trajectories; verbosity rises in 89.8%
- Agent code is 2.2x more verbose and 2.2x more eroded than 48 maintained human repositories
- Human code quality stays flat over time; agent code quality deteriorates monotonically with each iteration
- Mean high-CC function count grows from 4.1 at checkpoint 1 to 37.0 at checkpoint 8
- Prompt interventions ("anti-slop", "plan-first") reduce initial verbosity by up to 34.5% and erosion by up to 48.1%, but do not change the rate of degradation -- the slope stays the same, only the intercept shifts
- Quality-aware prompts do not improve pass rates (all p > 0.05) and increase cost by up to 48%
- Isolated solve rates range from 7.5% to 23.7%; core solve rates range from 19.4% to 53.8%

## Tags
`code-quality`, `benchmark`, `coding-agents`, `iterative-development`, `technical-debt`, `LLM-evaluation`, `software-engineering`

## Connections
- Directly relevant to **SingleAgentOutperforms** and **WhyMultiAgentFail**: SCBench shows that even single agents degrade over long horizons, which would compound further in multi-agent pipelines where code is passed between agents
- Related to **CooperBench**: both benchmark long-horizon coding tasks, but SCBench focuses on iterative self-extension and quality metrics rather than cooperative multi-agent development
- Connects to **AI_Scientists_Dont_Reason**: both papers highlight failure modes masked by pass-rate evaluations -- SCBench shows agents can pass tests while producing structurally degraded code, paralleling how AI scientists can produce superficially correct but fundamentally flawed outputs
- Relevant to **ScienceOfScaling**: SCBench's finding that more compute (cost grows over checkpoints) does not improve correctness echoes scaling limitations
- The degradation dynamics measured here would likely worsen under the multi-agent architectures studied in **MaAS**, **DELEGATE-52**, and **AgentScalingDiversity**, where handoffs between agents could amplify structural erosion
