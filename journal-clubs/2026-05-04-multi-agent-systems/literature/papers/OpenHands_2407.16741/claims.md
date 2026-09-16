# Claims

## Claim 1: OpenHands provides an integrated runtime for software-using agents.
**Claim:** The platform gives agents a developer-like action space by combining an event stream, executable actions, and a Docker-sandboxed runtime with bash, IPython, and browser control.

**Evidence:** The architecture section defines state as an event stream of actions and observations, describes `CmdRunAction`, `IPythonRunCellAction`, and browser actions, and explains that actions execute inside a Docker sandbox through an OpenHands action execution API.

**Caveats/Scope:** This is a platform-design claim, not proof that any particular agent reliably completes long-horizon tasks. Security and reliability still depend on sandbox configuration, model behavior, and task setup.

**Source pointers:** `paper.pdf`, Abstract; Figure 2; Section 2.1; Section 2.2; Appendix F.

## Claim 2: OpenHands is designed to be extensible across agent implementations and tools.
**Claim:** The agent abstraction, AgentSkills library, and AgentHub make OpenHands a reusable platform rather than a single hard-coded agent.

**Evidence:** Section 2.1 gives a minimal agent implementation pattern, Section 2.3 describes reusable Python-based skills such as file editing and document parsing, and Section 3 describes community-contributed agents including CodeActAgent, BrowsingAgent, GPTSwarm, and micro agents.

**Caveats/Scope:** Extensibility is shown by implementation examples and included agents; the paper does not quantify how easy third-party extension is across independent users or large organizations.

**Source pointers:** `paper.pdf`, Section 2.1; Section 2.3; Section 3; Table 1.

## Claim 3: Multi-agent collaboration is supported as a delegation primitive.
**Claim:** OpenHands can compose specialized agents by allowing a generalist agent to delegate subtasks to another agent.

**Evidence:** Section 2.4 introduces `AgentDelegateAction`, with the example of CodeActAgent delegating complex web-browsing work to BrowsingAgent; the WebArena results also report CodeActAgent v1.8 via delegation to BrowsingAgent.

**Caveats/Scope:** The paper shows platform support for delegation, but it does not establish that multi-agent delegation is generally superior to single-agent execution across tasks.

**Source pointers:** `paper.pdf`, Section 2.4; Section 3; Table 5.

## Claim 4: OpenHands integrates a broad benchmark suite for generalist digital agents.
**Claim:** The platform includes evaluation support for software engineering, web browsing, and miscellaneous assistance benchmarks.

**Evidence:** Table 2 lists 15 benchmarks, including SWE-Bench, HumanEvalFix, BIRD, BioCoder, ML-Bench, Gorilla APIBench, ToolQA, WebArena, MiniWoB++, GAIA, GPQA, AgentBench, MINT, Entity Deduction Arena, and ProofWriter.

**Caveats/Scope:** Some evaluations use subsets, modified settings, or cost-saving choices, so benchmark coverage should not be read as exhaustive validation on every full benchmark.

**Source pointers:** `paper.pdf`, Section 4; Table 2; Tables 4-6.

## Claim 5: OpenHands agents are evaluated as generalists and can be competitive, but not state of the art everywhere.
**Claim:** The same OpenHands agent family is shown working across software, web, and assistance tasks, while the paper explicitly notes that it may not top every category.

**Evidence:** Table 3 reports CodeActAgent v1.8 results across SWE-Bench Lite, WebArena, and GPQA; Table 4 reports SWE-Bench Lite and other software-task results; Tables 5 and 6 cover web and assistance benchmarks. The overview states that the same CodeAct agent runs without system-prompt modifications across major categories.

**Caveats/Scope:** Results are model-, version-, prompt-, and benchmark-setting-dependent. The strongest numbers vary by task, and several specialist baselines remain ahead on their own benchmarks.

**Source pointers:** `paper.pdf`, Section 4.1; Table 3; Table 4; Table 5; Table 6.

## Claim 6: The paper frames OpenHands as an open community artifact with engineering quality controls.
**Claim:** OpenHands is positioned as an open-source platform intended for research and practical agent development, with community scale and tests as part of the contribution.

**Evidence:** The abstract and introduction report a permissive MIT license, more than 2.1K contributions, over 188 contributors, and 32K GitHub stars. Appendix E describes integration tests that mock LLM responses and test prompts, actions, and sandbox behavior.

**Caveats/Scope:** Community statistics are a snapshot from the paper, and engineering quality controls reduce but do not eliminate regressions or benchmark instability.

**Source pointers:** `paper.pdf`, Abstract; Introduction; Appendix E.
