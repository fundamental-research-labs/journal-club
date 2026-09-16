# Claims

## Claim 1: OSWorld provides a general real-computer environment for multimodal agents.
**Claim:** OSWorld is designed to evaluate agents in controllable VM-based computer environments rather than in static datasets or narrow simulated domains.

**Evidence:** The environment initializes tasks from configuration files, restores VM snapshots, exposes screenshots and accessibility trees, executes raw mouse and keyboard actions, and runs post-processing plus evaluation functions after the agent finishes. The paper states support for Ubuntu, Windows, and macOS, while the main benchmark is built on Ubuntu with a smaller Windows analytic set.

**Caveats/Scope:** The published benchmark is primarily Ubuntu-based; Windows is represented by 43 adapted tasks, and macOS support is described at the environment level rather than as a main evaluated benchmark.

**Source pointers:** `paper.pdf`, Abstract; Sec. 2.2; Fig. 1; Fig. 2; Sec. 3.1; Table 4

## Claim 2: The benchmark is broad and uses execution-based final-state evaluation.
**Claim:** OSWorld's benchmark covers a diverse set of realistic computer tasks and uses task-specific execution scripts to judge whether the final state satisfies the instruction.

**Evidence:** The benchmark has 369 Ubuntu tasks, including 268 single-app tasks, 101 multi-app workflow tasks, 30 infeasible tasks, 302 initial states, and 134 evaluation functions. The evaluation examples include checking cookies, comparing spreadsheet files, and inspecting accessibility-tree state.

**Caveats/Scope:** The tasks and evaluators are hand-authored and heavily quality-controlled, so coverage is broad but not exhaustive; final-state evaluators may still miss side effects or rare false positives/negatives.

**Source pointers:** `paper.pdf`, Sec. 2.2.3; Table 1; Sec. 3.2; Sec. 3.3; Table 3; App. B.4/Table 10

## Claim 3: Current LLM/VLM agents perform far below humans on OSWorld.
**Claim:** The evaluated language and vision-language agent baselines are not close to human performance on real computer tasks.

**Evidence:** Table 5 reports human performance of 72.36% overall, while the best reported model setting reaches 12.24% overall. Screenshot-only VLM settings for strong models are around 5-6% overall, and many category-level scores are much lower.

**Caveats/Scope:** Results reflect the model versions, prompts, input settings, action space, and 15-step limit used in the May 2024 paper; stronger later agents or different scaffolds may change absolute numbers.

**Source pointers:** `paper.pdf`, Sec. 3.4; Fig. 4; Sec. 4.1; Sec. 4.2; Table 5

## Claim 4: Cross-application workflow tasks are especially hard for agents.
**Claim:** Tasks that require coordination across multiple applications are harder for the evaluated agents than single-application tasks.

**Evidence:** OSWorld includes 101 workflow tasks, 27.4% of the Ubuntu benchmark. In the GPT-4V Set-of-Mark analysis, single-app tasks score 13.74% while multi-app workflow tasks score 6.57%; Table 5 also shows workflow success rates remaining low across baselines.

**Caveats/Scope:** The single-app versus workflow comparison is reported mainly for GPT-4V under the Set-of-Mark setting in Table 6, though Table 5 supports the broader pattern of low workflow performance.

**Source pointers:** `paper.pdf`, Sec. 3.3; Table 3; Sec. 4.2; Table 5; Sec. 5.1; Table 6

## Claim 5: Accessibility trees and Set-of-Mark prompting are useful but unreliable aids.
**Claim:** Structured UI metadata and visual marking can improve some agent settings, but OSWorld shows that they are not uniformly beneficial.

**Evidence:** The paper evaluates accessibility-tree-only, screenshot-only, screenshot-plus-a11y, and Set-of-Mark settings. Table 5 shows model-dependent gains and regressions, and Sec. 4.2 argues that desktop UI density, high resolution, and noisy element boxes can counteract the benefits of Set-of-Mark.

**Caveats/Scope:** The conclusion depends on the paper's specific accessibility-tree filtering, SoM implementation, models, and desktop apps; better parsers or UI abstractions could change the tradeoff.

**Source pointers:** `paper.pdf`, Sec. 2.3; Sec. 4.1; Sec. 4.2; Table 5; App. C.3; App. C.4

## Claim 6: GUI grounding and operational knowledge are core bottlenecks.
**Claim:** Many failures arise because agents can plan plausible high-level actions but cannot reliably ground them into precise GUI operations or application-specific procedures.

**Evidence:** The analysis reports that more than 75% of 550 sampled failed examples include mouse-click inaccuracies. Additional qualitative cases show repeated misclicks, trouble recovering from noisy windows or pop-ups, weak knowledge of professional software menus, and hallucinated details in desktop interactions.

**Caveats/Scope:** The common-error analysis is qualitative and sampled, with much of the deeper analysis focused on GPT-4V under Set-of-Mark; it should be read as diagnosis rather than a complete taxonomy for all agents.

**Source pointers:** `paper.pdf`, Sec. 5.2; Fig. 8; Sec. 5.4; Fig. 9; Fig. 10; App. D.2; App. D.4
