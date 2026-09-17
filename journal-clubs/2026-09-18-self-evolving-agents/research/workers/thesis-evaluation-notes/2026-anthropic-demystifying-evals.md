# Anthropic: Demystifying evals for AI agents

- **Canonical:** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **Date/access:** 2026-01-09; full first-party HTML read 2026-09-16; no local copy retained.

Anthropic separates a trial transcript, the environment outcome, and the evaluation harness (definitions, lines 34–36). The article’s CORE-Bench example reports an initial 42% for Opus 4.5 and 95% after fixing rigid numeric grading, ambiguous task specifications, and irreproducible stochastic tasks (line 263). The change is an evaluation repair, not an agent capability update.

This is a consequential challenge to self-evolution claims: if an evolving agent optimizes a brittle judge or harness, score improvements can reflect evaluator changes. Strengths are concrete deployment experience and explicit outcome/process distinction. Limitations are vendor authorship, one benchmark example, and no independent human-agreement estimate in the inspected passage. Use as methodological evidence and require environment-state checks, randomized ordering, evaluator versioning, and audit trails.
