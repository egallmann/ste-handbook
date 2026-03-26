---
title: "Terminology"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# Terminology

## The Problem

Ordinary words already mean something in engineering culture. "Requirements," "model," "validation," "governance," and "architecture" are overloaded. If each chapter quietly redefines them, readers will infer parallel systems where STE intends one loop.

The cost is not pedantry. The cost is unreviewable arguments: people agree on a word and disagree on the object.

## The Reframe

Treat this chapter as a stabilization pass aligned to the handbook glossary meanings, grouped by where a term sits in the STE story. Prefer consistency over completeness. If a term is missing here, later chapters should still use the glossary sense when they introduce it.

## The Model

### Intent and architecture

| Term | Handbook sense | Common confusion |
|------|------------------|------------------|
| **Intent** | Normative commitments about what the system should be or do, separated from incidental detail while remaining traceable to **embodiment**. | “Intent” as vague motive or product vision without recordable commitments. Prefer explicit **artifacts** when you mean something reviewable. |
| **Architecture** | The structured arrangement of architectural **decisions** as a coherent system description, not only diagrams or “the important stuff.” | “Architecture” as a role title or as a single diagram. |
| **Decision** | A commitment that selects among feasible alternatives in a **design space**, under **constraints**, with rationale that should be recoverable later. | “Decision” as any choice made in a meeting without a durable record. |
| **Constraint** | A boundary on allowed behavior or allowed change; shrinks the **design space** or binds evolution. | “Constraint” as only external regulation. Internal invariants are **constraints** too. |
| **Design space** | The set of feasible approaches remaining after **constraints** are applied. | “Design space” as brainstorming breadth without **constraints**. |
| **Invariant** | A statement that must hold for the design to remain valid unless **governance** explicitly revises it. | “Invariant” as a test name only. Tests may be **evidence**; the invariant is the commitment. |
| **ADR** | Architecture Decision Record: durable, reviewable record of a **decision**, often with context, options, and consequences. | “ADR” as a template file nobody reads. The object is the recorded **decision**, not the file ritual. |
| **Architecture IR** | Canonical, machine-addressable architecture model compiled from **intent** **artifacts**; shared object for inspection, diff, and traceability. | “The model” or “the graph” when you mean the canonical IR. Say **Architecture IR** once, then proceed. |

**Prefer / avoid:** Prefer **intent** over generic “requirements” when you mean normative STE commitments. If you truly mean contractual requirements management, say so explicitly and map to **intent** once.

### Embodiment, evidence, and runtime-facing terms

| Term | Handbook sense | Common confusion |
|------|------------------|------------------|
| **Embodiment** | The realized system: code, configuration, operational behavior, interfaces, and operations practice; the descriptive side compared to **intent**. | Using **implementation** as a synonym for the whole operational reality. **Implementation** is code-level realization inside **embodiment**. |
| **Implementation** | Code-level (and closely adjacent) realization: modules, repos, concrete builds. | Collapsing “everything running” into **implementation**. Use **embodiment** for the full descriptive side. |
| **Evidence** | Observations with provenance used in assessment: tests, telemetry, analysis outputs, and similar. | “Evidence” as any screenshot or opinion. STE cares about observations you can tie to **scope** and **rules**. |
| **EDR** | Evidence-linked record of **embodiment** or operational reality used in assessment and traceability. | Treating any log line as an EDR. The handbook sense ties evidence to assessment and traceability jobs. |
| **Validation** | **Evidence**-linked assessment of **conformance** between declared **intent** and observed **embodiment**, mechanical where appropriate and judgment-shaped where necessary. | “Validation” as approval politics or as testing alone. Tests can be **evidence**; **validation** is the assessment story. |
| **Conformance** | The claim that **embodiment** matches declared **intent** for an agreed **scope** under agreed **rules**. | “Conformance” as green CI. CI may contribute **evidence**; **conformance** is the explicit claim. |
| **Drift** | Difference between maintained **intent** and observed **embodiment**, or divergence between projections of **intent**. | “Drift” as team culture decay. STE names structural mismatch first. |

**Prefer / avoid:** Prefer **evidence** and **validation** over “quality” when you mean assessable claims about **embodiment** versus **intent**.

### Governance, rules, and kernel-facing terms

| Term | Handbook sense | Common confusion |
|------|------------------|------------------|
| **Governance** | Human and procedural control loop: review, versioning, escalation, and allowed change over time. | “Governance” as bureaucracy charts. STE means ownership of legitimacy, not paperwork volume. |
| **Rules** | Explicit criteria and policies: what is allowed, what must be produced, how **evidence** maps to decisions. | “Rules” as informal team habits. If they are not explicit, they are hard to assess. |
| **Kernel** | Decision and admission logic that consumes **evidence** and published contracts to make orchestration decisions in the STE story (assessment and gating at the abstraction this book uses). | A specific repo name as the whole idea. The handbook names a role; implementations live elsewhere. |

**Prefer / avoid:** Prefer **governance** over “process” when you mean control over legitimacy of change, not generic workflow.

### Projection and publication

| Term | Handbook sense | Common confusion |
|------|------------------|------------------|
| **Projection** | A derived human-usable view from a canonical source, intended to track the same commitments as other projections when the pipeline is healthy. | Any diagram or document. Projections are accountable views, not freeform summaries. |
| **Compilation** | The structured transformation from **intent** **artifacts** into **Architecture IR** where that pipeline exists. | “Compilation” as only compiler builds. Here it names the intent-to-IR transform. |
| **Traceability** | Ability to follow links from **decisions** and **invariants** through structure to **evidence** and **governance** outcomes. | Traceability matrices as an end in themselves. Matrices are a means; accountable chains are the goal. |

**Prefer / avoid:** Prefer **projection** as the canonical handbook term; when bridging classic architecture literature “views,” tie **views** to **projections** once and continue with **projection**.

### Lifecycle (handbook level)

| Term | Handbook sense | Common confusion |
|------|------------------|------------------|
| **Lifecycle** | The repeating path from design intent through **embodiment**, **evidence**, assessment, acceptance or certification framing, and controlled change. | A waterfall phase diagram. STE lifecycles loop. |
| **Certification (or acceptance)** | Framed decision that a **scope** meets **intent** under **rules** with recorded **evidence** and **governance** visibility. | A single external badge only. Handbook usage includes internal acceptance gates. |
| **Change** | Revisiting **decisions** and **invariants** when **constraints** or reality move; produces new or updated **intent** and new assessment needs. | “Change” as only code churn without revisiting commitments. |

The time-shaped loop (stages, feedback, and repeat) lives in [The STE lifecycle](02-04-the-ste-lifecycle.md). This table only pins words so later prose stays consistent.

## The Implications

Stable vocabulary lowers the tax on every later chapter. Readers can focus on mechanism instead of translating words. Authors can write shorter explanations because the object behind each term is shared.

## Relationship to STE system

Deep dives in Parts 3 through 9 should inherit the meanings here rather than inventing parallel glossaries.

When two readings of a term would change an obligation, **ste-spec** and published contracts decide the technical meaning. This chapter orients reading; it does not override the specification.

**Next:** Continue with [System overview](02-03-system-overview.md). The grouped senses here attach to named boxes, artifacts, and flows there. Read [The STE lifecycle](02-04-the-ste-lifecycle.md) after that for the same structure read as a repeating loop over time.

## Summary

- Terms are grouped by role: **intent** and **architecture**, **embodiment** and **evidence**, **governance** and assessment, **projection**, lifecycle.
- **Architecture IR**, **Kernel**, **ADR**, **EDR**, **validation**, and **conformance** are STE load-bearing words: use them consistently.
- Prefer **embodiment** over using **implementation** as a stand-in for the whole built system.
- **ste-spec** is authoritative when precise semantics matter; this list aligns reading, not contracts.
