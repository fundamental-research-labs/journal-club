# Claims

## Claim 1
**Claim:** TheAgentCompany provides a self-hosted software-company environment for evaluating agents on realistic digital workplace workflows.

**Evidence:** The benchmark includes a local Docker workspace plus an intranet with GitLab, ownCloud, Plane, and RocketChat. It also includes simulated colleagues that agents can message for information needed to complete tasks.

**Caveats/Scope:** The company is fictional and non-embodied, and the environment is a simplified web-based workplace rather than a full enterprise deployment.

**Source pointers:** `paper.pdf`, Abstract; Section 3; Figure 1; Appendix G

## Claim 2
**Claim:** The benchmark covers multiple workplace roles and evaluates progress through checkpointed tasks rather than only final answers.

**Evidence:** Tasks include intents, checkpoints, evaluators, and setup/finalization code. The 175 tasks span software engineering, project management, data science, administration, HR, finance, and other categories, with full-completion and partial-completion metrics.

**Caveats/Scope:** The task set is curated rather than a representative labor-market sample, and the authors explicitly caution against inferring whole-job automation from the benchmark alone.

**Source pointers:** `paper.pdf`, Sections 4-5; Appendix B; Table 5; Appendix J

## Claim 3
**Claim:** Current baseline agents solve only a minority of TheAgentCompany tasks end to end.

**Evidence:** The strongest reported run, OpenHands 0.28.1 with Gemini-2.5-Pro, reaches 30.3% full completion and a 39.3% partial-completion score on the 175-task set. Claude-3.7-Sonnet is close behind but still below one-third full completion.

**Caveats/Scope:** These numbers are for the tested model versions, agent scaffolds, step budgets, and benchmark version in the local PDF; future agents may differ.

**Source pointers:** `paper.pdf`, Abstract; Section 7.1; Table 1

## Claim 4
**Claim:** Social interaction and complex workplace web interfaces are major failure points for the evaluated agents.

**Evidence:** The platform breakdown shows low performance on RocketChat and ownCloud tasks, and the error analysis highlights missed social implications in conversations and difficulty navigating modern web UIs.

**Caveats/Scope:** The result depends on the tested browsing interfaces and simulated-colleague setup; multimodal or UI-specialized agents may shift the failure profile.

**Source pointers:** `paper.pdf`, Section 7.2; Table 4; Section 7.3; Appendix H

## Claim 5
**Claim:** Agent success does not track human-perceived occupational difficulty in a simple way.

**Evidence:** The paper reports higher success on software-engineering and project-management tasks than on data-science, administrative, and finance tasks, and attributes some of the gap to document handling, communication, complex UIs, repetitive workflows, and limited public training data for private enterprise tasks.

**Caveats/Scope:** Some categories have small task counts, and the paper did not collect human-professional performance data for direct comparison.

**Source pointers:** `paper.pdf`, Section 7.2; Figure 2; Table 5; Appendix J

## Claim 6
**Claim:** The benchmark relies partly on LLM-based evaluators and simulated colleagues, but the paper scopes and audits those components.

**Evidence:** The paper states that 51 tasks use LLM evaluation, mainly as a fallback or supplement to deterministic checks, and that evaluators were reviewed and tested. It also reports an audit of early simulated-colleague tasks that found one role-play prompt ambiguity, which was fixed.

**Caveats/Scope:** LLM judges and simulated colleagues can still introduce errors or distribution shift, so claims based on those tasks should be read with that dependency in mind.

**Source pointers:** `paper.pdf`, Section 4; Appendix E; Appendix F; Appendix J
