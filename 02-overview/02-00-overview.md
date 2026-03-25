---
title: "Part 2: STE Overview"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# Part 2: STE Overview

## The Problem

Parts 0 and 1 did different jobs. Foundations named the dysfunction, the thesis, and the vocabulary precursors. Theoretical foundations showed why multiple disciplines touch the same lifecycle failure modes. What you may still lack is a clear idea of **how to read the rest of the handbook**: what Part 2 adds, how the next few chapters sequence, and how later parts relate without memorizing a catalog.

Without that reading map, later chapters can feel like a grab bag even when they are not. The risk is not ignorance of individual ideas. The risk is never knowing which chapter to open when a term or layer confuses you.

## The Reframe

Part 2 is the bridge from argument to architecture. It is orientation, not completion. The goal is a reader who knows **which chapter answers which kind of question**, uses core words without constant reinterpretation, and reads Parts 3 onward knowing what each part is for.

Think of Part 2 as installing a map before you hike the terrain. The trail details live in later parts; Part 2 names the trailheads.

## The Model

### What Part 2 contains

Part 2 is four chapters after this one, each with a narrow job:

1. **[What is STE?](02-01-what-is-ste.md)** gives a handbook-level definition, scope, non-goals, and the boundary between this book and **ste-spec**. It answers “what kind of thing is STE?” in language you can repeat accurately.
2. **[Terminology](02-02-terminology.md)** stabilizes vocabulary by role in the loop, not as a flat glossary. It exists so later chapters do not fight everyday English.
3. **[System overview](02-03-system-overview.md)** is the first end-to-end structural story: intent capture, canonical model, evidence, assessment, governance feedback, and where humans and agents participate.
4. **[The STE lifecycle](02-04-the-ste-lifecycle.md)** frames lifecycle language as a continuous control loop, not a one-time documentation phase. It prepares you for operational detail without turning this part into a process manual.

### How later parts deepen the map (high level)

The handbook’s later parts follow the technical spine described in the repository overview: intent, Architecture IR, kernel mechanics, the control loop, projections, conversation interfaces, lifecycle and governance, examples, and advanced topics. You do not need to memorize the table. You only need the idea that each part is a layer or a loop segment, not a separate methodology.

When a later chapter title names intent, IR, kernel, validation, or governance, treat it as a signpost: you are zooming into one region of the same story.

## The Implications

If you use Part 2 the way it is written, you should be able to read out of order later without losing the whole. Some readers will jump from foundations straight into intent or kernel chapters. That can work if you treat Part 2 as a repair pass whenever the story feels fragmented.

If you skip Part 2 entirely, you may still learn fragments, but you will pay a recurring tax: re-deriving where each kind of explanation lives.

## Relationship to STE system

Continue into Part 2’s chapters in sequence when you can. If you need a single next step after foundations and theory, start with [What is STE?](02-01-what-is-ste.md), then [Terminology](02-02-terminology.md), then [System overview](02-03-system-overview.md), then [The STE lifecycle](02-04-the-ste-lifecycle.md).

For normative semantics, schemas, and exact system contracts, **ste-spec** remains authoritative. This handbook explains relationships and intent; it does not replace the specification.

Handy return anchors from Part 0 and Part 1:

- [The STE thesis](../00-foundations/00-08-the-ste-thesis.md)
- [What STE is and is not](../00-foundations/00-07-what-ste-is-and-is-not.md)

**Next:** Open [What is STE?](02-01-what-is-ste.md) next. It states STE in handbook terms and draws the line between this book and **ste-spec**. The chapters that follow add shared vocabulary, a structural picture, and a time-shaped loop. None of them replace that first definition job.

## Summary

- Part 2 supplies a **reading map** and sequence before deep dives: definition, vocabulary, structure, lifecycle.
- The four chapters after this overview cover those jobs in that order.
- Later parts zoom into layers; Part 2 tells you **which layer** each part is about.
- **ste-spec** defines; the handbook orients.
