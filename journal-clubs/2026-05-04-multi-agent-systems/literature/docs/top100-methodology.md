# Top 100 Multi-Agent Papers: Curation Methodology

## Goal

Curate a list of the 100 most important multi-agent papers. "Agent" primarily refers to LLM-based agents, but the list should include pre-LLM multi-agent reinforcement learning, emergent communication, game-theoretic, and classical multi-agent systems work when it clearly shaped current LLM-agent research.

## Scope

Use four eligibility tiers so the final list does not drift into either "all LLM papers" or "all classical MARL papers."

1. **Core LLM multi-agent systems**: papers where multiple LLM-based agents communicate, debate, delegate, coordinate, specialize, or jointly act in an environment.
2. **Agent-system foundations**: single-agent reasoning, tool-use, memory, and software-agent papers that are repeatedly used as building blocks for multi-agent systems. Keep this tier capped in the final 100.
3. **Pre-LLM multi-agent foundations**: MARL, emergent communication, population training, social dilemmas, agent organizations, and classical MAS papers that introduced durable concepts.
4. **Surveys and benchmarks**: include when they became field-organizing artifacts or are useful for snowball expansion; do not treat survey status alone as sufficient for the final 100.

Exclude generic LLM/model papers unless they directly changed multi-agent system design, evaluation, or deployment.

## Methodology Review

The original citation-graph snowballing plan is the right backbone, but it needs more operational guardrails before it can produce a defensible top 100.

- **Stratify before expanding**: citation graphs will over-reward older MARL and under-reward newer LLM-agent work, while the current local corpus over-represents recent 2025-2026 software-agent papers. Seeds need explicit coverage quotas.
- **Add a recency-aware trend lane**: the top-100 effort is mainly about LLM-based multi-agent agents, so recent 2024-2026 work should be visible even when citations are immature. These papers still need artifacts, evaluations, or clear conceptual novelty; recency is a reason to inspect, not a substitute for quality.
- **Promote by evidence, not only citation count**: citation count, number of seed references, benchmark adoption, framework adoption, and conceptual novelty should all count. "Seed refs" is useful but should not be the sole promotion rule.
- **Separate core from adjacent foundations**: papers like ReAct and SWE-bench are important for LLM agents, but they are not themselves multi-agent papers. Track them as bridge seeds and cap their influence.
- **Normalize identifiers and years**: prefer arXiv IDs when available; use DOI or venue IDs for non-arXiv work. Use publication year when there is a formal venue, otherwise arXiv submission year.
- **Track provenance**: each candidate should record how it entered the pool: cited by seed, cites seed, survey, benchmark, conference award, or manual supplement.

## Seed Construction

Maintain about 100 active seeds for expansion. This is intentionally broader than the final top 100: the seed set is a search instrument, not the final ranking.

A good 100-seed set for this repo should roughly cover:

- 30-40 core LLM multi-agent framework, collaboration, debate, delegation, coordination, and society papers
- 15-25 recent trend papers from 2024-2026 that appear important but have immature citation signals
- 25-35 bridge papers for agent benchmarks, software agents, web/computer-use agents, tool-use, memory, and evaluation methodology
- 10-18 pre-LLM MARL, emergent communication, and population-training anchors
- 2-5 surveys that organize the literature

Temporal guardrails:

- At least 75 papers from 2023 or later
- At least 55 papers from 2024 or later
- At least 25 papers from 2025 or later
- No more than 20 pre-2020 papers unless the goal shifts toward historical MAS/MARL

When adding a seed, require at least one of:

- Introduced a widely reused framework, benchmark, architecture, or experimental setup
- Is cited by multiple current seeds or surveys
- Has become a common baseline or comparison point
- Covers a necessary sub-area gap in the seed set
- Represents a recent high-signal line of work that citation counts have not yet caught up with

Use these seed roles:

- `core`: directly about LLM-based multi-agent systems
- `trend`: recent high-signal work included to track the field's direction
- `bridge`: adjacent agent infrastructure, evaluation, or foundation paper that shapes multi-agent systems
- `anchor`: older MARL, emergent communication, or classical MAS foundation
- `survey`: field-organizing survey used for snowball expansion

Recent `trend` seeds need a lighter impact threshold but not a lighter quality bar. They should have at least one of: released code/data, meaningful benchmark or ablation, notable venue/organization signal, rapid adoption by adjacent work, or a clear new problem formulation.

## Citation-Graph Snowball Sampling

1. **Select seed papers**: start from `docs/seeds.md`.
2. **Expand via precedents**: for each seed, inspect references and add high-quality ancestors to `docs/candidates.md`.
3. **Expand via dependents**: inspect papers that cite each seed via Semantic Scholar, OpenAlex, Google Scholar, or venue pages. Add influential dependents and recent high-signal dependents.
4. **Supplement deliberately**: use surveys, major conference proceedings, AAMAS/MARL benchmarks, and field-maintained awesome lists to catch papers missed by citation graph traversal.
5. **Score candidates**: score each candidate before promotion or final selection.
6. **Promote new seeds sparingly**: promote candidates that either score highly or unlock an under-covered subgraph.
7. **Iterate**: target about 400 candidates before selecting the final 100.

## Scoring Rubric

Score each paper on a 0-100 scale:

- **Impact (30)**: citations, benchmark adoption, framework adoption, or clear downstream influence
- **Novelty (25)**: introduced a paradigm, architecture, evaluation setting, or conceptual lens
- **Breadth (20)**: relevance across multiple multi-agent sub-areas
- **Evidence quality (15)**: methodological rigor, reproducibility, artifacts, and robustness of claims
- **Recency signal (10)**: community attention for recent work whose citation counts are immature

For `trend` papers, recency can justify seed inclusion but should not justify final top-100 inclusion by itself. Before final promotion, require an evidence-quality score of at least 8/15 unless the paper is explicitly marked as a speculative trend pick.

Suggested thresholds:

- `seed`: 70+ or needed to cover a major sub-area gap
- `candidate`: 50+ or credible but not yet reviewed
- `top100`: 75+ after final comparative review
- `cut`: reviewed and out of scope, weak evidence, or superseded

## Trial Run: Seed Expansion to 100

On 2026-05-04, the seed set was expanded from 50 to 100 papers after reviewing the earlier methodology and adding an explicit recent-trend lane. The expansion deliberately favors 2024-2026 LLM-agent work while keeping older MARL/emergent-communication papers as anchors.

The expansion favored:

- Canonical LLM multi-agent systems: AutoGen, CAMEL, MetaGPT, ChatDev, AgentVerse, MAD, ChatEval, DyLAN, AI co-scientist, Mixture-of-Agents, Magentic-One, AgentScope
- Recent coordination and orchestration trends: evolving orchestration, decentralized coordination, topological reasoning benchmarks, learned collaboration, test-time multi-agent scaling
- Agent infrastructure and evaluation bridge papers: OpenHands, ReAct, SWE-agent, SWE-bench, WebArena, OSWorld, WorkArena, BrowserGym, AndroidWorld, TheAgentCompany, tau-bench
- Recent scientific/software-agent trend papers: AI Scientist, Agent Laboratory, AgentRxiv, Curie, MLGym, PaperBench, SWE-RL, SWE-smith, Multi-SWE-bench
- Pre-LLM anchors: RIAL/DIAL, CommNet, emergent language, MADDPG, COMA, QMIX, VDN, MAPPO, OpenAI Five, AlphaStar, SMAC
- Surveys for expansion coverage: LLM-based multi-agent systems and emergent communication

Current `docs/seeds.md` balance:

- 33 core LLM multi-agent papers
- 18 recent trend papers
- 32 bridge papers
- 15 historical anchors
- 2 surveys

Temporal balance:

- 83 papers from 2023-2026
- 63 papers from 2024-2026
- 38 papers from 2025-2026
- 13 papers from before 2020

Known follow-up work:

- Add provenance columns to `docs/candidates.md`
- Fill missing IDs for remaining candidates
- Run reference extraction over all 100 seeds
- Run dependent-paper collection for the top 25 seeds by sub-area centrality
- Split `docs/top100.md` into final selected papers versus watchlist/trend candidates once scoring is complete

## Tracking

- **Seed papers**: `docs/seeds.md`
- **Candidate list (~400)**: `docs/candidates.md`
- **Field map (1000)**: `docs/field-map-1000.md`, with machine-readable rows in `docs/field-map-1000.csv` and `docs/field-map-1000.yaml`
- **Final 100**: `docs/top100.md`

## Sub-Areas to Cover

- Multi-agent communication and language
- Multi-agent coordination and planning
- Emergent social behavior
- Society of agents / agent organizations
- Multi-agent debate and reasoning
- Tool use and environment interaction
- Multi-agent reinforcement learning
- Game-theoretic multi-agent systems
- Agent evaluation and benchmarks
- Scalability and population dynamics
- Software engineering and long-horizon agent work
- Scientific discovery and research agents
