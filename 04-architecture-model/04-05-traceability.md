---
title: "Traceability in Architecture IR"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Traceability in Architecture IR

## The Problem

**Traceability** is easy to promise and hard to sustain when nothing in the middle is **addressable**. Spreadsheets of requirement IDs rot first because they are not tied to a living structural spine. STE’s answer splits the problem: Part 3 explains **trace** links as a **governance** artifact across **intent**, IR, **embodiment**, and **evidence**. This chapter explains how **Architecture IR** **hosts** and **materializes** the structural legs of those traces so navigation and automation are real.

## The Reframe

Read this chapter as **IR-centric trace mechanics**, not a second definition of traceability. **Traceability** as a discipline—who owns links, what an edge means, lifecycle policy—is in [Traceability](../03-artifacts/03-06-traceability.md). Here, the focus is: which **entities** and **relationships** in IR carry **trace** endpoints; how **compilation** creates or updates graph-local links; how traces support **blast radius**, **scopes**, and **evidence** binding.

## The Model

### Endpoints on the graph

Many traces terminate **on** IR elements: a **constraint** binds to a component; an **ADR** maps to a changed interface edge; a test **scope** names a subgraph. IR provides **stable IDs** so those endpoints do not float when **projections** rearrange layout.

### Cross-type linking

Traces often cross artifact types: **intent** record → IR node → repository identity → **evidence** record. IR is the **hub** for the structural middle: without it, “which service” in a requirement and “which repo” in CI remain manually reconciled ([Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md)).

### Compilation-produced traces

**Compilation** can emit trace edges implied by **intent**: explicit references in **ADRs**, structured requirement IDs, tagged **invariants**. Automated maintenance matters; hand-drawn matrices do not scale ([The problem of lossy reasoning](../00-problem/00-02-the-problem-of-lossy-reasoning.md)).

### Impact and scopes

Given traces, queries become engineering actions: “what **evidence** must rerun if this interface changes?” or “which **constraints** mention this datastore?” The IR graph is the **reasoning surface** for those questions ([IR as a graph](04-07-ir-as-a-graph.md)).

## The Implications

Weakening graph-local trace endpoints—orphan IDs, stale compilation, renamed entities without migration—shows up as **governance** debt as fast as weakening **intent**. Policies can require minimum link coverage for regulated paths; exceptions need owners, same as for **constraint** waivers.

## Relationship to STE system

- **Layer-wide traceability:** [Traceability](../03-artifacts/03-06-traceability.md) (governance artifact; cross-type story).
- **Compilation:** [Compilation](04-04-compilation.md).
- **Evidence binding:** [Evidence](../03-artifacts/03-05-evidence.md), [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md).
- **Conformance:** [Conformance](../03-artifacts/03-07-conformance.md).
- **MBSE alignment:** [Model-based systems engineering](../01-theory/01-08-model-based-systems-engineering.md).

## Summary

- Part 3 defines **traceability** as a maintained cross-type link structure; Part 4 explains how **Architecture IR** **materializes** structural endpoints and compilation-backed edges.
- IR makes **blast radius** and **evidence** **scopes** **mechanical** rather than interpretive.
- Healthy traces require **stable identity** and honest **compilation**, not prettier matrices.

**Next:** [Diff and change](04-06-diff-and-change.md).
