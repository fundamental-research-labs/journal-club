# Claims

## Claim 1
**Claim:** Additive value decomposition enables decentralized greedy execution while training from a single team reward.

**Evidence:** The paper defines the joint action-value estimate as an approximate sum of local `Q_i(h_i, a_i)` terms and trains those terms by backpropagating the Q-learning loss through the summation. Because maximizing the sum over independent local action choices matches each agent greedily maximizing its own component, the learned agents can be deployed independently.

**Caveats/Scope:** This relies on an additive approximation to the joint value function; interactions that require non-additive coordination may not be represented well.

**Source pointers:** `paper.pdf`, Section 3; Figure 2

## Claim 2
**Claim:** VDN outperforms naive independent and fully centralized DQN-style baselines on the paper's cooperative gridworld tasks.

**Evidence:** The results compare the listed architectures over seven task variants, ten random seeds, and 50,000 training episodes. Figures 4 and 5 report that value-decomposition architectures have better normalized area-under-curve and final performance than independent learners and centralized baselines.

**Caveats/Scope:** The tasks are two-agent, partially observable gridworlds; the paper does not establish the same ranking for larger teams or high-dimensional domains.

**Source pointers:** `paper.pdf`, Sections 4.2-4.3; Figures 4-5; Appendix A

## Claim 3
**Claim:** VDN directly targets spurious team-reward credit assignment and the "lazy agent" failure mode.

**Evidence:** The introduction argues that independent learners can observe rewards caused by teammates and that centralized learners can settle on policies where one agent becomes inactive. VDN instead learns local value components from the joint TD signal, and the results section notes that value decomposition with weight sharing avoids the lazy-agent problem in the hard one-corridor Fetch task.

**Caveats/Scope:** The lazy-agent evidence is empirical and task-specific; weight sharing is not universally beneficial.

**Source pointers:** `paper.pdf`, Section 1; Sections 3-4.3

## Claim 4
**Claim:** Learned VDN components can recover sensible agent-specific value assignments without per-agent rewards.

**Evidence:** In Fetch, Figure 6 shows the total Q-value anticipating team reward events while individual component values spike around the corresponding agent's pickup or drop-off events, despite the environment exposing only team-level reward.

**Caveats/Scope:** This is a qualitative analysis from one learned Fetch policy, not a proof that decompositions are unique or generally interpretable.

**Source pointers:** `paper.pdf`, Section 4.4; Figure 6

## Claim 5
**Claim:** Architectural aids such as weight sharing, role identifiers, and information channels interact with task structure rather than providing a uniform improvement.

**Evidence:** The results report that shared weights help on Fetch with one corridor but are problematic in Checkers because one agent's reward magnitude is ten times larger. Role information helps when non-identical behavior is useful, and low-level information channels improve learning in Checkers while high-level communication learns more slowly overall.

**Caveats/Scope:** These comparisons use the paper's selected DQN/LSTM architectures and small gridworld tasks, so they should be treated as design guidance rather than universal rules.

**Source pointers:** `paper.pdf`, Sections 4.1-4.3; Table 1; Figures 4-5
