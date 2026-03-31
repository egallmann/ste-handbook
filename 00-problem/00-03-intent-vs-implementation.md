---
title: "Intent versus Implementation"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-24"
---

# Intent versus Implementation

## The Problem

When rationale has already thinned (see [The Problem of Lossy Reasoning](00-02-the-problem-of-lossy-reasoning.md)), a hidden category error gets worse: teams mix two different kinds of claim without noticing.

Engineering organizations constantly talk about "the system." In the same breath they mean what the system is **supposed** to be and what it **actually** is in repositories, configuration, and production. Those are not the same kind of statement.

When the two are not named, teams argue past each other. One person means a commitment. Another means a build. A third means what they saw in production last Tuesday. **Drift** and **conformance** become opinion because nobody can point to two distinct objects and compare them.

That confusion also worsens the failure mode in [The Problem of Lossy Reasoning](00-02-the-problem-of-lossy-reasoning.md). If narrative, code, and runtime are one undifferentiated blob, you cannot tell whether the story drifted away from reality or reality drifted away from commitments. Pain shows up as debate or incident, not as a check with a clear pass or fail.

## The Reframe

STE names two categories on purpose:

- **Intent** is **normative**: **decisions**, **constraints**, and **invariants** (what should hold, and often why).
- **Embodiment** is **descriptive**: what exists in code, infrastructure, configuration, and runtime (plus operations practice): what was built, what ran, and what you can observe.

**Validation** compares those two sides: declared **intent** to **embodiment** (and **evidence** about it); **drift** and **conformance** are defined on that comparison, not on opinion.

The chapter title keeps **implementation** because code-level work is where the confusion hurts first. In this handbook, **implementation** is the code-level portion of **embodiment** (modules, repos, concrete builds), not a synonym for the whole descriptive side. For adjacent definitions and the Part 0 term contract, see the key terms in [Part 0: Foundations](00-00-foundations-overview.md) and [Engineering as decision-making](00-01-engineering-as-decision-making.md).

STE's control loop compares **intent-shaped artifacts** to **embodiment-shaped evidence**. Merge the categories in conversation or in tooling, and you lose the ability to say, cleanly, what drifted from what.

## The Model

These are handbook definitions. They align teams; **ste-spec** remains the authority for normative technical detail where the two differ.

**Intent:** Normative commitments: **decisions**, **constraints**, and **invariants** that describe how a system is supposed to be structured and behave.

**Embodiment:** What exists in code, infrastructure, configuration, and runtime (including operations practice) that realizes **intent** in the real world.

**Drift:** Any difference between maintained **intent** and observed **embodiment**.

**Conformance:** The claim that **embodiment** (including observed runtime behavior where relevant) matches declared **intent**.

**Validation:** **Evidence**-linked assessment of whether that **conformance** claim holds under agreed **rules** and **scopes**.

The definitions above are the Part 0 anchor; later chapters **reference** them instead of rephrasing. In prose, **intent** also carries policies and rationale that make commitments intelligible later. It answers "what ought to hold?" and often "why did we commit to that?" **Embodiment** answers "what is actually there?" and "what happened when we exercised it?" **Drift** often grows slowly and unowned; for lifecycle treatment, see [drift](../06-governance/06-03-drift.md).

Both sides can be wrong or incomplete. Intent can be stale, vague, or internally inconsistent. Embodiment can be buggy, misconfigured, or absent. **Governance** and assessment need both in view so you can compare them on purpose.

### Examples in practice

#### Requirements versus tests

**Requirements** state intended behavior, constraints, or outcomes under stated conditions. In STE terms, treat them as **intent**-shaped commitments when they are meant to bind. **Tests** exercise **embodiment** (including **implementation**) and record results. A requirement is normative; a test run is descriptive **evidence** about a specific attempt. You need both: intent without tests is hard to verify; tests without declared intent are hard to govern ("why are we running this?").

#### ADRs versus code and infrastructure

An **Architecture Decision Record (ADR)** captures a decision in a reviewable shape: context, options, the commitment, and expected consequences. **Code** and **infrastructure definitions** carry that commitment out. The ADR is not "the system," and the repository is not "the rationale." Traceability between them shows which parts of **embodiment** exist because of which decisions.

#### Invariants versus runtime behavior

**Invariants** are declared properties that must hold (for example, safety or consistency rules). **Runtime behavior** is what you observe under load, failure, and change. Invariants are obligations on the intent side. Traces, metrics, logs, and replayed scenarios are observations on the **embodiment** and **evidence** side. Assessment asks whether observations support the claim that invariants hold.

#### Policies versus IAM configuration

A **policy** states who may do what under which conditions, often in organizational or regulatory language. **IAM configuration** (roles, bindings, permission sets) is the control plane state the platform enforces. The policy is normative; effective grants are descriptive. **Drift** between them is a common failure mode: the written rule says one thing while enforcement quietly says another.

#### Architecture versus deployed resources

**Architecture** here means declared structure and constraints: components, dependencies, boundaries, and rules that should govern change. **Deployed resources** are the instances, networks, identities, and relationships that exist in an environment. The diagram is not the account. The intended graph and the live graph are related; they are not the same object.

### Intent-shaped and embodiment-shaped artifacts

The table is a compact map. It is not exhaustive; it trains the eye to sort artifacts by role.

| Intent-shaped (normative) | Embodiment-shaped (descriptive) |
| --- | --- |
| Requirements, user stories with acceptance criteria as commitments | Test suites, test run results, CI job outputs |
| ADRs and other decision records | Application **implementation** (code, modules, services as built) |
| Declared invariants and constraint rules | Runtime signals, traces, probe results |
| Security and access policies (organizational intent) | IAM roles, bindings, permission sets, effective access graphs |
| Architecture descriptions and canonical models (including **Architecture IR** as a declared system shape) | Repositories, configs, infra-as-code, live resource inventories |
| (Not applicable: evidence is not intent) | **Evidence**: observations that **embodiment** did or behaved a certain way, with provenance |

**Evidence** sits with **embodiment** because it records what was observed, not what ought to be. The control loop uses **evidence** to test **intent**.

Incident-shaped version of the same confusion: an outage review concludes “we must never bypass the payment fraud check.” Product **intent** in slides agrees. A hotfix path still ships with a feature flag that skips the check for an internal tenant. **Embodiment** now allows what **intent** forbids, but the flag name sounds administrative, so **drift** stays invisible until the wrong customer segment hits it. Clean categories do not prevent mistakes. They make the mistake a **conformance** question instead of a vocabulary fight.

### Traceability, evidence, and the control loop

**Traceability** is defined in [Engineering as decision-making](00-01-engineering-as-decision-making.md). Here it is enough to stress the interface between **intent** and **embodiment**: a commitment must connect to where it is carried out and to the checks that observe it. That may mean explicit identifiers, links from tooling, compilation from intent into structural artifacts, or repository conventions. The mechanism varies. The requirement does not: if you cannot traverse from intent to **embodiment**, you cannot govern change. You can only react.

**Runtime evidence** captures descriptive reality in a shareable form: what ran, what was measured, what failed, under which version and environment. See [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md).

At the level this handbook cares about, the **control loop** is one sentence: compare intent-shaped artifacts to embodiment-shaped evidence using explicit rules, record the outcome, and act on it. Rules, **scope**, and reporting are part of [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md). The loop is only as honest as the separation it assumes.

### Mental model

```mermaid
flowchart LR
  intentArtifacts[IntentArtifacts]
  traceLinks[TraceLinks]
  embodimentEvidence[EmbodimentAndEvidence]
  assessment[Assessment]
  intentArtifacts --> traceLinks
  traceLinks --> embodimentEvidence
  embodimentEvidence --> assessment
```

**How to read it.** Intent lives in artifacts teams treat as normative. Trace links tie those artifacts to code, configuration, and environments. **Embodiment** and **evidence** describe what is there and what was observed. **Assessment** compares the two under rules and produces a governed result.

## The Implications

When intent and **embodiment** are not kept distinct:

- **Drift** becomes impossible to define. **Drift** is a relationship between two maintained objects. If "the doc" is also "the truth," nothing is left to diverge from except opinion.
- **Conformance** collapses into slogans. Without a declared intent side, "conformance" devolves into "looks fine to me."
- **Deterministic assessment** needs comparable artifacts. The same rule must apply to the same kinds of inputs. That requires intent in a stable shape and **evidence** in a stable shape so automation and humans can repeat the comparison.
- **Engineering governance** is, in practice, comparing normative commitments to descriptive reality under agreed **scope** and documented exceptions. If teams cannot point to intent artifacts separate from build outputs, **governance** has no stable object to version, review, or enforce.

None of this requires perfect documents or perfect systems. It requires **honest categories**.

## Where this leads

**Intent** and **embodiment** can be compared. The **architectural** slice of **intent** (boundaries, dependencies, rules for how the system may evolve) still needs a durable home that is not “whatever the senior staff remember.” The next chapter treats **architecture** as a structured, versioned **artifact** so **traceability** does not collapse back into local story.

## Relationship to STE system

- [The Problem of Lossy Reasoning](00-02-the-problem-of-lossy-reasoning.md) explains why rationale and commitments thin out over time. Separating **intent** from **embodiment** makes it easier to preserve and check what must survive that journey.
- The [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md) and [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md) describe where normative structure lives before and alongside compilation into other artifacts.
- [Kernel overview](../07-kernel/07-00-overview.md) introduces the engine that performs assessment over declared structure and evidence.
- [Part 8: Runtime Overview](../08-runtime/08-00-runtime-overview.md) and [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) cover the evidence and rule side of the control loop.
- [Drift](../06-governance/06-03-drift.md) names divergence between intent and reality over time; [Governance](../06-governance/06-06-governance.md) covers how organizations keep that comparison legitimate and actionable.

## Summary

- **Intent** is normative: the set of decisions, constraints, and invariants that describe how a system is supposed to be structured and behave; policies and rationale travel with it.
- **Embodiment** is descriptive: code, configuration, infrastructure, operations, and what you can observe; **implementation** names the code-level slice of that whole.
- **Drift** is any difference between maintained **intent** and observed **embodiment**; **conformance** (embodiment matches intent) and **deterministic assessment** need both sides as maintained objects.
- **Traceability** connects commitments to **embodiment**; **evidence** records observations about **embodiment** and runtime.
- STE's **control loop** compares intent-shaped artifacts to embodiment-shaped evidence under explicit rules, then drives the next engineering and **governance** actions from that comparison.
