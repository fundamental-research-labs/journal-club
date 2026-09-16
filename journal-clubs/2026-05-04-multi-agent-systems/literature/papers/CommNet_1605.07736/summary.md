# Learning Multiagent Communication with Backpropagation

**Authors:** Sainbayar Sukhbaatar, Arthur Szlam, Rob Fergus
**arXiv:** 1605.07736
**Venue:** NIPS 2016
**Date:** October 2016

## Problem
Cooperative multi-agent systems often need communication because each agent has limited local visibility, but many MARL systems either assume full observability or rely on hand-specified communication protocols. The paper asks whether agents can learn a useful communication protocol jointly with their policies and still support variable numbers of agents.

## Method
CommNet is a shared neural controller for fully cooperative agents. Each agent has a hidden state and receives a continuous communication vector computed from the average hidden states of the other agents. Repeating this update for one or more communication steps lets agents exchange information before sampling actions. Because communication is continuous, the whole controller can be trained by backpropagation under supervised losses or with policy-gradient reinforcement learning. The paper also describes local connectivity, skip connections, and recurrent/LSTM variants, and evaluates on lever pulling, traffic junction, combat, and bAbI question answering.

## Key Findings
- On the lever-pulling task, CommNet nearly solves the coordination problem under both supervised and reinforcement training, while the independent controller stays far lower (Table 1).
- On the traffic junction task, CommNet reduces collision failure rates across MLP, RNN, and LSTM modules, with the LSTM CommNet at 1.6% failure versus 9.4% for the independent LSTM baseline (Table 2).
- Communication becomes more valuable as traffic visibility decreases; the paper reports that CommNet still succeeds about 90% of the time when cars have zero visibility.
- In combat, CommNet improves win rates over independent and fully connected baselines across module choices, though some settings have large variance (Table 3).
- On bAbI, treating sentences as agents with communication improves over an independent MLP formulation and an LSTM baseline, but remains behind memory-network-style models designed for the dataset (Table 4).
- PCA analysis of traffic communication vectors suggests a sparse learned protocol: many messages are near zero, while distinct clusters align with locations and braking behavior relevant to avoiding collisions.

## Tags
`multi-agent`, `reinforcement-learning`, `learned-communication`, `continuous-communication`, `emergent-communication`, `message-passing`, `graph-neural-network`, `cooperative-agents`

## Connections
- Early neural learned-communication paper for cooperative MARL; useful historical background for later emergent communication and differentiable inter-agent messaging work.
- Closely related to Foerster et al.'s concurrent RIAL/DIAL work, but CommNet uses continuous broadcast-style communication cycles rather than discrete symbols as the primary channel.
- Connects learned agent communication to graph/message-passing neural networks: agents are nodes, communication edges can be broadcast or local, and the shared update is permutation invariant.
- Contrasts with modern LLM multi-agent communication systems such as AutoGen or CooperBench: CommNet studies non-language continuous protocols in small controlled domains rather than natural-language coordination in open-ended software tasks.
