# Review Rating Stability

This document records blinded stability checks for paper ratings produced with `docs/review-rubric.md`.

## Protocol

For a stability check:

1. Select one target paper folder under `papers/`.
2. Spawn five independent reviewers.
3. Give each reviewer access to `docs/review-rubric.md` and the target paper folder only.
4. Explicitly forbid reading `docs/paper-reviews.md` or any aggregate review file.
5. Ask each reviewer to return scores before seeing any other review.
6. Aggregate the numeric scores with mean, median, min/max range, and sample standard deviation.
7. Flag instability when the overall score range is greater than 2, when any core criterion range is greater than 1, or when reviewers cross the accept/reject boundary.

Core criteria are Novelty, Technical correctness and rigor, and Multi-agent specificity, following the rubric.

## Pilot: CooperBench

**Paper:** `papers/CooperBench_2601.13295`
**Date run:** 2026-05-04
**Reviewers:** 5 independent agents
**Bias control:** Each reviewer was explicitly instructed not to open, read, or use `docs/paper-reviews.md` or any aggregate review file. Each reviewer explicitly confirmed compliance. Aggregation below uses only the returned independent scores.

### Raw Scores

| Reviewer | Novelty | Significance | Rigor | Breadth | MAS specificity | Reproducibility | Clarity | Usefulness | Overall | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 4 | 5 | 4 | 4 | 5 | 3 | 4 | 4 | 8 | 4 |
| B | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 7 | 4 |
| C | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 7 | 4 |
| D | 4 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 8 | 4 |
| E | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 4 | 7 | 4 |

### Stability Statistics

Sample standard deviation is reported over the five reviewers.

| Measure | Mean | Median | Range | Sample SD |
|---|---:|---:|---:|---:|
| Novelty | 4.0 | 4 | 4-4 | 0.00 |
| Significance | 4.4 | 4 | 4-5 | 0.55 |
| Technical correctness and rigor | 4.0 | 4 | 4-4 | 0.00 |
| Empirical breadth and generality | 4.0 | 4 | 4-4 | 0.00 |
| Multi-agent specificity | 5.0 | 5 | 5-5 | 0.00 |
| Reproducibility and transparency | 3.4 | 3 | 3-4 | 0.55 |
| Clarity and positioning | 4.0 | 4 | 4-4 | 0.00 |
| Practical usefulness | 4.2 | 4 | 4-5 | 0.45 |
| Overall score | 7.4 | 7 | 7-8 | 0.55 |
| Confidence | 4.0 | 4 | 4-4 | 0.00 |

### Interpretation

The CooperBench ratings are stable under this five-reviewer check.

- Decision-level agreement is high: all reviewers rated the paper as `Accept`-level, with overall scores only ranging from 7 to 8.
- All three core criteria were exactly stable: Novelty = 4, Technical correctness and rigor = 4, Multi-agent specificity = 5.
- Five of eight criterion scores had exact agreement across all reviewers.
- The only criterion-level variation was one point on Significance, Reproducibility and transparency, and Practical usefulness.
- Confidence was unanimous at 4.

The main unstable dimension is not the paper's scientific contribution, but how reviewers credit unverified artifact availability. Reviewers giving Reproducibility = 4 credited the described prompts, containers, and claimed release more strongly; reviewers giving Reproducibility = 3 emphasized that external artifacts, exact API versions, decoding settings, costs, and traces were not verified from local materials.

### Consensus Themes

Common strengths:

- Real-repository collaborative coding benchmark with expert-written tests.
- Strong Solo vs Coop baseline that directly tests whether multiple agents help.
- Communication ablation showing that chat reduces merge conflicts but not end-to-end success.
- Multi-agent-specific failure analysis around communication, commitments, expectations, and partial observability.

Common weaknesses:

- Results may depend on the OpenHands-style setup and text-only communication channel.
- Token budget, model-call, latency, cost, decoding, and repeated-run controls are not reported strongly enough.
- Three- and four-agent scaling evidence is suggestive but based on a smaller subset.
- Some broad claims about social intelligence or general teamwork go beyond the coding benchmark evidence.

### Rubric Calibration Notes

Future versions of `docs/review-rubric.md` should clarify:

- Whether Reproducibility should credit claimed artifact release when the reviewer has not verified the external artifacts.
- Whether cost, token, latency, and model-call accounting belongs primarily under Technical correctness and rigor, Reproducibility, or both.
- Whether Practical usefulness should reward a strong cautionary benchmark even when the paper does not test many remedies.

## Pilot: CAMEL

**Paper:** `papers/CAMEL_2303.17760`
**Date run:** 2026-05-04
**Reviewers:** 5 independent agents
**Bias control:** Each reviewer was explicitly instructed not to open, read, or use `docs/paper-reviews.md`, `docs/review-stability.md`, or any aggregate review file. Each reviewer explicitly confirmed compliance. Aggregation below uses only the returned independent scores.

The local `summary.md`, `claims.md`, and `notes.md` files were stubs at review time, so reviewers primarily used `paper.pdf`.

### Raw Scores

| Reviewer | Novelty | Significance | Rigor | Breadth | MAS specificity | Reproducibility | Clarity | Usefulness | Overall | Confidence |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 4 | 4 | 2 | 3 | 3 | 4 | 3 | 4 | 6 | 4 |
| B | 4 | 4 | 2 | 3 | 3 | 4 | 4 | 4 | 6 | 4 |
| C | 4 | 4 | 2 | 3 | 3 | 4 | 4 | 4 | 6 | 4 |
| D | 4 | 4 | 2 | 3 | 3 | 4 | 4 | 4 | 6 | 4 |
| E | 4 | 4 | 2 | 3 | 3 | 4 | 3 | 4 | 6 | 4 |

### Stability Statistics

Sample standard deviation is reported over the five reviewers.

| Measure | Mean | Median | Range | Sample SD |
|---|---:|---:|---:|---:|
| Novelty | 4.0 | 4 | 4-4 | 0.00 |
| Significance | 4.0 | 4 | 4-4 | 0.00 |
| Technical correctness and rigor | 2.0 | 2 | 2-2 | 0.00 |
| Empirical breadth and generality | 3.0 | 3 | 3-3 | 0.00 |
| Multi-agent specificity | 3.0 | 3 | 3-3 | 0.00 |
| Reproducibility and transparency | 4.0 | 4 | 4-4 | 0.00 |
| Clarity and positioning | 3.6 | 4 | 3-4 | 0.55 |
| Practical usefulness | 4.0 | 4 | 4-4 | 0.00 |
| Overall score | 6.0 | 6 | 6-6 | 0.00 |
| Confidence | 4.0 | 4 | 4-4 | 0.00 |

### Interpretation

The CAMEL ratings are highly stable under this five-reviewer check.

- Decision-level agreement is exact: all reviewers gave the paper an overall score of 6.
- Seven of eight criterion scores had exact agreement across all reviewers.
- All three core criteria were exactly stable: Novelty = 4, Technical correctness and rigor = 2, Multi-agent specificity = 3.
- The only variation was one point on Clarity and positioning.
- Confidence was unanimous at 4.

The stable consensus is that CAMEL is foundational and practically useful, but weaker as evidence for intrinsic multi-agent advantage. Reviewers consistently credited the paper for early role-playing agents, inception prompting, reusable code/data, and agent failure-mode analysis. They consistently penalized it for weak or non-budget-matched baselines, preference-heavy evaluation, GPT-4 summarization/judging confounds, and limited isolation of interaction effects from more tokens, more calls, iterative decomposition, and answer length.

### Consensus Themes

Common strengths:

- Foundational early framework for LLM role-playing agents.
- Concrete two-agent protocol with task specifier, AI user, AI assistant, structured messages, and termination rules.
- Useful open artifacts: code, datasets, prompts, examples, and training details.
- Practical failure-mode taxonomy around role flipping, repeated instructions, flake replies, and infinite loops.

Common weaknesses:

- Main comparisons are not token-, call-, interaction-, or cost-matched.
- Baselines are weaker than budget-matched single-agent iterative prompting, self-consistency, self-dialogue, or planner/executor workflows.
- GPT-4 summarization and GPT-4-as-judge evaluation create possible evaluator and verbosity bias.
- Human preference evaluation is limited and may not establish domain-specific correctness.
- Broad claims about AI society, emergence, or cognition exceed what two prompted chat agents demonstrate.

### Rubric Calibration Notes

This run suggests the rubric is stable when reviewers can inspect the PDF directly, even when local paper notes are stubs. The main calibration point is historical significance: reviewers rewarded CAMEL's influence under Novelty, Significance, Reproducibility, and Practical usefulness, but still kept Technical correctness and rigor low because the experiments do not meet the current repo standard for budget-matched multi-agent evidence.
