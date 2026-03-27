---
title: "Projections"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Projections

## The Problem

“Generate documentation from the code” and “keep the diagram updated” are slogans without a **source of truth**. **Projections** fail when nobody defines **what** they project from, **how** selection works, or **when** regeneration happens. STE names **Architecture IR** as the structural **source** so **projections** become repeatable **views**, not one-off exports.

## The Reframe

A **projection** is produced by a **projection function**: inputs include an IR snapshot (and configuration: layout, filters, notation), outputs include human-consumable artifacts (SVG, PDF, HTML, slides). The function should be **versioned** or **reproducible** so “what we reviewed” is answerable. This chapter stays conceptual; toolchains live outside the handbook.

## The Model

### Selection and filtering

Projections **slice** the graph: by **scope**, by type (only data stores), by criticality, by team ownership. Filtering is not neutral—it encodes **stakeholder** questions. Those questions should be **named** so **governance** knows which projection supports which **decision**.

### Layout and notation

Layout is **presentation**; semantics ride on IR identities and edges. Changing layout should not change meaning. Notation mappings (C4 levels, UML profiles) are **conventions** teams adopt; STE cares that elements **map** to IR nodes and edges **deterministically**.

### Freshness and provenance

A projection should carry **provenance**: which IR version, which projection spec, when generated. Reviewers use provenance the same way they use artifact digests for **evidence**—to know **what** was on the table in a **governance** event.

### Tooling roles

Authoring tools may be interactive; **canonical** alignment happens when exports or live views **bind** to compiled IR, not when a picture floats in a shared drive ([Projections overview](04-08-projections-overview.md)).

## The Implications

Treat broken regeneration as a **severity**: blocking for regulated **scopes**, warning otherwise—policy choice, but not invisible. **Agents** and humans both consume **projections**; reproducible generation keeps **governed reasoning** stable when automation drafts prose around diagrams.

## Relationship to STE system

- **Neighbors:** [Diagrams](04-10-diagrams.md), [Projection documents](04-11-projection-documents.md), [View consistency](04-14-view-consistency.md).
- **Publication versus projection:** [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md).
- **Kernel / validation:** [Validation](../07-kernel/07-03-validation.md) (consistency checks may span projections and IR).

## Summary

- **Projections** are **functions** from **Architecture IR** (plus config) to human-usable artifacts.
- **Selection**, **notation**, and **provenance** are part of **accountability**, not cosmetics.
- Interactivity is fine; **forked truth** is not.

**Next:** [Diagrams](04-10-diagrams.md).
