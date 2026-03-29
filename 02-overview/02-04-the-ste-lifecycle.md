---
title: "The STE Lifecycle"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# The STE Lifecycle

## The Problem

Lifecycle language shows up everywhere in the handbook. Without a frame, readers import a waterfall picture: write **intent**, build once, test once, ship, done. Software-intensive systems do not behave that way. **Intent** moves. **Embodiment** moves. **Evidence** accrues continuously. **Governance** must handle mid-course corrections.

If Part 2 implied a document phase model, it would mis-train readers for everything that follows.

## The Reframe

Treat STE as a living **control loop**, not a phase model for documents. The useful analogy is feedback around a **reference** (**intent** and compiled **Architecture IR**), **measurements** (**evidence** about **embodiment**), and **actuators** (authorized edits to **intent**, **embodiment**, **rules**, and tooling) under **governance**—not “write requirements, then finish.” STE is lifecycle **governance**, not only a first-pass design exercise: legitimacy of change stays on the hook as **intent**, **architecture**, **embodiment**, and **evidence** move. Design and acceptance matter, but they repeat. **Evidence** is not a one-time gate. **Certification** or acceptance is a framed decision at a **scope** in time, not a permanent badge that excuses future drift. **Change** returns you to **decisions** and **invariants** with honest updates.

## The Model

### Handbook-level chain

At the highest level, STE repeats:

1. **Intent**
2. **Architecture** (**Architecture IR** as the canonical **system model**, **projections** and mechanical **queries** / analysis on IR, compiled from structured **intent**)
3. **Implementation** (**embodiment**)
4. **Evidence**
5. **Assessment**
6. **Conformance** (the claim **assessment** addresses)
7. **Change** (authorized updates to **intent**, **embodiment**, or both)
8. **Repeat**

The boxes and edges those steps use are in [System overview](02-03-system-overview.md). This chapter stresses **when** the loop turns, not a second structural diagram.

### Stages at handbook altitude

These stages are scaffolding for language, not a procedure you must copy verbatim:

1. **Design (intent formation).** **Decisions** under **constraints** land in **intent** **artifacts**. How compilation, **Architecture IR**, **projections**, and conversation surfaces connect is the structural story in [System overview](02-03-system-overview.md). At lifecycle altitude, design is whenever normative commitments are formed or revised.
2. **Embodiment (implementation and operation).** Teams realize **embodiment**: code, configuration, infrastructure, releases, and operational behavior. This stage is continuous, not a single build event.
3. **Evidence generation.** Pipelines, tests, telemetry, experiments, and audits produce **evidence** with provenance. **Evidence** is ongoing, especially after change.
4. **Assessment.** **Validation** compares **embodiment** to **intent** under **rules** for a declared **scope** (handbook sense in [Terminology](02-02-terminology.md)). Mechanical checks and judgment-shaped review both land here, with honesty about which is which.
5. **Certification or acceptance.** A **governance**-visible decision records that a **scope** is accepted for a purpose: release, region expansion, regulated milestone, or internal bar. The record should point at **evidence**, not at vibes.
6. **Change and re-evaluation.** New **constraints**, incidents, discoveries, or strategy shifts reopen **decisions**. Updated **intent** feeds back into the structural path (compile, assess) described in [System overview](02-03-system-overview.md). This is loop closure.

### Governance hooks across the lifecycle

**Governance** is not a final sign-off bolted on at the end. It appears when **intent** changes, when **exceptions** are granted, when **invariants** are revised, and when **assessment** shows **drift** that must be owned. The point is legibility: someone accountable authorized the state transition.

### Feedback edges (the continuous part)

Return paths include:

- **Assessment → governance:** non-**conformance** or risk signals trigger decisions.
- **Governance → intent:** revised **decisions** and **invariants** update the normative record.
- **Governance → embodiment:** planned remediation, feature work, or operational fixes.
- **Embodiment → evidence:** new behavior produces new observations, which feed the next assessment.

### API compatibility over time

Compatibility lived in declared **intent**; **embodiment** still diverged when a fast-follow service shipped a breaking change by accident. **Evidence** shows failing contract tests and rising client errors. **Assessment** flags **drift** between **intent** and **embodiment**. **Governance** chooses rollback, fix-forward, or a deliberate **intent** change with communicated impact. Weeks later, telemetry becomes new **evidence** for a smaller **scope** check. The lesson is recurrence: the loop runs again whenever reality moves.

## The Implications

Readers should expect recurring passes, not a single heroic alignment project. If this chapter reads like a waterfall document flow, reread it as **control**: each stage produces signals that **governance** uses to update the **reference** or the **embodiment** plan. Documentation-only STE fails precisely because it skips **evidence** and **governance** return paths. Tool-only STE fails when **intent** is thin and **governance** cannot say no.

## Relationship to STE system

Stage-by-stage lifecycle accountability is in Part 5 ([Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md)). Control loop mechanics live in Part 6 ([Governance overview](../06-governance/06-00-lifecycle-overview.md)). Operational detail, roles, and policy interfaces expand in that same governance part; start from [Governance overview](../06-governance/06-00-lifecycle-overview.md); it may still be skeletal, but it names the deeper roadmap.

Related orienting chapters:

- [How to read diagrams and projections](02-05-how-to-read-diagrams-and-projections.md)
- [Control loop overview](../06-governance/06-07-control-loop-overview.md)
- [Kernel overview](../07-kernel/07-00-overview.md)

Lifecycle semantics at the contract level remain in **ste-spec** where applicable.

**Next:** Continue into Part 3 with [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md). Part 2 ends with orientation; the handbook becomes operational about **intent** **artifacts**, **decisions**, and **constraints** there. After Part 4, Part 5 walks the lifecycle in depth. Keep [Governance overview](../06-governance/06-00-lifecycle-overview.md) in view when you need policy-oriented lifecycle mechanics beyond that walkthrough.

## Summary

- STE lifecycle language describes a repeating **closed-loop control** story, not a single pass through documents.
- Stages cover **intent**, **embodiment**, **evidence**, **assessment**, acceptance or certification, and **change**.
- **Governance** attaches at transitions, exceptions, and revisions, not only at the end.
- Parts 5 and 6 carry deeper lifecycle, governance, and control-loop framing; this chapter prevents waterfall misreadings.
