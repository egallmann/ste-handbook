---
title: "Compilation"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Compilation

## The Problem

If **Architecture IR** is edited by hand like a wiki, it becomes another document that **drifts** from **intent**. If every tool infers IR independently, there is no **canonical** model. **Compilation** names the disciplined bridge: structured **intent** **artifacts** (and related inputs) are transformed into **Architecture IR** under explicit rules, with failures that **governance** can see instead of silent graph rot.

## The Reframe

**Compilation**, in STE handbook usage, is the **intent-to-IR** pipeline—the **architecture model build** that turns governed **intent** **artifacts** into the canonical **Architecture IR**—not the programming-language sense alone. It parses normative inputs, resolves references, materializes **entities** and **relationships**, attaches metadata, and emits a model state suitable for storage, **diff**, **projection**, **query**, and **validation**. Determinism is an **expectation where honest**: same inputs and rules should yield the same structural result, modulo declared nondeterministic steps called out in policy.

## The Model

### Inputs

Typical inputs include **ADRs**, **requirements** and **constraints**, **invariants**, capability or context maps, and other structured **intent** records the organization admits into the pipeline. **ste-spec** and local policy define the exact set; the handbook claim is only that inputs are **structured enough** to fail visibly when incomplete or inconsistent.

### Stages (conceptual)

A compilation story often includes: **ingest** (read and normalize inputs), **resolve** (identifiers, versions, scopes), **elaborate** (expand patterns into concrete edges), **validate** (metamodel and policy checks), and **emit** (write IR state). Boundaries between validate-here versus validate-in-**Kernel** vary by deployment; conceptually, **compilation** proves “this **intent** set corresponds to a coherent structural model,” while **Kernel** work often combines IR with **evidence** for **admission** and **conformance** claims.

### Errors and governance

Compilation failures are **governance signals**: missing links, contradictory **constraints**, unknown identities. Teams choose whether failures block merge, warn, or route to exception workflows. The important shift is from hidden inconsistency to **accountable** outcomes ([Governed reasoning](../00-problem/00-05-governed-reasoning.md)).

### Relationship to admission

**Admission** (Part 7) may consume compiled IR plus **evidence** and contracts to decide what may progress. This chapter stops at the **model-build** story; for **Admission** framing see [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).

## The Implications

Treat **compilation** as part of the engineering **supply chain**. Changes to **intent** without recompilation produce **drift** between what **governance** approved and what IR claims. CI-like automation for compilation makes **projections** and checks trustworthy; skipping it trades speed for unreviewable structure.

## Relationship to STE system

- **Model concepts:** [Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md), [Entities](04-02-entities.md), [Relationships](04-03-relationships.md).
- **Artifact overview:** [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md).
- **Terminology:** [Terminology](../02-overview/02-02-terminology.md) (**compilation** sense).
- **Lifecycle:** [Architecture definition](../05-lifecycle/05-02-architecture-definition.md).
- **Kernel:** [Kernel overview](../07-kernel/07-00-overview.md), [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).

## Summary

- **Compilation** transforms structured **intent** into **Architecture IR** under explicit rules.
- Failures should be **visible** to **governance**, not absorbed informally.
- **Admission** and **evidence**-linked checks build on compiled IR; they are not the same job as compilation itself.

**Next:** [Traceability in Architecture IR](04-05-traceability.md).
