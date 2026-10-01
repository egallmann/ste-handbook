---
title: "Traceability in Architecture IR"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Traceability in Architecture IR

## The Problem

**Traceability** is easy to promise and hard to sustain when nothing in the middle is **addressable**. Spreadsheets of requirement IDs rot first because they are not tied to a living architectural spine. STE’s answer splits the problem: Part 3 explains **trace** links as a **governance** artifact across **intent**, IR, **embodiment**, and **evidence**. This chapter explains how **Architecture IR** and related machine-facing semantic surfaces **host** the mid-layer legs of those traces—including individually addressable Normative Propositions—so navigation and automation are real.

## The Reframe

Read this chapter as **IR-centric trace mechanics**, not a second definition of traceability. **Traceability** as a discipline—who owns links, what an edge means, lifecycle policy—is in [Traceability](../03-artifacts/03-06-traceability.md). Here, the focus is: which **entities** and **relationships** carry **trace** endpoints; how construction, materialization, and mapping create or update graph-local links; how traces support **blast radius**, **scopes**, **proposition-relative review**, and **evidence** binding—without inventing applicability edges.

## The Model

### Endpoints on the graph

Many traces terminate **on** model elements: a **constraint** binds to a component; an **ADR** maps to a changed interface edge; a Normative Proposition’s stable identity permits trace from declaring ADR into normalized representation and into Architecture IR where mapped; a test **scope** names a subgraph. Stable IDs keep those endpoints from floating when **projections** rearrange layout.

### Cross-type linking

Traces often cross artifact types: **intent** record → semantic entity → repository identity → **evidence** record. The architecture model is the **hub** for the structural and semantic middle: without it, “which service” in a requirement, “which proposition” in an ADR, and “which repo” in CI remain manually reconciled ([Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md)).

### Construction- and materialization-produced traces

Governed pipelines can emit or preserve trace edges implied by **intent**: explicit references in **ADRs**, structured requirement IDs, tagged **invariants**, ADR-contained Normative Propositions with stable identity, and normalized declaring-ADR qualification where embodiment surfaces provide it. Automated maintenance matters; hand-drawn matrices do not scale ([The problem of lossy reasoning](../00-problem/00-02-the-problem-of-lossy-reasoning.md)).

Do **not** invent automatic applicability edges from traceability. Traceability tells us what is connected and why; it does not prove that every reachable proposition governs every task.

### Impact, scopes, and candidate neighborhoods

Given traces, queries become engineering actions: “what **evidence** must rerun if this interface changes?”, “which **invariants** and Normative Propositions are candidates for review of this scope?”, “which embodiment relationships exist?” The model is the **reasoning surface** for those questions ([IR as a semantic graph](04-07-ir-as-a-graph.md)). Candidate and reachable remain distinct from applicable and conformant.

## The Implications

Weakening graph-local trace endpoints—orphan IDs, stale materialization, renamed entities without migration—shows up as **governance** debt as fast as weakening **intent**. Policies can require minimum link coverage for regulated paths; exceptions need owners, same as for **constraint** waivers. Proposition-relative review depends on stable NP identity and preserved declaring authority—not on treating every linked NP as task-governing.

## Relationship to STE system

- **Layer-wide traceability:** [Traceability](../03-artifacts/03-06-traceability.md) (governance artifact; cross-type story).
- **Compilation:** [Compilation and semantic materialization](04-04-compilation.md).
- **Evidence binding:** [Evidence](../03-artifacts/03-05-evidence.md), [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md).
- **Conformance:** [Conformance](../03-artifacts/03-07-conformance.md).
- **Later applicability work:** [Context assembly and MVC](../08-runtime/08-05-context-assembly-and-mvc.md).
- **MBSE alignment:** [Model-based systems engineering](../01-theory/01-08-model-based-systems-engineering.md).

## Summary

- Part 3 defines **traceability** as a maintained cross-type link structure; Part 4 explains how the architecture model **materializes** endpoints for structural and addressable normative semantics.
- Stable Normative Proposition identity enables declaring-ADR → representation → evidence linkage without inventing applicability.
- Traceability shows what is connected and why; reachability does not prove that every linked proposition governs every task.

**Next:** [Diff and change](04-06-diff-and-change.md).
