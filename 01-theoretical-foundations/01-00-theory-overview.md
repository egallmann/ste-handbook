---
title: "Part 1 — Theoretical Foundations Overview"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-23"
---

# Part 1 — Theoretical Foundations Overview

## The Problem

Software organizations rarely disagree about whether they need to ship, operate safely, or evolve under pressure. They disagree about *objects*: what counts as a system, what counts as a decision, what counts as evidence, and what “aligned” means when tools, people, and time move faster than memory.

That disagreement is not only social. It is structural. Different traditions name different slices of the same situation. A controls engineer reaches for feedback and stability language. A safety engineer reaches for hazards and assurance. An architect reaches for views and quality attributes. A systems engineer reaches for models and trace threads. Each tradition is useful. None of them, by itself, is a complete operational story for how intent stays honest against embodiment over the life of a software-intensive system.

Readers arrive with uneven backgrounds. Some will want to skip to “the STE parts.” That impulse is understandable, but it has a cost. Without a shared map, later chapters sound like a pile of mechanisms. With a map, the mechanisms read as answers to questions you can already name.

This part is also a place where enthusiasm can misfire. It is tempting to borrow a prestigious field and imply that STE “inherits” formal theorems, or that a metaphor is a proof. That kind of over-claiming does real harm. It trains skeptics to dismiss the whole program, and it trains believers to mistake vocabulary for rigor.

## The Reframe

Treat Part 1 as **scaffolding**, not a survey. Each chapter introduces a small vocabulary and a small set of mental moves that show up again later. The goal is not to teach the fields end to end. The goal is to make the handbook’s later language legible: why we talk about **drift** the way we do, why **Architecture IR** is a graph-shaped object, why **governance** is described as a loop, and why “lossy reasoning” is more than a metaphor.

STE is not invented from nothing, and it is not a rebranding of a single predecessor. Different disciplines studied different parts of the problem: boundaries and composition, feedback and error, information loss in representation, choice under uncertainty, regulation at multiple levels, architectural description, model-first engineering, and constraint-based assurance. STE’s job is to combine those insights into an **operational** engineering system: artifacts, compilation, assessment, and human control over time.

This handbook stays **explanatory**. Where contracts, semantics, or admission behavior must be exact, **ste-spec** and published technical contracts are authoritative. Part 1 orients you. It does not replace those sources.

### How to read this part

You can read linearly or out of order, but linear reading has a benefit. Later theory chapters assume you are comfortable naming systems, signals, decisions, and governance loops without mixing the metaphors blindly.

If you are impatient, skim the **Summary** sections first, then return to the **Model** sections for the definitions you actually need.

### Relationship to Part 0

Part 0 is a logical chain: it argues that engineering is **decision-making** under **constraints**, that informal channels are **lossy**, that **intent** must stay distinct from **embodiment** if **drift** and **conformance** are to mean anything, and that **governance** is how those commitments survive time.

Part 1 does not repeat that proof. It supplies **adjacent language** from established fields so you can recognize why STE names certain mechanisms the way it does. Think of Part 0 as the “why this book exists” argument. Think of Part 1 as the “what intellectual neighborhood we are standing in” map.

If you have not read Part 0, you can still read Part 1, but you may find some STE terms feel unmotivated. In that case, read [Engineering as decision-making](../00-foundations/00-01-engineering-as-decision-making.md) and [The STE thesis](../00-foundations/00-07-the-ste-thesis.md), then return here.

## The Model

### A map of the eight lenses

The chapters that follow are paired with the STE ideas they prepare. None of these pairings are claims of formal reduction.

**Systems theory** ([Systems theory](01-01-systems-theory.md)) gives **system**, **boundary**, **environment**, **state**, and the distinction between **structure** and **behavior**, plus composition and decomposition. STE uses that language when it talks about what the **Architecture IR** is a model *of*, and why “the system” is not a passive metaphor.

**Control theory** ([Control theory](01-02-control-theory.md)) gives **feedback**, **error**, **setpoint** (reference), and a careful, informal notion of **stability**. STE uses control vocabulary when it discusses comparing **intent** to **embodiment** and detecting **drift**. The handbook will be explicit where that language is **not** a literal control system.

**Information theory** ([Information theory](01-03-information-theory.md)) gives intuition for **signal versus noise**, **entropy**, and **lossless versus lossy** representation. STE uses that intuition to explain why informal channels thin **decision** rationale, why canonical artifacts matter, and why traceability is a preservation problem rather than a paperwork problem.

**Decision theory** ([Decision theory](01-04-decision-theory.md)) gives **options**, **commitments**, uncertainty, and updating beliefs when new **evidence** arrives. STE uses that framing for **ADRs**, decision lifecycle, and revisiting choices under **governance**.

**Cybernetics** ([Cybernetics](01-05-cybernetics.md)) emphasizes **regulation**, feedback at the level of organizations, and “second-order” control: steering the mechanisms that steer. STE connects this to **governance**, human-in-the-loop operation, and lifecycle oversight.

**Software architecture theory** ([Software architecture theory](01-06-software-architecture-theory.md)) treats **architecture** as structure plus behavior plus **constraints**, and it introduces **views** and **viewpoints** and **quality attributes**. STE connects this to **Architecture IR**, projections, and the separation between architectural description and **implementation** detail.

**Model-based systems engineering (MBSE)** ([Model-based systems engineering (MBSE)](01-07-model-based-systems-engineering.md)) treats models as primary engineering artifacts integrated across lifecycle. STE aligns on the idea of a compiled canonical model and trace threads, but it is not a blanket endorsement of every MBSE practice or toolchain.

**Safety and constraints engineering** ([Safety and constraints engineering](01-08-safety-and-constraints-engineering.md)) treats **hazards**, **constraints**, **invariants**, and assurance **evidence**. STE connects this to **invariants**, **constraints**, **conformance**, and certification language without turning the handbook into a safety standard.

### Shared vocabulary you should carry forward

Part 0 already established the core STE contract: **decisions** under **constraints**, **intent** versus **embodiment**, **validation** as **evidence**-linked **conformance** assessment, and **governance** over time. Part 1 does not redefine those terms. It adds *adjacent* vocabulary from other fields so later chapters can be precise without smuggling hidden assumptions.

If one sentence can serve as a guardrail for the whole part: **borrow mechanisms and vocabulary, not authority.**

Keep a habit of translation. When someone imports a strong metaphor from a favorite field, ask what object in STE it maps to: an **artifact**, a model element, an **invariant**, a **governance** decision, or an **evidence** item. If there is no mapping, treat the metaphor as private color, not shared engineering structure.

## The Implications

### What changes in how you argue

After Part 1, disagreements about architecture should be easier to route to the right question. Are we debating **boundary** placement? Are we debating control of change (**governance**)? Are we debating information loss in artifacts (**traceability**)? Are we debating commitments and their reversibility (**decisions** and **ADRs**)? Are we debating assurance (**evidence** and **invariants**)?

Mixing those questions silently is how teams talk past each other. Separating them is not bureaucracy. It is clarity.

### A concrete failure mode mixing vocabularies

Consider a review meeting where one engineer argues “the system is unstable” because incidents are frequent, another argues “we have an information problem” because nobody can find the authoritative diagram, and a third argues “we need better governance” because exceptions keep becoming normal. Those statements might all be true. They are not the same claim.

Without shared vocabulary, teams merge them into a single anxious blob and pick a single silver bullet: more testing, more process, more automation, more docs. Each remedy might help a real slice of the problem while missing another slice entirely.

Part 1 does not solve organizational politics. It does give you cleaner nouns: **state** and **boundary** for what “the system” is, **error** and **reference** for what “stability” might mean in a control metaphor, **noise** and **compression** for why documentation diverges, **options** versus **commitments** for what a decision record must preserve, and **invariants** for what must stay true for a design to remain valid. Cleaner nouns do not guarantee consensus, but they make disagreement inspectable.

### Where the analogies stop

These chapters are careful about limits. In particular:

- Control metaphors help describe comparison and correction behavior. They do not, by themselves, justify a specific automation design.
- Information-theoretic language here is **intuitive**. It is not a claim that engineering organizations have measurable channel capacities in bits.
- MBSE overlap is **selective**. STE’s scope is anchored in the handbook thesis and in **ste-spec**, not in every MBSE methodology choice.

If a chapter’s analogy helps you predict a failure mode or choose a representation, it has done its job. If it makes you feel certain without **evidence**, discard the certainty, keep the vocabulary.

### What to carry into later parts

If you remember only a few carries from Part 1, make them practical.

First, **name the boundary** before you argue about correctness. “The system” usually includes more than a service binary: dependencies, operators, data contracts, and time. Second, treat **intent** as something you can point to: records, models, **invariants**, not vibes. Third, treat **embodiment** as something you can observe and link **evidence** to. Fourth, expect **governance** to be part of the design: who may change what, under what review, with what trace thread.

Those carries align with the handbook thesis. Part 1 gives you language for why each carry is structurally motivated rather than culturally preferred.

## Relationship to STE system

Part 0 explains why implicit **decisions** and lossy channels produce **drift**. Part 1 explains *which traditional disciplines give language* for the objects STE makes explicit: models, projections, loops, and assurance.

Part 2 turns from scaffolding to the STE-shaped overview of the whole system story. Start with [Part 2 — STE overview](../02-overview/02-00-overview.md) when you want the map of parts and terminology at book scale.

From there, the handbook’s technical spine continues through **intent** (including **ADRs** and **invariants**), **Architecture IR** (system model, compilation, traceability), **projections**, **Kernel** and **validation**, and lifecycle **governance**. Many linked chapters are still outlines. Treat links as **directional**: they show where the argument continues, not a promise that every destination is already finished.

## Summary

- Part 1 is **scaffolding**: vocabulary and mental models that make later STE chapters intelligible as one system story.
- STE draws on multiple disciplines because each studied a real slice of engineering reality; STE combines them into operational artifacts, models, assessment, and **governance**.
- Metaphors and borrowed language are useful when they clarify mechanisms and failure modes; they are harmful when they substitute for **evidence** or imply formal proofs STE does not claim.
- **Systems**, **control**, **information**, **decisions**, **cybernetics**, **architecture**, **MBSE**, and **safety/constraints** chapters each prepare specific later terms: **Architecture IR**, **drift**, traceability, **ADRs**, **governance**, projections, compilation, and **invariants**.
- For STE’s integrated overview after theory, read [Part 2 — STE overview](../02-overview/02-00-overview.md); for normative precision, rely on **ste-spec** and published contracts rather than handbook prose.
