---
title: "Part 11: IR to projections"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# IR to projections

**Projections** are **views** of the architecture **generated from** **Architecture IR** (and, where the pipeline defines it, linked canonical sources): diagrams, inventories, traceability matrices, governance summaries, registries, and generated graphs or documents. They exist so humans and tools can **review** and **teach** without reading raw IR at scale.

## Derived and regenerable

Projections are **not** alternate sources of truth. If a diagram, table, or generated narrative disagrees with **published IR** for the same scope, the healthy response is to **fix compilation inputs or IR publication** and **regenerate**—not to hand-edit the projection and leave IR or ADRs unchanged. Hand-edited “pretty pictures” that bypass compilation are a common source of **drift** between what teams **see** and what the system **governs**.

Examples of projection-shaped outputs in Part 11 include **Mermaid** and other **generated** files under each example’s `projections/` tree, plus illustrative **projection query** sketches that show how tabular or document views **slice** IR.

## What projections are good for

- **Stakeholder views** — Executives, security, operations, and engineers each need different slices; multiple projections are normal.
- **Traceability and governance views** — Relating components to requirements, invariants, and activated rules (for example composite “what applies here” tables).
- **Consistency checks** — Comparing two projections for the same IR snapshot should not yield silent contradictions ([View consistency](../04-architecture-model/04-14-view-consistency.md)).

## Relationship to publication

STE distinguishes **publication** (binding, governed records) from **projection** (derived renderings). At the design layer, **intent** and **published IR** anchor governance; projections **explain** them. See [Publication versus projection](../03-artifacts/03-08-publication-vs-projection.md) and [Projections overview](../04-architecture-model/04-08-projections-overview.md).

## Where the examples show this

- **AI Gateway:** [`projections/README.md`](./ai-gateway-example/projections/README.md), [`projections/generated/`](./ai-gateway-example/projections/generated/), [`projection-queries.md`](./ai-gateway-example/projections/projection-queries.md).
- **Instance Scheduler:** [`instance-scheduler-example/projections/README.md`](./instance-scheduler-example/projections/README.md), generated views and [`projection-queries.md`](./instance-scheduler-example/projections/projection-queries.md).

## Relationship to STE system

- **Projections (Part 4):** [Projections](../04-architecture-model/04-09-projections.md), [Diagrams](../04-architecture-model/04-10-diagrams.md)

**Previous:** [ADR to Architecture IR](./03-adr-to-architecture-ir.md) · **Next:** [Conformance](./05-conformance.md) · **Part 11 index:** [00-overview](./00-overview.md)
