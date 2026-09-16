# Claims

## Claim 1: Agent-computer interfaces improve repository-level coding agents.

**Evidence:** SWE-agent defines an LM-specific ACI and reports stronger SWE-bench Lite performance than a Shell-only interactive agent using the same GPT-4 Turbo base model (18.00% vs. 11.00% resolved). It also exceeds the non-interactive RAG baselines on full SWE-bench and SWE-bench Lite.

**Caveats/Scope:** The main comparison is for the evaluated 2024 models, SWE-bench tasks, and a fixed per-instance cost budget; it does not prove that this exact interface is optimal for all coding agents or future models.

**Source pointers:** `paper.pdf`, Abstract; Section 4; Section 5; Table 1.

## Claim 2: The ACI framing treats commands and feedback format as first-class parts of an agent system.

**Evidence:** The paper defines an ACI as the available actions, action documentation, environment feedback, and history formatting between the LM and computer. SWE-agent implements this with search/navigation commands, a file viewer, a file editor, prompt/error templates, and context management.

**Caveats/Scope:** The design principles are derived from manual inspection, grid search, and SWE-bench-oriented engineering rather than a controlled theory of all possible digital interfaces.

**Source pointers:** `paper.pdf`, Section 2; Section 3; Appendix A.1; Table 4.

## Claim 3: Editing guardrails and compact editing actions materially affect performance.

**Evidence:** Table 3 reports that SWE-agent with GPT-4 Turbo reaches 18.0% on SWE-bench Lite with the full edit interface, dropping to 15.0% without linting and 10.3% without the edit command. The paper attributes these gaps to fewer silent edit failures, immediate file-view feedback, and rejection of selected syntax-breaking edits.

**Caveats/Scope:** The linting guardrail can constrain edit order, and the ablation is reported on SWE-bench Lite with GPT-4 Turbo rather than across every model and programming language.

**Source pointers:** `paper.pdf`, Section 3; Section 5.1; Table 3; Figure 6; Appendix A.1.

## Claim 4: Search, file viewing, and history presentation are performance-sensitive interface choices.

**Evidence:** Table 3 reports lower SWE-bench Lite performance for iterative search (12.0%) compared with summarized search (18.0%), for no search (15.7%), for 30-line or full-file viewers compared with a 100-line viewer, and for full history compared with keeping the last five observations.

**Caveats/Scope:** These are interface ablations within SWE-agent, so the exact magnitudes may depend on the task set, prompts, command implementation, and model behavior.

**Source pointers:** `paper.pdf`, Section 5.1; Table 3; Figure 5; Appendix A.1.

## Claim 5: SWE-agent's interface is portable across at least two long-context closed models.

**Evidence:** Although designed around GPT-4 Turbo, the same SWE-agent setup with Claude 3 Opus resolves 10.46% of full SWE-bench and 13.00% of SWE-bench Lite in Table 1. The experimental setup notes that smaller-context or weaker tested models performed poorly in the agent setting.

**Caveats/Scope:** Portability is shown for Claude 3 Opus and GPT-4 Turbo in the paper; it should not be generalized to all open-weight or shorter-context models.

**Source pointers:** `paper.pdf`, Abstract; Section 4; Section 5; Table 1.

## Claim 6: SWE-agent trajectories show recurring solve and failure patterns.

**Evidence:** Section 5.2 reports that solved trajectories commonly begin with reproduction or localization and then shift into edit-and-execute loops. For unresolved SWE-bench Lite trajectories, the authors' automated categorization finds many failures are incorrect or overly specific implementations, with failed-edit recovery also a major category.

**Caveats/Scope:** The failure-mode labels are produced by an LM-based classifier and validated on a small hand-labeled set, so they are best read as diagnostic categories rather than definitive causal proof.

**Source pointers:** `paper.pdf`, Section 5.2; Figure 7; Figure 8; Table 9; Appendix B.3-B.4.
