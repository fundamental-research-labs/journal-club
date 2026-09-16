# Claims

## Claim 1: Grounded compositional communication can emerge without human language supervision.

**Evidence:** Agents receive private physical goals and a shared task reward, while symbols have no pre-assigned meanings and there are no text corpora, human demonstrations, speaker/listener roles, turn-taking rules, or explicit language-correctness objectives. The learned protocols nevertheless develop a small interpretable vocabulary and syntax.

**Caveats/Scope:** The result is shown in a synthetic two-dimensional particle environment with simple goals and a small abstract symbol vocabulary; it should not be read as natural-language competence.

**Source pointers:** `paper.pdf`, Abstract; Introduction; "Grounded Communication Environment"; Conclusion

## Claim 2: In the main setting, symbolic communication improves cooperative task performance.

**Evidence:** With agents unable to observe each other, the no-communication baseline moves toward the centroid of landmarks. Table 1 reports much better physical reward with communication than without communication on both train and test episodes.

**Caveats/Scope:** This comparison is for the paper's main environment and reward definition; the baseline is deliberately communication-free and non-verbal communication is disabled in this experiment.

**Source pointers:** `paper.pdf`, Experiments; Table 1

## Claim 3: The learned protocols are compositional and context-sensitive.

**Evidence:** In two-agent settings the agents form separate symbols for landmark colors and action types; with more agents they add agent-reference symbols. In simplified settings with only one landmark or one action, symbols for those concepts do not form because the meaning is already clear from context.

**Caveats/Scope:** The symbol labels such as `GOTO`, color names, and agent names are human post-hoc interpretations for visualization; the underlying utterances remain arbitrary learned symbols.

**Source pointers:** `paper.pdf`, Introduction; "Syntactic Structure"; Figures 4 and 5

## Claim 4: Vocabulary-size pressure is an important inductive bias for compositionality.

**Evidence:** The method uses a Dirichlet-Process-inspired penalty to discourage unnecessarily large active vocabularies. Figure 6 shows agents exploring larger vocabularies during training and then settling into smaller active vocabularies that vary with environment complexity.

**Caveats/Scope:** Compositionality is not claimed to arise from reward alone; the vocabulary penalty and training across varied configurations are part of the setup.

**Source pointers:** `paper.pdf`, "Compositionality and Vocabulary Size"; "Symbol Vocabulary Usage"; Figure 6

## Claim 5: Physical grounding shapes both syntax and communication modality.

**Evidence:** The paper argues that `GOTO` is typically uttered first because movement takes time and can begin before the destination is heard. When verbal symbols are disabled but agents can observe gaze or position, they learn non-verbal strategies such as pointing, guiding, and direct pushing.

**Caveats/Scope:** These are qualitative behaviors in the paper's particular physics, sensing, and goal setup; the paper does not establish that the same structures would arise in richer embodied worlds.

**Source pointers:** `paper.pdf`, Introduction; "Syntactic Structure"; "Non-verbal Communication and Other Strategies"; Figure 7
