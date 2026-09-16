# Rethinking harness-evolution evaluation

## Source and access

**Source key:** `harness-evolution-evaluation`.

**Originals and source links:** [register](../sources.md#harness-evolution-evaluation); [canonical source](https://arxiv.org/abs/2607.12227v2). Retained unmodified: [harness-evolution-evaluation-paper-v2.pdf](../originals/harness-evolution-evaluation/harness-evolution-evaluation-paper-v2.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

[Paper v2](https://arxiv.org/html/2607.12227v2). Yike Wang et al.; submitted July 14, revised August 27, 2026; preprint. Accessed September 16; §§3–5 and Tables 1–3 checked. Family: Rethinking harness evolution.

## Question and methods

Does harness search beat spending comparable feedback and rollouts on solutions? Common initial harness; five-rollout budget; 89 Terminal-Bench 2.1 tasks; three models without tests, two with tests; two independent runs (§4.1).

## Results and evidence

Table 1 prints 67.4 average pass@1 for evolution versus 72.3 parallel sampling. The rounded evolution cells average 67.47, so retain “reported average” and avoid excessive precision. With tests, Table 2 reports 75.8 versus 86.0 pass@1. Separate 45/10/34 train/validation/test tasks yield 68.3 versus 67.7 for evolved versus initial harnesses (Table 3). Confidence intervals are not provided in these tables.

## Appraisal and limitations

### Authors' claim

Existing evaluation overstates reusable improvement.

### Interpretation and limitations

Strong counterexample to weak baselines, limited to the tested implementation and benchmark. Rollout matching is not total token, latency, or dollar matching. Small held-out set and two runs limit precision; “no significant gains” is the authors' characterization, not a significance test established here.

## Discussion and follow-up

Figure 2; Table 3. How many future tasks must amortize evolution cost?
