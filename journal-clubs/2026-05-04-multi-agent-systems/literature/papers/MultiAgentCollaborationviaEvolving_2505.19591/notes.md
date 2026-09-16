# Notes

## Why It Matters
This paper is a useful bridge between static LLM-agent workflows and learned agent orchestration. Its core contribution is not another fixed role-play pattern, but a cost-aware policy that decides which reasoning or tool agent should act next as task state evolves. That makes it relevant for scalable MAS design, especially where redundant agent calls and coordination overhead are the bottleneck.

## When To Cite
Cite it when discussing dynamic multi-agent orchestration, RL-trained agent routing, graph-of-thought-style agent topologies, cost-aware multi-agent inference, or empirical evidence that learned coordination can produce compact cyclic reasoning structures. It is also useful as a counterpoint to papers showing multi-agent coordination failures, because it proposes an explicit mechanism for adapting the collaboration structure.

## Key Terms
Puppeteer; centralized orchestrator; puppet agents; dynamic orchestration; adaptive evolution; REINFORCE; serialized orchestration; agent activation policy; graph-of-thought; Mimas subspace; Titan subspace; Puppeteer-Mono; compact topology; cyclic reasoning; token-cost reward; Terminator agent.
