---
title: "Stakeholder views"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-26"
---

# Stakeholder views

## The Problem

Different stakeholders **legitimately** need different pictures: **compliance** wants control flow and data residency; product wants capability maps; SRE wants deployment and failure domains. The failure mode is each group maintaining **private** diagrams that **contradict** each other. STE serves stakeholders by **tailoring projections** from **Architecture IR**, not by fragmenting **canonical** structure.

## The Reframe

A **stakeholder view** is an **architecture view** (a **projection** package) whose **selection**, **notation**, and **narrative** target a specific role’s **decisions**. The **underlying identities** remain IR-stable so **traceability** and **evidence** **scopes** do not fork by audience.

## The Model

### Audience and obligations

Name the **stakeholder**, their **decisions**, and the **obligations** they must see: which **constraints**, which **invariants**, which **interfaces**. The projection should make omissions **visible** (“out of scope for this sheet”) rather than silent.

### Abstraction level

Executives need aggregates; engineers need interfaces and dependencies. Both should **trace** to the same IR nodes—abstraction is **filtering** and **rollup**, not a second naming scheme.

### Evidence hooks

Stakeholder views can embed **evidence** pointers: which checks cover this boundary, which monitors watch this data path. That binds **assessment** stories to structure without duplicating **evidence** records ([Evidence](../03-artifacts/03-05-evidence.md)).

### Governance participation

Reviews invite the right **stakeholder** **views** as **artifacts** in the **governance** record: “we approved IR vNN with security view SV-12.” That beats approving a slide nobody can tie to a graph.

## The Implications

Resist “views for politics” that hide uncomfortable edges. **Governed reasoning** requires **honest** slices; **redaction** may exist for **confidentiality**, but **structure** behind redaction should still **conform** to IR within cleared **scopes**.

## Relationship to STE system

- **Architecture views:** [Architecture views](04-12-architecture-views.md).
- **Projection documents:** [Projection documents](04-11-projection-documents.md).
- **Lifecycle / governance:** [Governance and decision](../05-lifecycle/05-06-governance-and-decision.md), [Governance](../06-governance/06-06-governance.md).

## Summary

- **Stakeholder views** tailor **projections** without forking **canonical** **Architecture IR**.
- **Abstraction** is **rollup** and **filter**, not renamed reality.
- Tie **views** to **governance** events with **IR** **provenance**.

**Next:** [View consistency](04-14-view-consistency.md).
