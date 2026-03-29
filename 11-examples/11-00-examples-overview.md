# Part 11 — Examples Overview

This chapter explains the examples part: end-to-end walkthroughs that illustrate how STE artifacts chain together. Examples are illustrative; they do not define normative requirements.

## End-to-end examples

### AI Gateway (first walkthrough)

The primary walkthrough is **[STE examples: systems through the full lifecycle](00-overview.md)**. Read it for the **canonical eight-phase pipeline** (conversation → requirements → ADR-L / ADR-PS / ADR-PC → **rules activation** → Architecture IR → **runtime system**), then the **extension** (embodiment linkage, EDR, drift). Follow the files under `ai-gateway-example/` in the order given in [00-overview.md](00-overview.md), including [Phase 1 — conversation](ai-gateway-example/00-ste-conversation.md), [rules activation](ai-gateway-example/05b-rules-activation.md), and companion diagrams in `ai-gateway-example/diagrams/`.

For **Architecture IR → projection**, the same example includes [`ai-gateway-example/ir/architecture-ir.json`](ai-gateway-example/ir/architecture-ir.json) and **regenerated** Mermaid under [`ai-gateway-example/projections/generated/`](ai-gateway-example/projections/generated/), with [`projection-queries.md`](ai-gateway-example/projection-queries.md) as illustrative query-shaped specs.

### Instance Scheduler on AWS (second walkthrough, higher fidelity)

The second walkthrough lives under [`instance-scheduler-example/`](instance-scheduler-example/). It opens with **[canonical STE flow — Parts 1–8](instance-scheduler-example/00-canonical-ste-flow.md)** (**Human** + **AI (Architecture Partner)**; extracted artifacts; reader-facing **ADR**; **ADR steelman**; gap resolution and deferrals; architecture view; traceability), with **[Phase 1 entry](instance-scheduler-example/00-ste-conversation.md)** as a short navigation stub. Full STE may add a conversation engine, a separately voiced **Steelman** role, and **persona-routed** probes—**ste-rules-library** projections select rules from **signals**. The walkthrough then continues with **split** logical and physical ADRs, **[Phase 6 — rules activation](instance-scheduler-example/05d-rules-activation.md)**, **requirement** and **invariant** entities in [`instance-scheduler-example/ir/architecture-ir.json`](instance-scheduler-example/ir/architecture-ir.json), and **path-level** linkage to the public **[Instance Scheduler on AWS](https://github.com/aws-solutions/instance-scheduler-on-aws)** repository. Projections: [`instance-scheduler-example/projections/generated/`](instance-scheduler-example/projections/generated/) (includes a **traceability** view), with [`instance-scheduler-example/projection-queries.md`](instance-scheduler-example/projection-queries.md).

## Why this matters

Examples bridge abstraction to practice. Readers use them to sanity-check understanding of earlier parts. The **eight-phase spine** plus **artifact lineage** tables in [00-overview.md](00-overview.md) show STE as a **deterministic** path from conversation to runnable system, not a bag of templates.

## Planned coverage

- How to read examples
- Assumptions and simplifications
- Pointers to spec for real constraints

## Relationship to other chapters

- Example system ([chapter](11-01-example-system.md))
