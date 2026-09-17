# SHAPER: Self-Evolving Embodied Agents via Skill-Harness Evolution

## Source and access

**Source key:** `2026-shaper`.

**Originals and source links:** [register](../sources.md#2026-shaper); [canonical source](https://arxiv.org/abs/2608.11350v2). retention-restricted. [Manifest](../originals/manifest.json).

**Primary source:** Peidong Wang et al., *Self-Evolving Embodied Agents via Skill-Harness Evolution*, [arXiv:2608.11350v2](https://arxiv.org/abs/2608.11350v2), submitted 2026-08-11; v2 2026-09-10.

**Version/access:** v2 PDF, read 2026-09-16; §§3–4, Tables 1–3, Appendix A.4.

**Original:** see current acquisition record above. [Direct PDF](https://arxiv.org/pdf/2608.11350v2). ArXiv non-exclusive distribution license; no separate redistribution license found.

## Question and methods

### Question and role

Can a frozen embodied planner/executor improve by changing only persistent procedural instructions and context-building code, and do those changes transfer beyond the small rollout set used for evolution? SHAPER adds embodied action, held-out target categories, and active visual evidence gathering to the session.

### Methods and resource budget

SHAPER uses Qwen3.6-27B in planner and artifact-optimizer roles while keeping all model weights frozen. It evolves a textual skill first, then executable context-construction code while holding the selected skill fixed (§3). Harness candidates must compile and pass sandbox/schema checks before rollout.

VLABench uses the official fine-tuned π0 checkpoint as low-level executor. Evolution uses 15 training episodes and a fixed 24-episode validation set. Evaluation uses four disjoint custom cells crossing semantic/common-sense task form with seen/unseen targets: five task families and 40 episodes per family in each cell, **200 per cell, 800 total**. Episodes cap at 10 planner rounds/400 low-level steps. Same-data SFT and test-time selection/voting are comparators.

ESI-Bench uses 10 training questions, 10 validation questions, and a 231-question held-out subset matching official category proportions. The planner uses the benchmark action API for at most 30 steps. Both benchmarks use four beam-search rounds, width 3, branch factor 2, and feedback minibatches of four rollouts (§4.1, p.6).

## Results and evidence

Table 2 (p.6), VLABench success:

| Configuration | Overall |
| --- | ---: |
| Direct VLA | 23.25% |
| SFT, same 15 episodes | 24.00% |
| Seed Agent | 28.25% |
| Skill only | 33.50% |
| Harness only | 30.50% |
| SHAPER | 34.50% |

SHAPER minus Seed is +2.5 C1 (in-domain), +6.0 C2 (unseen target), +10.0 C3 (new task form), and +6.5 C4 (both shifted). Adding the harness after skill evolution changes the aggregate by only +1 point; the configurations are not factorial estimates and their effects are non-additive (§4.2).

Table 3 (p.7), ESI-Bench micro/macro accuracy: Seed 32.5/31.2, evolved skill 41.1/38.6, SHAPER 49.8/42.9. From skill-only to SHAPER, Enumerative Perception falls 33.3→27.8 (n=18) and Action Sequencing 40→20 (n=5), while Specular Reflection rises 20→60 (n=20), Perceptual Grounding 59.2→69.4 (n=49), and Spatial Relations 37.3→54.9 (n=51). The 42.9 macro score versus a published GPT-5 passive-view 40.3 is an external comparison on a different full evaluation set.

Logged evolution tokens correspond to about $2.25 for VLABench and $2.83 for ESI-Bench at stated Alibaba Cloud prices. These figures include rollout planning, judging, summarization, and optimization but exclude final evaluation and simulator/GPU infrastructure (§4.4; Appendix A.4).

## Appraisal and limitations

### Authors' claim, evidence, and interpretation

The authors argue that skill-plus-harness optimization is a cheap train-free adaptation route across fixed action interfaces. The disjoint train/validation/evaluation design supports held-out reuse of one selected artifact pair, and the gains occur in two distinct environments. “Cheap” applies only to token-equivalent optimizer cost, not total embodied rollout/simulator compute. The results are descriptive because there is no repeated artifact-search run, seed analysis, or interval.

### Strengths and limitations

Strengths: frozen planner/executor isolates external artifacts; small adaptation sets are separate from substantial held-out sets; task-form and category shifts are explicit; ablations show skill carries most VLABench gain; regressions are reported by category.

Limits: one optimization result can benefit from stochastic selection on a fixed validation set; no uncertainty is reported; custom VLABench splits are not official; ESI evaluation uses a subset; the comparator coverage differs between benchmarks; and the evolved harness includes task-conditioned evidence policies whose breadth outside these environments is unknown.

## Discussion and follow-up

### Candidate figures

Redraw the two-stage skill/harness update boundary and use the four VLABench cells to show where gains transfer. Pair aggregate improvement with the ESI category regressions.

[Prominent citations and their roles](../prominent-citations.md#2026-shaper)
