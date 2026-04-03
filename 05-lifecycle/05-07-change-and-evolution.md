---
title: "Part 5: Change and Evolution"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Change and evolution

**Change** is how systems move forward under STE: planned features, fixes, **intent** updates, model edits, and operational adjustments. **Evolution** is the accumulated effect of many such changes while **governance** keeps the story honest.

## Purpose of this stage

Close the control loop. Authorized **change** updates the artifacts and **embodiment** so that the next pass through **evidence** and **conformance** addresses a new honest baseline.

## Artifacts involved

Revised **intent** artifacts, updated **Architecture IR**, new or modified **implementation** artifacts, refreshed **trace** links, and new **evidence** after **change** lands. See [Change management](../06-governance/06-05-steelman-obligations-and-change-control.md) and [Diff and change](../04-architecture-model/04-06-diff-and-change.md).

## Human responsibility

Humans propose **change**, estimate risk, carry review duties, communicate impact to dependents, and ensure that **decisions** that authorized **change** are reflected in the artifact graph (not only in merged code).

## STE system responsibility

STE updates or regenerates affected records, recomputes **diffs** and projections, revalidates **trace** integrity where automated, schedules or triggers reassessment, and moves **lifecycle state** forward when policy defines those transitions.

## Transitions to the next stage

After **change**, the loop returns toward **intent formation** or **architecture definition** when commitments shift, toward **implementation and operation** when execution continues, and always toward fresh **evidence** before strong **conformance** claims recur. There is no terminal “done” state for a live system.

**Next stage chapter:** [Lifecycle states and transitions](05-08-lifecycle-states-and-transitions.md) integrates how those returns are recorded.

## Relationship to intent, implementation, and evidence

- **Intent:** **Change** may start from **intent** (policy or product shift) or end by revising **intent** when reality proved the old stance untenable.
- **Implementation:** Most visible **change** lands in **implementation** and operations first; STE still requires artifact and **trace** discipline so **embodiment** stays explainable.
- **Evidence:** Post-change **evidence** is the proof that **change** did what **governance** expected and did not break adjacent **constraints**.

## Relationship to other chapters

- [The governance model](../06-governance/06-02-the-governance-model.md)
- [Convergence](../06-governance/06-02-the-governance-model.md)
- [Steelman, obligations, and change control](../06-governance/06-05-steelman-obligations-and-change-control.md)
- **ste-spec** for change and versioning semantics.

**Next:** [Lifecycle states and transitions](05-08-lifecycle-states-and-transitions.md).
