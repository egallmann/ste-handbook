---
title: "Architecture Model and IR"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-10-06"
---

# Architecture Model and IR

**Artifact type:** Canonical **Architecture IR** (machine-oriented semantic architecture model and decompositions).  
**Role in STE:** Provide the canonical machine-addressable architecture model for tooling, linking, and **projection** generation—without replacing declaring-source authority.  
**Primary concern:** semantic architecture representation (structural and other admitted semantic entities).  
**Connects to:** intent artifact types (inputs to construction/compilation), **implementation** identities, **evidence** scopes, **traceability**, **conformance**, **publication** versus **projection**.

## The Problem this artifact solves

Without a single canonical architecture model, every tool builds its own graph from scraps. Views disagree, diffs are meaningless across teams, and automation cannot tell whether two changes touch the same dependency or the same Normative Proposition. **Architecture IR** exists so STE has one **machine-readable** semantic architecture model produced from **intent** and related inputs, suitable for inspection, **traceability**, and assessment.

## What the artifact is

**Architecture IR** is STE’s canonical **system model** at the architecture layer for an agreed **scope**: typed entities, relationships, and metadata needed for deterministic tooling and for shared mechanical reasoning. It carries structural semantics and other admitted semantic types (including decisions, invariants, and Normative Propositions where governed), materialized as graph-shaped records—not an informal wiki and not “just another diagram format.” “Architecture model” in handbook language refers to that canonical IR and its consistency rules as a product of compilation and related materialization. Representation does not transfer declaring authority from ADRs or other source artifacts.

It is not source code, though it maps to repositories and services. It is not a **projection** diagram, though **projections** render from it. It is not a repository index, manifest, or entity registry. Those discovery surfaces are generated from the validated authoring path. They are not compiled into semantic meaning, and they are not the exact source basis interpretation reads.

## How it is used in STE

Canonical records are produced through the ADR-Kit authoring API, not by hand. Authoring validation evaluates those records and regenerates discovery. It does not construct the exact source basis. Where mapping to **Architecture IR** exists, that representation stays distinct from the index. The **Kernel** role (Part 7) is the reserved decision role that may consume IR together with **evidence**. The authoring kit does not produce admission decisions. **Projections** (Part 4) render human-facing views so review does not fork reality. A projection is not the IR.

**Example:** A new dependency from the payment service to a marketing database appears in IR after compilation. A policy rule flags it because **intent** forbids that edge. The failure is visible before merge because the model is shared and addressable.

## How it relates to intent, implementation, or evidence

- **Intent:** IR represents commitments from **ADRs** (including ADR-local Normative Propositions where declared), requirements, **constraints**, and **invariants** plus compilation/materialization rules—without becoming the declaring authority.
- **Implementation:** IR references **embodiment** identities (services, repos, environments) so observation can target real artifacts.
- **Evidence:** ties to IR scopes (components, interfaces, paths) so results attach to the same objects **governance** discusses.

## How it participates in lifecycle and governance

IR changes should correlate with governed **intent** changes. Silent drift between IR and **embodiment** is a first-class STE concern: detection and response live in the control loop and **governance** parts. Compilation failures (intent inconsistent or incomplete) block or warn according to policy.

## Relationship to other artifacts

- [Architecture decision records](03-01-architecture-decision-records.md): decisions supply rationale and declaring authority; IR supplies machine-addressable representation of commitments.
- [Traceability](03-06-traceability.md): IR is the hub for many **traceability** edges.
- [Publication versus projection](03-08-publication-vs-projection.md): IR is published machine representation at the architecture model layer; diagrams are **projections**; declaring sources remain authority for normative intent.
- Part 4: [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md), [Compilation and semantic materialization](../04-architecture-model/04-04-compilation.md), [Traceability in Architecture IR](../04-architecture-model/04-05-traceability.md) for IR-centric depth.
