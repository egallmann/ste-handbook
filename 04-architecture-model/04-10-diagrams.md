---
title: "Diagrams"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Diagrams

## The Problem

Diagrams are the most seductive **projection** because they look like “the architecture.” In STE, a diagram is **authoritative** only insofar as it **faithfully renders** **Architecture IR** for a chosen slice and notation. When diagrams lead IR, **drift** is guaranteed: the picture wins meetings, the graph lags, **evidence** attaches to the wrong **scope**.

## The Reframe

Treat every architecture diagram in STE’s world as a **diagram projection**: boxes and lines **stand for** IR **entities** and **relationships**. Manual drawing is allowed as **authoring** if the result **round-trips** into IR through **compilation** or equivalent **governance**—otherwise it is informal sketching, explicitly not **canonical**.

## The Model

### Notation and mapping

Boxes map to **entity** identities; arrows map to **relationship** types. Legend and notation guide should declare the mapping so reviewers can check **semantics**, not only aesthetics. Ambiguous arrows (“connects to”) collapse distinct edge types and hide **constraints**.

### Levels and zoom

Layered notations (context, container, component, code in C4-like styles) are **filters** on the same IR, not separate models. Zoom changes **detail density**, not **truth**.

### Drift detection

Compare diagram exports to IR **diff** when feasible: unexpected visual changes without IR delta signal pipeline failure or manual tampering. **View consistency** practices extend this idea across multiple projections ([View consistency](04-14-view-consistency.md)).

### Accessibility and review

Diagrams help **humans**; **accessibility** (textual alternates, structured summaries) keeps **governed reasoning** inclusive and supports **agents** that consume text-first **projection** channels.

## The Implications

In reviews, ask: **which IR version** does this diagram represent, and **what slice**? If the answer is unknown, the diagram is **not** a **governance**-grade **artifact**—it may still be useful ideation, but it must not decide **conformance**.

## Relationship to STE system

- **Projection framing:** [Projections overview](04-08-projections-overview.md), [Projections](04-09-projections.md).
- **Views:** [Architecture views](04-12-architecture-views.md), [Stakeholder views](04-13-stakeholder-views.md).
- **Lossy reasoning:** [The problem of lossy reasoning](../00-problem/00-02-the-problem-of-lossy-reasoning.md).

## Summary

- Diagrams are **projections** of **Architecture IR**, not parallel sources of structural truth.
- **Notation** must preserve **entity** and **relationship** semantics.
- **Provenance** and **diff** alignment keep diagrams **accountable**.

**Next:** [Projection documents](04-11-projection-documents.md).
