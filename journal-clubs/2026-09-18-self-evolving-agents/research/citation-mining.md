# Recent-paper citation audit

**Historical seven-seed pass.** The later [per-paper prominent-citation map](prominent-citations.md) expands the citation check across reviewed papers, and the [coverage audit](thesis-coverage.md) records its application to the final thesis. The selection discussion below concerns the reading shortlist, not permission to omit a direct comparator from the essay.

**September 16, 2026; cutoff unchanged.** This targeted update mines what recent papers identify as predecessors, baselines, competitors, and limitations. It extends the existing corpus rather than restarting discovery. Three parallel `gpt-5.6-luna` low-reasoning discovery agents read seven seeds across three lanes; two additional `gpt-5.6-luna` medium-reasoning agents screened five consequential omissions. The coordinator checked primary sections/results, bibliographic identities, and selection decisions.

## What changed

The register grew **132→151 records**. **Five new substantive notes** bring the total to **48**; eleven additional sources remain abstract/metadata watchlist entries, and three foundational candidates are retained but excluded from the reading priorities. These are newly discovered older works, not nineteen new publications. Three licensed originals were added; SkillOpt and MLEvolve remain link-only under their arXiv distribution licenses.

| Recent seed | Citation context | Most useful additions | Outcome |
| --- | --- | --- | --- |
| [WikiSkill v1](https://arxiv.org/html/2608.27454v1), Aug 27 | §1, paragraph “A key design question”; §6, Experience-Driven Agent Skill Evolution | [SkillOpt](notes/2026-skillopt.md), [EvoSkill](notes/2026-evoskill.md), [Trace2Skill](notes/2026-trace2skill.md) | Three named comparators were missing as standalone records; now read and retained as reserves |
| [AgentStream v1](https://arxiv.org/html/2608.00155v1) and [SelfMem v1](https://arxiv.org/html/2607.03726v1) | Introduction and memory-related work | Existing A-MEM coverage; MemGPT foundation | Existing lineage confirmed; MemGPT is a limited-depth lead |
| [Dream-RSI v1](https://arxiv.org/html/2609.14858v1), Sep 14 | §1 exploration-policy motivation; §6 discovery and history-reuse paragraphs | [EvoX](notes/2026-evox.md), [MLEvolve](notes/2026-mlevolve.md) | Both screened as meta-search/experience-reuse reserves |
| [MetaRSI v2](https://arxiv.org/html/2609.06396v2), revised Sep 9 | §1 and §2.2 | STOP, SEAL, AFlow | Important predecessors already covered; revision date not treated as new publication |
| [HarnessDev v1](https://arxiv.org/html/2609.01437v1), Sep 1 | §5, Agent benchmarks and harness development | HarnessOpt-Bench, Meta-Agent Challenge; existing Evo-Bench | Missing development-evaluation leads now registered; full methods/results unread |
| [SHAPER v2](https://arxiv.org/html/2608.11350v2), revised Sep 10 | §2, Self-evolving agents | SkillOpt, EmbodiSkill, AutoHarness, AgentSpec | SkillOpt read; embodied alternatives remain watchlist candidates |

The lane reports record **29 selected citation edges**, including already-covered works: [memory/skills](workers/citation-mining-memory.md), [meta-improvement](workers/citation-mining-meta.md), and [harness/embodied](workers/citation-mining-harness.md). They are a bounded sample, not all references from these papers. Primary-source resolution and companion-repository inspection are distinguished from a second backward-citation generation; no second generation was completed. SeaEvo was found by related search and SkillsBench by coordinator keyword search, not inferred to be seed citations.

## Selection decision

**Keep the existing ten.** The five substantive additions strengthen interpretation and baseline coverage without requiring five more talk sections:

- **SkillOpt:** closest reserve for bounded skill-edit optimization. The screener conditionally suggested replacing Shopify; the coordinator retained the production perspective because WikiSkill already anchors skills.
- **Trace2Skill:** strong companion for cross-task/model transfer and failures; avoid assuming every skill variant improves every target.
- **EvoSkill:** useful failure-driven skill-folder predecessor; single-run evidence and an unresolved OfficeQA table/prose discrepancy constrain conclusions.
- **EvoX:** adds online search-strategy evolution as a comparator to Dream-RSI’s replay approach. It does not establish evaluator or model self-improvement.
- **MLEvolve:** adds graph search and retrospective memory in ML engineering. Heterogeneous leaderboard baselines do not isolate its causal advantage.

See [meta screening](workers/citation-screening-meta.md) and [skill screening](workers/citation-screening-skills.md). Rubric ratings are qualitative judgments; the coordinator reconciled lane preferences against the topic-wide shortlist. No citation frequency was treated as independent empirical support.

## Limits and follow-up

The newly indexed harness-evaluation and embodied papers need substantive reading before supporting findings. DeltaEvolve and SkyDiscover were resolved only from Dream-RSI’s bibliography and remain report-level leads; general model-based-RL references were not promoted into the core corpus. Search stopped at the bounded refinement budget, **not citation saturation**. Prior practitioner coverage was preserved; this pass did not reread social posts or talks.

Cheap discovery produced several inaccurate IDs/attributions. Coordinator checks corrected SEAL/STOP links, discarded an unrelated DeltaEvolve URL, and separated HarnessDev’s Meta-Agent Challenge citation from SHAPER’s ASPIRE citation. Primary-source verification remains necessary after discovery.
