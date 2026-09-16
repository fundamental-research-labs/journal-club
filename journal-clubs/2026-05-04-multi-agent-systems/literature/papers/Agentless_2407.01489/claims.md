# Claims

## Claim 1
**Claim:** A fixed, non-agentic pipeline can be competitive with autonomous software-engineering agents on SWE-bench Lite.

**Evidence:** Table 1 reports that Agentless with GPT-4o resolves 96 of 300 SWE-bench Lite tasks (32.00%) at $0.70 average cost. The paper states this is the highest result among the open-source approaches in its comparison, while several closed-source or commercial systems score higher.

**Caveats/Scope:** The claim is scoped to the paper's SWE-bench Lite setup, GPT-4o configuration, and the baselines/results available to the authors. It does not show that agentless pipelines dominate all autonomous agents or later model/tool versions.

**Source pointers:** Abstract; Section 4 "Experimental Setup"; Section 5.1 "Performance on SWE-bench Lite"; Table 1.

## Claim 2
**Claim:** Hierarchical localization is a major mechanism behind Agentless's low-context repair pipeline.

**Evidence:** Section 3.1 describes file-level, related-element, and edit-location localization. Table 2 shows combined prompt plus embedding file localization containing the ground-truth file in 81.67% of tasks, better than either component alone, and shows skeleton-format related-element localization outperforming complete-file input while using far less cost.

**Caveats/Scope:** The "contains ground truth" metric compares against developer patch locations and may miss alternative valid fixes. The ablation is on SWE-bench Lite repositories and does not establish performance on other languages or larger monorepos.

**Source pointers:** Section 3.1 "Localization"; Figure 1; Figure 2; Section 5.2.1 "Localization ablation"; Table 2.

## Claim 3
**Claim:** Sampling multiple edit-location sets and candidate Search/Replace patches improves repair over a single greedy localization/repair path.

**Evidence:** The default setup samples four edit-location sets and generates 10 patches per set, for 40 candidate patches per issue. Table 3 reports 96 fixes for the multi-sample setup versus 88 for greedy locations and 85 for merged multi-samples. Figure 6 shows performance rising with more patch samples before plateauing around the default sample budget.

**Caveats/Scope:** More samples increase inference and validation work, and the paper's own curve suggests diminishing returns after the chosen budget. The reported upper bound of 126 fixes depends on being able to select a correct patch from generated candidates, which the current ranking method cannot always do.

**Source pointers:** Section 3.2 "Repair"; Section 4 "Implementation"; Section 5.2.2 "Repair ablation"; Table 3; Figure 6.

## Claim 4
**Claim:** Generated reproduction tests provide important patch-selection signal, but they are imperfect and need conservative fallback behavior.

**Evidence:** Table 4 reports that majority voting alone resolves 77 tasks, adding regression tests resolves 81, and adding reproduction-test filtering reaches 96. Section 5.1.3 reports that Agentless generates 213 tests that reproduce the issue on the original repository, but only 94 also validate the ground-truth patch as resolved.

**Caveats/Scope:** Reproduction tests are synthesized from issue descriptions and can be incomplete or wrong. The method mitigates this by requiring regression-test filtering first and falling back to regression results when no patch passes the reproduction test.

**Source pointers:** Section 3.3 "Patch Validation"; Section 5.1.3 "Reproduction test results"; Section 5.2.3 "Patch validation ablation"; Table 4; Figure 7.

## Claim 5
**Claim:** The paper argues that SWE-bench Lite contains benchmark artifacts that can distort evaluation of software agents.

**Evidence:** The manual classification in Section 6.1 reports that 10.0% of tasks lack enough information, 4.3% contain the exact ground-truth patch in the issue description, and 5.0% contain misleading solution steps. The authors build SWE-bench Lite-S by removing exact-patch, misleading-solution, and insufficient-information cases, leaving 249 tasks.

**Caveats/Scope:** The classifications are manual and depend on the authors' definitions of problematic issues. Filtering improves interpretability but may also change the task distribution.

**Source pointers:** Section 6.1 "Problem Classification"; Figure 8; Section 6.2 "SWE-bench Lite-S"; Table 5.

## Claim 6
**Claim:** Agentless remains competitive on the paper's reported SWE-bench Verified comparison.

**Evidence:** Table 6 reports Agentless with GPT-4o solving 194 of 500 SWE-bench Verified tasks (38.80%). The text states this is second highest among open-source approaches in that table and best among techniques using GPT-4o.

**Caveats/Scope:** This is a reported comparison against the systems listed in the paper, not a continuously updated leaderboard result. It is still a benchmark result, not evidence of universal real-world reliability.

**Source pointers:** Section 6.3 "SWE-bench Verified"; Table 6; Section 7 "Threats to Validity".
