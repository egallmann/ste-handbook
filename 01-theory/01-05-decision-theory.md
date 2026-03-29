---
title: "Decision Theory"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-24"
---

# Decision Theory

## The Failure Mode

A pull request merges: new cache layer, thirty files, no **ADR**. The author and reviewer understood the trade. Six months later, operations needs to know whether stale reads are an acceptable failure mode or a bug. Nobody can reconstruct whether the team **committed** to eventual consistency or merely tolerated it for the demo. **STE needs this chapter** because **options** are not **decisions**, and **commitments** have to be addressable objects for **governance** and **validation**.

Engineering is a sequence of **irreversible decisions** under **uncertainty**. If those **decisions** are not recorded, the **design space** silently mutates: teams optimize against code and habit while believing they still honor old **constraints**. **Governance** and **validation** lose their reference.

Decisions have audiences. A choice obvious to the authors may be opaque to security, operations, a new hire, or an auditor. Recording **decisions** aligns perspectives on what is now supposed to be true. Without that, each audience reconstructs **intent** from partial channels, which raises **entropy** and produces avoidable conflict.

Many **decisions** never ship as **decisions**: they appear as merged pull requests, closed tickets, or “how we do things here.” When context changes, the organization rediscovers the choice as if it were a natural law. That is not only “bad documentation habits.” It is a missing object. If **commitments** stay implicit, **governance** cannot assess revisiting, **validation** cannot tell violation from supersession, and **drift** becomes a fog.

Decision theory, in the slice STE uses, is a language for **options**, **commitments**, uncertainty, and updating when new **evidence** arrives. STE does not import a formal utility calculus for teams. It imports a discipline: separate brainstorming from **commitment**, record what was chosen and why, and treat revisiting as a normal event under **governance**, not as betrayal.

## The Field Concept

A **decision** in this handbook is a **commitment** that selects among feasible alternatives under **constraints**, with rationale that should be recoverable later. Decision theory helps explain why that definition matters.

One useful move is to separate three things that teams often mash together: generating **options**, estimating consequences under **uncertainty**, and making a **commitment** that coordinates action. Brainstorming meetings often mix all three. The result is a transcript that supports none of them well. STE-friendly practice is to let **options** be plentiful early, then narrow, then record the **commitment** in an artifact designed for recovery.

Before **commitment**, the team inhabits a space of **options**. After **commitment**, some branches close. **Irreversibility** increases: downstream work attaches to the chosen path. Decision theory’s core picture matches engineering reality: you cannot keep every door open forever, and the cost of reversing depends on what you built on top.

### What this field studies (practical slice)

Decision theory studies choice under uncertainty: actions, outcomes, information, preferences, and updating beliefs when observations arrive. Formal treatments use precise mathematics. This handbook uses a lightweight mapping:

- **Uncertainty** means relevant facts are incomplete or future-contingent.
- **Options** are feasible alternatives before **commitment**.
- A **commitment** closes some **options** and enables coordinated action.
- **Evidence** updates what you should believe, and sometimes updates which **commitment** remains rational under **governance**.

### Core concepts STE needs

**Options versus commitments.** **Options** are not **decisions**. A design discussion that ends with “we could do A or B” is still pre-decision. A **commitment** is an organizational move: we will proceed as if A, we will not pursue B for now, and we understand the consequences well enough to work.

The failure mode is mistaking exploration for **commitment**, or **commitment** without recording. Both produce **entropy** later.

**State of knowledge.** **Uncertainty** is not shameful. It is the default. Good engineering makes **uncertainty** explicit: assumptions, unknowns, and what would change the choice. **ADRs** often include exactly that content.

**Preferences and constraints.** In formal theory, preferences rank outcomes. In STE, many “preferences” arrive as **constraints**: regulatory requirements, latency budgets, compatibility promises, staffing realities. **Constraints** shrink the **design space**. **Decisions** happen inside what remains.

**Revisiting decisions.** Decision theory expects updating. New **evidence** can make a once-rational choice less rational. STE aligns with that: **governance** should allow superseding an **ADR** with a successor record, not pretending history did not happen.

**Sunk cost versus valid reassessment.** Not every revisit is rational. Decision theory warns against throwing good money after bad purely because of past investment. Engineering has a parallel: organizations sometimes keep architectures because they paid for them. STE’s stance is not “never persist.” It is “persist with traceability.” If you reverse a major **decision**, do it as a **decision**, with explicit rationale and impact on **invariants**.

**Decision quality versus decision visibility.** A recorded **decision** can still be wrong. STE does not claim that **ADRs** guarantee wisdom. They guarantee inspectability. Inspectability is what allows organizations to learn: postmortems can point to the **commitment** that should have been different, rather than arguing about what people “meant.”

**Time and option value.** Some **options** expire. A migration window closes. A vendor offer ends. A security incident forces immediate response. Decision theory’s time dimension matches engineering reality: delaying **commitment** is sometimes correct, sometimes catastrophic. STE does not prescribe speed. It prescribes traceability: if time pressure forced a choice, record what **constraints** were active, what was known, and what risks were accepted. That record is how future reviewers distinguish recklessness from reasoned tradeoffs under pressure.

**Interlocking decisions.** Architectural choices rarely stand alone. A data model **decision** interacts with an operational **decision** about backups, which interacts with a security **decision** about access patterns. Decision theory often models single choices; engineering reality is a web. STE handles that web through **traceability**: link records, link model elements, and use **invariants** to state cross-cutting properties that must survive local changes.

### Default options and implicit commitments

Many “non-decisions” are **decisions** in disguise. If a team never chooses a persistence strategy explicitly, the first working prototype becomes the default. The organization then treats it as inevitable. Decision vocabulary helps name that move: inertia selected an **option** without recording **constraints** and tradeoffs.

STE does not demand endless debate before coding. It does ask for honest labeling. If you are prototyping, say so. If a prototype boundary hardened into a **commitment** because customers depended on it, record that **commitment** and its **constraints**. The failure mode is retroactive myth-making: “we always knew it would be this way.”

### Conflict resolution between decision records

Two **ADRs** can disagree, especially across teams or time. That is not a scandal. It is a signal that **governance** must reconcile **intent**: supersede, scope, or split ownership. Hidden disagreement is worse than visible disagreement. Visible disagreement can be traced; hidden disagreement becomes production incidents and political fights.

Decision theory’s updating story applies at the meta level: treat conflict as information that your **intent** graph is not coherent yet.

### A non-software analogy: bridge routing

Imagine choosing a bridge route across a river. Early in planning, many routes are **options**. Geotechnical surveys reduce **uncertainty**. Community **constraints** remove some **options**. A **commitment** chooses a route. Later, if new **evidence** shows foundation risk, revisiting the route is not “being flaky.” It is responding to reality. The important part is that the revisit is itself a governed change: new analysis, new approval, new communicated **intent**.

Software is faster and more malleable than civil engineering, which makes informal reversals tempting. Speed does not remove the need for traceability. It increases it, because **embodiment** can change faster than memory.

## What STE Takes From This Field

STE uses decision-theoretic language to motivate **ADRs** and decision lifecycle: capture context, **options**, and consequences; link **decisions** to **invariants** and **constraints**; and make reassessment explicit when **evidence** changes.

STE is anchored in “engineering as decision-making under **constraints**.” If **decisions** are not first-class, the rest of the system story collapses into tooling talk.

| Field concept | STE concept |
| --- | --- |
| **Options** | **Decision** exploration; **design space** before **commitment** |
| **Commitment** | **ADR**; **intent**; **design space** boundary |
| **Uncertainty** | **Evidence** for **validation**; **governance** revisit |
| Revisit triggers | **Governance** superseding or reopening a **decision** |
| **Design space** | **Constraint**; **invariant**; allowed **embodiment** |

**Control** language helps describe what happens after a **decision**: compare **embodiment** to declared **intent**, detect **error**, correct. **Information** language helps describe how **decisions** survive communication: preserve distinctions, reduce ambiguous reconstruction. **Decision** language names the missing middle: the explicit **commitment** that makes “reference” and “signal” concrete enough to **govern**.

**ADRs are not “documentation” in the weak sense.** They are **decision commitments** that bound the **design space** for future change: they record what was chosen, what was rejected, and what must remain inspectable when **embodiment** moves. STE does not require expected-value calculations for every feature. Decision theory does not set your **constraints**; ethics, regulation, and product vision live outside this chapter. Proportionality still matters: not every line needs an **ADR**, but high-reversal-cost **commitments** cannot live only in merged diffs.

## Where This Appears in STE

For **architecture decisions** as an intent surface, see [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md). For **requirements** and **constraints**, see [Requirements and constraints](../03-artifacts/03-02-requirements-and-constraints.md). For **invariants** as **commitments** about what must remain true, see [Invariants](../03-artifacts/03-03-invariants.md). For **governance** as the mechanism that allows superseding and versioning, see [governance](../06-governance/06-06-governance.md). Many chapters may still be outlines; links mark where the story continues.

Part 0 anchors the vocabulary: [Engineering as decision-making](../00-problem/00-01-engineering-as-decision-making.md). For **traceability** from **decision** to **embodiment**, see [Traceability in Architecture IR](../04-architecture-model/04-05-traceability.md).

**Decisions** also interact with lifecycle work: roadmaps, migrations, deprecations. A roadmap is not a substitute for **decision** records, but it should reference them. Otherwise schedules float free of **constraints**, and teams optimize locally against dates while unknowingly violating **invariants** chosen elsewhere.

Normative requirements for **ADR** schemas, statuses, and tool behavior belong in **ste-spec** where applicable.

**Assessment outcomes are decisions too.** A **validation** result is not only a boolean. Accepting risk under explicit **rules**, granting a time-bounded exception, or requiring additional **evidence** are organizational moves. They should be as traceable as code changes when they affect what is allowed to ship. Otherwise the organization’s true **constraints** live in informal tolerance, not in **intent**.

Teams sometimes use “alignment” as if it were a feeling. Decision vocabulary reframes it. Alignment means shared understanding of **commitments** and **constraints**, not shared enthusiasm. You can disagree emotionally yet remain aligned if you share the same recorded **intent** and the same **evidence** standards. Without recorded **commitments**, “alignment” is often just temporary politeness.

**ADRs** are STE’s standard durable shape for many architectural **decisions**: context, **decision**, status, consequences. They make **commitments** addressable. They create a place for **options** to live without pretending every rejected alternative was worthless.

Decision lifecycle connects to **validation**. If an **invariant** exists because of a **decision**, then checking **conformance** is partly checking whether later changes respected that **commitment** or explicitly revised it.

Decision lifecycle connects to **Architecture IR**. Compilation turns scattered **intent** into a canonical graph. **Decisions** explain why some edges exist. Without **decisions**, a graph can become a mere photograph of current habit.

STE encourages matching ceremony to reversal cost. Not every line of code needs an **ADR**. The failure mode STE targets is the opposite: high-reversal-cost **commitments** recorded only in merged diffs and oral lore. A practical heuristic is to ask whether a future team could safely change this area without understanding the **constraints** that shaped it. If not, record a **decision**.

## The Reference Problem

A reference is useless if nobody knows which **commitments** actually bound the **design space**. **Decision** theory’s practical gift to STE is explicit **options**, choices, and consequences made durable enough to revisit when **evidence** changes. Architecture Decision Records (**ADRs**) are the archetype: they turn “what we decided” into an addressable artifact **governance** can supersede without amnesia. Without that layer, **intent** collapses into reconstructed lore and **validation** argues against moving targets. Recorded **decisions** also tie **Architecture IR** edges to rationale; structure without **commitments** is a photograph, not an engineering reference.

## If You Ignore This Discipline

**Commitments** become implicit: the **design space** mutates in merged diffs and oral lore, **traceability** from **Architecture IR** to rationale breaks, and **governance** cannot tell a legitimate pivot from silent **drift**. **ADRs** are the durable shape STE uses to keep **decisions** addressable. Implicit **commitments** accelerate the familiar chain: continuous change → **Intent** drifts → **embodiment** diverges → **conformance** becomes unknown → **governance** loses control → risk accumulates. **This chapter protects:** recorded **commitments** and an explicit **design space**.

## Role in the STE Argument

This chapter supplies the link between stable models and accountable human choice. **Decision** vocabulary makes **ADRs** and successor records non-optional for high-reversal work: they close parts of the **design space** on purpose and make expensive reversals visible. That supports **traceability** from “why this edge exists” to later **embodiment** checks. Assessment outcomes (waivers, accepted risk, demands for more **evidence**) are **decisions** that deserve records. Together with **information** and **control** lenses, this is how STE reconnects **intent** to time: revisable references with audit trails, not frozen plans.

## Axioms

- **Options** exist before **commitment**; **decisions** close parts of the **design space** and should be recoverable later, not only inferable from code.
- **Uncertainty** and new **evidence** make revisiting **decisions** normal; STE expects **governance** and records, not silent pivots.
- **ADRs** are a practical STE artifact for capturing **decision** content: context, choice, and consequences, with explicit succession when replaced.
- **Validation** and **Architecture IR** depend on **decisions** being visible: otherwise **conformance** debates lack a stable reference.
- STE uses decision-theoretic language as engineering discipline, not as a demand for formal quantitative decision calculus in every case.
- Inertia creates implicit **commitments**; STE prefers explicit labeling, especially once customers and operators depend on a path.
- **Alignment** is shared understanding of **intent**, not the absence of disagreement.
- Time pressure changes which **options** remain; record what was known and which risks were accepted when **commitments** are made under stress.
- Superseding a prior **decision** should leave an audit trail: what changed in **constraints**, **evidence**, or risk appetite, not only a new preference.
- A good **decision** record makes the next revisit cheaper, even when the next revisit reverses the choice.

**Next:** [Safety and constraints engineering](01-06-safety-and-constraints-engineering.md) (**invariants**, **constraints**, assurance, **conformance**).
