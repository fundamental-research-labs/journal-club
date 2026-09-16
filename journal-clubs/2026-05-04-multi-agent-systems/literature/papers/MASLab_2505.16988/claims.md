# Claims

## Claim 1
**Claim:** MASLab provides a unified implementation layer for a broad set of LLM-based multi-agent methods.

**Evidence:** The paper lists 24 supported methods across single-agent baselines, general MAS, coding, math, scientific, and tool-required categories, and describes a common Python class/inference-function structure with shared preprocessing, resources, and configurations.

**Caveats/Scope:** The claim is about the authors' integrated research codebase, not an independent replication of every original system. Some methods are simplified or adapted, as described in the appendix re-implementation notes.

**Source pointers:** `paper.pdf`, Abstract; Table 1; Sections 3.1 and D

## Claim 2
**Claim:** Standardizing evaluation protocols is necessary because protocol choice can change both absolute scores and method rankings.

**Evidence:** On MATH with Llama-3.3-70B-Instruct, Figure 3 shows rank changes across five evaluation protocols; the text reports MAV moving from 1st under LLM two-step evaluation to 10th under a DyLAN-style rule-based metric, and AgentVerse dropping from 79.0 to 25.6 accuracy when switching evaluators.

**Caveats/Scope:** The most detailed protocol-comparison evidence is on MATH, so the magnitude of rank instability may differ on other domains.

**Source pointers:** `paper.pdf`, Section 3.2; Figure 3; Table 4

## Claim 3
**Claim:** In the paper's human audit, LLM-based answer evaluation is more reliable than the rule-based protocols tested.

**Evidence:** Table 4 reports 98.59 accuracy for LLM two-step evaluation and 98.35 for LLM-xVerify agreement with human checks on MATH, compared with 41.65, 65.65, and 27.29 for the three rule-based protocols.

**Caveats/Scope:** The audit is based on MATH and measures agreement with manual checks; it does not prove that LLM-as-judge evaluation is always reliable or unbiased.

**Source pointers:** `paper.pdf`, Section 3.2; Table 4

## Claim 4
**Claim:** Broad MAS benchmark results do not identify one universally dominant general-purpose method.

**Evidence:** Table 2 compares general methods across mathematics, science, knowledge, medicine, and coding benchmarks using Llama-3.3-70B-Instruct and Qwen-2.5-72B-Instruct. The authors explicitly observe that no method rules all domains, and that backend model choice changes the performance landscape.

**Caveats/Scope:** The benchmark suite is broad but mostly built from existing LLM benchmarks, which the limitations section notes are not specifically designed for MAS.

**Source pointers:** `paper.pdf`, Section 4.1; Table 2; Appendix A

## Claim 5
**Claim:** Tool access is a major factor for MAS performance on GAIA-style assistant tasks.

**Evidence:** Section 4.1 and Figure 7 report that tool-augmented methods outperform single-agent and tool-less MAS baselines on GAIA. Table 5 shows ReAct-MASLab achieving the best overall GPT-4.1 result while using fewer tokens per query than OWL-Roleplaying.

**Caveats/Scope:** These results depend on the paper's GAIA validation-set setup, tool suite, and operation limits; tool instability is also identified as a failure source.

**Source pointers:** `paper.pdf`, Section 4.1; Figure 7; Table 5; Section C.2

## Claim 6
**Claim:** MAS reliability depends on more than reasoning quality; formatting and tool-use failures are substantial bottlenecks.

**Evidence:** The scaling analysis finds that smaller Qwen backends can fail to follow required interaction formats, and Table 3 attributes large fractions of AgentVerse failures to format errors. The GAIA failure analysis for OWL-Roleplaying reports many failures from tool usage rather than only incorrect final answers.

**Caveats/Scope:** The format-error table focuses on AgentVerse with Qwen-2.5-14B-Instruct, and the tool-error analysis focuses on OWL-Roleplaying with GPT-4.1 on GAIA.

**Source pointers:** `paper.pdf`, Sections 4.2 and 4.3; Table 3; Figure 10
