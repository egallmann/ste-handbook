---
title: "Kernel inputs and outputs"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel inputs and outputs

## The Problem

Integration failures often come from unclear handoffs: teams treat logs, markdown, or ad hoc JSON as if they were **Architecture IR** or **KernelAdmissionAssessment**. Without a disciplined I/O story, **deterministic decisions** are impossible to rely on.

## The Reframe

Treat the **Kernel role** as a **pure decision system** at the model level:

**Inputs → evaluation → deterministic outputs.**

All inputs must be **contract-shaped** where **ste-spec** defines contracts. **Evidence**, including **ArchitectureEvidence**, remains **non-decision-bearing** until the Kernel role evaluates it in context.

## The Model

### Inputs

| Input | Role in evaluation |
|-------|---------------------|
| **Architecture IR** | Declared structural model and identities the Kernel role traverses for **Query**, **Explain**, and **Coverage**. |
| **Compiled IR Document** | Validated merge artifact per **ste-spec**; the integration-state input prepared after **IR validation**. |
| **Evidence** | Observations about **embodiment** and tooling health, including **ArchitectureEvidence** where applicable. |
| **Change proposal** | A declared delta or request evaluated under **Admission** rules. |
| **Governance rules** | Policy inputs that constrain what may pass **Admission** and how **Coverage** is interpreted. |
| **Lifecycle state** | Context for time-sliced expectations (what “current” means for a scope). |

### Outputs

| Output | What it represents |
|--------|-------------------|
| Query results | Structured answers to “what exists” questions over **Architecture IR**. |
| Explanation graph | Trace structures linking entities to **intent**, rules, and **Evidence**. |
| Coverage report | Structured account of gaps, orphans, missing **Evidence**, and weak governance attachment. |
| **Admission** decision | Allow / deny (and related semantics) for a **change proposal**; **KernelAdmissionAssessment** where **ste-spec** defines that payload. |
| **Governance** violations | Findings that map rule breaches to **Architecture IR** identities and **Evidence** references (where rule evaluation is in scope). |
| **Lifecycle** status | Summaries of architecture state against **lifecycle** expectations (as this capability matures). |

### IR validation versus Admission

- **IR validation** checks mechanical rules on **Architecture IR** and the **Compiled IR Document** (shape, provenance, contract constraints).
- **Admission** evaluates eligibility and blocking semantics for progress or change, emitting **KernelAdmissionAssessment** at the defined boundary.

They are sequential concerns in the integration story: invalid IR cannot silently become admissible.

## The Implications

- Pipelines should preserve input identity and versioning so **deterministic decision** claims remain meaningful.
- Consumers should treat **KernelAdmissionAssessment** as authoritative for **Admission** at the handoff, not reinterpret parallel channels.

## Relationship to STE system

- Reasoning operations: [Kernel reasoning surface](07-05-kernel-reasoning-surface.md).
- **Evidence** artifact layer: [Evidence](../03-artifacts/03-05-evidence.md).
- **Runtime** role: [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md), [Runtime–Kernel contract](../08-runtime/08-06-runtime-kernel-contract.md).

## Summary

- Kernel evaluation is **input → evaluation → output** with contracts from **ste-spec**.
- **ArchitectureEvidence** is **non-decision-bearing** until evaluated; **KernelAdmissionAssessment** is decision-bearing for **Admission**.
- **IR validation** prepares or guards inputs; **Admission** answers whether change may proceed.
