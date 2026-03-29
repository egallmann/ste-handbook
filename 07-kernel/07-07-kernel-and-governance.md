---
title: "Kernel and governance"
status: draft
maturity: L1
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel and governance

## The Problem

**Governance** assigns ownership, exceptions, and authorized change over time. If the **Kernel role** is misread as “the governance system,” teams abdicate human accountability; if it is isolated from **governance**, assessments never change what organizations may build.

## The Reframe

The **Kernel role** supplies **deterministic decisions** and structured findings (**Query**, **Explain**, **Coverage**, **Admission**). **Governance** decides what those findings mean for policy: merges, waivers, remediation plans, and updates to **intent**. The Kernel role informs **governance**; it does not replace accountable judgment on ambiguous tradeoffs.

## The Model

### Intended interaction

- **Kernel** emits **machine-readable** outcomes (including **KernelAdmissionAssessment** for **Admission** where **ste-spec** applies).
- **Governance** consumes outcomes within the control loop: [Assessment to decision](../06-governance/06-12-assessment-to-decision.md), [Decision to change](../06-governance/06-13-decision-to-change.md), [Governance](../06-governance/06-06-governance.md).

### Capability posture (honest snapshot)

| Capability | Current | Planned |
|------------|---------|---------|
| **Governance** enforcement | No | Yes |
| **Lifecycle** evaluation | No | Yes |
| Runtime compliance | Partial | Yes |
| IDE integration | No | Yes |
| **Conversation Engine** interface | No | Yes |
| Control plane | Emerging | Yes |

**Emphasis (this section):** **Governance** enforcement rows are **Planned** mechanical depth; today, **governance** processes often interpret Kernel-style outputs outside a single unified enforcement plane.

## The Implications

- Design policy so **Admission** outcomes map cleanly to **governance** actions (block, exception with owner, required follow-up **Evidence**).
- Keep **ste-spec** as the shared contract between **Kernel** outputs and **governance** automation.

## Relationship to STE system

- [Control loop overview](../06-governance/06-07-control-loop-overview.md)
- [Drift](../06-governance/06-03-drift.md)
- [Kernel overview](07-00-overview.md)

## Summary

- The **Kernel role** produces structured assessments; **governance** authorizes change.
- Deep mechanical **governance** enforcement through the Kernel plane is **Planned**; the handbook snapshot above states current versus intended coverage.
