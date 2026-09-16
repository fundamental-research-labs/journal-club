# Claims

## Claim 1: Continuous communication makes learned inter-agent messaging differentiable.

**Evidence:** CommNet gives each agent a hidden state and a continuous communication vector computed from other agents' hidden states. The paper emphasizes that this channel can be trained by backpropagation and combined with either supervised learning or a policy-gradient RL outer loop.

**Caveats/Scope:** The formulation assumes fully cooperative agents with a shared reward or shared supervised objective. The communication channel is an internal continuous vector, not discrete or human-readable language.

**Source pointers:** `paper.pdf`, Abstract; Sections 1, 2.1; Appendix A

## Claim 2: The CommNet controller is designed to handle variable agent counts and permutation-invariant agent ordering.

**Evidence:** Section 2.1 normalizes the communication vector by the number of other agents and notes that the resulting block matrix is dynamically sized and permutation invariant. Section 2.2 extends the same idea to local neighborhoods interpreted as a dynamic graph.

**Caveats/Scope:** This flexibility depends on shared module parameters and compatible agent state encodings; the paper says heterogeneous agent types are not fully exploited.

**Source pointers:** `paper.pdf`, Sections 2.1, 2.2; Figure 1; Section 5

## Claim 3: On the lever-pulling toy task, learned communication is enough to coordinate agents that only observe their own identity.

**Evidence:** With five active agents sampled from a pool of 500, CommNet reaches 0.99 under supervised training and 0.94 under reinforcement training on the distinct-levers metric, while the independent controller is 0.59 in both cases.

**Caveats/Scope:** This is a deliberately simple one-step coordination task; the supervised version uses a target assignment based on sorting agent IDs.

**Source pointers:** `paper.pdf`, Section 4.2; Table 1; Appendix B

## Claim 4: CommNet improves simulated traffic and combat performance relative to no communication and several alternative communication baselines.

**Evidence:** In traffic, CommNet lowers failure rates for MLP, RNN, and LSTM modules, including 1.6% failure for LSTM CommNet versus 9.4% for independent LSTM. In combat, CommNet reports higher win rates than independent, fully connected, and discrete-communication baselines across the main module choices.

**Caveats/Scope:** These are MazeBase simulations with fixed reward definitions, training budgets, and small agent counts. Combat results have substantial variance in some CommNet runs.

**Source pointers:** `paper.pdf`, Sections 4.3.1, 4.3.3; Tables 2, 3

## Claim 5: The learned traffic protocol is sparse and partly interpretable.

**Evidence:** The traffic analysis finds that many communication vectors are near zero, while several PCA clusters correspond to cars at specific locations and correlate with other cars braking at collision-relevant locations.

**Caveats/Scope:** The interpretation is based on probing a simple traffic environment; it should not be generalized to rich semantic language.

**Source pointers:** `paper.pdf`, Section 4.3.2; Figure 3; Appendix D

## Claim 6: CommNet can be repurposed as a communication-based neural reasoning model, but is not state of the art for bAbI.

**Evidence:** On the 10K bAbI tasks, CommNet with MLP modules has 7.1% mean error and 3 failed tasks, improving on the independent MLP formulation (15.2%, 9 failed tasks) and LSTM baseline (36.4%, 16 failed tasks), but trailing MemN2N and DMN+.

**Caveats/Scope:** The bAbI formulation treats sentences as agents, which is a useful abstraction for information exchange but not a standard multi-agent environment.

**Source pointers:** `paper.pdf`, Section 4.4; Table 4; Appendix E
