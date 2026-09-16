# Claims

## Claim 1
**Claim:** Virtual context management can extend a fixed-context LLM by letting the model page information between prompt memory and external stores.

**Evidence:** MemGPT defines main context as the prompt tokens and external context as out-of-context data, then gives the LLM function calls for editing working context, searching recall storage, searching archival storage, and chaining calls before responding. Figure 3 summarizes the architecture.

**Caveats/Scope:** This is a system architecture claim, not a guarantee that every function-calling model will manage memory well. Results depend on prompt design, storage/retrieval quality, and the underlying LLM's ability to call tools reliably.

**Source pointers:** `paper.pdf`, Abstract; Section 2; Figure 3; Section 2.4

## Claim 2
**Claim:** MemGPT improves long-term conversational consistency on the paper's deep memory retrieval benchmark.

**Evidence:** In the Multi-Session Chat DMR task, MemGPT variants substantially outperform their fixed-context counterparts in Table 2: for example, GPT-4 rises from 32.1% to 92.5% accuracy and GPT-4 Turbo rises from 35.3% to 93.4%.

**Caveats/Scope:** The benchmark augments MSC with generated session-6 questions and uses an LLM judge plus ROUGE-L recall; the fixed-context baseline receives a summary of prior conversations rather than full paginated history.

**Source pointers:** `paper.pdf`, Section 3.1.1; Table 2; Appendix 6.1.1-6.1.3

## Claim 3
**Claim:** Persistent memory can make conversation openers more personalized and engaging.

**Evidence:** On the conversation opener task, MemGPT-generated openers score at or above the human opener on persona-similarity metrics SIM-1 and SIM-3 across the tested base models, and the text notes that MemGPT tends to produce more verbose openers covering more persona information.

**Caveats/Scope:** The metric rewards overlap with gold persona labels, so it measures use of remembered persona facts more directly than human-perceived engagement. SIM-H remains highest for the human-written opener by construction.

**Source pointers:** `paper.pdf`, Section 3.1.2; Table 3

## Claim 4
**Claim:** In document QA, MemGPT can use iterative archival search to operate over more documents than fit in the model's prompt.

**Evidence:** The document QA setup loads the document set into archival storage and lets MemGPT repeatedly query paginated search results. The paper argues this removes the fixed-context limit on the number of retrieved documents the agent can inspect, while fixed-context baselines are bounded by whatever retrieved documents are placed in the prompt.

**Caveats/Scope:** MemGPT still depends on embedding search surfacing useful candidates somewhere in the ranking, and the paper notes that document QA is challenging for all methods because of retriever limitations. GPT-3.5 performance degrades due to weaker function calling.

**Source pointers:** `paper.pdf`, Section 3.2.1; Figure 5; Figure 6; Appendix 6.1.4-6.1.5

## Claim 5
**Claim:** MemGPT's function-chaining memory loop supports multi-hop retrieval better than plain fixed-context prompting in the nested KV task.

**Evidence:** The nested key-value task requires repeatedly looking up values that may themselves be keys. The paper reports that GPT-3.5 drops to 0% at one nesting level, GPT-4 and GPT-4 Turbo hit 0% by three nesting levels, while MemGPT with GPT-4 remains unaffected across the tested nesting levels.

**Caveats/Scope:** This is a synthetic retrieval task with 140 UUID key-value pairs and sampled ordering configurations; it tests controlled multi-hop lookup rather than broad reasoning.

**Source pointers:** `paper.pdf`, Section 3.2.2; Figure 7; Figure 8; Appendix 6.1.6
