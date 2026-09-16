# Claims

## Claim 1
**Claim:** Agent Laboratory frames autonomous research as a human-initiated assistant workflow rather than a replacement for human ideation.

**Evidence:** The system takes a human research idea as input, then runs literature review, experimentation, and report-writing phases to produce a code repository and research report. The paper explicitly contrasts this with systems that generate their own research ideas.

**Caveats/Scope:** The demonstrated domain is machine-learning research, and the generated reports are intended to help researchers understand and scale up the work rather than serve as final human-quality papers.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3; Figure 1; Figure 2

## Claim 2
**Claim:** The workflow operationalizes research through specialized agent roles and solver modules.

**Evidence:** The paper describes a PhD agent for literature review, PhD/Postdoc planning dialogue, ML/SW Engineer data and experiment work, `mle-solver` for iterative ML code generation and scoring, and `paper-solver` for scaffolded report generation, editing, compilation, and review.

**Caveats/Scope:** The workflow is relatively fixed and phase-structured; the limitations section notes restricted paper organization, limited figure handling, and lack of flexible repository-level code management.

**Source pointers:** `paper.pdf`, Sections 3.1-3.3; Figures 2-4; Section 5.1

## Claim 3
**Claim:** Human evaluation shows meaningful backend differences, but autonomous outputs remain below top-conference paper quality.

**Evidence:** In autonomous mode, reviewers rated o1-preview highest on usefulness and NeurIPS-style overall score, while o1-mini had the highest experimental-quality score. The paper reports human overall scores of 3.5/10 for gpt-4o, 3.8/10 for o1-mini, and 4.0/10 for o1-preview, below the cited NeurIPS acceptance-score average.

**Caveats/Scope:** The evaluation uses 15 generated papers from five selected topics and reviews by volunteer PhD students; the result should not be generalized to all research domains or future models.

**Source pointers:** `paper.pdf`, Section 4.1; Section 4.1.1; Figure 5; Figure 6

## Claim 4
**Claim:** Automated paper-review scores substantially overestimate the quality of Agent Laboratory outputs relative to human reviewers.

**Evidence:** The paper reports automated NeurIPS-style reviewers averaging 6.1/10 overall, while human reviewers averaged 3.8/10 on the same generated papers, with similar gaps across criteria such as clarity and contribution.

**Caveats/Scope:** This result concerns the paper's generated reports and adapted automated NeurIPS-review setup; it is evidence against relying on self-review alone, not against all possible automated evaluation protocols.

**Source pointers:** `paper.pdf`, Section 4.1.1; Figure 6

## Claim 5
**Claim:** Co-pilot mode improves externally judged paper quality over autonomous mode, but does not close the conference-quality gap.

**Evidence:** External evaluators rated co-pilot papers higher overall than autonomous papers, with the largest reported improvements in quality, soundness, and overall score. The co-pilot overall average remained below the cited NeurIPS 2024 accepted-paper average.

**Caveats/Scope:** Co-pilot experiments used o1-mini for most phases and a small set of researchers/topics; participants also reported difficulty steering agents to execute their exact project vision.

**Source pointers:** `paper.pdf`, Section 3.3.1; Section 4.2; Figure 7; Section 5

## Claim 6
**Claim:** `mle-solver` is competitive on the paper's selected MLE-Bench subset.

**Evidence:** On 10 low-complexity text/tabular MLE-Bench challenges, the paper reports that `mle-solver` submitted valid solutions for all tasks, obtained four medals, and exceeded median human performance on six of ten tasks, outperforming the compared MLAB, OpenHands, and AIDE runs by those measures.

**Caveats/Scope:** The comparison uses a selected 10-task subset and custom input formatting; invalid submissions from prior methods were excluded when averaging valid scores, so this should be cited as evidence within the paper's evaluation setup.

**Source pointers:** `paper.pdf`, Section 4.4; Figure 9
