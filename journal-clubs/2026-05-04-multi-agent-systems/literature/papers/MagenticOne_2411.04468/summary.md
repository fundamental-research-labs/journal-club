# Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks

**Authors:** Adam Fourney, Gagan Bansal, Hussein Mozannar, Cheng Tan, Eduardo Salinas, Erkang (Eric) Zhu, Friederike Niedtner, Grace Proebsting, Griffin Bassman, Jack Gerrits, Jacob Alber, Peter Chang, Ricky Loynd, Robert West, Victor Dibia, Ahmed Awadallah, Ece Kamar, Rafah Hosn, Saleema Amershi
**arXiv:** 2411.04468
**Venue:** Preprint
**Date:** November 2024

## Problem
General-purpose AI agents need to plan, use tools, recover from errors, and complete open-ended multi-step tasks across web, file, and coding environments. The paper targets this generalist setting rather than a single domain, and also addresses the difficulty of evaluating stateful agents whose actions can change files, browser state, accounts, or benchmark environments.

## Method
Magentic-One is a five-agent AutoGen-based system. A central Orchestrator maintains a task ledger for facts, guesses, and high-level plans, then runs a progress-ledger loop to decide whether the task is complete, whether the team is looping, whether progress is being made, which agent should act next, and what instruction to give. The worker agents are tool-centric: WebSurfer operates a Chromium browser, FileSurfer reads local files through a markdown preview tool, Coder writes and analyzes Python code, and ComputerTerminal executes code and shell commands. The authors also introduce AutoGenBench, an evaluation harness that runs agentic benchmarks with controlled initial conditions, Docker isolation, logs, repeated runs, and parallel execution.

## Key Findings
- Magentic-One is evaluated on GAIA, AssistantBench, and WebArena using the same core team design, with benchmark-specific answer formatting and setup prompts.
- Table 1 reports that the GPT-4o/o1-preview variant reaches 38.0% on GAIA and 13.3 exact match / 27.7 accuracy on AssistantBench, statistically comparable to the SOTA systems considered by the authors; the GPT-4o-only variant reaches 32.8% on WebArena, comparable to most SOTA methods but below WebPilot and Jace.AI.
- On the authors' WebArena split, performance is 35.1% on validation tasks and 30.5% on the held-out test split, which they treat as evidence that public WebArena evaluation can overfit and needs a hidden test set.
- GAIA validation ablations show that the ledger-based Orchestrator and all worker agents contribute: replacing the Orchestrator with a simple GroupChat controller drops performance, and removing any worker agent reduces success.
- Error analysis finds recurring failures from persistent inefficient actions, insufficient verification, inefficient navigation, underused resources, ignored errors, flawed technical steps, and imperfect team communication.
- The paper is explicit about limitations: high cost and latency, incomplete modality and action coverage, simple coding capabilities, fixed team membership, and no cross-task learning.

## Tags
`multi-agent`, `generalist-agents`, `agent-orchestration`, `tool-use`, `web-agents`, `agentic-evaluation`, `AutoGen`, `AutoGenBench`, `GAIA`, `AssistantBench`, `WebArena`

## Connections
- Builds directly on **AutoGen_2308.08155** by using AutoGen v0.4 as the multi-agent substrate and contributing a concrete generalist team architecture.
- Complements **GAIA_2311.12983** and **WebArena_2307.13854** as a system paper that evaluates across those benchmarks rather than introducing only a benchmark.
- Related to **WebVoyager_2401.13919**, **Mind2Web_2306.06070**, and **BrowserGymEcosystemforWebAgentResearch_2412.05467** through web-agent navigation, but Magentic-One adds file and code agents under a central orchestrator.
- Useful context for **CooperBench_2601.13295**, **CAID_2603.21489**, **SingleAgentOutperforms_2604.02460**, and **WhyMultiAgentFail_2503.13657** because it is an optimistic multi-agent architecture whose own ablations and error analysis expose coordination overhead and verification failures.
- Sits near **MetaGPT_2308.00352**, **ChatDev_2307.07924**, **AgentScope_2402.14034**, and **AgentVerse_2308.10848** as part of the shift from role-prompted multi-agent demos toward reusable agent frameworks and orchestrated tool use.
