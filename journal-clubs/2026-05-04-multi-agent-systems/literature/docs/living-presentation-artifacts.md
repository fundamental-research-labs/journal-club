# Living Presentation Artifacts

## Premise

PowerPoint was historically significant because it made business presentation production self-service. It did not invent slides; it gave knowledge workers a practical container for composing, presenting, and sharing ideas without depending on a graphics department, slide bureau, or specialized production workflow.

The AI-native successor should probably not be "a deck with an AI chat box." It should also not be "any folder of files plus an LLM." The useful target is a bounded artifact for helping a group understand, discuss, and decide.

Working definition:

> A living presentation artifact is a shareable, bounded, interactive object that combines narrative, evidence, visuals, data, and agent-mediated Q&A to help an audience move from context to understanding or decision.

## Why PowerPoint Worked

PowerPoint's strength came from a productive level of constraint:

- A finite sequence: the deck
- A bounded surface: the slide
- A small set of primitives: text, image, shape, chart, table
- A presentation mode: one person can lead a group through the material
- A leave-behind mode: others can read the artifact later

This constraint made the format general enough to express many business ideas, but not so general that it became arbitrary software. You can use PowerPoint for strategy, sales, education, status reporting, and fundraising; you generally do not use it for music editing, database administration, or long-form software workflows.

## The New Boundary

The next dominant presentation form should preserve that boundedness while changing the primitives.

It should exclude:

- A random collection of files with a generic chatbot
- A general-purpose website or application with no authored communicative shape
- A pure dashboard that exposes data but does not guide interpretation
- A static document that cannot support questions, inspection, or scenario changes

It should include:

- A default narrative path
- Inspectable claims and evidence
- Interactive views
- Scoped agent assistance
- Stable versions or snapshots
- A mode for live presentation and a mode for asynchronous reading

The primary job is explanation, persuasion, alignment, and decision-making.

## Layers

### Narrative Layer

There should still be a default path. Someone should be able to press "present" and guide an audience through the argument:

- What is the topic?
- Why does it matter?
- What evidence exists?
- What choices are available?
- What recommendation is being made?
- What happens next?

Without this layer, the artifact becomes an information space rather than a presentation.

### Evidence Layer

Every important claim should be connected to underlying material: source documents, spreadsheets, interview notes, dashboards, code, customer tickets, financial models, citations, or transcripts.

The audience should be able to ask where a number came from, inspect the assumptions behind a claim, and see counterexamples or uncertainty. Traditional decks often hide evidence; living artifacts should make evidence inspectable.

### Interaction Layer

Interaction should serve understanding rather than novelty. Useful interactions include:

- Filtering a chart
- Changing assumptions
- Comparing scenarios
- Drilling into a claim
- Asking questions
- Generating an explanation for a different audience
- Simulating timing, pricing, staffing, or roadmap alternatives

This makes the format closer to a website than a deck, but still bounded by the communicative purpose.

### Agent Layer

The agent should be scoped to the artifact. It is not the artifact itself.

The bad version is a pile of files plus a chatbot. The better version is an authored argument with a corpus, data model, permissions, and an agent that can answer questions, explain assumptions, create alternate views, reveal provenance, and help the presenter adapt to the audience.

### Snapshot Layer

Living artifacts need stable versions. A serious organizational conversation needs a canonical snapshot: "This is the version reviewed on May 4, 2026."

Liveness is valuable, but accountability requires versioning. The successor to PowerPoint needs both.

## Possible Primitives

The new primitives are probably less like slide objects and more like communicative objects:

- Claim
- Evidence
- View
- Data object
- Scenario
- Decision
- Question
- Annotation
- Action

The "slide" may become a view: a composed screen that can contain text, charts, simulations, embedded media, source excerpts, live components, or agent-generated explanations. Views can still be sequenced, but they can also be branched and queried.

## Core Design Tension

The hard problem is preserving authorial intent.

PowerPoint works because the creator controls order, emphasis, and pacing. AI-native artifacts can become infinitely explorable but lose their spine. The winning form likely needs both:

> A strong default narrative path, plus controlled explorable depth around each point.

In short, the successor to PowerPoint should be bounded like a deck, explorable like a website, evidenced like a research workspace, and conversational like an agent.
