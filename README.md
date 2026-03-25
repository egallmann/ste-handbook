# STE Handbook

## What is System of Thought Engineering (STE)?

System of Thought Engineering (STE) is a model-driven architecture and governance discipline. Architectural intent is captured in structured, reviewable artifacts; compiled into a canonical architecture model (Architecture IR); and assessed against implementation and runtime evidence using deterministic methods where appropriate. STE treats architecture as an explicit, versioned system of decisions—not only as informal documentation or incidental diagrams.

## Purpose of this repository

This repository publishes the **STE Handbook** manuscript: long-form technical documentation that explains concepts, relationships, lifecycle, and end-to-end flows. It is structured as a book manuscript suitable for sustained reading and for tooling that needs a stable outline.

**This handbook is explanatory, not normative.** When this repository and the specification disagree, **`ste-spec` is authoritative** for what the system must do and mean.

## How this repository relates to other STE repositories

| Repository | Role |
|------------|------|
| **`ste-spec`** | Normative specification: contracts, invariants, semantic constraints, and boundaries other STE work relies on. |
| **`adr-architecture-kit`** | Tooling and patterns for authoring and managing architectural intent (including ADR surfaces) that feed the STE pipeline. |
| **`ste-kernel`** | Decision and admission logic that consumes evidence and published contracts to make deterministic orchestration decisions. |
| **`ste-runtime`** | Runtime integration and execution concerns that connect live systems to STE evidence and assessment flows (as defined in that repository). |

The handbook **orients** readers and connects narrative to those authorities; it does not replace them.

## Section map (Parts 0–11)

| Part | Title | Role |
|------|--------|------|
| 0 | Foundations | Problem, thesis, and vocabulary precursors. |
| 1 | Theoretical foundations | Disciplinary scaffolding (systems, information, control, cybernetics, decision theory, safety, software architecture, MBSE, synthesis). |
| 2 | Overview | What STE is, terminology, system overview, lifecycle summary. |
| 3 | Intent | Decisions, ADR planes, invariants, constraints, capabilities. |
| 4 | Architecture IR | Canonical system model, compilation, traceability, diff, graph view. |
| 5 | Kernel | Admission, validation, divergence and convergence, evidence, conformance, deterministic assessment. |
| 6 | Control loop | End-to-end loop from intent through evidence to decisions and change; continuous certification. |
| 7 | Projections | Diagrams, documents, views, consistency across projections. |
| 8 | Conversation engine | Human interface: interrogation, capture, agents, rule activation, human-in-the-loop. |
| 9 | Lifecycle and governance | Design, change, drift, convergence, certification, governance. |
| 10 | Examples | Walkthroughs linking conversation → ADR → IR → projections → conformance → drift. |
| 11 | Advanced topics | Deeper or emergent subjects (semantic graphs, scoring, multi-agent policy, safety framing). |

For the full table of contents with links, see **[SUMMARY.md](SUMMARY.md)**. For a short thesis statement, see **[STE-MANIFESTO.md](STE-MANIFESTO.md)**.

## Where to start

1. Open **[SUMMARY.md](SUMMARY.md)** for the complete reading order.
2. Read **Part 0 (Foundations)** and **Part 2 (Overview)** for orientation, or follow the parts in order for a linear read.
3. Use the intent → kernel → control-loop parts as the technical spine; use the examples part for integrated walkthroughs.

Diagrams under **`diagrams/`** are Mermaid sketches for learning; they are not authoritative architecture definitions. See **[DISCLAIMER.md](DISCLAIMER.md)** for limitations of use.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
