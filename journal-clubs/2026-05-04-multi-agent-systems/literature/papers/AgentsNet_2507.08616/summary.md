# AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs

**Authors:** Florian Grotschla, Luis Muller, Jan Tonshoff, Mikhail Galkin, Bryan Perozzi
**arXiv:** 2507.08616
**Venue:** Preprint
**Date:** July 2025

## Problem
Existing multi-agent LLM benchmarks often measure task success with small agent groups, but do not directly test whether a network of agents can self-organize, use its topology, communicate locally, and coordinate toward a globally valid solution. AgentsNet frames these as core distributed-system capabilities rather than as side effects of general reasoning benchmarks.

## Method
AgentsNet maps five classical distributed computing problems into LLM-agent tasks: graph coloring, minimal vertex cover, maximal matching, leader election, and consensus. Each agent is an LLM node in a graph, knows only its name and immediate neighbors, exchanges JSON messages with neighbors for fixed synchronous rounds, and then emits a task-specific final answer. The main evaluation uses small-world, scale-free, and Delaunay graph topologies with 4, 8, and 16 agents; an additional scaling probe goes up to 100 agents. Scoring is strict binary success for the whole network, with soft scores reported in the appendix.

## Key Findings
- AgentsNet is not saturated by frontier models: the best reported aggregate score is Gemini 2.5 Pro at 0.80, followed by Claude 3.7 Sonnet at 0.70 and Gemini 2.5 Flash at 0.69.
- Consensus and leader election are often easier than graph coloring, matching, and especially vertex cover; the paper reports low vertex-cover success for most models on larger graphs.
- Performance generally drops as graph size increases. In the 20- to 100-agent scaling experiment with Gemini 2.0 Flash, success falls toward zero at 100 agents.
- Qualitative traces show that strategy coordination is a major failure mode: agents may agree on plans too late, follow unstated local strategies, over-trust inaccurate or outdated neighbor messages, or fail to revise assumptions.
- The benchmark is generative and topology-aware, so difficulty can be increased by changing graph size and structure rather than by hand-authoring new tasks.

## Tags
`multi-agent`, `benchmark`, `distributed-systems`, `graph-reasoning`, `message-passing`, `coordination`, `local-communication`, `scalability`

## Connections
- Complements **CooperBench**: both probe multi-agent coordination failures, but AgentsNet isolates graph-topology and message-passing behavior rather than collaborative software patches.
- Contrasts with **CAID**: CAID imposes centralized delegation and git-based isolation, while AgentsNet tests decentralized local communication and emergent coordination.
- Related to broad agent benchmarks such as **MultiAgentBench** and **AgentBench**, but focused on theoretically grounded distributed coordination tasks.
- Useful alongside topology-based multi-agent work such as GPTSwarm and AgentVerse because it asks whether agents can actually exploit a communication graph, not just whether a fixed topology improves final accuracy.
