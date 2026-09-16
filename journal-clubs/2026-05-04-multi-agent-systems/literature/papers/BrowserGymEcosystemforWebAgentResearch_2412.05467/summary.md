# The BrowserGym Ecosystem for Web Agent Research

**Authors:** Thibault Le Sellier De Chezelles, Maxime Gasse, Alexandre Lacoste, Alexandre Drouin, Massimo Caccia, Leo Boisvert, Megh Thakkar, Tom Marty, Rim Assouel, Sahar Omidi Shayegan, Lawrence Keunho Jang, Xing Han Lu, Ori Yoran, Dehan Kong, Frank F. Xu, Siva Reddy, Quentin Cappart, Graham Neubig, Ruslan Salakhutdinov, Nicolas Chapados
**arXiv:** 2412.05467
**Venue:** Preprint
**Date:** February 2025

## Problem
Web-agent research is fragmented across benchmarks with different APIs, setup requirements, action spaces, validation logic, and logging practices. This makes it hard to compare agents fairly, reproduce results, or test a new agent or benchmark without bespoke integration work.

## Method
The paper extends BrowserGym into a unified Gymnasium-style environment for browser tasks, with standardized observations, configurable action spaces, benchmark metadata, backend preparation, and task registration. It adds AgentLab as the companion experiment framework: studies can run many episodes in parallel, relaunch failures, record reproducibility metadata, inspect traces with AgentXRay, and reuse prompt/model abstractions for agent development. The ecosystem integrates MiniWoB, WebArena, VisualWebArena, WorkArena, WebLINX, and AssistantBench under the same interface.

## Key Findings
- BrowserGym exposes a broad benchmark set through one observation/action API, including synthetic UI tasks, self-hosted realistic websites, enterprise workflows, static trace prediction, and open-web question answering.
- AgentLab targets the practical bottlenecks of web-agent evaluation: parallel experiment execution, failed-run relaunching, reproducibility logging, trace replay, and step-level visual inspection.
- In the showcased GenericAgent evaluation, Claude 3.5 Sonnet leads most benchmark rows, while GPT-4o performs best on VisualWebArena, where visual inputs matter.
- The reported results still show large unsolved areas: even the strongest evaluated agents remain weak on difficult enterprise tasks, open-web information retrieval, and WorkArena L3.
- The authors treat reproducibility and safety as open challenges because live websites, changing APIs, robot detection, agent collisions, and arbitrary web actions can all affect results.

## Tags
`web-agents`, `browser-automation`, `benchmarking`, `agent-evaluation`, `gymnasium`, `reproducibility`, `LLM-agents`, `VLM-agents`, `experiment-management`

## Connections
- Directly extends **WorkArena** by exposing WorkArena tasks through BrowserGym and using them as part of the large-scale evaluation suite.
- Complements WebArena, VisualWebArena, WebLINX, MiniWoB, and AssistantBench by making them interoperable through a shared API rather than treating each benchmark as an isolated codebase.
- Useful context for papers about web-agent capability claims because it separates agent design from benchmark plumbing and encourages multi-benchmark evaluation.
- Relevant to safety and reliability work on UI agents because the limitations section highlights open-web risk, robot detection, non-determinism, and concurrent-agent interference.
