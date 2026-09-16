# Claims

## Claim 1
**Claim:** PaperBench operationalizes AI research replication as a from-scratch repository-building task over recent ML papers.

**Evidence:** Agents receive a paper and addendum, must produce a repository with `reproduce.sh`, and are evaluated after the repository is run in a fresh environment. The benchmark covers 20 ICML 2024 Spotlight and Oral papers, and original author code or online replications are blacklisted.

**Caveats/Scope:** The dataset is curated rather than exhaustive, and the benchmark currently contains only 20 papers.

**Source pointers:** `paper.pdf`, Abstract; Sec. 2.1; Sec. 2.2; Sec. 2.5; Sec. 3; Table 2

## Claim 2
**Claim:** Author-reviewed hierarchical rubrics make partial progress on complex paper replication measurable.

**Evidence:** Each paper has a weighted rubric tree whose leaf nodes are graded as binary criteria and propagated upward into a Replication Score. The rubrics distinguish Code Development, Execution, and Result Match requirements, and the full benchmark contains 8,316 leaf nodes.

**Caveats/Scope:** Rubric design and weighting require expert judgment, and different valid rubrics could emphasize different aspects of a paper.

**Source pointers:** `paper.pdf`, Sec. 2.3; Sec. 2.4; Fig. 2; Table 1; Sec. 3.1; Appendix C

## Claim 3
**Claim:** LLM-based judging is necessary for PaperBench-scale evaluation, but it remains an approximation to expert grading.

**Evidence:** The authors report that manual expert grading takes tens of hours per paper, so they introduce SimpleJudge and JudgeEval. On JudgeEval, o3-mini with the SimpleJudge scaffold reaches 0.83 F1 at the reported cost level and is used for the main results.

**Caveats/Scope:** The paper notes that the judge is not deterministic and is not as accurate as expert human grading; JudgeEval is an auxiliary benchmark rather than a proof of perfect grading.

**Source pointers:** `paper.pdf`, Sec. 4; Sec. 4.1; Sec. 4.2; Table 3; Sec. 7; Appendix G

## Claim 4
**Claim:** The evaluated frontier agents show non-trivial progress but do not competently replicate full ML papers.

**Evidence:** In the main BasicAgent setup, Claude 3.5 Sonnet (New) scores 21.0% on average, o1 scores 13.2%, and the other tested models score below 10%. On the reported human-baseline subset, best-of-3 ML PhD participants score 41.4% after 48 hours, compared with 26.6% for o1.

**Caveats/Scope:** These are initial baselines under specific scaffolds, model versions, run limits, and compute settings; the paper explicitly leaves room for better scaffolding.

**Source pointers:** `paper.pdf`, Abstract; Sec. 5.1; Sec. 5.2; Sec. 5.4; Table 4; Fig. 3; Sec. 8

## Claim 5
**Claim:** Agent scaffold and long-horizon work behavior materially affect PaperBench performance.

**Evidence:** IterativeAgent improves o1 from 13.2% to 24.4% and o3-mini from 2.6% to 8.5%, while reducing Claude 3.5 Sonnet from 21.0% to 16.1%. The authors' log inspection finds early termination, weak strategizing under time limits, and tool-use struggles for some models.

**Caveats/Scope:** IterativeAgent is one prompt/scaffold variant, so the results show scaffold sensitivity rather than identifying an optimal agent design.

**Source pointers:** `paper.pdf`, Sec. 5.2; Sec. 5.3; Table 4; Table 5; Fig. 3; Appendix F

## Claim 6
**Claim:** PaperBench Code-Dev trades robustness for accessibility.

**Evidence:** The Code-Dev variant skips the reproduction step and grades only Code Development nodes, reducing grading and infrastructure burden. The paper reports o1 with IterativeAgent scoring 43.4% on Code-Dev and describes its correlation with full PaperBench as weak.

**Caveats/Scope:** Because it does not verify execution or result reproduction, Code-Dev should be treated as a noisy proxy rather than a replacement for the full benchmark.

**Source pointers:** `paper.pdf`, Sec. 2.6; Table 6; Sec. 7
