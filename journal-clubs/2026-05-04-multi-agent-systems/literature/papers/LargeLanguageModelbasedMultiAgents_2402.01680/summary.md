# Large Language Model based Multi-Agents: A Survey of Progress and Challenges

**Authors:** Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang
**arXiv:** 2402.01680
**Venue:** Preprint
**Date:** April 2024

## Problem
LLM-based multi-agent systems had rapidly expanded across coding, robotics, debate, social simulation, games, economics, policy, and public-health settings, but the work was fragmented. The survey asks how these systems should be described and compared: what environments they operate in, how agents are profiled, how agents communicate, how capabilities improve, what applications and benchmarks exist, and what challenges remain.

## Method
The paper is a taxonomy-driven survey. It first contrasts single-agent LLM capabilities with multi-agent systems, then organizes LLM-MA work around four system axes: agents-environment interface, agent profiling, agent communication, and agent capability acquisition. It also groups applications into problem solving and world simulation, summarizes implementation frameworks such as MetaGPT, CAMEL, and AutoGen, lists commonly used datasets and benchmarks, and closes with open challenges.

## Key Findings
- LLM-MA systems are framed as combining specialized agent profiles with inter-agent interaction, extending single-agent planning, tool use, and memory.
- The survey's core schema distinguishes interface choices, profiling methods, communication patterns, and capability-acquisition mechanisms.
- Applications cluster into problem solving, such as software development, embodied agents, science experiments, and science debate, and world simulation, such as society, gaming, psychology, economy, recommender systems, policy, and disease propagation.
- Communication design is a first-class dimension: systems vary by cooperative, debate, or competitive paradigms; layered, decentralized, centralized, or shared-message-pool structures; and mostly textual content.
- The paper identifies open problems around multimodal environments, hallucination propagation, collective intelligence, scaling and orchestration, and benchmark coverage for emergent multi-agent behavior.

## Tags
`LLM-MA`, `multi-agent-survey`, `agent-communication`, `agent-profiling`, `capability-acquisition`, `world-simulation`, `problem-solving`, `benchmarks`

## Connections
- Provides broad background for frameworks such as AutoGen, MetaGPT, and CAMEL.
- Useful taxonomy for later empirical multi-agent coding work such as CooperBench and CAID, which stress-test coordination and orchestration choices.
- Complements agent benchmarks such as AgentBench and WebArena by focusing on multi-agent system design and applications rather than only single-agent task performance.
- Sets up recurring corpus themes: communication topology, role specialization, shared environments, hallucination propagation, and benchmark gaps for emergent behavior.
