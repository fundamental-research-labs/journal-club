# AgentRxiv: Towards Collaborative Autonomous Research

**Authors:** Samuel Schmidgall, Michael Moor
**arXiv:** 2503.18102
**Venue:** Preprint
**Date:** March 2025

## Problem
Autonomous research agent systems can generate papers, run experiments, and write reports, but they usually operate as isolated laboratories. The paper argues that this misses a key property of scientific progress: researchers iteratively build on prior work and share partial discoveries over time.

## Method
AgentRxiv is a local, arXiv-like preprint server for autonomous agent laboratories. Agents can upload papers, search and retrieve prior agent-generated reports, and access results asynchronously through a web app and JSON API. The system extracts text and metadata from uploaded papers, embeds stored papers and search queries with a SentenceTransformer, ranks matches by cosine similarity, and returns the top relevant prior work during the agents' literature review stage. Experiments build on Agent Laboratory, tasking agents with discovering reasoning and prompting techniques for MATH-500, then testing the best discovered method across other benchmarks, models, and parallel laboratory settings.

## Key Findings
- In a sequential run, giving agents access to prior AgentRxiv papers supports cumulative improvement on MATH-500, from a 70.2% gpt-4o mini baseline to 78.2% with Simultaneous Divergence Averaging (SDA).
- Removing access to previous AgentRxiv papers causes MATH-500 progress to plateau around 73-74% in the reported ablation.
- SDA generalizes beyond its discovery setting in the paper's tests: it improves GPQA, MMLU-Pro, and MedQA with the same base setup, and averages a smaller gain across five non-reasoning models and four benchmarks.
- Three parallel agent laboratories sharing through AgentRxiv find improvements faster and report a higher best MATH-500 score than the sequential setup, but at substantially higher total cost and with redundant experimentation.
- The paper is explicit about reliability limits: generated research can hallucinate results, reward hack, or fail due to code and LaTeX issues, so reported accuracies were manually checked by humans.

## Tags
`autonomous-research`, `multi-agent`, `scientific-discovery`, `preprint-server`, `agent-memory`, `retrieval`, `prompt-engineering`, `MATH-500`, `Agent-Laboratory`

## Connections
- Extends **Agent Laboratory** by adding a shared archival and retrieval layer so agent-generated papers can become inputs to later agent runs.
- Related to **AI Scientist** and other autonomous discovery systems, but focuses on cumulative knowledge sharing rather than isolated end-to-end paper generation.
- Relevant to multi-agent coordination work such as **CooperBench** and **CAID**: AgentRxiv studies collaboration through asynchronous artifact sharing rather than direct chat, shared-code editing, or branch-and-merge workflows.
- Useful counterpoint for agent scaling discussions because parallel labs improve wall-clock discovery speed while reducing compute efficiency.
