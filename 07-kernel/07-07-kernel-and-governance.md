---
title: "Kernel and governance"
status: draft
maturity: L1
last_reviewed: "2026-10-06"
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
- **Governance** consumes outcomes within the control loop: [Authority and decision rights](../06-governance/06-03-authority-and-decision-rights.md), [Steelman, obligations, and change control](../06-governance/06-05-steelman-obligations-and-change-control.md), [Section overview (Part 6)](../06-governance/06-00-section-overview.md).

### Implementation posture

Posture for this role is stated once in [Kernel responsibilities](07-03-kernel-responsibilities.md). There is no current supported/public admission producer in this path. The authoring kit does not produce admission decisions. The reference/public path should not be treated as the current integration seam. Governance still owns authorization. The kernel role informs that authorization when a supported producer exists. It does not replace judgment.

## The Implications

- Design policy so **Admission** outcomes map cleanly to **governance** actions (block, exception with owner, required follow-up **Evidence**).
- Keep **ste-spec** as the shared contract between **Kernel** outputs and **governance** automation.

## Relationship to STE system

- [The governance model](../06-governance/06-02-the-governance-model.md)
- [Authority and decision rights](../06-governance/06-03-authority-and-decision-rights.md)
- [Admission, eligibility, and enforcement](../06-governance/06-04-admission-eligibility-and-enforcement.md)
- [Kernel overview](07-00-overview.md)

## Summary

- The **Kernel role** produces structured assessments; **governance** authorizes change.
- Deep mechanical governance enforcement is not the current supported authoring seam. The role remains. See [Kernel responsibilities](07-03-kernel-responsibilities.md).
