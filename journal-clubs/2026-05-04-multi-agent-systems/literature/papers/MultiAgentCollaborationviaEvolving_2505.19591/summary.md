# Multi-Agent Collaboration via Evolving Orchestration

**Authors:** Yufan Dang, Chen Qian, Xueheng Luo, Jingru Fan, Zihao Xie, Ruijie Shi, Weize Chen, Cheng Yang, Xiaoyin Che, Ye Tian, Xuantang Xiong, Lei Han, Zhiyuan Liu, Maosong Sun
**arXiv:** 2505.19591
**Venue:** NeurIPS 2025
**Date:** October 2025

## Problem
LLM-based multi-agent systems often use static or manually designed agent topologies. As tasks become more complex and agent pools grow, those fixed structures can create coordination overhead, redundant computation, ineffective communication, and weak scalability. The paper asks whether a dynamic orchestrator can improve both collaboration quality and inference efficiency.

## Method
Puppeteer treats multi-agent reasoning as a sequential decision process controlled by a centralized policy. At each step, the policy observes the evolving global task state and selects one agent from a pool of model, reasoning-pattern, and tool combinations. The serialized trajectory can be folded back into a directed reasoning graph, allowing chains, branches, cycles, and repeated agent activations without predefining a fixed topology. The orchestrator is trained online with REINFORCE using rewards that combine task quality with token or compute cost, encouraging the policy to activate useful agents and terminate or prune redundant reasoning.

## Key Findings
- Table 1 reports the best average performance for evolved Puppeteer in both tested agent subspaces: 0.6324 in Mimas and 0.7731 in Titan, ahead of the listed pure-model, single-agent, and multi-agent baselines by average score.
- Evolution generally improves the orchestrator over its initialized phase; for example, Titan Puppeteer rises from 0.6893 to 0.7731 average score, while Titan Puppeteer-Mono rises from 0.6671 to 0.7453.
- Figures 2 and 3 show token consumption declining through training across most settings, suggesting the reward design can improve efficiency rather than simply spending more inference.
- Section 3.3 and Figure 6 argue that learned organizations become more compact and cyclic, with denser agent interaction graphs and more feedback loops after evolution.
- Hyperparameter analysis in Figure 7 shows a non-monotonic trade-off between topology width/depth, token cost, and accuracy; larger search structures are not automatically better.
- Appendix D notes important limits: rewards are coarse-grained, the agent/tool set is fixed, and the system can still show occasional mis-coordination or agreement on wrong behavior.

## Tags
`multi-agent`, `LLM-agents`, `agent-orchestration`, `reinforcement-learning`, `dynamic-topology`, `graph-of-thought`, `tool-use`, `efficiency`

## Connections
- Extends graph-optimized MAS work such as **GPTSwarm** and **MacNet** by using a centralized policy that dynamically unfolds agent activations during inference rather than relying on a fixed graph.
- Contrasts with **MAS-GPT**, which trains an LLM to generate a task-specific MAS in one shot; Puppeteer instead learns an online orchestration policy over a fixed agent/tool pool.
- Responds to concerns in **WhyMultiAgentFail** and **CooperBench** by treating coordination structure and cost-aware agent selection as core optimization targets.
- Related to **ChatDev** and **AgentVerse** as LLM multi-agent frameworks, but focused on adaptive reasoning topologies rather than role-play workflows.
- Relevant to **AgentScalingDiversity** and **ScienceOfScaling** because it studies when more agents or wider/deeper orchestration helps versus when it adds overhead.
