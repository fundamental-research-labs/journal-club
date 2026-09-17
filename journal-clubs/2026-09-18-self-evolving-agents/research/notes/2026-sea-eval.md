# SEA-Eval

## Source and access

**Source key:** `2026-sea-eval`.

**Originals and source links:** [register](../sources.md#2026-sea-eval); [canonical source](https://arxiv.org/abs/2604.08988v3). Retained unmodified: [2026-sea-eval-paper-v3.pdf](../originals/2026-sea-eval/2026-sea-eval-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Primary source:** Sihang Jiang et al., *SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment*, [arXiv:2604.08988v3](https://arxiv.org/abs/2604.08988v3), submitted 2026-04-10; v3 2026-05-24.

**Version/access:** v3 PDF, read 2026-09-16; §§4.2–5.4, Tables 1–4, Figures 3–6, limitations/appendix metric definitions.

## Question and methods

### Question and role

How should a self-evolving agent be evaluated when identical final success rates can hide different learning, transfer, interference, and cost trajectories? This is the most direct source in the lane for explaining why an episodic final score is insufficient.

### Methods and experimental setting

SEA-Eval contains 32 atomic desktop/web tasks: 12 Easy, 18 Normal, and 2 Hard. It constructs 92 length-5 sequences: 32 correlated, 30 orthogonal, and 30 implicit-intent (§4.3.4, p.10). Correlated streams repeat one instance three times and then substitute two variable-slot variants: `R1→R2→R3→A2→A3`. Orthogonal streams insert three unrelated tasks and then return to the identical or a similar target (§4.3.2, pp.9–10). A noisy-memory condition preloads 20 unrelated skills (§4.3.3).

The empirical comparison uses GenericAgent, OpenClaw, Hermes, Claude Code, and Codex in container sandboxes. Claude Opus 4.6 is the core model for Easy-Correlated runs except Codex, which uses GPT-5.5 (§5.1–5.2, p.11). Hermes, Claude Code, and Codex have a 15-minute timeout. Token consumption and success rate are primary metrics; derived measures describe convergence, transfer, and post-interference stability.

## Results and evidence

Table 2 (p.11), mean tokens in thousands from R1 to R3 and aggregate success rate:

| System | R1 | R3 | SR |
| --- | ---: | ---: | ---: |
| GenericAgent | 198.7 | 63.6 | 95.0% |
| OpenClaw | 1905.1 | 1118.7 | 96.7% |
| Hermes | 355.9 | 226.7 | 65.0% |
| Claude Code | 252.0 | 99.7 | 91.7% |
| Codex | 128.7 | 115.3 | 85.0% |

The abstract's maximum **31.2×** token difference is at an individual-task level; it is not the aggregate ratio in Table 2. Figure 4 (p.12) reports median R3-versus-R1 token changes of −78% for GenericAgent and −28% for Codex. Under orthogonal interference, Figure 5/p.13 reports GenericAgent median changes of −35.2% on the identical target and −29.2% on the similar target; OpenClaw changes −13.1% and +22.2%. Table 3/p.14 reports stage-mean stability, including A3-versus-A2 increases of +45.6% for GenericAgent and +47.2% for Codex, versus −38.9% for Claude Code.

## Appraisal and limitations

### Authors' claim, evidence, and interpretation

The authors argue that success-only evaluation creates a capability illusion and that convergence of token use distinguishes genuine from pseudo-evolution. The evidence does establish that final success and execution cost trajectories can diverge sharply in these systems. It does not establish token decline as a sufficient definition of learning. Caching, a low initial token baseline, framework overhead, stored answers, and task-specific compression can produce similar curves.

### Strengths and limitations

Strengths are the explicit sequence structures, variable-slot transfer, interference condition, and attention to cost trajectories. Important limits: foundation models differ across systems; prompt caching makes some token accounting opaque; no seeds, run counts, or uncertainty intervals are reported in the inspected setup; the headline empirical table is for Easy-Correlated tasks rather than all 92 sequences; and Hermes orthogonal experiments were incomplete (footnote 8, p.13). Composite normalized scores clip and combine metrics with different meanings, so raw trajectories are preferable for teaching.

## Discussion and follow-up

### Candidate figures

Redraw the correlated/orthogonal sequence design from Table 1 and pair it with selected raw trajectories from Figures 4–5. Do not reproduce the composite radar chart without explaining normalization.

[Prominent citations and their roles](../prominent-citations.md#2026-sea-eval)
