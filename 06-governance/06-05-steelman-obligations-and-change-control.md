---
title: "Steelman, obligations, and change control"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-04-02"
---

# Steelman, obligations, and change control

## Why this matters

**Governance** needs a way to **stress-test** decisions before **implementation** momentum makes reversal expensive—**lock-in before closure**. In STE, **steelmanning** is a **formal governance function**, not discussion etiquette: it is how the organization forces **decision closure** and **checkable obligations** before build pressure wins.

## The problem

Architecture debates often collapse into **weak objections** or **rubber stamps**. Meanwhile, teams start building from half-formed decisions because schedules pressure “movement.” The result is **implementation lock-in** without **decision closure**.

## The reframe

**Steelman** the strongest version of a proposal and its best **counter-cases** so that **ADRs** and linked **Architecture IR** carry **examined** commitments.

- **Decision closure** — the organization accepts the record for a **scope** and **time horizon**, with explicit **obligations** for what must be revisited when triggers fire.
- **Obligation creation** — gates gain **checkable** requirements (evidence types, IR impact, reviews) defined in [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md).
- **Change control** — **implementation** work is tied to those commitments so **embodiment** does not outrun declared **intent**.

Human interface patterns live in [Steelman](../09-human-interface/09-04-steelman.md); this chapter states why that practice is **governance-critical**.

## Steelman as governance, not commentary

A **steelman** pass answers governance-grade questions, for example:

- What is the **strongest** case for this option, including for stakeholders who lose something?
- What **invariants** or **constraints** does it stress?
- What **evidence** would **falsify** the decision in the next delivery cycle?
- What **alternatives** were rejected, and why are they still weaker under declared priorities?

The output should be **durable enough** to link from **decision records**, not only chat scrollback.

## Binding ADRs and implementation

**Implementation must not proceed on a binding ADR that has not completed steelman review**, except where the record is **explicitly marked exploratory** and org policy allows that path (for example **E-ADRs** in **ste-spec**—exploratory records not published as binding spec ADRs). Use **ste-spec** `status.md` and project ADR policy for promotion rules; the handbook point is **control**: do not mix **exploration** and **binding** intent without labels and owners.

## No implementation until architectural decisions are sufficiently hardened

**Sufficiently hardened** is not infinite analysis. It means:

- Decisions that bound **structure**, **trust boundaries**, and **failure modes** are **written**, **versioned**, and **traceable**.
- **Architecture IR** reflects those commitments for the scopes that will be built next.
- Known **open questions** are **explicitly** flagged as **risk** or **follow-up obligations**, not smuggled as tacit assumptions.

STE distinguishes **converged ADRs** (binding architectural commitments) from **exploratory** records used to learn under execution pressure.

## ADR quality and decision closure

**ADR** quality is a **governance** signal. Thin ADRs force **admission** and reviewers to guess. Strong ADRs state **context**, **decision**, **consequences**, and **rejected alternatives** with links into **Architecture IR** where structure is touched ([Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md)). **Closure** is the acceptance and obligation pattern described under **Decision closure** above (scope, horizon, explicit revisit triggers).

## Obligations on the path to implementation

Examples of **obligations** tied to change control:

- Required **evidence** types for a release class.
- Required **diff** or **impact** analysis against **Architecture IR** identities.
- Required **steelman** or **review** roles for high-risk decision categories.

Obligations should be **checkable**, not vibes. They connect **intent** to the **enforcement posture** described in Part 6 without confusing **rules** with the **architecture** itself.

## Relationship to other chapters

- [Admission, eligibility, and enforcement](06-04-admission-eligibility-and-enforcement.md)
- [Authority and decision rights](06-03-authority-and-decision-rights.md)
- [Conversation to ADR](../11-examples/02-conversation-to-adr.md)
- [Change and evolution](../05-lifecycle/05-07-change-and-evolution.md)
- [Decision capture](../09-human-interface/09-03-decision-capture.md)

**Next:** [Determinism, provenance, and audit](06-06-determinism-provenance-and-audit.md).
