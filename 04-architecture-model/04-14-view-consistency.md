---
title: "View consistency"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# View consistency

## The Problem

Inconsistent **projections** destroy trust faster than missing ones. If the deployment diagram shows a dependency the security view omits, reviewers cannot know which **governance** story was true. **View consistency** is the discipline that multiple **projections** **render** the same **Architecture IR** commitments for their **scopes**, modulo **explicit** tolerances.

## The Reframe

**Consistency** is not “all views look identical.” It is “no view **contradicts** IR for the **claims** it makes.” Different slices may omit elements, but they must not **assert** edges or properties that IR forbids or lacks. **Validation** can automate some checks; **governance** owns the rest ([Governed reasoning](../00-problem/00-05-governed-reasoning.md)).

## The Model

### Same snapshot, many renderings

A **consistency** baseline is: projections consumed together in a **governance** event reference the **same** IR snapshot (or compatible versions under merge rules). Mixed snapshots recreate meeting arguments that no **diff** can settle.

### Cross-projection predicates

Useful checks include: every edge shown in view A exists in IR; every boundary in security view maps to a trust **entity** in IR; service names in docs match IR labels and IDs. Predicate design is policy and **ste-spec** territory; the handbook asserts the **category** of checks.

### Tolerances and waivers

Sometimes views **intentionally** simplify: collapsing clusters, showing logical rather than physical paths. **Tolerances** should be **documented**—what simplification is allowed, what must never be simplified. **Waivers** are **governance** objects when simplification risks **misleading** **assessment**.

### Drift and conformance

**Drift** between projections and IR is **structural** **debt**. **Conformance** discussions often assume IR matches **intent** and **embodiment**; projection **conformance** is the prior step: do **derived** views still **track** **canonical** structure? Skipping it makes **evidence** and **Kernel** work look green while humans steer from false pictures ([The governance model](../06-governance/06-02-the-governance-model.md)).

## The Implications

Add **projection** checks to CI where practical: regenerate and **diff** outputs, fail on orphan elements, flag notation mappings that drop edge types. Pair automated checks with periodic human **review** of **viewpoint** definitions—**rules** rot too.

## Relationship to STE system

- **Projections cluster:** [Projections overview](04-08-projections-overview.md) through [Stakeholder views](04-13-stakeholder-views.md).
- **Kernel** (**IR validation** and reasoning surface): [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).
- **Publication versus projection:** [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md).

## Summary

- **View consistency** means **projections** do not **contradict** **Architecture IR** for the claims they make.
- **Snapshots**, **predicates**, and **documented tolerances** make consistency **checkable**.
- Projection **drift** undermines **conformance** before **evidence** is even collected.

**Next:** [Illustrative walkthrough](04-15-illustrative-walkthrough.md) shows minimal **intent**→**projection** shapes in one chain. Then continue to Part 5 — [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md) or deepen **Kernel** mechanics in [Kernel overview](../07-kernel/07-00-overview.md).
