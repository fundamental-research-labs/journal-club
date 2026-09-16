# Emergence of Grounded Compositional Language in Multi-Agent Populations

**Authors:** Igor Mordatch, Pieter Abbeel
**arXiv:** 1703.04908
**Venue:** AAAI 2018
**Date:** July 2018

## Problem
Most language-learning systems model statistical regularities in text, but that does not explain why communication arises or how agents learn to use it to coordinate. This paper asks whether grounded, compositional language can emerge from non-linguistic cooperative goals without text corpora, human demonstrations, assigned speaker/listener roles, or explicit language-use rewards.

## Method
The paper defines a cooperative partially observable Markov game in a continuous two-dimensional particle world with multiple agents and landmarks. Agents have private grounded goals such as going to or looking at a landmark, sometimes requiring another agent to act, and all agents share a joint reward. Each agent uses the same decentralized neural policy, with recurrent modules for communication streams and shared modules for physical observations so execution can vary by number of agents and entities. Discrete utterances are trained through a Gumbel-Softmax relaxation, allowing backpropagation through the joint physical and communication dynamics. The system adds an auxiliary goal-prediction reward and a Dirichlet-Process-inspired vocabulary penalty to encourage compact active vocabularies.

## Key Findings
- Learned discrete symbol streams develop interpretable vocabularies and syntax, with symbols that can refer separately to landmarks, actions, and agents.
- Communication substantially improves task reward over a no-communication baseline in the main tested setting; Table 1 reports test physical reward of -0.392 with communication versus -0.920 without.
- The emergent language is context-sensitive: when only one landmark or one action type is possible, agents omit symbols for concepts already clear from context.
- Physical grounding affects word order; for example, the action symbol corresponding to `GOTO` tends to appear first because the listener can start moving before receiving the destination symbol.
- A vocabulary-size penalty leads agents to explore larger symbol sets early and then settle into smaller active vocabularies aligned with task complexity.
- When verbal communication is unavailable but physical observation is possible, agents discover non-verbal strategies such as pointing, guiding, and pushing.

## Tags
`emergent-language`, `grounded-language`, `multi-agent-rl`, `compositionality`, `communication`, `gumbel-softmax`, `embodied-agents`, `cooperative-markov-games`

## Connections
- Useful early evidence for treating language as a tool for coordination rather than only a distribution over text.
- Complements work on differentiable multi-agent communication by grounding discrete protocols in physical action, private goals, and shared reward.
- Relevant to later multi-agent communication research because it separates learned symbolic protocols from human-readable natural-language dialogue.
- Connects to compositionality and language-evolution arguments: the paper explicitly tests vocabulary pressure and varied task configurations as drivers of reusable symbols.
