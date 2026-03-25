---
title: "Requirements and Constraints"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Requirements and Constraints

**Artifact type:** Requirement and **constraint** records (including capability-style obligation bundles).  
**Role in STE:** State what must be satisfied and which bounds apply, as normative **intent** in the graph.  
**Primary concern:** intent (obligations and design-space bounds, not “must always hold” properties; those are **invariants**).  
**Connects to:** **ADRs**, **invariants**, **Architecture IR**, **evidence**, **traceability**, **conformance**.

## The Problem this artifact solves

Work proceeds from tacit expectations. “We need it fast” and “it must never drop data” live in different heads until a failure proves they were never reconciled. Structured **requirements** and **constraints** make obligations **testable in principle**, **traceable**, and **negotiable** under **governance** instead of exploding in production.

## What the artifact is

**Requirements** (in STE handbook use) are structured statements of what the system or service must satisfy: behavior, quality attributes, interfaces, or operational outcomes. **Constraints** are bounds on the design space: standards, resource limits, regulatory rules, compatibility floors, or forbidden patterns.

**Capabilities** (what the system must be able to do) appear as requirement families or named obligation bundles, not as an untyped aside. A capability such as “authenticated clients may revoke sessions” should appear as explicit requirements with owners and review status, the same as any other normative statement.

These artifact types are **intent**. They are not **Architecture IR** itself, though they compile into or reference IR elements where STE defines that binding. They differ from **invariants** (see [Invariants](03-03-invariants.md)): requirements and **constraints** name obligations and bounds; **invariants** name properties that must hold continuously in scope.

## How it is used in STE

People **specify** obligations; STE holds requirement and **constraint** records, **compilation**, and links under **ste-spec**. **Validation** plans and **evidence** scopes attach to stable identifiers so **conformance** can be argued with records, not opinions.

**Example:** A latency **constraint** caps P99 for a checkout path. CI performance tests and production SLO monitors produce **evidence** tied to that **constraint** identifier. When the business relaxes the number, the **constraint** artifact updates under **governance**, and scopes for checks update with it.

## How it relates to intent, implementation, or evidence

- **Intent:** requirements and **constraints** are normative **intent**.
- **Implementation:** **Embodiment** is judged against them through **evidence** and assessment.
- **Evidence:** binds to requirement or **constraint** IDs (or equivalent scopes) so pass or fail means something specific.

## How it participates in lifecycle and governance

Changes to requirements or **constraints** need the same discipline as **ADRs**: impact analysis, review, and updates to linked IR or rules. Waivers need owners and expiry when policy requires. Capability changes often drive interface and **invariant** updates; those links should not be implicit.

## Relationship to other artifacts

- [Architecture decision records](03-01-architecture-decision-records.md): major requirement shifts often follow from or trigger recorded decisions.
- [Invariants](03-03-invariants.md): **constraints** and **invariants** overlap in language; STE treats **invariants** as properties that must hold, often narrower and more checkable than broad requirements.
- [Architecture model and IR](03-04-architecture-model-and-ir.md): structural requirements map to elements and relationships in the IR.
- [Conformance](03-07-conformance.md): **conformance** claims reference requirements and **constraints** as their normative side.
- Part 1: [Safety and constraints engineering](../01-theoretical-foundations/01-06-safety-and-constraints-engineering.md) for theoretical grounding.
