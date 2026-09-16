# Claims

## Claim 1
**Claim:** WebArena provides a realistic and reproducible web environment for autonomous web agents.

**Evidence:** The paper builds self-hosted, fully functional websites for e-commerce, forum discussion, software collaboration, and content management, plus tools and knowledge resources such as maps, a calculator, a scratchpad, offline Wikipedia, and user manuals. The sites are packaged with Docker images and reset scripts so evaluations can be rerun from deterministic starting states.

**Caveats/Scope:** The environment is still a curated replica with sampled data, selected domains, and bounded resources such as a northeast-US map and a Wikipedia snapshot, so it is more reproducible than the live web but not a complete substitute for it.

**Source pointers:** Abstract; Sec. 2; Sec. 2.2; Appendix A.1; Appendix A.2; Fig. 1

## Claim 2
**Claim:** WebArena evaluates functional task completion rather than only matching reference action traces.

**Evidence:** The benchmark provides 812 natural-language intents and task-specific reward functions. Information-seeking tasks use exact, must-include, or fuzzy semantic matching, while navigation and content/configuration tasks use programmatic checks over URLs, page contents, intermediate states, databases, APIs, or JavaScript-selected page elements.

**Caveats/Scope:** Some rewards are authored for specific task templates and some information-seeking evaluations use GPT-4 for fuzzy matching, so evaluator design and model-judge reliability remain part of the measurement.

**Source pointers:** Sec. 3; Sec. 3.1; Sec. 3.2; Table 1; Appendix A.7; Appendix A.8

## Claim 3
**Claim:** Contemporary prompt-based LLM agents were far below human performance on the benchmark.

**Evidence:** Table 2 reports human success at 78.24%. The best GPT-4-based baseline in the paper reaches 14.41% overall success; GPT-4 with chain-of-thought and the unachievable-task hint reaches 11.70%, GPT-3.5 with chain-of-thought reaches 8.75%, and TEXT-BISON-001 reaches 5.05%.

**Caveats/Scope:** These results are for the authors' few-shot baseline agents, accessibility-tree observations, model versions available at the time, and a 30-state-transition limit. Human performance is measured on a sampled set rather than every benchmark instance.

**Source pointers:** Abstract; Sec. 4; Sec. 5; Table 2; Appendix A.5; Appendix A.6

## Claim 4
**Claim:** The instruction to stop on unachievable tasks creates a tradeoff between avoiding impossible tasks and prematurely giving up.

**Evidence:** In the error analysis, GPT-4 with the unachievable hint incorrectly marks 54.9% of feasible tasks as impossible. Removing the hint raises GPT-4 overall success to 14.41% and achievable-task success to 13.02%, but unachievable-task success drops to 44.44%.

**Caveats/Scope:** The tradeoff depends on the exact prompt wording, task mix, and how unachievable intents are represented; it should not be treated as a universal result for all web-agent prompting.

**Source pointers:** Sec. 5.1; Table 2; Appendix A.9

## Claim 5
**Claim:** Solving one instance of a task template does not imply robust generalization to similar web tasks.

**Evidence:** In the no-UA-hint template analysis, GPT-4 achieves 100% success on only four of the 61 templates with at least one successful execution, while GPT-3.5 achieves full completion on none. The paper notes that small variations can change task length and difficulty, such as forking one repository versus all repositories from an organization.

**Caveats/Scope:** The analysis is restricted to templates with at least one successful execution and to the baseline models evaluated, so it measures consistency among partially solvable templates rather than the full benchmark distribution.

**Source pointers:** Sec. 5.1; Table 3

## Claim 6
**Claim:** The authors attribute many failures to weak exploration, state tracking, and fine-grained observation interpretation.

**Evidence:** Appendix error analysis describes GPT-4 latching onto nearby but wrong information, missing granular page-state cues such as already-entered text, repeating the same invalid action, and neglecting previous-action information. Figure 11 shows representative failed trajectories.

**Caveats/Scope:** This is qualitative error analysis from observed failures, not a complete taxonomy with measured frequencies for every error type.

**Source pointers:** Appendix A.10; Fig. 11; Sec. 5.1
