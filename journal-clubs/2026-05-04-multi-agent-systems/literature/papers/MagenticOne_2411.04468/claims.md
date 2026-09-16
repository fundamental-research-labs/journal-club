# Claims

## Claim 1
**Claim:** Magentic-One frames generalist task solving as a centralized, ledger-driven multi-agent workflow rather than as one monolithic tool-using agent.

**Evidence:** The Orchestrator maintains a task ledger for facts, guesses, and plans and a progress ledger for step-by-step routing, progress checks, loop detection, and completion decisions. It directs four tool-centric worker agents: WebSurfer, FileSurfer, Coder, and ComputerTerminal.

**Caveats/Scope:** This is an architecture claim and does not by itself prove that centralized orchestration is always superior to peer-to-peer or single-agent designs.

**Source pointers:** `paper.pdf`, Figure 2; Section 4.1; Section 4.2

## Claim 2
**Claim:** Magentic-One is presented as a generalist system because the same core agent team is evaluated across GAIA, AssistantBench, and WebArena.

**Evidence:** Section 5.1 states that an identical Magentic-One configuration was used for all three benchmarks, with benchmark-specific final prompts and setup code. Section 5.2 argues that no prior non-base-model baseline in Table 1 had been evaluated across all three benchmarks.

**Caveats/Scope:** The setup is not perfectly benchmark-agnostic: each benchmark uses its own answer-format prompt, and WebArena needs login/setup prompts and site-specific clarifications.

**Source pointers:** `paper.pdf`, Section 5.1; Section 5.2; Table 1

## Claim 3
**Claim:** The reported benchmark results place Magentic-One near state-of-the-art systems on the evaluated agentic benchmarks, but not uniformly above them.

**Evidence:** Table 1 reports 38.0% GAIA and 13.3 exact match / 27.7 accuracy on AssistantBench for the GPT-4o/o1-preview variant, with statistical comparability to the SOTA methods considered. The GPT-4o-only variant reports 32.8% on WebArena, comparable to most SOTA methods but statistically below WebPilot and Jace.AI.

**Caveats/Scope:** Baselines are leaderboard results as of October 21, 2024; some are not open-source or independently described. WebArena lacks a hidden test set, and the o1-preview variant is not reported for WebArena because refusal behavior made comparison unfair.

**Source pointers:** `paper.pdf`, Section 5.2; Table 1; Appendix A

## Claim 4
**Claim:** The ledger-based Orchestrator and each worker agent contribute measurably to performance in the authors' ablation study.

**Evidence:** On GAIA validation, replacing the Orchestrator with a simple GroupChat controller reduces performance, and removing any single worker agent also reduces performance. The paper reports a 31% drop without full ledgers and 21% to 39% drops when individual worker agents are removed.

**Caveats/Scope:** The ablations are on GAIA validation tasks with the GPT-4o configuration, so the magnitude may not transfer to AssistantBench, WebArena, other models, or other task distributions.

**Source pointers:** `paper.pdf`, Section 5.3; Figure 3

## Claim 5
**Claim:** Magentic-One's major observed failure modes are inefficient persistence, insufficient verification, and navigation errors rather than only missing tool access.

**Evidence:** The automated log analysis identifies persistent-inefficient-actions, insufficient-verification-steps, and inefficient-navigation-attempts as the top error codes across validation logs, with underutilized resources and neglected errors also appearing frequently.

**Caveats/Scope:** The error codes are derived through GPT-4o-assisted qualitative coding of logs, not a fully manual or externally validated taxonomy; they describe observed benchmark runs, not all possible deployments.

**Source pointers:** `paper.pdf`, Section 5.4; Figure 4; Appendix C

## Claim 6
**Claim:** AutoGenBench is intended to make agentic evaluation more rigorous by controlling stateful side effects.

**Evidence:** AutoGenBench starts each task from fresh Docker containers, keeps logs on the host machine, supports repeated runs and parallel execution, and is motivated by examples where previous agent actions could install packages, delete files, or otherwise bias later runs.

**Caveats/Scope:** The tool addresses experimental isolation and logging, but the paper notes that the benchmarks still focus mainly on final-answer accuracy and do not fully capture cost, latency, user value, or subjective task quality.

**Source pointers:** `paper.pdf`, Section 5.1; Section 6.2
