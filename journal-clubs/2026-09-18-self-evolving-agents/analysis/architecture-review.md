# Thesis architecture review

Reviewed September 18, 2026. Scope: the complete current `thesis.md`, all six sections, as an argument about the field. Line references below refer to the unchanged thesis reviewed in this pass. Findings are analyst judgments about structure and inference, not newly established empirical results.

The thesis has a defensible core: retained experience can improve later work, but this is distinct from improving the learning process and from sustained acceleration. Its strongest passages explain WikiSkill's separation of knowledge and skills, compare learning with expert guidance and additional attempts, and distinguish Hyperagents' two transfer experiments. The main problems are in how these pieces fit together. Six structural issues merit revision; the first two affect the meaning of the conclusion.

## Resolution — September 18, 2026

The subsequent authorized rewrite addresses all six findings. This document preserves the review of the prior essay; its line references are historical. The current thesis and coverage audit supersede the proposed outline below.

| Finding | Resolution in current thesis |
| --- | --- |
| Competing endpoints | Opening and conclusion now center on future-task value; improved adaptation and acceleration are separate extensions. |
| Overgeneralized final test | Portable-improver and coupled-feedback controls have different stated attribution targets; cross-domain transplantation is no longer required for all compounding claims. C012 records intervention limits. |
| Method catalog | Developed comparisons replace the list of editable surfaces and scientific-search branch; 27 direct source families remain from the former 40, with all 13 omissions justified in the coverage audit. |
| Conflated failures | Relevance, retention, and interface change are separated from unreliable corrections and evaluator integrity; the validation gate introduces feedback earlier. |
| Insufficient synthesis | The value, relevance, and closing sections develop the conditional recurrence/expertise explanation, with alternative explanations and a discriminating within-protocol test in C011/C012. |
| Implicit learner | The introduction names the complete system and distinguishes proposal, judgment, acceptance, and retention responsibilities, including outside assistance. |

The analysis skill now requires section-level inferences before paper selection, explanatory payoff after results, and a check that section endings accumulate an interpretation. It distinguishes material limitations from audit detail and forbids treating citation reconciliation as a requirement to retain every source in prose. The rewrite preserves consequential counterevidence; the change is in reasoning and emphasis, not evidence status.

## 1. Two central questions compete for the ending — high priority

**Location:** introduction, lines 5–17; final section, lines 101–111. Claims C011–C012, C020–C021.

The opening asks whether experience becomes lasting value through transfer, retention, and affordable adaptation. The final paragraph instead devotes its first two sentences to the requirements for sustained compounding and the failure of WikiSkill and Hyperagents to establish it. Continual learning returns in the last sentence. The introduction does announce the stronger question, so this is a weighting problem rather than an entirely unannounced topic change.

This gives the strongest, least-established claim the role of final verdict. A reader can leave remembering that acceleration remains unproven without a clear answer to when ordinary experience-driven learning is useful. Yet useful continual learning does not need acceleration to justify itself. The coverage audit says the two are separate achievements; the essay's emphasis does not fully deliver that separation.

**Repair:** make lasting future-task value the organizing question throughout. End by synthesizing what the evidence establishes about reuse, comparative value, and durability. Give learned improvement methods a clearly bounded extension of that argument. If recursive acceleration is intended to be the primary subject instead, rebuild the opening and source selection around that question; merely changing the final heading would not resolve the split. The existing README supports the first choice.

## 2. The final test is narrower than the claim it purports to define — high priority

**Location:** lines 81, 97, 105, 109–111. Claims C009, C012, C017, C021.

Line 105 proposes attaching original and learned improvement methods to identical task agents. This is a useful intervention for isolating the value of a transferable method. Line 111 then says that establishing sustained compounding *would require* repeatedly larger gains under that arrangement on new task streams. A particular attribution test has become a universal requirement.

The essay itself supplies reasons to keep these questions separate. Line 81 recognizes learned initializations and generated update data as meta-learning without improver-code rewriting. Task competence and improvement behavior can also develop together. Transplanting one component may test modularity or compatibility as well as learning. Conversely, a portable improver might deliver a one-time advantage without creating repeated positive feedback. Transfer breadth, causal attribution, and acceleration are separate dimensions.

The retained Economics paper explicitly distinguishes narrow acceleration from broad capability spillover (§2.4), and temporary growth spurts from sustained behavior (§2.5). It does not make cross-domain portability to an identical base agent a universal condition. Hyperagents' whole-implementation transfer leaves an attribution gap; that gap should not define all possible self-improvement.

**Repair:** keep the transplant comparison as a proposed test of an independently reusable improvement method. For a coupled system, propose repeated matched-start trajectories with a control that prevents improvements from feeding back into subsequent improvement production. State what the intervention actually isolates. Specify the resource measure, difficulty measure, and observed horizon; reserve extrapolation beyond that horizon as a further claim. Present these as alternative experimental designs, not an already validated universal protocol.

## 3. The mechanism section expands into a catalog before establishing its payoff — medium priority

**Location:** lines 21–41; parallel pattern at lines 83–97.

The WikiSkill explanation has a coherent sequence: what to retain, how the components work, what the comparator establishes. After that, the section successively introduces retry/reflection, executable skills, playbooks, linked memory, harness search, and weight updates. Several blocks at lines 33–39 could exchange places without changing the inference. In the meta-learning section, MemSkill/STOP, the DGM lineage, and the scientific-search examples have a similar partial independence. Parallel comparisons are legitimate, but the essay needs to say what comparing them resolves.

The introduction also explains EWC and GEM mechanisms before the reader reaches a developed modern example. Their historical role is useful; some implementation detail would do more work beside the later retention problem. Removing the foundations entirely would recreate the earlier grounding gap.

**Repair:** retain WikiSkill as the developed case, then choose contrasts for explicit consequences: direct injection versus retrieval changes exposure to irrelevant knowledge; external state versus weight updates changes how interference and rollback occur; changing a task procedure versus its generator changes the claim being tested. Integrate predecessor comparisons where they constrain novelty. Move remaining mechanism detail to supporting notes only when its role has a named representative. Reconcile the prominent-citation audit after any condensation; breadth of reading does not require equal space in the essay.

## 4. One section conflates failure to reuse, bad learning signals, and invalid measurement — medium priority

**Location:** “The next task can change the verdict,” lines 59–75. Claims C007–C008, C010, C015–C016, C019.

The first half asks whether previously useful knowledge remains relevant: task mixing, retention, retrieval, retirement, and changing tools. The second half moves to generated labels, training deterioration, production repair, and evaluator integrity. These are connected, but they fail at different points. A sound lesson can be irrelevant; an applicable lesson can be wrong; an apparent gain can be a measurement error. A single umbrella of durability does not explain which comparison distinguishes them.

This placement also postpones trustworthy feedback until after readers have accepted validation gates as the mechanism selecting useful changes. An evaluator outside edit permissions protects one boundary, but does not by itself establish that the evaluator measures the desired behavior. The existing Shopify qualification recognizes shared blind spots; the structure should preserve that distinction.

**Repair:** introduce the role and limits of feedback when explaining the update gate. Separate the later questions of whether knowledge survives changing work and whether the learning/measurement signal remains trustworthy. Keep R-Zero's decline beside its unresolved causal explanations, and retain the positive internalization counterexample. Use Shopify to explain how these requirements interact in a production design, with its lack of controlled efficacy evidence visible.

## 5. The evidence receives careful caveats but too little comparative synthesis — medium priority

**Location:** lines 31, 47–55, 61–75, and 111.

The reader learns why each result is bounded, but receives less help explaining the pattern across results. FinEvo motivates value from recurring procedures; AgentStream tests heterogeneous work; the harness critique motivates alternative uses of compute. The thesis correctly refuses to pool their scores. It can still develop a conditional explanation of why reuse, task relevance, feedback quality, and the amount of future work might change the payoff.

At present, these factors mostly recur as caveats or proposed controls. The closing sentence names desirable outcomes—transfer, retention, affordability—without synthesizing what design choices could support them. That makes the thesis stronger as an evaluation checklist than as an interpretation of the field.

**Repair:** state a conditional interpretation and its strongest challenge. For example: reusable task structure may make accumulated procedures valuable, while selective access and reliable feedback may determine whether that value survives diverse work; the required development effort must be spread over enough useful reuse. Explicitly label this as synthesis, not a causal result from comparing FinEvo with AgentStream. A discriminating experiment would vary task recurrence and relevance under the same model, feedback, and total resource budget. Include the alternative explanation that differences in benchmark construction or starting expertise account for the apparent pattern.

## 6. The unit that learns and the meaning of “self” remain implicit — medium priority

**Location:** lines 11–15, 25, 37–39, 73, and 85. Claim C001.

The introduction usefully includes memories and software within the learner. But the examples then alternate among a deployed agent retaining experience, a fixed designer searching for a new agent, an outer training process learning an adaptation policy, and an organizational pipeline using stronger models and human annotators. The essay acknowledges several boundaries locally; it lacks one compact explanation tying them together.

Consequently, readers must repeatedly infer whether the improvement belongs to a task agent, a larger optimization system, or the team operating it. “Self” can inadvertently imply more autonomy than the measured process has. The claim ledger already contains the necessary distinction: it identifies which update decisions the agent controls.

**Repair:** establish early that the analysis follows the complete learning system, while naming who proposes changes, supplies feedback, accepts updates, and retains state. Distinguish offline development from adaptation during subsequent use. Carry those boundaries through the main examples. Do not rank more autonomous systems as more effective without a comparison supporting that claim.

## Proposed argument structure

The central claim should be that experience has demonstrated bounded value for later tasks, while its practical payoff depends on what is retained, where it applies, how changes are validated, and the cost of reuse. Improving the process that produces those changes is a further achievement with a separate evidence burden.

1. Establish the inherited problem: accumulating useful capability while adapting, with the complete system as the learner and explicit limits on what “self” means.
2. Explain how experience becomes a reusable change, using WikiSkill and a small number of consequential contrasts. Introduce feedback and acceptance here.
3. Ask whether producing that change adds value beyond a strong starting procedure and additional attempts. Use FinEvo and the harness critique; make the reuse horizon explicit.
4. Ask whether the value survives later work. Separate relevance, retention, environmental change, and feedback failures, then synthesize the conditions suggested by the evidence.
5. Ask whether experience can improve the learning process itself. Develop Hyperagents' positive transfer evidence and unresolved attribution, then bound the separate acceleration question.
6. Conclude with the supported account of useful experience-driven learning and the few experiments that would discriminate the remaining explanations. Keep detailed evaluation protocol in supporting analysis if it overwhelms the conclusion.

This is an essay dependency outline, not a slide sequence. Preserve the strongest positive and negative evidence, historical grounding, predecessor comparisons, and source-specific qualifications. The revision needs a clearer hierarchy, not a larger source inventory.

## Review scope and verification

Read the complete thesis and checked its section openings, introduction–conclusion alignment, movable paragraph groups, and proposed tests. Consulted the README, landscape, source register, claim ledger, coverage audit, prominent-citation aggregate/reconciliation, workflow, and relevant reading notes. Checked acquisition records before reopening retained WikiSkill v1, Hyperagents v1, and Economics of Recursive Self-Improvement v1 passages. WikiSkill's method/setup, Hyperagents' transfer comparisons, and the Economics paper's narrow/broad distinction support the boundary checks above. Other empirical statements retain their earlier recorded review depth.

This review reuses the September 16 frontier cutoff and September 18 foundation revision. It introduces no new literature findings, numerical corrections, experiments, or freshness claim. At the time of the review, the thesis, claim ledger, and presentation had not been rewritten; the resolution above records the later analysis revision. Existing source-access and evidence limitations remain. A structural revision should update C012's proposed-test wording, preserve C001/C009/C020/C021's distinctions, and reconcile actual essay coverage before a new presentation handoff.
