# Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments

**Authors:** Ryan Lowe, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel, Igor Mordatch
**arXiv:** 1706.02275
**Venue:** Preprint
**Date:** June 2017; local PDF is arXiv v4 dated March 2020

## Problem
Independent deep RL methods are brittle in multi-agent environments because every agent is learning while the others change, making the environment non-stationary from any one agent's perspective. Q-learning loses the usual stationarity assumptions behind replay, while policy-gradient methods can get high-variance credit signals when rewards depend on several agents' coordinated actions. The target setting includes cooperative, competitive, and mixed physical/communication tasks where policies must execute using only local observations.

## Method
MADDPG adapts DDPG to centralized training with decentralized execution. Each agent has a local actor that maps its own observation to an action, but during training it learns a separate centralized critic conditioned on shared state/observations and all agents' actions. This lets agents have different or conflicting reward functions while still using replay and target networks. The paper also adds online approximations of other agents' policies when their policies are not directly known, and policy ensembles that expose each agent to multiple collaborator or opponent behaviors during training.

## Key Findings
- The centralized critic substantially improves cooperative communication: after 25,000 episodes, MADDPG reaches the target in 84.0% of evaluation episodes versus 32.0% for DDPG and lower rates for DQN, actor-critic, TRPO, and REINFORCE.
- In physical deception, MADDPG cooperative agents learn to cover landmarks to mislead an adversary; the paper reports high agent success and much lower adversary success than several DDPG pairings.
- In cooperative navigation and predator-prey, the advantage is less binary but MADDPG shows better coordination metrics, including fewer collisions in navigation and stronger predator performance against DDPG prey.
- In covert communication, MADDPG-trained Alice/Bob achieve larger advantage over Eve than DDPG-trained agents, without the extra cryptography-specific training tricks used in prior work.
- Learned approximations of other agents' policies can support MADDPG training in the cooperative communication task without a significant convergence slowdown, and policy ensembles improve competitive robustness in the reported tasks.

## Tags
`multi-agent-rl`, `MADDPG`, `actor-critic`, `DDPG`, `centralized-training-decentralized-execution`, `mixed-motive-games`, `emergent-communication`, `policy-ensembles`

## Connections
- A core early reference for centralized training with decentralized execution in deep multi-agent reinforcement learning.
- Extends DDPG rather than value-based MARL, making it important for continuous-control particle-world benchmarks with physical actions.
- Closely connected to work on emergent communication and grounded communication, but removes the requirement that communication occur through a differentiable channel.
- Useful contrast with later multi-agent coordination papers: this paper solves training-time non-stationarity with shared critic information, while later agent-system work often focuses on runtime communication, delegation, and integration.
