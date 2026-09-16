# tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

**Authors:** Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan
**arXiv:** 2406.12045
**Venue:** Preprint
**Date:** June 2024

## Problem
Most agent and tool-use benchmarks either give all user information up front or evaluate static trajectories. Real deployed agents must instead converse with users, gather missing information, call APIs, follow detailed domain policies, and remain reliable across repeated interactions with the same underlying intent.

## Method
tau-bench formulates each task as an interaction among a language agent, a simulated user, and hidden databases exposed through API tools. Each domain contains database JSON files, Python APIs, a domain policy document, user-simulator instructions, and ground-truth database actions/outputs. The first release covers two customer-service domains: tau-retail and tau-airline. Evaluation compares the final database state and required user-facing outputs to an annotated unique goal state, and the paper introduces pass^k to measure whether an agent succeeds consistently across k repeated stochastic trials.

## Key Findings
- tau-bench combines realistic dialogue, API use, and policy following: tau-retail has users/products/orders and 115 tasks, while tau-airline has users/flights/reservations and 50 tasks.
- Function calling is the strongest tested agent interface, but even the best reported model, gpt-4o, reaches only 61.2 pass^1 on tau-retail and 35.2 on tau-airline.
- Reliability drops sharply under repeated trials: in tau-retail, gpt-4o function calling falls below 25 pass^8 despite pass^1 above 60.
- Failure analysis on tau-retail highlights wrong tool arguments or user-facing information, incorrect policy-driven decisions, and partial completion of compound requests.
- Removing the policy prompt hurts gpt-4o much more on tau-airline than tau-retail, suggesting the airline domain better stresses ad-hoc rule following.

## Tags
`language-agents`, `tool-use`, `function-calling`, `user-simulation`, `task-oriented-dialogue`, `agent-benchmark`, `reliability`, `policy-following`, `customer-service`

## Connections
- Complements WebArena, WebShop, AgentBench, BFCL, ToolBench, and ToolEmu by adding multi-turn user interaction and domain-policy adherence to tool-use evaluation.
- Useful alongside WorkArena and other real-world agent benchmarks when discussing business-process agents that must use APIs rather than only browse or operate UIs.
- Connects to task-oriented dialogue work such as MultiWOZ, but replaces static dialogue replay with LM-simulated users and database-state evaluation.
- The pass^k metric is a useful counterpoint to code-generation pass@k: for deployed service agents, repeated consistency is often more important than at-least-once discovery.
