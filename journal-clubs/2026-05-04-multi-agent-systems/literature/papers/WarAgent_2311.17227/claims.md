# Claims

## Claim 1
**Claim:** WarAgent operationalizes historical conflict simulation as a structured LLM multi-agent system rather than as free-form role-play.

**Evidence:** The paper defines country profiles with six dimensions, a bounded action space for diplomatic and military moves, country agents, secretary agents, and Board/Stick state trackers for external relations and domestic mobilization.

**Caveats/Scope:** The abstraction deliberately simplifies diplomacy: actions are discrete, communication publicity is mostly binary, and the current Stick implementation emphasizes mobilization while leaving other domestic variables for future work.

**Source pointers:** `paper.pdf`, Sections 3.2-3.4, 4.1-4.2; Figures 5-7; Listings 1-4

## Claim 2
**Claim:** GPT-4-based WarAgent simulations can reproduce some plausible historical alliance and mobilization patterns, but war-declaration accuracy remains much weaker.

**Evidence:** In the WWI default setting, Table 2 reports GPT-4 scores of 77.78 for alliance accuracy, 54.60 for war declaration, and 92.09 for mobilization. The human evaluation also observes recurring Britain-France, German Empire-Austria-Hungary, and Serbia-Russia alliances across GPT-4 WWI runs.

**Caveats/Scope:** The quantitative evaluation averages seven runs and compares only selected relationship states at chosen historical checkpoints. The paper itself reports lower performance for Claude-2 and GPT-3.5 and notes non-sensible alliances or random war declarations in those models.

**Source pointers:** `paper.pdf`, Sections 6.1.1-6.1.3; Table 2; Listings 5-6

## Claim 3
**Claim:** Anonymization is a central mechanism for reducing direct replay of known historical narratives.

**Evidence:** The paper anonymizes country names, locations, and events, then contrasts anonymized simulations with de-anonymized prompts. De-anonymized WWI simulations align quickly and consistently with historical alliances and mobilization across models, while anonymized simulations produce more varied, sometimes historically non-occurring relations. A GPT-3.5 counterfactual-knowledge fine-tuning experiment still produced global-war outcomes.

**Caveats/Scope:** These experiments do not prove the absence of memorization; they show behavioral differences under the authors' anonymized and de-anonymized prompt regimes. The counterfactual fine-tuning test is limited to GPT-3.5 and the constructed WWI counterfactual dataset.

**Source pointers:** `paper.pdf`, Section 3.4, Section 6.1.4, Appendix A; Tables 3-5

## Claim 4
**Claim:** In the WWI counterfactual trigger study, stronger triggers increased escalation risk, but war was not guaranteed in every run.

**Evidence:** With a null trigger, the three GPT-4 runs produced a cold-war-like standoff with mobilization but no direct war. The Anglo-German naval incident led to war in one of three runs. The Austria-Russia Dardanelles conflict led to global war in two of three runs.

**Caveats/Scope:** The experiment is observational, uses WWI only, uses GPT-4 only, and runs three simulations per trigger. It is best read as exploratory evidence about prompt-conditioned agent dynamics, not as a causal estimate about real history.

**Source pointers:** `paper.pdf`, Section 6.2

## Claim 5
**Claim:** The paper's counterfactual profile edits suggest historical background, key policy, public morale, and agent aggressiveness matter more than raw military capacity or resources in the tested cases.

**Evidence:** More aggressive system prompts produced first-round war declarations, while conservative settings produced alliances, non-intervention treaties, and peace agreements but no war declarations after 10 rounds. Removing the France-German Empire historical grievance removed direct war involvement between them. Modifying U.S. public morale or key policy caused first-round alliance requests with Britain and France in all three simulations. Changing France/German Empire military capacity or resources showed no obvious war-involvement pattern change.

**Caveats/Scope:** The experiments focus on specific countries and prompt edits, with small run counts and qualitative interpretation. The results should not be generalized to all historical settings or treated as validated political theory.

**Source pointers:** `paper.pdf`, Section 6.3; Appendix C

## Claim 6
**Claim:** WarAgent is presented as a suggestive social-simulation aid, not a verified predictor for policy decisions.

**Evidence:** Section 7 explicitly discusses criticisms of social simulation, including simplicity, limited real-world relevance, and verification challenges, and argues that simulation outputs should be interpreted as informative suggestions or rationales. Section 8.1 lists missing mechanisms such as communication time lags, espionage, graded publicity, and variable mobilization timelines.

**Caveats/Scope:** The paper's broader language about peacekeeping and conflict prevention should be read through these limitations. The local review should avoid treating simulated outcomes as reliable forecasts.

**Source pointers:** `paper.pdf`, Sections 7, 8.1, 8.2
