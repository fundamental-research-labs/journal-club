# Claims

## Claim 1
**Claim:** SWE-RL turns open-source pull request evolution into a reinforcement learning signal for repository-level issue repair.

**Evidence:** The method builds RL items from GitHub PRs containing an issue, code context, and oracle patch. The policy emits search/replace edits after reasoning; malformed outputs receive -1 reward, and valid outputs are rewarded by patch similarity to the oracle using `difflib.SequenceMatcher`, with GRPO for optimization.

**Caveats/Scope:** The reward is syntactic patch similarity, not semantic equivalence, so alternative correct fixes may be undervalued. The training corpus is a heavily filtered PR subset rather than all software evolution.

**Source pointers:** `paper.pdf`, Abstract; Figure 1; Section 2; Equation 1; Appendix A; Section 5 Limitations.

## Claim 2
**Claim:** Llama3-SWE-RL-70B sets the paper's best <=100B open-model result on SWE-bench Verified.

**Evidence:** Table 1 reports 41.0% pass@1 on SWE-bench Verified with Agentless Mini, above the listed <=100B baselines including Llama3-SWE-SFT-70B at 36.2%, SWE-Fixer-72B at 32.8%, and SWE-Gym-32B at 32.0%.

**Caveats/Scope:** This is an end-to-end result using Agentless Mini with many repair and test samples, not a scaffold-free model-only comparison. Larger or closed-source systems in the table still reach higher scores.

**Source pointers:** `paper.pdf`, Section 3.1 Evaluation setup; Section 3.2; Table 1.

## Claim 3
**Claim:** SWE-RL improves repair ability beyond both the base Llama model and a strong SFT baseline under oracle localization.

**Evidence:** Table 2 provides oracle localized files and removes localization/test-generation steps. Llama3-SWE-RL-70B reaches 34.8 repair performance with 95.6% correct format, compared with Llama3-SWE-SFT-70B at 29.6 and base Llama-3.3-70B-Instruct at 5.4 with greedy decoding or 16.6 with majority voting.

**Caveats/Scope:** The setup gives oracle files and uses a single greedy repair for the RL and SFT models, so it isolates repair skill rather than full autonomous issue resolution.

**Source pointers:** `paper.pdf`, Section 3.3; Table 2.

## Claim 4
**Claim:** Agentless Mini benefits from scaling repair samples and reproduction tests, but the returns plateau.

**Evidence:** Figure 4 reports a large SWE-bench Verified gain as repair samples increase from 20 to 160, then only small gains up to 500 samples. Test samples improve performance up to around 20, with no reported difference between 20 and 30.

**Caveats/Scope:** These gains are tied to the paper's reranking pipeline and compute budget. They show inference-time search and test selection effects, not only changes in the trained model.

**Source pointers:** `paper.pdf`, Section 3.4; Figure 4; Appendix B.

## Claim 5
**Claim:** RL on issue-solving data appears to improve out-of-domain reasoning more consistently than the SFT baseline.

**Evidence:** Table 3 compares the base, SFT, and RL models on HumanEval+, BigCodeBench-Hard, CRUXEval, MATH, and MMLU. The RL model is best or tied on the reported tasks and shows especially large improvements on CRUXEval and MATH, while the SFT model often trails the base model.

**Caveats/Scope:** The evaluations use zero-shot greedy decoding, and the paper notes that small individual gains are not always statistically significant by themselves. MATH also has a strict-vs-lenient formatting caveat.

**Source pointers:** `paper.pdf`, Section 3.5; Table 3.

## Claim 6
**Claim:** Continuous patch-similarity reward works better than exact-match reward for real-world software patches.

**Evidence:** The reward ablation reports 34.8 repair performance for the continuous reward versus 29.0 for the discrete exact-match reward, with similar format accuracy. The training dynamics show the discrete reward staying near zero because exact oracle patch matches are rare.

**Caveats/Scope:** This is a single reward-family ablation in the paper's setup. Continuous similarity still does not guarantee semantic correctness.

**Source pointers:** `paper.pdf`, Section 3.6; Figure 5; Section 5 Limitations.
