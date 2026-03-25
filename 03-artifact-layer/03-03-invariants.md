---
title: "Invariants"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Invariants

## The Problem this artifact solves

Systems fail in predictable ways when unstated assumptions break: invariants that “everyone knew” were never written down, or were written in prose that tools cannot use. **Invariants** as **intent** artifacts make those assumptions **explicit**, **stable**, and **eligible for validation** so teams cannot silently violate them across refactors.

## What the artifact is

An **invariant** is a statement of a property that must hold in a defined scope: data rules, ordering guarantees, safety boundaries, or architectural rules (“every external call passes through the gateway”). In STE **invariants** are **intent** artifacts. They are narrower than a full requirements catalog: they name what must remain true for the system to remain the same system in a **governance** sense.

They are not **evidence** of correctness; they are commitments that **evidence** and rules may check. They are not the **Architecture IR** graph, though they link to IR elements when compilation defines that mapping.

## How it is used in STE

Authors record **invariants** when the organization commits to a property. Static analysis, tests, monitors, or manual audits produce **evidence** against those records. When an **invariant** must change, **governance** updates the artifact and replans **validation** scope.

**Example:** “No service other than the auth service may read the password hash column.” That **invariant** drives access reviews, schema tooling rules, and database audit **evidence**. Breaking it is either a defect or a governed change to the **invariant**.

## How it relates to intent, implementation, or evidence

- **Intent:** **invariants** are hard **intent**: properties that must hold.
- **Implementation:** **Embodiment** must respect them; violations are **drift** or failures unless explicitly waived under policy.
- **Evidence:** demonstrates whether the property holds for declared scopes and moments in time.

## How it participates in lifecycle and governance

Relaxing or tightening an **invariant** is a high-signal act. It should trigger review of **ADRs**, **constraints**, IR compilation, and **conformance** pipelines. Temporary waivers need accountable owners and dates where safety or policy demands.

## Relationship to other artifacts

- [Requirements and constraints](03-02-requirements-and-constraints.md): **constraints** bound the design space; **invariants** state properties that must hold within it.
- [Architecture decision records](03-01-architecture-decision-records.md): decisions may add, remove, or reinterpret **invariants**.
- [Architecture model and IR](03-04-architecture-model-and-ir.md): **invariants** often attach to components, interfaces, or data entities in the IR.
- [Conformance](03-07-conformance.md): **conformance** frequently means “**invariants** and requirements hold under **evidence**.”
- Part 5: [Validation](../05-kernel/05-03-validation.md) for assessment mechanics.
