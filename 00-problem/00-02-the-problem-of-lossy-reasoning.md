---
title: "The Problem of Lossy Reasoning"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# The Problem of Lossy Reasoning

## The Problem

Once you treat engineering as **decision-making under constraints** (see [Engineering as decision-making](00-01-engineering-as-decision-making.md)), a second product of the work becomes visible: **rationale**. Rationale answers why an option was chosen, what was ruled out, which assumptions were treated as true, and which **constraints** were binding at the time. **Traceability** needs both the **decision** and enough rationale to interpret it later.

Rationale is as much a product of engineering work as the code and diagrams. It is also fragile. An organization that must operate and change a system for years cannot rely on the decision living only in the moment it was made. It has to preserve rationale across handoffs, reorgs, tooling changes, and turnover. If rationale does not travel well, the organization still has behavior, habits, and **artifacts**, but it loses the thread of **why** the system is shaped the way it is.

This chapter names the predictable failure mode: **lossy reasoning**. **Reasoning** here means the structured content of engineering argument, not private thought. **Lossy reasoning** is what happens when that content moves through people, documents, and time the way audio passes through a cheap chain of compressors: detail disappears, structure collapses, and what remains is often just a label for the outcome. The point is not that people are careless. Channels have limited bandwidth, memory is finite, and prose is easy to shorten. The loss is systemic unless the organization treats reasoning as something to preserve on purpose.

Typical symptoms include:

- **Shorter explanations.** A careful argument becomes a sentence, then a slogan, then silence.
- **Missing assumptions.** A choice that depended on a traffic level, a vendor posture, or a regulatory reading is retold as a preference or a style rule.
- **Forgotten constraints.** Limits that were real when the decision was taken harden into "we have always done it this way" without a record of what would break if you stopped.
- **Conclusions without reasons.** Wikis and tickets capture the final shape ("we use service mesh X") but not the trade space that made X tolerable compared to Y.
- **Decisions that become habit.** Operational practice and code paths persist while the reviewable commitment behind them does not.

For the decision-making framing this chapter builds on, see [Engineering as decision-making](00-01-engineering-as-decision-making.md).

## The Reframe

It is tempting to treat those symptoms as a people problem: write more, remember better, stay longer. That misreads the geometry of the work.

Engineering organizations are **distributed systems for information**. Signals pass through serial queues: meetings, tickets, docs, code review, on-call notes, training. Each hop has finite attention and a preferred format. Each hop is an opportunity to drop structure that did not fit the format or the deadline.

Reframing the issue as **information preservation** does three things. It removes blame as the primary explanation. It points toward design: what to record, where, in what shape. It lines up with the rest of this handbook, which treats **intent** and **architecture** as **artifacts** that must survive the same hops code survives.

A compact definition you can carry forward:

> **Lossy reasoning** is the practical failure mode in which engineering rationale loses fidelity as it is copied, summarized, and handed off, so that **decisions** become harder to review, reconcile, or check against reality.

This is the obstacle STE is aimed at. It is worth naming because many well-run teams already feel the drag without having a shared label for the mechanism.

**Lossy reasoning** is the *mechanism*: rationale and structure thin as they move through channels. **Drift**, in the Part 0 sense developed in [Intent versus Implementation](00-03-intent-vs-implementation.md), is a common *observable outcome*: the gap between what the organization still believes it decided and what **embodiment** and behavior support. The mechanism explains how teams arrive at that gap without anyone choosing it on purpose.

## The Model

**Lossy reasoning** is the progressive loss of decision-relevant information as rationale moves between people, artifacts, and points in time. The outcome is not always total ignorance. Often the organization still "knows" what it does. What thins out is the recoverable structure: alternatives, assumptions, **constraints**, and the explicit links between them.

### Where loss occurs

Loss is not one event. It accumulates across ordinary work. A few common sites:

**Conversations.** Design reviews and incident discussions often produce rich context in the room. What survives afterward is minutes, memory, and whatever someone writes down while context is still hot. The spoken graph of dependencies and rejected options rarely lands intact in any durable artifact.

**Handoffs.** When ownership moves from one team or vendor to another, the receiving side gets repositories, runbooks, and access. They do not automatically get the reasoning that made those artifacts look the way they do. A handoff note that says "use the blue pipeline" preserves procedure, not rationale.

**Staff turnover.** When experienced engineers leave, they take fluency with them. Remaining systems encode outcomes of past **decisions**, but the map from outcome to reason is often reconstructed later from code and folklore.

**Summaries.** Status updates and executive briefings compress weeks of engineering into a few lines. Compression is the job. What drops out first is usually the structure of the trade, because it does not fit the format.

**Documentation that captures conclusions but not reasoning.** An architecture page that lists "our platform choices" without alternatives, constraints, and supersession rules is a catalog of outcomes. It helps onboarding skim the present. It does not preserve the decision record future maintainers need when the environment changes.

**Long-lived systems after original designers are gone.** A service written ten years ago may still run well while the constraints that shaped it (hardware limits, partner APIs, org boundaries) have changed several times. Without a preserved rationale, every change is a small gamble about which old assumptions still bind.

Those sites stack in real programs. A principal engineer agrees in a meeting that retries must stay bounded for a specific partner API; the ticket closes as �fix retries�; the wiki still describes the old policy six months later; the author leaves; the on-call runbook mentions �back off� without numbers. Two teams then ship different limits, each convinced they honored �what we decided.� The **embodiment** is not mysterious. The recoverable **intent** is.

Each site is normal. Together they form a pipeline that strips structure unless something counteracts it.

### Why prose alone is an unstable carrier of intent

Prose is excellent for explanation, persuasion, and nuance. For many audiences it is the right medium the first time a decision is communicated. The trouble appears when prose must serve as the **only** durable carrier of engineering **intent** across many readers, reviewers, and tools over years.

**Weak structure for consistent review.** A long narrative does not force explicit fields for context, options, constraints, and consequences. Reviewers read for clarity and mistakes they already know to look for. Two reviewers can approve the same document while attending to different parts of the argument. What is "reviewed" is not always the same object in practice.

**Ambiguity under reuse.** The same paragraph supports multiple readings once it leaves the author. Terms like "secure," "scalable," or "simple" pick up local meaning in one team and a different meaning in another. Without a shared structured vocabulary, alignment is negotiated repeatedly in chat.

**Hard to validate automatically.** Tools can lint code and sometimes configuration. They cannot, in general, decide whether a prose document still matches a running system or whether a new change violates a **constraint** that was stated only in passing on page six.

**Hard to detect drift against prose.** When embodiment moves, there is no mechanical diff between "what the words meant when written" and "what the system does now." **Drift** shows up as surprise, argument, or incident, not as a failing check.

**Inconsistent interpretation across roles.** Security, reliability, and product leads each stress different sentences. None of that is bad faith. It is what happens when the binding commitments are not separated from narrative in a form everyone can point to.

Prose remains valuable. STE does not ask organizations to stop writing. It asks them not to treat unstructured prose as the sole long-term store for commitments that must survive contact with automation, audits, and time.

### Lossy compression as analogy

A useful analogy is **lossy compression** in information theory. A lossy codec throws away detail humans are thought not to need. Play that chain often enough, or change the listener, and artifacts appear. Organizations do something similar to rationale unless they preserve the parts that must be recovered later. The lost pieces are often not emotional nuance. They are the explicit assumptions and constraints that make a **decision** rational.

Part 1 returns to that idea under the heading of **information theory**: not bit rates for meetings, but **encoding**, **distinguishability**, and what has to stay in the representation if **intent** is to survive handoffs.

## The Implications

When rationale thins, the organization pays in predictable ways:

**Repeated debates about old decisions.** Without a stable record, the same trade is re-derived from scratch whenever pressure rises. Teams burn cycles proving again what was already settled, or they settle it differently because the **constraints** have shifted and nobody can see the old ones.

**Hidden constraints.** Outcomes embedded in code and habit behave like immovable facts. The organization obeys limits it no longer names. Those limits are hard to challenge on purpose because they are not represented as **decisions** that can be superseded.

**Inconsistent decisions across teams.** Without shared, checkable statements of **intent**, each group improvises from local context. The system grows a patchwork of compatible-looking choices that do not compose into one coherent **architecture** story.

**Drift between intent and system behavior.** Declared direction (in slides, wikis, or hallway consensus) diverges from what actually runs: an *outcome* of thinned rationale and weak records as much as of any single bad change. The gap is slow until it is expensive. For a fuller treatment of mismatch over time, see [The governance model](../06-governance/06-02-the-governance-model.md).

**Weak audit and governance.** Auditors and regulators ask for **evidence** that controls and commitments are real. **Governance** asks who may change what, under which rules, with which **traceability**. If reasoning lives only in informal narrative, there is little stable object to version, review, or attach policy to. See [Section overview (Part 6)](../06-governance/06-00-section-overview.md).

None of these outcomes requires negligence. They follow when the information an organization needs to steer is not preserved in a form that stays reviewable.

## Where this leads

**Lossy reasoning** explains why rationale thins; it does not yet separate what should be true from what exists. The next chapter names **intent** and **embodiment** as two sides so **drift** and **conformance** are not opinion.

## Relationship to STE system

STE does not promise perfect fidelity. No discipline can. It aims to make reasoning **less lossy** by giving rationale durable structure and by connecting that structure to what runs.

Later handbook parts develop decision records, **intent** models, **Architecture IR**, **validation**, and **governed reasoning** as responses to that failure mode. For how **intent** is represented as artifacts, see [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md) and [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md). For the canonical structural compilation of **architecture**, see [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md). For **conformance** assessment, see [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md).

## Summary

- **Reasoning degrades** as it moves through conversations, handoffs, summaries, and time unless the organization preserves decision-relevant structure on purpose.
- **Lossy reasoning** names that failure mode: shrinking explanations, missing assumptions and **constraints**, and outcomes that persist without recoverable rationale; treat it as the *mechanism* whose common *outcome* includes **drift** between declared **intent** and **embodiment**.
- **Prose alone** is a weak long-term carrier for binding engineering **intent** because it lacks stable structure for review, automation, and **drift** detection across many readers and years.
- **Consequences** include relitigation, hidden **constraints**, inconsistent **decisions** across teams, **drift** between declared **intent** and behavior, and **governance** that lacks a stable object to enforce.
- The issue is **systemic information loss**, not a verdict on individuals; like repeated lossy compression, each hop drops detail unless the representation keeps what must be recovered.
- **STE** uses structured **artifacts**, **traceability**, and **evidence**-linked checks to reduce loss; **governed reasoning** (see [Governed reasoning](00-05-governed-reasoning.md)) names how **reasoning** stays accountable under explicit **rules**, **scope**, and **evidence** expectations.
