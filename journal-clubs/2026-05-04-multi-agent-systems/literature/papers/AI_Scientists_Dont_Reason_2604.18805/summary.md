# AI Scientists Produce Results Without Reasoning Scientifically

**Authors:** Martino Rios-Garcia, Nawaf Alampara, Chandan Gupta, Indrajeet Mandal, Sajid Mannan, Ali Asghar Aghajani, N. M. Anoop Krishnan, Kevin Maik Jablonka
**arXiv:** 2604.18805
**Venue:** Preprint
**Date:** April 2025

## Problem
LLM-based agents are increasingly deployed to conduct scientific research autonomously, but whether their reasoning adheres to the epistemic norms that make science self-correcting is unknown. Existing benchmarks measure only task completion, not reasoning quality.

## Method
The authors build Corral, an evaluation framework spanning 8 scientific domains (spectroscopy, wet-lab qualitative analysis, circuit inference, retrosynthesis, AFM, molecular dynamics, catalyst surface construction, ML pipelines) with graded task scopes from workflow execution to hypothesis-driven inquiry. They evaluate 3 frontier models (GPT-4o, Claude Sonnet 4.5, GPT-OSS-120B) paired with 2 scaffold architectures (ReAct, structured tool-calling) across 25,000+ agent runs. They analyze performance via item response theory (IRT) and variance decomposition, then separately analyze the epistemological structure of reasoning traces by annotating each step as an epistemic operation (hypothesis, test, evidence, judgment, update, commitment) and constructing directed dependency graphs. They also run trace intervention experiments where agents receive partial successful trajectories as context.

## Key Findings
- The base model accounts for 41.4% of explained variance in task success; the scaffold accounts for only 1.5%; tool-description verbosity accounts for 0.1%
- Evidence is ignored in 68% of traces; beliefs are never updated in 71% of traces; refutation-driven belief revision occurs in only 26%
- Untested claims (hypotheses stated without designing experiments to test them) appear in 53% of traces overall, 63% in hypothesis-driven domains
- Convergent multi-test evidence (multiple independent lines of evidence for one hypothesis) is rare at 7%
- Agents do not adapt their reasoning to epistemic demand: the same reasoning topology appears for workflow execution and hypothesis-driven inquiry
- Trace interventions (injecting successful partial trajectories) rescue workflow tasks with 1-2 steps but require near-complete trajectories (n-2 or n-1 steps) to help in hypothesis-driven domains
- Reliability (pass-hat-k, all k trials succeed) drops below 0.05 by k=4-6 in hypothesis-driven domains, even with interventions
- Reasoning patterns persist across scaffold architectures, domains, and intervention conditions -- they are properties of the base model

## Tags
`LLM-agents`, `scientific-reasoning`, `evaluation`, `epistemology`, `benchmark`, `scaffold-vs-model`, `reasoning-failures`, `reliability`

## Connections
- Directly supports **SingleAgentOutperforms**: both find that scaffold engineering contributes far less than the base model to agent performance, reinforcing that architectural choices matter less than model capability
- Complements **WhyMultiAgentFail**: this paper shows single agents fail at disciplined reasoning; multi-agent systems built on the same base models would inherit these epistemic failures
- Relevant to **ScienceOfScaling**: the finding that reasoning ability (41.4% of variance) dominates scaffold (1.5%) informs scaling discussions -- scaling the model matters more than scaling the scaffold
- Connects to **SlopCodeBench**: both examine quality of agent outputs beyond pass/fail metrics, finding that surface-level success hides deeper process failures
- Relevant to **CooperBench** and **DELEGATE-52**: cooperative and delegation benchmarks should consider whether agents can reason scientifically when tasks require hypothesis testing and evidence evaluation
- Contrasts with **MaAS** (multi-agent-as-a-service): orchestration frameworks cannot fix base-model reasoning deficits identified here
