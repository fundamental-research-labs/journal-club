# Claims

## Claim 1
**Claim:** SWE-bench-Live is designed to reduce benchmark staleness and contamination risk for repository-level issue resolution.

**Evidence:** The initial release uses real GitHub issues created between January 1, 2024 and April 20, 2025, and the authors plan monthly updates. They frame this as a response to SWE-bench-style datasets being static and potentially present in model training data.

**Caveats/Scope:** Freshness reduces contamination risk but does not prove that no model has seen every issue, PR, or repository artifact. The initial release is restricted to Python repositories.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3.4; Figure 2.

## Claim 2
**Claim:** SWE-bench-Live substantially broadens real issue-resolution benchmark coverage while preserving test-based evaluation.

**Evidence:** The dataset contains 1,319 task instances from 93 open-source Python repositories, compared in Table 1 against SWE-bench, SWE-bench Verified, SWE-Gym, Multi-SWE-bench, and SWE-smith. Tasks keep the SWE-bench-style requirement that a generated patch resolve an issue and pass designated tests.

**Caveats/Scope:** The comparison is about benchmark construction and coverage, not a guarantee that every task is equally hard or equally representative of all software domains.

**Source pointers:** `paper.pdf`, Abstract; Table 1; Section 3; Section 3.4; Appendix B.

## Claim 3
**Claim:** REPOLAUNCH automates the main construction bottleneck: producing executable, reproducible environments for issue-resolution tasks.

**Evidence:** REPOLAUNCH identifies relevant setup files, selects a Docker base image, interactively installs/builds the repository, verifies tests, and finalizes a Docker image for each valid instance. The paper also adds a time-machine package-installation mechanism to avoid dependency version drift from packages released after the base commit.

**Caveats/Scope:** The paper describes the pipeline and validation logic, but environment success still depends on repository metadata, test parsers, agent behavior, and the Python/package ecosystem assumptions in the initial release.

**Source pointers:** `paper.pdf`, Figure 1; Section 3.2; Section 3.3.

## Claim 4
**Claim:** Current agent/model combinations perform much worse on SWE-bench-Live than on SWE-bench Verified under comparable conditions.

**Evidence:** The best full-benchmark result reported is OpenHands with Claude 3.7 Sonnet at 19.25% resolved. The authors rerun the same agent/model setup on SWE-bench Verified and report 43.20% resolved.

**Caveats/Scope:** The gap is consistent with overfitting or contamination concerns, but it could also reflect differences in repository mix, issue selection, environment difficulty, or benchmark validation.

**Source pointers:** `paper.pdf`, Section 4.2; Table 4.

## Claim 5
**Claim:** The benchmark exposes a sharp difficulty increase for multi-file, large-patch, and large-repository fixes.

**Evidence:** Section 4.4 reports that single-file patches changing fewer than five lines are solved about 48% of the time, while patches touching at least three files or more than 100 lines fall below 10%; patches touching seven or more files are not solved in the reported analysis. Appendix Figure 7 also shows lower resolved rates for larger repositories.

**Caveats/Scope:** Patch size and repository size are heuristic difficulty proxies; small repositories can still be hard due to build systems or domain logic.

**Source pointers:** `paper.pdf`, Section 4.4; Figure 5; Appendix C and Figure 7.

## Claim 6
**Claim:** SWE-bench-Live includes a smaller Lite subset for cheaper experimentation without changing the task format.

**Evidence:** The Lite subset samples 50 instances per month from issues created between October 2024 and March 2025, producing 300 instances. Tables 3 and 4 use Lite results to screen agent/model combinations before evaluating the top combinations on the full benchmark.

**Caveats/Scope:** Lite is a convenience subset and should not replace full-benchmark evaluation when measuring final model capability.

**Source pointers:** `paper.pdf`, Section 3.4; Section 4.2; Table 3; Table 4.
