---
title: "Why the Kernel exists"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# Why the Kernel exists

## The Problem

Software organizations routinely lose the thread between **decisions**, declared structure, and what is observed in **embodiment**. Informal reasoning fills the gap: meetings, chats, and tacit senior-engineer judgment. That mode scales poorly and produces **lossy reasoning**—the same facts support incompatible stories, and automation cannot tell which story is binding.

## The Reframe

STE treats architecture as a maintained object: **intent** compiles to **Architecture IR**, **Evidence** observes **embodiment**, and **governance** closes the loop. A dedicated **Kernel role** exists so that **evaluation**—whether structure is complete, traceable, supported by **Evidence**, and safe to change—is not re-implemented differently in every tool, agent, or CI script.

The Kernel role is the **deterministic** counterpart to stochastic assistance. Assistants may draft; humans may judge narrative tradeoffs; the Kernel role answers whether, under declared rules, a **change proposal** is **admissible** and whether the model is **covered** and **explained** to the depth policy requires.

## The Model

Separating **authorship** from **evaluation** yields three structural benefits:

1. **Accountability:** Decisions attach to **intent** artifacts and **Architecture IR** identities, not to ephemeral chat state.
2. **Repeatability:** The same **Architecture IR**, **Evidence**, and **change proposal** yield the same **deterministic decision** when policy is fixed.
3. **Automation safety:** Downstream systems act on **machine-readable** outcomes (**Admission**, coverage reports, explanation graphs) instead of re-parsing prose.

The Kernel role does not remove human **governance**; it makes the mechanical prelude to **governance** honest and inspectable.

## The Implications

- If a workflow needs “is this allowed?” answers, route them through **Admission** semantics rather than informal approval only.
- If a workflow needs “what is missing?” answers, treat **Coverage** as a first-class output of the architecture reasoning system.

## Relationship to STE system

- Foundations: [The problem of lossy reasoning](../00-problem/00-02-the-problem-of-lossy-reasoning.md), [Deterministic versus stochastic systems](../00-problem/00-06-deterministic-vs-stochastic-systems.md).
- System story: [System overview](../02-overview/02-03-system-overview.md), [The STE lifecycle](../02-overview/02-04-the-ste-lifecycle.md).
- Role definition: [What is the Kernel?](07-01-what-is-the-kernel.md).

## Summary

- The **Kernel role** exists to make **evaluation** of **Architecture IR** and **Evidence** **deterministic**, **traceable**, and **machine-readable**.
- It addresses **lossy reasoning** by centralizing mechanical decisions that must not be re-derived ad hoc in every tool.
- It complements human **governance**; it does not replace accountable judgment on ambiguous tradeoffs.
