# Claims

## Claim 1
**Claim:** MAPoRL frames collaborative LLM debate as a multi-agent RL problem rather than a prompt-only protocol.

**Evidence:** The method defines each agent's state from the full interaction history, uses a learned verifier to score answers, and trains turn-specific agent policies and value functions with multi-agent PPO. The influence-aware reward includes the current answer score and future verifier scores from the same and other agents.

**Caveats/Scope:** The experiments instantiate this idea mainly in collaborative debate; the paper states the framework can apply to other multi-LLM systems if responses can be evaluated, but does not demonstrate many such systems.

**Source pointers:** `paper.pdf`, Figure 1; Section 3.1; Section 3.2; Appendix F

## Claim 2
**Claim:** Co-training agents can improve multi-turn collaboration where off-the-shelf debate does not.

**Evidence:** In Experiment 1, off-the-shelf Phi-3 debate does not reliably gain accuracy across turns even with a larger response budget, while MAPoRL-trained Phi-3 agents improve over turns on GSM8K and ANLI. The response-transition analysis shows more useful wrong-to-right revisions for MAPoRL-trained agents.

**Caveats/Scope:** Results are from the authors' debate setup, small instruction models, and the GSM8K/ANLI tasks; larger models or different interaction protocols may behave differently.

**Source pointers:** `paper.pdf`, Section 4.3; Figure 2; Figure 3; Figure 4

## Claim 3
**Claim:** The measured gains are not explained only by MAPoRL models learning more task-specific knowledge.

**Evidence:** The no-collaboration control gives each model only the original question. Off-the-shelf Phi-3 and MAPoRL-trained turn-2/turn-3 models have similar single-question accuracy on GSM8K and ANLI, while their collaborative performance differs in the debate setting.

**Caveats/Scope:** This is a control, not a proof that no task knowledge is learned; it is reported for the evaluated models and datasets.

**Source pointers:** `paper.pdf`, Section 4.3, Remark 2

## Claim 4
**Claim:** MAPoRL's learned collaboration can transfer across task domains in the tested directions.

**Evidence:** Table 5 reports that agents trained on ANLI and evaluated on GSM8K improve from 0.640 off-the-shelf final-turn accuracy to 0.720, and agents trained on GSM8K and evaluated on ANLI improve from 0.468 to 0.507 by the final turn.

**Caveats/Scope:** Transfer is shown for two dataset directions with the same overall debate/evaluation setup; it should not be read as broad evidence across arbitrary domains.

**Source pointers:** `paper.pdf`, Section 4.5; Table 5

## Claim 5
**Claim:** Verifier rewards strengthen MAPoRL, but multi-agent co-adaptation also helps under sparse final-answer rewards.

**Evidence:** Appendix G.7 reports GSM8K final-turn accuracy of 0.809 for MAPoRL with verifier rewards and 0.746 without verifier rewards, compared with 0.639 for off-the-shelf debate. Appendix G.8 also reports single-agent RL with verifier rewards at 0.732, below MAPoRL's final-turn result.

**Caveats/Scope:** These ablations are reported on GSM8K and depend on verifier quality; the appendix also notes reward hacking and verifier/generator architectural alignment issues.

**Source pointers:** `paper.pdf`, Appendix E.2; Appendix G.7, Table 7; Appendix G.8, Table 8

## Claim 6
**Claim:** Naive supervised fine-tuning on filtered high-quality debate trajectories did not induce collaboration in the authors' setup.

**Evidence:** Experiment 5 generated 12,800 off-the-shelf debate trajectories, selected the top 10%, and fine-tuned on them. The reported accuracy dropped to 0.578 at turn 2 and 0.525 at turn 3, below the off-the-shelf comparison.

**Caveats/Scope:** This rules out one straightforward SFT recipe, not all supervised or iterative data-generation approaches; the paper explicitly notes contemporaneous iterative SFT systems that use additional techniques.

**Source pointers:** `paper.pdf`, Section 4.7
