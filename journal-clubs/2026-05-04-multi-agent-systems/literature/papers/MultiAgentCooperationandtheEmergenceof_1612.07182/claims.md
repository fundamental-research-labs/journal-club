# Claims

## Claim 1
**Claim:** Simple neural sender-receiver agents can learn a discrete communication protocol that solves the two-image referential game.

**Evidence:** The setup gives agents only a success/failure reward for whether the receiver selects the target image. After 50K training games, Table 1 reports 99-100% test communication success across the tested sender architectures, vocabulary sizes, and image representations.

**Caveats/Scope:** The task is a cooperative, two-image forced-choice game with aligned rewards, fixed one-symbol messages, and pretrained CNN visual features. High game success does not mean the protocol is natural language.

**Source pointers:** `paper.pdf`, Sections 2-4; Table 1.

## Claim 2
**Claim:** Sender architecture affects the richness of the learned code even when task success is high.

**Evidence:** Informed senders converge faster in Figure 2 and use between 10 and 58 symbols in Table 1, while agnostic senders reach similar communication success but collapse to a compact two-symbol vocabulary. The SVD analysis argues that the informed sender's extra symbol usage is not merely redundant synonymy.

**Caveats/Scope:** Richness is measured indirectly by used-symbol counts and symbol-usage spectra. The comparison is limited to the paper's two hand-designed sender architectures and fixed hyperparameters.

**Source pointers:** `paper.pdf`, Section 3; Section 4; Figure 2; Table 1.

## Claim 3
**Claim:** Emergent symbols acquire above-chance semantic structure relative to human object categories.

**Evidence:** The paper groups objects by their majority activated symbols and evaluates cluster purity against McRae broad categories. Table 1 reports purity significantly above simulated chance in all configurations, with informed senders higher than agnostic senders; Figure 3 shows visually nearby object vectors often sharing symbols.

**Caveats/Scope:** Purity is far from perfect, and the evaluation relies on predefined McRae categories plus CNN feature geometry. Semantic alignment here is not the same as compositional or conversational natural language.

**Source pointers:** `paper.pdf`, Section 4; Table 1; Figure 3.

## Claim 4
**Claim:** Removing low-level common knowledge can encourage more abstract class-level reference without destroying coordination.

**Evidence:** In the object-level reference variant, sender and receiver see different images with the same target and distractor ImageNet classes, so they cannot coordinate on image-specific details. Table 2 still reports 92-100% communication success and significant above-chance purity, and the text describes a small purity increase.

**Caveats/Scope:** The effect is modest and still depends on ImageNet classes, VGG features, and two-choice referential games. It should be read as an environment-design hint rather than a general recipe for semantic language.

**Source pointers:** `paper.pdf`, Section 4.1; Table 2; Figure 3.

## Claim 5
**Claim:** Mixing referential-game learning with supervised object naming can ground some emergent symbols in conventional labels.

**Evidence:** With an informed sender, fc image features, and a 100-symbol vocabulary, the sender alternates between game play and supervised image classification. The paper reports full coordination after training, 88 used symbols, 70% purity, and exact production of the correct supervised target label in 47% of eligible image pairs versus 1% chance.

**Caveats/Scope:** The supervised task covers only a subset of object labels, and exact label alignment is measured only when the target belongs to those supervised categories. This is lexical grounding, not full natural-language competence.

**Source pointers:** `paper.pdf`, Section 5.

## Claim 6
**Claim:** The grounded code is partially interpretable to humans beyond directly supervised categories.

**Evidence:** In a ReferItGame-derived follow-up, agents again reached perfect communication and used all 100 symbols. In a crowdsourced two-image choice study, human participants selected the target image in 68% of cases from the sender-emitted word, with a significant correlation between true and guessed images.

**Caveats/Scope:** The human evaluation covers 298 selected image pairs and remains far from perfect. Many successful cases rely on indirect or metonymic word-image associations rather than literal object naming.

**Source pointers:** `paper.pdf`, Section 5; Figure 4.
