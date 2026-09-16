# MemGPT: Towards LLMs as Operating Systems

**Authors:** Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez
**arXiv:** 2310.08560
**Venue:** Preprint
**Date:** February 2024

## Problem
LLMs have fixed context windows, which makes long conversations and large-document analysis difficult even when the underlying model is strong. Simply expanding transformer context is expensive and can still fail when models underuse information buried in long prompts. The paper asks whether an LLM agent can instead manage context as a scarce memory resource, paging relevant information into the prompt when needed.

## Method
MemGPT treats the prompt as "main context" and external stores as longer-term memory. Its main context includes read-only system instructions, a writable working context, and a FIFO message queue; external context includes recall storage for conversation history and archival storage for larger documents or data. The LLM uses function calls to edit working memory, search recall or archival storage, and chain multiple retrieval steps before answering. A queue manager issues memory-pressure warnings and evicts old messages into recall storage, giving the model a mechanism analogous to OS virtual memory paging.

## Key Findings
- On the Multi-Session Chat deep memory retrieval task, MemGPT improves all tested base models over fixed-context baselines; the largest reported runs are GPT-4 + MemGPT and GPT-4 Turbo + MemGPT, both above 90% accuracy in Table 2.
- On conversation openers, MemGPT generates openers that score similarly to or above human openers on persona-similarity metrics, though not on direct similarity to the human-written opener.
- For multi-document QA, MemGPT can iteratively page through archival search results, so its effective document pool is not limited to the documents that fit in the model prompt.
- On nested key-value retrieval, MemGPT with GPT-4 remains robust across increasing nesting levels, while fixed-context baselines fail on multi-hop lookup as nesting grows.
- Performance depends on the underlying model's ability to use function calls reliably; the paper reports weaker behavior for GPT-3.5 and some dropoff for GPT-4 Turbo in nested lookup.

## Tags
`long-context`, `memory`, `llm-agents`, `virtual-context`, `retrieval`, `function-calling`, `conversational-agents`, `document-qa`

## Connections
- Connects long-context LLM work with retrieval-augmented agents by making retrieval and memory edits part of the agent control loop rather than a one-shot preprocessing step.
- Relevant to papers on persistent agent memory, including conversational agents and generative-agent systems that need user-specific long-term state.
- Useful contrast to long-context scaling papers: MemGPT argues for memory hierarchy and paging even when larger context windows are available.
- Related to tool-using agents: the core mechanism is reliable function calling for self-directed memory updates, search, pagination, and multi-step retrieval.
