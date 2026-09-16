# Notes

## Why It Matters
SWE-RL is a concrete example of using real software evolution, not synthetic coding puzzles alone, to train an open model for repository-level issue repair. Its main contribution is the pragmatic reward design: use the merged PR patch as an oracle and reward partial patch similarity, making RL feasible without executing every training instance.

## When To Cite
Cite this paper for RL-based training of software engineering LLMs, SWE-bench Verified open-model results, patch-similarity rewards, PR-derived software evolution corpora, Agentless-style issue-resolution pipelines, and evidence that issue-repair RL can transfer to broader reasoning benchmarks.

## Key Terms
SWE-RL; Llama3-SWE-RL-70B; software evolution data; pull request seeds; oracle patch; search/replace edits; `difflib.SequenceMatcher`; GRPO; Agentless Mini; SWE-bench Verified; reproduction tests; regression tests; reranking; continuous reward; discrete reward; out-of-domain reasoning.
