# Claims

## Claim 1: SWE-bench turns real GitHub issue resolution into executable model evaluation.

**Evidence:** The benchmark is constructed from merged pull requests that resolve issues, add tests, and pass an execution-based filter requiring at least one fail-to-pass test after the reference solution is applied. Model predictions are evaluated by applying generated patches to the original codebase and running the relevant tests.

**Caveats/Scope:** The local paper's benchmark covers Python repositories selected from popular PyPI packages; the authors discuss extending the collection process to other languages and domains as future work.

**Source pointers:** `paper.pdf`, Section 2.1, Section 2.2, Appendix A.1-A.4, Figure 1, Figure 2, Figure 8

## Claim 2: SWE-bench is substantially more repository-scale than short code-generation benchmarks.

**Evidence:** The paper reports 2,294 task instances across 12 repositories, with average non-test codebases of 3,010 files and 438K lines. Reference solutions average edits across 1.7 files, 3.0 functions, and 32.8 lines, and issue statements average 195 words.

**Caveats/Scope:** These are aggregate statistics for the curated SWE-bench set, not a claim that every instance is large or multi-file.

**Source pointers:** `paper.pdf`, Section 2.3, Figure 3, Table 1, Appendix Table 10

## Claim 3: Contemporary language models solve only a small fraction of SWE-bench tasks in baseline settings.

**Evidence:** In the BM25 retrieval setting in the local PDF, full SWE-bench resolve rates are low across evaluated models: Claude 3 Opus is 3.79%, Claude 2 is 1.97%, GPT-4-turbo is 1.31%, ChatGPT-3.5 is 0.17%, and SWE-Llama variants are 0.70%.

**Caveats/Scope:** These results are for the paper's prompting, retrieval, patch-generation format, model versions, and evaluation harness; later agentic systems may perform differently.

**Source pointers:** `paper.pdf`, Section 5, Table 5

## Claim 4: Code localization is a central bottleneck, not just context-window size.

**Evidence:** BM25 recall of oracle files rises with larger maximum context, but model resolution can decrease as more context is included. Oracle retrieval and oracle-collapsed retrieval improve results, indicating that knowing where to edit and avoiding irrelevant context both matter.

**Caveats/Scope:** The evidence comes from BM25 and oracle-style ablations; it does not rule out stronger retrieval, search, tool use, or agentic localization methods.

**Source pointers:** `paper.pdf`, Section 4.1, Section 5, Table 2, Table 3, Table 6, Figure 5, Appendix Table 18

## Claim 5: SWE-Llama demonstrates a path for open repository-editing models but also reveals distribution-shift sensitivity.

**Evidence:** The authors fine-tune CodeLlama-Python 7B and 13B models on 19,000 issue-PR pairs from 37 disjoint repositories, but note that SWE-Llama performs poorly under BM25 retrieval after being trained with oracle-retrieved files.

**Caveats/Scope:** The training corpus is separate from the evaluation repositories, and the reported models use the paper's LoRA fine-tuning setup and context construction.

**Source pointers:** `paper.pdf`, Section 3, Section 5, Appendix B, Table 5, Appendix Table 18

## Claim 6: Passing the target tests is not equivalent to human-quality maintenance.

**Evidence:** The qualitative analysis finds generated patches are often greedy and narrow, and Table 8 shows applied model patches are much shorter than corresponding gold patches. The discussion explicitly warns that execution-based testing alone cannot guarantee comprehensiveness, efficiency, or readability.

**Caveats/Scope:** The benchmark's primary metric remains test-based issue resolution; broader code quality is analyzed qualitatively rather than used as the main score.

**Source pointers:** `paper.pdf`, Section 5.1, Section 7, Table 8, Figure 6
