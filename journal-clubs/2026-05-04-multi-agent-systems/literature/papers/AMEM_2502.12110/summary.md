# A-Mem: Agentic Memory for LLM Agents

**Authors:** Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, Yongfeng Zhang
**arXiv:** 2502.12110
**Venue:** Preprint
**Date:** October 2025

## Problem
LLM agents need long-term memory to use historical experience during extended interactions. Existing memory systems can store and retrieve past interactions, but many rely on predefined storage schemas, fixed read/write points, or static graph structures that limit adaptation when new tasks, relationships, and user histories emerge.

## Method
A-Mem is a Zettelkasten-inspired memory system for LLM agents. Each interaction is converted into an atomic memory note with original content, timestamp, LLM-generated keywords, tags, contextual description, embedding, and links. When a new memory arrives, A-Mem retrieves nearby historical notes with embedding similarity, asks an LLM to generate meaningful links, and can evolve existing notes by updating their context, keywords, and tags in light of the new memory. At retrieval time, the system embeds the current query and retrieves the top-k relevant memories as context for the agent.

## Key Findings
- On LoCoMo long-term conversational QA, A-Mem is reported with the best average F1/BLEU-1 ranking across the six tested foundation-model settings, though not every task category is won by A-Mem.
- On DialSim, A-Mem outperforms the LoCoMo and MemGPT baselines across the reported F1, BLEU-1, ROUGE-L, ROUGE-2, METEOR, and SBERT-similarity metrics.
- Ablations show that removing both link generation and memory evolution sharply weakens performance; keeping link generation but removing memory evolution gives intermediate results, while the full system is best across the reported categories.
- Selective top-k retrieval reduces prompt token length substantially compared with full-history baselines in the paper's setup.
- Scaling experiments report linear memory usage like vector-retrieval baselines and low retrieval latency up to 1 million stored memories; this excludes the cost of LLM-based note construction and evolution.

## Tags
`agent-memory`, `LLM-agents`, `long-term-memory`, `Zettelkasten`, `memory-evolution`, `retrieval`, `LoCoMo`, `DialSim`

## Connections
- Directly related to **MemGPT** as a competing long-term memory architecture, but A-Mem emphasizes evolving note networks rather than virtual context management.
- Connects to **MemoryBank** and other agent memory systems by replacing mostly fixed memory operations with LLM-generated note attributes, links, and updates.
- Adjacent to agentic RAG: A-Mem argues that agency should occur not only at retrieval time but also during memory storage, linking, and evolution.
- Useful alongside benchmark work on long-context and long-term conversational agents, especially LoCoMo-style multi-hop and temporal QA.
