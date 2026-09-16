# Claims

## Claim 1
**Claim:** Carefully configured PPO is a strong cooperative MARL baseline, despite common assumptions that off-policy methods are more sample-efficient.

**Evidence:** The abstract, main results, and conclusion report competitive or superior final returns and sample efficiency for PPO-based methods across MPE, SMAC, Google Research Football, and Hanabi.

**Caveats/Scope:** The claim is empirical and limited to the paper's cooperative, discrete-action, mostly homogeneous-agent benchmarks and chosen tuning protocol.

**Source pointers:** `paper.pdf`, Abstract; Sec. 4.1-4.5; Sec. 6

## Claim 2
**Claim:** MAPPO and IPPO are competitive with strong off-policy baselines on SMAC.

**Evidence:** Table 1 reports median evaluation win rates over six seeds. The paper states that MAPPO and IPPO perform at least as well as QMix in most maps, and that MAPPO is comparable or superior to RODE in 10 of 14 maps under the same training-sample budget.

**Caveats/Scope:** Some maps remain hard or high-variance, and the paper notes that additional samples can be needed for convergence in at least one SMAC map.

**Source pointers:** `paper.pdf`, Sec. 4.3; Table 1; Appendix D.1

## Claim 3
**Claim:** MAPPO performs strongly on Google Research Football academy scenarios without relying on intrinsic rewards or offline pretraining.

**Evidence:** Table 2 shows MAPPO outperforming QMix in every reported GRF scenario and matching or exceeding CDS in most scenarios; the paper separately notes that TiKick uses pretrained models and is not a direct comparison.

**Caveats/Scope:** Results use GRF academy scenarios with dense shared rewards, and TiKick comparisons are qualified because TiKick uses human expert pretraining.

**Source pointers:** `paper.pdf`, Sec. 4.4; Table 2

## Claim 4
**Claim:** A centralized critic can matter in harder cooperative settings such as multi-player Hanabi.

**Evidence:** Table 3 reports Hanabi-Full scores for 2-5 players. The paper states that MAPPO is comparable or superior to SAD and VDN in nearly every setting, and that MAPPO's margin over IPPO grows as the number of agents increases.

**Caveats/Scope:** The Hanabi experiments are reported over at least three seeds, use up to 10B environment steps, and do not include auxiliary tasks.

**Source pointers:** `paper.pdf`, Sec. 4.5; Table 3

## Claim 5
**Claim:** MAPPO's strong performance depends on specific implementation and hyperparameter choices, not only on the PPO objective.

**Evidence:** Section 5 identifies five influential factors: value normalization, centralized value-function input representation, limited sample reuse, PPO clipping strength, and batch size. The corresponding ablations show clear performance trends and motivate concrete best-practice suggestions.

**Caveats/Scope:** The suggestions are practical empirical guidance rather than theoretical guarantees, and the authors explicitly leave theoretical analysis for future work.

**Source pointers:** `paper.pdf`, Sec. 5.1-5.5; Fig. 2-8; Sec. 6
