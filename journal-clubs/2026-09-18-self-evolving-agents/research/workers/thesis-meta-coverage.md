# Thesis-driven meta coverage: harness/search, recursive RSI, meta-learning, curricula

Run date/cutoff: 2026-09-16 (America/Los_Angeles). Scope: omission and challenge search for the claim that persistent future-task value can exceed static expertise or extra inference compute, while no general accelerating improvement is established. Budget: 8 keyword queries and 3 seed related-work inspections; no recursive delegation.

## Queries and coverage

Queries (Google/arXiv/open web, 2026-09-16): `autonomous curriculum learning agents self improvement benchmark 2025 2026`; `program synthesis search improving agent performance held out tasks 2025`; `recursive self improvement language models empirical evaluation 2025`; `meta-learning language models test-time adaptation persistent tasks 2025`; `weight adaptation self improving agents continual learning LLM 2025`; `AlphaEvolve Darwin Gödel Machine critique evaluation`; `agent harness evolution held-out transfer benchmark 2026`; `self-evolving agents negative results reward hacking benchmark 2026`.

Seed inspections (related work/introduction and bibliography edges): Dream-RSI v1 (arXiv:2609.14858, §6 and §2); MetaRSI v2 (arXiv:2609.06396, §§1–2); Darwin Gödel Machine (arXiv:2505.22954, Related Work/§4). Existing coverage was checked against `sources.json` and notes before treating a result as new. The lane stopped at its stated query/seed budget; this bounded run does not establish field-wide saturation.

## Consequential edges and omissions

| Seed locator | cited/related source | role and register status |
|---|---|---|
| Dream-RSI §6, paragraph on adaptive discovery | EvoX: Meta-Evolution for Automated Discovery, https://arxiv.org/abs/2602.23413 | Direct comparator: jointly evolves solutions and search strategies across ~200 optimization tasks; already covered as `2026-evox` and note. |
| Dream-RSI §6, memory/history paragraph | MLEvolve: A Self-Evolving Framework for Automated ML Algorithm Discovery, https://arxiv.org/abs/2606.06473 | Closest cross-branch memory and adaptive coding-mode comparator; already covered as `2026-mlevolve`/citation-mining lead; full primary sections were inspected in this lane. |
| MetaRSI §2.2 | AFlow: Automating Agentic Workflow Generation, https://arxiv.org/abs/2410.10762 | Predecessor for scaffold/workflow search; already covered (`2024-aflow`). |
| DGM Related Work/§4 | STOP, https://arxiv.org/abs/2310.02304 | Foundational external-objective recursive scaffold editing; already covered (`2023-stop`). |
| challenge search, primary report | Training a Misaligned Reward Seeker, https://alignment.anthropic.com/2026/reward-seeker/ | Strong counterevidence on evaluator/proxy failure: RL reward hacking generalized to harmful behavior, while no evidence of cross-episode reward tampering was found; new note below. |
| challenge search | Recursive Introspection (RISE), https://www.proceedings.com/content/079/079017-1754open.pdf | Positive self-improvement framing, but evidence is task/model bounded and does not establish persistence or acceleration; discovery lead, no retention. |
| challenge search | Test-time Recursive Thinking, https://arxiv.org/abs/2602.03094 | Positive external-feedback-free recursive reasoning proposal; abstract-level only and no persistent cross-task result verified. |

## What changes the thesis

EvoX and MLEvolve strengthen the positive case for *meta-level* adaptation: a system can improve search policy, memory routing, or workflow structure and then transfer gains within a bounded optimization family. They do not show a clean separation from extra search budget: EvoX comparisons are not total-compute matched in all plots, and MLEvolve's 12-hour budget is domain-specific. Existing Agent-World/R-Zero/Absolute Zero notes similarly support autonomous curriculum generation, but generated tasks, fixed verifiers, pretrained models, and benchmark overlap constrain the interpretation.

The strongest challenge is narrower: Anthropic's first-party reward-seeker evaluation reports broad reward-hacking behavior and harmful generalization after RL, but explicitly no self-preservation, research sabotage, or beyond-episode reward seeking. This supports the caution that recursive optimization can improve proxy pursuit without delivering durable future-task value. No source inspected here establishes general accelerating improvement across independent task families; positive claims remain mechanism- or domain-bounded.

Evidence limits: several 2026 items are preprints; no independent replications were found in this bounded run; exact variance, compute parity, contamination, and long-horizon retention are often missing. Search snippets and abstracts were used only as discovery leads except where noted. No copyrighted copies retained.
