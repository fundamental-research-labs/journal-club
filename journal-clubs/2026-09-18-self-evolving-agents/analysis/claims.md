# Claim ledger

September 16, 2026. Confidence is an analytic judgment about the scoped claim, not a statistical probability. “Reported” does not mean reproduced. Source keys resolve in the [register](../research/sources.md); methods, denominators, and review depths remain in its linked notes. Presentation mapping belongs in the storyboard when slides are developed.

## C001

- **Claim / type:** For this session, self-evolution means experience changes retained state that affects subsequent behavior; “self” identifies which update decisions the agent controls. Operational definition / analyst synthesis.
- **Support:** `2023-reflexion`, [Algorithm 1](https://arxiv.org/abs/2303.11366v4); `2023-voyager`, [§2](https://arxiv.org/abs/2305.16291); `2025-self-adapting-language-models`, [§3](https://arxiv.org/abs/2506.10943v2).
- **Challenge / comparability:** Authors use different boundaries, including within-task retries. Persistent state alone does not demonstrate improvement; these distinct systems are examples, not replications.
- **Confidence / status:** High for usefulness as an explicit convention; usable with that label.
- **Change criterion:** Revise if the session includes systems without retained changes; distinguish their task-local search.

## C002

- **Claim / type:** The reviewed 2023–2026 literature broadens the editable components and increasingly tests reuse through stream, reset, and held-out controls. Dated synthesis, not a publication-count or adoption estimate.
- **Support:** `2023-stop`, [October 3, 2023, Algorithm 1](https://arxiv.org/abs/2310.02304v3); `2025-gepa`, [July 25, 2025, Algorithm 1](https://arxiv.org/abs/2507.19457v2); `2025-r-zero`, [August 7, 2025, §2](https://arxiv.org/abs/2508.05004v4); `hyperagents`, [March 19, 2026, §3](https://arxiv.org/abs/2603.19461v1); `agentstream`, [July 31, 2026, setup](https://arxiv.org/html/2608.00155v1); `harnessdev`, [September 1, 2026, §4.3](https://arxiv.org/abs/2609.01437v1). Dates from the register; revisions differ.
- **Challenge / comparability:** STOP already changes improver code in 2023. Selection of recent papers can create a false historical progression; these studies do not share a capability scale. Related DGM/Hyperagents methods are not independent confirmations.
- **Confidence / status:** Moderate; usable as a trend in this corpus. **Change criterion:** Broader dated coverage could weaken the claimed shift in emphasis.

## C003

- **Claim / type:** WikiSkill reports useful held-out skill gains under its benchmark protocol, with exceptions. Reported finding.
- **Support:** `wikiskill`, [v1 Table 1, Appendix B Table 6, Appendix C](https://arxiv.org/abs/2608.27454v1): Qwen-3.5-9B macro accuracy 29.9→47.4; three evolution runs. Test sizes across five benchmarks: 124/85/280/172/134. Qwen-3.5-4B OfficeQA declines 30.2→28.5.
- **Challenge / comparability:** Five benchmarks are equally weighted; small validation sets, injected skills, and OfficeQA reference-page assistance limit deployment extrapolation. No numerical CI in Table 1. Comparisons and ablations belong to one evidence family; extra computation is not fully normalized.
- **Confidence / status:** Moderate; usable within protocol. **Change criterion:** Matched-cost replication with realistic retrieval or new domains could narrow the gain.

## C004

- **Claim / type:** A learned policy for generating weight-update data improves SEAL's single-passage adaptation, but continued editing still forgets. Reported finding.
- **Support:** `2025-self-adapting-language-models`, [v2 Table 2, §5/Figure 6, Appendix B](https://arxiv.org/abs/2506.10943v2): Qwen2.5-7B 47.0% with SEAL versus 39.7% with untrained synthetic data; 974 questions from 200 held-out passages. Later updates degrade prior knowledge.
- **Challenge / comparability:** Stronger-model synthetic data scores 46.3% here and exceeds SEAL in the larger incorporation conditions. Questions share passages; final-score repeated-run uncertainty is absent. This is one study, separate from skill benchmarks.
- **Confidence / status:** Moderate; usable. **Change criterion:** Independent repeated runs and retention-aware evaluation could change the advantage.

## C005

- **Claim / type:** Retained experience helps recurring FinEvo procedures relative to paired resets; a strong static skill explains much of one scaffold's improvement. Reported finding.
- **Support:** `2026-finevo-bench`, [v1 §§4.1–4.3, Tables 3/5](https://arxiv.org/html/2608.06144v1): 120 tasks, 20 scenes, three order permutations; common Qwen3.7-Max backbone. Four scaffold gains: 9.33–19.37 rubric points. Claude Code carrier comparison: reset 71.58, static expert skill 86.67, full evolution 89.47.
- **Challenge / comparability:** Main effects lack across-run intervals. Repeated tasks/orders are not 360 independent task types. Scoring and feedback share rubrics; one expert calibrates 120 outputs. Skill ablation is one scaffold, and updating adds computation. Rubric points are not accuracy percentage points.
- **Confidence / status:** Moderate; usable for recurring procedures, not open-world transfer. **Change criterion:** Novel procedures, independent judging, or cost-matched static controls could reduce the advantage.

## C006

- **Claim / type:** The tested harness evolution does not beat parallel sampling at equal rollout count; its separate held-out gain is small. Reported finding.
- **Support:** `harness-evolution-evaluation`, [v2 §§4.1–4.4, Tables 1–3](https://arxiv.org/abs/2607.12227v2): 89 Terminal-Bench 2.1 tasks, five rollouts, two runs; reported no-test averages 67.4 evolution versus 72.3 sampling. Separate 45/10/34 split: 68.3 evolved versus 67.7 initial.
- **Challenge / comparability:** Rollouts do not match tokens, dollars, or future amortization. Small held-out set; no table CIs. One implementation cannot establish that all harness evolution fails. Retain the printed average despite rounded-cell arithmetic differences.
- **Confidence / status:** Moderate; usable. **Change criterion:** A stronger evolved harness with repeated, independent transfer and lifetime-cost superiority would narrow the critique.

## C007

- **Claim / type:** AgentStream's tested retained-state methods have modest aggregate gains and substantial configuration-dependent regressions. Reported finding plus documented arithmetic reconstruction.
- **Support:** `agentstream`, [v1 Tables 2 and 11–13](https://arxiv.org/html/2608.00155v1), [existing audit](../research/check-agentstream-aggregates.py): six benchmarks × 50 tasks, three models, five methods, three order seeds. Isolated/sequential/interleaved mean gains: +1.37/+0.75/+0.90 pp. Interleaved has 28 positive and 17 negative cells.
- **Challenge / comparability:** The 45 cells share tasks; they are not independent datasets. The reported ± reproduces sample SD of three seed-level means, not a CI. Native benchmark metrics differ. FinEvo's larger gains use different tasks and rubric feedback, so they are not a direct contradiction or ranking.
- **Confidence / status:** Moderate for generality; usable descriptive finding. **Change criterion:** Diverse independent streams and controlled retrieval/feedback ablations could revise the pattern.

## C008

- **Claim / type:** Additional self-generated training can reverse an earlier gain; label degradation alone is not an established causal explanation. Reported finding / causal limitation.
- **Support:** `2025-r-zero`, [v4 Appendix D Table 6, Appendix E](https://arxiv.org/abs/2508.05004v4): two-model math score 49.12 at step 45 falls to 46.52 at step 60; model-size-specific collapse occurs at different pseudo-label accuracies.
- **Challenge / comparability:** Missing training-run intervals and full compute ledger; judge-based label audits; curriculum difficulty and synthetic-data diversity also change. This is a bounded counterexample to monotonicity, not the typical collapse rate. Disputed main-table/prose aggregates are excluded.
- **Confidence / status:** Moderate; usable for the observed decline, causal mechanism unresolved. **Change criterion:** Replicated fixed-label-quality and fixed-difficulty interventions could identify causes or show instability was run-specific.

## C009

- **Claim / type:** Explicit meta-improvement has promising finite results, but these studies do not demonstrate sustained domain-general acceleration. Evidence synthesis.
- **Support:** `hyperagents`, [v1 §§3/5.2–5.3, Figure 4](https://arxiv.org/abs/2603.19461v1): transferred/fresh math scores 0.640/0.610, authors report p>0.05, five runs. `2026-dream-rsi`, [v1 §§3–4, Figure 3](https://arxiv.org/html/2609.14858v1): same-model Lasso discovery 550→317 calls, downstream mean runtime 3,587.1→2,931.0 ms across six held-out datasets.
- **Challenge / comparability:** These positive mechanisms challenge blanket skepticism. However, Hyperagents retains outer controls; Dream-RSI omits complete meta-optimization costs/repeat uncertainty and replay covers recorded branches. Its six datasets evaluate discovered solvers, not six independent controller-training runs. Distinct systems, not replications.
- **Confidence / status:** Moderate; usable with finite scope. **Change criterion:** Repeated cross-domain transfer of the improver at fixed lifetime cost, with increasing improvement efficiency across cycles, would strengthen the acceleration case.

## C010

- **Claim / type:** Shopify describes an integrated production learning pipeline; its article does not isolate the causal benefit of continual learning. First-party reported architecture / evidence limitation.
- **Support:** `2026-shopify-sidekick`, [August 5 article, trajectory repair, training, and GraphQL sections](https://shopify.engineering/sidekicks-continual-learning-loop): harness search, repaired data, SFT/GRPO, daily weight updates, serving compression.
- **Challenge / comparability:** No public ablation, longitudinal quality table, identified frontier baseline, or full cost ledger. One company account is an existence signal, not industry adoption evidence. Shared judge use across stages permits correlated blind spots; it does not prove gaming.
- **Confidence / status:** Moderate for the described design; usable with company attribution. Efficacy superiority remains provisional. **Change criterion:** Released longitudinal evaluations and independent judging could strengthen efficacy claims.

## C011

- **Claim / type:** The corpus supports useful bounded learning loops; the practical case for self-evolution depends on retained benefit, transfer, regressions, and cost. Central analyst inference.
- **Support:** C003–C010, with primary links and locators above. Positive matched controls and negative stress tests jointly explain the preferred thesis.
- **Challenge / comparability:** Extra compute and task specialization may explain much of the value; stronger future meta-learning could change the picture. No pooled effect or estimate of which bottleneck dominates is defensible. Study families and shared benchmarks prevent treating every paper as independent confirmation.
- **Confidence / status:** Moderate; usable as interpretation. **Change criterion:** Broad, replicated, economical improver transfer would strengthen the recursive view; disappearance of gains under strong controls would strengthen the specialization view.

## C012

- **Claim / type:** Compare evolution against static expertise, reset state plus extra inference, and a fixed improver under a complete lifetime budget, using independent evaluation and retention checks. Analyst recommendation.
- **Support:** C004–C010; especially FinEvo Table 5, harness critique Tables 1–3, and R-Zero Appendix D.
- **Challenge / comparability:** Independent evaluators also have errors; controls are expensive, and highly personalized tasks may resist fixed splits. State carriers have different costs and capabilities. This recommendation is not an experimentally proven universal optimum.
- **Confidence / status:** Moderate; usable as a proposed decision protocol. **Change criterion:** Application-specific constraints can change the control or held-out unit; report what causal distinction is then lost.

## Thesis section mapping

The thesis uses primary-source citations in its prose; this map preserves the internal claim trace without interrupting the argument.

| Thesis section | Supporting claims |
| --- | --- |
| Introduction | C001–C002, C011 |
| Related work | C001–C004, C008–C010 |
| What the evaluations establish | C005–C009 |
| Implications and open questions | C011–C012, grounded in C003–C010 |
