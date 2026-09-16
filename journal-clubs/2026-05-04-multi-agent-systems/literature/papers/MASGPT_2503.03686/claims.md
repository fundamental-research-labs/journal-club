# Claims

## Claim 1: MAS construction can be framed as a language generation task.

**Claim:** MAS-GPT turns the problem of building an LLM-based multi-agent system into a text-to-code generation task: the input is a user query and the output is executable MAS code.

**Evidence:** The paper defines MAS as a Python `forward` function where agent prompts are variables, LLM calls are function calls, and relationships among agents are string concatenations. Figures 2 and 3 illustrate the executable representation and the training/inference pipeline.

**Caveats/Scope:** The executable representation is a simplification of MAS design; it is best suited to prompt-level agent composition and does not by itself solve tool integration, memory, safety, or runtime reliability.

**Source pointers:** `paper.pdf`, Abstract; Section 3.1; Section 3.2; Figure 2; Figure 3.

## Claim 2: Consistency-oriented data construction is central to training MAS-GPT.

**Claim:** The paper's dataset pipeline is designed to make query-MAS pairs both effective and learnable by enforcing consistency across similar queries and within each query-MAS pair.

**Evidence:** The pipeline constructs query and MAS pools, evaluates query-MAS compatibility, selects high-performing MAS for groups of similar queries, and refines selected MAS to better align with the query. Table 1 reports 11,442 training samples and 7,580 unique MAS variants.

**Caveats/Scope:** The pipeline depends on automatic evaluation, clustering/grouping, LLM-based refinement, and the quality of the initial MAS pool; errors in any stage can become training signal.

**Source pointers:** `paper.pdf`, Section 3.2; Table 1; Table 10; Table 11.

## Claim 3: MAS-GPT improves average benchmark performance over the tested baselines.

**Claim:** In the paper's main comparison, MAS-GPT outperforms more than 10 single-agent and multi-agent baselines on average across diverse benchmarks.

**Evidence:** Table 2 reports MAS-GPT as the best average performer across eight benchmarks using Llama-3-70B-Instruct as the MAS-driving model. Table 3 reports the best average score with Qwen2.5-72B-Instruct and GPT-4o-mini drivers.

**Caveats/Scope:** Improvements are benchmark- and setup-specific. Some individual benchmark columns are not won by MAS-GPT, and several evaluations rely on LLM-based answer extraction or judgment for non-code tasks.

**Source pointers:** `paper.pdf`, Section 4.1; Section 4.2; Table 2; Table 3; Appendix C.2.

## Claim 4: One-inference MAS generation can reduce inference-time construction cost.

**Claim:** MAS-GPT is intended to replace manual MAS design or iterative per-query MAS optimization with a single 32B-model inference that generates the MAS.

**Evidence:** The abstract, Figure 1, and Section 3 state that MAS-GPT generates a query-specific executable MAS in one inference. Figure 4(c) compares inference-call cost and reports MAS-GPT as the best performance/cost tradeoff among the plotted methods.

**Caveats/Scope:** This cost accounting excludes the one-time cost of dataset construction and fine-tuning, and it treats the MAS-GPT generation call as lower cost because the generator is smaller than the MAS-driving LLM.

**Source pointers:** `paper.pdf`, Abstract; Section 3.3; Figure 1; Figure 4(c).

## Claim 5: The reported gains depend on the data selection/refinement recipe and scale with training resources.

**Claim:** MAS-GPT's performance is not just a base-model capability; it depends on the proposed training data recipe and improves with more data and larger generators.

**Evidence:** Table 4 shows lower performance when inter-consistency selection, MAS adjustment, or reasoning-process refinement is removed. Figure 5 reports that more training data reduces extraction/execution failures and improves benchmark performance, while larger base models generally perform better.

**Caveats/Scope:** The scaling study is exploratory and limited to the paper's data, model sizes, and benchmarks; it does not establish a general law for all MAS generators.

**Source pointers:** `paper.pdf`, Section 4.3; Table 4; Figure 5.
