---
title: "Kernel and developer tooling"
status: draft
maturity: L1
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel and developer tooling

## The Problem

Developers experience STE through editors, local checks, and CI. If those surfaces reinvent **Admission** semantics, every integration diverges. If they ignore **Kernel** outcomes, **deterministic decisions** never reach the keyboard.

## The Reframe

CLI, IDE, and CI channels are **consumers** of **Kernel role** outputs: the same **machine-readable** artifacts should drive pre-commit feedback, merge gates, and dashboards. The **Kernel role** remains implementation-agnostic; developer tooling is responsible for presenting outcomes and collecting **change proposals** compatible with evaluation.

## The Model

### Intended interaction

- Local and remote automation requests **Query** / **Explain** / **Coverage** / **Admission** results from the integration plane.
- Editors assist authors but treat **KernelAdmissionAssessment** (where applicable) as authoritative for **Admission** at the gate.

### Capability posture (honest snapshot)

| Capability | Current | Planned |
|------------|---------|---------|
| **Governance** enforcement | No | Yes |
| **Lifecycle** evaluation | No | Yes |
| Runtime compliance | Partial | Yes |
| IDE integration | No | Yes |
| **Conversation Engine** interface | No | Yes |
| Control plane | Emerging | Yes |

**Emphasis (this section):** **IDE integration** that surfaces **Kernel** decisions uniformly is **Planned**; many workflows today rely on partial or manual bridges.

## The Implications

- Prefer one decision source for **Admission** across local and CI environments.
- Surface **Coverage** and **Explain** outputs early to reduce late gate surprises.

## Relationship to STE system

- [System overview](../02-overview/02-03-system-overview.md)
- [Conformance and assessment](../05-lifecycle/05-05-conformance-and-assessment.md)
- [Determinism and fail-closed](07-06-determinism-and-fail-closed.md)

## Summary

- Developer tooling should **execute and enforce** **Kernel** outcomes, not reinterpret them.
- Rich **IDE integration** is **Planned** maturity alongside a stronger control plane.
