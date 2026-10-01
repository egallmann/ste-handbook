---
title: "Relationships"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Relationships

## The Problem

A bag of labeled boxes is not an architecture. What matters is **how** architectural objects connect: depends on, talks to, deploys into, declared in, implements, governs, supersedes. When those connections live only in heads or slide decks, **impact analysis** fails and **drift** hides in “we thought that was indirect.” **Architecture IR** makes **relationships** first-class so the model is **relational truth**, not a parts catalog.

That truth is not only topology. Semantic relationships make decisions, invariants, Normative Propositions, and structural elements explainable and traversable. If “reachable from this component” is mistaken for “governs this task,” discoverability becomes a false governance oracle.

## The Reframe

A **relationship** is a typed, oriented **edge** between **entities** in the system model, governed by the metamodel: which types may connect, what cardinality means, and what semantics the edge claims. Construction and materialization may emit relationships from governed intent; others may be asserted or derived under policy. **Projections** **render** subgraphs; they do not **define** the edge set.

Exact relationship names and cardinalities belong in **ste-spec** and product contracts. The handbook does not invent relation verbs for convenience. ste-spec’s architecture relationship grammar includes structural and semantic edges such as declared-in, references, enforces, enables, governs, implemented-by, embodied-in, and supersession links—alongside topology-facing dependence and interface edges where admitted.

## The Model

### Typed edges and semantics

Edge **type** carries meaning: “depends on” is not interchangeable with “declared in,” “implements,” or “enforces.” STE’s payoff is **mechanical** use—blast radius, forbidden paths, candidate normative neighborhoods—so synonym collapse in the model is a **governance** bug unless explicitly aliased with clear rules.

### Identity of endpoints

Source and target **identity** matter. Relationships bind addressable entities; vague labels do not. When a Normative Proposition is linked or qualified relative to a declaring ADR or related architecture objects, endpoints must remain the same identities used for **diff**, **trace**, and projection.

### Provenance and qualification

Relationship representation has semantics: asserted versus derived, declaring context, and provenance/qualification fields where contracts provide them. Ownership of an ADR-scoped Normative Proposition may be preserved by authoring containment and by normalized declaring-ADR qualification; a relationship edge does not manufacture that authority by itself.

### Multiplicity and roles

Relationships may encode **roles** (client/server, producer/consumer) and **multiplicity**. These facts support **validation**: a policy that forbids a database dependency from a public edge tier is a **graph predicate**, not a paragraph in a wiki.

### Contracts and interfaces

Interface-like relationships bundle obligations: operation sets, schemas, SLAs. At handbook altitude, treat them as architectural commitments linked to **intent** and to **evidence**. Detailed contract languages belong in **ste-spec** and product standards.

### Derived versus asserted

Some edges are **asserted** in **intent** or by curators; others are **derived** by interpretation, compilation, or analysis from lower-level inputs. The model should be clear which is which for **governance**: derived edges may be regenerated; asserted edges may require explicit change records when overwritten. Heuristic or inferred edges must not be treated as explicit declaring authority without uplift.

### Reachability is not applicability

Traversal makes things discoverable. **Reachability does not imply applicability.**

A semantic node being linked to an ADR, reachable from a component, visible in a registry, selected by a query, or shown in a projection does **not** by itself establish:

- authority;
- effectivity;
- applicability to a task;
- conformance.

Graph presence and relationship inclusion are facts about representation. Task-relative applicability remains later system work (conceptually toward [Context assembly and MVC](../08-runtime/08-05-context-assembly-and-mvc.md)). Part 4 establishes that candidate context can be discovered without pretending the discovery algorithm is settled here.

## The Implications

Teams should resist encoding the same fact twice under different edge types without a **derivation** rule. Duplication breeds silent contradiction—one projection shows an allowed path, another hides it. **View consistency** ([View consistency](04-14-view-consistency.md)) and **validation** exist partly to catch that class of failure.

Resist treating “this Normative Proposition is one hop from the change surface” as “this Normative Proposition governs the change.” Candidate neighborhoods are useful; governance claims need authority, effectivity, and applicability discipline beyond the edge list.

## Relationship to STE system

- **Nodes:** [Entities](04-02-entities.md).
- **Graph reasoning:** [IR as a semantic graph](04-07-ir-as-a-graph.md), [Diff and change](04-06-diff-and-change.md).
- **Traces on edges:** [Traceability in Architecture IR](04-05-traceability.md).
- **Conformance structure:** [Conformance](../03-artifacts/03-07-conformance.md).
- **Drift:** [The governance model](../06-governance/06-02-the-governance-model.md).

## Summary

- **Relationships** are typed edges that carry architectural **semantics**, not mere lines on a diagram.
- Structural and semantic relationships both matter; only contract-admitted relation types belong in the model.
- **Compilation**, **assertion**, and **derivation** must be distinguishable for **governance** and **diff**.
- Reachability and relationship presence do not manufacture authority, effectivity, applicability, or conformance.

**Next:** [Compilation and semantic materialization](04-04-compilation.md).
