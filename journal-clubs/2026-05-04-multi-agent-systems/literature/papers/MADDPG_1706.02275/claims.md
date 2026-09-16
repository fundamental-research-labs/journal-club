# Claims

## Claim 1
**Claim:** Independent single-agent RL methods face structural difficulties in multi-agent learning.

**Evidence:** The paper explains that Q-learning sees a non-stationary transition process as other agents update their policies, which undermines replay assumptions. It also gives a simple binary-action cooperative example where the chance of a single-sample policy-gradient step pointing in the correct direction decreases exponentially with the number of agents.

**Caveats/Scope:** The formal variance example is deliberately simplified and sparse-reward; it supports the intuition rather than proving failure for every independent learner or environment.

**Source pointers:** `paper.pdf`, Sections 1 and 3; Proposition 1 and Appendix proof.

## Claim 2
**Claim:** MADDPG enables centralized training while preserving decentralized execution.

**Evidence:** Each agent learns an actor using only its own observation, but trains a separate centralized critic that conditions on joint state or observations and all agents' actions. Because each critic is per-agent, reward functions can differ or conflict across agents.

**Caveats/Scope:** The training setup assumes access to other agents' observations/actions, or learnable approximations of their policies. The authors note that the critic input grows with the number of agents.

**Source pointers:** `paper.pdf`, Section 4.1, Equations 4-6, Figure 1, Appendix Algorithm 1, Conclusion.

## Claim 3
**Claim:** MADDPG outperforms decentralized baselines on the cooperative communication benchmark.

**Evidence:** In cooperative communication after 25,000 episodes, Table 1 reports 84.0% target reach for MADDPG versus 32.0% for DDPG, 24.8% for DQN, 17.2% for actor-critic, 20.6% for TRPO, and 13.6% for REINFORCE. The text attributes this to the centralized critic giving a more consistent training signal for speaker/listener coordination.

**Caveats/Scope:** This is a small particle-world communication task, and success is measured by target reach after convergence rather than broad transfer to unrelated domains.

**Source pointers:** `paper.pdf`, Section 5.2, Figures 4-6, Appendix Table 1.

## Claim 4
**Claim:** MADDPG handles mixed cooperative-competitive environments better than DDPG in the reported experiments.

**Evidence:** In physical deception, Table 4 reports much larger agent-vs-adversary success gaps for MADDPG agents against DDPG adversaries than for the reverse pairing. In predator-prey, MADDPG predators catch DDPG prey more often than DDPG predators catch MADDPG prey. In covert communication, MADDPG-trained Alice/Bob have a larger success advantage over Eve than DDPG-trained agents.

**Caveats/Scope:** The results are from the paper's particle-world environments and metrics; the paper does not establish that MADDPG dominates all possible adversarial MARL algorithms or larger-scale games.

**Source pointers:** `paper.pdf`, Section 5.2, Figure 3, Appendix Tables 3-5, Figure 8.

## Claim 5
**Claim:** Agents can learn usable approximations of other agents' policies for MADDPG training.

**Evidence:** Section 4.2 introduces per-agent approximations of other agents' policies trained online from replay-buffer samples. Section 5.3 reports that in cooperative communication, using approximated policies reaches the same success rate as using true policies without significant convergence slowdown, despite imperfect KL fit.

**Caveats/Scope:** The empirical demonstration is limited to cooperative communication, so the paper leaves open how robust approximate policy modeling is in larger or more adversarial settings.

**Source pointers:** `paper.pdf`, Sections 4.2 and 5.3, Equation 7, Figure 7.

## Claim 6
**Claim:** Policy ensembles improve robustness in competitive multi-agent training.

**Evidence:** The method samples among multiple sub-policies during training so agents interact with a variety of collaborator or competitor behaviors. Section 5.4 reports that ensemble policies are stronger than single policies in competitive environments, with Figure 3 comparing single-policy and ensemble MADDPG and Appendix Table 6 giving additional evaluations.

**Caveats/Scope:** The ensemble experiments use small numbers of sub-policies and selected particle-world tasks; the added training cost and scaling behavior are not deeply analyzed.

**Source pointers:** `paper.pdf`, Sections 4.3 and 5.4, Figure 3, Appendix Table 6.
