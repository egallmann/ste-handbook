---
title: "Example step 0 — STE conversation (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 0 — STE conversation (grounding)

## Purpose

Show **convergence architecture through a conversational interface**: one **human designer** states what they want in plain language, while a **conversation engine** (CE) works with an **Architect agent**. The Architect agent does not speak with one voice—it **loads personas** (for example **FinOps**, **Security**, **AWS Cloud**, **Operations**) based on **signals**. Signals can be **semantic** (the user said “waste,” “24/7,” “Org,” “IAM”) or **structural** (projections from **ste-rules-library** rules that say which **agents** and **personas** must activate for this lifecycle phase or risk class). When the user is **vague or overloaded**, the **conversation agent (CE) explains** interpretations and **trade-offs**, then asks for a **commitment**.

As STE design **moves through phases**, those same governance rules are **projected into ADRs** and related artifacts—so the **personas that showed up in chat** are not a stunt; they trace to **rule-driven** obligations that later appear as **canonical** structure (requirements, invariants, decisions). This transcript **tags personas explicitly** for pedagogy; a full stack would **activate** them from **projected rule bundles** plus CE routing.

This **scripted transcript** is **illustrative**: it ends at expectations that match the public **[Instance Scheduler on AWS](https://github.com/aws-solutions/instance-scheduler-on-aws)** story (scheduled EC2/RDS start/stop, hub and optional spoke stacks) without claiming to quote AWS or any product UI.

> **Illustrative only.** Pedagogical fiction; **ste-spec** (sibling repo under the workspace) is normative for Architecture IR semantics; **adr-architecture-kit** for ADR field shapes; **ste-rules-library** for how rules are authored and projected in a complete STE program.

## Architect agent, personas, and rule projection

**Agent:** **Architect** — responsible for **structured probes** that narrow the design space.

**Personas** (illustrative catalog; your library may define more):

```text
Personas: [ FinOps, Security, AWS_Cloud, Operations, … ]
```

- **FinOps** — cost, utilization patterns, schedule economics, scope of environments.
- **Security** — trust, IAM blast radius, auditability, least privilege.
- **AWS Cloud** — accounts, Organizations, hub/spoke landing-zone patterns, regional coverage.
- **Operations** — opt-in mechanics, day-2 tooling (CLI/API), operator ergonomics.

**Activation (conceptual):**

1. **Signals** from the user utterance or from **structured context** (e.g. “multi-account” mentioned → elevate **AWS Cloud** persona priority).
2. **Projected rules** from **ste-rules-library** (and similar governance surfaces) that state *when* the Architect agent must run which persona—for example “any design touching cross-account trust MUST invoke Security + AWS Cloud personas before logical closure.”
3. **Constraints on system shape** (what is allowed, mandatory, or forbidden) are part of the **authoritative** artifact set—not side notes. Projections from the rules library express **durable** obligations; they do not evaporate after the chat ends.
4. **ADRs enact** those obligations for **this** program: they record **accepted** architecture—decisions, invariants, boundaries—so the governed “shape” of the system is **declared** in the same documentation-state layer as human intent.
5. **STE reasons over the total system model**: canonical **intent and ADRs**, **derived Architecture IR**, **runtime/evidence** where applicable, **and** the **rules and invariants** that remain in force—including the parts **enacted and specialized** by ADRs. Persona probes in conversation are an **early** view of that same bundle; later lifecycle stages **evaluate** conformance against the **whole** graph, not ADRs in isolation.

The dialogue below **simulates** steps 1–2 with **hand-authored** persona tags. In production STE, **persona activation** should be **explainable** (“Security persona fired because rule **R-…** projected from ste-rules-library for `cross_account_boundary`”).

## How to read the speakers

| Speaker | Role |
|---------|------|
| **You** | Single user (design owner). You drive goals and trade-offs. |
| **CE** | **Conversation engine** — keeps turns coherent, **explains** when the user is unclear (options, risks, common meanings), summarizes, checks for gaps. |
| **Architect agent** *(persona: …)* | **Architect agent** with an **active persona** named in parentheses. Each turn is a **probe** that persona would own. |

Together, **CE + Architect agent** simulate **governed design chat**: the CE **teaches the design space** when needed; the Architect agent **pulls** specificity through **persona-shaped** questions until the model is **narrow enough** for a requirements snapshot and ledger.

## Where this chapter sits in the STE control loop

This conversation is **not** a sidebar to engineering. In STE, **governed design chat** is how **intent is captured and bounded** before it hardens into documents the toolchain can reason over.

**Flow (conceptual):**

1. **This conversation** narrows the design space and surfaces **commitments**, **constraints**, and **open questions**.
2. The CE’s **convergence summary** becomes the **prose precursor** to the **Requirements Snapshot** ([Step 1](./01-requirements-snapshot.md))—stable ids, capabilities, invariants, constraints, NFRs.
3. Anything still **under-specified** (how schedules bind to resources, where state lives, periodic evaluation shape, trust packaging) becomes **Decision Ledger** rows ([Step 2](./02-decision-ledger.md)) that **logical ADRs** must later resolve—without inventing a parallel decision list.
4. **ADRs**, **Architecture IR**, **EDR**, and drift checks **trace back** to what was said (or explicitly deferred) here.

STE starts with a **governed design conversation** that converges into **structured intent**; the rest of the example is the control loop operating on that intent.

**Transcript vs trace notes:** Lines labeled **You**, **CE**, and **Architect agent** are the **simulated chat**. The design owner’s turns (**You**) use plain ALL CAPS for emphasis, not Markdown bold in the dialogue. Lines beginning with **`[Trace → …]`** are **handbook-only**: they show how an utterance feeds **requirements**, **ledger questions**, **logical ADR topics**, and (sparingly) **physical** design—for the reader, not an in-product UI.

**Pacing:** The CE sometimes sends **several short turns in a row**—the way a design partner **explores options** before locking in—instead of one dense paragraph.

---

## 1. Problem statement (cost, always-on non-prod)

**You:** Our AWS bill is loud for what we actually use. Dev and test EC2 and RDS basically sit there 24/7 burning money.

**You:** I just want them OFF when nobody’s using them, you know what I mean.

[Trace → Requirement: **RQCAP-5181** — cost-driven expectation of **power management** for non-prod compute and databases; seeds the capability row in the Requirements Snapshot.]

---

## 2. Clarify automation shape (schedule vs idle vs manual)

**CE:** I’ll unpack that—we shouldn’t bake in the wrong **automation shape**.

**CE:** When someone says “**shut things off**,” it usually means one of three things:

- **(a) Clock-based** — fixed windows (evenings, nights, weekends, or explicit weekday hours).
- **(b) Idle-based** — stop when there’s been **no traffic / no work** for a while.
- **(c) Ad hoc** — whoever remembers clicks **Stop** in the console.

**CE:** **(c)** doesn’t scale.

**CE:** **(b)** can save money, but it needs **trustworthy idle signals**. **RDS** and **long batch jobs** are easy to misread as “idle”—if we guess wrong, we **hurt** people.

**CE:** **(a)** is the boring default for non-prod: **predictable**, **easier to audit** (named schedules, IAM tied to that story), and it matches the **nights-and-weekends** energy you started with.

**CE:** Unless you **want** to chase idle detection, I’ll steer the next questions toward **(a)** for non-prod **EC2/RDS**. I’ll also keep **“no babysitting one-off scripts”** as part of the **operator** goal.

**CE:** **Does that match what you meant?**

**You:** (a). I wasn’t specific enough. I want them OFF nights and weekends, and SCHEDULABLE on weekdays.

**CE:** **Tradeoff, explicit:** **Idle (b)** might squeeze more savings, but we’d owe the org **signal engineering**, **false-positive playbooks**, and a harder **audit** story. **Clock (a)** trades some savings for **predictability** and **reviewable** intent.

**You:** I’ll take the trade. (a). I’m not productizing “are we idle yet?” for v1.

[Trace → Decision (conversation): **clock-based** automation for v1; **idle** deferred.]

[Trace → Invariant: **RQINV-5181** — automation should stay bound to **declared** time policy (supports “no silent ad-hoc path” later).]

[Trace → Decision Ledger Question: **LDEC-5182** — unit of **periodic evaluation** (interval/batch) ties to clock-based orchestration.]

[Trace → Logical ADR topic: **ADR-L-INST-001** (scheduling domain).]

---

## 3. Scope (non-prod first, EC2 and RDS)

**CE:** **Bounded** on shape: **cost and toil** are the headline; **clock-based non-prod EC2/RDS** is the **North Star**—**dark** nights and weekends, **named weekday windows** you can tune—not idle guessing. I’m **routing** to the **Architect agent**: **FinOps** first (scope/economics), then **Security**, **AWS Cloud**, and **Operations** as signals warrant.

> **Reader note (not in-chat):** In a full STE loop, **ste-rules-library** projections would typically **sequence** those personas when **signals** and **phase gates** match the active rule bundle.

**Architect agent** *(persona: FinOps)*: Which **environments** are in scope first—non-prod only, or prod too? Any **minimum uptime** windows we must never cross (e.g. nightly batch)?

**You:** NON-PROD FIRST. Prod is later-if-ever, not v1. No sacred “always-on” batch story in those accounts. If we break something we’ll WIDEN windows on purpose, not by accident.

[Trace → Requirement: scope boundary for **RQCAP-5181** (non-prod v1; prod explicitly out of initial commitment).]

---

## 4. Environments (single-account vs multi-account)

**Architect agent** *(persona: Security)*: Any automation that **starts and stops** instances needs a clear **trust story**. Are you okay with a **dedicated orchestration identity** that calls EC2/RDS APIs, with **everything auditable**—both **who changed policy** and **what the automation actually did**—and **no** ad-hoc console clicks as the “real” control plane?

**You:** Yeah. ONE path. IAM and CloudTrail, so six months from now I’m not reconstructing “who touched prod” from Slack scrollback.

**You:** Not a pile of tribal runbooks, and I’m NOT doing “give everyone PowerUser and hope.”

**Architect agent** *(persona: AWS Cloud)*: Is this **one AWS account** or many? Do you use **Organizations**, or might some teams stay isolated for a while?

**You:** We’re mostly on Org, but SINGLE-ACCOUNT STILL HAS TO WORK. I’m not arm-wrestling every LOB into the same landing zone on day one.

**You:** I don’t know what big-company “normal” is here. PICK SOMETHING SANE and explain it in English.

[Trace → Requirement: **RQCAP-5182** — optional **cross-account** story must coexist with **single-account** realism.]

[Trace → Invariant: **RQINV-5181** — single **auditable** control path (no parallel “shadow ops”).]

[Trace → NFR: **RQNFR-5182** — **operational visibility**: evidence for **configuration changes** and **automation actions** (feeds audit/ops expectations in the snapshot).]

[Trace → Logical ADR topic: **ADR-L-INST-002** (trust and account topology).]

---

## 5. Topology (hub vs per-account control plane)

**CE:** Fair—“**normal**” isn’t one design. Some enterprises **centralize** in one account; others **isolate** every LOB. Neither is automatically **safer** or **cheaper**—it’s a **governance** choice. From your last line I’m going to **encode**: **single-account** must work **without** pretending everyone is multi-account, **and** when you **do** use many accounts, we need a **documented** trust pattern—not ad hoc sharing of root keys.

**CE:** **Topology tradeoff**, plain English:

- **Per-account scheduler** — smaller **blast radius** per component, but **N** deployments, **N** config drifts, harder **standard audit** across the estate.
- **Hub account** — one place to **review** orchestration and **correlate** logs; the trade is a **sensitive hub** we must **lock down** and **least-privilege** into spokes.

**You:** I’ll take the HUB trade IF the spoke side is boring and SCOPED: I’m not accepting “scheduler can power-cycle the universe.”

[Trace → Decision (conversation): **hub + spoke** for multi-account, with **explicit** least-privilege into member accounts.]

[Trace → Decision Ledger Question: **LDEC-5183** — how **multi-account trust** is packaged (spoke stack, roles, parameters).]

[Trace → Logical ADR topic: **ADR-L-INST-002**.]

---

## 6. Trust and IAM (blast radius, reviewability)

**Architect agent** *(persona: AWS Cloud)*: For **multi-account**, are you comfortable with a **hub** that runs the scheduler and **spoke** accounts that only grant **least privilege** to that hub—**documented in templates**, not hand-wired trust?

**You:** Fine, if I can SEE the blast radius and IAM diffs go through the same review as every other infra change, I’m good.

**Architect agent** *(persona: Security)*: Some designs use a **broad org-wide** power role so “automation is easy.” That’s the opposite of what you just said. Are we **ruling that out**?

**You:** RULED OUT. I don’t want a SINGLE role that can START/STOP EVERYTHING everywhere “because platform.” If we need power, it needs to be EXPLAINABLE and SCOPED to what this system actually does.

[Trace → Invariant: **RQINV-5182** — spoke roles **scoped** to the **scheduler principal** and **actions required** (no org-wide generic power role).]

[Trace → Physical-System design: **hub** runs orchestration; **spokes** hold **resource-scoped** trust—later detailed in physical/spoke ADR material.]

---

## 7. Opt-in model (tags vs registry)

**Architect agent** *(persona: Operations)*: How should teams **opt in**? New CMDB, or something already on resources?

**You:** We already TAG for ownership. Hang the schedule off a TAG and teams opt in by tagging. I’m NOT standing up a CMDB for this.

[Trace → Decision (conversation): **tag-driven** opt-in.]

[Trace → Decision Ledger Question: **LDEC-5181** — how schedules **attach** to resources (**tags** vs external registry).]

[Trace → Logical ADR topic: **ADR-L-INST-001**; Physical-Component responsibility: **tag discovery / resource binding** (later component ADR).]

---

## 8. Operator experience (CLI/API vs only CloudFormation)

**Architect agent** *(persona: FinOps)*: **RDS** as well as EC2—same **schedule vocabulary** where possible?

**You:** Same vibe: ONE vocabulary for humans. RDS can be weird under the hood; I still don’t want two different languages for humans.

**CE:** When we say **one vocabulary**, we mean a **small stable set of concepts** teams can learn once—typically **schedules**, **periods**, and **time zones**—not ad hoc strings per service. That’s what we’ll ask doc and tooling to preserve.

**Architect agent** *(persona: Operations)*: Operators will need something beyond **only** CloudFormation for **day-2** schedule tweaks—CLI or internal tooling. Is that in scope for “acceptable operator experience”?

**You:** Yeah, templates for DEPLOY, fine. But day-two tweaks need CLI OR API; I’m not filing a stack update every time someone shifts office hours.

[Trace → Constraint: **RQCONST-5182** — customer-facing configuration uses **stable concepts** (schedules, periods, time zones).]

[Trace → Decision Ledger Question: **LDEC-5181** (binding + vocabulary coherence).]

---

## 9. Control plane style (managed services vs custom controller)

**Architect agent** *(persona: FinOps)*: Cheap pattern historically: a **small always-on instance** with a cron job and some scripts. Fits “we already have a bastion.” Want that?

**You:** NO. I’m not running a PET scheduler fleet we patch, rotate, and babysit. If this is real, it needs to look like PLATFORM: MANAGED building blocks, REPEATABLE deploy, THE SAME ops model as the rest of our AWS stuff.

**CE:** Captured: prefer **managed primitives** for the **control plane** (orchestration, state, APIs)—not a **custom** always-on **controller VM** pattern.

[Trace → Constraint: **RQCONST-5181** — control plane built from **AWS-managed** primitives (aligns with Lambda/EventBridge/DynamoDB-shaped solutions).]

[Trace → Decision Ledger Question: **LDEC-5184** — where **configuration, state, and registry** records live (follows from managed, API-addressable design).]

[Trace → Physical-System design: **serverless / managed** data and compute tier (later CDK-aligned physical design).]

---

## 10. Convergence summary (bounded intent)

**Architect agent** *(persona: Operations)*: Last ops check: schedules will be evaluated on a **cadence**—minutes granularity, not “once a day surprises.” Acceptable?

**You:** Acceptable. Non-prod can tolerate A FEW MINUTES of skew if the BEHAVIOR is predictable.

[Trace → NFR: **RQNFR-5181** — **configurable** scheduling **interval** (minutes-scale evaluation cadence).]

**CE:** **Convergence check** — bounded intent we’re recording:

- **Capabilities:** **Clock-based** start/stop for **EC2 and RDS** in **non-prod** first—**off** nights and weekends, **configurable weekday** windows; **optional** **multi-account** via **hub + spoke** with **documented** IAM; **tag-driven** opt-in.
- **Invariants:** **No** stop/start outside **declared** schedule bindings and **registered** trust; **no** parallel “shadow” control plane; **spoke** access **least-privilege** to the **hub scheduler principal**—**no** org-wide generic power role.
- **Constraints:** Control plane **prefers managed AWS constructs**; customer-facing config uses **stable concepts**—**schedules**, **periods**, **time zones**.
- **NFRs:** **Configurable evaluation interval** (minutes-scale); **operational visibility**—logs/metrics/alarm hooks enough to audit **who changed policy** and **what ran against resources**.
- **Scope:** **Non-prod** for v1; **prod** explicitly **not** committed; **EC2 + RDS**.
- **Trust model:** **Hub/spoke** when multi-account; **single-account** must remain a **valid** deployment shape.
- **Operator interface:** **IaC for deploy**; **CLI/API** for **day-2** schedule and config tweaks.
- **Deferred / ledger-sized:** exact **attachment** mechanics, **evaluation** implementation choice, **trust packaging**, and **persistence** layout—those become **Decision Ledger** questions, not guesses in chat.

This summary is the **prose precursor** to the **Requirements Snapshot** ([Step 1](./01-requirements-snapshot.md)). Anything we **deferred** becomes **Decision Ledger** rows ([Step 2](./02-decision-ledger.md)) that **logical ADRs** must **resolve**—so nothing “appears from nowhere” in later steps.

**You:** Yep, that’s the record. LOCK IT IN.

---

## 11. Trace ID table (conversation → later artifacts)

| Kind | Id | Short label |
|------|-----|-------------|
| Capability expectation | RQCAP-5181 | Scheduled EC2/RDS power management |
| Capability expectation | RQCAP-5182 | Cross-account scheduling (optional) |
| Constraint | RQCONST-5181 | Prefer managed AWS constructs for control plane |
| Constraint | RQCONST-5182 | Stable schedule vocabulary (schedules, periods, time zones) |
| Invariant | RQINV-5181 | Schedule/trust-bound automation only |
| Invariant | RQINV-5182 | Least-privilege spoke access for scheduler |
| NFR | RQNFR-5181 | Configurable scheduling interval (minutes-scale) |
| NFR | RQNFR-5182 | Operational visibility for audit (policy vs actions) |

These ids appear again in [Step 1](./01-requirements-snapshot.md) and [Step 2](./02-decision-ledger.md). Ledger rows **LDEC-5181**–**LDEC-5184** link back to the snapshot items above.

---

## Summary

- **Governed conversation** is the **first** control-loop beat: it **bounds intent** before ids and ADRs exist.
- **Personas** stand in for **domains of concern** (cost, trust, landing zone, ops)—not flavor text.
- **Tradeoffs** (clock vs idle, hub vs per-account, managed vs pet controller) **narrow** the design space **explicitly**.
- **Trace notes** and the **id table** make **provenance** visible: later **requirements**, **ledger questions**, and **ADRs** **inherit** from what was said here.

---

**Previous:** [Part 11 examples overview](../00-overview.md) · **Next:** [Step 1 — Requirements snapshot](./01-requirements-snapshot.md)
