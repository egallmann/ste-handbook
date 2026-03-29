---
title: "Kernel reasoning surface"
status: draft
maturity: L2
last_reviewed: "2026-03-28"
diagrams: no
---

# Kernel reasoning surface

## The Problem

“Architecture reasoning” collapses into informal opinions when teams cannot separate **what exists**, **why it exists**, **what is missing**, and **what may change**. STE needs a small, stable vocabulary for those questions—one that automation can implement without re-deriving philosophy per repository.

## The Reframe

The **Kernel role** exposes four operations—**Query**, **Explain**, **Coverage**, and **Admission**—over **Architecture IR**, **Evidence**, **governance rules**, and **lifecycle state**. These are not optional UX features; they are the contract surface for mechanical architecture reasoning in STE.

## The Model

### Query — what exists

**Query** returns structured facts from **Architecture IR** (and projections derived under **ste-spec** rules), not inferred opinion. Typical families include:

- Which components, services, or modules exist as modeled entities.
- Which **decisions** (**ADRs** or decision records) bind to which structural elements.
- Which capabilities or interfaces are declared.
- Which **invariants** and constraints attach to which scopes.

**Query** answers “what is declared true in the compiled model?”

### Explain — why it exists

**Explain** traverses traceability: from a structural element back to the **intent** that authorized it, the **invariants** that constrain it, the **governance rules** that interpret policy, and the **Evidence** that supports or challenges conformance claims. Outputs are **explanation graphs** or equivalent structured traces suitable for review and automation.

**Explain** answers “what reasoning chain justifies this element’s presence and shape?”

### Coverage — what is missing

**Coverage** compares “what the model claims should exist or be governed” against “what is present, linked, and evidenced.” Illustrative classes of findings:

- Missing decision implementations (declared obligations without modeled realization).
- Orphan components (modeled elements without required **intent** linkage).
- Unconstrained components (elements lacking required **invariants** or policy attachment).
- Missing **Evidence** where policy expects observation (**ArchitectureEvidence** or other **Evidence** channels).
- Ungoverned decisions (**intent** records not reflected in **Architecture IR** or not reachable by **Query**).

**Coverage** answers “where is the architecture incomplete relative to policy?”

### Admission — is change allowed

**Admission** evaluates a **change proposal** against **Architecture IR**, **Evidence**, **governance rules**, and **lifecycle state**. It emits **Admission** outcomes; where **ste-spec** defines the handoff, **KernelAdmissionAssessment** is the decision-bearing payload. The role is **fail-closed**: if required inputs or constraints are absent, the default posture is deny or block—not silent approval.

**Admission** answers “may this change proceed under declared rules?”

### Minimum viable architecture reasoning system

These four operations form the **minimum viable architecture reasoning system** in STE:

| Operation | Question answered |
|-----------|-------------------|
| **Query** | What exists? |
| **Explain** | Why does it exist? |
| **Coverage** | What is missing? |
| **Admission** | Is change allowed? |

**STE concept (explicit):** If a system can answer these four questions **deterministically** against **Architecture IR** and **Evidence** under declared policy, it constitutes an **architecture reasoning system** in STE’s sense. Larger tool ecosystems compose **around** this core; they do not replace it with ad hoc judgment inside CI scripts or chat transcripts.

## The Implications

- Product surfaces (IDE, CI, assistants) should map their features to these four operations to avoid semantic drift.
- **Admission** must not be reimplemented with different semantics per team; **ste-spec** is the shared contract.

## Relationship to STE system

- Overview: [Kernel overview](07-00-overview.md).
- Determinism: [Determinism and fail-closed](07-06-determinism-and-fail-closed.md).
- **Architecture IR** depth: [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md).

## Summary

- **Query**, **Explain**, **Coverage**, and **Admission** are the **Kernel role**’s stable reasoning surface.
- Together they define STE’s **minimum viable architecture reasoning system** when answers are **deterministic** and contract-backed.
- **KernelAdmissionAssessment** names the **Admission** outcome shape where **ste-spec** requires it.
