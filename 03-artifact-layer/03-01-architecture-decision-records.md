---
title: "Architecture Decision Records"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-26"
---

# Architecture Decision Records

**Artifact type:** Architecture decision record (**ADR**).  
**Role in STE:** Capture a chosen commitment and its rationale as a stable **intent** record in the artifact graph.  
**Primary concern:** intent.  
**Connects to:** requirements and **constraints**, **invariants**, **Architecture IR**, **traceability**, **conformance**.

## The Problem this artifact solves

Important choices disappear into memory, tickets, or informal decks. Nobody can reconstruct **why** the system looks the way it does, so redesigns repeat arguments and teams ship incompatible interpretations. **ADRs** exist so decisions are **durable**, **addressable**, and **supersedable** without pretending the past never happened.

## What the artifact is

An **ADR** is a structured record of an architecture **decision**: context, options considered, the chosen commitment, and consequences. In STE it is an **intent** artifact type. It is not an omnibus narrative that describes the whole system, and it is not source code. It may reference **Architecture IR** elements once compiled, but the record carries rationale and decision status that the IR does not replace.

STE may distinguish multiple ADR surfaces (for example lifecycle or packaging) in **ste-spec**. At handbook altitude, treat them as one family: recorded decisions with explicit lifecycle.

## How it is used in STE

People **decide**; STE **materializes** ADR records under governed workflows where **ste-spec** defines capture. **Governance** approves superseding records when the organization changes course. Compilation aligns **Architecture IR** and downstream checks. Reviewers use ADRs to ask whether **embodiment** matches recorded commitments.

**Example:** An ADR states public API v1 remains backward compatible for twelve months. A breaking change proposal triggers **governance**: supersede the ADR or reject the change, not a debate about memory.

## How it relates to intent, implementation, or evidence

- **Intent:** ADRs are primary **intent**. They state what the organization chose.
- **Implementation:** **Embodiment** should reflect committed decisions; gaps motivate **drift** investigation or record updates.
- **Evidence:** ADRs do not replace tests or monitors, but they explain what **conformance** claims should mean when linked to scopes and checks.

## How it participates in lifecycle and governance

Creating, superseding, or retiring an ADR should follow an explicit path: owner, reviewers, and visibility into impact on **Architecture IR** and **validation** scope. Exceptions (for example a time-bounded waiver) belong in governed records, not only in chat.

## Relationship to other artifacts

- [Requirements and constraints](03-02-requirements-and-constraints.md): ADRs often commit to requirements or tighten **constraints**; requirements can force a new ADR when they change.
- [Invariants](03-03-invariants.md): a decision may introduce or relax **invariants**; both should stay aligned.
- [Architecture model and IR](03-04-architecture-model-and-ir.md): compilation ties decisions to canonical elements where STE defines that mapping.
- [Traceability](03-06-traceability.md): links from ADR identifiers to IR nodes and checks.
- Part 4: [Architecture IR overview](../04-architecture-ir/04-00-architecture-ir-overview.md) for IR depth.
- Part 8: [Decision capture](../09-conversation-engine/09-03-decision-capture.md) for conversational capture that must still land in durable records.
