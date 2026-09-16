# Claims

## Claim 1: COMA is a centralized-training, decentralized-execution actor-critic method.

**Evidence:** The paper uses decentralized actors that condition on local action-observation histories, while the critic is used only during learning and can condition on global state, joint history, and joint actions. Figure 1 shows the training-only critic path and decentralized actor execution.

**Caveats/Scope:** This assumes a setting where extra state information is available during training but not execution. The experiments use cooperative, discrete-action StarCraft micromanagement tasks.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 4, "Counterfactual Multi-Agent Policy Gradients"; Figure 1.

## Claim 2: The counterfactual baseline targets multi-agent credit assignment without extra simulations or hand-chosen default actions.

**Evidence:** COMA computes an agent-specific advantage by comparing the critic value of the actual joint action against a baseline that marginalizes over one agent's action while keeping the other agents' actions fixed. The method is motivated as a way to get difference-reward-like credit assignment without replaying counterfactual simulator states or selecting a default action.

**Caveats/Scope:** The baseline is only as useful as the learned centralized critic. The local PDF also includes an erratum revising the proof of Lemma 1, so theoretical references should cite the corrected version.

**Source pointers:** `paper.pdf`, Section 4, Equation 4; Appendix A; Errata.

## Claim 3: COMA's critic representation makes the counterfactual baseline practical for discrete actions.

**Evidence:** Instead of outputting a value for every joint action, the critic takes the other agents' actions as input and outputs Q-values for all actions of the selected agent. The paper states this reduces the output size from `|U|^n` to `|U|` and permits the baseline to be evaluated with a single forward pass per agent, batched across agents.

**Caveats/Scope:** The input still grows with the number of agents and actions. The authors note that exploration, not only critic centralization, remains a scalability bottleneck.

**Source pointers:** `paper.pdf`, Section 4; Figure 1c; Section 5, "Architecture & Training"; Appendix B.

## Claim 4: The experimental benchmark deliberately makes StarCraft micromanagement decentralized and partially observable.

**Evidence:** The setup restricts each unit's field of view to its firing range, removes access to attack-move macro-actions, and uses local observations for actors while reserving global state for the critic. The experiments cover symmetric teams on 3m, 5m, 5w, and 2d 3z scenarios with a shared damage-based reward.

**Caveats/Scope:** The enemy is the built-in StarCraft AI, and the scenarios are small by later StarCraft benchmark standards. The environment design is intended to stress decentralized control and credit assignment rather than broad game play.

**Source pointers:** `paper.pdf`, Section 5, "Decentralised StarCraft Micromanagement"; Figure 2; Table 1.

## Claim 5: COMA outperforms the reported actor-critic baselines on final StarCraft win rates.

**Evidence:** Figure 3 and Table 1 show COMA with the highest mean final win percentage among local-field-of-view methods on all four maps. Table 1 reports COMA means of 87, 81, 82, and 47 percent on 3m, 5m, 5w, and 2d 3z, respectively, with the strongest non-COMA local-field-of-view baselines lower on each map.

**Caveats/Scope:** Results are averaged over the final 1000 evaluation episodes with confidence intervals and are specific to the authors' implementations, hyperparameters, and StarCraft scenarios. Comparisons to published centralized controllers are not apples-to-apples because those controllers use full field of view, centralized control, and macro-actions.

**Source pointers:** `paper.pdf`, Section 6; Figure 3; Table 1.
