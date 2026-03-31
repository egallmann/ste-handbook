---
title: "How to read diagrams and projections"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# How to read diagrams and projections

## The Problem

Handbook **diagrams** are easy to treat like **architecture**: a compelling figure feels authoritative, especially when it matches a mental model you already hold. **Registries**, **graphs**, and exported tables feel like “the database of truth” for the same reason. Without a short reading discipline, you can invert STE’s authority story—arguing from ink and generated files while skipping **intent** **artifacts**, published **Architecture IR**, and **governance**.

## The Reframe

In STE, **diagrams** are **projections**: they explain and orient; they do not replace **canonical** records. **Machine-facing** **registries** and **graph** exports are also **projections**: compiled, regenerable views over the same commitments **Architecture IR** is supposed to carry—useful for **query**, **diff**, and tooling, not a competing legislature.

## The Model

### Diagrams are not the architecture

When a chapter shows a Mermaid figure, read it as a **map of roles and flows**. If prose and sketch disagree during drafting, trust the prose until the sketch is repaired—never the reverse. For the primary closed-loop map, start from [System overview](02-03-system-overview.md).

### Registries and graphs are machine-facing projections

**Manifests**, **architecture indices**, **entity** and **relationship** **registries**, **system** and **component** registries, and similar outputs exist so automation can **traverse** and **check** structure at scale. They should **rebuild** from **canonical** inputs under the same rules each time. Editing them by hand to “fix a presentation” creates **decorative fiction** unless the change is folded back into **intent** or IR and **regenerated**.

### Physical-system versus physical-component ADRs

At handbook altitude: **physical-system** ADRs describe **subsystem** boundaries, topology, and the coarse shape of how major parts connect—**where** responsibility is divided. **Physical-component** ADRs carry **implementable** responsibility: concrete components, interfaces, and expectations that **realization** can satisfy. Both **refine** **logical** ADRs; they do not invent a separate decision stack ([Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md)).

### Unresolved entries and review artifacts

**Unresolved** registries, gap lists, and **review** summaries are **workflow** and **evidence** surfaces: they make omissions visible and track what still needs an owner or a **governance** decision. They are not **primary authority** for what the system **is**; closure belongs in **intent** records and published IR, with traces that link back.

## The Implications

When something looks wrong in a **derived** file, ask first whether **intent** or **Architecture IR** is wrong, whether **compilation** failed silently, or whether **projections** are **stale**. When an assistant or operator consumes graph state, ask whether **freshness** and **reconciliation** **gates** were satisfied—not only whether the natural-language answer sounded plausible ([Preflight and the Reasoning Gate](../08-runtime/08-04-preflight-and-reasoning-gate.md)).

## Relationship to STE system

- **Canonical versus derived diagram:** [Projections overview](../04-architecture-model/04-08-projections-overview.md).
- **Projection bundle over IR:** [IR as a graph](../04-architecture-model/04-07-ir-as-a-graph.md).
- **Publication versus projection:** [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md).
- **Worked minimal shapes:** [Illustrative walkthrough](../04-architecture-model/04-15-illustrative-walkthrough.md).

Normative schemas and admission behavior live in **ste-spec**.

## Summary

- **Diagrams** explain; **Architecture IR** and **intent** **artifacts** publish what is binding for structure and decisions.
- **Registries** and **graphs** are **compiled** **projections** for machines; **regenerate** them instead of treating hand edits as truth.
- **Physical-system** ADRs bound subsystems; **physical-component** ADRs bound implementable parts; both **refine** **logical** **intent**.
- **Unresolved** and **review** artifacts surface **gaps** and **process**; they do not replace **governance** closure in **canonical** records.

**Next:** [The STE lifecycle](02-04-the-ste-lifecycle.md) for how the loop runs over time.
