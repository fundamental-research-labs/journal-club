# Library Drift / Ratchet

## Source and access

**Source key:** `library-drift`.

**Originals and source links:** [register](../sources.md#library-drift); [canonical source](https://arxiv.org/abs/2605.19576v3). Retained unmodified: [2026-library-drift-paper-v3.pdf](../originals/2026-library-drift/2026-library-drift-paper-v3.pdf). Paper license: http://creativecommons.org/licenses/by-nc-sa/4.0/. [Manifest](../originals/manifest.json).

[Paper v3](https://arxiv.org/html/2605.19576v3); [reference code](https://github.com/amazon-science/Self-Evolving-Agents-Ratchet/). Xing Zhang et al.; May 19, revisions June 25 and July 29, 2026. Repository reports FAGEN@ICML 2026 workshop acceptance for Library Drift. Accessed September 16; §§5–7 and Table 1 read. Family: Ratchet (companion paper and code are shared evidence).

## Question and methods

When does accumulated skill guidance harm? Routing, authoring priors, bounded storage, and retirement; single-call solver, not a tool-using agent. Select 100 difficult MBPP+ tasks using five baseline seeds, split 60/40; 100 rounds, three seeds (§6.1).

## Results and evidence

Table 1 gain is last-ten minus first-ten mean pass@1: default +0.328±0.018 SD; harsh retirement −0.019±0.010. This differs from round-zero 0.258→late-window 0.584. Default costs about 14.5k calls and 6.5 hours, versus no-injection 10k and 2.3 hours (§6.4).

## Appraisal and limitations

### Authors' claim

Lifecycle management prevents skill-library drift.

### Interpretation and limitations

Ablations expose harmful overcorrection as well as benefits. Forty selected evaluation tasks, one model, repeated evaluations, and unmatched costs constrain generalization. A no-injection control cannot by itself isolate harm from unbounded accumulation. The non-divergence proof was not audited.

## Discussion and follow-up

Table 1, Figure 2: how much evidence should precede retirement?

[Prominent citations and their roles](../prominent-citations.md#library-drift)
