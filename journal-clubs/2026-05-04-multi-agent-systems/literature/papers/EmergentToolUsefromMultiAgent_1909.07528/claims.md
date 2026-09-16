# Claims

## Claim 1: Multi-agent hide-and-seek induces a multi-stage autocurriculum.

**Evidence:** The paper reports six qualitatively distinct phases in self-play training: running/chasing, fort building, ramp use, ramp defense, box surfing, and surf defense. Each new behavior changes the task faced by the opposing team, creating pressure for a counter-strategy.

**Caveats/Scope:** The phases are identified in a particular simulated hide-and-seek environment and are partly qualitative, though supported by object movement/locking statistics. The authors explicitly describe the strategy space as bounded.

**Source pointers:** Abstract; Section 5; Figure 1; Figure 3; Appendix A.1

## Claim 2: Tool use emerges without an explicit tool-use reward.

**Evidence:** Agents receive only team hide-and-seek visibility rewards, plus boundary penalties, yet hiders learn to construct shelters from boxes, seekers learn to use ramps to enter shelters, seekers learn box surfing, and hiders learn to lock boxes and ramps defensively.

**Caveats/Scope:** The tools and affordances are engineered into the simulator, and some behaviors exploit simulator details, especially box surfing. This is not evidence of open-ended real-world tool use.

**Source pointers:** Section 3; Section 5; Figure 1; Appendix A.1; Section 7

## Claim 3: Scale, architecture, and environment randomization are enabling conditions.

**Evidence:** The default 64k-batch, 1.6M-parameter setup reaches ramp defense after 132.3M episodes; smaller 16k and 8k batch experiments did not converge in the reported setting. Reducing environment randomization yields fewer emergent stages, and an omniscient value function is reported as critical for reaching later stages at the tested scale.

**Caveats/Scope:** These are ablations for one environment, one training stack, and one era of distributed PPO implementation. They show sensitivity, not a universal scaling law.

**Source pointers:** Section 5; Figure 4; Appendix A.2 / Table A.1; Appendix A.4 / Figure A.3

## Claim 4: Multi-agent competition can target object interaction more naturally than intrinsic motivation in this domain.

**Evidence:** Count-based exploration produces strong agent and box movement only when the count state is restricted to relevant low-dimensional box-position features. With richer full-state representations, object movement drops substantially; RND performs only slightly better in the full-state setting. The authors argue self-play avoids manually selecting the "interesting" state dimensions.

**Caveats/Scope:** The comparison uses movement statistics as a proxy for meaningful behavior, and the intrinsic-motivation baselines are not exhaustive. The result supports a domain-specific contrast rather than a general rejection of intrinsic motivation.

**Source pointers:** Section 6.1; Figure 5; Appendix D

## Claim 5: Transfer tests provide a useful but mixed quantitative evaluation of emergent skills.

**Evidence:** The paper introduces five targeted tests: Object Counting, Lock and Return, Sequential Lock, Construction from Blueprint, and Shelter Construction. Hide-and-seek pretraining outperforms scratch and count-based pretraining on Lock and Return, Sequential Lock, and Construction from Blueprint, but underperforms count-based pretraining on Object Counting and matches final reward while learning slower than scratch on Shelter Construction.

**Caveats/Scope:** The tests are domain-specific and share action/object structure with hide-and-seek. The mixed results suggest useful representations but limited skill reuse and entangled learned behaviors.

**Source pointers:** Section 6.2; Figure 6; Appendix C; Appendix A.5
