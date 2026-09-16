# Counterfactual Multi-Agent Policy Gradients

**Authors:** Jakob N. Foerster, Gregory Farquhar, Triantafyllos Afouras, Nantas Nardelli, Shimon Whiteson
**arXiv:** 1705.08926
**Venue:** AAAI 2018
**Date:** May 2017 arXiv release; local PDF is arXiv v3 dated December 2024

## Problem
Cooperative multi-agent reinforcement learning needs decentralized execution policies, but global rewards make it hard to assign credit to each agent's action. Independent actor-critic methods ignore much of the centralized training information, while naive centralized critics still give every actor a noisy global training signal.

## Method
COMA is an actor-critic method for centralized training with decentralized execution. Each agent executes a shared recurrent actor conditioned only on its local action-observation history and agent identity. During training, a centralized critic conditions on the global state, joint history, and joint action. The policy-gradient advantage for each agent subtracts a counterfactual baseline: the critic marginalizes over that agent's possible actions while keeping the other agents' actions fixed. The critic is represented so it outputs Q-values for all actions of one agent in a single forward pass rather than enumerating the full joint action space.

## Key Findings
- COMA outperforms independent actor-critic baselines and centralized-critic ablations on four partially observable StarCraft micromanagement scenarios.
- The central critic helps: centralized baselines outperform decentralized IAC variants in the reported experiments.
- The counterfactual baseline matters: COMA improves over a centralized Q/V ablation that uses a standard value baseline instead.
- Table 1 reports the best mean final win percentages among local-field-of-view methods for COMA on all four maps: 3m, 5m, 5w, and 2d 3z.
- Best COMA agents are competitive with some previously published centralized StarCraft controllers, though those comparisons use easier full-field-of-view, central-control settings.

## Tags
`multi-agent-rl`, `centralized-training`, `decentralized-execution`, `actor-critic`, `policy-gradient`, `credit-assignment`, `counterfactual-baseline`, `StarCraft`

## Connections
- Foundational CTDE actor-critic paper for cooperative MARL, closely related to later methods such as MAPPO that also rely on centralized critics with decentralized policies.
- Complements value-factorization approaches by handling credit assignment through an agent-specific policy-gradient baseline rather than decomposing a joint action-value function.
- Useful predecessor for StarCraft micromanagement and SMAC-style benchmark discussions.
- Related to difference rewards and aristocrat utilities, but replaces simulator-based default-action comparisons with critic-evaluated counterfactuals.
- Contrasts with communication-centered multi-agent work: COMA improves coordination without requiring agents to communicate at execution time.
