# AlphaEvolve

## Source and access

**Source key:** `2025-alphaevolve`.

**Originals and source links:** [register](../sources.md#2025-alphaevolve); [canonical source](https://arxiv.org/abs/2506.13131). Retained unmodified: [2025-alphaevolve-paper-v1.pdf](../originals/2025-alphaevolve/2025-alphaevolve-paper-v1.pdf). Paper license: CC BY-NC-ND 4.0 on canonical arXiv record; PDF also contains Google DeepMind copyright/all-rights-reserved notice; original retained unmodified under arXiv-declared license. [Manifest](../originals/manifest.json).

**Source/key:** `2025-alphaevolve` — Alexander Novikov et al., *AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery*. [arXiv](https://arxiv.org/abs/2506.13131), [versioned arXiv PDF](https://arxiv.org/pdf/2506.13131v1), [official PDF](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/AlphaEvolve.pdf). First submitted 2025-06-16; latest and read arXiv version **v1, 2025-06-16**, verified from the submission history and PDF stamp `arXiv:2506.13131v1 [cs.AI] 16 Jun 2025`. Read 2026-09-16: architecture, §§3.1–3.4, Tables 1–2, Figure 8, limitations.

## Question and methods

AlphaEvolve uses an ensemble of Gemini 2.0 Flash and Pro to mutate code, maintain a diverse program database, and score candidates with user-written automatic evaluators. It targets algorithm design, mathematics, and production system optimization rather than improving its own agent harness.

## Results and evidence

The paper reports state-of-the-art improvements for 14 matrix-multiplication targets and a rank-48 algorithm for multiplying 4×4 complex matrices, improving the prior rank-49 construction (Table 2, §3.1). Across more than 50 mathematical problems it matches best-known constructions on roughly 75% and reports improvements on about 20% (§1), but full problem-level details are deferred. Engineering deployments include a discovered data-center scheduling heuristic and a matrix-kernel tiling heuristic associated with a 23% kernel speedup and 1% reduction in Gemini training time (§3.3). Figure 8 ablations average three independent runs; most other search counts, compute, and variance are not disclosed.

## Appraisal and limitations

### Interpretation

This is strong adjacent evidence that evolutionary code search can make externally validated scientific and production discoveries when a faithful evaluator exists. It does not directly show an agent improving the process that generates its own modifications.

### Limitations

Proprietary infrastructure and incomplete budgets impede reproduction. Many industrial and mathematical claims lack denominators, candidate counts, confidence intervals, or released artifacts in this white paper. Automated evaluation narrows applicability, and optimizing the supplied metric can miss unmeasured qualities.

## Discussion and follow-up

Which discoveries depend on a faithful automatic evaluator, and how far can that evaluation model extend?

[Prominent citations and their roles](../prominent-citations.md#2025-alphaevolve)
