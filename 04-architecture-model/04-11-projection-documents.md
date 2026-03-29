---
title: "Projection documents"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Projection documents

## The Problem

Long-form write-ups—decision summaries, onboarding guides, **compliance** narratives—often duplicate structure that already lives in **Architecture IR**. Unmoored prose **drifts**; facts disagree across pages; **governance** cannot tell which text matched **what** was approved. **Projection documents** solve the pattern: narrative **generated or anchored** to IR so updates propagate when the model moves.

## The Reframe

A **projection document** is a **text-first projection**: templated sections, embedded references to IR elements, tables produced from queries, and **provenance** of the IR snapshot. It is still a **projection**—not a second **canonical** model. Human editing may wrap generated cores with judgment-shaped context; **governance** should separate **generated structural facts** from **commentary** when **assessment** requires clarity.

## The Model

### Templates and slots

Templates declare **slots** filled from IR: service catalogs, interface lists, ownership matrices, dependency roll-ups. Slots **fail closed** when data is missing, surfacing **compilation** gaps instead of silent blanks that readers fill with guesses.

### Embeddings and references

Stable **references** (IDs, deep links) connect paragraphs to **entities** and **relationships**. When IR **diff** shows a breaking interface change, linked sections flag **stale** text until regenerated or explicitly waived.

### Mixed content

Some paragraphs will remain hand-written: rationale, historical context, customer commitments. STE does not forbid prose; it demands **honesty** about what is **machine-backed** versus interpretive. **ADRs** remain the durable home for **decision** rationale; projection documents **summarize** and **navigate**, they do not replace **intent** records ([Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md)).

### Publication boundaries

If a document is **published truth** for a **scope**, classify it per [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md). Most projection documents are **derived**; a few may be elevated to **publication** with explicit **governance**.

## The Implications

Documentation teams and engineers share responsibility: templates and **projection** jobs are engineering assets. **Agents** that draft docs should consume the same **projection** pipeline to avoid a new shadow graph in natural language.

## Relationship to STE system

- **Diagram projections:** [Diagrams](04-10-diagrams.md).
- **Views:** [Architecture views](04-12-architecture-views.md), [Stakeholder views](04-13-stakeholder-views.md).
- **Traceability:** [Traceability in Architecture IR](04-05-traceability.md).

## Summary

- **Projection documents** ground narrative in **Architecture IR** via templates, queries, and stable references.
- Separate **generated structural facts** from interpretive prose for **assessment** clarity.
- Elevation to **publication** is a **governance** choice, not the default for generated docs.

**Next:** [Architecture views](04-12-architecture-views.md).
