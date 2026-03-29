---
title: "Part 11: ADR to Architecture IR"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# ADR to Architecture IR

After **canonical design** is captured in ADRs, STE **compiles** a machine-consumable **Architecture IR**: a normalized graph of entities, relationships, boundaries, contracts, and **trace** edges. This chapter is about that **design → compiled model** transition—not about drawing new architecture by editing JSON by hand.

## Rules activation

**Rules activation** connects **governance** to the emerging design: signals in conversation, requirements, and ADRs—and especially **technology and responsibility choices** as they land—**select** applicable rules throughout the design arc (illustrated in Part 11 with **ste-rules-library** patterns). The walkthrough’s **rules activation** step **records** **signal → rule → reason** explicitly once those signals are stable enough to teach; that is not the first moment rules matter. Activation records **why** a rule applies; they **inform** compilation and assessment. Treat activation as **derived governance context** tied to canonical design, not as a replacement for ADRs.

## What Architecture IR is

- **Derived** from **ADRs** (and related canonical inputs) plus compilation and linking rules defined in **ste-spec** and your program policy—not an independent “second design document.”
- A **compiled / normalized** representation: components, relationships, deployment mappings, requirement and invariant nodes where the pipeline includes them, and traceability to source records.
- The **structural substrate** for a declared scope: analysis, **projections**, and runtime-oriented reasoning read IR. **Published IR** is what downstream **projections** must track for structural consistency (see [Projections overview](../04-architecture-model/04-08-projections-overview.md)).

## Authority split (no contradiction with Part 4)

- **ADRs remain canonical design authority** — If the architecture *should* change, humans revise **intent** and **ADRs** under governance; you then **recompile** IR.
- **IR is derived** — You do not “fix” a wrong architecture by tweaking IR alone while leaving ADRs stale; that hides drift instead of resolving it.
- **Structural publication** — For automation and projections, **published IR** is the binding structural graph for that scope. That is compatible with IR being **derived from** ADRs: authority flows **from** ADRs **into** IR through compilation.

For compilation concepts in depth, see [Compilation](../04-architecture-model/04-04-compilation.md) and [Traceability in Architecture IR](../04-architecture-model/04-05-traceability.md).

## Where the examples show this

- **Rules activation:** [AI Gateway — rules activation](./ai-gateway-example/05b-rules-activation.md); [Instance Scheduler — rules activation](./instance-scheduler-example/05d-rules-activation.md).
- **Derived IR:** [AI Gateway — derived Architecture IR](./ai-gateway-example/06-derived-architecture-ir.md); [Instance Scheduler — derived Architecture IR](./instance-scheduler-example/06-derived-architecture-ir.md).

## Relationship to STE system

- **Architecture model and IR:** [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md)
- **IR as a graph:** [IR as a graph](../04-architecture-model/04-07-ir-as-a-graph.md)

**Previous:** [Conversation to ADR](./02-conversation-to-adr.md) · **Next:** [IR to projections](./04-ir-to-projections.md) · **Part 11 index:** [00-overview](./00-overview.md)
