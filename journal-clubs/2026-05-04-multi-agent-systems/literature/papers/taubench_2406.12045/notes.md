# Notes

## Why It Matters
tau-bench is a compact benchmark for a deployment-relevant agent setting: a model must talk to a user, collect missing information, use APIs, obey written policies, and make the same correct decision across repeated interactions. Its pass^k framing is especially useful because it makes reliability, not just average task success, part of the benchmark target.

## When To Cite
Cite this paper when discussing tool-using language agents, customer-service agents, LM user simulators, multi-turn human-agent interaction, policy-following evaluation, database-state rewards, or reliability metrics for agents. It is also useful as evidence that strong function-calling models can still fail on realistic API workflows involving partial information and domain-specific rules.

## Key Terms
- tau-bench
- Tool-Agent-User Interaction Benchmark
- tau-retail
- tau-airline
- function calling
- LM-simulated user
- domain policy
- database-state evaluation
- pass^k
- pass@k
- POMDP
- rule following
- compound requests
