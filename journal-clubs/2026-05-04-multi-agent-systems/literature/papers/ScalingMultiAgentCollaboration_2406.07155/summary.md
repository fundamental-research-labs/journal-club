# Scaling Large-Language-Model-based Multi-Agent Collaboration

**Authors:** Chen Qian, Zihao Xie, YiFei Wang, Wei Liu, Kunlun Zhu, Hanchen Xia, Yufan Dang, Zhuoyun Du, Weize Chen, Cheng Yang, Zhiyuan Liu, Maosong Sun
**arXiv:** 2406.07155
**Venue:** ICLR 2025
**Date:** March 2025

## Problem
Most LLM multi-agent systems evaluate small teams, often fewer than ten agents, so it is unclear whether adding agents at inference time yields predictable gains or just coordination overhead. The paper asks whether a "collaborative scaling law" exists and what network structures make larger agent teams workable without context explosion.

## Method
MACNET organizes agents as a directed acyclic graph. Actor agents occupy nodes and produce artifacts, while critic agents occupy edges and issue refinement instructions. Reasoning proceeds in topological order through local dual-agent interactions, and only the refined artifact is propagated forward rather than the full conversation. The paper evaluates chain, star, tree, mesh, layer, and random topologies on MMLU, HumanEval, SRDD, and CommonGen-Hard against COT, AutoGPT, GPTSwarm, and AgentVerse, using GPT-3.5 for interactive reasoning.

## Key Findings
- Table 1 reports that MACNET variants achieve the strongest average "Quality" scores among the evaluated methods, with random and mesh topologies leading on the aggregate metric.
- MACNET is not uniformly best on every dataset: for example, AgentVerse is strongest on HumanEval, while MACNET variants are stronger on average across the four tasks.
- Topology matters. The paper finds no single topology wins everywhere, but irregular random topologies often outperform regular ones and use substantially less time than dense mesh topologies.
- The artifact-only memory control is presented as the key scalability mechanism, reducing the sink-agent context growth from quadratic to linear in the network scale under the paper's mesh analysis.
- Scaling agent networks from 2^0 to 2^6 nodes produces a sigmoid/logistic-style performance curve with saturation, supporting collaboration among more than a thousand node-and-edge agents in dense settings.
- The proposed explanation for collaborative emergence is that larger networks surface more diverse critique/refinement aspects and produce longer, more comprehensive artifacts; the paper treats this as a plausible mechanism rather than a settled causal proof.

## Tags
`multi-agent`, `LLM-agents`, `collaborative-scaling-law`, `MACNET`, `graph-topology`, `actor-critic`, `artifact-refinement`, `inference-time-scaling`, `ICLR-2025`

## Connections
- Related to **MoreAgentsIsAllYouNeed** because both study whether adding LLM agents improves performance, but MACNET emphasizes structured interdependent interaction rather than independent sampling or voting.
- Extends the line from **AgentVerse**, **ChatDev**, and **GPTSwarm** by treating agent organization as a topology and comparing chains, trees, graphs, and random networks.
- Useful context for **AgentScalingDiversity** and **ScienceOfScaling** because it frames multi-agent collaboration as an inference-time scaling phenomenon with saturation and topology-dependent returns.
- A counterpoint for **WhyMultiAgentFail**, **SingleAgentOutperforms**, and **CooperBench**: this paper argues scaling can help when topology and memory flow are constrained, while later work stresses coordination failures in less controlled settings.
