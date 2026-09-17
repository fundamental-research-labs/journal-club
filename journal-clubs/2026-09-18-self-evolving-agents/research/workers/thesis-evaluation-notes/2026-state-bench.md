# STATE-Bench: a benchmark for AI agent memory

- **Canonical:** https://opensource.microsoft.com/blog/2026/05/19/introducing-state-bench-a-benchmark-for-ai-agent-memory/
- **Date/access:** 2026-05-19; first-party article sections on scoring and baseline read 2026-09-16; no local copy retained.

STATE-Bench is memory-agnostic and targets realistic enterprise tasks (lines 125–126). It runs each task five times, reports average completion, uses deterministic final-environment-state scoring for state-mutating tasks, and reports pass^5 reliability (line 145). Microsoft’s GPT-5.1 no-memory baseline completed fewer than half reliably; travel pass^5 was about 30% (line 152).

The benchmark operationalizes the thesis’s future-task criterion: retained state should improve later outcomes and consistency, not merely retrieval scores. The repeated-run design also exposes variance hidden by pass@1. Limitations: vendor baseline, three domains, and LLM judging for procedural/informational tasks; independent replication and judge calibration are needed. The article describes a benchmark and baseline, not evidence that a memory system causes lasting improvement.
