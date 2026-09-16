# Claims

## Claim 1: Sequential social dilemmas model cooperation and defection as learned policies.

**Claim:** SSDs extend matrix-game social dilemmas by treating cooperation and defection as properties of temporally extended policies in partially observable Markov games, rather than as atomic actions.

**Evidence:** The paper defines SSDs using cooperative and defective policy sets whose empirical payoff matrix satisfies the standard social dilemma inequalities, and motivates the definition by listing limitations of matrix-game social dilemmas.

**Caveats/Scope:** The cooperative and defective policy sets must be chosen or thresholded by a social behavior metric; the definition does not automatically classify every legal policy.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 2.2; Figure 2

## Claim 2: Empirical game-theoretic analysis can recover matrix-game structure from Markov games.

**Claim:** Learned policies in a sequential Markov game can be mapped to empirical payoff matrices and classified as classic social dilemmas such as Prisoner's Dilemma, Chicken, or Stag Hunt.

**Evidence:** The authors sample learned cooperative and defective policies, play them against one another, average payoffs for the four matrix cells, and classify the resulting empirical games. Gathering yields mostly prisoner-dilemma-like SSD cases, and Wolfpack contains Chicken, Stag Hunt, and Prisoner's Dilemma regions.

**Caveats/Scope:** The classification depends on the learned policy populations, selected environment parameters, and empirical rollout estimates; it is not an exhaustive equilibrium analysis of all possible policies.

**Source pointers:** `paper.pdf`, Sections 5.1-5.2; Figure 5; Figure 6

## Claim 3: Resource scarcity promotes conflict in Gathering.

**Claim:** In the Gathering game, aggressive tagging emerges when resources are scarce and rival removal is consequential, while more abundant environments produce less aggressive policies.

**Evidence:** Beam-use rate is used as the behavior metric for defection. The paper reports that agents trained with low apple abundance or high tagged-agent timeout learn highly aggressive policies, while agents trained with high abundance or low timeout are less aggressive.

**Caveats/Scope:** Beam use is a proxy for defection in this specific gridworld; tagging has no direct reward and the result depends on the DQN training setup and chosen parameter sweep.

**Source pointers:** `paper.pdf`, Section 5.1; Figure 3; Figure 4; Figure 6

## Claim 4: Team-hunting incentives promote cooperation in Wolfpack.

**Claim:** In Wolfpack, increasing the team capture reward or capture radius increases cooperative hunting behavior.

**Evidence:** The paper measures cooperation through the average number of wolves per capture and reports that larger group benefit and larger capture radius lead to more wolves participating in captures. It also describes two cooperative strategies: moving together before hunting, and waiting near prey for the partner to arrive.

**Caveats/Scope:** The cooperation metric is tied to the Wolfpack reward design, where shared capture rewards represent protection of a carcass from scavengers.

**Source pointers:** `paper.pdf`, Section 5.2; Figure 3; Figure 4

## Claim 5: Implementation complexity can reverse how agent capacity affects social behavior.

**Claim:** The same agent-parameter change can have different social effects across SSDs because cooperation and defection can have different implementation difficulty in different environments.

**Evidence:** Larger network size increases defection in Gathering, where targeting another agent with a beam is the more complex behavior, but decreases defection in Wolfpack, where coordinated pack hunting is the more complex behavior.

**Caveats/Scope:** The interpretation of network size as capacity and DQN parameters as social-behavior analogues is descriptive; these agents do not model human deliberation or explicit recursive reasoning.

**Source pointers:** `paper.pdf`, Section 5.3; Section 6; Figure 7

## Claim 6: Static matrix games can hide behaviorally important differences between social dilemmas.

**Claim:** Two SSDs can induce similar matrix-game summaries while making different predictions about the emergence and stability of cooperation.

**Evidence:** The paper argues that both Gathering and Wolfpack contain prisoner-dilemma-like empirical payoff matrices, but the sequential structure makes cooperation easier to learn in Gathering-like settings and harder in Wolfpack-like settings.

**Caveats/Scope:** This does not make matrix-game models useless; it shows that they can miss learning and implementation effects when policy execution is sequential.

**Source pointers:** `paper.pdf`, Section 1; Section 6; Figure 6; Figure 7
