---
title: "Determinism, provenance, and audit"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-04-02"
---

# Determinism, provenance, and audit

## Why this matters

**Governance** must support **audit**: a later reviewer should reconstruct decisions without relying on memory or model reruns. That requires **determinism** where **ste-spec** promises it for the **Kernel** decision core, and **provenance** everywhere else honesty demands traceability.

## Determinism where specs require it

For **Kernel**-shaped outcomes covered by **ste-spec**, **determinism** is a **design requirement**: same **Architecture IR** identity and content, same **evidence** payloads, same **change proposal** and policy inputs in scope → same **decision** ([Determinism and fail-closed](../07-kernel/07-06-determinism-and-fail-closed.md)).

Determinism is **not** claimed for creative drafting, exploratory chat, or heuristic assistants. It **is** claimed for the **decision core** that gates **Admission** where contracts apply.

## Provenance where determinism is not the contract

**Provenance** is the default expectation for payloads and records that must be **inspectable** when specs do not pin a deterministic **Kernel** outcome: **evidence** packaging, projections, human decisions recorded as artifacts, and toolchain outputs that feed **eligibility**. Consumers should be able to see **which** embodiment snapshot, **which** tool versions, **which** IR revision, and **which** scope label produced a payload ([Evidence and observation](../08-runtime/08-02-evidence-and-observation.md)). **Freshness**, **validity**, and lineage as **eligibility** inputs are covered in [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).

**Decisions** should link to the **Kernel** or human records that justified them, not only narrative summaries. **Admission** artifacts exist precisely to make that link **machine-stable** where **ste-spec** defines them.

## Replayability and explainability

**Replay** (re-running checks on the same inputs) and **explain** (structured narratives of why a verdict followed) are complementary. Replay supports **automation**; explain supports **human sensemaking** ([Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md)).

**Explain** must not smuggle nondeterministic judgment into places specs mark **deterministic**. When ambiguity remains, **governance** should route to **human owners** rather than fabricating certainty.

## Audit as a first-class governance outcome

**Enforcement** stops bad progress. **Audit** lets organizations **learn** after incidents and defend **proceed/stop** later. A reviewer should be able to reconstruct:

- **What** was decided (verdict, gate outcome, or human acceptance).
- **From which artifacts** (intent records, **Architecture IR** revision, **evidence** payloads, change proposal).
- **Under which rules** and **policy** (obligations, org bars, **ste-spec** contracts in play).
- **With which evidence** (scoped, provenanced payloads tied to **embodiment** and IR snapshots).
- **Why** the decision followed (**Explain** and linked rationale where specs allow; human records where judgment is reserved—not LLM reruns as authority).

STE’s artifact split (**intent**, **Architecture IR**, **evidence**, **Kernel** outputs) exists to make that comparison **possible**.

## Governance supports audit, not only enforcement

Wire formats and contract families evolve; **ste-spec** `status.md` marks which bridges are **stable** versus **draft** (for example some **governance-decision-record** and **rule-projection** work). This chapter stays at **handbook altitude**: audit is a **first-class goal**, even when every serialization is not yet final.

## Relationship to other chapters

- [Section overview](06-00-section-overview.md)
- [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md)
- [Kernel and governance](../07-kernel/07-07-kernel-and-governance.md)
- [Policy and governance (advanced)](../13-advanced-topics/13-07-policy-and-governance.md)

**Back to:** [Section overview](06-00-section-overview.md).
