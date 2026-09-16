# Claims

## Claim 1
**Claim:** Mind2Web broadens web-agent evaluation beyond narrow or simulated environments.

**Evidence:** The dataset uses real-world websites and reports 2,350 retained tasks from 137 websites across 31 domains, with high-level task descriptions and an average of 1,135 page elements. Table 1 contrasts this scope with prior web/mobile datasets that use simplified websites, fewer environments, or lower-level instructions.

**Caveats/Scope:** The coverage is still mostly English-language, U.S.-oriented websites, and tasks are proposed by MTurk annotators rather than all possible user populations.

**Source pointers:** Abstract; Section 2.2; Section 2.3; Table 1; Section 6.

## Claim 2
**Claim:** The benchmark frames web automation as high-level instruction following over grounded action sequences.

**Evidence:** Each instance includes a task description, an action sequence of target-element and operation pairs, and webpage snapshots. Supported operations cover common browser interactions such as click, type, and select option, and actions can span multiple pages of a website.

**Caveats/Scope:** Evaluation is based on cached snapshots and recorded traces, so it is not a fully live online environment and may miss alternative valid paths that were not cached.

**Source pointers:** Section 2.1; Figure 2; Section 2.2; Section 6; Appendix C.1.

## Claim 3
**Claim:** A two-stage model is a practical way to handle large real-world HTML pages.

**Evidence:** MindAct first uses a fine-tuned DeBERTa cross-encoder to rank DOM elements, then asks an LLM to choose among filtered candidates and predict the operation. The paper reports Recall@50 of 88.9%, 85.3%, and 85.7% for cross-task, cross-website, and cross-domain candidate generation.

**Caveats/Scope:** Candidate generation can still bottleneck downstream action prediction, and the main MindAct setup uses textual HTML context rather than rendered visual information.

**Source pointers:** Section 3; Figure 3; Figure 4; Section 4.3; Section 6.

## Claim 4
**Claim:** The multiple-choice MindAct formulation improves step-level action prediction over direct generation and classification baselines.

**Evidence:** Table 2 shows the best Flan-T5 MindAct variant reaching 52.0% step success on cross-task evaluation and roughly 39% step success on unseen websites/domains, above the listed generation and classification baselines where comparable metrics are available.

**Caveats/Scope:** Whole-task success remains low because every step must be correct, and step-wise evaluation supplies the ground-truth action history rather than rolling out accumulated model errors.

**Source pointers:** Section 3.2; Table 2; Section 4.2; Section 4.3.

## Claim 5
**Claim:** Generalizing from familiar tasks to unfamiliar website structures remains a major challenge.

**Evidence:** The paper reports that all models perform best on the cross-task split, with an average step-success gap of more than 10 absolute points compared with cross-website and cross-domain settings. It interprets the similar cross-website and cross-domain results as evidence that page design and interaction logic are harder than domain labels alone.

**Caveats/Scope:** The conclusion is tied to the paper's split design and offline evaluation setup; different website distributions or live interaction may change the relative difficulty.

**Source pointers:** Section 4.1; Figure 6; Section 4.3.

## Claim 6
**Claim:** The paper identifies several open problems for deployable generalist web agents.

**Evidence:** The limitations section highlights dataset representation limits, missing multimodal page information in MindAct, limited modeling of interaction dynamics, lack of mid-task human-agent interaction, offline-vs-online evaluation issues, and safety concerns around sensitive or malicious web actions.

**Caveats/Scope:** These are prospective limitations and research directions rather than fully evaluated failure modes.

**Source pointers:** Section 6; Section 7.
