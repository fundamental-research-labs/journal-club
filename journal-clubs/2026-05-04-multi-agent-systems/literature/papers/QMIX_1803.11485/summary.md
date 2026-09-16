# QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning

**Authors:** Tabish Rashid, Mikayel Samvelyan, Christian Schroeder de Witt, Gregory Farquhar, Jakob Foerster, Shimon Whiteson
**arXiv:** 1803.11485
**Venue:** Proceedings of the 35th International Conference on Machine Learning (ICML 2018)
**Date:** June 2018

## Problem
Cooperative multi-agent reinforcement learning often needs decentralized execution: each agent must act from its own local action-observation history. During training, however, simulators may expose global state and remove communication constraints. The paper asks how to exploit centralized training to learn a joint action-value function while still extracting tractable decentralized policies.

## Method
QMIX is a value-based centralized-training/decentralized-execution method. Each agent has a recurrent network estimating a local action-value `Qa` from its own observation history and action. A mixing network combines the per-agent values into a joint `Qtot`, with non-negative mixing weights enforcing monotonicity between each `Qa` and `Qtot`. Hypernetworks condition the mixing weights and biases on the global state, allowing centralized state information to shape the joint value estimate without being needed at execution time. The method is trained end-to-end with an off-policy temporal-difference loss.

## Key Findings
- The monotonic factorization makes the centralized greedy action over `Qtot` consistent with independent greedy choices over each agent's `Qa`, avoiding enumeration of the full joint action space.
- On the paper's StarCraft II micromanagement tasks, QMIX generally outperforms independent Q-learning and VDN, with the clearest gains on heterogeneous-unit maps.
- A two-step matrix game illustrates the representational difference: QMIX recovers the optimal branch that VDN's additive factorization cannot represent.
- Ablations indicate that both global state conditioning and nonlinear mixing matter on heterogeneous maps, while simpler variants can be competitive on easier homogeneous maps.
- The monotonic constraint is also the method's main limitation: QMIX cannot perfectly represent joint values where an agent's preferred action depends non-monotonically on the simultaneous actions of other agents.

## Tags
`multi-agent-rl`, `centralized-training-decentralized-execution`, `value-factorization`, `QMIX`, `StarCraft-II`, `Dec-POMDP`, `deep-Q-learning`, `cooperative-agents`

## Connections
- Extends VDN by replacing a fixed additive decomposition with a learned monotonic, state-conditioned mixing network.
- Contrasts with IQL by using centralized joint value learning instead of treating other learning agents as part of a non-stationary environment.
- Provides a value-based alternative to centralized-critic actor-critic approaches such as COMA.
- Foundational citation for later cooperative MARL work that uses StarCraft micromanagement and value-decomposition baselines.
