---
title: "Part 5: Intent Formation"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Intent formation

**Intent formation** is when normative commitments take durable shape: what the system should do, what is ruled out, and which **decisions** record why. In STE this is never assumed to be a single front-loaded phase. **Intent** revises whenever strategy, risk, or learning demands it, always under **governance**.

Much **intent** starts as conversation at the human boundary; STE’s job is to **materialize** that discussion into structured **intent** **artifacts** under capture and review policy, then **compile** toward **Architecture IR** when structure is ready—see [Conversation engine overview](../09-human-interface/09-00-conversation-engine-overview.md) and [System overview](../02-overview/02-03-system-overview.md).

## Purpose of this stage

Establish and revise declared direction so that **embodiment** and **evidence** can be judged against something explicit, reviewable, and traceable rather than against memory or informal narrative.

## Artifacts involved

Primary **intent** artifacts: **ADRs**, requirements, **constraints**, and **invariants**. Supporting material may compile toward **Architecture IR** once structure is stable enough to model. See [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md), [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md), [Invariants](../03-artifacts/03-03-invariants.md), and [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md).

## Human responsibility

Humans specify goals, propose and approve **decisions**, write or accept requirement and **constraint** statements, define **invariants**, resolve conflicts between **intent** sources, and participate in review paths defined by policy. They remain accountable for what the organization claims the system must satisfy.

## STE system responsibility

STE captures governed inputs into structured records where workflows define it, preserves provenance and versioning, prepares or updates compilation inputs toward **Architecture IR**, and keeps **trace** edges coherent when **intent** artifacts supersede or refine prior records.

## Transitions to the next stage

The system moves toward **architecture definition** when enough **intent** exists to compile or refine a canonical structural model for a **scope**, without requiring a big-bang freeze. Partial **intent** with explicit **scopes** is normal. Return to this stage whenever **governance** authorizes **intent** change after **conformance** gaps or new **constraints**.

**Next stage chapter:** [Architecture definition](05-02-architecture-definition.md).

## Relationship to intent, implementation, and evidence

- **Intent:** This stage is where **intent** is authored and revised.
- **Implementation:** Little or no code-level change is required to *form* **intent**, but existing **embodiment** may inform discovery of conflicts that force **intent** updates.
- **Evidence:** Prior **evidence** (for example regression or incident data) often triggers **intent** revision; this stage consumes that signal through human **governance**, not by replacing decisions with raw metrics.

## Relationship to other chapters

- [The STE lifecycle](../02-overview/02-04-the-ste-lifecycle.md)
- [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md)
- [Compilation](../04-architecture-model/04-04-compilation.md)
- [Intent to implementation](../06-governance/06-02-the-governance-model.md)
- **ste-spec** for record schemas and workflow hooks.

**Next:** [Architecture definition](05-02-architecture-definition.md).
