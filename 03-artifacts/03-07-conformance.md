---
title: "Conformance"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-10-06"
---

# Conformance

**Artifact type:** **Conformance** claim and recorded assessment outcomes (governance artifacts).  
**Role in STE:** State and store whether **embodiment** satisfies **intent** and **constraints** for declared scopes, grounded in **evidence** and **trace** links.  
**Primary concern:** governance (evaluated claims and recorded results).  
**Connects to:** **intent**, **Architecture IR**, **evidence**, **traceability**, assessment rules (Part 5).

## The Problem this artifact solves

Teams argue in circles about whether the system “meets requirements” because nobody defines what would count as proof. **Conformance** in STE is **evaluation of evidence against intent and constraints along trace links**: which obligations apply, which scopes, which checks ran, which **evidence** records support the outcome, under which rules. Without that structure, “passing CI” is mood, not engineering.

## What the artifact is

A **conformance** posture combines normative **intent**, canonical **Architecture IR** as representation, **evidence** records, **traceability**, and assessment rules. Recorded **conformance** results are **governance artifacts**. They **presuppose** intent records, evidence records, and **trace** edges. They are not standalone scores, and they are not the output of authoring validation.

The **artifact layer** names the claim you defend in review: “we conform” means a structured story others can inspect. Authoring validation does not establish that claim. **Admission** is the reserved Kernel decision role (Part 7), not a Part 5 algorithm and not a kit operation. Lifecycle assessment is Part 5. Observation is not a verdict.

## How it is used in STE

**Governance** and release processes ask for **conformance** summaries tied to versioned **intent** and IR. A failing check is a challenged **conformance** claim, not a personal slight. **Drift** appears when **conformance** was once supported but **evidence** or **embodiment** moved without updating **intent** or scopes.

**Example:** A release candidate must show green contract tests and policy scans for all services on the payment boundary. The **conformance** bundle lists obligation IDs, IR scopes, and **evidence** record IDs. A missing **trace** link blocks ship until fixed or waived under policy.

## How it relates to intent, implementation, or evidence

- **Intent** and **constraints** define obligations.
- **Implementation:** **embodiment** must realize them.
- **Evidence:** supports the claim; **traceability** binds evidence to obligations.

## How it participates in lifecycle and governance

Waiving **conformance** for a scope or window is a **governance** act: owner, rationale, and often re-evaluation date. Persistent failure triggers **governance** choices: fix **embodiment**, revise **intent**, or stop claiming **conformance** where it no longer holds.

## Relationship to other artifacts

- [Evidence](03-05-evidence.md): **conformance** without **evidence** is hollow.
- [Traceability](03-06-traceability.md): binds obligations to checks and scopes.
- [Invariants](03-03-invariants.md) and [Requirements and constraints](03-02-requirements-and-constraints.md): common obligation sources.
- Part 5: [Conformance and assessment](../05-lifecycle/05-05-conformance-and-assessment.md); Part 7: [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) for the decision-role questions (Query, Explain, Coverage, **Admission**). Those questions describe the role. They are not the current supported integration seam of the authoring kit.

Part 3 frames **conformance** as **governance** outcomes in the artifact system; Part 5 frames how assessment produces them.
