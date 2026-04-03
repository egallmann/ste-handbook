---
title: "Determinism and fail-closed"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# Determinism and fail-closed

## The Problem

If architecture gates drift with mood, reviewer fatigue, or non-repeatable assistant behavior, organizations cannot audit **why** a change was allowed. **Determinism** is not pedantry; it is the precondition for trustworthy automation and **governance**.

## The Reframe

The **Kernel role** is a **decision engine**, not a brainstorming partner. Its outputs must be **deterministic decisions** under fixed policy: the same inputs yield the same results. Where inputs are incomplete, STE prefers **fail-closed** behavior—**deny** or **block**—over silent acceptance.

## The Model

### Rules (explicit)

1. **Input equality → decision equality.** The same **Architecture IR** (including the same validated **Compiled IR Document** identity and content under **ste-spec** rules), the same **Evidence** (including the same **ArchitectureEvidence** payloads where used), the same **change proposal**, and the same **governance rules** and **lifecycle state** in scope → the same **deterministic decision**.
2. **Missing required information → deny or block.** Unknowns are not treated as benign defaults. This is **fail-closed** behavior at the Kernel boundary.
3. **Machine-readable outcomes.** Decisions must serialize into contract-shaped artifacts (for example **KernelAdmissionAssessment** for **Admission** where **ste-spec** defines it).
4. **Automatable outcomes.** Downstream CI, IDE, and policy engines must be able to act on Kernel outputs without re-interpretation through natural language.
5. **No probabilistic decision core.** The Kernel role **must not** depend on **probabilistic reasoning** (including large language models) to determine **Admission**, **Coverage**, or **Explain** truth. Stochastic tools may **author** inputs or **draft** proposals; they do not define the **decision core**.

### Evidence posture

**Evidence** (including **ArchitectureEvidence**) is **non-decision-bearing** at the handoff until the Kernel role evaluates it. That separation preserves auditability: observations are facts; **Admission** is a decision.

### Relationship to IR validation

**IR validation** is deterministic mechanical checking of **Architecture IR** artifacts under **ste-spec**. It supports determinism but does not replace **Admission** semantics.

## The Implications

- Teams should version policy inputs alongside **Architecture IR** inputs when claiming reproducibility.
- Any nondeterminism introduced by infrastructure (timestamps, flaky fetches) must be bounded or eliminated at the integration boundary if it affects decisions.

## Relationship to STE system

- Foundations: [Deterministic versus stochastic systems](../00-problem/00-06-deterministic-vs-stochastic-systems.md).
- Reasoning surface: [Kernel reasoning surface](07-05-kernel-reasoning-surface.md).
- Governance model: [The governance model](../06-governance/06-02-the-governance-model.md).

## Summary

- **Deterministic decisions** and **fail-closed** behavior make **Admission** and related outputs auditable.
- Kernel outcomes must be **machine-readable** and **automatable**; the **decision core** excludes **probabilistic reasoning**.
- **Evidence** informs decisions but is not itself a decision until evaluated by the **Kernel role**.
