---
title: "Kernel and conversation engine"
status: draft
maturity: L1
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel and conversation engine

## The Problem

Conversational tools excel at **elicitation** and synthesis; the **Kernel role** excels at **deterministic evaluation**. If conversations pretend to be **Admission**, organizations lose **fail-closed** guarantees. If the Kernel ignores conversational outputs entirely, structured **intent** never benefits from modern authoring interfaces.

## The Reframe

The **Conversation Engine** (handbook Part 9 — Human interface) lives at the boundary where humans and assistants shape **intent**. Its job is to produce reviewable **artifacts** and structured proposals compatible with compilation into **Architecture IR**. The **Kernel role** evaluates those artifacts and proposals—it does not “chat,” and it does not replace human **governance**.

## The Model

### Intended interaction

- Conversation produces and refines **intent** records and **change proposals**.
- Compilation pipelines produce **Architecture IR** inputs (see [Compilation](../04-architecture-model/04-04-compilation.md)).
- **Kernel** evaluates compiled inputs and **Evidence**, returning **Query** / **Explain** / **Coverage** / **Admission** results.

### Capability posture (honest snapshot)

| Capability | Current | Planned |
|------------|---------|---------|
| **Governance** enforcement | No | Yes |
| **Lifecycle** evaluation | No | Yes |
| Runtime compliance | Partial | Yes |
| IDE integration | No | Yes |
| **Conversation Engine** interface | No | Yes |
| Control plane | Emerging | Yes |

**Emphasis (this section):** A first-class **Conversation Engine** interface to the **Kernel role**—stable handoffs from elicitation to evaluation—is **Planned**.

## The Implications

- Assistants may draft; only **ste-spec**-backed evaluation paths should gate **Admission**.
- UX should show **Kernel** outcomes as structured decisions, separate from conversational narrative.

## Relationship to STE system

- [Human interface overview](../09-human-interface/09-00-conversation-engine-overview.md)
- [Conversation interface](../09-human-interface/09-01-conversation-interface.md)
- [Kernel reasoning surface](07-05-kernel-reasoning-surface.md)

## Summary

- **Conversation Engine** elicits **intent**; **Kernel** evaluates compiled **Architecture IR** and **Evidence**.
- Tight integration between conversation flows and **Kernel** evaluation is **Planned**; the role split is stable today.
