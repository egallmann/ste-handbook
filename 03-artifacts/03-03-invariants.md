---
title: "Invariants"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Invariants

**Artifact type:** **Invariant** record.  
**Role in STE:** State a property that must hold in a defined scope, as hard **intent** checkable against **embodiment**.  
**Primary concern:** intent (must-hold truths, distinct from general requirements and **constraints** in [Requirements and constraints](03-02-requirements-and-constraints.md)).  
**Connects to:** **ADRs**, requirements and **constraints**, **Architecture IR**, **evidence**, **traceability**, **conformance**.

## The Problem this artifact solves

Systems fail when unstated assumptions break: properties “everyone knew” were never captured as typed records, or lived only in prose tools cannot use. **Invariant** artifact types make those assumptions **explicit**, **stable**, and **eligible for validation** so teams cannot silently violate them across refactors.

## What the artifact is

An **invariant** is a statement of a property that must hold in a defined scope: data rules, ordering guarantees, safety boundaries, or architectural rules (“every external call passes through the gateway”). In STE **invariants** are **intent** artifacts. They are narrower than a full requirements catalog: they name what must remain true for the system to remain the same system in a **governance** sense.

They are not **evidence** of correctness; they are commitments that **evidence** and rules may check. They are not the **Architecture IR** graph, though they link to IR elements when compilation defines that mapping. That linkage is how “must hold” statements become **mechanically targetable** alongside graph-shaped structure under agreed **rules**.

## How it is used in STE

People **define** non-negotiable properties; STE stores **invariant** records and links them into IR and checks where **ste-spec** defines it. Static analysis, tests, monitors, or manual audits produce **evidence** against those records. When an **invariant** must change, **governance** updates the record and replans **validation** scope.

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
- Part 7: [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) for assessment mechanics.
