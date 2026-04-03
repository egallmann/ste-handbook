# STE Handbook

## What is System of Thought Engineering (STE)?

**System of Thought Engineering (STE)** is a model-driven discipline for software-intensive systems in which **architecture is treated as an explicit, versioned system of decisions under constraints**. Intent is captured in structured, reviewable artifacts, compiled into a **canonical architecture model (Architecture IR)** that teams can query, diff, and trace, and assessed against **embodiment** (code, configuration, and operational reality) using **evidence-linked validation** (deterministic where that is appropriate, judgment where it is not). STE’s through-line is **governance over time**: decisions stay recoverable, drift becomes visible, and change stays tied to explicit assessment rather than silent divergence.

The **STE Handbook** explains that discipline: how the pieces fit, why they matter, and how they support bounded, safe use of automation. It is **explanatory, not normative**. When narrative and specification disagree, **`ste-spec` is authoritative** for what the system must do and mean.

## What problem STE solves

Organizations routinely suffer **lossy reasoning**: rationale thins across handoffs, **documentation drift** diverges from what was actually decided, and **architecture drift** shows up as mismatch between declared intent and the running system. Informal architecture hides commitments in chat, tickets, and one-off diagrams, so the group cannot reliably answer what was chosen, why, or whether it still holds.

That gap is sharper when **tools and agents** participate in design and implementation: without **machine-readable intent**, durable constraints, and repeatable assessment, automation tends to **accelerate inconsistency** rather than align with decisions. STE targets the structural failure modes: **untraceable intent**, **unowned drift**, and **unrepeatable validation**, not “people ignoring docs.”

## The STE pipeline

End-to-end, STE is often described as:

**Conversation → requirements → ADRs → rules → Architecture IR → runtime (evidence)**

Conversation and interrogation surface intent; **requirements** and **constraints** bound the design space; **Architecture Decision Records (ADRs)** record decisions with rationale; **rules** encode what must hold, what evidence counts, and how assessments map to admission or change; the **Architecture IR** is the compiled, canonical model; **runtime** and related embodiment produce **evidence** that closes the loop through validation and governance. Exact stages and contracts are defined in **`ste-spec`** and supporting repositories.

## Purpose of this repository

This repository publishes the **STE Handbook** manuscript: long-form technical documentation that explains concepts, relationships, lifecycle, and end-to-end flows. It is structured as a book manuscript suitable for sustained reading and for tooling that needs a stable outline. The handbook **orients** readers and connects narrative to **`ste-spec`** and implementation repositories; it does not replace them.

## The STE repositories

| Repository | Role |
|------------|------|
| **`ste-spec`** | Normative specification: contracts, invariants, semantic constraints, and boundaries other STE work relies on. |
| **`ste-handbook`** | This repository: explanatory manuscript, lifecycle narrative, and orientation. |
| **`ste-runtime`** | Runtime integration and execution concerns that connect live systems to STE evidence and assessment flows (as defined in that repository). |
| **`adr-architecture-kit`** | Tooling and patterns for authoring and managing architectural intent (including ADR surfaces) that feed the STE pipeline. |
| **`ste-kernel`** | Decision and admission logic that consumes evidence and published contracts to make deterministic orchestration decisions. |

## How humans work with STE

Humans remain the source of **judgment**, **trade-offs**, and **governance**. Typical use is conversational and iterative: clarify intent, capture decisions in durable artifacts, compile or refresh the **Architecture IR**, and run assessments against evidence when embodiment changes. STE is not “the machine replaces architects”; it is **structured intent plus evidence-linked validation** so humans and carefully bounded automation do not amplify silent drift. **Part 9 (Human interface)** and **Part 10 (AI interface)** expand conversation, decision capture, and rule-governed agent surfaces.

## How to read this handbook

The manuscript is organized as **Parts 0 through 13**. **[SUMMARY.md](SUMMARY.md)** is the table of contents and suggested reading order.

- **Orientation:** Part 0 (problem and thesis) and Part 2 (overview, terminology, system picture, lifecycle summary, and how to read diagrams and projections).
- **Depth along the spine:** Part 3 (artifacts) → Part 4 (Architecture IR) → Part 5 (lifecycle stages) → Part 6 (governance control model) → Part 7 (kernel) → Part 8 (runtime).
- **Interfaces:** Part 9 (human), Part 10 (AI).
- **Examples:** Part 11.

For a short thesis statement, see **[STE-MANIFESTO.md](STE-MANIFESTO.md)**.

### Section map (Parts 0 through 13)

| Part | Title | Role |
|------|--------|------|
| 0 | Problem | Problem, thesis, and vocabulary precursors. |
| 1 | Theory | Disciplinary scaffolding (systems, information, control, cybernetics, decision theory, safety, software architecture, MBSE, synthesis). |
| 2 | Overview | What STE is, terminology, system overview, lifecycle summary, and how to read diagrams and projections. |
| 3 | Artifacts | ADRs, requirements, invariants, Architecture IR connection, evidence, traceability, conformance, publication versus projection. |
| 4 | Architecture model | Canonical system model (IR), compilation, traceability, diff, graph view, projections as model-facing views, and an illustrative artifact walkthrough. |
| 5 | Lifecycle | Lifecycle stages: intent through evidence, conformance, decisions, change, and state transitions. |
| 6 | Governance | Governance control model: authority and decision rights, admission and eligibility, enforcement posture, steelman and change control, determinism and audit (Part 5 carries the staged lifecycle narrative). |
| 7 | Kernel | Kernel role: Query, Explain, Coverage, Admission; deterministic assessment; contracts with **ste-spec**; interfaces to runtime and governance. |
| 8 | Runtime | Observation, evidence, freshness, preflight, context assembly, and Runtime interfaces to Kernel, governance, and the semantic graph. |
| 9 | Human interface | Conversation, interrogation, decision capture, steelman, reference patterns, human-in-the-loop. |
| 10 | AI interface | Agents, rule activation, and machine-mediated STE surfaces. |
| 11 | Examples | Walkthroughs linking conversation → ADR → IR → projections → conformance → drift. |
| 12 | Adoption | Introducing and scaling STE in organizations. |
| 13 | Advanced topics | Deeper or emergent subjects (semantic graphs, scoring, multi-agent policy, safety framing). |

**Where to start:** Open **[SUMMARY.md](SUMMARY.md)**, read Part 0 and Part 2 for orientation (or follow parts in order), then use the spine above. For an integrated walkthrough, use **[Part 11: Canonical example](11-examples/00-overview.md)** (AI Gateway: intent through drift and correction).

Diagrams under **`diagrams/`** are Mermaid sketches for learning; they are not authoritative architecture definitions.

## Relationship to other disciplines

- **Model-based systems engineering (MBSE):** STE shares the idea of a **canonical model** and traceable structure, with STE’s emphasis on **ADRs**, **Architecture IR**, **evidence**, and **governance loops** for software-intensive systems. Part 1 situates MBSE in the theory spine.
- **Agile:** STE does not prescribe ceremonies or roles; it addresses **traceability**, **explicit decisions**, and **controlled change** so iterative delivery does not collapse intent into irrecoverable noise.
- **DevOps:** Operational reality matters as **embodiment** and **evidence**, but this book is not a DevOps methods catalog; pipelines and runtime topics appear where they support **validation** and **governance**.
- **Software architecture:** STE treats architecture as **structured decisions** with **projections** from a single canonical model, rather than as informal “important diagrams.”

## Examples

**Part 11: Examples** walks a system through STE end-to-end. Start at **[11-examples/00-overview.md](11-examples/00-overview.md)** and the **AI Gateway** step sequence linked from **[SUMMARY.md](SUMMARY.md)**.

## Status of the project

STE and this handbook are **experimental** and **evolving**. Content may be incomplete, reorganized, or superseded; verify implementation behavior against **`ste-spec`** and the relevant code repositories. See **[DISCLAIMER.md](DISCLAIMER.md)** for limitations of use and the “as is” stance.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
