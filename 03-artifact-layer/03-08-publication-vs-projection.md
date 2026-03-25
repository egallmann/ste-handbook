---
title: "Publication versus Projection"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Publication versus Projection

## The Problem this artifact solves

Diagrams and documents multiply until each stakeholder has a favorite truth. Review happens on slides while builds use repos, and nobody notices they diverged. STE separates **publication** (what is binding and versioned) from **projection** (derived human views). Without that split, **governance** debates the wrong objects and **traceability** breaks the first time someone edits a PNG.

## What the artifact is

**Publication** means committing normative or canonical material through STE’s governed paths: **intent** artifacts, compiled **Architecture IR**, published rules, and other records **ste-spec** treats as authoritative inputs. **Projection** means rendering derived views from that material: diagrams, narrative docs, tables, and stakeholder-specific summaries.

A projection may simplify or highlight; it must not silently contradict published truth. If it does, the bug is in the renderer, the data, or the **governance** of what was published.

## How it is used in STE

Authors change published artifacts under review. Tooling regenerates **projections** from IR and linked sources. Readers consume projections for speed; auditors and automation follow publication identifiers. When a projection looks wrong, the fix is usually in IR or **intent**, not in hand-editing the slide.

**Example:** A C4 diagram is a **projection** from IR. Editing the diagram without updating **intent** or IR creates decorative fiction. The **governance**-correct move is to change the model, recompile, and regenerate.

## How it relates to intent, implementation, or evidence

- **Intent** and **Architecture IR** are primary **publication** targets at the design layer.
- **Embodiment** is published in repositories and infrastructure definitions; **evidence** records publish observations.
- **Projections** sit on top: they explain and persuade without replacing canonical stores.

## How it participates in lifecycle and governance

Policy can require certain **projections** for review boards, but decisions must still anchor to published records. **Governance** of **projections** is indirect: you govern sources and generation. Exceptions (hand-drawn sketches in early ideation) should be labeled as non-normative or folded back into **intent** before they drive commitments.

## Relationship to other artifacts

- [Architecture model and IR](03-04-architecture-model-and-ir.md): canonical source for many **projections**.
- [Architecture decision records](03-01-architecture-decision-records.md): published rationale; projections may summarize ADRs but do not replace them.
- [Traceability](03-06-traceability.md): links should target published IDs, not projection-only labels.
- Part 7: [Projections overview](../07-projections/07-00-projections-overview.md), [Diagrams](../07-projections/07-02-diagrams.md), [View consistency](../07-projections/07-06-view-consistency.md).

Part 3 states the distinction; Part 7 develops **projection** practice and risks.
