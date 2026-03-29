---
title: "Architecture views"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Architecture views

## The Problem

Classic architecture literature talks about **views** to manage complexity. Without a **canonical** model, “views” become separate mini-models that diverge. STE reframes **views** as **projections** of **Architecture IR**: coherent slices that answer specific **concerns** while sharing identities and edges with all other views.

## The Reframe

An **architecture view** (in this handbook) is a **governed projection package**: a selected subgraph (or derived summary) of IR, a notation or document template, and a stated **concern**—security, deployment, data flow, development structure, and so on. Multiple views are **orthogonal lenses** on **one** structural object, not competing truths.

## The Model

### Concerns and slices

A **concern** names the question the view serves: “Where does data cross trust boundaries?” “Which services participate in checkout?” **Slicing** chooses entities and edges relevant to that concern, possibly hiding irrelevant neighbors for clarity. Hiding is not deletion from IR; it is **filtering** in the **projection** function.

### Viewpoints (conceptual)

A **viewpoint** is the pattern behind a family of views: conventions, metamodel mapping, and review expectations. Viewpoints align teams so security and platform reviews look at **consistent** renderings of the same graph.

### Consistency across views

Because views share IR, a change should propagate: update IR once, regenerate views. **Inconsistency** between views signals pipeline failure, outdated snapshots, or **explicit** tolerances documented under **governance** ([View consistency](04-14-view-consistency.md)).

### Standards alignment

ISO/IEC/IEEE 42010-style thinking fits STE as long as **view** means **projection** tied to IR. STE adds the **compilation** and **evidence** spine missing from document-only view practices.

## The Implications

Define viewpoints **explicitly** for your organization; do not rely on informal “the way we draw security.” **Governance** reviews should name the **viewpoint** and **IR** version under review.

## Relationship to STE system

- **Projections overview:** [Projections overview](04-08-projections-overview.md).
- **Stakeholder tailoring:** [Stakeholder views](04-13-stakeholder-views.md).
- **Software architecture theory:** [Software architecture theory](../01-theory/01-07-software-architecture-theory.md).
- **MBSE:** [Model-based systems engineering](../01-theory/01-08-model-based-systems-engineering.md).

## Summary

- **Architecture views** are **governed projections** answering named **concerns** from shared **Architecture IR**.
- **Viewpoints** standardize how slices are taken and presented.
- **Consistency** is expected because views are **not** independent models.

**Next:** [Stakeholder views](04-13-stakeholder-views.md).
