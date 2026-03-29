---
title: "Part 5: Lifecycle States and Transitions"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Lifecycle states and transitions

**Lifecycle state** is how STE and the organization remember where a **scope** sits in its governance story: under design, building, under assessment, accepted for a purpose, under **exception**, retired, and so on. **Transitions** are the allowed moves between states, usually gated by **evidence**, **conformance**, and human approval.

## Purpose of this stage

Replace implicit status (known only in chat or ticket color) with **durable, queryable state** tied to artifacts. That makes parallel work, audits, and automation safer.

## Artifacts involved

Lifecycle state records (as defined by policy and **ste-spec**), links to **conformance** results and **evidence**, **ADR** or **governance** records that justify **exceptions**, and **Architecture IR** revisions that accompany major transitions. See [Lifecycle overview](../06-governance/06-00-lifecycle-overview.md) and [Design lifecycle](../06-governance/06-01-design-lifecycle.md).

## Human responsibility

Humans define or adopt the state machine that fits the organization, own approvals for sensitive transitions, and refuse to stamp “accepted” without **evidence** commensurate with risk.

## STE system responsibility

STE records current and historical state per **scope**, enforces allowed transitions when automation can, blocks illegal transitions, attaches mandatory artifacts to transitions, and exposes state in **projections** for operators and auditors.

## Transitions to the next stage

This chapter completes the staged walkthrough of Part 5. The operational loop continues: **change** drives new **evidence**, which drives new **assessment**, which drives new **governance** **decisions**. Read Part 6 for phase-by-phase control-loop mechanics and governance operations that align with these states.

## Relationship to intent, implementation, and evidence

- **Intent:** State often reflects whether **intent** for a **scope** is considered **stable**, **under revision**, or **superseded**.
- **Implementation:** **Embodiment** state (for example deployed versus deprecated) should align with recorded lifecycle state or explainable **exceptions**.
- **Evidence:** Transitions that matter for safety or compliance should cite **evidence** appropriate to the bar; weak **evidence** should not advance high-stakes states.

## Relationship to other chapters

- [Lifecycle overview](05-00-lifecycle-overview.md)
- [Control loop overview](../06-governance/06-07-control-loop-overview.md)
- [Lifecycle overview](../06-governance/06-00-lifecycle-overview.md)
- **ste-spec** for normative state names, transition guards, and interfaces.

**Next:** Return to the loop entry at [Intent formation](05-01-intent-formation.md) as needed, or continue to Part 7 [Kernel overview](../07-kernel/07-00-overview.md) for the reasoning surface, **Admission**, and **IR validation** depth.
