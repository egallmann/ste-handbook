---
title: "Evidence and Observation"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-30"
---

# Evidence and Observation

## The Problem

Teams treat logs, metrics, and screenshots as interchangeable with architecture knowledge. They are not. Without a disciplined distinction between observation (what was sensed) and durable evidence bound to **Architecture IR**, assessment cannot compare desired structure to actual behavior in a repeatable way. **Kernel** evaluation lacks typed inputs.

## The Reframe

Observation is **Runtime**’s raw structured sense of embodiment or the observation toolchain: channel, time, scope, and hooks toward **Architecture IR** identities. **ArchitectureEvidence** is what observations become when packaging rules are met: EDR-shaped records (handbook sense) that reference the same identities **Architecture IR** uses, so **Kernel** and governance can replay arguments across tools and time.

Neither observation nor **ArchitectureEvidence** is intent; neither replaces ADRs or **Architecture IR**.

## Why this matters

**Observed** state is the only honest picture of embodiment. If it is not structured, scoped, and linkable, the control loop cannot close. Reasoning safety for humans and AI depends on that chain being explicit.

## The Model

### Observation

An observation includes:

- Channel (tests, telemetry, reconciliation outcomes, synthetic checks, toolchain health—illustrative list).
- Time and environment scope (commit, deployment slice, service boundary).
- Identity hooks alignable to **Architecture IR** nodes, trace edges, or obligation identifiers.

Observations may be ephemeral until promoted; policy defines retention and minimum fields.

### Evidence

**ArchitectureEvidence** packages observations into durable records that support assessment:

- What was observed (outcome, metric, structured result).
- Where it applies (scope).
- Provenance (pipeline, actor, inputs where policy requires).
- Links to **Architecture IR** and trace as required for the conformance story.

Exact envelopes are ste-spec; the handbook requires addressability relative to **Architecture IR**.

### Evidence versus artifacts versus IR

| Object | Role |
|--------|------|
| Intent artifacts (ADRs, invariants, …) | Declare what should hold; human-governed **canonical** intent sources. |
| **Architecture IR** | Compiled structural model of that intent for machine traversal and **Kernel** input. |
| Evidence (**ArchitectureEvidence**) | **Observed** record of embodiment; input to compare, not a substitute for intent or **Architecture IR**. |
| Projections | **Derived** views of **Architecture IR** (or tooling outputs); not evidence unless separately packaged as such. |

### Observation → evidence promotion

| Stage | Character |
|-------|-----------|
| Observation | Structured sense; may be transient; may await linkage. |
| Evidence | Meets provenance and **Architecture IR** binding rules; suitable for **Kernel** and audit. |

### Non-decision-bearing

**Runtime**-side records state what was observed. **Admission** and verdict live with **Kernel** and governance ([Runtime–Kernel Contract](08-06-runtime-kernel-contract.md)).

### Categories (handbook level)

Tests, audits, telemetry, and similar channels become **ArchitectureEvidence** when packaged; binding to **Architecture IR** makes assessment legible. Shapes are normative in ste-spec.

### Immutability and supersession

Evidence is typically append-only or superseded-by newer records under governance—not silently rewritten.

How evidence is classified (fresh, stale, invalid, missing) is defined in [Freshness and Validity](08-03-freshness-and-validity.md); this chapter stops at durable, addressable **ArchitectureEvidence**.

## The Implications

- Define channel contracts: mandatory fields before promotion to evidence.
- Forbid using projection files as evidence unless packaged and scoped as observation of a defined pipeline outcome.
- Require identity hooks early: without them, traceability and deterministic **Kernel** behavior do not scale.

## Relationship to STE system

- [Evidence](../03-artifacts/03-05-evidence.md)
- [Intent versus implementation](../00-problem/00-03-intent-vs-implementation.md)
- [Entities](../04-architecture-model/04-02-entities.md), [Traceability in Architecture IR](../04-architecture-model/04-05-traceability.md)
- [Evidence and observation](../05-lifecycle/05-04-evidence-and-observation.md), [Implementation to evidence](../06-governance/06-10-implementation-to-evidence.md)
- [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md)

## Summary

- Observation structures embodiment signals; **ArchitectureEvidence** makes them durable and **Architecture IR**-addressable.
- Intent, **Architecture IR**, evidence, and projections are different object classes; conflating them breaks the loop.
- Evidence is input to **Kernel** comparison; it is not **Admission**.

Classification of evidence states is the subject of the next chapter.

**Next:** [Freshness and Validity](08-03-freshness-and-validity.md).
