---
title: "Part 11: Drift and correction"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# Drift and correction

**Drift** is **divergence** between what the organization **committed to** (intent and design), what the **compiled model** says, what **actually runs**, and what **evidence** shows—when that divergence is **not** covered by a governed exception. Drift can appear at **multiple layers** at once: requirements out of date versus conversation, ADRs out of date versus requirements, IR or projections stale versus ADRs, runtime changed without revising design, or observed behavior inconsistent with stated controls.

## Evidence and EDR

**EDR**-shaped **evidence** (and related structured observations) records **what happened** in operational reality: a concrete basis for assessment instead of architecture folklore. Drift detection uses such evidence together with **linkage** back to IR and ADRs so findings are **actionable** and **traceable**.

## Correction must be governed

**Correction** is not “silent rerouting.” It flows back through **governed change**: revisiting **intent**, **requirements**, the **decision ledger**, and **ADRs** as needed; **recompiling** **Architecture IR**; **regenerating** **projections**; updating **runtime** and **linkage**; and recording new **evidence**. That loop is what makes STE a **lifecycle** system rather than a one-off documentation exercise.

Part 11’s closing steps show a **pedagogical** drift scenario and a **governed** path back toward alignment; organizational policy fills in approvals, ownership, and tooling.

## Where the examples show this

- **AI Gateway:** [Drift and correction](./ai-gateway-example/09-drift-and-correction.md)
- **Instance Scheduler:** [Drift and correction](./instance-scheduler-example/09-drift-and-correction.md)

## Relationship to STE system

- **Governance model (drift in the loop):** [The governance model](../06-governance/06-02-the-governance-model.md)
- **Lifecycle:** [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md)
- **Part 11 entry:** [STE examples overview](./00-overview.md)

**Previous:** [Conformance](./05-conformance.md) · **Next (walkthroughs):** [AI Gateway — conversation](./ai-gateway-example/00-ste-conversation.md) or [00-overview](./00-overview.md) for full maps · **Part 11 index:** [00-overview](./00-overview.md)
