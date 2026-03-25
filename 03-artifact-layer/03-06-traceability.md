---
title: "Traceability"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Traceability

**Artifact type:** **Trace** links (governance artifact: typed edges and identifiers in the artifact graph).  
**Role in STE:** Connect intent, structural, implementation, and evidence records so impact and obligation are navigable.  
**Primary concern:** governance (linking structure; not a standalone write-up).  
**Connects to:** all canonical artifact types; especially **Architecture IR**, **evidence**, **conformance**.

## The Problem this artifact solves

When links are only mental, impact analysis fails. Nobody can answer which requirements a service satisfies, which **ADRs** authorized an interface, or which checks matter for a **constraint**. **Traceability** is the **cross-type linking structure** of the STE artifact system: maintained references among **intent**, **Architecture IR**, **implementation** / **embodiment**, and **evidence** (and governance records where stored), so change is navigable and review is finite.

## What the artifact is

**Traceability** is not a separate idea you bolt on after the fact. Without canonical artifact types and stable IDs, links cannot mean anything repeatable. In STE, **traceability** is the property that **trace** edges exist in the graph: requirement to IR element to repository identity to **evidence** record, or **ADR** to compiled elements to validation scopes. **ste-spec** defines schemas, compilation outputs, and metadata that materialize those edges.

**Trace** links are **governance artifacts**: they must be maintained under policy. Humans **govern and correct** link quality; STE **creates and updates** links through compilation, ingestion, and automation where **ste-spec** assigns that responsibility.

## How it is used in STE

Reviewers follow **trace** paths during design and **governance** reviews. Automation uses the same graph to select checks, scope **evidence** collection, and highlight blast radius for a proposed change.

**Example:** A **constraint** on encryption at rest links to three storage components in IR. A change that adds a new store without updating the **constraint** or its links surfaces as a compilation or policy gap instead of a surprise audit finding.

## How it relates to intent, implementation, or evidence

- **Intent:** supplies normative endpoints (what must be satisfied).
- **Implementation:** **embodiment** supplies physical endpoints (what exists).
- **Evidence:** supplies the observational leg (what was checked).

## How it participates in lifecycle and governance

Weakening **traceability** (dropping IDs, orphaning records) is a **governance** failure comparable to weakening **intent**. Policies can require minimum link coverage for production paths or regulated scopes. Exceptions need explicit handling when STE allows them.

## Relationship to other artifacts

- [Architecture model and IR](03-04-architecture-model-and-ir.md): IR is the central spine for many edges.
- [Evidence](03-05-evidence.md): **evidence** records must reference stable scopes to participate in **traceability**.
- [Conformance](03-07-conformance.md): **conformance** uses **traceability** to bind obligations to checks and results.
- Part 4: [Traceability](../04-architecture-ir/04-05-traceability.md) for IR-internal and compilation-oriented mechanics.

Part 3 treats **traceability** as a layer-wide **governance** structure; Part 4 explains how IR carries it mechanically.
