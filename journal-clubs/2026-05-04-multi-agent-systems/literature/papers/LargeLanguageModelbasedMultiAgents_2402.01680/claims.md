# Claims

## Claim 1
**Claim:** The survey's central contribution is a four-axis taxonomy for LLM-based multi-agent systems: agents-environment interface, agent profiling, agent communication, and agent capability acquisition.

**Evidence:** The introduction says the paper is organized around these unresolved questions, and Section 3 develops the four axes with Figure 2 as the general architecture.

**Caveats/Scope:** This is a survey taxonomy rather than an experimentally validated causal model.

**Source pointers:** `paper.pdf`, Abstract; Section 1; Section 3; Figure 2; Table 1

## Claim 2
**Claim:** The paper groups LLM-MA environment interfaces into Sandbox, Physical, and None.

**Evidence:** Section 3.1 defines Sandbox as simulated or virtual environments, Physical as real-world environments with physical constraints, and None as settings where agents mainly communicate without a specific external environment; Table 1 applies these labels across surveyed work.

**Caveats/Scope:** The grouping reflects the surveyed literature available to the authors, not a complete ontology of all possible environments.

**Source pointers:** `paper.pdf`, Section 3.1; Table 1

## Claim 3
**Claim:** Communication design in LLM-MA systems should be analyzed by paradigm, structure, and content.

**Evidence:** Section 3.3 separates communication paradigms into cooperative, debate, and competitive forms; communication structures into layered, decentralized, centralized, and shared message pool forms; and notes that content is typically textual and application-dependent.

**Caveats/Scope:** The survey describes observed patterns but does not rank which communication design is best for a given task.

**Source pointers:** `paper.pdf`, Section 3.3; Figure 3; Table 1

## Claim 4
**Claim:** Capability acquisition is organized around feedback sources and agent adjustment mechanisms.

**Evidence:** Section 3.4 identifies feedback from the environment, agent interactions, humans, or none, and describes adjustment through memory, self-evolution, and dynamic generation.

**Caveats/Scope:** The mechanisms vary widely by application, and the paper does not benchmark their comparative effectiveness.

**Source pointers:** `paper.pdf`, Section 3.4; Table 1

## Claim 5
**Claim:** The surveyed applications divide into two broad streams: problem solving and world simulation.

**Evidence:** Section 4 explicitly introduces these two streams. Problem-solving examples include software development, embodied agents, science experiments, and science debate; world-simulation examples include society, gaming, psychology, economy, recommender systems, policy making, and disease propagation.

**Caveats/Scope:** The authors note that the field is fast-growing and maintain an external repository for updates, so the paper is a snapshot rather than an exhaustive permanent catalog.

**Source pointers:** `paper.pdf`, Section 4; Table 1; Table 2

## Claim 6
**Claim:** The paper's open challenges emphasize multimodality, hallucination propagation, collective intelligence, scaling and orchestration, evaluation, and broader applications.

**Evidence:** Section 6 has dedicated subsections on multimodal environments, hallucination, collective intelligence, scaling up LLM-MA systems, evaluation and benchmarks, and applications beyond the surveyed set.

**Caveats/Scope:** These are research-agenda claims; the paper motivates them from the survey rather than testing proposed solutions.

**Source pointers:** `paper.pdf`, Sections 6.1-6.6; Section 7
