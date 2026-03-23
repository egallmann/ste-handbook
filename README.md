# STE Handbook

## What is System of Thought Engineering (STE)?

System of Thought Engineering (STE) is a model-driven architecture and governance approach that encodes architectural intent as machine-readable decisions, compiles that intent into a canonical architecture model (Architecture IR), enforces constraints and invariants, and validates system behavior against intent using deterministic evidence and conformance testing. STE treats architecture as an explicit, evolvable system of decisions—not only as informal documentation.

## Purpose of this repository

This repository is the **STE Handbook**: explanatory technical documentation for STE. It is meant to help readers understand concepts, relationships, lifecycle, and how the pieces fit together. It may include walkthroughs, diagrams, and deeper technical narrative than fits comfortably in a normative specification.

**This handbook is explanatory, not normative.** When this repository and the specification disagree, **`ste-spec` is authoritative** for what the system must do and mean.

## How this repository relates to other STE repositories

| Repository | Role |
|------------|------|
| **`ste-spec`** | Publishable **normative** architectural specification: contracts, invariants, semantic constraints, and boundary definitions other STE work relies on. |
| **`ste-kernel`** | Decision and admission logic that consumes evidence and published contracts to make deterministic orchestration decisions. |
| **`adr-architecture-kit`** | Tooling and patterns for authoring, structuring, and managing **architectural intent** (for example ADR surfaces) that feed the broader STE pipeline. |

The handbook **orients** readers and connects narrative to those authorities; it does not replace them.

## Where to start (reading order)

1. Open **[SUMMARY.md](SUMMARY.md)** for the full table of contents.
2. Start with **[01-overview/](01-overview/)**—especially *What is STE?*, *The problem*, and *System overview*.
3. Continue through **02–08** in order (intent → Architecture IR → kernel and runtime → projections → conversation engine → lifecycle → examples) as your questions lead you.

Diagrams under **`diagrams/`** are **Mermaid** sketches and **projections** for learning; they are not authoritative architecture definitions. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for contribution and branching rules, and **[DISCLAIMER.md](DISCLAIMER.md)** for limitations of use.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
