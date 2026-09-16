# Claims

## Claim 1
**Claim:** AgentCoder improves pass@1 over the zero-shot LLMs and optimization baselines evaluated in the paper.

**Evidence:** Table 1 reports the highest listed results for AgentCoder across HumanEval, HumanEval-ET, MBPP, and MBPP-ET. With GPT-4, AgentCoder reaches 96.3, 86.0, 91.8, and 91.8 pass@1 on those datasets; with GPT-3.5-turbo, its mean pass@1 is 84.1 versus 75.3 for the listed CodeCoT baseline.

**Caveats/Scope:** The evaluation is primarily on function-level Python benchmarks and uses pass@1. Some baseline numbers are taken from reported papers, so implementation and model-version differences may affect comparability.

**Source pointers:** Abstract; Section 4.2 "RQ1: How does AgentCoder perform?"; Table 1.

## Claim 2
**Claim:** The full programmer, test designer, and test executor loop is more effective than partial agent combinations.

**Evidence:** Table 2 shows the GPT-3.5-turbo ablation: programmer-only scores 61.0/52.4/47.9/35.0 on HumanEval/HumanEval-ET/MBPP/MBPP-ET, while full AgentCoder scores 79.9/77.4/89.9/89.1. The two partial pairings improve over programmer-only but remain well below the full system.

**Caveats/Scope:** This supports the paper's specific role design and prompts, not every possible multi-agent coding architecture.

**Source pointers:** Section 3 "Methodology"; Section 4.3 "RQ2"; Figure 1; Table 2.

## Claim 3
**Claim:** Iterative execution feedback improves AgentCoder within the tested repair budget.

**Evidence:** Table 3 reports monotonic gains from one to five iterations on all four GPT-3.5-turbo datasets, including HumanEval moving from 74.4 to 79.9 and MBPP-ET from 80.3 to 89.1 pass@1.

**Caveats/Scope:** The paper studies up to five iterations; it does not establish that more iterations would keep helping or that the same pattern holds for all models and tasks.

**Source pointers:** Section 3.3 "Test executor agent"; Section 4.4 "RQ3"; Table 3.

## Claim 4
**Claim:** AgentCoder's independent test designer generates more reliable tests than the compared test-generation baselines.

**Evidence:** Table 4 measures whether generated tests pass canonical solutions. AgentCoder with GPT-3.5-turbo scores 87.8 on HumanEval and 89.9 on MBPP, while direct GPT-3.5-turbo test generation scores 47.0 and 57.2 and CodeCoT scores 67.1 and 79.0. AgentCoder with GPT-4 also exceeds the MetaGPT GPT-4 comparison in the table.

**Caveats/Scope:** A test passing the canonical solution is a proxy for test correctness; it does not prove the test suite catches every relevant bug.

**Source pointers:** Section 3.2 "Test designer agent"; Section 4.5 "RQ4"; Table 4.

## Claim 5
**Claim:** AgentCoder's generated tests cover more canonical-solution lines than the compared test-generation methods.

**Evidence:** Table 5 reports line coverage of canonical solutions. AgentCoder with GPT-3.5-turbo covers 87.5 on HumanEval and 89.5 on MBPP, above CodeCoT's 77.2 and 82.9. AgentCoder with GPT-4 reaches 91.7 and 92.3, above the MetaGPT GPT-4 comparison.

**Caveats/Scope:** Line coverage measures execution coverage, not semantic adequacy, mutation score, or real-world test quality.

**Source pointers:** Section 4.6 "RQ5"; Table 5; Appendix A.3 Figures 2-5.

## Claim 6
**Claim:** Separating code generation and test design across agents is better than making one agent do both in one conversation.

**Evidence:** The single-agent-vs-multi-agent ablation reports higher pass@1 for the multi-agent setup in Table 7, higher test accuracy in Table 6, and higher test line coverage in Table 8. For example, HumanEval pass@1 is 71.3 for the single-agent setup and 79.9 for multiple agents.

**Caveats/Scope:** The single-agent baseline is the paper's particular code-then-test prompting setup, so stronger single-agent prompting or external tooling might narrow the gap.

**Source pointers:** Section 4.7 "RQ6"; Tables 6, 7, and 8.
