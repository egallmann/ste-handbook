---
title: "Diff and change"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Diff and change

## The Problem

“What changed in the architecture?” collapses without a **canonical** model. File diffs show text motion; slide decks are not comparable; tribal knowledge updates invisibly. **Architecture IR** enables **diff** over addressable architecture semantics: added or removed **entities** and **relationships**, attribute changes, normative statement or force changes, and trace endpoint moves—**if** identities are stable and versions are comparable.

A purely structural diff story is incomplete once decisions, invariants, and Normative Propositions are first-class machine-facing semantics.

## The Reframe

**Diff** over the architecture model is an engineering object alongside code diff. It answers whether a change is a **refactor** (identity-preserving rearrangement), an **additive** extension, or a **semantic** shift that should trigger **governance**, **evidence** reruns, or **intent** updates. **Change** to the architecture is then **recorded** as model delta plus linked **intent** delta, not only as merged PRs in unrelated repos.

Mechanical diff can show that bytes or fields changed. It must **not** automatically conclude that meaning was preserved, that materiality changed, or that identity should be preserved or replaced—unless an exact deterministic rule governs that case. Where Normative Proposition doctrine assigns meaning and materiality continuity to competent review, say so and stop.

## The Model

### Comparable snapshots

Diff assumes two **snapshots** of the model (or base versus proposed) under agreed **scope** and **versioning**. Snapshot policy—how often the model is frozen for review, how branches work—is organizational; STE requires honesty about what is being compared.

### Categories of change

Useful conceptual buckets include:

- **Structural** entity and relationship lifecycle (introduce, deprecate, merge, split, new dependency, removed interface);
- **Decision** semantic change;
- **Invariant** change;
- **Normative Proposition** statement, normative-force, scope, or rationale change where semantically relevant;
- **Semantic relationship** and provenance/qualification change;
- **Annotation** changes (criticality, ownership) where applicable;
- **Trace** graph changes;
- **Identity continuity** versus replacement.

Each category has different **risk** and **evidence** implications. Stable identity makes semantic diff valuable: reviewers can see “this proposition changed” rather than “a paragraph moved.”

### Mechanical diff versus meaning judgment

Field-level comparison is mechanical. Judgments that meaning was preserved, that a wording edit is immaterial, or that a new identity is required remain **semantic review** concerns where contracts assign them that way. Do not imply that every wording edit requires new identity; follow accepted authority for continuity rules.

### Identity and rename

Renames and identity migrations are **first-class** events: without migration rules, diff degenerates into “delete all, add all.” **Governance** should treat identity migration as a **decision**-visible change when **traceability** or **evidence** history must remain continuous—especially for addressable Normative Propositions whose authority remains with the declaring ADR.

### Link to intent change

Model diff alone is incomplete. **Intent** **artifacts** should move in **lockstep** when semantics change: an **ADR** update explains why a Normative Proposition or structural edge moved ([Change and evolution](../05-lifecycle/05-07-change-and-evolution.md)). Silent model-only edits recreate **drift** between normative sources and machine representation.

## The Implications

Publish **architecture changelogs** derived from model diff for human review; use the same diff to drive selective **validation** (“only rerun checks touching this subgraph”). **Projections** should reflect post-diff state automatically when regenerated—if they do not, you have a **projection** pipeline bug, not “architecture changed.”

When Normative Proposition fields change, preserve declaring-authority and identity discipline in the changelog narrative so reviewers do not mistake a normalized or projected view for a new policy source.

## Relationship to STE system

- **Graph framing:** [IR as a semantic graph](04-07-ir-as-a-graph.md).
- **Governance:** [Change management](../06-governance/06-05-steelman-obligations-and-change-control.md), [The governance model](../06-governance/06-02-the-governance-model.md).
- **Lifecycle:** [Architecture definition](../05-lifecycle/05-02-architecture-definition.md).
- **Kernel** reasoning: [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).

## Summary

- **Diff** over the architecture model compares addressable structural and semantic commitments, not diagram opinion.
- **Identity** discipline makes semantic diff meaningful across time—including for Normative Propositions.
- Mechanical field change is not automatic proof of material meaning change or identity replacement; competent review remains where contracts require it.
- Model changes should pair with **intent** changes when **semantics** move.

**Next:** [IR as a semantic graph](04-07-ir-as-a-graph.md).
