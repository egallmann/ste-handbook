---
title: "Part 2: STE Overview"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# Part 2: STE Overview

## The Problem

Parts 0 and 1 did different jobs. Foundations named the dysfunction, the thesis, and the vocabulary precursors. Theoretical foundations showed why multiple disciplines touch the same lifecycle failure modes. What you may still lack is a single picture of STE as a system you can point at: the major objects, how they connect, and how later parts of the book unpack each layer.

Without that picture, it is easy to read later chapters as a grab bag: intent here, kernel there, projections elsewhere. The risk is not ignorance of individual terms. The risk is never seeing the whole shape clearly enough to navigate.

## The Reframe

Part 2 is the bridge from argument to architecture. It is orientation, not completion. The goal is a reader who can sketch STE on a whiteboard, use core words without constant reinterpretation, and read Parts 3 onward with a stable mental model of where each layer sits.

Think of Part 2 as installing a map before you hike the terrain.

## The Model

### What Part 2 contains

Part 2 is four chapters after this one, each with a narrow job:

1. **[What is STE?](02-01-what-is-ste.md)** gives a handbook-level definition, scope, non-goals, and the boundary between this book and **ste-spec**. It answers “what kind of thing is STE?” in language you can repeat accurately.
2. **[Terminology](02-02-terminology.md)** stabilizes vocabulary by role in the loop, not as a flat glossary. It exists so later chapters do not fight everyday English.
3. **[System overview](02-03-system-overview.md)** is the first end-to-end structural story: intent capture, canonical model, evidence, assessment, governance feedback, and where humans and agents participate.
4. **[The STE lifecycle](02-04-the-ste-lifecycle.md)** frames lifecycle language as a continuous control loop, not a one-time documentation phase. It prepares you for operational detail without turning this part into a process manual.

### How later parts deepen the map (high level)

The handbook’s later parts follow the technical spine described in the repository overview: intent, Architecture IR, kernel mechanics, the control loop, projections, conversation interfaces, lifecycle and governance, examples, and advanced topics. You do not need to memorize the table. You only need the idea that each part is a layer or a loop segment, not a separate methodology.

When a later chapter names **Architecture IR**, **Kernel**, **validation**, or **governance**, you should already know which region of the map you are zooming into.

## The Implications

If you use Part 2 the way it is written, you should be able to read out of order later without losing the whole. Some readers will jump from foundations straight into intent or kernel chapters. That can work if you treat Part 2 as a repair pass whenever the story feels fragmented.

If you skip Part 2 entirely, you may still learn fragments, but you will pay a recurring tax: re-deriving structure from scattered definitions.

## Relationship to STE system

Continue into Part 2’s chapters in sequence when you can. If you need a single next step after foundations and theory, start with [What is STE?](02-01-what-is-ste.md), then [Terminology](02-02-terminology.md), then [System overview](02-03-system-overview.md), then [The STE lifecycle](02-04-the-ste-lifecycle.md).

For normative semantics, schemas, and exact system contracts, **ste-spec** remains authoritative. This handbook explains relationships and intent; it does not replace the specification.

Handy return anchors from Part 0 and Part 1:

- [The STE thesis](../00-foundations/00-08-the-ste-thesis.md)
- [What STE is and is not](../00-foundations/00-07-what-ste-is-and-is-not.md)

## Summary

- Part 2 turns thesis and theory into a navigable system shape before deep dives.
- The four chapters after this overview cover definition, vocabulary, structure, and lifecycle framing in that order.
- Later parts zoom into layers; Part 2 supplies the atlas.
- **ste-spec** defines; the handbook orients.
