---
title: "Admission, eligibility, and enforcement"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-04-02"
---

# Admission, eligibility, and enforcement

## Why this matters

Gated work—merge, release, promoted infra, expensive or autonomous change—needs **preconditions** that can be checked, not habits. If **eligibility** is **assumed** instead of **assessed**, **admission** collapses into theater. Lifecycle context for **conformance** and **change** sits in Part 5 ([Conformance and assessment](../05-lifecycle/05-05-conformance-and-assessment.md), [Change and evolution](../05-lifecycle/05-07-change-and-evolution.md)); this chapter is the **control** reading of those gates.

## Admission, eligibility, and enforcement (definitions)

- **Admission** — Under policy, is the system **allowed to attempt** this gated operation (merge, release, promotion, high-risk automation, and similar)? Admission is about **permission to try**, not “everything is fine.”
- **Eligibility** — **Right now**, are the **prerequisites satisfied**: architecture declaration and **Architecture IR** coverage for the risk class, **evidence** scoped and valid, **rules** and **obligations** met, freshness and provenance adequate for the decision?
- **Enforcement** — If admission or eligibility fails, what **happens next**: block, deny, require remediation, or route to human owners as policy defines?

The core governance question—intent, evidence, policy, and **proceed**—is stated in [Section overview](06-00-section-overview.md). **Kernel**-shaped outcomes for mechanical parts of admission and eligibility live in Part 7 ([Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md), [Determinism and fail-closed](../07-kernel/07-06-determinism-and-fail-closed.md), [Kernel and governance](../07-kernel/07-07-kernel-and-governance.md)); human governance still owns judgment-shaped regions policy and **ste-spec** reserve.

## The problem

Teams often treat “we have some ADRs” or “we ran tests” as sufficient. STE asks a sharper question: for **this** change, **this** scope, and **this** moment, is the **architecture declaration** complete enough, the **evidence** valid and fresh enough, and the **rules** satisfied for the gate you are trying to pass?

## No execution without sufficient architecture and evidence

**Execution** here means any materially risky step policy attaches to: shipping, merging to protected branches, promoting infra, or running autonomous change at scale. STE’s posture is: **do not pretend** those steps are governed if inputs are missing, stale, or out of scope.

**Sufficient architecture** means **Architecture IR** and **intent** coverage appropriate to the risk class and **ste-spec** contracts in play, not a fixed document count.

**Sufficient evidence** means observations are **scoped**, **provenanced**, and **valid** for the claims under test ([Evidence](../03-artifacts/03-05-evidence.md), [Runtime overview](../08-runtime/08-00-runtime-overview.md), [Freshness and validity](../08-runtime/08-03-freshness-and-validity.md)).

## Eligibility inputs: freshness, validity, and provenance

These properties support **eligibility** (prerequisites **now**), not a vague “we tried”:

- **Freshness:** evidence and projections must be **current enough** for the decision. Stale graphs and stale test bundles are common sources of false confidence.
- **Validity:** payloads must satisfy contract and schema expectations; broken tool output is not neutral, it is **ineligible** input.
- **Provenance:** consumers must see **where** a payload came from, **what** IR or embodiment snapshot it reflects, and **which** toolchain version produced it. Full **audit** reconstruction—what was decided, from which artifacts, under which rules, with which evidence, and why—is the focus of [Determinism, provenance, and audit](06-06-determinism-provenance-and-audit.md).

## Eligibility is assessed, not assumed

**Eligibility** is a **verdict** supported by checks, not an attitude. Mechanical parts surface through **Kernel**-shaped outcomes where defined; humans own policy interpretation where contracts do not close the question ([Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md)).

## Policy, posture, and enforcement

Distinguish:

- **Policy:** the organization’s declared bars, scopes, exceptions culture, and risk ownership. Policy can exist in prose, config, and code.
- **Posture:** what is **actually enforced mechanically today** versus what is **advisory** or manual. Posture changes as tooling matures.
- **Full behavioral governance:** sustained, inspectable enforcement across the surfaces where work happens (CI, pre-merge, IDE, lifecycle transitions). STE aims here; it is **not** claimed as uniformly complete yet ([Kernel and governance](../07-kernel/07-07-kernel-and-governance.md)).

**Phase-gated realization** means later phases add **depth** without rewriting the authority story. Early phases may emphasize **IR validation** and a narrow **Admission** slice; later phases widen **lifecycle** hooks and **conversation** integration.

## Fail-closed semantics

Where inputs required for a decision are missing or ambiguous, STE prefers **deny** or **block** over silent acceptance ([Determinism and fail-closed](../07-kernel/07-06-determinism-and-fail-closed.md)). **Fail-closed** behavior is how governance avoids “unknown means OK.”

## Deterministic controls and the LLM boundary

Where **ste-spec** defines assessment and **Admission** semantics, the **Kernel** must be **deterministic** for those outcomes; probabilistic models must not **be** that **decision core** ([Determinism and fail-closed](../07-kernel/07-06-determinism-and-fail-closed.md)). The boundary between **determinism** (where required) and **provenance** (everywhere traceability is needed) is developed in [Determinism, provenance, and audit](06-06-determinism-provenance-and-audit.md).

## Invariants, rules, and obligations (crisp distinctions)

These terms overlap in ordinary speech. In STE they split cleanly:

| Term | Role | Notes |
|------|------|--------|
| **Invariant** | A **must-hold** architectural truth in **intent**, checkable against **embodiment** under scope. | Hard **intent**; changing one is a high-signal governance act ([Invariants](../03-artifacts/03-03-invariants.md)). |
| **Rule** | A **constraint** or check, mechanical or procedural, that enforces expectations on records or behavior. | Rules **encode** policy fragments; they are **not** the architecture graph. |
| **Obligation** | What a gate or process **must demonstrate** or **satisfy** to proceed (evidence types, reviews, tool passes). | Obligations **instantiate** policy for a specific transition; they bridge **intent** to **enforcement**. |

Obligations can reference **invariants** and **rules** without collapsing the categories. **Steelman** and change control tie to obligations in [Steelman, obligations, and change control](06-05-steelman-obligations-and-change-control.md).

## Relationship to other chapters

- [Authority and decision rights](06-03-authority-and-decision-rights.md)
- [The governance model](06-02-the-governance-model.md)
- [Steelman, obligations, and change control](06-05-steelman-obligations-and-change-control.md)
- [Conformance and assessment](../05-lifecycle/05-05-conformance-and-assessment.md)

**Next:** [Steelman, obligations, and change control](06-05-steelman-obligations-and-change-control.md).
