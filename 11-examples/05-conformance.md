---
title: "Part 11: Conformance"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# Conformance

**Conformance** asks whether **reality matches commitments**: whether the **running system** and its **evidence** align with what **design** and the **compiled model** say should exist and how it should behave. Part 11 illustrates this after **runtime** and **linkage** are in view; the handbook’s artifact and kernel chapters define the concept in full.

## Semantic linkage

Meaningful conformance requires **semantic linkage**: durable association between **runtime resources** (code paths, infrastructure identifiers, APIs) and **design elements** in **ADRs** and **Architecture IR**. Without linkage, checks devolve to generic linting; with linkage, assessments can answer **system-scoped** questions (“this **component** in **this** environment”) and attach results to **traceable** IDs.

## What gets compared

Conformance reasoning typically spans:

- **ADR intent** — Obligations, boundaries, controls, and acceptance hints stated at logical and physical layers.
- **Architecture IR** — Structural commitments and relationships in the **published** compiled model for the scope under review.
- **Runtime resources and embodiment** — What is deployed, configured, and exercised.

Together, these answer questions such as:

- Is the system **built as designed** (components, integrations, zones)?
- Are **required controls** present and attached to the right scopes?
- Do **observations** (**EDR**, tests, telemetry) support or contradict the **designed** posture?

Exact check definitions and kernel behavior live in **ste-spec** and [Conformance](../03-artifacts/03-07-conformance.md); [Kernel conformance](../05-lifecycle/05-05-conformance-and-assessment.md) describes assessment mechanics at a high level.

## Where the examples show this

Runtime inventory and **code semantic linkage** appear in step 7 of each walkthrough; **EDR**-shaped evidence appears in step 8—those steps **set up** the narrative that conformance and drift build on.

- **AI Gateway:** [Code linkage + runtime](./ai-gateway-example/07-code-semantic-linkage.md), [EDR example](./ai-gateway-example/08-edr-example.md).
- **Instance Scheduler:** [Code linkage + runtime](./instance-scheduler-example/07-code-semantic-linkage.md), [EDR](./instance-scheduler-example/08-edr-example.md).

## Relationship to STE system

- **Conformance (artifacts):** [Conformance](../03-artifacts/03-07-conformance.md)
- **Kernel reasoning surface and evidence:** [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md), [Evidence](../03-artifacts/03-05-evidence.md)

**Previous:** [IR to projections](./04-ir-to-projections.md) · **Next:** [Drift and correction](./06-drift.md) · **Part 11 index:** [00-overview](./00-overview.md)
