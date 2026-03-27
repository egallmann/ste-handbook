---
title: "Architecture Model and IR"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Architecture Model and IR

**Artifact type:** Canonical **Architecture IR** (compiled architecture model and decompositions).  
**Role in STE:** Provide the **structural** single source of truth for tooling, linking, and **projection** generation.  
**Primary concern:** structural.  
**Connects to:** intent artifact types (inputs to compilation), **implementation** identities, **evidence** scopes, **traceability**, **conformance**, **publication** versus **projection**.

## The Problem this artifact solves

Without a single canonical architecture model, every tool builds its own graph from scraps. Views disagree, diffs are meaningless across teams, and automation cannot tell whether two changes touch the same dependency. **Architecture IR** exists so STE has one **machine-readable** structural truth compiled from **intent** and related inputs, suitable for inspection, **traceability**, and assessment.

## What the artifact is

**Architecture IR** is STE’s canonical architecture model: entities, relationships, and metadata needed for deterministic tooling. It is the compiled structural **intent** at the architecture level, materialized as graph-shaped records, not an informal wiki. “Architecture model” in handbook language refers to that canonical IR and its consistency rules as a product of compilation.

It is not source code, though it maps to repositories and services. It is not a **projection** diagram, though **projections** render from it.

## How it is used in STE

**Intent** drives compilation; STE **maintains** IR updates, diffs, and consistency. Tools traverse the graph and drive **validation** rules. The **Kernel** role (Part 7) consumes IR together with **evidence** to assess **conformance** claims. **Projections** (Part 4) render human-facing views from the same IR so review does not fork reality.

**Example:** A new dependency from the payment service to a marketing database appears in IR after compilation. A policy rule flags it because **intent** forbids that edge. The failure is visible before merge because the model is shared and addressable.

## How it relates to intent, implementation, or evidence

- **Intent:** IR is derived from **ADRs**, requirements, **constraints**, and **invariants** plus compilation rules.
- **Implementation:** IR references **embodiment** identities (services, repos, environments) so observation can target real artifacts.
- **Evidence:** ties to IR scopes (components, interfaces, paths) so results attach to the same objects **governance** discusses.

## How it participates in lifecycle and governance

IR changes should correlate with governed **intent** changes. Silent drift between IR and **embodiment** is a first-class STE concern: detection and response live in the control loop and **governance** parts. Compilation failures (intent inconsistent or incomplete) block or warn according to policy.

## Relationship to other artifacts

- [Architecture decision records](03-01-architecture-decision-records.md): decisions supply rationale; IR supplies the structural projection of commitments.
- [Traceability](03-06-traceability.md): IR is the hub for many **traceability** edges.
- [Publication versus projection](03-08-publication-vs-projection.md): IR is published truth at the architecture model layer; diagrams are **projections**.
- Part 4: [Architecture IR overview](../04-architecture-model/04-00-architecture-ir-overview.md), [Compilation](../04-architecture-model/04-04-compilation.md), [Traceability](../04-architecture-model/04-05-traceability.md) for IR-centric depth.
