# Cross-batch shortlist challenge

Reviewed September 16, 2026 against all lane screening reports and substantive notes available at handoff. The target is a topic-wide priority reading list for a technically literate 45-minute journal club, not ten talk sections and not a leaderboard. Families are counted once even when a companion paper supplies a necessary qualification.

## Recommendation

Make **one swap**:

> **Replace Dream-RSI with the R-Zero / Absolute Zero self-play family, led by R-Zero and with Absolute Zero as the companion.**

Do not make a second swap. The other proposed omissions are useful reserves or companions, but replacing another family would reduce evidence quality, independence, or mechanism coverage more than it would help.

### Why this swap improves the set

The provisional list already contains **Hyperagents**, which directly asks whether the process generating agent changes can itself improve. Dream-RSI is a distinct implementation—replay-based exploration-policy editing around a frozen coding agent—but fills the same high-level “improve the improver” slot. Both belong in the analysis, yet two of ten priority families overweight meta-improvement relative to the field.

R-Zero adds a missing mechanism: a Challenger and Solver autonomously create and learn from a curriculum through weight updates. It also supplies unusually useful negative evidence. Its GPT-4o-audited pseudo-label accuracy falls **79%→69%→63%** across steps 15/30/45, and the two-model system peaks at **49.12** after step 45 then falls to **46.52** at step 60 (Table 5 and Appendix Table 6). This gives the shortlist a concrete case where self-generated training initially helps and then degrades. Absolute Zero is the positive companion: executable self-play improves the reported Qwen2.5-Coder-7B aggregate **40.2→50.4**, while still showing task-level regressions and incomplete compute accounting. Treat them as one evidence family rather than two slots.

The swap is based on coverage and evidence, not publication date. Dream-RSI is newer but has no independent-run intervals or complete cost ledger; replay can overfit a finite history pool, and its clearest held-out transfer concerns the discovered Lasso solver rather than the exploration controller across unseen domains. Keep it as a close alternative and pair its mechanism diagram with Hyperagents when discussing meta-level improvement. The within-model **550→317 discovery-call** comparison and individual Lasso regressions remain worth mentioning.

## Resulting ten-family set and role

| Family | Primary role in the evidence base | Why it earns a slot / qualification |
| --- | --- | --- |
| Rethinking harness-evolution evaluation | Budget-matched negative/control evidence | Directly asks whether evolution beats spending the same five rollouts on solutions; held-out 45/10/34 split finds 68.3 versus 67.7. Two runs and a 34-task test limit precision, but no other selected source supplies this counterfactual as cleanly. |
| WikiSkill | Controlled positive persistent-knowledge mechanism | Held-out train/validation/test splits, three evolution runs, five models, and an explicit OfficeQA regression. It grounds “experience changes retained state” with inspectable wiki and skill layers. |
| GEPA | Prompt/context evolution versus weight-space RL | Six tasks with train/validation/test splits and a clear Pareto reflective-search mechanism. Its AIME regression, unmatched total compute, and the VISTA defective-seed challenge must travel with it. |
| SEAL | Direct learned self-edit for model weights | The clearest source in the set where a model writes synthetic data and optimization instructions that cause parameter updates. Held-out tasks/passages and forgetting tests strengthen it; narrow selected ARC tasks and two outer rounds constrain the claim. |
| Hyperagents | Improving the modification process | Five-run experiments and explicit task/meta-agent code sharing make it the best selected representative for improving the improver. Its math transfer endpoint is nonsignificant and the five-run CIs are run-level bootstraps; it supports finite meta-improvement, not indefinite compounding. |
| AgentStream | Conditional performance under task order and mixing | Six benchmarks × 50 tasks, three order seeds, five methods, and three models show positive and negative cells. It prevents every positive memory/context result from being read as order-independent. |
| HarnessDev | Harness creation plus post-freeze generalization | Creation covers 2,207 instances; evolution separates 189 feedback tasks from 630 held-out SWE-Pro tasks across nine lineages. Direction agreement is only 34/64 adjacent switches, which makes it both positive mechanism evidence and a stability warning. |
| FinEvo-Bench | Matched persistence control in professional workflows | Three paired stateful/reset permutations, 120 open-ended financial tasks, expert judge calibration, compliance outcomes, and cost accounting. It demonstrates learning recurring professional procedures, not open-world financial competence. |
| Shopify Sidekick | Production loop and deployment economics | Only selected practitioner family spanning harness search, repaired data, SFT, GRPO, daily weight updates, and prompt compression at reported production scale. The absence of public quality tables, ablations, and raw traces must remain visible; select it for systems coverage, not causal efficacy. |
| R-Zero / Absolute Zero | Autonomous self-generated curriculum and collapse | Adds the otherwise missing self-play/weight-training branch, with both positive multi-benchmark changes and direct late-stage deterioration. Lead with R-Zero for role separation and collapse; use AZR as the positive executable-reward companion. Internal aggregate inconsistencies, missing run uncertainty, and incomplete compute keep evidence at medium strength. |

## Redundancy audit

- **Hyperagents and Dream-RSI:** meaningful mechanism difference, same shortlist role. Hyperagents has repeated runs and directly shares editable code between task and meta agents; retain it. Dream-RSI remains the first alternate for a session specifically about meta-policy learning or offline replay.
- **Harness critique and HarnessDev:** not redundant. One supplies the counterfactual budget/control argument; the other shows creation/evolution across multiple lineages with a separate held-out set. Their tension is a feature.
- **WikiSkill, GEPA, and AgentStream:** three distinct roles. WikiSkill tests a durable knowledge/skill representation, GEPA searches prompts with rich textual feedback, and AgentStream stress-tests several retained-state methods under order and mixing. AgentStream should qualify the first two rather than replace them.
- **FinEvo-Bench and Shopify Sidekick:** both use professional workflows, but their evidence functions differ. FinEvo supplies a paired controlled benchmark; Shopify supplies a production architecture and economics case with weak public efficacy evidence.
- **SEAL and R-Zero/AZR:** both change weights, but SEAL learns explicit task-local update programs from external context, while R-Zero/AZR generate their own curricula. Keeping both prevents “weight evolution” from collapsing into one mechanism.

## Omission assessment

### Strong reserves, no additional swap

**HGM.** HGM is the strongest resource-accounted DGM continuation: at 800 evaluations it reaches 56.7/30.5 versus DGM 53.3/27.1 on SWE-Verified-60/Polyglot while using 517/347 versus 1,231/2,385 allocated CPU-hours; it also gains 34.8→40.1 on 207 nonoverlapping SWE-Lite tasks. It is excellent background for the DGM lineage, but Hyperagents already represents that lineage's more central session question—whether the modification process improves—and HarnessDev supplies independent harness evidence. Promote HGM if the talk shifts toward search policy or fitness proxies.

**EvoHarnessBench.** Its 17 staged streams, 802 unique tasks, adaptation/evaluation separation, and three-run population SDs add a valuable *interface-change* axis. AgentStream already occupies the broader streaming-evaluation slot with task-order/model/method interactions, while HarnessDev covers autonomous harness changes. Use EvoHarnessBench as the first evaluation reserve or as a companion example that adding tools can harm old tasks; it does not displace either selected source.

**Library Drift / Ratchet.** This is the best repeated lifecycle failure example: three seeds and harsh retirement turn a default +0.328 late-minus-early gain into −0.019. Its 40 selected evaluation tasks, one model, repeated exposure, and unmatched costs make it narrower than AgentStream. Use it as a concrete retirement-policy figure within the memory section.

**ACE.** ACE is a strong central context-engineering paper with official splits and detailed token/latency accounting. It is omitted only because GEPA represents context search, WikiSkill represents persistent structured experience, and AgentStream independently includes ACE and shows its Claude Opus 4.7 interleaved score can fall below vanilla (61.9 versus 63.9). If the session narrows to online playbooks, ACE should replace GEPA rather than add an eleventh context family.

**Escher-Loop.** The strongest alternate meta-optimization experiment: matched 10M equivalent-token budgets and three-run ablations show a clear Kissing Number advantage, but Circle Packing is tied/slightly favors a static pool and all tests reuse three fixed geometry instances. It lacks unseen-task transfer. It is more redundant with Hyperagents than R-Zero/AZR and remains a reserve.

**Ground Truth First.** Methodologically impressive longitudinal memory evaluation, with full-history controls, provenance, re-judging, and cluster-aware tests. Its central tenure result uses six synthetic users; the primary exact sign-flip result is p=.063, and the artifact package was pending. The list already contains the general harness-evaluation critique, WikiSkill, and AgentStream, so GTF would overallocate scarce slots to evaluation/memory. Use it if memory evaluation becomes the session's thesis.

**Reef.** Better public infrastructure evidence than Shopify in some respects: Apache-2.0 code, inference receipts, delayed-feedback attribution, candidate versioning, and recipe outputs. Its measured meta-harness result is weak for efficacy—a fresh same-task comparison of 22/60 versus 21/60, not a held-out task test. Shopify covers more of the production learning loop, weight updates, scale, and serving economics. Keep Reef as Shopify's implementation companion.

**NVIDIA NemoClaw memory.** The 186-question deterministic benchmark, public corpus/answers/verdicts, same base model, and explicit regressions make this the strongest practitioner memory artifact. The evaluated self-model adapter/memory is missing, only one synthetic corpus and run are reported, and compute is radically different and declared incomparable. WikiSkill supplies stronger controlled memory/skill evidence; Shopify preserves broader practitioner coverage. NemoClaw is the first replacement if the organizer values artifact inspectability over a full production-loop case.

### Family selected by the recommended swap

**AZR/R-Zero.** Select as one family, led by R-Zero. Do not allocate separate slots. R-Zero supplies the more important self-correction to the field's narrative—pseudo-label decay and late collapse—while AZR supplies broader positive executable-reward evidence. The companion self-play-dynamics paper can qualify capacity/entropy claims without becoming an eleventh family.

## Final judgment

The resulting list has a defensible balance: three external-state mechanisms (WikiSkill, GEPA, HarnessDev), two weight-update mechanisms (SEAL, R-Zero/AZR), one meta-improvement family (Hyperagents), three evaluation/deployment stressors with different roles (harness critique, AgentStream, FinEvo-Bench), and one production systems account (Shopify). It includes positive results, regressions, late-stage collapse, budget controls, held-out tests, professional tasks, and deployment constraints without letting the newest recursive label dominate selection.
