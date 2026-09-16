# Claims

## Claim 1
**Claim:** Agent Forest improves accuracy over single-query inference across the paper's evaluated tasks and non-GPT-4 backbones.

**Evidence:** Table 2 and Figure 3 compare single-query results to Agent Forest at ensemble size 40 for Llama2-13B, Llama2-70B, and GPT-3.5-Turbo on GSM8K, MATH, Chess, MMLU, and HumanEval; every listed "Ours" score is higher than the corresponding "Single" score. Appendix Table 7 reports one-way ANOVA p-values below 0.05 across ensemble sizes.

**Caveats/Scope:** GPT-4 is included only as a single-query comparison, not as an Agent Forest backbone in Table 2. The result is benchmark accuracy under the authors' extraction and voting rules, not a claim about all agent tasks.

**Source pointers:** `paper.pdf`, Abstract; Section 3; Section 5.1; Figure 3; Table 2; Appendix B.2/Table 7

## Claim 2
**Claim:** A sufficiently large smaller-model ensemble can sometimes outperform a larger model queried once.

**Evidence:** On GSM8K, Table 2 reports Llama2-13B with Agent Forest at 0.59 accuracy versus single-query Llama2-70B at 0.54; Figure 1 presents the same qualitative point as ensemble size increases.

**Caveats/Scope:** This is not universal across tasks or model pairs. It also ignores latency and token-cost differences between many smaller calls and one larger-model call.

**Source pointers:** `paper.pdf`, Figure 1; Section 5.1; Table 2

## Claim 3
**Claim:** Agent Forest is largely orthogonal to prompting and multi-agent collaboration methods because it can be layered on top of them.

**Evidence:** Table 3 evaluates CoT, Zero-Shot CoT, SPP, Debate, and Reflection standalone and with Agent Forest; most "+Ours" entries improve over the standalone method, and Section 5.2 summarizes improvements across arithmetic, general reasoning, and code tasks.

**Caveats/Scope:** The paper reports notable failures when combining Debate with Llama2 on HumanEval, attributing them to noisy references to other agents' answers disrupting code logic. Debate experiments also use a smaller maximum ensemble size because of computational overhead.

**Source pointers:** `paper.pdf`, Section 4; Section 5.2; Table 3; Figures 8-13

## Claim 4
**Claim:** Agent Forest's relative benefit depends on task difficulty and model strength rather than being a fixed additive gain.

**Evidence:** Table 6 shows higher relative gains on MATH than GSM8K and larger gains for Llama2-13B than GPT-3.5-Turbo. Section 6 then isolates three difficulty dimensions and reports that gains increase then decrease with inherent difficulty, increase with the number of reasoning steps, and that absolute performance rises with the prior probability of the correct answer.

**Caveats/Scope:** The detailed difficulty analysis uses controlled synthetic math tasks, mainly with GPT-3.5-Turbo, so the properties are suggestive mechanisms rather than universal laws.

**Source pointers:** `paper.pdf`, Section 6; Table 6; Figure 6

## Claim 5
**Claim:** Step-wise and hierarchical variants can improve over flat Agent Forest when task structure exposes intermediate steps or easier subproblems.

**Evidence:** Section 6.3 proposes Step-wise Agent Forest after observing per-step error accumulation, and Figure 7 reports larger gains than flat Agent Forest in the controlled multi-step setting. Section 6.4 proposes Hierarchical Agent Forest; in the reported K=32 task, the homogeneous hierarchy improves accuracy from 21% to 31%, and the heterogeneous GPT-3.5/GPT-4 hierarchy improves from 35% to 47%.

**Caveats/Scope:** These variants are evaluated on designed mathematical tasks, not the full benchmark suite. They require usable task decomposition or intermediate answers.

**Source pointers:** `paper.pdf`, Section 6.3; Section 6.4; Figure 7

## Claim 6
**Claim:** The method's main practical cost is proportional growth in token usage with ensemble size.

**Evidence:** Section 5.5 states that token usage increases proportionally with the number of agents or method executions; Table 5 gives single-agent token usage by task and method, and Figure 14 plots token budget against accuracy.

**Caveats/Scope:** The paper frames cost optimization as future work. It does not provide a full economic analysis across providers, batching strategies, latency constraints, or smaller-model deployment costs.

**Source pointers:** `paper.pdf`, Section 5.5; Table 5; Figure 14; Section 7
