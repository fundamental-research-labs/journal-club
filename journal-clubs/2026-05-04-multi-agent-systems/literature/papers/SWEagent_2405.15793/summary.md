# SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press
**arXiv:** 2405.15793
**Venue:** NeurIPS 2024
**Date:** November 2024

## Problem
Language-model agents are increasingly used in digital environments, but standard human-oriented interfaces such as the Linux shell are brittle for repository-scale software engineering. Agents must localize relevant code, inspect files without overflowing context, make precise edits, run tests, and recover from mistakes; raw command-line tools often make these subtasks verbose, silent, or error-prone.

## Method
The paper introduces the agent-computer interface (ACI): the commands available to an LM agent and the format of environment feedback returned after each action. SWE-agent is an LM plus an ACI built on top of a Linux shell. Its interface includes summarized repository/file search commands, a line-numbered file viewer, a line-range `edit` command with immediate post-edit feedback, linting guardrails that reject selected syntax-breaking edits, file creation/submission commands, ReAct-style thought/action turns, concise response templates, and history collapsing that keeps recent observations while reducing stale context. The evaluation uses GPT-4 Turbo and Claude 3 Opus on SWE-bench full/Lite and HumanEvalFix, with comparisons to retrieval-augmented generation and a Shell-only interactive agent.

## Key Findings
- On the full SWE-bench test set, SWE-agent with GPT-4 Turbo resolves 12.47% of tasks (286/2,294), compared with 1.31% for the GPT-4 Turbo RAG baseline reported in Table 1.
- On SWE-bench Lite, SWE-agent with GPT-4 Turbo resolves 18.00% of tasks, compared with 11.00% for the Shell-only GPT-4 Turbo agent and 2.67% for GPT-4 Turbo RAG.
- The same ACI is usable with another long-context model: SWE-agent with Claude 3 Opus resolves 10.46% on full SWE-bench and 13.00% on SWE-bench Lite.
- Interface ablations show large drops from removing the edit command, removing linting, using iterative search, shrinking/expanding the file viewer too far, or keeping full history instead of recent observations.
- On HumanEvalFix, Table 2 reports high pass@1 for SWE-agent with GPT-4 Turbo across Python, JavaScript, and Java, supporting the claim that the editing interface helps beyond SWE-bench.
- Behavior analysis finds recurring trajectories: agents tend to start with reproduction and/or localization, then move into edit-and-execute loops; unresolved runs are often incorrect or overly specific implementations, with cascading failed edits also common.

## Tags
`software-engineering-agents`, `agent-computer-interface`, `SWE-bench`, `repository-repair`, `tool-use`, `coding-agents`, `interface-ablation`, `execution-feedback`

## Connections
- Complements **SWE-bench** by providing an interactive agent system rather than a non-interactive patch-generation baseline.
- Useful background for **SWEbenchGoesLive**, which studies live/contamination-resistant variants of the SWE-bench evaluation setting.
- A single-agent interface-design counterpoint to multi-agent coding work such as **CooperBench** and **CAID**: before adding coordination, the base agent-computer interface strongly affects performance.
- Related to broader computer-use benchmarks such as **WorkArena**, but focused on repository-level search, editing, and test execution.
