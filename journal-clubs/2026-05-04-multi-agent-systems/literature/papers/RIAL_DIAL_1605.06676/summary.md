# Learning to Communicate with Deep Multi-Agent Reinforcement Learning

**Authors:** Jakob N. Foerster, Yannis M. Assael, Nando de Freitas, Shimon Whiteson
**arXiv:** 1605.06676
**Venue:** Advances in Neural Information Processing Systems 29 (NIPS 2016)
**Date:** May 2016

## Problem
Cooperative agents in partially observable environments may need to communicate private observations before they can act optimally, but no protocol is supplied in advance. The paper asks how deep reinforcement learning can discover limited-bandwidth communication protocols when rewards are sparse and success depends on both sending useful messages and interpreting them correctly.

## Method
The paper introduces two approaches under centralized learning with decentralized execution. Reinforced Inter-Agent Learning (RIAL) combines deep recurrent Q-networks with independent or parameter-shared Q-learning over environment and communication actions. Differentiable Inter-Agent Learning (DIAL) replaces discrete communication actions during training with differentiable real-valued channels between agents, then uses a discretise/regularise unit to add noise during training and binarize messages at execution. Experiments evaluate these methods against a no-communication baseline on a switch-riddle task and two MNIST-based communication games.

## Key Findings
- DIAL learns communication protocols more reliably than RIAL in the harder settings because gradients can pass through the message channel from receiver back to sender.
- Parameter sharing is important: in the switch-riddle experiments it speeds learning, and without sharing RIAL fails to beat the no-communication baseline for the four-agent case.
- On the MNIST games, DIAL substantially outperforms the alternatives; RIAL fails on multi-step MNIST and gets stuck or unstable on colour-digit MNIST.
- The learned DIAL protocols are interpretable enough to extract decision trees or binary coding schemes from sampled episodes.
- Noise in the differentiable channel is not cosmetic; it regularizes continuous training-time messages so they discretize cleanly at execution.

## Tags
`multi-agent-rl`, `emergent-communication`, `differentiable-communication`, `ctde`, `deep-q-learning`, `partial-observability`, `rnn`, `protocol-learning`

## Connections
- A foundational pre-LLM paper for emergent communication in cooperative multi-agent systems.
- Closely related to CommNet, but DIAL focuses on training communication through differentiable channels that are discretized for decentralized execution.
- Connects to later centralized-training/decentralized-execution multi-agent RL methods by showing how centralized training can expose inter-agent gradients unavailable at execution time.
- Useful background for modern multi-agent agentic systems because it separates communication-channel design, shared parameters, and executable decentralized policies.
