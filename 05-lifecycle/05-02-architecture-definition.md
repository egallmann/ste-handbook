---
title: "Part 5: Architecture Definition"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Architecture definition

**Architecture definition** turns governed **intent** into a coherent structural commitment carried in **Architecture IR** and readable **projections**. It is incremental: the model deepens as **decisions** harden and **scopes** narrow.

## Purpose of this stage

Make **architecture** a first-class, inspectable object: a canonical arrangement of elements and relationships that teams can diff, trace, and assess instead of relying on divergent diagrams or tacit knowledge.

## Artifacts involved

**Architecture IR**, structural elements and relationships, and **projections** derived from the canonical model. **Traceability** links connect **intent** artifacts to model elements. See [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md), [Traceability](../03-artifacts/03-06-traceability.md), [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md), and Part 4 ([Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md)).

## Human responsibility

Architects and accountable owners define or accept the structural commitments that compilation encodes, resolve ambiguities before they become silent **drift**, and review **projections** for fidelity to **intent**. Humans judge when the model is adequate for a **scope** and purpose, within policy.

## STE system responsibility

STE compiles structured **intent** and related inputs into **Architecture IR**, maintains internal consistency where automated checks exist, preserves change history and **diff**, maintains **trace** edges from **intent** to IR, and regenerates **projections** from canonical sources.

## Transitions to the next stage

Work shifts toward **implementation and operation** when the organization commits to realizing **embodiment** against the declared structure for a **scope** (build, configure, deploy, run). That shift can happen in slices, not only as a program-wide gate. Return to this stage when **intent** changes require recompilation or when **evidence** shows the model no longer matches reality.

**Next stage chapter:** [Implementation and operation](05-03-implementation-and-operation.md).

## Relationship to intent, implementation, and evidence

- **Intent:** **Architecture IR** expresses structured **intent** about shape, interfaces, and allowed dependencies; it should not silently contradict **ADRs**, **constraints**, and **invariants**.
- **Implementation:** **Implementation** (code, infra, configuration) will realize or diverge from the IR; the IR is the declared side of that comparison.
- **Evidence:** This stage rarely produces operational **evidence** itself, but it sets what later **evidence** must speak to (for example which interfaces and **scopes** are in play).

## Relationship to other chapters

- [System overview](../02-overview/02-03-system-overview.md)
- [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md)
- [Projections overview](../04-architecture-model/04-08-projections-overview.md)
- [Intent to implementation](../06-governance/06-09-intent-to-implementation.md)
- **ste-spec** for IR semantics and compilation contracts.

**Next:** [Implementation and operation](05-03-implementation-and-operation.md).
