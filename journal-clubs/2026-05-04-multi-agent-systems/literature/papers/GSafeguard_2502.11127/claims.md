# Claims

## Claim 1: Multi-agent safeguards need topology-aware detection.
**Claim:** In LLM-based multi-agent systems, compromised agents can spread harmful information through communication edges, so attack detection should consider the utterance graph rather than only single-agent inputs and outputs.

**Evidence:** The paper formalizes MAS as a graph, defines attack detection over the set of attacked agents, and introduces a multi-agent utterance graph whose node features capture agent utterance histories and whose edge features capture inter-agent interaction histories.

**Caveats/Scope:** This is a modeling and design claim supported by the paper's threat model and experiments; it assumes that communication traces and topology are available to the defense.

**Source pointers:** `paper.pdf`, Sections 2, 3.1, and 3.2; Figure 2

## Claim 2: G-Safeguard reduces malicious information spread under prompt injection.
**Claim:** G-Safeguard lowers attack success rate in many prompt-injection experiments after several rounds of MAS communication.

**Evidence:** Table 1 reports lower R3 attack success rates with G-Safeguard on CSQA and MMLU across chain, tree, star, and random topologies for the evaluated LLMs. The authors summarize average reductions of about 18-20 percentage points in lower-connectivity topologies and about 25 percentage points in higher-connectivity topologies for CSQA and MMLU.

**Caveats/Scope:** The strongest reported improvements are for prompt injection on CSQA and MMLU. GSM8K effects are smaller and sometimes mixed, so this should not be generalized to all task types.

**Source pointers:** `paper.pdf`, Section 4.2, Table 1, Figure 3, Appendix Tables 3-5

## Claim 3: The detector transfers across LLM backbones and topologies.
**Claim:** A G-Safeguard model trained on one MAS data source can identify attackers in MAS instances built from other LLMs and graph structures.

**Evidence:** The paper trains using GPT-4o-mini-generated communication data and evaluates on systems using GPT-4o, LLaMA-3.1-70B, Claude-3.5-haiku, and DeepSeek-V3. Figure 4 reports attacker-recognition accuracy across chain, tree, star, and random topologies under memory attack, and Table 1 shows ASR reductions across multiple LLM/topology combinations.

**Caveats/Scope:** Transfer is empirical within the paper's generated attack scenarios and datasets. The authors note weaker recognition for some GPT-4o and DeepSeek-V3 cases, even though most plotted results exceed 75%.

**Source pointers:** `paper.pdf`, Section 4.2, Figure 4, Table 1

## Claim 4: Edge pruning is the paper's concrete remediation mechanism.
**Claim:** Once risky agents are detected, G-Safeguard remediates attacks by removing their outgoing communication edges for the next interaction round.

**Evidence:** Section 3.3 defines topological intervention by excising outgoing edges from the detected attacker set, with the goal of suppressing adversarial message propagation. The limitation section clarifies that this curtails further dissemination rather than preventing the first compromise.

**Caveats/Scope:** Edge pruning may reduce useful communication from falsely flagged agents and depends on detector accuracy. The method is reactive because it needs communication data before intervening.

**Source pointers:** `paper.pdf`, Section 3.3 and Limitation

## Claim 5: G-Safeguard is evaluated as scaling beyond its training graph size.
**Claim:** The paper argues that G-Safeguard can be trained on a small MAS and applied directly to larger MAS without retraining.

**Evidence:** Section 4.3 trains on an 8-agent MAS and evaluates on systems with 20, 35, 50, 65, and 80 agents. Table 2 reports lower ASR with G-Safeguard across these larger settings, and the authors highlight a 39.23 percentage-point recovery in one 65-agent setting.

**Caveats/Scope:** The scaling result is within the paper's constructed experimental family and does not prove robustness for arbitrary production MAS architectures.

**Source pointers:** `paper.pdf`, Section 4.3, Table 2, Figure 5

## Claim 6: G-Safeguard can be plugged into a role-based MAS benchmark setting.
**Claim:** The safeguard can be integrated into a CAMEL-style multi-role MAS and still identify attackers across different LLM backbones.

**Evidence:** Section 4.4 evaluates attacker recognition in CAMEL-built multi-role systems on CSQA and MMLU. Figure 6 reports recognition accuracy above 80% for the evaluated LLM configurations.

**Caveats/Scope:** This is an experimental integration with constructed attack scenarios, not evidence of deployment in a live production MAS.

**Source pointers:** `paper.pdf`, Section 4.4, Figure 6
