---
title: "Kernel and runtime"
status: draft
maturity: L1
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel and runtime

## The Problem

**Runtime** tooling observes **embodiment** and tooling health; the **Kernel role** evaluates declarations against those observations. Blurring the two produces either “the build is the architecture” or “the architecture ignores reality.”

## The Reframe

The **Runtime** role produces **Evidence**, including **ArchitectureEvidence**-shaped payloads defined in **ste-spec**. That **Evidence** is **non-decision-bearing** until the **Kernel role** evaluates it alongside **Architecture IR** and policy. **Admission** (**KernelAdmissionAssessment**) is emitted only from the Kernel side of the boundary, not from **Runtime**.

## The Model

### Intended interaction

- **Runtime** gathers observations (freshness, diagnostics, reconciliation signals) into **Evidence** records.
- **Kernel** loads **Evidence**, runs **Query** / **Explain** / **Coverage** / **Admission** as scoped, and emits **deterministic decisions**.

### Capability posture (honest snapshot)

| Capability | Current | Planned |
|------------|---------|---------|
| **Governance** enforcement | No | Yes |
| **Lifecycle** evaluation | No | Yes |
| Runtime compliance | Partial | Yes |
| IDE integration | No | Yes |
| **Conversation Engine** interface | No | Yes |
| Control plane | Emerging | Yes |

**Emphasis (this section):** **Runtime compliance** is **Partial** today—**Evidence** paths exist, but uniform policy interpretation across workspaces remains uneven.

## The Implications

- Treat **ArchitectureEvidence** as an input contract, not a verdict.
- Align **RECON** and related runtime narratives with **Evidence** handoffs described in **ste-spec**.

## Relationship to STE system

- [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md), [Runtime–Kernel Contract](../08-runtime/08-06-runtime-kernel-contract.md), [Runtime Architecture Components and Flow](../08-runtime/08-09-runtime-architecture-components-and-flow.md)
- [Evidence](../03-artifacts/03-05-evidence.md)
- [Kernel inputs and outputs](07-04-kernel-inputs-and-outputs.md)

## Summary

- **Runtime** observes; **Kernel** decides.
- **Evidence** is **non-decision-bearing** at the handoff; **KernelAdmissionAssessment** carries **Admission** decisions where defined.
- End-to-end **Runtime compliance** evaluation is **Planned** maturity relative to the full STE story.
