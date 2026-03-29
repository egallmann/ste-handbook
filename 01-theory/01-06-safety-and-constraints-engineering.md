---
title: "Safety and Constraints Engineering"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# Safety and Constraints Engineering

## The Failure Mode

A break-glass IAM role ships for an incident; the ticket says “remove after drill.” The role stays. New services inherit the binding because the template is copy-paste friendly. **Intent** still says “least privilege,” but **embodiment** quietly carries a superuser path. **STE needs this chapter** because high-severity failures and everyday **constraints** share one requirement: explicit **invariants**, honest **evidence**, and **governance** that can tell a waiver from a quiet rewrite.

High-severity failures often trace to implicit authority or silent erosion of mandatory properties. Without explicit **invariants**, **constraints**, and **evidence**, organizations cannot argue assurance or **conformance** with integrity as **embodiment** moves.

Some failures are ordinary bugs: wrong output, slow page, annoyed user. Other failures are harms: injury, loss of life, loss of critical public function, catastrophic data compromise, systemic unfairness that becomes structural harm. Safety and assurance fields exist because “try harder” is not a control strategy when consequences are severe.

Even when consequences are less dramatic, **constraints** still matter: data integrity rules, access boundaries, financial correctness **constraints**, operational limits. When those properties are treated as vibes, **drift** becomes a security and reliability problem rather than a documentation problem.

“We have alerts” is another quiet trap. Alerts are sensors. They misfire, get ignored, or get bypassed under pressure. Assurance asks whether the right properties are monitored, whether on-call response is **governed**, whether alert fatigue is treated as its own hazard, and whether post-incident work updates **intent** or only restarts services.

Software culture flips between extremes: everything labeled “safety” for drama, or safety language dismissed as someone else’s job. STE takes a middle stance: **constraints** and **invariants** are normal engineering objects; assurance is **evidence**-linked argument; **governance** must allow revisiting assumptions without silent erosion.

## The Field Concept

### A software-shaped hazard pattern: authority without traceability

Many severe software failures share a skeleton: a component had authority to cause harm (money movement, data exposure, physical actuation, privileged access), while the organizational **intent** about that authority was implicit. **Governance** could not see when authority expanded because expansion happened through small, unreviewed changes. Assurance was replaced by optimism.

STE’s response is structural: make authority-related **invariants** explicit, connect them to **Architecture IR** elements where possible, and require **evidence** that changes affecting authority were reviewed as such. This is not only “security scanning.” It is **governance** of the **design space** where risk concentrates. Handbook usage of **Architecture IR** follows **`ste-spec`** terminology (cross-repo contract); it is not **`ArchModel`** (the adr-architecture-kit internal compiler structure).

### What this field studies (practical slice)

Safety engineering studies how systems fail in ways that cause harm, how to reduce risk to tolerable levels, and how to argue that reductions are real rather than imagined. It emphasizes **hazards**, causal factors, mitigations, monitoring, and organizational controls. Related **constraints** practice studies mandatory properties: physical limits, legal requirements, compatibility commitments, resource envelopes.

Software-specific safety and assurance work translates those ideas into failures modes like uncontrolled actuation, unsafe states, privilege escalation, data corruption, and loss of availability in critical contexts.

### Core concepts STE needs

**Hazard.** A **hazard** is a condition that can lead to harm or unacceptable loss in a relevant context. In software-intensive systems, hazards may be technical (a bad state transition), operational (unsafe procedure under pressure), or socio-technical (misaligned incentives causing routine bypass). STE does not require teams to label every bug a hazard. It does encourage precise language when severity demands it.

**Risk and tolerability (light touch).** Risk combines severity and likelihood in some framing. Organizations set tolerability thresholds. STE does not prescribe a numeric method. It aligns with the structural point: not all **constraints** are equal; some deserve stronger **evidence** and stricter **governance**.

**Mitigation and controls.** **Mitigations** reduce risk: design changes, guards, monitoring, human procedures, defense in depth. In STE vocabulary, many mitigations appear as **invariants**, **rules**, automated checks, and operational playbooks linked to **evidence**.

**Invariant.** An **invariant** is a statement that must hold for the design to remain valid unless explicitly revised through **governance**. Safety culture often calls these properties “must never” or “always” conditions. STE uses **invariant** as the handbook term (field concept: mandatory property that must remain true).

**Constraint.** A **constraint** shrinks the **design space**: what is allowed to change, what boundaries must hold, what resources are bounded. **Constraints** can be environmental, contractual, safety-related, or self-imposed. Safety regimes add external **constraints** that software must respect.

**Assurance and assurance cases (informal).** **Assurance** is justified confidence backed by structured argument and **evidence**. An assurance case connects claims (“we mitigated X”) to evidence items (tests, analyses, audits, operational metrics). STE’s **validation** story is adjacent: compare declared **intent** (including **invariants**) to **embodiment** using **evidence**.

**Conformance.** **Conformance** is the claim that **embodiment** matches declared **intent**. In safety contexts, non-conformance can be catastrophic. In ordinary software, it may still be costly. STE uses **conformance** broadly but expects proportionality in rigor.

**Certification (pattern, not hype).** **Certification** language in STE refers to repeatable assessment patterns: defined **rules**, defined **evidence**, recorded outcomes, and **governance** for exceptions. It does not automatically imply third-party certification regimes unless an organization is actually in one.

**Human factors and procedure.** Many hazards live at the boundary of software and human procedure: runbooks that are impossible under stress, permissions that encourage unsafe shortcuts, dashboards that mislead. STE treats operational practice as part of **embodiment** relevant to **validation** when **intent** claims operational safety properties. This is another place where “the system” **boundary** matters ([Systems theory](01-01-systems-theory.md)).

**Security as a constraints domain (without collapsing domains).** Security engineering is not identical to safety engineering, but it shares assurance shape: threat modeling, controls, monitoring, incident learning. STE’s vocabulary overlaps at **invariants** and **evidence**. The handbook does not pretend every security property is a safety property. It does insist that high-severity security **commitments** deserve the same traceability discipline as other **constraints**.

### Non-software analogy: railway signaling invariants

Rail systems separate “what trains may do” from “what operators wish would happen.” Signals encode **invariants** about route occupancy and speed. Procedures encode **constraints** under degraded modes. Assurance includes inspections, tests, and incident learning. The system is socio-technical: technology plus **governance** plus training.

Software rarely has physical levers, but it often has the same moral shape: states that must be impossible, transitions that require proof, and bypass paths that must be **governed**.

### Testing cultures and assurance gaps

Testing is necessary but not sufficient for assurance. Tests demonstrate behavior under modeled conditions. Assurance asks whether the model covered reality: realistic loads, realistic adversaries, realistic operator mistakes, realistic dependency failures. STE encourages treating test suites as **evidence** artifacts tied to explicit claims, and treating assurance arguments as the map that explains what the tests mean and what they omit.

For teams without a formal hazard process, the lightweight version still applies: name the worst realistic failures, name the **invariants** that prevent them, and connect those **invariants** to **evidence** and **governance**. Rigor scales with severity, but the structure scales down.

## What STE Takes From This Field

If you strip the specialized vocabulary away, the core move is simple: name what must not happen, name what must remain true, and build a loop that checks reality against those **commitments** with **evidence**. That loop is the same STE backbone described in Part 0, viewed through the lens of high-severity failure.

Safety engineering thinks in terms of **hazards**, mitigations, defenses in depth, and assurance cases: structured arguments supported by **evidence**. **Constraints** engineering (in a broad sense) thinks about what must never happen, what must always hold, and what bounds are acceptable under uncertainty.

STE connects that mindset to software architecture through **invariants** and explicit **constraints**, plus **validation** and **governance**. The handbook uses “certification” language in a disciplined way: not as a generic compliment, but as a pattern of repeatable assessment tied to declared **intent** and recorded outcomes.

This chapter is not a safety standard. It imports concepts, not checklists from regulated domains.

Because STE aims at **governance**, **conformance**, and continuous assurance, readers should recognize the family resemblance to safety and assurance practice without STE pretending to replace domain-specific engineering regimes.

| Field concept | STE concept |
| --- | --- |
| **Hazard** / mitigation | **Invariant**; **constraint**; **validation** target |
| Assurance case | **Evidence**; **conformance** argument |
| **Certification** pattern (handbook sense) | **Validation** loop; **governance** of exceptions |

**STE vocabulary (explicit).** In this handbook’s use for assurance-heavy arguments: an **invariant** is a must-always-hold property unless revised through **governance**. A **constraint** is a limit on the **design space** (what may change, what must remain bounded). **Assurance** is **evidence**-backed confidence in claims, not optimism. **Conformance** is the claim that **embodiment** matches declared **intent** (including **invariants** and **constraints**); rigor scales with severity.

STE is not a safety certification scheme and does not replace domain compliance. Proportionality matters: avoid pseudo-safety theater for routine work. Learned and probabilistic components still need **constraints**, monitoring **evidence**, and **governance** ([Deterministic versus stochastic systems](../00-problem/00-06-deterministic-vs-stochastic-systems.md)). Assurance competes for budget with unowned **drift**; spend where **constraints** demand it.

### Cross-links within Part 1

[Cybernetics](01-04-cybernetics.md) discusses **second-order** **governance** failures; safety regimes discover those quickly when audits contradict daily practice. [Information theory](01-02-information-theory.md) discusses **evidence** clarity; assurance collapses when **evidence** is ambiguous. [Decision theory](01-05-decision-theory.md) discusses explicit revisiting; safety cultures require controlled change to **invariants**, not silent edits.

## Where This Appears in STE

For **invariants** as an intent surface, see [Invariants](../03-artifacts/03-03-invariants.md). For **constraints**, see [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md). For **validation** and **evidence**, see [Kernel reasoning surface](../07-kernel/07-05-kernel-reasoning-surface.md) and [runtime evidence](../08-runtime/08-00-runtime-evidence.md). For **governance** of exceptions, see [governance](../06-governance/06-06-governance.md). For continuous loop framing, see [the control loop](../06-governance/06-08-the-control-loop.md). Targets may be skeletal; links are directional.

For foundational vocabulary on **conformance** and **validation**, Part 0 remains authoritative: [Intent versus Implementation](../00-problem/00-03-intent-vs-implementation.md). Normative assurance semantics belong in **ste-spec** and domain standards where applicable.

If your organization already runs a risk register or hazard analysis process, STE is not asking you to replace it. STE asks that outputs connect to **intent** artifacts and **traceability** threads so software change does not silently bypass the hazards you already named.

That integration is where many “paper safety” programs fail: the hazard list lives in a binder, while engineers ship from a different reality. STE’s architectural center of gravity is meant to reduce that split.

STE uses **invariants** and **constraints** as first-class **intent** objects. They are not comments. They are statements that **validation** can target, wholly or partly, mechanical or judgment-based. STE uses **evidence** expectations to prevent assurance from becoming storytelling. If you claim defense in depth, show the layers and show how you detect layer failure.

Part 0 distinguishes **deterministic** checks from **stochastic** or judgment-shaped domains. Safety and assurance cultures often pursue determinism where reality allows: typed interfaces, automated proofs in narrow scopes, hardware interlocks, configuration checks. STE encourages the same discipline for software **invariants** that can be checked mechanically, while remaining honest about residual judgment.

STE uses **governance** to handle the real world: waivers, incident-driven relaxations, emergency changes. Safety culture’s lesson is not “no exceptions.” It is “exceptions must be visible, time-bounded, and learned from.”

A frequent erosion pattern: an incident produces a “temporary” waiver for a **constraint** everyone knows is load-bearing. The waiver lives in a ticket comment. Six months later it is still in effect, nobody owns expiry, and new features assume the relaxed rule is normal. **Governance** can treat that as undeclared **drift** in **intent**, not as a private operational habit.

Assurance practice distinguishes “find who failed” from “make failure modes less likely.” STE aligns with the second posture structurally: **drift** is treated as a systems property, not a moral verdict. That does not remove accountability. It relocates accountability to **governance** mechanisms: who approved a waiver, what **evidence** supported it, what follow-up **invariant** updates happened.

## The Reference Problem

Some properties must hold regardless of sprint theater. **Invariants** and **constraints** are how STE names non-negotiable reference statements about allowed behavior and **design space**. Safety and **constraints** engineering clarifies that the reference is not only “features shipped” but “hazards bounded, assumptions explicit, assurance argued.” When those statements live only in slides or implicit team habit, **validation** cannot scale rigor with severity, and **governance** cannot tell a waiver from a quiet rewrite. **Conformance** needs crisp must-hold claims and **evidence** that actually tests them; otherwise assurance becomes storytelling while **embodiment** wanders.

## If You Ignore This Discipline

**Invariants** erode and **constraints** blur: severity collapses into vibes, **validation** cannot scale rigor to risk, and **governance** cannot tell a waiver from a quiet rewrite. When mandatory properties go soft, the usual chain follows: continuous change → **Intent** drifts → **embodiment** diverges → **conformance** becomes unknown → **governance** loses control → risk accumulates. **This chapter protects:** explicit **invariants**, **constraints**, and **evidence**-backed assurance language.

## Role in the STE Argument

This chapter hardens the chain where stakes are highest: it connects **intent** to mandatory properties and **evidence** expectations, so **drift** is not treated as a uniform low-cost glitch. **Invariants** and **constraints** give **Architecture IR** and **validation** something falsifiable beyond generic quality adjectives. It aligns **governance** with honest exceptions: visible, time-bounded waivers instead of undeclared risk. **Conformance** language scales with consequence, without pretending every domain is mechanically decidable. **Control** and **cybernetics** loops need properties worth defending; this chapter supplies that vocabulary.

## Axioms

- Safety and **constraints** thinking supplies vocabulary for severe failure modes, mandatory properties, and assurance backed by **evidence**, not slogans.
- **Hazards** and mitigations map to STE **invariants**, **constraints**, **rules**, and **validation** practices; **governance** handles exceptions honestly.
- **Conformance** is the match claim between **intent** and **embodiment**; rigor should scale with consequence severity.
- “Certification” language in STE names a repeatable assessment pattern, not automatic membership in external certification regimes.
- STE imports assurance discipline selectively; it does not replace domain safety engineering or compliance programs.
- High-risk authority without explicit **invariants** and **governance** is a recurring hazard pattern in software-intensive systems.
- Prefer mechanical **invariant** checks where honest; keep explicit space for judgment where **stochastic** factors remain.
- Tests are **evidence** items inside a larger assurance argument; passing tests do not automatically close the assurance story.
- Probabilistic and learned behaviors require **constraints** on allowed behavior and monitoring **evidence**, not abandonment of assurance discipline.
- Existing hazard and risk processes should connect to shipped **intent**, not live in parallel binders.
- Operational telemetry and alerting are part of assurance only when tied to declared properties and reviewed under **governance**.
- Even informal teams benefit from the hazard shape: worst failures, **invariants**, **evidence**, and **governance**, scaled to severity.

**Next:** [Software architecture theory](01-07-software-architecture-theory.md) (**structure**, **behavior**, **views**, **Architecture IR**).
