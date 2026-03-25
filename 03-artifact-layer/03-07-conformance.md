---
title: "Conformance"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Conformance

## The Problem this artifact solves

Teams argue in circles about whether the system “meets requirements” because nobody defines what would count as proof. **Conformance** in STE names a **claim**: stated **intent** (including **invariants** and **constraints**) is satisfied by **embodiment** for declared scopes, supported by **evidence** and interpreted under rules. Without that structure, “passing CI” is mood, not engineering.

## What the artifact is

A **conformance** posture in STE combines normative **intent**, canonical **Architecture IR**, **evidence** records, and assessment rules (often executed or orchestrated by **Kernel**-shaped components). The **artifact layer** contribution is the **claim** and its linkage: which obligations, which scopes, which **evidence**, which outcomes.

This chapter is not the full admission algorithm. It names the object you defend in review: “we conform” means a structured story others can inspect.

## How it is used in STE

**Governance** and release processes ask for **conformance** summaries tied to versioned **intent** and IR. Developers use the same vocabulary while coding: a failing check is a challenged **conformance** claim, not a personal slight. **Drift** appears when **conformance** was once supported but **evidence** or **embodiment** moved without updating **intent** or scopes.

**Example:** A release candidate must show green contract tests and policy scans for all services on the payment boundary. The **conformance** bundle lists obligation IDs, IR scopes, and **evidence** record IDs. A missing link blocks ship until fixed or waived under policy.

## How it relates to intent, implementation, or evidence

- **Intent:** defines obligations.
- **Implementation:** **embodiment** must realize them.
- **Evidence:** supports the claim; without **evidence**, **conformance** is assertion only.

## How it participates in lifecycle and governance

Waiving **conformance** for a scope or window is a **governance** act: owner, rationale, and often re-evaluation date. Persistent failure triggers **governance** choices: fix **embodiment**, revise **intent**, or stop claiming **conformance** where it no longer holds.

## Relationship to other artifacts

- [Evidence](03-05-evidence.md): **conformance** without **evidence** is hollow.
- [Traceability](03-06-traceability.md): links obligations to checks and scopes.
- [Invariants](03-03-invariants.md) and [Requirements and constraints](03-02-requirements-and-constraints.md): common obligation sources.
- Part 5: [Conformance](../05-kernel/05-07-conformance.md), [Validation](../05-kernel/05-03-validation.md), [The admission model](../05-kernel/05-02-the-admission-model.md) for kernel-oriented depth.

Part 3 frames **conformance** as an artifact-layer claim; Part 5 frames how assessment produces outcomes.
