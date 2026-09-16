# Claims

## Claim 1
**Claim:** MIRROR improves StableToolBench tool-learning performance over the reported planning, reflection, multi-agent, and supervised fine-tuning baselines across the tested LLM cores.

**Evidence:** Table 1 reports MIRROR as the strongest average method for GPT-3.5 Turbo, Claude 3 Haiku, Qwen2.5-72B, and GPT-4o. Section 4.2 states that average Pass Rate gains over the next best method range from 2.5 to 7.0 points, while ToolLlama-2 and ToolGen supervised fine-tuning baselines remain around 46% average Pass Rate.

**Caveats/Scope:** The result is specific to StableToolBench, the tested LLM cores, the listed baselines, and the paper's evaluation setup. Win Rate uses GPT-4 Turbo as an evaluator against GPT-3.5+ReAct, so it is partly judge-model dependent.

**Source pointers:** `paper.pdf`, Section 4.2 and Table 1.

## Claim 2
**Claim:** MIRROR improves TravelPlanner delivery and constraint satisfaction over ReAct, but it does not solve full plan feasibility.

**Evidence:** Table 2 shows MIRROR ahead of ReAct on Delivery Rate, Commonsense Pass Rate, and Hard Constraint Pass Rate for GPT-4o Mini, Qwen2.5-72B, and GPT-4o. The same section explicitly notes that Final Pass Rate remains challenging, with very low final feasibility scores even under MIRROR.

**Caveats/Scope:** The TravelPlanner evaluation uses the validation set in a two-stage mode due to computational constraints, not the full test set. The claim should be read as an improvement in partial planning metrics rather than reliable end-to-end travel planning.

**Source pointers:** `paper.pdf`, Sections 4.1-4.2, Table 2, Appendix A, and Appendix B.

## Claim 3
**Claim:** Intra-reflection before execution or handoff is a meaningful contributor to MIRROR's gains.

**Evidence:** Table 3 reports that the full GPT-4o Mini MIRROR configuration reaches 85.7 average Pass Rate on StableToolBench. Removing Planner, Tool, or Answer Agent intra-reflection lowers the average to 82.1, 81.3, and 79.4 respectively; removing all intra-reflection lowers it to 78.7.

**Caveats/Scope:** This is an ablation on StableToolBench with GPT-4o Mini, so it does not isolate every possible prompt, threshold, model, or benchmark variant.

**Source pointers:** `paper.pdf`, Sections 3.4 and 4.3, Table 3, and Figure 3.

## Claim 4
**Claim:** Inter-reflection through short-term and long-term memory is also necessary for the reported framework performance.

**Evidence:** The method defines Short-Term Memory for local tool/parameter failure recovery and Long-Term Memory for full task-trajectory revision. Table 3 reports that removing inter-reflection lowers average Pass Rate from 85.7 to 80.5; removing long-term memory lowers it to 83.3, and removing short-term memory lowers it to 81.1.

**Caveats/Scope:** The memories are task-local, and the discussion states that this limits cross-task generalization. The ablation does not prove the same memory design is optimal outside the paper's tool-learning setup.

**Source pointers:** `paper.pdf`, Sections 3.5, 4.3, and 4.5; Table 3.

## Claim 5
**Claim:** MIRROR's reflection depth has an efficiency frontier rather than improving monotonically with more rounds.

**Evidence:** Section 4.3 reports five inter-reflection rounds as the best tested setting, reaching 85.7 Pass Rate at 13.6k tokens per query. Three rounds reduce Pass Rate to 83.4 at 12.8k tokens, while seven rounds increase token use to 17.2k and reduce Pass Rate to 82.3. Figure 4 also positions MIRROR as higher-performing than several baselines while using fewer tokens than DFSDT and Smurfs.

**Caveats/Scope:** Token costs and optimal round count are model- and implementation-dependent. The comparison is against the paper's selected baselines and settings, not a general theorem about reflection budgets.

**Source pointers:** `paper.pdf`, Section 4.3 and Figure 4.

## Claim 6
**Claim:** The prompt-based Tool Agent outperforms the tested function-calling replacement in this framework.

**Evidence:** Table 3 compares default MIRROR, which uses a prompt-based Tool Agent, with an FC configuration using function calling for the Tool Agent. The prompt-based configuration reaches 85.7 average Pass Rate, while FC reaches 83.2.

**Caveats/Scope:** This is a narrow Tool Agent strategy ablation. It does not imply that all function-calling APIs or future function-calling models are worse than prompting.

**Source pointers:** `paper.pdf`, Section 4.3 and Table 3.
