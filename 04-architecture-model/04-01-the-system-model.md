---
title: "The system model"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# The system model

## The Problem

People use “model” to mean a picture, a spreadsheet, or an informal shared understanding. For STE, **Architecture IR** must be a **single coherent system model**: the set of architectural **entities** and **relationships**—structural and other admitted semantic types—that together describe architectural reality under discussion for a declared **scope**, with rules for identity and consistency. If that holistic object is not explicit, you cannot diff “the architecture” across commits, attach **evidence** to stable parts, or argue about **conformance** without talking past each other.

## The Reframe

[Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md) defines **Architecture IR**. This chapter names the **system model**: the conceptual **whole** that IR carries—not one diagram and not one document, but the **graph-shaped** description whose nodes and edges are the referents for **traceability**, construction and materialization output, **projection** generation, and mechanical **queries**.

The system model is the coherent machine-addressable representation of architectural reality **admitted for a declared scope**. It includes structural entities and relationships; semantic commitments represented from governed sources (including decisions, invariants, and Normative Propositions where admitted); provenance and qualification needed to interpret them; and addressable relationships among them.

It is **not** merely the structural counterpart to intent. Intent and declaring artifacts remain source authority. The system model says what architecture means in addressable form **as represented**—without becoming an authority sink that absorbs declaring ADRs.

Serialization format is secondary. What matters is that the model is **one** addressable object in engineering practice, even if stored in shards.

## The Model

### Holistic semantic graph

The system model is naturally **relational**. Components sit in contexts; interfaces connect them; dependencies and data flows are edges; decisions, invariants, and Normative Propositions may attach as typed nodes with qualifying provenance. STE treats this as a **graph** for reasoning: traversal for impact and candidate context, grouping for **scopes**, and attachment points for **evidence** and **traces** ([IR as a semantic graph](04-07-ir-as-a-graph.md)).

Reachability identifies candidates. It does not by itself prove applicability or conformance.

### Identity and stability

Elements need **stable identities** within the model’s versioning story so that **diff** means “this edge moved” or “this proposition’s statement changed” rather than “this string looks different.” Identity policy is part of **governance**: renames, merges, splits, and identity replacement are **changes** to the model, not invisible edits ([Diff and change](04-06-diff-and-change.md)).

Stable identity enables reference, comparison, traversal, projection, review, and provenance. It does **not** grant independent lifecycle or policy authority to an ADR-scoped Normative Proposition.

### Consistency expectations

The model obeys **consistency rules** appropriate to its language: typed edges, cardinality, allowed attributes, and contract-level validation. Violations should surface visibly at construction, interpretation, or validation time—conceptually, “the model” should not silently contain contradictions that tooling then papers over. Mechanical validation of shape and contract semantics is not competent judgment of semantic materiality or meaning preservation where contracts reserve that judgment.

### Scope of one model instance

A given **Architecture IR** instance corresponds to a declared **scope**: a product, a fleet slice, a bounded system-of-systems view, or another agreed boundary. Handbook prose does not fix how organizations partition models; it insists that **within** a scope, the model is **canonical machine representation** of admitted architecture semantics at that layer—not a second declaring authority, and not a reconstruction of all reality.

### Representation without authority transfer

The model can contain representations of normative semantics without becoming their declaring authority. Product normalized surfaces may demonstrate the same idea as embodiment evidence; they are not automatically Architecture IR unless accepted STE semantic authority establishes that mapping ([Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md)).

## The Implications

Teams should name **what** their model instance represents and **what** it deliberately omits. Omissions are fine if explicit; hidden omissions produce false confidence in **assessment**. **Projections** should label their slice of the same model so reviewers know which commitments they are looking at—and must not imply that selected Normative Propositions govern a task merely by appearing in a view.

## Relationship to STE system

- **Overview:** [Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md).
- **Building blocks:** [Entities](04-02-entities.md), [Relationships](04-03-relationships.md).
- **Artifact framing:** [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md).
- **System picture:** [System overview](../02-overview/02-03-system-overview.md).
- **Foundations:** [Architecture as a first-class artifact](../00-problem/00-04-architecture-as-a-first-class-artifact.md).

## Summary

- The **system model** is the coherent machine-addressable description carried by **Architecture IR**—structural and other admitted semantic commitments for a declared **scope**.
- **Identity** and **consistency** make **diff**, **traceability**, and **evidence** binding meaningful.
- The model may represent normative semantics without becoming declaring authority; **scope** must stay explicit so canonical representation is not confused with partial views or applicability.

**Next:** [Entities](04-02-entities.md).
