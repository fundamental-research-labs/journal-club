# ExpeL: LLM Agents Are Experiential Learners

## Source and access

Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang, *ExpeL: LLM Agents Are Experiential Learners*, arXiv:2308.10144v3 (first 2023-08-20; v3 2024-12-20), https://arxiv.org/abs/2308.10144. Full arXiv HTML read 2026-09-16, including §§4–6 and appendices C–E/J. The arXiv page marks CC BY 4.0; no local copy retained.

## Question and methods

ExpeL asks whether a frozen LLM agent can learn across tasks by collecting trial-and-error trajectories, extracting natural-language insights, and recalling successful trajectories at evaluation. Training uses ReAct with Reflexion retries (at most Z retries) to populate an experience pool (§4.1, lines 146–151). An insight LLM processes success/failure pairs and groups of successful trajectories using ADD, EDIT, UPVOTE, and DOWNVOTE; importance counts can remove weak insights (§4.2, lines 152–166). At evaluation, all extracted insights are appended and top-k successful trajectories are retrieved by task similarity (§4.3, lines 167–170). Environments are deterministic and textual (HotpotQA, ALFWorld, WebShop, FEVER); four-fold validation reports mean and standard error (§5.1, lines 338–343).

## Results and evidence

The paper reports ExpeL outperforming ReAct/Act across domains, with ablation values of HotpotQA 39.0±1.7% and ALFWorld 59.0±0.3% for the combined method; retrieval-only and insight-only variants are lower (Table 3, lines 398–412). The authors compare cross-task learning with Reflexion: HotpotQA 40% at Reflexion R3 versus 39% ExpeL, and ALFWorld 54% versus 59% (the HTML sentence reverses the apparent ordering; the accompanying values should be checked against the figure/table before quoting). Transfer uses source-task insights plus a small amount of target-task examples (§4.4, lines 171–173 and 328–330).

## Appraisal and limitations

ExpeL is an important foundation for inter-task, non-parametric learning: it combines reusable abstract guidance with episodic demonstrations, making its role distinct from ACE's context optimization and MemRL's learned utility/Q-values. However, experience gathering spends Reflexion retries, evaluation is on deterministic text environments, and the same frozen GPT-3.5 family performs actions; no lifetime cost accounting or broad continual stream is established. Authors acknowledge text-only scope, closed-source API dependence, context-window pressure, and the absence of theoretical guarantees (§6, lines 413–417). The apparent ALFWorld/Reflexion comparison inconsistency is a reporting limitation requiring cautious use.

## Discussion and follow-up

Use ExpeL to establish the historical baseline that “learning” can mean external insight plus retrieval without weight updates. Its central challenge to the current thesis is positive forward transfer, but the decisive missing controls are static expert insights, equal-budget retries, larger task streams, stale/incorrect insight tests, and retention of earlier skills. No independent reproduction was performed.
