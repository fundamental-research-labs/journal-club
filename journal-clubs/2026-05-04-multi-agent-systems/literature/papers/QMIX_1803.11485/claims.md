# Claims

## Claim 1: Monotonic factorization enables decentralized greedy execution

**Claim:** QMIX can learn a centralized joint action-value function while still allowing each agent to act greedily with respect to its own local value function.

**Evidence:** The method enforces a monotonic relationship between `Qtot` and each per-agent `Qa`, so the global argmax over `Qtot` matches the tuple of individual argmax operations over the `Qa` values. The mixing network keeps its weights non-negative and is trained end-to-end with a DQN-style TD loss.

**Caveats/Scope:** This relies on the value function being representable under the monotonic constraint and on the cooperative centralized-training/decentralized-execution setting.

**Source pointers:** `paper.pdf`, Abstract; Section 4, Equations 4-6; Figure 2.

## Claim 2: QMIX is more expressive than VDN but still constrained

**Claim:** QMIX strictly generalizes VDN's additive value decomposition to nonlinear monotonic combinations of per-agent values, but it cannot represent arbitrary joint action-value functions.

**Evidence:** VDN represents `Qtot` as a sum of individual values. QMIX instead uses a monotonic mixing network whose weights and biases are generated from the global state by hypernetworks. The appendix states that QMIX can represent value functions factored into nonlinear monotonic combinations, and gives examples of monotonic and non-monotonic payoff matrices.

**Caveats/Scope:** The monotonic class excludes cases where one agent's best action depends non-monotonically on another agent's simultaneous action; partial observability can also make the required local action ordering unavailable to an agent.

**Source pointers:** `paper.pdf`, Sections 3.4, 4, and 4.1; Figure 2; Appendix A.1 and Table 3.

## Claim 3: The two-step game isolates the representational advantage

**Claim:** In the toy two-step matrix game, QMIX learns the optimal branch whereas VDN learns a suboptimal branch.

**Evidence:** The main text reports that VDN selects Action A at the first step and receives reward 7, while QMIX recovers the optimal strategy with reward 8. Appendix tables show the learned `Qtot` values and final test rewards for VDN, QMIX, and ablations.

**Caveats/Scope:** This is a deliberately small diagnostic game under full exploration, so it supports the representation argument rather than proving broad empirical superiority.

**Source pointers:** `paper.pdf`, Section 5; Tables 1-2; Appendix B.2-B.3 and Tables 4-6.

## Claim 4: QMIX improves over IQL and VDN on StarCraft II micromanagement tasks

**Claim:** On the paper's six decentralized StarCraft II combat maps, QMIX is generally the strongest value-based method among IQL, VDN, and QMIX.

**Evidence:** The results section says IQL fails to learn policies that consistently defeat the enemy, VDN improves over IQL by learning basic coordination, and QMIX is strongest across the maps, especially in heterogeneous-agent scenarios such as `3s 5z` and `1c 3s 5z`.

**Caveats/Scope:** The evaluation is limited to the selected micromanagement maps, reward design, unit types, and StarCraft II setup used in the paper.

**Source pointers:** `paper.pdf`, Sections 6.1 and 7.1; Figure 3; Appendix D and Figure 6.

## Claim 5: State conditioning and nonlinear mixing both matter

**Claim:** QMIX's strongest performance on heterogeneous StarCraft II maps depends on combining global state conditioning with nonlinear value mixing.

**Evidence:** The ablations remove hypernetwork state conditioning (`QMIX-NS`), remove nonlinear mixing (`QMIX-Lin`), or add only a state-dependent term to VDN (`VDN-S`). The paper reports that heterogeneous maps require both central state information and nonlinear factorization for good performance.

**Caveats/Scope:** On a homogeneous map such as `3m`, nonlinear factorization is not always necessary; the value of each component depends on task structure.

**Source pointers:** `paper.pdf`, Sections 6.2 and 7.2; Figure 4; Appendix D and Figure 7.

## Claim 6: Learned policies show interpretable coordination patterns

**Claim:** QMIX's learned policies include coordinated micromanagement tactics that are qualitatively different from simpler baselines.

**Evidence:** The learned-policy analysis describes QMIX positioning Stalkers so Zealots cannot reach them on `2s 3z`, using Zealots to block before attacking, and showing similar behavior on `3s 5z`. The paper also notes that both QMIX and VDN learn a semicircle positioning strategy on `8m`.

**Caveats/Scope:** These are qualitative behavior observations from selected trained policies, not a separately quantified behavioral benchmark.

**Source pointers:** `paper.pdf`, Section 7.3.
