---
title: "Instance Scheduler example — how to read + Phase 1 (Step 0) conversation"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# How to Read This Example

This walkthrough is a **full STE lifecycle**, not a lesson in “how to write ADRs.” Read it as one thread: **intent** hardens into **decisions** and **architecture**, the architecture **compiles** into a **system model (IR)**, **implementation** links to that model, **runtime evidence** attaches back to intent, and **drift** triggers **governed correction**.

In a complete STE program, humans **do not** hand-author the **substrate**: you **talk about what you want** in governed design conversation (**Phase 1**; **Step 0** in this folder is the illustration), and STE **owns** the rest—**generating**, **validating**, and **maintaining** canonical ADRs, the **compiled system model (Architecture IR)**, and the links that make drift and evidence machine-checkable. **ADRs and IR** are **AI- and toolchain-first**; you are free to **move on to design or exploration** while STE **processes** those plans in the background.

**Losing the full shape of the system in your head is expected** at scale. **Projections** exist for **on-demand orientation**: pull the **explicit view** you need—traceability, topology, capability map—when you need to **re-ground**, without holding the entire graph in working memory.

| Phase | Steps | What you are doing |
|-------|-------|---------------------|
| **Intent** | 0–2 | **Phase 1** conversation → **Phase 2** frozen requirements → decision questions (ledger) |
| **Architecture** | 3a–5d | **ADR-L**, **ADR-PS**, **ADR-PC**, then **Phase 6 — rules activation** ([Step 5d](./05d-rules-activation.md)) |
| **Compiled model** | 6 | **Phase 7** — ADRs **compiled** into **Architecture IR** (queryable graph) |
| **Runtime + linkage** | 7 | **Phase 8** runtime inventory + **extension** — code and infrastructure linked to IR entities |
| **Evidence** | 8 | **EDR** attaches **runtime and operational** evidence to the model |
| **Governance** | 9 | **Drift** (model vs reality) becomes visible; **correction** flows back through intent or implementation |

**Step 0** below is **Phase 1 — Conversation**: a **two-role simulation** (Architect + Stakeholder)—**not** a single-user chat. In full STE, a **conversation engine**, **Steelman**, and **persona-routed** Architect probes may appear; those concerns are **folded into the Architect voice** here for readability.

---

# Step 0 — STE conversation (grounding) — Phase 1

## Purpose

Show **intent and design decisions emerging from a real architecture conversation**, not from a documentation template. A **system owner / stakeholder** states **needs and constraints** in plain language; an **Architect** **challenges assumptions**, **surfaces risks**, and **walks tradeoffs** until commitments are **specific enough** to freeze into a **Requirements Snapshot** and **Decision Ledger**. This is **design** first; later steps in the example map the resulting shape to a **public AWS reference implementation** for pedagogy—without treating that product as the subject of the chat.

In **full STE**, the same beat may include a **conversation engine (CE)** for facilitation, **Steelman** for rule- and gap-pressure, **persona routing** on the Architect side, and **toolchain-generated** ADRs. **This transcript is a slice:** only **Stakeholder** and **Architect** speak (two-role simulation), so readers can follow the **substance** of the design without extra roles in the script.

> **Illustrative only.** Pedagogical fiction; **ste-spec** (sibling repo under the workspace) is normative for Architecture IR semantics; **adr-architecture-kit** for ADR field shapes; **ste-rules-library** for how rules are authored and projected in a complete STE program.

## Full STE: personas and rule projection (sidebar)

In production, the **Architect**’s concerns are often **split across personas** (for example **FinOps**, **Security**, **AWS Cloud**, **Operations**) driven by **signals** and **ste-rules-library** projections—so cost, trust, landing zone, and ops probes are **explainable** and **repeatable**. **This dialogue** folds those concerns into a **single Architect voice**. The obligations are the same: **constraints** and **invariants** that will later appear as **canonical** rows and **ledger** questions—not informal opinions.

## How to read the speakers

| Speaker | Role |
|---------|------|
| **Stakeholder** | **System owner** — states **goals**, **constraints**, and **risk appetite**; accepts or rejects tradeoffs. |
| **Architect** | **Challenges** vague goals, **names options**, and **forces** decisions. May use **several short turns in a row** to unpack a tradeoff before asking for commitment. In full STE, this voice is often **specialized** by persona; here it is **collapsed for readability**. |
| **Steelman agent** | In full STE, **steel-mans** the **present-state** design against **rules** and **obligations**, surfacing gaps for **compliant closure** or **documented waiver**. **Not voiced** in this transcript. |

**Steelman and ADR-PC:** Steelman also carries the intent of **physical-component ADRs (ADR-PC)**: they are **executable architecture**—recorded **specifically enough** that implementation can proceed **without further human guidance** for decisions the ADR should have closed. **Underspecification** is a **gap** to **resolve** under the rules or to **waive** with **explicit acknowledgement**, same as any other obligation breach.

**Architect** in this example does **some** of the gap-surfacing **Steelman** would amplify in a full program (rule conflicts, “you said X but implied Y”). **CE** does **not** appear as a speaker; there is **no conversation engine** line in the dialogue below.

### Conversation topics → artifacts (preview)

The dialogue below is a **design session**: topics resolve into **capabilities**, **invariants**, **ledger questions**, and **logical boundaries** (later split across **ADR-L-INST-001** and **ADR-L-INST-002**). Use this table while you read the transcript.

| Conversation topic | Artifact produced (illustrative ids) |
|--------------------|--------------------------------------|
| Cost / scheduled power management | Capability (**RQCAP-5181**) |
| Multi-account + single-account realism | Capability (**RQCAP-5182**) |
| Explainability (“why stop/start”); audit trail | NFR / visibility (**RQNFR-5182**) |
| Drift detection and correction (intent) | Feeds later lifecycle; visibility (**RQNFR-5182**) |
| One auditable path; no shadow automation | Invariant (**RQINV-5181**) |
| Schedule + trust binding; no ad-hoc stop/start | Invariant (**RQINV-5181**) |
| Least-privilege; no org-wide power role | Invariant (**RQINV-5182**) |
| How schedules attach; stable vocabulary | Decision ledger (**LDEC-5181**) |
| Orchestration unit (interval vs event-driven) | Decision ledger (**LDEC-5182**) |
| Multi-account trust packaging | Decision ledger (**LDEC-5183**) |
| Where config, state, and registry live | Decision ledger (**LDEC-5184**) |
| Hub vs per-account control plane; spoke blast radius | Logical boundary → **ADR-L-INST-001** / **ADR-L-INST-002** |

## Where this chapter sits in the STE control loop

This conversation is **not** a sidebar to engineering. In STE, **governed design chat** is how **intent is captured and bounded** before it hardens into documents the toolchain can reason over.

**Flow (conceptual):**

1. **This conversation** narrows the design space and surfaces **commitments**, **constraints**, and **open questions**.
2. A **Steelman agent** (in full STE) **steel-mans** the **present-state** design against **rules** and **already accepted obligations**: it **surfaces gaps**—missing constraints, ambiguous trust, rule conflicts—so you can **define intent** and **close** those gaps in a **compliant** way, or **record** **documented acknowledgement** when you **intentionally waive** a rule. The **Architect** here performs **part** of that pressure. When later artifacts approach **physical-component** closure, the same posture applies the **ADR-PC** bar: **executable architecture** (implement **without** depending on unstated human judgment). *(This handbook transcript does not simulate Steelman dialogue; it is omitted for length.)*
3. The **Architect–stakeholder convergence summary** becomes the **prose precursor** to the **Requirements Snapshot** ([Step 1](./01-requirements-snapshot.md))—stable ids, capabilities, invariants, constraints, NFRs.
4. Anything still **under-specified** (how schedules bind to resources, where state lives, periodic evaluation shape, trust packaging) becomes **Decision Ledger** rows ([Step 2](./02-decision-ledger.md)) that **logical ADRs** must later resolve—without inventing a parallel decision list.
5. **ADRs**, **Architecture IR**, **EDR**, and drift checks **trace back** to what was said (or explicitly deferred) here—and to **compliant closure** or **recorded waiver** where Steelman forced a gap visible.

STE starts with a **governed design conversation** that converges into **structured intent**; the rest of the example is the control loop operating on that intent.

**Transcript vs trace notes:** Lines labeled **Stakeholder** and **Architect** are the **simulated chat**. The **Steelman agent** and **CE** are **not** voiced here (see table above). The stakeholder’s turns use plain ALL CAPS for emphasis, not Markdown bold in the dialogue. Lines beginning with **`[Trace → …]`** are **handbook-only**: they show how an utterance feeds **requirements**, **ledger questions**, **logical ADR topics**, and (sparingly) **physical** design—for the reader, not an in-product UI.

**Pacing:** The **Architect** sometimes sends **several short turns in a row**—the way a design partner **explores options** before locking in—instead of one dense paragraph.

---

## 1. Problem, platform bar, and safety posture

**Stakeholder:** We need a system that **automatically starts and stops EC2 and RDS** on a **schedule** to reduce cost—not a project that lives in someone’s shell history.

**Stakeholder:** It must support **multiple AWS accounts**, stay **safe** so we do not stop **critical** systems by accident, stay **auditable**, and be **centrally governed** while still operating in member accounts.

**Stakeholder:** **Least privilege** across accounts. **No** relying on humans SSHing in to run scripts. When an instance state changes, we must be able to answer **why**—for ops and for audit.

**Stakeholder:** We need **drift** handled: if someone **manually** changes IAM, tags, or parameters outside the governed path, we **detect** that and **correct** or **escalate** under change control—not discover it from a surprise bill.

**Stakeholder:** Schedules and **run state** must **persist**. The system must **run continuously**—not a nightly job everyone forgets.

[Trace → Requirement: **RQCAP-5181** — cost-driven expectation of **power management** for compute and databases; seeds the capability row in the Requirements Snapshot.]

**Architect:** Good—stated as a **platform**, not a script. On **safety**, there are three common patterns: **allowlist** only explicitly enrolled resources; **denylist** “never touch” classes; **approval workflow** per disruptive action.

**Architect:** Allowlist + explicit schedule binding is usually the right cost/automation fit. Pure denylist (“do not touch prod”) without positive binding still leaves gray area. **Per-stop approvals** do not scale at hundreds of instances.

**Stakeholder:** I want **positive binding**: only resources that are **explicitly** tied to a declared schedule—and **registered** trust—get automated power actions. No “we implied it was okay.”

**Architect:** That implies **no parallel ad-hoc** automation path as the real control plane—otherwise audit breaks.

**Stakeholder:** ONE governed path. IAM and CloudTrail, not Slack archaeology.

[Trace → Invariant: **RQINV-5181** — single **auditable** control path; schedule/trust-bound automation (supports “no silent ad-hoc path” in the snapshot).]

---

## 2. Automation shape (clock vs idle vs manual)

**Architect:** “Shut things off” still splits three ways: **(a) clock windows**, **(b) idle detection**, **(c) ad hoc** console or CLI by whoever is awake.

**Architect:** **(c)** fails your **governance** bar. **(b)** can save more money but needs **trustworthy idle signals**—**RDS** and long jobs are easy to misread; false stops are a **safety** incident.

**Architect:** **(a)** trades some savings for **predictability** and **reviewable** intent—named windows, easier tie to **why** something stopped.

**Stakeholder:** **(a)**. OFF nights and weekends; **configurable** weekday on/off. I am not standing up “are we idle yet?” as a product for v1.

[Trace → Decision (conversation): **clock-based** automation for v1; **idle** deferred.]

[Trace → Invariant: **RQINV-5181** — automation bound to **declared** time policy (reinforces schedule-bound posture).]

[Trace → Decision Ledger Question: **LDEC-5182** — unit of **periodic evaluation** (interval/batch) ties to clock-based orchestration.]

[Trace → Logical ADR topic: **ADR-L-INST-001** (scheduling domain).]

---

## 3. Scope (environments and services)

**Architect:** **Environments** for v1—**non-prod** only first, or **prod** in scope on day one? Any **always-on** commitments we must never violate in those accounts?

**Stakeholder:** **NON-PROD FIRST**. Prod is later-if-ever for v1. If we break something we **widen** windows on purpose—not by silent automation roulette.

**Architect:** **Services**—**EC2 and RDS** both, or split the problem?

**Stakeholder:** **Both**. Same human-facing story for teams where possible.

[Trace → Requirement: scope boundary for **RQCAP-5181** (non-prod v1; prod explicitly out of initial commitment; EC2 + RDS).]

---

## 4. Explainability, audit, and observability tradeoffs

**Architect:** “Why was this instance stopped?” needs a **decision record**: schedule id, evaluation window, resource binding, principal. For **observability**, options are **logs only**, **structured events** on a bus, or pushing summaries into an **audit database**.

**Architect:** Logs-only is cheapest but harder to **correlate** across accounts. **Structured events** improve **cross-service** stitching. A dedicated **audit DB** is powerful and expensive—you own schema, retention, and access control.

**Stakeholder:** I need enough to **prove** posture to security and FinOps: **who changed policy**, **what the automation did**, and **hooks** for alarms—not a science project. **Logs + metrics + alarm hooks** are the minimum; we can grow toward richer **event** shapes if the control plane supports it.

[Trace → NFR: **RQNFR-5182** — **operational visibility**: evidence for **configuration changes** and **automation actions** (feeds audit/ops expectations in the snapshot).]

[Trace → Logical ADR topic: **ADR-L-INST-002** (trust and account topology) when cross-account **correlation** matters.]

---

## 5. Accounts, topology, and multi-account mechanics

**Architect:** **Single account** today, **Org** tomorrow—is **single-account** still a **valid** deployment?

**Stakeholder:** **Yes.** Not every LOB lands in the same pattern on day one.

**Architect:** For **multi-account**, mechanics vary: **central AssumeRole** into member roles; **agents** running in each account; **stack-set**-style **registration** artifacts per spoke. The trade is **operational uniformity** vs **blast radius** and **drift** across **N** copies.

**Architect:** **Topology**: **fully distributed** scheduler in every account vs a **hub** that **orchestrates** with **least-privilege** spokes.

**Architect:** Distributed reduces **central** sensitivity but multiplies **deployments** and **config drift**. A **hub** concentrates review and **logging correlation**; you must **lock down** the hub and **scope** spoke trust.

**Stakeholder:** **Hub** is acceptable if spokes are **boring** and **scoped**—no “scheduler can power-cycle the universe.”

[Trace → Requirement: **RQCAP-5182** — optional **cross-account** story must coexist with **single-account** realism.]

[Trace → Decision (conversation): **hub + spoke** for multi-account, with **explicit** least-privilege into member accounts.]

[Trace → Decision Ledger Question: **LDEC-5183** — how **multi-account trust** is packaged (dedicated spoke stack, central assume-role patterns, org integrations—ledger alternatives).]

[Trace → Logical ADR topic: **ADR-L-INST-002**.]

---

## 6. Trust model and IAM blast radius

**Architect:** Some orgs install one **broad org-wide** power role so automation is “easy.” That melts **reviewability** and **blast radius**.

**Architect:** The alternative is a **hub principal** plus **scoped spoke roles**—more **IAM** files, but each attachment is **explainable** and maps to **this** workload.

**Stakeholder:** **RULED OUT** on mega-role. No single identity that can **start/stop everything** “because platform.” **Explainable** and **scoped** only. IAM diffs go through the **same** review as other infra.

**Architect:** Good—trust is **template-driven**, not hand-wired keys.

[Trace → Invariant: **RQINV-5182** — spoke roles **scoped** to the **scheduler principal** and **actions required** (no org-wide generic power role).]

[Trace → Physical-System design: **hub** runs orchestration; **spokes** hold **resource-scoped** trust—later detailed in physical/spoke ADR material.]

---

## 7. How schedules attach (tags vs central registry)

**Architect:** **Attachment**: **resource tags**, a **central registry**, or **hybrid**. Tags ride on what teams already do; a registry adds **control** and **migration** cost.

**Stakeholder:** We already **tag** for ownership. **Hang schedules off tags**—teams opt in by tagging. I am **not** funding a CMDB for this v1.

[Trace → Decision (conversation): **tag-driven** opt-in.]

[Trace → Decision Ledger Question: **LDEC-5181** — how schedules **attach** to resources (**tags** vs external registry).]

[Trace → Logical ADR topic: **ADR-L-INST-001**; Physical-Component responsibility: **tag discovery / resource binding** (later component ADR).]

---

## 8. Human vocabulary and day-2 operations

**Architect:** **EC2 and RDS** under the hood differ; for humans we should keep **one vocabulary**—typically **schedules**, **periods**, **time zones**—not bespoke strings per service.

**Architect:** For **day-2** tweaks, **IaC-only** is painful. Do you accept **CLI or API** for schedule changes without a full stack redeploy?

**Stakeholder:** **Templates for deploy**, yes. **CLI or API** for day-two—I am not opening a stack update ticket every time office hours shift.

[Trace → Constraint: **RQCONST-5182** — customer-facing configuration uses **stable concepts** (schedules, periods, time zones).]

[Trace → Decision Ledger Question: **LDEC-5181** (binding + vocabulary coherence).]

---

## 9. Control plane and persistence shape

**Architect:** Classic anti-pattern: a **pet EC2** with cron. Fits “we have a bastion” culture; fails **patching**, **rotation**, and **scale**.

**Stakeholder:** **No pet fleet.** **Managed** building blocks, **repeatable** deploy, same **ops model** as the rest of our cloud estate.

**Architect:** Then we need an **API-addressable** home for **config**, **runtime state**, and **registry** rows. **DynamoDB-style** keyed access fits **high-churn** automation; **RDS** helps **relational reporting** but adds **ops** surface; **S3 manifests** are simple and weak for **concurrent** writers and **fine-grained** queries.

**Stakeholder:** **Keyed lookups** for operational truth—no DBA ticket to explain “why this never stopped.” We will consciously pick a **fast document/key store** shape, own **metrics and alarms** on it, and not let tables become **mystery sprawl**.

[Trace → Constraint: **RQCONST-5181** — control plane built from **AWS-managed** primitives (Lambda/EventBridge/data-plane patterns).]

[Trace → Decision Ledger Question: **LDEC-5184** — where **configuration, state, and registry** records live (**dynamodb_tables** vs **rds** vs **s3_manifests** in the ledger).]

[Trace → Physical-System design: **serverless / managed** data and compute tier (later CDK-aligned physical design).]

---

## 10. Orchestration unit (interval vs event-driven)

**Architect:** Clock-based intent still needs an **orchestration unit**: **periodic evaluation** (“what should be running now”) vs **purely event-driven** reactions. **Event-only** can look elegant; **EC2/RDS** life-cycle and **audit replay** often want a **bounded evaluation slice**.

**Stakeholder:** **Minutes-scale** batch is fine if the story is “converges within **N** minutes,” not random surprises. **Predictable** beats **clever** for non-prod cost work.

[Trace → Decision Ledger Question: **LDEC-5182** — **fixed_interval_lambda** vs **streaming_events_only** vs mixed; conversation commits to **interval-shaped** orchestration for v1.]

---

## 11. Drift, misconfiguration, and evidence hooks

**Architect:** Two recurring failures: **tag or parameter drift**—resources **silently** stop matching schedules—and **IAM break-glass** that never gets removed. **Drift detection** needs **linkage** between **declared** config and **observed** IAM/tags plus **evidence** for remediation.

**Stakeholder:** Agreed. **Logs and metrics** tied to **schedule actions** and **config changes**, with **hooks** for **governance**. Mystery stop/start is a **failure mode**, not noise we absorb.

[Trace → NFR: **RQNFR-5182** — **operational visibility** for audit (policy vs actions); foreshadows **EDR** and **drift** in Steps 8–9 without adding new finding ids.]

---

## 12. Convergence summary (bounded intent)

**Architect:** Last check: evaluation on a **cadence**—**minutes** granularity, not once-a-day surprises. Acceptable?

**Stakeholder:** Acceptable. Non-prod can tolerate **a few minutes** of skew if **behavior** is predictable.

[Trace → NFR: **RQNFR-5181** — **configurable** scheduling **interval** (minutes-scale evaluation cadence).]

**Architect:** **Convergence check** — bounded intent we are recording:

- **Capabilities:** **Clock-based** start/stop for **EC2 and RDS** in **non-prod** first—**off** nights and weekends, **configurable weekday** windows; **optional** **multi-account** via **hub + spoke** with **documented** IAM; **tag-driven** opt-in.
- **Invariants:** **No** stop/start outside **declared** schedule bindings and **registered** trust; **no** parallel “shadow” control plane; **spoke** access **least-privilege** to the **hub scheduler principal**—**no** org-wide generic power role.
- **Constraints:** Control plane **prefers managed AWS constructs**; customer-facing config uses **stable concepts**—**schedules**, **periods**, **time zones**.
- **NFRs:** **Configurable evaluation interval** (minutes-scale); **operational visibility**—logs/metrics/alarm hooks enough to audit **who changed policy** and **what ran against resources**.
- **Scope:** **Non-prod** for v1; **prod** explicitly **not** committed; **EC2 + RDS**.
- **Trust model:** **Hub/spoke** when multi-account; **single-account** must remain a **valid** deployment shape.
- **Operator interface:** **IaC for deploy**; **CLI/API** for **day-2** schedule and config tweaks.
- **Deferred / ledger-sized:** exact **attachment** mechanics, **evaluation** implementation choice, **trust packaging**, and **persistence** layout—those become **Decision Ledger** questions, not guesses in chat.
- **Closed loop:** The ids above feed the **Requirements Snapshot**, **Decision Ledger**, **Architecture IR**, **code linkage**, **EDR**, and **drift checks** in later steps—STE treats this as a **continuous governed system**, not a one-time design write-up.

This summary is the **prose precursor** to the **Requirements Snapshot** ([Step 1](./01-requirements-snapshot.md)). Anything we **deferred** becomes **Decision Ledger** rows ([Step 2](./02-decision-ledger.md)) that **logical ADRs** must **resolve**—so nothing “appears from nowhere” in later steps.

**Stakeholder:** That is the record. **LOCK IT IN.**

---

## 13. Trace ID table (conversation → later artifacts)

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
- The **Architect** voice here carries **cross-cutting** concerns—**cost**, **safety**, **trust**, **operations**, **observability**—that **full STE** would often **route** through **personas** and **ste-rules-library** projections.
- **Tradeoffs** (allowlist vs denylist vs approval; clock vs idle vs ad hoc; hub vs distributed; AssumeRole vs agents vs registration artifacts; tags vs registry; logs vs events vs audit DB; interval vs event-driven evaluation; DynamoDB vs RDS vs manifest-style storage; mega-role vs scoped hub/spoke trust) **narrow** the design space **explicitly**—this transcript **designs** a scheduling platform; it does **not** narrate a vendor product.
- **Trace notes** and the **id table** make **provenance** visible: later **requirements**, **ledger questions**, and **ADRs** **inherit** from what was said here.

---

**Previous:** [Part 11 examples overview](../00-overview.md) · **Next:** [Step 1 — Requirements snapshot](./01-requirements-snapshot.md)
