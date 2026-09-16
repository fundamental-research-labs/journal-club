# Claims

## Claim 1
**Claim:** Learning communication protocols is hard because useful messages only receive reward when another agent also learns to interpret and act on them.

**Evidence:** The setting section frames cooperative partially observable tasks with private observations and limited-bandwidth messages. It explicitly argues that positive rewards are sparse because a sender's useful message is only reinforced if the receiver interprets it correctly.

**Caveats/Scope:** This claim is about the paper's fully cooperative, shared-reward environments with no predefined protocol; adversarial, fully observable, or hand-designed communication settings differ.

**Source pointers:** `paper.pdf`, Sections 1 and 4.

## Claim 2
**Claim:** RIAL can learn communication by treating messages as reinforcement-learning actions, but it lacks direct cross-agent feedback.

**Evidence:** RIAL uses recurrent Q-networks to select both environment actions and communication actions, with variants for independent agents and shared parameters. The paper contrasts this with DIAL by noting that RIAL is end-to-end trainable within an agent but not across agents, so gradients do not pass between sender and receiver.

**Caveats/Scope:** RIAL remains a meaningful baseline and works on easier switch-riddle cases; the limitation is most visible when protocol discovery requires richer feedback than trial-and-error message rewards.

**Source pointers:** `paper.pdf`, Sections 5.1 and 5.2; Figure 1.

## Claim 3
**Claim:** DIAL uses centralized training to make communication differentiable while preserving decentralized execution with discrete messages.

**Evidence:** During training, DIAL routes real-valued messages between C-Nets so the receiver's downstream error gradient can update the sender. During execution, the discretise/regularise unit maps messages to binary values, matching the task's limited communication channel.

**Caveats/Scope:** The paper mainly studies discrete messages after binarization; continuous-message protocols are described as naturally supported but not the main experimental focus.

**Source pointers:** `paper.pdf`, Section 5.2; Figure 1; Appendix A.

## Claim 4
**Claim:** Parameter sharing materially improves protocol learning.

**Evidence:** In the switch-riddle results, parameter sharing speeds both RIAL and DIAL. For the four-agent switch task, DIAL with parameter sharing performs best, while RIAL without sharing is reported as unable to beat the no-communication baseline.

**Caveats/Scope:** The paper evaluates small cooperative tasks; the benefit may depend on agent homogeneity and whether a shared policy with agent-index inputs is appropriate.

**Source pointers:** `paper.pdf`, Section 5.1 "Parameter Sharing"; Section 6.2; Figure 4.

## Claim 5
**Claim:** DIAL's differentiable communication is especially valuable on delayed, image-based communication games.

**Evidence:** On colour-digit and multi-step MNIST games, the paper reports that DIAL substantially outperforms RIAL and NoComm. It attributes multi-step MNIST success to gradients that optimize message content with respect to rewards several time steps later, and shows an extracted binary coding scheme for digits.

**Caveats/Scope:** These are synthetic MNIST communication games, not natural language tasks; the conclusion is about learning compact task-specific protocols.

**Source pointers:** `paper.pdf`, Section 6.3; Figure 6; Appendix B.

## Claim 6
**Claim:** Noise in DIAL's communication channel helps continuous training messages become usable discrete execution messages.

**Evidence:** The experiments and appendix show that adding Gaussian noise before the logistic channel regularizes activations into separable modes, reducing discretization error. The paper states that noise was essential for successful training in its setup.

**Caveats/Scope:** Noise level is a hyperparameter, and Appendix C shows the required amount depends on channel capacity and whether the task rewards over-encoding.

**Source pointers:** `paper.pdf`, Section 6.4; Figures 7-9; Appendix C.
