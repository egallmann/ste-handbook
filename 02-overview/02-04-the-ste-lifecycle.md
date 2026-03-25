---
title: "The STE Lifecycle"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# The STE Lifecycle

## The Problem

Lifecycle language shows up everywhere in the handbook. Without a frame, readers import a waterfall picture: write **intent**, build once, test once, ship, done. Software-intensive systems do not behave that way. **Intent** moves. **Embodiment** moves. **Evidence** accrues continuously. **Governance** must handle mid-course corrections.

If Part 2 implied a document phase model, it would mis-train readers for everything that follows.

## The Reframe

Treat STE as a living control loop. Design and acceptance matter, but they repeat. **Evidence** is not a one-time gate. **Certification** or acceptance is a framed decision at a **scope** in time, not a permanent badge that excuses future drift. **Change** returns you to **decisions** and **invariants** with honest updates.

## The Model

### Stages at handbook altitude

These stages are scaffolding for language, not a procedure you must copy verbatim:

1. **Design (intent formation).** **Decisions** under **constraints** become **intent** **artifacts** and compile into **Architecture IR** where the pipeline exists. **Projections** help humans review what the commitments imply.
2. **Embodiment (implementation and operation).** Teams realize **embodiment**: code, configuration, infrastructure, releases, and operational behavior. This stage is continuous, not a single build event.
3. **Evidence generation.** Pipelines, tests, telemetry, experiments, and audits produce **evidence** with provenance. **Evidence** is ongoing, especially after change.
4. **Assessment.** **Validation** compares **embodiment** to **intent** under **rules** for a declared **scope**. Mechanical checks and judgment-shaped review both land here, with honesty about which is which.
5. **Certification or acceptance.** A **governance**-visible decision records that a **scope** is accepted for a purpose: release, region expansion, regulated milestone, or internal bar. The record should point at **evidence**, not at vibes.
6. **Change and re-evaluation.** New **constraints**, incidents, discoveries, or strategy shifts reopen **decisions**. Updated **intent** flows back through compilation, fresh **evidence**, and new assessments. This is the loop closure.

### Governance hooks across the lifecycle

**Governance** is not a final sign-off bolted on at the end. It appears when **intent** changes, when **exceptions** are granted, when **invariants** are revised, and when **assessment** shows **drift** that must be owned. The point is legibility: someone accountable authorized the state transition.

### Feedback edges (the continuous part)

Return paths include:

- **Assessment → governance:** non-**conformance** or risk signals trigger decisions.
- **Governance → intent:** revised **decisions** and **invariants** update the normative record.
- **Governance → embodiment:** planned remediation, feature work, or operational fixes.
- **Embodiment → evidence:** new behavior produces new observations, which feed the next assessment.

### API compatibility again, over time

At design time, **intent** records compatibility promises. During **embodiment**, a fast-follow service ships a breaking change by accident. **Evidence** surfaces failing contract tests and rising client errors. **Assessment** flags **drift** between **intent** and **embodiment**. **Governance** chooses rollback, a fix-forward plan, or a deliberate **intent** change with communicated impact. Two weeks later, telemetry becomes new **evidence** for a smaller **scope** check. That is the lifecycle shape STE assumes.

## The Implications

Readers should expect recurring passes, not a single heroic alignment project. Documentation-only STE fails precisely because it skips **evidence** and **governance** return paths. Tool-only STE fails when **intent** is thin and **governance** cannot say no.

## Relationship to STE system

This chapter frames language for the whole book. Operational detail, roles, and policy interfaces expand in Part 9 and adjacent chapters. Start from [Part 9: Lifecycle and Governance overview](../09-lifecycle-governance/09-00-lifecycle-overview.md); it may still be skeletal, but it names the deeper roadmap.

Related orienting chapters:

- [Control loop overview](../06-control-loop/06-00-control-loop-overview.md)
- [Kernel overview](../05-kernel/05-00-kernel-overview.md)

Lifecycle semantics at the contract level remain in **ste-spec** where applicable.

## Summary

- STE lifecycle language describes a repeating loop, not a single pass through documents.
- Stages cover **intent**, **embodiment**, **evidence**, **assessment**, acceptance or certification, and **change**.
- **Governance** attaches at transitions, exceptions, and revisions, not only at the end.
- Part 9 carries operational depth; this chapter prevents waterfall misreadings.
