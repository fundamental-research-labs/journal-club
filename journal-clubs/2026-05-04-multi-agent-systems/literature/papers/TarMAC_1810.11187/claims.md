# Claims

## Claim 1
**Claim:** TarMAC provides targeted continuous communication while preserving decentralized execution.

**Evidence:** Each agent emits a message split into a signature/key and value. Receivers compute query-signature attention weights and aggregate message values accordingly. A centralized critic is used only during training; at test time, each policy acts from local observation, recurrent state, and received messages.

**Caveats/Scope:** Targeting is implicit property matching, not explicit symbolic addressing of named agents. Messages are continuous machine-level vectors, not human-readable language.

**Source pointers:** `paper.pdf`, Section 4, Figure 1, Equations 1-4, Table 1.

## Claim 2
**Claim:** Targeted attention improves cooperative navigation most clearly when message relevance differs across agents.

**Evidence:** In SHAPES, the hardest reported setting has four agents in a 50x50 grid with mixed goals. TarMAC reports 85.8% success, compared with 82.4% for communication without attention and 69.1% for no communication. The paper notes that communication and attention benefits increase with environment and goal complexity.

**Caveats/Scope:** The SHAPES setting is synthetic and the advantage over mean-pooled communication is modest on easier or shared-goal variants.

**Source pointers:** `paper.pdf`, Section 5.1, Figure 2, Table 2.

## Claim 3
**Claim:** Multi-round communication can matter more than increasing message dimensionality.

**Evidence:** On the hard traffic junction task, 2-round TarMAC reports 97.1% success, above 1-round TarMAC at 84.6%, CommNet at 78.9%, and no communication at 74.1%. The message-size ablation reports that 2-round communication improves hard-traffic performance substantially over 1-round, even with small message values.

**Caveats/Scope:** The number of rounds is a hyperparameter and the paper reports no further gains beyond two rounds in this environment. The easy traffic setting is nearly saturated by several methods.

**Source pointers:** `paper.pdf`, Section 5.2, Figure 3, Table 3.

## Claim 4
**Claim:** The learned attention patterns are interpretable enough to diagnose what agents route to one another.

**Evidence:** In SHAPES visualizations, agents attend to others observing their target colors and later self-attend once goals are reached. In traffic, cars receive high attention near sensitive junction locations, and the number of cars attended to tracks the number of active cars, with the paper reporting a positive Spearman correlation.

**Caveats/Scope:** These are visualization and correlation analyses, not causal interventions proving that each attention edge is necessary.

**Source pointers:** `paper.pdf`, Section 5.1, Figure 2; Section 5.2, Figure 4.

## Claim 5
**Claim:** TarMAC can use compact communication to improve high-dimensional first-person multi-agent navigation.

**Evidence:** On the 4-agent House3D find-fireplace task, TarMAC reports 68.9% success and 82.5 average steps, compared with 64.3% and 101.3 steps for mean-pooled communication and 62.1% and 186.5 steps for no communication. The paper emphasizes that the learned message vector is much smaller than the visual observation.

**Caveats/Scope:** This is one House3D object-goal task with shaped rewards and a long but finite horizon; the method remains far from perfect success in this setting.

**Source pointers:** `paper.pdf`, Section 5.3, Figure 5, Table 4.

## Claim 6
**Claim:** In mixed or competitive settings, targeted attention is useful when paired with a separate decision about whether to communicate.

**Evidence:** The paper argues that TarMAC's soft attention alone can leak information through low but nonzero attention probabilities. It therefore replaces IC3Net's message averaging with TarMAC attention so agents learn both when to communicate and whom to address. In Predator-Prey, IC3Net + TarMAC reaches lower average episode lengths than IC3Net alone, and the 2-round variant is best among reported variants.

**Caveats/Scope:** This claim is for the IC3Net hybrid, not standalone TarMAC, and is tested on Predator-Prey with a small number of independent runs.

**Source pointers:** `paper.pdf`, Section 5.4, Figure 6, Table 5.
