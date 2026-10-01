---
title: "Entities"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Entities

## The Problem

Architecture conversations mix nouns freely—“service,” “module,” “decision,” “MUST statement”—without saying which ones are **first-class in the model**. If those nouns do not map to stable **entities** in **Architecture IR**, tools cannot align, **traces** cannot land, and **evidence** cannot target a definite **scope**. The failure looks like tooling gaps; the cause is often missing entity discipline.

That discipline is not only structural. When Normative Propositions and invariants exist only as prose fragments, reviewers reconstruct meaning from modal language, and identity and authority blur.

## The Reframe

In Architecture IR, an **entity** is a **typed node** in the architecture model: an independently addressable semantic object admitted under the governed Architecture IR ontology. ste-spec names the canonical semantic entity types and how they may realize onto mechanical surfaces at a pinned IR version. Exact inventories and schemas belong there; the handbook fixes the *role* of entities as the addressable units of the machine-oriented architecture model.

Entities are **not** the same as files or classes, though they may **map** to **implementation** identities. Being an entity does **not** make all entity types peers in authority. Different families have different ownership and lifecycle rules.

## The Model

### Conceptual families (not an exhaustive inventory)

Under accepted Architecture IR semantics, entity types include families such as:

**Structural semantics** — for example systems, components, interfaces, integrations, and related structural types.

**Intent / normative and decision semantics** — including **Decision**, **Invariant**, and **NormativeProposition**, among other architecture-facing types accepted STE semantic authority admits (for example constraint and capability where in scope).

**Evidence and governance-facing semantics** — such as evidence, gaps, reviews, overrides, and remediation where the ontology includes them.

**Contract-governed extension semantics** — custom or consumer-qualified entities only where current authority permits them. Arbitrary modal prose does not become a Normative Proposition; mechanical tooling must not infer NP admission from MUST/SHOULD wording alone.

**NormativeProposition** and **Invariant** are peer semantic types. An invariant expresses must-remain-true semantics under its governed scope. A Normative Proposition expresses ADR-local required/prohibited/recommended/discouraged/permitted meaning through a closed normative-force vocabulary. Neither is collapsed into the other because both may use modal language.

### Normative Proposition as addressability without independent authority

A Normative Proposition is the clearest handbook example of:

```text
stable identity + addressability
        WITHOUT
independent authority / lifecycle
```

In authoring, the NP is **ADR-contained**; authority and lifecycle remain with the declaring ADR. In normalized embodiment surfaces, an NP envelope may carry explicit declaring-ADR qualification and source-artifact qualification so ownership and provenance survive detachment from source position. That qualification **preserves** authority derived from the declaring ADR; it does not create new authority.

Do not invent a dedicated compiled Architecture IR `kind` for NormativeProposition where accepted STE semantic authority has not established one. Mechanical realization and the deferred canonical-entity / identity realization (CE-01) remain deferred; the corresponding ste-spec mechanical / corpus integration remains deferred.

### Typing and roles

Each entity has a **type** that constrains which **relationships** it may participate in and which attributes matter. Typing is what makes the graph **mechanical**: queries and rules can ask for typed neighborhoods instead of scraping labels.

### Identity

Entities carry **identifiers** stable across updates within the versioning story. Where identity doctrine applies, identity is not derived from prose, paths, hashes, ordering, source location, or composition position. Human recognition surfaces such as alias identifiers and alias names (where used) are not canonical identity.

Identity ties **intent** references, construction and materialization output, **projection** anchors, and **evidence** **scopes** to the **same** object. Without that, “component A” in a test report and “component A” in a diagram are accidents of wording—and the same is true for Normative Propositions reviewed across tools.

### Attributes and annotations

Beyond graph edges, entities may carry attributes and annotations: ownership, criticality, lifecycle state (where applicable to that type), links to external systems of record, and similar metadata. Normative Propositions, under released ADR-Kit embodiment evidence, do not invent an independent governance lifecycle merely by being represented. Annotations must not become a shadow model that contradicts declaring authority or graph semantics.

### Product surfaces versus STE ontology

Authoring and normalized product registries may use implementation vocabulary such as entity-type strings and entity registries. Those surfaces are embodiment evidence. They are **not** Architecture IR unless accepted STE semantic authority establishes that mapping. Handbook doctrine follows the STE Entity ontology, not product implementation names.

## The Implications

Defining which entity types are in play for a scope is a **design** and **governance** act. Too few types collapse distinct concerns; too many duplicate **implementation** detail in the model. STE expects the cut to be **explicit**, **contract-admitted**, and **stable** enough to construct, validate, and review—without treating every node as equally authoritative.

## Relationship to STE system

- **Structure:** [The system model](04-01-the-system-model.md), [Relationships](04-03-relationships.md).
- **Trace attachment:** [Traceability in Architecture IR](04-05-traceability.md), [IR as a semantic graph](04-07-ir-as-a-graph.md).
- **Intent binding:** [Invariants](../03-artifacts/03-03-invariants.md), [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md), [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md).
- **Embodiment mapping:** [Implementation and operation](../05-lifecycle/05-03-implementation-and-operation.md).
- **Explanatory depth:** [Can architecture change what a model is likely to do?](../13-architectural-essays/13-05-can-architecture-change-what-a-model-is-likely-to-do.md).

## Summary

- **Entities** are typed, identifiable nodes in **Architecture IR**—the addressable units of the semantic architecture model.
- Structural types and governed semantic types (including **Decision**, **Invariant**, and **NormativeProposition**) may all be entities; authority and lifecycle rules differ by type.
- **NormativeProposition** and **Invariant** are peers; NP identity is addressability, not independent policy authority.
- ste-spec remains STE-wide Architecture IR authority where integrated; product registry vocabulary is embodiment evidence, not automatic IR doctrine.

**Next:** [Relationships](04-03-relationships.md).
