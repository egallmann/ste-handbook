---
title: "Kernel as control plane"
status: draft
maturity: L1
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel as control plane

## The Problem

Without a control plane, STE fragments into disconnected validators, each with its own semantics. A **control plane** centralizes **deterministic decisions** so **governance**, CI, and authoring tools coordinate on one architectural truth.

## The Reframe

The **Kernel role** is STE’s emerging **control plane**: the locus where **Architecture IR**, **Evidence**, and policy meet before the organization acts. This is directional—**control plane** maturity is **Emerging** relative to the full vision—but the architectural intent is stable: one integration contracts with **ste-spec**, many consumers execute outcomes.

## The Model

### What “control plane” means here

- **Single decision semantics** for **Admission** and related mechanical outcomes (**KernelAdmissionAssessment** where defined).
- **Repeatable** evaluation keyed to **Compiled IR Document** identity and validated **Evidence** inputs.
- **Composable** enforcement: CI, IDE, and **governance** workflows attach to the same outputs.

### Implementation posture

Posture is stated once in [Kernel responsibilities](07-03-kernel-responsibilities.md). A control plane is the direction of the reserved decision role. It is not the current supported/public integration seam. The discovery bundle an integration might load is authoring discovery, not interpreted meaning and not admission.

### Normative pointers

Conceptual framing for IR-mediated evolution and integration authority appears in **ste-spec** and related logical decision records; this handbook does not duplicate mechanical contracts.

## The Implications

- Keep Architecture IR semantics in **ste-spec**. Do not multiply bespoke checks that treat discovery indexes or handbook admission payloads as the current integration center.
- Treat **IR validation** and **Admission** as foundational stages in any control-plane story.

## Relationship to STE system

- [Kernel overview](07-00-overview.md)
- [Kernel and governance](07-07-kernel-and-governance.md)
- [Kernel and developer tooling](07-10-kernel-and-developer-tooling.md)

## Summary

- The **Kernel role** is STE’s **control plane** in intent: **deterministic decisions** consumed across tooling and **governance**.
- The role remains. There is no current supported/public admission producer in this path. The authoring kit does not produce admission decisions.
