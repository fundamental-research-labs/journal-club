# Claims

## Claim 1
**Claim:** Encoding software-development SOPs gives LLM agents a more reliable collaboration structure than free-form multi-agent dialogue.

**Evidence:** MetaGPT defines Product Manager, Architect, Project Manager, Engineer, and QA Engineer roles, then routes work through PRDs, system designs, task assignments, code, and QA artifacts. The paper argues that these structured intermediate outputs reduce ambiguity, irrelevant chatter, and cascading hallucinations.

**Caveats/Scope:** This is partly a design claim. The paper supports it with downstream results and role ablations, but it does not isolate every SOP component in a large controlled experiment.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3.1; Figures 1 and 3

## Claim 2
**Claim:** MetaGPT improves single-attempt code-generation performance on HumanEval and MBPP in the reported GPT-4 setup.

**Evidence:** Figure 4 reports MetaGPT at 85.9% Pass@1 on HumanEval and 87.7% Pass@1 on MBPP, above the compared code LLMs and GPT-4 baselines in the figure.

**Caveats/Scope:** The experiments modify prompts to match response-format requirements, and HumanEval/MBPP are function-level coding benchmarks rather than full software-engineering projects.

**Source pointers:** `paper.pdf`, Section 4.1; Section 4.2; Figure 4; Appendix Table 7

## Claim 3
**Claim:** On the paper's SoftwareDev project-generation tasks, MetaGPT produces more executable outputs than the compared autonomous-agent frameworks.

**Evidence:** Table 1 reports higher executability and lower human revision cost for MetaGPT than ChatDev in the main SoftwareDev comparison. Appendix Table 4 reports an average executability score of 3.9 for MetaGPT versus 2.1 for ChatDev and 1.0 for AutoGPT, LangChain, and AgentVerse across seven representative tasks.

**Caveats/Scope:** SoftwareDev is a self-generated benchmark of 70 tasks, and the main comparison uses seven representative tasks with human-scored executability. Results should not be read as a broad production-readiness guarantee.

**Source pointers:** `paper.pdf`, Section 4.1; Section 4.2; Table 1; Appendix C.1; Appendix Table 4; Appendix Table 8

## Claim 4
**Claim:** Role specialization is a functional contributor, not just presentation.

**Evidence:** The role ablation in Table 3 shows engineer-only generation has executability 1.0 and high revision cost, while adding Product Manager, Architect, and Project Manager reaches executability 4.0 and reduces revisions.

**Caveats/Scope:** The ablation uses two tasks and increasing roles also increases expense, so the result is directional rather than a universal scaling rule for arbitrary agent teams.

**Source pointers:** `paper.pdf`, Section 4.3; Section 4.4; Table 3

## Claim 5
**Claim:** Executable feedback improves MetaGPT beyond structured handoffs alone.

**Evidence:** Section 3.3 defines a loop where the Engineer writes tests, runs code, observes execution results, and debugs until tests pass or retries are exhausted. Section 4.4 reports gains of 4.2 Pass@1 points on HumanEval and 5.4 points on MBPP from adding executable feedback; Table 1 also shows lower human revision cost versus MetaGPT without feedback.

**Caveats/Scope:** The mechanism depends on tasks where useful execution or tests are available, and the paper caps retries at three. It may not catch semantic errors that do not surface in the available tests.

**Source pointers:** `paper.pdf`, Section 3.3; Section 4.4; Figure 4; Table 1; Appendix Table 9
