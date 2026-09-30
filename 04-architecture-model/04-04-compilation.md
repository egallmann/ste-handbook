---
title: "Compilation and semantic materialization"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-09-30"
---

# Compilation and semantic materialization

## The Problem

If **Architecture IR** is edited by hand like a wiki, it becomes another document that **drifts** from **intent**. If every tool infers architecture independently, there is no **canonical** machine model. If “compile” is used as one vague verb for construct, persist, admit, promote, and conform, teams cannot tell which boundary failed when meaning goes wrong.

The older handbook story of a simple intent→structural-IR transform is no longer enough. Governed semantics—including Normative Propositions—must be constructible and validatable without inventing authority, applicability, or completed IR mapping by accident.

## The Reframe

**Compilation**, in STE handbook usage, names the disciplined bridge from governed architecture sources toward the canonical machine-oriented architecture model—not the programming-language sense alone. Modern toolchains also distinguish **authoring construction**, **qualification against an exact semantic basis**, **interpretation and validation**, **normalized semantic representation**, **materialization**, and **governed mapping or integration** into Architecture IR where applicable.

These are conceptual responsibilities. Implementations may combine or sequence them differently. Part 4 preserves the boundaries even when a product pipeline is integrated end-to-end.

## The Model

### Conceptual stages

```text
governed authoring intent
        ↓
candidate construction
        ↓
qualification / exact semantic basis
        ↓
interpretation / validation
        ↓
normalized semantic representation
        ↓
governed mapping / integration where applicable
        ↓
Architecture IR / downstream semantic consumers
```

Collapse stages only when authoritative contracts define them as one operation.

**Normalized semantic representation ≠ Architecture IR** unless accepted ste-spec establishes that mapping. Product normalized models demonstrate that Decision, Invariant, NormativeProposition, and related semantics can be represented and addressed; they do not automatically become compiled Architecture IR kinds or identity schemes.

### Construction (detached candidates)

**Authoring construction** may build schema- and contract-governed **candidate** semantic state: for example a candidate authoring document or fragment with established identity where contracts authorize it. Successful construction returns **detached** candidate results validated against an **exact semantic basis**.

Construction does **not** by itself:

- persist repository source;
- reserve aliases;
- admit repository architecture;
- perform governance acceptance or promotion;
- admit architecture into a Runtime graph;
- mutate a Runtime Snapshot;
- establish implementation conformance.

Compact authoring input is **semantic compression** of contract-declared ceremony. It is **not** permission to infer material architectural intent. Tooling must not invent missing decisions, rationales, relationships, Normative Propositions, applicability, materiality, or other undeclared meaning from compact input or from arbitrary modal prose.

### Exact semantic basis and qualification

Consumers must know **which** contracts and artifacts they are allowed to interpret—not an ambient “latest.” Exact qualification is not preferred-or-supported status by itself, and not authority-by-recency. Supported ≠ preferred; preferred ≠ current unless a contract defines them that way; available ≠ default; released ≠ promoted-current; successor ≠ current.

Unknown contracts, incompatible semantic bases, invalid shapes, unresolved authority, invalid relationships, and whole-result violations required by contracts should **fail visibly**.

### Interpretation, validation, and normalization

Interpretation and validation check candidate or sealed inputs against the exact basis. Deterministic machinery may validate structure and contract semantics. It **must not** claim competent semantic judgment it does not possess: it must not certify semantic materiality or assert meaning-preserving identity continuity where contracts assign those judgments to competent review.

Normalization produces machine-facing semantic surfaces under those contracts. **Normalization ≠ applicability.** **Semantic normalization ≠ Runtime graph admission.**

### Materialization

**Materialization** produces materialized machine-facing semantics from a sealed complete basis under declared qualification. Materialization does **not** create authority, governance acceptance, applicability, or conformance. It does not mint declaring authority by reading or including a Normative Proposition.

### Mapping toward Architecture IR

Where ste-spec and adapters define governed mapping or integration, normalized or authored semantics may realize onto Architecture IR and related consumer surfaces. Where mapping is incomplete or deferred—including NormativeProposition compiled `kind` and CE-01 identity unification—handbook prose must not invent completion. Downstream consumers may still use normalized surfaces as embodiment evidence without renaming them Architecture IR.

### Errors and governance

Failures are **governance signals**: missing links, contradictory constraints, unknown identities, invalid NP shape, unresolved declaring authority. Teams choose whether failures block merge, warn, or route to exception workflows. The important shift is from hidden inconsistency to **accountable** outcomes ([Governed reasoning](../00-problem/00-05-governed-reasoning.md)).

### Relationship to admission and promotion

**Admission** (Part 7 and Runtime stories) may consume compiled or integrated model state plus **evidence** and contracts to decide what may progress. **Governance promotion** is a separate legitimacy act. This chapter stops at the model-build and materialization story; construction and materialization are not admission, and not promotion.

## The Implications

Treat construction and materialization as part of the engineering **supply chain**. Changes to **intent** without re-running the governed bridge produce **drift** between what **governance** approved and what machine surfaces claim. Automation makes **projections** and checks trustworthy; skipping it trades speed for unreviewable semantics.

Do not predict unreleased package promotion from the existence of successor contracts. Describe implemented and accepted architecture honestly; keep supported, executable, public, released, preferred, current, and default states distinct.

## Relationship to STE system

- **Model concepts:** [Architecture model (Architecture IR) overview](04-00-architecture-ir-overview.md), [Entities](04-02-entities.md), [Relationships](04-03-relationships.md).
- **Artifact overview:** [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md).
- **Terminology:** [Terminology](../02-overview/02-02-terminology.md) (**compilation** sense).
- **Lifecycle:** [Architecture definition](../05-lifecycle/05-02-architecture-definition.md).
- **Kernel:** [Kernel overview](../07-kernel/07-00-overview.md), [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).

## Summary

- **Compilation and semantic materialization** name the bridge from governed sources toward machine-facing architecture semantics and, where mapped, **Architecture IR**.
- **Construction**, **normalization**, **materialization**, **persistence**, **admission**, **promotion**, and **conformance** are distinct.
- Compact input does not authorize inventing material intent; mechanical validation does not replace competent semantic review where contracts require it.
- Normalized product surfaces are not automatically Architecture IR; exact contract qualification is not ambient latest.

**Next:** [Traceability in Architecture IR](04-05-traceability.md).
