---
title: "Diff and change"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Diff and change

## The Problem

“What changed in the architecture?” collapses without a **canonical** model. File diffs show text motion; slide decks are not comparable; tribal knowledge updates invisibly. **Architecture IR** enables **structural diff**: added or removed **entities** and **relationships**, attribute changes, and trace endpoint moves—**if** identities are stable and versions are comparable.

## The Reframe

**Diff** over IR is an engineering object alongside code diff. It answers whether a change is a **refactor** (identity-preserving rearrangement), an **additive** extension, or a **semantic** shift (new dependency class, boundary move) that should trigger **governance**, **evidence** reruns, or **intent** updates. **Change** to the architecture is then **recorded** as model delta plus linked **intent** delta, not only as merged PRs in unrelated repos.

## The Model

### Comparable snapshots

Diff assumes two **snapshots** of IR (or base versus proposed) under agreed **scope** and **versioning**. Snapshot policy—how often IR is frozen for review, how branches work—is organizational; STE requires honesty about what is being compared.

### Categories of structural change

Useful conceptual buckets include: **entity** lifecycle (introduce, deprecate, merge, split), **relationship** changes (new dependency, removed interface), **annotation** changes (criticality, ownership), and **trace** graph changes. Each category has different **risk** and **evidence** implications.

### Identity and rename

Renames are **first-class** events: without migration rules, diff degenerates into “delete all, add all.” **Governance** should treat identity migration as a **decision**-visible change when **traceability** or **evidence** history must remain continuous.

### Link to intent change

Model diff alone is incomplete. **Intent** **artifacts** should move in **lockstep** when semantics change: an **ADR** or **invariant** update explains why the graph moved ([Change and evolution](../05-lifecycle/05-07-change-and-evolution.md)). Silent graph-only edits recreate **drift** between normative and structural records.

## The Implications

Publish **architecture changelogs** derived from IR diff for human review; use the same diff to drive selective **validation** (“only rerun checks touching this subgraph”). **Projections** should reflect post-diff state automatically when regenerated from IR—if they do not, you have a **projection** pipeline bug, not “architecture changed.”

## Relationship to STE system

- **Graph framing:** [IR as a graph](04-07-ir-as-a-graph.md).
- **Governance:** [Change management](../06-governance/06-02-change-management.md), [Drift](../06-governance/06-03-drift.md).
- **Lifecycle:** [Architecture definition](../05-lifecycle/05-02-architecture-definition.md).
- **Kernel:** [Divergence](../07-kernel/07-04-divergence.md), [Convergence](../07-kernel/07-05-convergence.md).

## Summary

- **Diff** over **Architecture IR** is structural comparison, not diagram opinion.
- **Identity** discipline makes diff meaningful across time.
- Model changes should pair with **intent** changes when **semantics** move.

**Next:** [IR as a graph](04-07-ir-as-a-graph.md).
