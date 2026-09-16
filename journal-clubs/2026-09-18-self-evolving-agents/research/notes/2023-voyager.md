# Voyager: An Open-Ended Embodied Agent with Large Language Models

## Source and access

**Source key:** `2023-voyager`.

**Originals and source links:** [register](../sources.md#2023-voyager); [canonical source](https://arxiv.org/abs/2305.16291). retention-restricted. [Manifest](../originals/manifest.json).

**Source:** Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi “Jim” Fan, Anima Anandkumar, “Voyager: An Open-Ended Embodied Agent with Large Language Models,” arXiv:2305.16291, 2023, [canonical record](https://arxiv.org/abs/2305.16291), [full HTML](https://arxiv.org/html/2305.16291), [PDF](https://arxiv.org/pdf/2305.16291), [project](https://voyager.minedojo.org). Accessed 16 September 2026; full HTML methods, experiments, ablations, and limitations reviewed. The arXiv HTML page exposes a CC BY 4.0 license link; repository/code license should be verified before retaining copies.

## Question and methods

Can a black-box LLM agent learn open-ended, long-horizon behavior in Minecraft without gradient updates? Voyager combines (1) an automatic curriculum proposing progressively harder exploration objectives, (2) an ever-growing executable skill library, and (3) iterative prompting using environment feedback, interpreter errors, and self-verification (§1, lines 69–92; §2, lines 93–157). Persistent state is the vector-indexed library of verified programs and the exploration/task history. GPT-4 weights, control primitives, Minecraft simulator, and base prompts remain frozen; GPT-3.5 generates skill descriptions/retrieval queries and some curriculum context (§§2.1–2.3, lines 100–141). New skills are committed only after self-verification (§2.3, lines 146–157).

## Results and evidence

### Evaluation and repeated vs new tasks

Voyager is evaluated in MineDojo against ReAct, Reflexion, and AutoGPT (§1, lines 91–92). The headline outcomes are 3.3× more unique items, key technology milestones up to 15.3× faster, and 2.3× longer traversal (§1, lines 91–92). The learning run is an open-ended stream in one Minecraft world, where the curriculum continually proposes tasks based on state, completed/failed tasks, and exploration progress (§2.1, lines 100–116). Thus much of the gain measures accumulation across a related task stream, not independent iid tasks. The authors additionally test reuse of the learned skill library in a new Minecraft world for novel tasks; they state Voyager can solve these from scratch while other methods struggle (§1, lines 71–73, 91–92). The exact novel-world task count and uncertainty should be taken from the paper’s result tables before using a quantitative transfer claim.

### Ablations and mechanism evidence

Six components are ablated: automatic curriculum, skill library, environment feedback, execution errors, self-verification, and GPT-4 code generation (§3.4, lines 201–214; Appendix B.3). Replacing the curriculum with random selection reduces discovered item count by 93%; removing self-verification reduces it by 73% (§3.4, lines 203–214). Without the skill library, performance tends to plateau later, supporting the role of persistent executable procedures (§3.4, lines 207–210). These are component ablations within the same Minecraft exploration setting, not independent replications or transfer tests.

## Appraisal and limitations

### Authors' claim vs interpretation

Authors describe Voyager as lifelong learning through an automatically growing, reusable, interpretable skill library without parameter fine-tuning (§1, lines 70–88). The evidence supports a strong demonstration of procedural accumulation and some new-world reuse. My interpretation is that Voyager changes the agent’s external program library and curriculum state while keeping the model and tool substrate fixed; it is therefore a predecessor to skill/harness evolution, but not autonomous modification of its own harness or improvement algorithm.

### Limitations

The authors report significant GPT-4 API cost, occasional stuck skill generation, self-verification errors, impossible curriculum proposals, invalid fuel/tool hallucinations, and dependence on GPT-4 quality (§4, lines 226–231). The method can also accumulate executable procedures without a demonstrated long-horizon retirement or regression policy. New-world transfer is promising but narrower than domain-general transfer: the environment, APIs, and task family remain Minecraft. For this session, use Voyager to explain why persistent executable skills can compound capabilities, while asking whether the evaluator, curriculum, and tool interface are themselves allowed to evolve.

## Discussion and follow-up

Which control would separate reusable skill learning from the benefit of additional GPT-4 calls?
