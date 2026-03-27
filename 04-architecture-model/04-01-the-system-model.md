---
title: "The system model"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# The system model

## The Problem

People use “model” to mean a picture, a spreadsheet, or an informal shared understanding. For STE, **Architecture IR** must be a **single coherent system model**: the set of architectural **entities** and **relationships** that together describe the structure under discussion, with rules for identity and consistency. If that holistic object is not explicit, you cannot diff “the architecture” across commits, attach **evidence** to stable parts, or argue about **conformance** without talking past each other.

## The Reframe

[Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md) defines **Architecture IR** and the **architecture model** idea. This chapter names the **system model**: the conceptual **whole** that IR carries—not one diagram and not one document, but the **graph-shaped** description whose nodes and edges are the referents for **traceability**, **compilation** output, and **projection** generation. It is the structural counterpart to **intent**: **intent** says what is allowed and why; the system model says what the architecture **is** in terms of components, boundaries, and links—**as committed** through the pipeline.

Serialization format is secondary. What matters is that the model is **one** addressable object in engineering practice, even if stored in shards or services physically.

## The Model

### Holistic graph

The system model is naturally **relational**. Components sit in contexts; interfaces connect them; dependencies and data flows are edges; capabilities may attach to subtrees. STE treats this as a **graph** for reasoning: traversal for impact, grouping for **scopes**, and attachment points for **evidence** and **traces** ([IR as a graph](04-07-ir-as-a-graph.md)).

### Identity and stability

Elements need **stable identities** within the model’s versioning story so that **diff** means “this edge moved” rather than “this string looks different.” Identity policy is part of **governance**: renames, merges, and splits are **changes** to the model, not invisible edits ([Diff and change](04-06-diff-and-change.md)).

### Consistency expectations

The model obeys **consistency rules** appropriate to its language: typed edges, cardinality, allowed attributes, and compilation invariants. Violations surface at **compilation** or **validation** time depending on where the rule lives—conceptually, “the model” should not silently contain contradictions that tooling then papers over.

### Scope of one model instance

A given **Architecture IR** instance corresponds to a declared **scope**: a product, a fleet slice, a bounded system-of-systems view, or another agreed boundary. Handbook prose does not fix how organizations partition models; it insists that **within** a scope, the model is **canonical** for structural truth at that layer.

## The Implications

Teams should name **what** their IR instance represents and **what** it deliberately omits. Omissions are fine if explicit; hidden omissions produce false confidence in **assessment**. **Projections** should label their slice of the same model so reviewers know which structural commitments they are looking at.

## Relationship to STE system

- **Overview:** [Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md).
- **Building blocks:** [Entities](04-02-entities.md), [Relationships](04-03-relationships.md).
- **Artifact framing:** [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md).
- **System picture:** [System overview](../02-overview/02-03-system-overview.md).
- **Foundations:** [Architecture as a first-class artifact](../00-problem/00-04-architecture-as-a-first-class-artifact.md).

## Summary

- The **system model** is the whole structural description carried by **Architecture IR**, understood as one coherent graph-shaped object.
- **Identity** and **consistency** make **diff**, **traceability**, and **evidence** binding meaningful.
- **Scope** must be explicit so **canonical** IR is not confused with partial views.

**Next:** [Entities](04-02-entities.md).
