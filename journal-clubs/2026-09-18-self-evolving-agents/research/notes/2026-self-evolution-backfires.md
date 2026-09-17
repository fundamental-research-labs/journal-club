# When Self-Evolution Backfires: Pre-Commit Gating against Skill Contamination in LLM Agents

## Source and access

**Source key:** `2026-self-evolution-backfires`.

**Originals and source links:** [register](../sources.md#2026-self-evolution-backfires); [canonical source](https://arxiv.org/abs/2608.05810). retention-restricted. [Manifest](../originals/manifest.json).

. [arXiv v1](https://arxiv.org/abs/2608.05810v1); [PDF](https://arxiv.org/pdf/2608.05810v1). Linfang Shang et al. (Tencent); August 6, 2026. Read September 16, 2026: full paper, methods, Tables 1–4, and uncertainty discussion inspected. PDF download succeeded temporarily. No copy retained: arXiv grants only its non-exclusive distribution license, not a reusable paper license; no code release is identified in the paper.

## Question and methods

### Question and method

Can bad skills contaminate descendants, making deletion after admission insufficient? Verifier-as-Gatekeeper applies schema validation, single-skill behavioral A/B replay, and one-call semantic review before admission; a second greedy gate retains only subsets with positive held-out marginal gain. The utility is neither known monotone nor submodular, so the subset procedure is explicitly heuristic (§Method).

### Splits, controls, models, and compute

Terminal-Bench 2's 89 tasks are stratified with a fixed seed into Event 50 for five rounds of distillation/evaluation, Holdout 14 for gate A/B replay and marginal-gain estimates, and untouched Test 25 for final frozen-pool evaluation. Each round uses k=3 rollouts per task and deterministic TB2 graders. The primary Hy3 ReAct agent is compared with a static three-skill seed, unconditional admission, post-hoc rollback, and VaG. Cross-model Test-25 evaluation freezes the Hy3 pool and uses DeepSeek-V4-Pro, GPT-5.4, Claude Sonnet 4.5, and Qwen3.6-35B-A3B; cross-benchmark evaluation uses all 200 InterCode NL2Bash tasks. No independent evolution repeats are reported. Table 1 reports mean per-trial tokens, but training/gating tokens, wall time, model calls, and dollar cost are not totaled; semantic review costs one inference/candidate and joint selection at most 14 replays/round.

## Results and evidence

On Event-50, ungated pass@1 rises 48→60→62, then falls to 52→50 as its pool grows 35→179; VaG rises 52→58→62→68→72 with 5→37 skills (Table 1). Event-50 has only 2 easy, 31 medium, and 17 hard tasks. Wilson bands are about 30 points wide and overlap; the paper explicitly bases its claim on trajectory shape rather than significant per-round contrasts. Removing eight harmful source skills gives 50→52; oracle lineage cleanup reaches 56.7 versus the 62.3 peak and 72 VaG (Figure 4). On untouched Test-25, the frozen VaG pool improves all five backbones by 8–16 points over the static seed (Table 3), but the table does not show round-by-round ungated collapse. On InterCode, seed/ungated/VaG are 57.5/65.5/69.0 (Table 4). Table 2's Event-50 ablations lower VaG from 72 to 70 without schema validation, 62 without holdout replay, 68 without semantic review, and 64 without marginal-gain selection.

## Appraisal and limitations

### Authors' claim

Contamination produces a capability phase transition, descendant inheritance makes it structurally irreversible, and pre-commit gates outperform cleanup.

### Interpretation and limitations

The paper offers a vivid mechanistic example and a useful admission-gate design. The main inverted-U and rollback effects are measured on Event, the same tasks driving skill creation across five correlated rounds; k=3 repeats are not independent evolution trajectories. Test-25 supports positive transfer of the gated final pool but does not independently reproduce the phase transition or VaG's monotonic trajectory. The statement that the trajectory difference cannot arise by chance is unsupported by a repeated-trajectory test. InterCode shares shell operations with TB2. This is credible exploratory counterevidence and a strong reserve source, but Library Drift remains stronger for repeated lifecycle comparisons and AgentStream stronger for broad order/configuration effects.

## Discussion and follow-up

Table 1 and Figure 4 distinguish deletion of a bad source from prevention of descendant formation. Ask what provenance and sealed replay set an admission gate needs in deployment.

[Prominent citations and their roles](../prominent-citations.md#2026-self-evolution-backfires)
