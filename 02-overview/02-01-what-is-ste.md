---
title: "What Is STE?"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# What Is STE?

## The Problem

Labels stick fast. STE is easy to file under categories that almost fit: “better architecture docs,” “model-based systems engineering for software,” “a kernel service,” or “how we use AI in development.” Each label captures a slice. None of them carries the full obligation STE implies: to keep declared **intent**, built **embodiment**, **evidence**, and **governance** structurally connected as the system changes.

When STE is misfiled, teams import the vocabulary and drop the loop. You get ornate decision records that nobody assesses, or a canonical model that nobody treats as normative, or automation that drafts text without reviewable commitments. The failure mode is familiar: the artifact exists; the accountability does not.

## The Reframe

STE is a discipline for software-intensive systems under continuous change. It treats **architecture** as the **structure of decisions**, maintained as reviewable **intent** **artifacts** and, where appropriate, compiled into a canonical machine-addressable model (**Architecture IR**). It treats **embodiment** (code, configuration, runtime behavior, operations) as the descriptive side you compare to that **intent**. It treats **validation** as **evidence**-linked assessment of **conformance** under explicit **rules** and **scopes**. It treats **governance** as the durable human and procedural control loop that makes those objects legitimate over time.

That is not a toolchain slogan. It is a claim about what has to stay connected for engineering arguments to remain inspectable.

## The Model

### Handbook definition

**System of Thought Engineering (STE)** is the practice of engineering software-intensive systems so that **decisions** under **constraints** are recorded, structured, and traceable; **intent** stays distinct from **embodiment**; **architecture** is carried as durable **artifacts** and a canonical **Architecture IR** where compilation applies; change is assessed through **evidence**-linked **validation**; and **governance** closes the loop from assessment to allowed updates. STE is model-driven in the practical sense that shared structure is carried in explicit models and records, not only in chat and tacit team memory. It is architecture-centered because the primary durable commitments are architectural: what the system is allowed to be, how major decisions cohere, and what must remain true.

### Scope

STE addresses:

- How organizations record and evolve architectural **intent** without losing rationale.
- How that **intent** compiles into a shared structural object (**Architecture IR**) suitable for inspection, diff, and traceability.
- How **evidence** ties claims about **embodiment** to those records.
- How **governance** turns assessments into controlled change rather than ad hoc overrides.

### Non-goals and what STE is not

STE is not a replacement for domain engineering, safety case methodology where your industry already has one, or product management. It is not a promise that every property you care about can be checked mechanically. It is not “documentation discipline” divorced from assessment. It is not a single vendor product.

STE is also not a substitute for **ste-spec**. The specification carries normative contracts. The handbook explains how the ideas fit together and how to read the system story.

### A concrete hinge: one API change

Imagine a team changes a public API. **Intent** might be recorded as a decision to keep backward compatibility for two releases. **Embodiment** is what shipped: the schema, the gateway rules, the client breakage you discover in practice. **Evidence** might include contract tests, canary metrics, and support tickets. **Conformance** is the claim that **embodiment** matches the declared compatibility **intent** for an agreed **scope**. If the claim fails, **governance** decides whether to fix code, amend **intent**, or accept a bounded exception with owners and follow-up. STE names each of those objects so the conversation cannot collapse into “we thought it was fine.”

### Model-driven and architecture-centered

Model-driven, here, means the organization maintains explicit structured representations that multiple parties can inspect and diff, not that diagrams precede thought. Architecture-centered means the spine of durable commitments runs through architectural decisions and invariants, not that every line of code is modeled on a shelf.

### Roles of intent, evidence, governance, and conformance

- **Intent** states what should be true and why.
- **Evidence** states what you observed about **embodiment**.
- **Conformance** is the comparison claim between the two under **rules**.
- **Governance** decides what happens when **conformance** fails, when **constraints** change, or when **intent** must be revised honestly.

## The Implications

If STE matches your problem, the shift is structural. Reviews attach to **artifacts** and **scopes**. Arguments cite compiled structure where it exists. Automation and agents participate where **machine-readable intent** and **governed reasoning** make participation safe, rather than wherever tooling is convenient.

If STE does not match your problem, forcing the vocabulary still produces theater. The discipline assumes you want traceable **decisions**, honest **validation**, and **governance** that can say “no” or “not yet.”

## Relationship to STE system

The next chapters make the definition operable. [Terminology](02-02-terminology.md) disambiguates words that look ordinary. [System overview](02-03-system-overview.md) shows how the major pieces connect. [The STE lifecycle](02-04-the-ste-lifecycle.md) places those pieces in time.

For exact semantics and interfaces, rely on **ste-spec** and published contracts. This chapter is the orientation layer.

## Summary

- STE is a discipline that connects **intent**, **Architecture IR**, **embodiment**, **evidence**, **validation**, and **governance** into one inspectable evolution story.
- It is model-driven and architecture-centered in the handbook sense above, not as a synonym for any single MBSE practice or AI workflow.
- **Conformance** names the match claim; **evidence** and **rules** make that claim discussable; **governance** makes outcomes accountable.
- **ste-spec** is authoritative for normative detail; the handbook explains shape and reading order.
