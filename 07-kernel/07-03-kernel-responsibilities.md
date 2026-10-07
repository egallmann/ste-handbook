---
title: "Kernel responsibilities"
status: draft
maturity: L2
last_reviewed: "2026-10-06"
diagrams: no
---

# Kernel responsibilities

## The Problem

Without an explicit responsibility list, teams assign “kernel work” to compilers, CI jobs, agents, or dashboards interchangeably. That diffusion breaks **fail-closed** behavior and makes **Admission** semantics unclear.

## The Reframe

This chapter states what the **Kernel role** must guarantee when a supported producer provides it. It does not describe the authoring kit, and it does not treat an older reference snapshot as the current integration seam.

When a supported producer provides the role, the guarantees are: the same inputs yield the same outcome; evidence is not a verdict until evaluated; IR validation is not admission.

## The Model

There is no current supported/public admission producer in this path. The authoring kit does not produce admission decisions. The reference/public path should not be treated as the current integration seam.

Kernel admission is a **reserved / logical architectural role**. Query, Explain, Coverage, and Admission name that role. They are not implemented product behavior on the current supported/public path. Named payloads such as **ArchitectureEvidence** and **KernelAdmissionAssessment** are handbook models ahead of the active supported producer. Do not build the authoring integration against them as if they were the live seam.

A discovery bundle (index and manifest) is an authoring projection. A separate integration might load it. Loading it is not a decision and not semantic interpretation.

**IR validation** and **Admission** remain different obligations inside the role. Conflating them, or conflating either with authoring validation, is a false equivalence.

The repeated posture tables that used to appear in the adjacency chapters point here. They are not a second status catalogue.

## The Implications

- The role stays. The older “Implemented” snapshot does not.
- **ste-spec** governs interchange when a supported producer exists. This chapter does not invent that producer.

## Relationship to STE system

- Overview: [Kernel overview](07-00-overview.md).
- Determinism: [Determinism and fail-closed](07-06-determinism-and-fail-closed.md).
- Adjacent roles: [Kernel and governance](07-07-kernel-and-governance.md), [Kernel and runtime](07-08-kernel-and-runtime.md).

## Summary

- The **Kernel role** is reserved on this path: Query, Explain, Coverage, and Admission describe what a supported producer must do, not what the authoring kit does now.
- There is no current supported/public admission producer in this path. The authoring kit does not produce admission decisions.
