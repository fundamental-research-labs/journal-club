# Generative Agents: Interactive Simulacra of Human Behavior

**Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
**arXiv:** 2304.03442
**Venue:** UIST 2023
**Date:** October 2023

## Problem
Interactive systems, games, design tools, and social simulations need agents that behave believably over time, but scripted NPCs and single-prompt LLM personas struggle with open-ended behavior, long-term coherence, changing memories, and cascading social interactions among many agents.

## Method
The paper introduces "generative agents": LLM-driven agents embedded in a Sims-like sandbox town, Smallville. Each agent starts with a short natural-language persona and accumulates a memory stream of observations, plans, and reflections. A retrieval function combines recency, importance, and relevance to select memories for prompting. Reflection periodically synthesizes raw observations into higher-level inferences, while planning creates daily agendas and recursively decomposes them into shorter actions. Users can observe, converse with, or intervene in the world through natural language.

## Key Findings
- In Smallville, 25 agents produced individual routines and emergent social behaviors such as information diffusion, relationship formation, and coordination around a Valentine's Day party from a small initial seed.
- In a controlled interview evaluation, the full architecture was rated more believable than ablations that removed reflection, planning, or memory access, suggesting that all three components contribute to coherent behavior.
- The end-to-end two-day deployment showed information spreading through the community: Sam's candidacy and Isabella's party reached additional agents without direct user scripting.
- The architecture remained imperfect: failures included missing relevant memories, embellishing facts, choosing socially odd locations or actions, and overly formal or cooperative dialogue inherited from the underlying model.

## Tags
`generative-agents`, `llm-agents`, `human-ai-interaction`, `multi-agent-simulation`, `believable-agents`, `memory-retrieval`, `reflection`, `planning`, `npc-behavior`, `social-simulation`

## Connections
- Early canonical reference for LLM agents that combine long-term memory, retrieval, reflection, and planning rather than relying on stateless prompting.
- Important bridge between believable-agent/NPC research and modern LLM-based agent architectures.
- Related to social simulacra and synthetic-user work, but extends it from stateless personas to persistent agents with evolving memory and relationships.
- Relevant to later multi-agent systems work: it demonstrates emergent coordination, but also exposes fragility around hallucination, memory retrieval, and social norm grounding.
- Complements benchmark papers such as CooperBench by showing multi-agent social behavior in a sandbox rather than evaluating task success in shared software work.
