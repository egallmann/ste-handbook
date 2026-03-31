---
title: "Evidence"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Evidence

**Artifact type:** **Evidence** record (including **EDR**-shaped observation with provenance).  
**Role in STE:** Capture structured observation of **embodiment** so assessment and **governance** can point at what was exercised.  
**Primary concern:** evidence.  
**Connects to:** **implementation** / **embodiment**, **Architecture IR** scopes, intent obligations, **traceability**, **conformance**.

## The Problem this artifact solves

Teams confuse “we ran tests” with “we know what we proved.” Raw logs scatter across CI vendors and dashboards without stable identity, scope, or provenance. **Evidence** artifact types exist so observations of **embodiment** are **records**: referencable, tied to what was exercised, and usable in **governance** without re-running the world.

## What the artifact is

**Evidence** in STE is structured observation of **embodiment**: test results, analysis outputs, telemetry snapshots, logs, metrics, or similar channels, captured as records (handbook sense: **EDR**-shaped) with enough metadata to interpret them later. An evidence record is not **intent**; it does not define what should be true. It records what was observed, when, where, and under which scope.

This chapter is artifact-shaped. **Kernel** mechanics for ingestion and assessment live in Part 5.

## How it is used in STE

STE **collects and structures** observations into evidence records as changes move; people interpret results and govern follow-up. Reviewers and **governance** consume summaries linked to **Architecture IR** elements and **intent** identifiers. Historical **evidence** supports audits and **drift** analysis when behavior shifts without a matching record change.

**Example:** A contract test run produces a record referencing the consumer and provider interface IDs in IR, the commit SHA, and pass or fail. A **conformance** narrative for a release cites those records instead of a screenshot of a green build.

## How it relates to intent, implementation, or evidence

- **Intent:** defines what must hold; **evidence** does not replace it.
- **Implementation:** **embodiment** is what **evidence** observes (builds, deployments, runtime).
- **Evidence:** the third leg: observation that connects **intent** to reality for assessment.

## How it participates in lifecycle and governance

Retention, access, and integrity rules for **evidence** are policy matters. **Governance** may require certain **evidence** classes before promotion or certification. Disputes (“that test does not cover the risk”) are settled by tightening scopes or adding checks, then recording the new obligation in **intent** or rules.

## Relationship to other artifacts

- [Conformance](03-07-conformance.md): **conformance** claims consume **evidence** under explicit scopes.
- [Traceability](03-06-traceability.md): links **evidence** records to IR nodes and **intent** IDs.
- [Architecture model and IR](03-04-architecture-model-and-ir.md): scopes reference canonical elements.
- Part 8: [Runtime Overview](../08-runtime/08-00-runtime-overview.md), [Evidence and Observation](../08-runtime/08-02-evidence-and-observation.md); Part 7: [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) for assessment behavior.

This chapter states what the **evidence** artifact is for at the layer level; Part 5 states how assessment uses it in the lifecycle.
