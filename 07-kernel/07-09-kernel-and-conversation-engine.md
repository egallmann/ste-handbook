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
- Authoring validation evaluates canonical source and regenerates discovery. It does not compile indexes into Architecture IR meaning and does not construct an exact source basis (see [Compilation](../04-architecture-model/04-04-compilation.md)).
- **Kernel** evaluates compiled inputs and **Evidence**, returning **Query** / **Explain** / **Coverage** / **Admission** results.

### Implementation posture

Posture is stated once in [Kernel responsibilities](07-03-kernel-responsibilities.md). Conversation may elicit intent. It does not admit. A stable handoff from elicitation into the decision role remains part of the role’s design. It is not the current supported authoring seam.

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
