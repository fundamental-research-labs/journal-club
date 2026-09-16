# Reflexion: Language Agents with Verbal Reinforcement Learning

## Source and access

**Source key:** `2023-reflexion`.

**Originals and source links:** [register](../sources.md#2023-reflexion); [canonical source](https://arxiv.org/abs/2303.11366v4). Retained unmodified: [2023-reflexion-paper-v4.pdf](../originals/2023-reflexion/2023-reflexion-paper-v4.pdf). Paper license: http://creativecommons.org/licenses/by/4.0/. [Manifest](../originals/manifest.json).

**Source:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao, “Reflexion: Language Agents with Verbal Reinforcement Learning,” arXiv:2303.11366, v4 (10 October 2023), [canonical record](https://arxiv.org/abs/2303.11366), [full HTML](https://arxiv.org/html/2303.11366), [PDF](https://arxiv.org/pdf/2303.11366). The HTML identifies the paper as CC BY 4.0 (header, lines 58–60); code and datasets are released at [github.com/noahshinn024/reflexion](https://github.com/noahshinn024/reflexion), whose current license should be checked before redistribution. Accessed 16 September 2026; full HTML methods, experiments, appendices, and limitations reviewed.

## Question and methods

### Question and mechanism

Can an LLM agent improve from trial feedback without weight updates? Reflexion separates an Actor, Evaluator, and Self-Reflection model. After each trajectory, the evaluator supplies a score, the reflection model turns the trajectory and score into verbal feedback, and that text is appended to memory for the next trial (Algorithm 1 and §§3.1–3.5, lines 126–179). The editable/persistent state is the episodic text memory (`mem`, bounded in practice to 1–3 experiences); actor/evaluator/reflection model weights, prompts, action space, and environment remain fixed (§§3.4–3.5, lines 173–179). It is therefore in-context adaptation and policy-as-memory, not parameter learning or code/harness evolution.

### Experiments and denominators

ALFWorld uses 134 environments across six task types (§4.1, lines 181–188). Reflexion completes 130/134 with the heuristic self-evaluation setup and reports learning over 12 consecutive trials; the baseline plateau and the Reflexion curve are across repeated attempts on the same environments (§4.1 results, lines 189–196). This is within-task retry learning, not an unseen-task generalization test. HotPotQA evaluates 100 questions; ReAct/CoT agents retry failed questions, with up to three consecutive failed attempts, and the memory contains three experiences (§4.2, lines 197–207). Again, improvement is measured on repeated questions. Programming evaluates HumanEval and MBPP in Python and Rust plus a new 40-question LeetcodeHardGym; generated tests are capped at six and programming memory at one experience (§4.3, lines 211–216). Table 1 reports pass@1: HumanEval Python 91.0, HumanEval Rust 68.0, MBPP Python 77.1, MBPP Rust 75.4, Leetcode Hard Python 15.0 (Table 1, lines 217–224). The paper’s “pass@1” is within the iterative Reflexion protocol, so it should not be read as a single-shot score unless the exact evaluation condition is preserved.

## Results and evidence

### Transfer and ablations

The paper’s main evidence is repeated-task improvement. It does not establish broad held-out transfer of memories across task distributions. The WebShop appendix is useful counterevidence: on 100 shopping environments, runs are stopped after four trials because Reflexion shows no improvement; the authors attribute this to local minima and insufficiently diverse exploration (Appendix B.1, lines 368–372). Additional-model results on 100 HotPotQA questions vary by base model (Table 5, lines 305–313), and a weaker starchat-beta HumanEval result is 0.26 for both baseline and Reflexion (Table 4, lines 299–304), indicating the method depends on the model’s ability to produce useful self-corrections.

## Appraisal and limitations

### Authors' claim vs interpretation

Authors claim verbal feedback acts as a semantic gradient and produces gains across sequential decision making, reasoning, and coding (§1, lines 65–80). The evidence supports a narrower claim: bounded textual memory can improve repeated attempts when feedback is grounded and the model can use it. My interpretation is that Reflexion established a durable-memory primitive and an important evaluation warning: “learning” curves may reflect retries on the same item. The paper does not show that the memory improves unseen tasks, survives changing interfaces, or improves the procedure that generates future updates.

### Strengths, limits, and orientation value

Strengths are modular attribution (actor/evaluator/reflection), interpretable stored updates, grounded feedback from environments/tests, and explicit ablations. Limits include evaluator/self-reflection reliability, short memory windows, task-specific heuristics, repeated-task evaluation, no weight or code changes, and failure on exploration-heavy WebShop. For this session, use Reflexion as the historical contrast between changing retained context and changing the harness itself. It is foundational orientation, not a top candidate for self-evolving-agent evidence.

## Discussion and follow-up

How would the conclusion change if every evaluation used a new task instead of another attempt on the same task?
