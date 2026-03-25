---
title: "Part 5: Conformance and Assessment"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Conformance and assessment

**Assessment** compares **embodiment** (via **evidence**) to declared **intent** and **Architecture IR** under explicit **rules** for a stated **scope**. **Conformance** is the property those checks address: alignment within the defined bar, with recorded outcomes.

## Purpose of this stage

Turn “does it match what we said?” into inspectable results: mechanical checks where possible, documented human judgment where necessary, always tied to artifacts rather than private opinion.

## Artifacts involved

**Conformance** results, assessment reports, rule definitions, and links from findings back to **intent**, IR elements, and **evidence**. The **Kernel** role in STE orchestrates much of this machinery in implementations. See [Conformance](../03-artifact-layer/03-07-conformance.md), [Validation](../06-kernel/06-03-validation.md), and [Deterministic assessment](../06-kernel/06-08-deterministic-assessment.md).

## Human responsibility

Humans own the **rules** and thresholds that automation enforces, adjudicate edge cases, decide when judgment-shaped review replaces or supplements mechanical checks, and accept accountability for waivers or **exceptions** where policy allows.

## STE system responsibility

STE runs configured checks, aggregates **evidence**, records **conformance** outcomes with pointers to inputs, highlights **drift** and non-conformance, and prevents silent erasure of failed assessments where immutability policy applies.

## Transitions to the next stage

When **assessment** surfaces material gaps or when **conformance** passes at a bar that **governance** cares about, the process moves to **governance and decision**: accept, reject, defer, or demand **change**. Return to this stage whenever **embodiment** or **intent** moves enough to invalidate prior results.

**Next stage chapter:** [Governance and decision](05-06-governance-and-decision.md).

## Relationship to intent, implementation, and evidence

- **Intent:** **Conformance** is meaningless without declared **intent** and structural commitments; the **rules** instantiate those commitments.
- **Implementation:** **Embodiment** supplies the behavior that **evidence** captures; **assessment** closes the loop from **implementation** reality back to claims.
- **Evidence:** **Assessment** consumes **evidence** as its primary input alongside the normative artifacts.

## Relationship to other chapters

- [Terminology](../02-overview/02-02-terminology.md) (**validation** sense)
- [Assessment to decision](../07-control-loop/07-05-assessment-to-decision.md)
- [Divergence](../06-kernel/06-04-divergence.md)
- **ste-spec** for assessment interfaces and result shapes.

**Next:** [Governance and decision](05-06-governance-and-decision.md).
