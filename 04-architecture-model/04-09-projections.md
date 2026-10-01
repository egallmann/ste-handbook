---
title: "Projections"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Projections

## The Problem

“Generate documentation from the code” and “keep the diagram updated” are slogans without a **source of truth**. **Projections** fail when nobody defines **what** they project from, **how** selection works, or **when** regeneration happens. STE names **Architecture IR** as the canonical machine-oriented architecture model so **projections** become repeatable **views**, not one-off exports—and so Normative Propositions are not silently re-authored by display tooling.

## The Reframe

[Projections overview](04-08-projections-overview.md) states the policy: declaring sources retain authority; IR is **canonical machine representation**; projections are **derived**. Here, treat a **projection** as a **projection function**: inputs include an IR snapshot (and configuration: layout, filters, notation), outputs include human-consumable artifacts (SVG, PDF, HTML, slides). The function should be **versioned** or **reproducible** so “what we reviewed” is answerable. This chapter stays conceptual; toolchains live outside the handbook.

## The Model

### Selection and filtering

Projections **slice** the graph: by **scope**, by type (only data stores; only Normative Propositions declared by a named ADR), by criticality, by team ownership. Filtering is not neutral—it encodes **stakeholder** questions. Those questions should be **named** so **governance** knows which projection supports which **decision**.

**Selection is not applicability determination.** If a projection includes Normative Propositions, say why they were selected, preserve provenance and declaring authority, and distinguish “included in this view” from “governs this task.”

### Layout and notation

Layout is **presentation**; semantics ride on model identities and edges. Changing layout should not change meaning. Notation mappings (C4 levels, UML profiles) are **conventions** teams adopt; STE cares that elements **map** to model nodes and edges **deterministically**.

### Provenance and normative metadata

A projection should carry **provenance**: which IR (or related) version, which projection spec, when generated. For normative semantics, projections must not silently strip the metadata required to understand meaning: identity, declaring authority, normative force, scope, and related qualification. Reviewers use provenance the same way they use artifact digests for **evidence**—to know **what** was on the table in a **governance** event.

### Tooling roles

Authoring tools may be interactive; **canonical** alignment happens when exports or live views **bind** to the governed architecture model, not when a picture floats in a shared drive ([Projections overview](04-08-projections-overview.md)).

## The Implications

Treat broken regeneration as a **severity**: blocking for regulated **scopes**, warning otherwise—policy choice, but not invisible. Automation and humans both consume **projections**; reproducible generation keeps **governed reasoning** stable when generated or assisted prose ships next to diagrams. Do not let a filtered NP list become a de facto obligation set for an unstated task.

## Relationship to STE system

- **Neighbors:** [Diagrams](04-10-diagrams.md), [Projection documents](04-11-projection-documents.md), [View consistency](04-14-view-consistency.md).
- **Publication versus projection:** [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md).
- **Kernel / validation:** [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) (consistency checks may span projections and IR).
- **Later applicability:** [Context assembly and MVC](../08-runtime/08-05-context-assembly-and-mvc.md).

## Summary

- **Projections** are **functions** from the architecture model (plus config) to human-usable artifacts.
- **Selection**, **notation**, and **provenance** are part of **accountability**, not cosmetics; selection ≠ applicability.
- Normative projections must preserve enough identity, authority, force, scope, and provenance to avoid silently changing meaning.
- Interactivity is fine; **forked truth** is not.

**Next:** [Diagrams](04-10-diagrams.md).
