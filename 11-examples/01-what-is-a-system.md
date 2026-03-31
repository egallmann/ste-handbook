---
title: "Part 11: What is a system?"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# What is a system?

In everyday language, a “system” is often **only** what is deployed: services, networks, data stores, schedules. In STE, that slice is necessary but not sufficient. A **system** is the **whole governed object** you reason about over time: the thread from **intent** through **design** and **compilation** to **embodiment**, **evidence**, and **operational history**.

## What a system includes

Taken together, a system in STE terms spans:

- **Intent** — what the organization wants, bounded by dialogue and discovery.
- **Requirements** — frozen, traceable expectations (capabilities, constraints, invariants, NFRs) that anchor design.
- **Decisions** — explicit questions and resolutions (including a **decision ledger** that bounds the design space before ADRs commit).
- **Design** — **ADR-L**, **ADR-PS**, and **ADR-PC** records: canonical architectural authority for this scope.
- **Compiled model** — **Architecture IR**: a derived, normalized graph of entities, relationships, and trace links (not a second informal design).
- **Runtime embodiment** — what is actually built, configured, and running (repos, infrastructure, APIs, jobs).
- **Evidence** — structured observation of behavior and posture (**EDR**-shaped records, tests, telemetry), linked back to intent and IR where policy requires it.
- **Operational history** — how the system changed under governance: assessments, drift findings, corrections, and revisions to upstream artifacts.

Part 11’s walkthroughs **show** these pieces in file-sized steps; this chapter names the whole so those steps snap into one mental model.

## Four useful distinctions

These are **views of the same system**, not four unrelated things. They diverge when governance or tooling fails—**drift** is that divergence made inspectable.

| View | What it is |
|------|------------|
| **Designed system** | What **ADRs** (plus requirements and ledger) **say** the architecture is: capabilities, topology, components, interfaces, and obligations. |
| **Compiled system model** | The **Architecture IR** snapshot: machine-consumable structure and traceability **derived** from canonical design inputs and rules-linked compilation. |
| **Running system** | **Embodiment**: actual resources, code paths, and integrations in environments. |
| **Observed system** | What **evidence** shows the running system **did** or **exhibited**: assessments, EDRs, conformance outcomes, operational signals. |

**Drift** appears when any of these views **disagree** without a governed exception: design says one topology, IR or projections lag a design change, runtime differs from IR or ADRs, or observed behavior contradicts stated controls. Part 11 closes with **drift detection** and **governed correction** so the loop returns to **intent** and **ADRs**, then through **IR** and **runtime** again.

## Relationship to STE system

- **Artifact layer:** [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md)
- **Lifecycle and loop:** [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md)
- **Part 11 entry and walkthrough maps:** [STE examples overview](./00-overview.md)

**Next:** [Conversation to ADR](./02-conversation-to-adr.md) · **Part 11 index:** [00-overview](./00-overview.md)
