# Claims

## Claim 1: Multi-agent failures can be classified into recurring system-level categories.

**Evidence:** MAST organizes empirically observed failures into system design issues, inter-agent misalignment, and task verification failures, with fine-grained modes under each.

**Caveats/Scope:** The taxonomy is empirically grounded but not claimed to be exhaustive for all future MAS designs.

**Source pointers:** `summary.md`; `source/01_abstract.tex`; `source/05_findings.tex`

## Claim 2: MAS failures are often caused by architecture, prompts, coordination, or verification, not only by weak base models.

**Evidence:** The paper emphasizes that better MAS design can improve outcomes with the same underlying model, and reports intervention gains from role-specification and topology changes.

**Caveats/Scope:** Interventions improve results but do not fully solve reliability.

**Source pointers:** `source/05_findings.tex`; `source/06_discussions.tex`; `source/09_solutions.tex`

## Claim 3: Verification helps but superficial verifier agents are insufficient.

**Evidence:** Systems with explicit verifiers tend to show fewer total failures, yet examples show code can pass shallow checks while violating task objectives; high-level verification improves ChatDev in a case study.

**Caveats/Scope:** Verification needs domain-appropriate tests and objective checks, not just final-stage review.

**Source pointers:** `source/05_findings.tex`; `source/09_solutions.tex`; `summary.md`

## Claim 4: Failure profiles differ by MAS framework and model choice.

**Evidence:** The discussion reports framework-specific patterns, such as premature termination, step repetition, and verification-heavy failures, and compares GPT-4o with Claude 3.7 Sonnet inside MetaGPT.

**Caveats/Scope:** Cross-system comparisons can be affected by differing tasks and benchmarks, so profiles are best used diagnostically.

**Source pointers:** `source/06_discussions.tex`; `source/10_mast_analysis.tex`

## Claim 5: MAST can be used as a practical debugging and evaluation tool.

**Evidence:** The paper builds an LLM-as-a-judge pipeline for scalable annotation and uses before/after failure-mode breakdowns to evaluate interventions.

**Caveats/Scope:** Automated annotation is validated against human labels but still depends on trace quality and taxonomy fit.

**Source pointers:** `source/04_methodology.tex`; `source/06_discussions.tex`; `source/09_solutions.tex`
