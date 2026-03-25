---
title: "Traceability"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Traceability

## The Problem this artifact solves

When links are only mental, impact analysis fails. Nobody can answer which requirements a service satisfies, which **ADRs** authorized an interface, or which tests matter for a **constraint**. **Traceability** in STE is the maintained graph of references between **intent**, **Architecture IR**, **embodiment**, and **evidence** so change is navigable and review is finite.

## What the artifact is

**Traceability** is not one file type. It is the property that identifiers and edges exist so tools and humans can walk the chain: requirement to IR element to repository path to **evidence** record, or **ADR** to compiled elements to validation scopes. STE encodes traceability through schemas, compilation outputs, and record metadata defined in **ste-spec**.

Handbook level: treat **traceability** as a cross-cutting obligation on the artifact layer, implemented by concrete links rather than narrative prose alone.

## How it is used in STE

Authors and tools add or preserve links when **intent** or IR changes. Reviewers follow links during design and **governance** reviews. Automation uses the same graph to select checks, scope **evidence** collection, and highlight blast radius for a proposed change.

**Example:** A **constraint** on encryption at rest links to three storage components in IR. A change that adds a new store without updating the **constraint** or its links surfaces as a compilation or policy gap instead of a surprise audit finding.

## How it relates to intent, implementation, or evidence

- **Intent:** supplies the normative endpoints of **traceability** (what must be satisfied).
- **Implementation:** **embodiment** supplies the physical endpoints (what exists).
- **Evidence:** supplies the observational edge (what was checked).

## How it participates in lifecycle and governance

Weakening **traceability** (dropping IDs, orphaning records) is a **governance** problem comparable to weakening **intent**. Policies can require minimum link coverage for production paths or regulated scopes. Exceptions need explicit handling when STE allows them.

## Relationship to other artifacts

- [Architecture model and IR](03-04-architecture-model-and-ir.md): IR is the central spine for many edges.
- [Evidence](03-05-evidence.md): **evidence** records must reference stable scopes to participate in **traceability**.
- [Conformance](03-07-conformance.md): **conformance** arguments lean on **traceability** to show which checks map to which obligations.
- Part 4: [Traceability](../04-architecture-ir/04-05-traceability.md) for IR-internal and compilation-oriented **traceability** depth.

Part 3 explains **traceability** as a layer concern; Part 4 explains how IR carries it mechanically.
