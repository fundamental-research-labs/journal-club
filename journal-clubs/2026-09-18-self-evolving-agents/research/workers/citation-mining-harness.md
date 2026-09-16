# Citation mining: harness and embodied systems

September 16, 2026 cutoff. Discovery: `gpt-5.6-luna`, low reasoning; coordinator audited seed text and bibliography and corrected the initial report. Two full-text seeds: [HarnessDev v1](https://arxiv.org/html/2609.01437v1) (September 1) and [SHAPER v2](https://arxiv.org/html/2608.11350v2) (first August 11; revision September 10). Agent-World was an optional metadata check, not a mined third seed. Budget: up to three seeds and 12 useful edges. No second citation generation was completed: following a reference to its primary page is source resolution.

Queries: `site:arxiv.org/html/2609.01437 HarnessDev introduction related work`; `site:arxiv.org/html/2608.11350 SHAPER related work`; `site:arxiv.org SkillOpt persistent natural-language skill 2026 Yang`; `site:arxiv.org AgentSpec embodied agent scaffolds 2026`. Primary records were checked for new entries. Cited findings remain unverified unless separately screened.

| Seed / exact section and paragraph cue | Cited source | Role attributed by seed authors | Register coverage / access |
| --- | --- | --- | --- |
| HarnessDev §1, opening paragraph after Figure 1, “As agents move” | [Natural-Language Agent Harnesses](https://arxiv.org/abs/2603.25723) | Harness-representation predecessor; Pan et al. | New `2026-natural-language-agent-harnesses`; abstract/metadata |
| HarnessDev §5, “Agent benchmarks and harness development” | [The Meta-Agent Challenge](https://arxiv.org/abs/2606.04455) | Closely related Creation comparator | New `2026-meta-agent-challenge`; abstract/metadata |
| HarnessDev §5, same paragraph, “HarnessOpt-Bench” | [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301) | Closest concurrent Evolution comparator | New `2026-harnessopt-bench`; abstract/metadata |
| HarnessDev §5, same paragraph, “Evo-Bench” | [Evo-Bench](https://arxiv.org/abs/2608.09096v2) | Fixed-runtime, final-revision development benchmark | Existing `2026-evo-bench`; prior record reused |
| HarnessDev §5, “Automated agent design and evolution”, “Self-Harness” | [Self-Harness](https://arxiv.org/abs/2606.09498) | Model-specific edits plus regression testing | New `2026-self-harness`; abstract/metadata |
| HarnessDev §1, paragraph “This evaluation gap” | [Reflexion](https://arxiv.org/abs/2303.11366) | Trace-based behavioral diagnosis predecessor | Existing `2023-reflexion`; prior substantive note |
| SHAPER §1, paragraph “A common approach” | [Open X-Embodiment](https://arxiv.org/abs/2310.08864) | Weight-update/data background, not a demonstrated SHAPER baseline | New background record; abstract/metadata; not selected |
| SHAPER §1, “Train-free embodied adaptation” | [Code as Policies](https://arxiv.org/abs/2209.07753) | Programmable robot-interface predecessor | New background record; abstract/metadata; not selected |
| SHAPER §2, “Self-evolving agents” | [EmbodiSkill](https://arxiv.org/abs/2605.10332) | Skill-only adaptation comparator | New `2026-embodiskill`; abstract/metadata |
| SHAPER §2, “Self-evolving agents” | [SkillOpt](https://arxiv.org/abs/2605.23904) | Fixed-harness skill optimizer | New `2026-skillopt`; subsequently substantively screened |
| SHAPER §2, “Self-evolving agents” | [AutoHarness](https://arxiv.org/abs/2603.03329) | Harness/code-policy synthesis comparator | New `2026-autoharness`; abstract/metadata |
| SHAPER §2, “Self-evolving agents” | [AgentSpec](https://arxiv.org/abs/2606.14674) | Controlled scaffold composition rather than rollout-driven optimization | New `2026-agentspec`; abstract/metadata |

Additional background resolved during QC: SWE-agent appears in HarnessDev §5 “Automated agent design and evolution”; ASPIRE appears in SHAPER §1 and §2, **not** HarnessDev's Lu et al. reference (which is Meta-Agent Challenge). Both are registered with limited reading depth. Agentic Harness Engineering is already covered; the initial worker's Pan attribution was wrong, so that edge was dropped.

The strongest unreviewed follow-ups are HarnessOpt-Bench/Meta-Agent Challenge for development evaluation, and EmbodiSkill/AutoHarness/AgentSpec for embodied comparisons. Stop reason: the stated edge budget was reached. No search-saturation claim; full-text screening of these watchlist items remains conditional on session emphasis. SkillOpt was screened separately. No source text retained by this lane.
