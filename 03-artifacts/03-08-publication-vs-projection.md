---
title: "Publication versus Projection"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Publication versus Projection

**Artifact type:** **Publication** (canonical, binding records) versus **projection** (derived human-facing representations).  
**Role in STE:** Separate governed **published state** from regenerable views so **traceability** and review anchor on identifiers in the graph.  
**Primary concern:** governance (how truth is published and surfaced); secondary: structural views rendered from IR.  
**Connects to:** **Architecture IR**, intent records, **evidence** summaries, Part 4 **projection** practice.

## The Problem this artifact solves

Diagrams and exported narratives multiply until each stakeholder has a favorite truth. Review happens on presentation surfaces while builds use repos, and nobody notices they diverged. STE separates **publication** (what is binding and versioned in the artifact system) from **projection** (derived human-facing output). Without that split, **governance** debates the wrong objects and **traceability** breaks the first time someone edits a static image without updating the model.

## What the artifact is

**Publication** means committing normative or canonical material through STE’s governed paths: **intent** records, compiled **Architecture IR**, published rules, and other inputs **ste-spec** treats as authoritative. **Projection** means rendering derived views from that material: diagrams, narrative **projection** outputs, tables, and stakeholder-specific summaries.

A projection may simplify or highlight; it must not silently contradict published truth. If it does, the bug is in the renderer, the data, or the **governance** of what was published.

## How it is used in STE

People **approve** changes to **published** records under **governance**; STE **regenerates** **projections** from IR and linked sources. Readers consume projections for speed; auditors and automation follow publication identifiers. When a projection looks wrong, the fix is usually in IR or **intent**, not in hand-editing the rendered view.

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
- Part 4: [Projections overview](../04-architecture-model/04-08-projections-overview.md), [Diagrams](../04-architecture-model/04-10-diagrams.md), [View consistency](../04-architecture-model/04-14-view-consistency.md).

Part 3 states the distinction; Part 4 develops **projection** practice and risks.
