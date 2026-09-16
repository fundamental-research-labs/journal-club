# Claims

## Claim 1
**Claim:** AgentBench operationalizes LLM-as-agent evaluation as multi-round interaction across diverse environments rather than static question answering.

**Evidence:** The benchmark defines eight environments grouped as code-grounded, game-grounded, and web-grounded tasks, with each environment requiring the model to alternate observations and actions under task-specific metrics.

**Caveats/Scope:** The benchmark targets text-only prompted LLM agents; it does not cover multimodal embodied control or heavily scaffolded agents with search, reflection, or multiple rollouts.

**Source pointers:** `paper.pdf`, Section 2; Section 3; Figure 2; Table 2

## Claim 2
**Claim:** In the paper's evaluated model set, API-based commercial LLMs substantially outperform open-source LLMs on AgentBench.

**Evidence:** Table 3 reports GPT-4 (0613) as the strongest model with a 4.01 overall score, all API-based models above 1.00, and an average API score much higher than the OSS average; the best tested OSS model under 70B is CodeLlama-34B-Instruct at 0.96 overall.

**Caveats/Scope:** This is a snapshot of the models evaluated in the paper, mostly 2023-era systems plus later marked additions, and should not be generalized to current OSS models without re-running the benchmark.

**Source pointers:** `paper.pdf`, Table 3; Section 4.2; Figure 1; Figure 3

## Claim 3
**Claim:** Even the strongest evaluated model is not uniformly reliable as a practical agent.

**Evidence:** The paper states that even GPT-4 is not qualified as a practically usable agent, and Table 3 shows uneven GPT-4 performance across environments: strong House Holding and Digital Card Game results but much lower scores on tasks such as Lateral Thinking Puzzles and Web Browsing.

**Caveats/Scope:** The statement is based on GPT-4 (0613) under the benchmark's simple prompting setup and task limits; stronger scaffolding or newer models could change the result.

**Source pointers:** `paper.pdf`, Section 2; Table 3; Section 4.2

## Claim 4
**Claim:** AgentBench failures often reflect limits in long-horizon reasoning, format following, and action validity.

**Evidence:** The paper categorizes outcomes as Completed, Context Limit Exceeded, Invalid Format, Invalid Action, and Task Limit Exceeded. Table 4 shows Task Limit Exceeded as common across several tasks, Invalid Format concentrated in Database and Digital Card Game, and Invalid Action concentrated in House Holding and Web Browsing.

**Caveats/Scope:** These are coarse execution-outcome categories averaged over many models and tasks; they identify symptoms, not always the underlying cognitive cause.

**Source pointers:** `paper.pdf`, Section 2; Table 4; Section 4.3; Appendix J.1; Appendix J.2.1

## Claim 5
**Claim:** Code tuning has mixed effects on agent performance.

**Evidence:** The authors compare CodeLlama and Llama-2 families and argue that code tuning helps relatively procedural tasks such as Web Shopping but can hurt tasks requiring strategic reasoning or situational awareness, such as Digital Card Game and Operating System.

**Caveats/Scope:** This is an observational comparison between model families, not a controlled ablation of training data; architectural, alignment, and decoding differences may contribute.

**Source pointers:** `paper.pdf`, Section 4.3; Appendix J.2.5; Figure 10; Table 3

## Claim 6
**Claim:** High-quality alignment data appears important for agent behavior.

**Evidence:** The paper contrasts Vicuna-13B, aligned on ShareGPT data, with Llama-2-13B and reports stronger AgentBench performance for Vicuna-13B, comparable to the much larger CodeLlama-34B in overall score.

**Caveats/Scope:** The comparison is suggestive rather than causal because the models differ beyond the alignment-data source.

**Source pointers:** `paper.pdf`, Section 4.3; Table 3
