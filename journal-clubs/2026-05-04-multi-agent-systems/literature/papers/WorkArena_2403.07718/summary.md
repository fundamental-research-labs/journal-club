# WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?

**Authors:** Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Leo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, Alexandre Lacoste
**arXiv:** 2403.07718
**Venue:** ICML 2024
**Date:** July 2024

## Problem
Web agents are often evaluated on consumer sites, synthetic UI tasks, or narrow browsing problems, leaving unclear whether they can perform routine enterprise knowledge-work tasks through realistic graphical interfaces. The paper asks how capable LLM-based browser agents are when interacting with complex business software rather than clean benchmark webpages.

## Method
The authors introduce WorkArena, a remote-hosted benchmark on the ServiceNow platform with 33 task types and 19,912 unique instances across lists, forms, knowledge bases, service catalogs, dashboards, and menus. Tasks use natural-language goals, validation functions, and hand-written Playwright oracle functions. They also introduce BrowserGym, an OpenAI Gym-style browser environment with chat-based instructions, accessibility-tree/HTML/screenshot observations, element identifiers, coordinates, browser-tab support, and high-level or Python action spaces. Experiments evaluate GPT-4o, GPT-4o with vision, GPT-3.5, and Llama3-70B agents on WorkArena, MiniWoB, and WebArena, plus ablations of BrowserGym features.

## Key Findings
- WorkArena is substantially harder than simple web-task benchmarks: in the main comparison, GPT-4o reaches 42.7% success, while GPT-3.5 reaches 6.1% and Llama3-70B reaches 17.9%.
- Performance varies sharply by task type: GPT-4o performs well on knowledge-base and service-catalog tasks, but all tested agents get 0% on list-filter tasks.
- The authors attribute difficulty to realistic enterprise UI properties, including dynamic widgets, non-standard HTML, nested frames/shadow DOMs, and very large page observations.
- BrowserGym enables a common evaluation harness across WorkArena, MiniWoB, and WebArena; the paper reports competitive zero-shot results on WebArena with the same agent framework.
- Ablations suggest chain-of-thought prompting is important, while adding more observation/action features, persistent thought history, screenshots, or coordinate actions does not reliably improve WorkArena performance.

## Tags
`web-agents`, `browser-automation`, `ui-agents`, `enterprise-software`, `benchmark`, `ServiceNow`, `BrowserGym`, `WorkArena`, `multimodal-agents`

## Connections
- Complements **WebArena** by shifting web-agent evaluation from consumer/social/developer sites to enterprise workflow software.
- Related to **MiniWoB** and **WebShop** as a harder, more realistic browser-control benchmark with validation and oracle functions.
- Useful alongside agent benchmark papers that test tool use or software engineering agents: WorkArena stresses UI navigation, long page contexts, and business workflow execution rather than code editing.
- Relevant to multi-agent and delegation work because it supplies concrete browser tasks where future teams of agents might need to coordinate UI state, memory, and user handoff.
