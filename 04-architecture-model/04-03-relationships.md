---
title: "Relationships"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Relationships

## The Problem

A bag of labeled boxes is not an architecture. What matters is **how** boxes connect: depends on, talks to, deploys into, reads from, delegates to, satisfies. When those connections live only in heads or slide decks, **impact analysis** fails and **drift** hides in “we thought that was indirect.” **Architecture IR** makes **relationships** first-class so the model is **relational truth**, not a parts catalog.

## The Reframe

A **relationship** is a typed, directed (or otherwise oriented) **edge** between **entities** in the system model, governed by the metamodel: which types may connect, what cardinality means, and what semantics the edge claims. **Compilation** materializes many relationships from **intent**; others may be asserted or ingested under policy. **Projections** **render** subgraphs; they do not **define** the edge set.

## The Model

### Typed edges and semantics

Edge **type** carries meaning: “depends on” is not interchangeable with “owned by” or “implements.” STE’s payoff is **mechanical** use—blast radius, forbidden paths, interface contracts—so synonym collapse in the model is a **governance** bug unless explicitly aliased with clear rules.

### Multiplicity and roles

Relationships may encode **roles** (client/server, producer/consumer) and **multiplicity** (one-to-many service instances). These facts support **validation**: a policy that forbids a database dependency from a public edge tier is a **graph predicate**, not a paragraph in a wiki.

### Contracts and interfaces

Interface-like relationships bundle obligations: operation sets, schemas, SLAs. At handbook altitude, treat them as **structural commitments** linked to **intent** (**ADRs**, **invariants**) and to **evidence** (contract tests, probes). Detailed contract languages belong in **ste-spec** and product standards.

### Derived versus asserted

Some edges are **asserted** in **intent** or by curators; others are **derived** by **compilation** or analysis from lower-level inputs. The model should be clear which is which for **governance**: derived edges may be regenerated; asserted edges may require explicit change records when overwritten.

## The Implications

Teams should resist encoding the same fact twice under different edge types without a **derivation** rule. Duplication breeds silent contradiction—one projection shows an allowed path, another hides it. **View consistency** ([View consistency](04-14-view-consistency.md)) and **validation** exist partly to catch that class of failure.

## Relationship to STE system

- **Nodes:** [Entities](04-02-entities.md).
- **Graph reasoning:** [IR as a graph](04-07-ir-as-a-graph.md), [Diff and change](04-06-diff-and-change.md).
- **Traces on edges:** [Traceability in Architecture IR](04-05-traceability.md).
- **Conformance structure:** [Conformance](../03-artifacts/03-07-conformance.md).
- **Drift:** [The governance model](../06-governance/06-02-the-governance-model.md).

## Summary

- **Relationships** are typed edges that carry architectural **semantics**, not mere lines on a diagram.
- **Compilation**, **assertion**, and **derivation** must be distinguishable for **governance** and **diff**.
- Graph **predicates** turn **intent** **constraints** into checkable structure.

**Next:** [Compilation](04-04-compilation.md).
