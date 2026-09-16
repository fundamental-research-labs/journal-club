# Claims

## Claim 1
**Claim:** ChatDev frames end-to-end software prototyping as a multi-agent communication problem rather than a single prompt-to-code generation step.

**Evidence:** The framework assigns LLM agents software roles and organizes them into a chat chain covering design, coding, code completion, review, and testing, with each subtask producing intermediate text or code that feeds later subtasks.

**Caveats/Scope:** The workflow is sequential and waterfall-like; it is aimed at prototype generation from text requirements, not arbitrary production software engineering workflows.

**Source pointers:** `paper.pdf`, Abstract; Section 3; Section 3.1; Figure 2.

## Claim 2
**Claim:** The chat-chain decomposition improves reported software quality over the evaluated single-agent and multi-agent baselines.

**Evidence:** In Table 1, ChatDev reports the best average completeness, executability, consistency, and combined quality scores compared with GPT-Engineer and MetaGPT on the authors' dataset.

**Caveats/Scope:** The metrics are proxy measures for generated software quality; the paper notes that general-purpose software evaluation is difficult and does not fully cover functionality, robustness, safety, or user-friendliness.

**Source pointers:** `paper.pdf`, Section 4; Section 4.1; Table 1; Section 6.

## Claim 3
**Claim:** Communicative dehallucination is presented as a mechanism for reducing coding hallucinations during review and testing.

**Evidence:** The method lets an assistant ask the instructor for more precise details before giving a final response, and the ablation removing this mechanism lowers completeness, executability, consistency, and quality relative to full ChatDev.

**Caveats/Scope:** The evidence is an ablation in the authors' setup; it does not isolate every possible cause of hallucination or prove the mechanism generalizes beyond the tested prompts, model, and tasks.

**Source pointers:** `paper.pdf`, Section 3.2; Section 4.2; Table 4.

## Claim 4
**Claim:** Role prompting is a major contributor to ChatDev's reported performance.

**Evidence:** The ablation without role assignments shows the largest quality drop among the reported component removals, and the authors' analysis says role prompts influence whether agents produce GUI-oriented implementations or specific bug-finding feedback.

**Caveats/Scope:** The result depends on the role prompts and task distribution used by ChatDev; it should not be interpreted as proving that any role assignment improves any agent system.

**Source pointers:** `paper.pdf`, Section 3.1; Section 4.2; Table 4.

## Claim 5
**Claim:** Different language modes play different roles in the development process.

**Evidence:** The communication analysis reports that natural-language design discussions support comprehensive system design, while programming-language communication in review and testing helps identify missing implementations, imports, exceptions, and runtime errors.

**Caveats/Scope:** This is an analysis of ChatDev dialogue traces and reviewer/tester categories, not a controlled linguistic study independent of the framework.

**Source pointers:** `paper.pdf`, Abstract; Section 4.3; Figures 3-5.

## Claim 6
**Claim:** ChatDev's outputs should be treated as prototype software rather than reliable production systems.

**Evidence:** The limitations section states that agents may implement simple logic with low information density, require clear detailed requirements, use more tokens and time than single-agent approaches, and are currently more suitable for prototype systems than complex real-world applications.

**Caveats/Scope:** This is the authors' own caution about the evaluated system; stronger models, tools, or verification pipelines could change the practical boundary.

**Source pointers:** `paper.pdf`, Section 6.
