# Claims

## Claim 1: tau-bench evaluates interactive tool use under domain policies.

**Evidence:** The benchmark setup gives the agent a domain policy, access to database API tools, and an LM-simulated user. The agent must converse with the user while reading/writing hidden databases through tools, and task success depends on the final database state plus required user-facing outputs.

**Caveats/Scope:** The first release demonstrates the framework in synthetic customer-service domains rather than arbitrary real deployments.

**Source pointers:** Abstract; Section 3, "tau-bench: A benchmark for Tool-Agent-User Interaction"; Figure 1; Figure 2.

## Claim 2: The benchmark trades task quantity for carefully annotated, repeatable evaluation.

**Evidence:** Task instances include hidden user instructions and annotations of ground-truth database write actions and outputs. The reward compares the final database to a unique goal state, and Table 1 reports 115 tau-retail tasks and 50 tau-airline tasks.

**Caveats/Scope:** The paper notes that the rule-based reward is not a sufficient condition for perfect real-world behavior, because an agent could reach the right database state while violating a policy such as explicit confirmation.

**Source pointers:** Section 3, "Task instances" and "Reward"; Section 4, "Benchmark Construction"; Table 1; Discussion.

## Claim 3: pass^k measures reliability across repeated user-agent trajectories.

**Evidence:** The paper defines pass^k as the chance that all k independent trials of a task succeed, averaged across tasks. It is motivated by customer-service reliability, where an agent should consistently handle semantically identical requests despite stochastic variation in dialogue.

**Caveats/Scope:** pass^k depends on the simulator and agent sampling setup; it measures repeated success on the same benchmark tasks, not all forms of deployment robustness.

**Source pointers:** Section 3, "Pass^k metric"; Section 5.1, "Agent consistency via pass^k"; Figure 4.

## Claim 4: Current function-calling agents remain far from reliable on tau-bench.

**Evidence:** In the main model comparison, gpt-4o is the best function-calling model but reports 61.2 pass^1 on tau-retail, 35.2 on tau-airline, and 48.2 average. The authors emphasize that all models remain far from solving the benchmark.

**Caveats/Scope:** Results are for the tested June 2024-era models, the paper's function-calling/ReAct/Act baselines, and at least three trials per task for main results.

**Source pointers:** Section 5, "Experiments"; Section 5.1, "Main results"; Table 2.

## Claim 5: Consistency degrades rapidly as repeated-trial requirements tighten.

**Evidence:** The paper reports that gpt-4o function calling has over 60 average task success on tau-retail at pass^1 but falls below 25 at pass^8, showing that repeated stochastic conversations expose instability hidden by average success.

**Caveats/Scope:** The detailed pass^k plot is reported for tau-retail, so the same numerical trend should not be assumed for every domain without evaluation.

**Source pointers:** Abstract; Section 5.1, "Agent consistency via pass^k"; Figure 4.

## Claim 6: Failures cluster around database reasoning, rule following, and compound requests.

**Evidence:** The tau-retail failure analysis of gpt-4o function calling identifies wrong arguments or wrong user-facing information, wrong policy-driven decisions, and partial resolution of multi-request tasks. The policy-removal ablation further shows a large gpt-4o drop on tau-airline, where rules are more complex and ad-hoc.

**Caveats/Scope:** The manual failure breakdown focuses on tau-retail and one strong baseline; it is diagnostic rather than a complete taxonomy for all agents.

**Source pointers:** Section 5.2, "Research challenge analysis"; Figure 5; Figure 6; Table 3; Appendix C.2 examples.
