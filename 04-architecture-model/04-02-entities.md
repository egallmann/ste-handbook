---
title: "Entities"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Entities

## The Problem

Architecture conversations mix nouns freely—“service,” “module,” “subsystem,” “bounded context”—without saying which ones are **first-class in the model**. If those nouns do not map to stable **entities** in **Architecture IR**, tools cannot align, **traces** cannot land, and **evidence** cannot target a definite **scope**. The failure looks like tooling gaps; the cause is often missing entity discipline.

## The Reframe

An **entity** in **Architecture IR** is a typed node in the system model: something that can be referenced, versioned, linked, and projected. Examples at the architecture layer include logical components, deployable units, interfaces, data stores, external systems, and capability groupings—**exact** inventories belong in **ste-spec** and your metamodel; the handbook fixes the *role* of entities as **the addressable units of structure**.

Entities are **not** the same as files or classes, though they may **map** to **implementation** identities. The model stays at the abstraction where architectural commitments live.

## The Model

### Typing and roles

Each entity has a **type** (or metamodel class) that constrains which **relationships** it may participate in and which attributes matter. Typing is what makes the graph **mechanical**: queries and rules can ask for “all components exposing this interface” instead of scraping labels.

### Identity

Entities carry **identifiers** stable across updates within the versioning story. Identity ties **intent** references, **compilation** output, **projection** anchors, and **evidence** **scopes** to the **same** object. Without that, “component A” in a test report and “component A” in a diagram are accidents of wording.

### Attributes and annotations

Beyond graph edges, entities may carry **annotations**: ownership, criticality, lifecycle state, links to external systems of record, and similar metadata. Annotations participate in **governance** and **validation** when **rules** reference them; they should not become a shadow model that contradicts the graph.

### Boundaries as entities

Boundary elements—trust zones, deployment boundaries, API surfaces—often appear as entities or as first-class facets of entities. Their job is to make **constraints** from **intent** **bindable** to structure: “no dependency across this edge” is a claim about **relationships** anchored on identifiable **entities**.

## The Implications

Defining entity types is a **design** act, not clerical overhead. Too few types collapse distinct concerns; too many duplicate **implementation** detail in IR. The right cut depends on the system and **governance** appetite; STE expects the cut to be **explicit** and **stable** enough to compile and review.

## Relationship to STE system

- **Structure:** [The system model](04-01-the-system-model.md), [Relationships](04-03-relationships.md).
- **Trace attachment:** [Traceability in Architecture IR](04-05-traceability.md), [IR as a graph](04-07-ir-as-a-graph.md).
- **Intent binding:** [Invariants](../03-artifacts/03-03-invariants.md), [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md).
- **Embodiment mapping:** [Implementation and operation](../05-lifecycle/05-03-implementation-and-operation.md).

## Summary

- **Entities** are typed, identifiable nodes in **Architecture IR**—the units **traceability** and **evidence** attach to.
- **Identity** and **typing** make automated reasoning and **diff** possible.
- Entities sit at **architecture** abstraction; they **reference** **implementation**, they do not replace source code.

**Next:** [Relationships](04-03-relationships.md).
