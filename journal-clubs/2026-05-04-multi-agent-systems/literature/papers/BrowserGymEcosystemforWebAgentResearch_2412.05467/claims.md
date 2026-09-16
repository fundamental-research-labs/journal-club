# Claims

## Claim 1: BrowserGym unifies diverse web-agent benchmarks behind one environment API.

**Evidence:** The paper describes BrowserGym as a Gymnasium-compatible interface with common observation/action loops, task registration, benchmark metadata, and backend preparation. Table 1 lists the integrated benchmark families: MiniWoB, WebArena, VisualWebArena, WorkArena L1/L2/L3, WebLINX, and AssistantBench.

**Caveats/Scope:** The interface standardizes evaluation plumbing, but individual benchmarks still differ in task semantics, backends, stochasticity, and validation methods.

**Source pointers:** `paper.pdf`, Sections 3 and 4; Figure 3; Table 1.

## Claim 2: BrowserGym gives web agents richer and more controllable browser interaction channels than a single raw representation.

**Evidence:** The observation space includes task goals or chat history, open tabs, DOM, accessibility tree, screenshots, element IDs, bounding boxes, visibility indicators, Set-of-Marks metadata, and last-action error feedback. The action space can be raw Python/Playwright or constrained through action mappings and high-level primitives.

**Caveats/Scope:** Rich observations do not guarantee better agent performance; agents must still choose how to filter, format, and use the available information within model context limits.

**Source pointers:** `paper.pdf`, Sections 3.1 and 3.2; Figures 4-6; Appendix A, Table 3.

## Claim 3: AgentLab is designed to make large-scale web-agent experiments reproducible and inspectable.

**Evidence:** AgentLab introduces Study objects for organizing runs, parallel execution through ray or joblib, relaunching failed tasks, AgentXRay for trace inspection, reproducibility metadata, a reproducibility journal, leaderboard support, and a ReproducibilityAgent that replays action sequences to detect environment drift.

**Caveats/Scope:** The paper is careful that reproducibility remains limited by external factors such as live websites, package changes, API model updates, operating systems, browser rendering, and stochastic tasks.

**Source pointers:** `paper.pdf`, Sections 5.1-5.4 and 7.1; Figure 9.

## Claim 4: A unified ecosystem enables multi-benchmark model comparisons that would be cumbersome with separate benchmark codebases.

**Evidence:** The authors run AgentLab's GenericAgent with six LLM/VLM backbones across the BrowserGym benchmark suite and report consolidated success rates, episode counts, costs, and average steps. The discussion argues that the same experiment would be difficult using the original fragmented benchmark implementations.

**Caveats/Scope:** The comparison depends on one default agent configuration, specific model checkpoints and APIs, benchmark-specific skips or inherited results, and the selected task splits/settings.

**Source pointers:** `paper.pdf`, Sections 6.1, 6.2, and 7; Table 2; Appendix E, Table 5.

## Claim 5: Current general web agents remain far from robust across difficult browser tasks.

**Evidence:** Table 2 shows low success rates on several hard settings, including WorkArena L3, AssistantBench, and WorkArena L2 for most non-Claude models. The error section identifies recurring navigation, form-handling, task-understanding, stuck-behavior, extraction, and external-system failures.

**Caveats/Scope:** These failures are reported for GenericAgent and the evaluated model checkpoints; specialized agents or later models may behave differently.

**Source pointers:** `paper.pdf`, Sections 6.2 and 6.3; Table 2; Appendix H.

## Claim 6: Web-agent benchmark standardization must still contend with safety and operational constraints.

**Evidence:** The limitations section discusses reproducibility problems from localization and dynamic web content, risks from letting agents act on the open web, robot detection on open-web tasks, database collisions between concurrent agents, and synchronous browser-loop bottlenecks.

**Caveats/Scope:** BrowserGym mitigates some issues, such as URL protections for several benchmarks and warnings, but does not solve the broader deployment safety problem.

**Source pointers:** `paper.pdf`, Sections 7.1, 7.2, and 8.
