---
title: "Authority and decision rights"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-04-02"
---

# Authority and decision rights

## Why this matters

When authority is vague, tools and models fill the gap. **Governance** in STE **structures** authority so AI can **assist** and **challenge** without **silently redefining** what is true, admissible, or binding.

## Authority by layer

**Artifacts are canonical at their layer**: normative records for that concern, under agreed scope and versioning. The same idea is tabulated in the [section overview](06-00-section-overview.md); here the map is by **layer**.

### Intent layer

**Intent artifacts** (**ADRs**, **invariants**, requirements, **constraints**) are the **canonical normative records** for what the organization declares about decisions, must-hold properties, and obligations at the **intent layer**.

### IR / architecture model layer

**Architecture IR** is the **canonical compiled system model** for the **architecture layer** for an agreed scope: the machine-addressable graph of **entities** and **relationships** produced under **compilation** rules ([Architecture IR overview](../04-architecture-model/04-00-architecture-ir-overview.md), [Compilation](../04-architecture-model/04-04-compilation.md)). **Compilation** turns structured **intent** into **Architecture IR** under explicit rules. That makes IR **compiled authority** for structure: the object **queries**, **diffs**, and **admission** consume when contracts refer to architecture.

Narrative documents and diagrams **project** or **explain** IR; they do not supersede it. Projections, wiki pages, and assistant-generated summaries can **lag** or **drift** from IR. Governance treats them as **second-class** relative to IR for structural truth unless explicitly adopted through the **intent** pipeline.

### Evidence layer

**Runtime** observes **embodiment** and packages **evidence** and **governance signals** ([Runtime overview](../08-runtime/08-00-runtime-overview.md), [Governance signals and semantic graph lifecycle](../08-runtime/08-07-governance-signals-and-semantic-graph-lifecycle.md)). For their scope, evidence artifacts are **canonical as records of observation**—they **inform** assessment and human process. They do **not** replace **Architecture IR** or **intent**.

**Exports** (dependency graphs, semantic graphs, registry bundles) built from IR, embodiment, or tool heuristics are **derived**; they may be operationally essential but are **not** a second canonical architecture.

### Kernel decision authority (contract-shaped)

The **Kernel** role emits **deterministic**, **machine-readable** outcomes for the reasoning surface (**Query**, **Explain**, **Coverage**, **Admission**) where **ste-spec** defines the contracts ([Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md)). For **Admission**, that means **Kernel-shaped decisions** over declared inputs, not narrative opinion.

The Kernel is **not** the owner of business policy tradeoffs that specs intentionally leave to humans. It **implements** **assessment** and **admission** semantics, not **organizational mission** judgment.

## Chat and views are not structural authority

**Chat** and informal conversation are **not** authority: they may **draft** or **discuss**, but they do not replace **intent** records, **Architecture IR**, or **Kernel**-shaped **Admission** where contracts apply. **Graphs** and **views** are **derived** unless the organization explicitly adopts them through the **intent** / **IR** pipeline.

## Authority at a glance

| Layer | Canonical at this layer | Who / what decides | Typical mistake |
|-------|-------------------------|--------------------|-----------------|
| **Intent** | ADRs, invariants, requirements, constraints | Humans (owners, review) as policy defines | Treating chat or a summary as the decision record |
| **Architecture IR** | Compiled graph for agreed scope | **Compilation** rules from structured intent; human policy on scope | Letting diagrams or tool exports override IR |
| **Evidence** | Scoped, provenanced observation payloads | **Runtime** / pipelines that package **embodiment**; humans on interpretation at policy edges | Stale or unscoped bundles passed as “proof” |
| **Kernel (contracts)** | Deterministic outcomes where **ste-spec** applies | **Kernel** logic over declared inputs; humans where specs reserve judgment | Asking an LLM to “be” **Admission** when contracts require determinism |

## Runtime: evidence producer, not policy authority

**Runtime** observes, classifies, packages, and signals. It does **not** stand in for **governance** approval or **Kernel** **Admission** semantics. Framing Runtime as “the policy engine” would invert STE’s authority map.

## Rules: constraints and obligations, not architecture

**Rules** (checks, linters, policy packs, prompts that activate checks) express **constraints** and **obligations**: what must be shown, what fails a gate, what must hold before a tool proceeds ([Rule activation](../10-ai-interface/10-02-rule-activation.md)). How **invariants**, **rules**, and **obligations** differ at gates is centralized in [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).

**Rules** do **not** replace **Architecture IR** or **intent**. A rule can require that an invariant is recorded; it does not **become** the invariant.

## Human role in governance

Humans remain **decision owners** at boundaries **ste-spec** and policy reserve: prioritization, exceptions with accountability, acceptance of ambiguous tradeoffs, and revision of **intent** when reality demands it. **Governance** does not remove humans; it **routes** authority so automation does not smuggle choices past owners.

AI may **draft**, **interrogate**, and **surface** gaps; it must not **overwrite** canonical records or **pretend** admission without **Kernel**-shaped outcomes where contracts apply ([Agents](../10-ai-interface/10-01-agents.md)).

## Relationship to other chapters

- [Section overview](06-00-section-overview.md)
- [The governance model](06-02-the-governance-model.md)
- [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md)
- [Kernel and governance](../07-kernel/07-07-kernel-and-governance.md)

**Next:** [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).
