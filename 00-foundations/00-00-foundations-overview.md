---
title: "Part 0: Foundations Overview"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-23"
---

# Part 0: Foundations

## The Problem

If you have built or operated software for long enough, you know that engineering is not mostly typing. It is a sequence of choices made under pressure. Those choices echo into every later change, incident review, and conversation about what the system is allowed to become.

Substantial systems are bundles of **decisions** under **constraints**. The running system is the residue of those **decisions**, whether or not anyone can still name them. When the record of commitments is thin, organizations reconstruct **intent** from code, operations, and partial **evidence**. That work is structural, not a verdict on individuals.

When **intent** travels mainly through informal channels, **drift** follows: mismatch between what the organization believes it decided and what **embodiment** supports. Without a shared problem statement, later technical chapters read as a bag of mechanisms. With it, they read as answers to questions you already agree are worth asking.

## The Reframe

The Foundations part of this handbook is not a tutorial and not a sales argument. It is orientation: a careful statement of the problem that makes the rest of the book intelligible as one continuous engineering argument.

Part 0 is written as a **logical chain**, not as a set of standalone essays. Each chapter introduces a gap that the next chapter closes or reframes. By the end, the STE thesis should read as a necessary conclusion, not an early slogan.

**Part 0 establishes the shared foundations that make STE readable as a single discipline, not a collection of mechanisms.**

**System of Thought Engineering (STE)** is the name this handbook gives to a discipline that addresses **lossy reasoning**, implicit **decisions**, thin **intent**, and **drift**. The full thesis is stated at the end of Part 0 so it can read as a conclusion. If you want the compact answer first, read [The STE thesis](00-07-the-ste-thesis.md), then return to the start of the chain.

## The Model

The chapters in Part 0 build one story in order:

1. [Engineering as decision-making](00-01-engineering-as-decision-making.md) names engineering as **decision-making** under **constraints** and defines **traceability**, so the chain has a precise starting vocabulary.
2. [The problem of lossy reasoning](00-02-the-problem-of-lossy-reasoning.md) explains why rationale and records degrade across channels and time, which answers why **traceability** does not appear by accident.
3. [Intent versus Implementation](00-03-intent-vs-implementation.md) separates **intent** from **embodiment** so **drift** and **conformance** are definable, which answers what two sides **validation** must compare.
4. [Architecture as a first-class artifact](00-04-architecture-as-a-first-class-artifact.md) places **architecture** in structured, versioned **artifacts**, which answers where the **architectural** half of **intent** lives between prose and production.
5. [Governed reasoning](00-05-governed-reasoning.md) constrains **reasoning** with explicit **rules**, **scope**, and **evidence**, which answers how reviews stay repeatable once **artifacts** exist.
6. [Deterministic versus Stochastic Systems](00-06-deterministic-vs-stochastic-systems.md) separates **deterministic** checks from **stochastic** or judgment-shaped work, which answers what repeatability can honestly mean for assessment.
7. [The STE thesis](00-07-the-ste-thesis.md) integrates the chain into one discipline and states what to carry into the rest of the book.

### Key terms in Part 0

These terms are used with stable meanings in Part 0 (full gloss: [.writing-rules/04-terminology.md](../.writing-rules/04-terminology.md)):

- **Decision:** A commitment that closes design space among feasible alternatives under **constraints**, with rationale that should be recoverable later.
- **Constraint:** A limit that reduces design options; it shrinks the design space or binds evolution.
- **Intent:** Normative commitments: **decisions**, **constraints**, and **invariants**, traceable to **embodiment**.
- **Embodiment:** What exists in code, infrastructure, configuration, and runtime (and operations practice); the descriptive side you compare to **intent**.
- **Implementation:** The code-level portion of **embodiment** (modules, repos, concrete builds), not a synonym for the whole descriptive side.
- **Drift:** Any difference between maintained **intent** and observed **embodiment**.
- **Conformance:** The claim that **embodiment** matches declared **intent** (including observed runtime behavior where relevant).
- **Evidence:** Observations, with provenance, about what **embodiment** did or is; input to **validation**.
- **Validation:** **Evidence**-linked assessment of **conformance** under agreed **rules** and **scopes**.
- **Architecture:** The **structure of decisions** that shape the system, not only diagrams.
- **Architecture IR:** The canonical compiled **architecture** model derived from **intent** **artifacts**; machine-addressable and shared for inspection and diff.
- **Governed reasoning:** **Reasoning** constrained by explicit **rules**, **scope**, and **evidence** expectations, tied to versioned **artifacts** and **governance** loops.
- **Governance:** Control over system change over time: review, versioning, escalation, and allowed change.
- **Deterministic:** Repeatable assessment under defined **rules** and **inputs** (and stated assumptions), treated as stable for **governance** where honest.
- **Stochastic:** Residual variability or judgment-shaped domains that remain even when the procedure is honest; expectations must be explicit.

## The Implications

Code, tests, and documentation each help, but none alone is a durable, structured home for **architectural** commitments that you can revisit, compare, and check as the system evolves. Part 0 connects those pieces into a single loop so readers can carry one vocabulary into later parts.

This book explains the ideas and how they fit together. Where exact contracts matter, they belong in **ste-spec** and in code and systems built to match them. The handbook orients you; it does not replace those authorities.

## Where this leads

The chain starts where the work starts: [Engineering as decision-making](00-01-engineering-as-decision-making.md), which defines **decision**, **constraint**, **design space**, and **traceability** for the rest of Part 0.

## Relationship to STE system

Part 0 concludes in [The STE thesis](00-07-the-ste-thesis.md), which states what STE is and what to read next in the wider handbook. **ste-spec** remains normative for wire formats, semantics, and admission behavior wherever the handbook points beyond orientation.

## Summary

- Part 0 is one **logical chain** from **decisions** and **constraints** through **lossy reasoning**, **intent** versus **embodiment**, **architecture** as **artifacts**, **governed reasoning**, and **deterministic** versus **stochastic** assessment to the **STE thesis**.
- **Decisions** close design space; **constraints** reduce options; **traceability** links commitments to **embodiment** and **evidence**.
- **Drift** and **conformance** require two maintained sides; **validation** is **evidence**-linked assessment under **rules** and **scopes**.
- **Governance** and **governed reasoning** keep change reviewable over time; **Architecture IR** is the shared compiled structural object for **architecture**.
