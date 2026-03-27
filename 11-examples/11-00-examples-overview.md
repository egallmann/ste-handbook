# Part 11 — Examples Overview

This chapter explains the examples part: end-to-end walkthroughs that illustrate how STE artifacts chain together. Examples are illustrative; they do not define normative requirements.

## End-to-end examples

### AI Gateway (first walkthrough)

The primary walkthrough is **[STE examples: systems through the full lifecycle](00-overview.md)** — AI Gateway section — followed in order by the steps under `ai-gateway-example/` (requirements snapshot → ledger → ADR ladder → derived IR → code linkage → EDR → drift and correction) and the companion diagrams in `ai-gateway-example/diagrams/`.

For **Architecture IR → projection**, the same example includes [`ai-gateway-example/ir/architecture-ir.json`](ai-gateway-example/ir/architecture-ir.json) and **regenerated** Mermaid under [`ai-gateway-example/projections/generated/`](ai-gateway-example/projections/generated/), with [`projection-queries.md`](ai-gateway-example/projection-queries.md) as illustrative query-shaped specs.

### Instance Scheduler on AWS (second walkthrough, higher fidelity)

The second walkthrough lives under [`instance-scheduler-example/`](instance-scheduler-example/). It adds **Step 0** (single-user design chat: **conversation engine** + **Architect agent** with **personas**—FinOps, Security, AWS Cloud, Operations; full STE: **ste-rules-library** projections select personas and **project into ADRs**), **split** logical and physical ADRs, **requirement** and **invariant** entities in [`instance-scheduler-example/ir/architecture-ir.json`](instance-scheduler-example/ir/architecture-ir.json), and **path-level** linkage to the public **[Instance Scheduler on AWS](https://github.com/aws-solutions/instance-scheduler-on-aws)** repository. Projections: [`instance-scheduler-example/projections/generated/`](instance-scheduler-example/projections/generated/) (includes a **traceability** view), with [`instance-scheduler-example/projections/projection-queries.md`](instance-scheduler-example/projections/projection-queries.md).

## Why this matters

Examples bridge abstraction to practice. Readers use them to sanity-check understanding of earlier parts.

## Planned coverage

- How to read examples
- Assumptions and simplifications
- Pointers to spec for real constraints

## Relationship to other chapters

- Example system ([chapter](11-01-example-system.md))
