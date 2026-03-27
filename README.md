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

## Section map (Parts 0–13)

| Part | Title | Role |
|------|--------|------|
| 0 | Problem | Problem, thesis, and vocabulary precursors. |
| 1 | Theory | Disciplinary scaffolding (systems, information, control, cybernetics, decision theory, safety, software architecture, MBSE, synthesis). |
| 2 | Overview | What STE is, terminology, system overview, lifecycle summary. |
| 3 | Artifacts | ADRs, requirements, invariants, Architecture IR connection, evidence, traceability, conformance, publication versus projection. |
| 4 | Architecture model | Canonical system model (IR), compilation, traceability, diff, graph view, and projections as model-facing views. |
| 5 | Lifecycle | Lifecycle stages: intent through evidence, conformance, decisions, change, and state transitions. |
| 6 | Governance | Policy, drift, certification, and the control loop as governed operation. |
| 7 | Kernel | Admission, validation, divergence and convergence, conformance, deterministic assessment. |
| 8 | Runtime | Runtime evidence and integration with live systems. |
| 9 | Human interface | Conversation, interrogation, decision capture, steelman, reference patterns, human-in-the-loop. |
| 10 | AI interface | Agents, rule activation, and machine-mediated STE surfaces. |
| 11 | Examples | Walkthroughs linking conversation → ADR → IR → projections → conformance → drift. |
| 12 | Adoption | Introducing and scaling STE in organizations. |
| 13 | Advanced topics | Deeper or emergent subjects (semantic graphs, scoring, multi-agent policy, safety framing). |

For the full table of contents with links, see **[SUMMARY.md](SUMMARY.md)**. For a short thesis statement, see **[STE-MANIFESTO.md](STE-MANIFESTO.md)**.

## Where to start

1. Open **[SUMMARY.md](SUMMARY.md)** for the complete reading order.
2. Read **Part 0 (Problem)** and **Part 2 (Overview)** for orientation, or follow the parts in order for a linear read.
3. Use the artifacts → architecture model → lifecycle → governance → kernel → runtime spine; use **[Part 11 — Canonical example](11-examples/00-overview.md)** for an integrated walkthrough (AI Gateway: intent through drift and correction).

Diagrams under **`diagrams/`** are Mermaid sketches for learning; they are not authoritative architecture definitions. See **[DISCLAIMER.md](DISCLAIMER.md)** for limitations of use.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
