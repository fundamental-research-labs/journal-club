# Suggested Manuscript Integration

These are narrow, additive citation opportunities for
`manuscript/multi-agent-review-draft/index.qmd`.

## Introduction and Scope

Add one sentence after the paragraph describing early systems:

> By 2025, the same design vocabulary had become product infrastructure:
> OpenAI, Google, AWS, Microsoft, Anthropic, Salesforce, and ServiceNow were
> shipping SDKs, protocols, managed supervisors, agent fabrics, and observability
> layers for multi-agent or multi-agent-adjacent workflows.

Candidate citations:

- OpenAI Agents SDK / AgentKit: `openaiAgentsTools2025`, `openaiAgentKit2025`
- Google A2A / ADK: `googleA2A2025`, `googleADK2025`
- AWS Bedrock MAC: `awsBedrockMultiAgent2024`, `awsBedrockMAC2025`
- Salesforce / ServiceNow enterprise fabrics: `salesforceAgentforce3_2025`,
  `servicenowAIFabric2025`

## From Prompts to Runtimes

This section is the best place to add industry references. The current paragraph
already mentions AutoGen, Magentic-One, OpenHands, and related frameworks. Add a
short follow-on paragraph:

> Industry platforms made the same shift visible outside the paper literature.
> OpenAI's Agents SDK exposed handoffs and agents-as-tools; Google released ADK
> and A2A for multi-agent development and interoperability; AWS Bedrock added a
> managed supervisor/subagent collaboration model; and enterprise platforms such
> as Salesforce Agentforce and ServiceNow AI Agent Fabric framed agents as
> managed, observable workforces rather than isolated chatbots.

Use citations:

- `openaiAgentsTools2025`
- `googleADK2025`
- `googleA2A2025`
- `awsBedrockMultiAgent2024`
- `salesforceAgentforce3_2025`
- `servicenowAIFabric2025`

## The Coordination Reality Check

The Cognition and LangChain posts would strengthen the manuscript's practical
critique without weakening the academic tone. Add them as industry commentary,
not as experimental evidence:

> This concern is echoed in practitioner reports. Cognition argues that coding
> agents fail when subagents do not share full traces and when independent
> actions encode conflicting implicit decisions. LangChain's multi-agent
> benchmarks similarly identify supervisor "translation" and context clutter as
> practical causes of degradation.

Use citations:

- `cognitionDontBuildMultiAgents2025`
- `langchainBenchmarkMultiAgent2025`
- `langchainWhenMultiAgent2025`

## Mechanisms of Multi-Agent Value

The Anthropic Research system is especially useful for the "read-heavy vs
write-heavy" distinction:

> Production reports suggest a useful distinction between read-heavy and
> write-heavy multi-agent systems. Anthropic's Research system uses parallel
> subagents primarily to gather evidence, while a lead agent synthesizes the
> final answer; LangChain argues that this is easier to stabilize than workflows
> where multiple agents concurrently mutate a shared artifact.

Use citations:

- `anthropicMultiAgentResearch2025`
- `langchainWhenMultiAgent2025`

## Verification and Artifacts

Add industry coding-agent examples after the CAID paragraph or before it:

> Commercial coding agents are converging on the same artifact-centered pattern:
> isolated workspaces, logs, tests, branches, pull requests, and human review.
> OpenAI Codex, GitHub Copilot coding agent, Cursor Background Agents, and
> Claude Code on the web all expose versions of this delegated task portfolio.

Use citations:

- `openaiCodex2025`
- `githubCopilotCodingAgent2025`
- `cursorBackgroundAgentsDocs`
- `anthropicClaudeCodeWeb2025`

## Governing Shared State

Add a short paragraph after the safety/control bullet list:

> Enterprise agent platforms are already turning this into a control-plane
> problem. Salesforce Agentforce 3 emphasizes session tracing, observability,
> MCP-based tool connectivity, and command-center monitoring; ServiceNow's AI
> Agent Fabric frames agent-to-agent, agent-to-tool, and system-to-system
> communication as governed infrastructure; Google A2A similarly treats
> cross-agent communication as an interoperability layer.

Use citations:

- `salesforceAgentforce3_2025`
- `servicenowAIFabric2025`
- `googleA2A2025`

## Orchestration as a Control Problem

Add after the trace-format research question:

> Industry systems point in the same direction: production agent platforms now
> sell not only agents, but also traces, evals, command centers, sandboxes,
> connector registries, and protocol layers.

Use citations:

- `openaiAgentKit2025`
- `openaiAgentsSdkEvolution2026`
- `salesforceAgentforce3_2025`
- `servicenowAIFabric2025`
- `cursorBackgroundAgentsDocs`

## Citation Caution

Recommended wording:

- "Industry reports suggest..."
- "Production platforms increasingly expose..."
- "Product documentation shows..."
- "Practitioner accounts argue..."

Avoid wording:

- "This proves..."
- "Industry systems demonstrate that multi-agent systems improve..."
- "The best architecture is..."

Product posts are strong evidence for what builders are shipping and what
problems they consider important. They are weak evidence for causal performance
claims unless they include detailed evaluation methods, baselines, costs, and
failure analysis.
