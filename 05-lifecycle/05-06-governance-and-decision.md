---
title: "Part 5: Governance and Decision"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Governance and decision

**Governance** turns **assessment** outcomes into legitimate system states: what may ship, what must stop, what **exceptions** exist, and who owns the follow-up. **Decisions** here include certification, acceptance, prioritization of remediation, and escalation when **intent** must change.

## Purpose of this stage

Ensure that transitions in risk and quality are **owned**, **recorded**, and **reviewable**. Without this stage, **conformance** becomes noise and **drift** becomes nobody’s problem.

## Artifacts involved

Decision records (often **ADR**-shaped updates or addenda), approval artifacts, **exception** packages with **scope** and expiry where policy requires, lifecycle state transitions, and links to the **evidence** and **conformance** records that justified the call. See [Governance](../06-governance/06-06-governance.md) and [Certification](../06-governance/06-05-certification.md).

## Human responsibility

Accountable roles accept or reject releases and milestones, grant or deny **exceptions**, set organizational **rules**, assign owners for remediation, and decide when strategy requires **intent** revision rather than patch-level fixes.

## STE system responsibility

STE enforces policy gates where automated, records decisions and state transitions immutably when configured, routes work items or blocking signals to the right owners, and preserves an audit-friendly trail from **evidence** to decision.

## Transitions to the next stage

Authorized work enters **change and evolution**: updates to **intent**, **Architecture IR**, **embodiment**, or all three, according to the decision. If the decision is “hold,” the system may remain in a monitoring posture but still accumulates new **evidence**.

**Next stage chapter:** [Change and evolution](05-07-change-and-evolution.md).

## Relationship to intent, implementation, and evidence

- **Intent:** **Governance** may require revising **intent** when **assessment** shows the old bar is wrong, not only when code is wrong.
- **Implementation:** Decisions authorize or block **implementation** **change** and operational actions.
- **Evidence:** Legitimate decisions cite **evidence** and **conformance** results rather than replacing them with narrative alone.

## Relationship to other chapters

- [Governed reasoning](../00-problem/00-05-governed-reasoning.md)
- [Decision to change](../06-governance/06-13-decision-to-change.md)
- [Continuous certification](../06-governance/06-14-continuous-certification.md)
- **ste-spec** for policy interfaces and lifecycle hooks.

**Next:** [Change and evolution](05-07-change-and-evolution.md).
