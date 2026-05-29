---
title: "Projections"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-05-29"
---

# Projections

## The Problem

“Generate documentation from the code” and “keep the diagram updated” are slogans without a **source of truth**. **Projections** fail when nobody defines **what** they project from, **how** selection works, or **when** regeneration happens. STE names **Architecture IR** as the structural **source** so **projections** become repeatable **views**, not one-off exports.

## The Reframe

[Projections overview](04-08-projections-overview.md) states the policy: IR is **canonical**, projections are **derived**. Here, treat a **projection** as a **projection function**: inputs include an IR snapshot (and configuration: layout, filters, notation), outputs include human-consumable artifacts (SVG, PDF, HTML, slides). The function should be **versioned** or **reproducible** so “what we reviewed” is answerable. This chapter stays conceptual; toolchains live outside the handbook.

## The Model

### Selection and filtering

Projections **slice** the graph: by **scope**, by type (only data stores), by criticality, by team ownership. Filtering is not neutral—it encodes **stakeholder** questions. Those questions should be **named** so **governance** knows which projection supports which **decision**.

### Layout and notation

Layout is **presentation**; semantics ride on IR identities and edges. Changing layout should not change meaning. Notation mappings (C4 levels, UML profiles) are **conventions** teams adopt; STE cares that elements **map** to IR nodes and edges **deterministically**.

### Freshness and provenance

A projection should carry **provenance**: which IR version, which projection spec, when generated. Reviewers use provenance the same way they use artifact digests for **evidence**—to know **what** was on the table in a **governance** event.

Richer metadata improves accountability but does not change authority. A
projection may include source references, traceability links, freshness labels,
or compression rationale. Those fields help readers follow the projection back
to its source graph and owning artifacts; they do not make the projection an
ADR, **Architecture IR**, **ArchitectureEvidence**, or a **Kernel** outcome.

### Multi-resolution projections

Some projection pipelines need more than one level of detail from the same
graph substrate. A system-context view, a service topology, a capability-domain
view, and a full machine-facing graph may all be legitimate projections of the
same underlying state.

In STE, this is not a license to hand-write competing diagrams. A
multi-resolution projection is still a **projection function**: the level is an
explicit input, and the output remains **derived**. Lower-resolution views
compress detail for human cognition; higher-resolution views preserve detail for
inspection, traceability, and machine consumption. The discipline is that
compressed nodes and edges must remain traceable back to their source graph
material.

STE recognizes two projection lineages that share that discipline but not the
same substrate. **IR-anchored projections**—the compilation pipeline described
in Part 4—take a compiled **Architecture IR** snapshot (plus configuration) as
input. **Runtime workspace projections** take extracted graph slices, merged
workspace graph material, or related runtime state as input; **Runtime** builds
and invalidates them under observation rules, not as a substitute for
compilation. Both lineages stay **derived**, reproducible, and traceable; they
differ in what triggers rebuild and what provenance must record. For graph
postures on the runtime side, see [Semantic Graphs](../13-advanced-topics/13-01-semantic-graphs.md);
for lifecycle and governance signals, see [Governance Signals and Semantic Graph Lifecycle](../08-runtime/08-07-governance-signals-and-semantic-graph-lifecycle.md).

The exact resolution vocabulary belongs in the implementing toolchain and, when
shared across components, in **ste-spec**. The handbook-level rule is simpler:
projection level changes presentation and selection; it does not create a new
authority source.

### Tooling roles

Authoring tools may be interactive; **canonical** alignment happens when exports or live views **bind** to compiled IR, not when a picture floats in a shared drive ([Projections overview](04-08-projections-overview.md)).

## The Implications

Treat broken regeneration as a **severity**: blocking for regulated **scopes**, warning otherwise—policy choice, but not invisible. Automation and humans both consume **projections**; reproducible generation keeps **governed reasoning** stable when generated or assisted prose ships next to diagrams.

## Relationship to STE system

- **Neighbors:** [Diagrams](04-10-diagrams.md), [Projection documents](04-11-projection-documents.md), [View consistency](04-14-view-consistency.md).
- **Publication versus projection:** [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md).
- **Kernel / validation:** [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) (consistency checks may span projections and IR).

## Summary

- **Projections** are **derived projection functions**; the canonical compilation path takes **Architecture IR** (plus config) as input.
- **IR-anchored** and **runtime workspace** projection lineages share traceability discipline but differ in substrate and invalidation triggers.
- **Selection**, **notation**, and **provenance** are part of **accountability**, not cosmetics.
- Provenance-rich projections remain projections; metadata links them back to authority but does not move authority into the view.
- Multi-resolution projections are derived views at different levels of detail; compression must preserve traceability.
- Interactivity is fine; **forked truth** is not.

**Next:** [Diagrams](04-10-diagrams.md).
