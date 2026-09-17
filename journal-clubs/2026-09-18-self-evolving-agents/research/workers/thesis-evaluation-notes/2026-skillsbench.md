# SUPERSEDED — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

Coordinator instruction: do not use this older 84-task account; current v4/v1.1 numbers are being verified separately.

- **Canonical:** https://www.skillsbench.ai/skillsbench.pdf
- **Date/access:** preprint 2026-02-13; full 34-page PDF read 2026-09-16; no local copy retained.

SkillsBench evaluates 84 tasks across 11 domains under no-Skill, curated-Skill, and self-generated-Skill conditions with deterministic verifiers and 7,308 trajectories (abstract; §§2–3, pp. 1–4). It uses five trials per task, container isolation, oracle solutions, leakage audits, and programmatic assertions (§§2.2–3.5, pp. 2–5). Curated Skills raise mean pass rate 24.3%→40.6% (+16.2 percentage points across seven model-harness configurations); self-generated Skills average 21.0%, versus 21.5% with no Skills (Table 3, p. 5). Self-generated performance is negative for Opus 4.5 and GPT-5.2 (Table 3).

This is direct evidence for the thesis’s fixed-expertise counterfactual: externally curated procedural knowledge helps, while agents prompted to author the knowledge they need do not improve on average. It narrows any positive claim to iterative, feedback-driven evolution. Strengths include deterministic verification, multiple models/harnesses, domain breadth, and leakage review. Limitations: curated Skills receive human authoring effort; self-generation is one-shot rather than longitudinal; Gemini lacks the self-generated condition; and five trials/task remain modest. It does not refute continual learning, but sets a strong static baseline.
