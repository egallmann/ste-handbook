---
title: "Kernel responsibilities"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel responsibilities

## The Problem

Without an explicit responsibility list, teams assign “kernel work” to compilers, CI jobs, agents, or dashboards interchangeably. That diffusion breaks **fail-closed** behavior and makes **Admission** semantics unclear.

## The Reframe

This table states what the **Kernel role** is responsible for at the STE model level. **Implemented** rows reflect capabilities that exist in the reference integration path today; **Planned** rows name obligations the architecture expects to deepen over time. Exact mechanics remain in **ste-spec** and implementing components.

**Maturity note:** For this chapter, treat **Implemented** as **L2** (defined and present in reference integrations but still evolving) and **Planned** as **L1** (concept and contract direction without full product coverage).

## The Model

| Responsibility | Description | Status |
|----------------|-------------|--------|
| Load **Architecture IR** | Consume the unified architecture model inputs required for evaluation (including the validated **Compiled IR Document** per **ste-spec**). | Implemented |
| Load **Evidence** | Consume **Evidence** inputs (including **ArchitectureEvidence**-shaped payloads) for assessment contexts. | Implemented |
| Query architecture | Answer what exists: components, decisions, capabilities, **invariants**, and related entities as modeled in **Architecture IR**. | Implemented |
| Explain architecture | Answer why it exists: trace edges from structure to **intent**, rules, and supporting **Evidence**. | Implemented |
| Coverage analysis | Identify missing or weakly governed architecture: gaps, orphans, missing **Evidence**, unconstrained elements. | Implemented |
| **Admission** control | Evaluate **change proposals** under declared constraints; emit **Admission** outcomes (**KernelAdmissionAssessment** where **ste-spec** applies). | Implemented |
| **Governance** enforcement | Apply **governance rules** as mechanical obligations beyond core **IR validation** (policy-shaped outcomes). | Planned |
| **Lifecycle** evaluation | Evaluate architecture state across **lifecycle** transitions and time-sliced expectations. | Planned |
| Drift detection | Classify sustained mismatch between declared **Architecture IR** and **Evidence** about **embodiment** (feeds **governance** narratives). | Planned |
| **Conversation Engine** interface | Support structured handoffs so elicited **intent** can be evaluated consistently (without making conversation the decision core). | Planned |
| IDE integration | Support development tooling consuming the same **deterministic decisions** as CI. | Planned |

**IR validation** (mechanical validation of **Architecture IR** / **Compiled IR Document** under **ste-spec**) is part of the integration path that prepares inputs for **Admission** evaluation; it is not the same activity as **Admission** itself.

## The Implications

- **Planned** rows are roadmap truth for the handbook, not promises about a single release.
- Product prioritization may implement **Planned** rows in different order; **ste-spec** governs interchange when those capabilities land.

## Relationship to STE system

- Overview: [Kernel overview](07-00-overview.md).
- Determinism: [Determinism and fail-closed](07-06-determinism-and-fail-closed.md).
- Adjacent roles: [Kernel and governance](07-07-kernel-and-governance.md), [Kernel and runtime](07-08-kernel-and-runtime.md).

## Summary

- The **Kernel role** loads **Architecture IR** and **Evidence**, answers **Query** / **Explain** / **Coverage**, and performs **Admission**.
- **Governance** enforcement, **lifecycle** evaluation, drift, conversation, and IDE integrations are **Planned** expansions of the same role model.
