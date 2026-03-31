---
title: "What is the Kernel?"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# What is the Kernel?

## The Problem

Readers often map “the kernel” to a repository, a CLI, or a single runtime process. That mapping collapses **accountability**: STE needs a crisp definition of **what decides** when structured **intent**, a compiled model, and **Evidence** must be reconciled under explicit rules.

## The Reframe

In STE, the **Kernel** is a **system role**: the **decision engine** that evaluates **Architecture IR**, **Evidence**, **change proposals**, **governance rules**, and **lifecycle state**, and produces **deterministic**, **machine-readable** outcomes. It is **not** a database of record for architecture, **not** an **ADR** generator, **not** a code scanner asserted as authority over declared structure, and **not** a probabilistic assistant. It **evaluates** and **decides**.

**ste-kernel** is an implementation of that role. This chapter remains valid if that implementation changes shape, so long as contracts in **ste-spec** are honored.

**Disambiguation:** The **Invariant Kernel** (a governance concept in STE’s vocabulary) is **not** the same thing as the **Kernel role** or **ste-kernel**. When **ste-spec** uses the product name **ste-kernel**, read it as “the reference integration component,” not as the abstract role definition.

## The Model

### Kernel as evaluator, not author

The Kernel role answers structured questions against supplied inputs. It produces **decisions**, not open-ended **suggestions**. Creative elaboration, drafting, and exploratory design live at the **Conversation Engine** and human workflows; the Kernel role closes the loop with **Admission**, coverage, and traceable explanations.

### Operating objects

The Kernel role operates over:

- **Architecture IR** and the validated **Compiled IR Document** (per **ste-spec**).
- **Evidence**, including **ArchitectureEvidence**-shaped payloads from the **Runtime** role (**non-decision-bearing** until evaluated).
- **Change proposals** (declared deltas evaluated under rules).
- **Governance rules** and **lifecycle state** as policy context.

### System and repository responsibilities

| System or artifact plane | Responsibility |
|--------------------------|----------------|
| **ste-spec** | Defines contracts and schemas (including **Architecture IR**, **ArchitectureEvidence**, **KernelAdmissionAssessment**, **IR validation**, **Admission**). |
| **adr-architecture-kit** | Compiles authoring-time artifacts toward **Architecture IR** inputs; internal **ArchModel** is not the cross-repo interchange. |
| **ste-runtime** | Produces **Evidence** (for example **ArchitectureEvidence**); does **not** emit **KernelAdmissionAssessment**. |
| **Kernel role** (implemented by **ste-kernel** among possible integrations) | Evaluates merged, validated inputs and decides. |
| **Conversation Engine** | Elicits **intent** and design rationale at the human boundary ([Human interface overview](../09-human-interface/09-00-conversation-engine-overview.md)). |
| **IDE** | Authors and refactors implementation and, where permitted, structured **intent** artifacts. |
| **CI** | Enforces decisions and policy gates in the integration pipeline. |
| **Handbook** | Explains roles and reasoning; **ste-spec** is normative for mechanics. |

## The Implications

- Integration code should treat **IR validation** and **Admission** as different obligations; conflating them produces false confidence.
- Tooling should consume **Kernel** outcomes as structured artifacts, not reinterpret them in ad hoc natural language.

## Relationship to STE system

- Overview and diagrams: [Kernel overview](07-00-overview.md).
- Responsibilities and maturity: [Kernel responsibilities](07-03-kernel-responsibilities.md).
- Inputs and outputs: [Kernel inputs and outputs](07-04-kernel-inputs-and-outputs.md).
- Reasoning surface: [Kernel reasoning surface](07-05-kernel-reasoning-surface.md).

## Summary

- The **Kernel** is the **decision engine** **role**; **ste-kernel** is one implementation.
- The role **evaluates** **Architecture IR**, **Evidence**, **change proposals**, and policy context; it does **not** substitute scanning or generation for declared **intent**.
- **ste-spec** defines interchange truth; **adr-architecture-kit**, **ste-runtime**, IDE, CI, and the **Conversation Engine** occupy adjacent responsibilities.
