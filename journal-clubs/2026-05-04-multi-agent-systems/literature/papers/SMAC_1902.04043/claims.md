# Claims

## Claim 1: SMAC fills a benchmark gap for cooperative MARL.

**Evidence:** The introduction argues that single-agent RL benefited from standardized environments such as ALE and MuJoCo, while cooperative MARL was still dominated by one-off toy domains. SMAC is proposed as a standard set of StarCraft II micromanagement tasks for partially observable, cooperative, multi-agent learning.

**Caveats/Scope:** The benchmark covers cooperative micromanagement, not full StarCraft II gameplay or general-sum multi-agent games.

**Source pointers:** Abstract; Section 1; Section 2.

## Claim 2: SMAC enforces decentralized execution while allowing centralized training.

**Evidence:** Each allied unit is an independent agent that receives local observations from a limited sight range and can attack only enemies in shooting range. The global state is available only during centralized training, and Appendix B states that test-time policies must use only each agent's own action-observation history.

**Caveats/Scope:** The environment uses SC2LE raw API features rather than human-like pixels, and observations/action spaces are benchmark design choices rather than the native StarCraft II interface.

**Source pointers:** Section 3; Section 4, "State and Observations" and "Action Space"; Appendix B.

## Claim 3: The scenario suite is designed to require different coordination skills.

**Evidence:** Table 1 lists 14 scenarios with varied unit compositions and asymmetries. Section 4 and Appendix A describe focus fire, avoiding overkill, kiting, terrain use, and choke-point control as required micromanagement skills.

**Caveats/Scope:** The paper gives task-design rationales and baseline behavior, not formal proofs that each named skill is necessary in every scenario.

**Source pointers:** Section 4; Table 1; Appendix A.1.

## Claim 4: Naive focus fire is not sufficient for strong SMAC performance.

**Evidence:** The results compare against a heuristic that attacks the closest enemy with the whole team. The authors report poor heuristic performance across much of the suite and use this to argue that SMAC requires more complex behavior than closest-enemy focus fire.

**Caveats/Scope:** The heuristic is intentionally simple and ignores partial observability, so it is a lower bar rather than a competitive hand-engineered controller.

**Source pointers:** Section 6; Figures 3-6; Appendix D, Table 2.

## Claim 5: QMIX is the strongest reported baseline, but many scenarios remain unsolved.

**Evidence:** Section 6 states that QMIX achieves the highest overall test win percentage and is the best performer on up to eight scenarios during training. Table 2 shows high QMIX scores on easy maps but weak results on several hard or super-hard maps, including near-zero performance on some scenarios.

**Caveats/Scope:** These are results for the authors' architectures, training budgets, shaped rewards, and 2019 baseline implementations; later algorithms may change the leaderboard.

**Source pointers:** Section 6; Figures 3-8; Appendix C; Appendix D, Table 2.

## Claim 6: The paper standardizes evaluation methodology, not just environment assets.

**Evidence:** Appendix B recommends preserving environment settings, using decentralized policies at evaluation, plotting mean win percentage over environment steps, running independent seeds, reporting medians and percentile bands, and documenting compute resources.

**Caveats/Scope:** These are proposed best practices rather than an externally enforced benchmark protocol.

**Source pointers:** Appendix B; Appendix B.1.
