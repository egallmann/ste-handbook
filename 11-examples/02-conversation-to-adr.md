---
title: "Part 11: Conversation to ADR"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# Conversation to ADR

This transition is where **intent becomes design**: messy, human discovery is converted into **governed, traceable** records that downstream compilation and runtime reasoning can attach to.

## The chain

1. **Conversation / intent discovery** — Dialogue surfaces the problem, constraints, tradeoffs, and risks. It is the **origin story** for trace links; in full STE it may be supported by facilitation, steelmanning, and persona-routed probes. The handbook examples fold much of that into a readable transcript or flow.
2. **Requirements snapshot** — **Bounded expectations**: structured rows (capabilities, constraints, invariants, NFRs) with **trace** back to conversation segments. This freezes “what we agreed we need” so design cannot silently drift from unstated wishes.
3. **Decision ledger** — **Bounded design space**: explicit questions tied to requirements (options, unknowns, tensions). The ledger does not replace ADRs; it **frames** what the logical ADR must resolve.
4. **Logical ADR (ADR-L)** — **Architectural intent**: capabilities, boundaries, and decisions that **answer** the ledger and **satisfy** requirements. This is where logical commitments live.
5. **Physical-system ADR (ADR-PS)** — **Topology and environment**: trust zones, integrations, deployment-shaped structure—refining logical intent into something deployable.
6. **Physical-component ADR (ADR-PC)** — **Implementable units**: interfaces, models, deployment targets, acceptance hints—what engineering can build against.

Together, the snapshot and ledger are **canonical inputs** to the ADR ladder. The **ADR family** is **canonical design authority** for the architecture in scope: if the design is wrong, you **revise ADRs** (and upstream requirements or ledger) under governance—not downstream derived artifacts.

## What this phase does *not* do

It does not yet produce **Architecture IR** or **projections** as hand-authored truths. Those are **derived** in later phases from ADRs, rules inputs, and compilation (see [ADR to Architecture IR](./03-adr-to-architecture-ir.md)).

## Where the examples show this

- **AI Gateway:** [Conversation](./ai-gateway-example/00-ste-conversation.md) → [Requirements snapshot](./ai-gateway-example/01-requirements-snapshot.md) → [Decision ledger](./ai-gateway-example/02-decision-ledger.md) → [Logical ADR](./ai-gateway-example/03-logical-adr.md) → [Physical-system ADR](./ai-gateway-example/04-physical-system-adr.md) → [Physical-component ADR](./ai-gateway-example/05-physical-component-adr.md).
- **Instance Scheduler:** [Canonical STE flow](./instance-scheduler-example/00-canonical-ste-flow.md) (extended dialogue and extracted artifacts), then [Requirements snapshot](./instance-scheduler-example/01-requirements-snapshot.md) through the split [logical](./instance-scheduler-example/03a-logical-adr-scheduling.md) / [physical](./instance-scheduler-example/04a-physical-system-hub.md) steps in [00-overview](./00-overview.md).

## Relationship to STE system

- **Intent artifacts:** [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md), [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md)
- **Part 11 entry:** [STE examples overview](./00-overview.md)

**Previous:** [What is a system?](./01-what-is-a-system.md) · **Next:** [ADR to Architecture IR](./03-adr-to-architecture-ir.md) · **Part 11 index:** [00-overview](./00-overview.md)
