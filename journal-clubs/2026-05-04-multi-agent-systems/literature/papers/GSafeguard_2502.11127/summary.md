# G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems

**Authors:** Shilong Wang, Guibin Zhang, Miao Yu, Guancheng Wan, Fanci Meng, Chongye Guo, Kun Wang, Yang Wang
**arXiv:** 2502.11127
**Venue:** Preprint
**Date:** February 2025

## Problem
LLM-based multi-agent systems inherit single-agent security risks and add a new failure mode: malicious or misleading utterances can propagate through agent-to-agent communication. Existing guardrails often operate on individual prompts or outputs and do not account for MAS topology, communication history, or the need to transfer across different agent counts, LLM backbones, and interaction structures.

## Method
G-Safeguard treats a multi-agent dialogue as a dynamic utterance graph. At the end of each dialogue round, it embeds each agent's current and historical utterances as node features and embeds pairwise interaction histories as edge features. An edge-aware graph neural network performs node classification to identify attacked or infected agents. For remediation, G-Safeguard prunes outgoing edges from detected risky agents in the next round, limiting further spread of adversarial information. The paper trains the detector with cross-entropy on attack labels and evaluates prompt injection, tool attack, and memory poisoning across several MAS topologies, datasets, and LLM backbones.

## Key Findings
- The paper reports that G-Safeguard reduces attack success rate after multi-round communication under prompt injection on CSQA and MMLU, with larger reported reductions in denser topologies.
- The defense is presented as topology- and model-transferable: a detector trained on GPT-4o-mini communication data is evaluated across GPT-4o, LLaMA-3.1-70B, Claude-3.5-haiku, and DeepSeek-V3 systems and multiple graph structures.
- Scalability experiments train on an 8-agent MAS and apply the same safeguard to larger MAS with 20 to 80 agents without retraining.
- In a CAMEL-style multi-role setting, G-Safeguard identifies attackers with reported accuracy above 80% on CSQA and MMLU.
- Results are not uniformly positive across every condition: some tool-attack settings worsen with G-Safeguard, and the paper's limitation section notes that the method reacts after communication data exists rather than preventing initial compromise.

## Tags
`multi-agent-security`, `LLM-agents`, `prompt-injection`, `memory-poisoning`, `tool-attack`, `GNN`, `topology-aware-defense`, `utterance-graph`, `edge-pruning`

## Connections
- Extends single-agent guardrail thinking by making inter-agent communication topology part of both detection and remediation.
- Closely related to NetSafe-style work on topology-based misinformation or toxicity propagation in MAS, but adds a concrete GNN detector and edge-pruning treatment.
- Relevant to MAS framework papers such as AutoGen, CAMEL, GPTSwarm, AgentPrune, and graph-structured agent pipelines because it treats the communication graph as a security surface.
- Complements multi-agent evaluation work such as CooperBench by focusing on security and contamination rather than collaborative coding success.
