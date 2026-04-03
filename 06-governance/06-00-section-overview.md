---
title: "Part 6: Governance - Section overview"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-04-02"
---

# Part 6: Governance - section overview

**Governance** in STE is the **control structure that determines when the system may proceed**. It is not a paperwork stage beside engineering. It is part of the **operating model**: the structure that assigns **authority**, defines what counts as **admissible** evidence and architecture, bounds **decision rights**, and states when **execution** and change are allowed or blocked.

The core governance question is: **Given declared intent, current evidence, and active policy, is this system allowed to proceed?** Answering it ties together **intent** (ADRs, invariants, requirements), **Architecture IR**, **embodiment**, **evidence**, **rules** and organizational **policy**, and **Kernel** outcomes where **ste-spec** defines contracts.

## What governance controls in STE

- **Authority** — who or what may declare normative truth at each layer and what consumers must treat as binding; [Authority and decision rights](06-03-authority-and-decision-rights.md).
- **Admission** — whether a gated operation may be **attempted** under policy; [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).
- **Eligibility** — whether **prerequisites are satisfied right now** (coverage, freshness, validity, required artifacts); same chapter.
- **Enforcement** — what happens when admission or eligibility fails (block, deny, require remediation); same chapter.
- **Audit** — whether a later reviewer can reconstruct **what** was decided, **from which inputs**, **under which rules**, and **why**; [Determinism, provenance, and audit](06-06-determinism-provenance-and-audit.md).

## Part 5 to Part 8 (lifecycle, control, kernel, runtime)

[Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md) walks **stages** and artifacts in time order. **Part 6** states **when progress is allowed** against that backdrop: the control reading of the same story. [Kernel overview](../07-kernel/07-00-overview.md) is where **assessment** and **Admission** are mechanically defined where **ste-spec** applies; [Runtime overview](../08-runtime/08-00-runtime-overview.md) is where **embodiment** is observed and packaged into **evidence** that governance and the Kernel consume—not where organizational policy is invented.

This part explains the control model at handbook altitude. [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md) and [Architecture IR overview](../04-architecture-model/04-00-architecture-ir-overview.md) define **what** is recorded; Part 6 defines **how those records participate in proceed/stop decisions**.

## Why this matters

Without a clear governance model, teams default to two bad equilibria: **ungoverned assistance** (models and tools act without durable authority or evidence discipline), or **theater** (process and documents that do not constrain reasoning or execution). STE is built to avoid both by tying **intent**, **Architecture IR**, **evidence**, **Kernel** assessment, and human **accountability** into one explicit control story.

## Canonical, derived, and enforced (a legend for Part 6)

Read these terms consistently across Part 6 and the rest of the handbook:

| Category | Meaning in STE | Examples at handbook altitude |
|----------|----------------|------------------------------|
| **Canonical (for a layer)** | The durable, normative records that define what is **declared true** for that concern, under agreed scope and versioning. | **Intent artifacts** (**ADRs**, **invariants**, requirements, **constraints**) as normative records; **Architecture IR** as the **compiled canonical system model** for the architecture layer ([Architecture IR overview](../04-architecture-model/04-00-architecture-ir-overview.md)). |
| **Derived** | Machine- or human-facing views and payloads **computed from** canonical inputs or from **embodiment**, with lineage and freshness that can be checked. | Projections, many graph exports, registry bundles built for tools, packaged **evidence** from **Runtime** observation pipelines. Derived objects are **not** authoritative over **Architecture IR** or **intent**. |
| **Enforced** | Controls that **block, allow, or require** actions based on rules and machine-shaped outcomes, when policy and implementation attach to them. | **IR validation**, **Admission** and related **Kernel** outputs where **ste-spec** defines contracts; org policy gates on those outputs. Enforcement **depth is phased**: some paths are mature, others are still emerging ([Kernel and governance](../07-kernel/07-07-kernel-and-governance.md)). |

**Normative** in Part 6 names the same posture as **canonical (for a layer)**: declared commitments that bind assessment for that concern—not informal chat or unscoped summaries.

**Rules** (organizational or mechanical) **constrain** behavior and define **obligations**; they are **not** a substitute for the **architecture** as declared in **intent** and **Architecture IR**. See [Authority and decision rights](06-03-authority-and-decision-rights.md) and [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).

## Maturity: doctrine versus phased realization

The **governance doctrine** in STE (authority split, canonical versus derived, deterministic assessment at the Kernel boundary, Runtime as evidence producer) is **stable enough to build on** and aligns with the public **ste-spec** handoff boundary described in **ste-spec** `status.md`.

**Mechanical governance** (unified enforcement across CI, IDE, lifecycle, and conversation surfaces) is **phased**. Where implementation is still catching up, this part states that explicitly instead of implying a finished control plane. Deep policy-as-code and analytics belong with [Policy and governance (advanced)](../13-advanced-topics/13-07-policy-and-governance.md).

## Reading order (Part 6)

1. [Why governance exists](06-01-why-governance-exists.md) — failure modes when AI participates at scale; control versus compliance.
2. [The governance model](06-02-the-governance-model.md) — operational control; before, during, and after execution.
3. [Authority and decision rights](06-03-authority-and-decision-rights.md) — canonical artifacts, Kernel versus Runtime, humans and AI at the boundary.
4. [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md) — preconditions, gates, posture versus full behavioral governance, invariants versus rules versus obligations.
5. [Steelman, obligations, and change control](06-05-steelman-obligations-and-change-control.md) — formal challenge function, ADR closure, implementation discipline.
6. [Determinism, provenance, and audit](06-06-determinism-provenance-and-audit.md) — repeatable decisions, evidence lineage, auditability.

## Relationship to other handbook parts

- **Architecture IR:** [Architecture IR overview](../04-architecture-model/04-00-architecture-ir-overview.md) defines the canonical structural model; governance explains why that model must exist for control to be real.
- **Kernel:** [Kernel overview](../07-kernel/07-00-overview.md), [Determinism and fail-closed](../07-kernel/07-06-determinism-and-fail-closed.md), [Kernel and governance](../07-kernel/07-07-kernel-and-governance.md).
- **Runtime:** [Runtime overview](../08-runtime/08-00-runtime-overview.md), [Governance signals and semantic graph lifecycle](../08-runtime/08-07-governance-signals-and-semantic-graph-lifecycle.md).
- **Rules and AI interface:** [Rule activation](../10-ai-interface/10-02-rule-activation.md); [Agents](../10-ai-interface/10-01-agents.md).
- **Conversation and ADR capture:** [Steelman](../09-human-interface/09-04-steelman.md), [Decision capture](../09-human-interface/09-03-decision-capture.md), [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md).
- **Foundations:** [Governed reasoning](../00-problem/00-05-governed-reasoning.md), [System overview](../02-overview/02-03-system-overview.md).

**Next:** [Why governance exists](06-01-why-governance-exists.md).
