# Notes

## Why It Matters
SWE-smith is important because it treats SWE-agent progress as a data-infrastructure problem. Instead of waiting for scarce real issues with clean tests and buildable historical environments, it creates many test-validated regressions from current repositories and turns solved runs into training trajectories. The paper is also a useful reference point for open-weight SWE agents: its strongest model is trained with a relatively small number of successful trajectories but reaches a strong SWE-bench Verified result for a single-attempt open-weight setup.

## When To Cite
Cite when discussing scalable training data for coding agents, synthetic repository-level bugs, execution-based validation, SWE-bench-style task generation, open-weight SWE-agent fine-tuning, or the storage and human-labor bottlenecks of task-first benchmark construction. Also cite for ablations on bug-generation strategy, generated issue text, repository diversity, repository specialization, and failure modes of a fine-tuned SWE-agent model.

## Key Terms
SWE-smith; SWE-agent-LM-32B; software engineering agents; execution environment; synthetic bug; Fail-to-Pass test; LM Modify; LM Rewrite; Procedural Modification; Combine Bugs; PR Mirror; rejection-sampling fine-tuning; expert trajectory; SWE-agent; SWE-bench Verified; Qwen 2.5 Coder Instruct; Claude 3.7 Sonnet; repository specialization; repetitive actions; localization failure.
