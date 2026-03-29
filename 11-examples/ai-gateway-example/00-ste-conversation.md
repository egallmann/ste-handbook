---
title: "AI Gateway example — how to read + Phase 1 conversation"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# How to read this example (Phase 1)

This walkthrough is a **full STE lifecycle** in miniature: **intent** hardens into **decisions** and **architecture**, the architecture **compiles** into **Architecture IR**, **implementation** links to that model, **evidence** attaches, and **drift** closes the loop. **Phase 1** is the **grounding conversation**—the same beat as [Instance Scheduler Step 0](../instance-scheduler-example/00-ste-conversation.md), with a **smaller** system and **fewer** ADR files.

In a complete STE program, **Steelman** and **persona-routed** probes pressure the design against **ste-rules-library** projections. **This transcript** folds **security, FinOps, and operations** into a **single Architect voice** so readers can follow the **thread** without extra speakers.

| Phase | Steps (this folder) | What you are doing |
|-------|---------------------|-------------------|
| **Intent** | 0–2 | Conversation → **requirements snapshot** → **decision ledger** |
| **Architecture** | 3–5b | **ADR-L**, **ADR-PS**, **ADR-PC**, **rules activation** |
| **Compiled model** | 6 | **Architecture IR** |
| **Runtime + linkage** | 7 | **What runs** + embodiment linkage |
| **Evidence / governance** | 8–9 | **EDR**, **drift** |

**Step 0** below is **Phase 1 — Conversation**: a **two-role simulation** (**Stakeholder** + **Architect**).

> **Illustrative only.** **ste-spec** is normative for Architecture IR semantics.

## Purpose

Show **intent emerging from a realistic design conversation**—not a template—before [Step 1 — Requirements snapshot](./01-requirements-snapshot.md) freezes ids. Later steps stay **pedagogically aligned** to a small AWS-shaped gateway; the **chat** is about **your** platform problem, not a vendor product walkthrough.

## How to read the speakers

| Speaker | Role |
|---------|------|
| **Stakeholder** | **Product / platform owner** — goals, constraints, risk appetite; accepts or rejects tradeoffs. |
| **Architect** | **Challenges** vague goals, **names options**, **surfaces risks**; may use **several short turns** before asking for commitment. |

**Steelman** and a **conversation engine** are **not** voiced. **`[Trace → …]`** lines are **handbook-only** (trace seeds for Step 1).

**Pacing:** The **Stakeholder** uses plain **ALL CAPS** for emphasis in dialogue, not Markdown bold.

**Transcript vs trace notes:** Simulated chat first; trace lines show how utterances become **RQCAP / RQCONST / RQINV / RQNFR** rows.

### Conversation topics → artifacts (preview)

| Conversation topic | Artifact produced (illustrative ids) |
|--------------------|-------------------------------------|
| One gateway; route by policy | Capability (**RQCAP-0001**) |
| Automatic failover across providers | Capability (**RQCAP-0002**) |
| Multiple named cloud providers | Constraint (**RQCONST-0001**) |
| Normalized success contract | Constraint (**RQCONST-0002**) |
| Auth before provider; no shadow paths | Invariant (**RQINV-0001**) |
| Secrets discipline; no key logging | Invariant (**RQINV-0002**) |
| Latency / throughput bar | NFRs (**RQNFR-0001**, **RQNFR-0002**) |
| Health checks, retry budgets, secret store product | Decision ledger (Step 2) |

## Where this sits in the STE control loop

1. This conversation **narrows** the design space and surfaces **commitments** and **open questions**.
2. Anything still **fuzzy** (exact health semantics, retry caps, which secret store, streaming vs unary v1) becomes **ledger-sized** in [Step 2](./02-decision-ledger.md)—not **silent** assumptions in Step 1.
3. **ADRs** later **resolve** those questions; **IR**, **linkage**, and **EDR** **trace back** here.

---

# Step 0 — STE conversation (grounding) — Phase 1

## 1. Problem, fragmentation, and platform bar

**Stakeholder:** We have **three** LLM vendors in play. Every team ships their own **SDK spaghetti**—retries, timeouts, “oh we just call OpenAI from the service.” I want **ONE place** that **owns** routing and failure handling so we stop paying for the same incident **three** different ways.

**Architect:** When you say **one place**, is that **mandatory** for all new code on day one, or do you expect a **long tail** of direct calls we have to **sunset**?

**Stakeholder:** **Mandatory for new** external LLM traffic. Existing stuff gets a **migration lane**—I am not pretending we flip a switch overnight—but **no new** “just import the vendor SDK in the monolith” without going through the gateway.

**Architect:** Good—that is a **governance** statement, not only a **library**. Risk: if the gateway is **optional**, you will still get **shadow** paths the moment someone is in a hurry.

**Stakeholder:** Then treat **shadow paths** as **technical debt with a name**. The **platform bar** is: **customer-facing and partner** API traffic goes through the gateway for v1. Internal batch can wait—we are not optimizing cold-start batch here.

[Trace → Capability seed: **RQCAP-0001** — **central AI request routing** for **edge** traffic; implies **policy-owned** path vs ad hoc SDK use.]

---

## 2. Scope, edge first, callers, and deferrals

**Architect:** **Edge** means **your** public/partner HTTP surface—confirm **no** requirement yet for **async** workers pulling from queues?

**Stakeholder:** **Correct for v1.** If we need queue consumers later, that is a **second** conversation—we should not **pretend** one Lambda shape fits both.

**Architect:** **Unknown** worth parking early: who **authenticates** the caller—API gateway only, or does the gateway **trust** an internal auth service?

**Stakeholder:** We **already** have bearer validation **upstream** of business logic today. I want the gateway to **assume** “caller identity is **resolved** before we pick a provider”—exact **wiring** can be ledger work, but the **bar** is **no anonymous** fan-out to paid APIs.

[Trace → Invariant seed: **RQINV-0001** — **authenticated** traffic before **provider** routing; mechanism deferred to ledger / ADR.]

---

## 3. Routing intent versus failover

**Stakeholder:** Routing is not only “pick OpenAI.” We need **policy**: **tenant tier**, **data sensitivity**, maybe **cost cap** per request class. Failover is the **other** half—when **provider A** is **down** or **rate-limited**, we **shift** without every app recompiling.

**Architect:** Those are **two** pressures: **static policy** (which provider for workload class) vs **dynamic** health. Mixing them in one **if-statement** in each service is how you got here.

**Architect:** For **dynamic** cutover, are we okay with **stale** health—**last N minutes** of errors—or do you need **synchronous** health probes on **every** request?

**Stakeholder:** I am **not** requiring per-request probes on v1—that sounds like **latency** suicide. I want **bounded** behavior: **automatic** move on **clear** failure signals, with **ceilings** on retries so we do not **DDOS ourselves** against a burning vendor.

[Trace → Capability seed: **RQCAP-0002** — **provider failover** with **automation**; **retry bounds** → ledger.]

---

## 4. Failure modes, ambiguity, and iteration

**Architect:** **Ambiguity:** is **throttling** (429) the same class as **5xx** for failover? Some teams **back off**; others **rotate** provider immediately.

**Stakeholder:** **Unknown** for v1 policy detail—I want **both** to be **governed** outcomes, not developer taste. **Record** that we need a **default** and **tunables** per route class.

**Architect:** **Risk:** **all** providers unhealthy—what should the **client** see? **Synthetic** “try later” vs **propagate** last error?

**Stakeholder:** **Honest errors** beat **magic**. We still need a **consistent** **envelope** so clients are not parsing three **different** failure JSON blobs—that is part of the **platform** promise.

[Trace → Constraint seed: **RQCONST-0002** — **normalized** client-visible contract on **success**; **error envelope** intent feeds same constraint row / ledger nuance in Step 2.]

**Architect:** **Tradeoff:** **fail open** (degrade features) vs **fail closed** (hard error). Product call?

**Stakeholder:** **Fail closed** for **paid** external calls—**no silent** freeform fallback that **ships** PII to the wrong jurisdiction. If we add **degrade** later, it is **explicit** policy, not an accident.

---

## 5. Response contract, errors, and streaming deferral

**Architect:** Providers disagree on **token** fields, **finish_reason**, **tool** calls. Do we **hide** that behind a **single** response schema on the **happy path**?

**Stakeholder:** **Yes on happy path.** Internally we can keep **provider diagnostics** for **ops**, but **apps** should see **one** shape for “completion succeeded.”

**Architect:** **Streaming**—SSE chunking—is that **in** v1 or **explicitly out**?

**Stakeholder:** **OUT for v1 API** unless we **already** commit the **contract** this quarter. I would rather **ship** unary **well** than **half** stream and **break** mobile clients. **Unknown** logged: streaming is a **fast follow** with its **own** ADR.

[Trace → Decision (conversation): **unary** v1 scope; **streaming** explicitly **deferred**—feeds ledger / later ADR, not silent requirement.]

---

## 6. Authentication boundary, secrets discipline, blast radius

**Architect:** **Secrets:** are provider keys **ever** on developer laptops for **prod-equivalent** tests?

**Stakeholder:** **NO.** Central store only for paths that can hit **real** providers. **No** keys in **logs**, **traces**, or **support tickets**—if debug needs a **redacted** trace id, fine.

[Trace → Invariant seed: **RQINV-0002** — **provider credentials** never logged or exposed.]

**Architect:** **Blast radius:** one **gateway** role with **all** keys vs **partitioned** secrets per provider or per **tenant class**?

**Stakeholder:** I want **partitioning** **eventually**. For v1 I will accept **one** gateway **execution role** **if** access is **tight** and **audited**—but **record** that **tenant-isolated** keys are on the **roadmap**, not **forgotten**.

[Trace → Ledger pressure: secret **partitioning** vs **single** role—**LDEC** candidates in Step 2; ties to **RQCONST-0001** multi-provider reality.]

---

## 7. Data handling, logging risk, observability bar

**Architect:** **Risk:** prompts can contain **PII**. Default logging often **captures** bodies. What is the **minimum** **observability** you need without **storing** prompts?

**Stakeholder:** **Request id**, **route id**, **provider id**, **latency breakdown**—gateway vs provider. **No** full **prompt/response** bodies in **INFO** logs in **prod**. If **debug** is required, **time-boxed** **elevated** logging with **approval**—that is **process**, but the **architecture** has to **allow** **redaction** hooks.

**Architect:** So **operational** proof is **metrics + structured fields**, not **payload archaeology**.

**Stakeholder:** Right. I still need to **answer** “**why** did we **route** here?” for **incident** review—that is **metadata**, not **content**.

[Trace → NFR / visibility seed: ties to **RQNFR-*** **and** later EDR posture; **prompt logging** → ledger / ADR-PC **test** strategy.]

---

## 8. Latency, throughput, and honest unknowns

**Architect:** You said **boring**—translate to **numbers**. **P95** for **your** hop only?

**Stakeholder:** **Under half a second P95** for the **gateway** piece under **normal** load—not counting **provider** **thinking** time. We are not **magicians**.

**Architect:** **Throughput:** what **sustained** RPS **must** pass **load** **before** GA?

**Stakeholder:** **1k RPS** **sustained** for the **launch** tenant **suite** in **soak**. If **sales** promises **more**, we **re-open** capacity—**do not** **encode** **10x** **hope** as a **silent** **assumption**.

[Trace → NFR seeds: **RQNFR-0001**, **RQNFR-0002**.]

**Architect:** **Unknown:** **cold start** sensitivity—**interactive** **UX** vs **batch**—you already **scoped** **edge**; still worth **recording** that **autoscaling** **shape** is **ledger** work.

**Stakeholder:** Agreed. **I am not** picking **Fargate vs Lambda** in this room—I want the **SLO** **fixed** and the **compute** choice to be **explicit** later.

[Trace → Constraint seed: **RQCONST-0001** — **multiple named** cloud **LLM** providers; **technology signal** `serverless` stays a **hint** until **ADR-L** closes compute.]

---

## 9. Operations posture and single funnel

**Architect:** **On-call**—when **providers** **degrade**, do you want **runbooks** tied to **route** **classes** and **automatic** **failover**, or **human** **toggle**?

**Stakeholder:** **Automatic** for **transient** **HTTP** **failures** we already **agreed**. **Human** for **policy** changes—**pricing**, **new** vendor, **jurisdiction**—those go through **change** **control**, not **PagerDuty** **creativity**.

**Architect:** That matches a **single** **funnel**: **config** **changes** are **auditable**; **runtime** **adaptation** is **algorithmic** within **bounds**.

**Stakeholder:** **ONE** **governed** **path** for **new** **LLM** **traffic** in v1. I am **tired** of **proving** **security** **posture** **team** by **team**.

[Trace → Reinforces **RQCAP-0001** **platform** **funnel**; pairs with **RQINV-0001** **auth** **boundary**.]

---

## 10. Convergence summary (bounded intent)

**Architect:** **Last pass**—what are we **recording** as **v1** **intent** vs **explicit** **deferrals**?

**Stakeholder:** **Recording:** **Edge** **gateway**; **policy** **routing** **plus** **automatic** **failover** **within** **bounds**; **normalized** **success** **contract**; **auth** **before** **providers**; **central** **secrets**; **no** **payload** **logging** **by** **default**; **P95** / **RPS** **bars** **as** **stated**.

**Stakeholder:** **Deferring:** **streaming** **API**; **batch** **workers**; **exact** **retry** **and** **health** **semantics**; **secret** **partitioning** **layout**; **compute** **shape** (**Lambda** vs **containers**). Those become **ledger** **rows** and **ADRs**—**not** **mystery** **defaults**.

[Trace → **Requirements** **snapshot** **feeds** [Step 1](./01-requirements-snapshot.md); **ledger** **feeds** [Step 2](./02-decision-ledger.md).]

**Stakeholder:** **LOCK** **that** **record**.

---

## 11. Trace ID table (conversation → later artifacts)

| Kind | Id | Short label |
|------|-----|-------------|
| Capability | RQCAP-0001 | Central routing / single funnel (edge v1) |
| Capability | RQCAP-0002 | Provider failover with bounded automation |
| Constraint | RQCONST-0001 | Multiple named cloud LLM providers |
| Constraint | RQCONST-0002 | Normalized client contract (success + honest errors) |
| Invariant | RQINV-0001 | Authenticate before routing to providers |
| Invariant | RQINV-0002 | Provider credentials never logged or exposed |
| NFR | RQNFR-0001 | Gateway hop P95 latency bar |
| NFR | RQNFR-0002 | Sustained RPS soak bar |

These ids appear again in [Step 1](./01-requirements-snapshot.md). **Ledger** questions (**LDEC-0001** …) are introduced in [Step 2](./02-decision-ledger.md)—they **close** **deferred** **mechanisms** **without** **contradicting** this **chat**.

---

## Problem statement (record)

Deliver a **governed AI gateway** for edge traffic that routes requests under policy, fails over across multiple cloud LLM providers within bounded automation, exposes a normalized client contract on success (with honest, consistent errors), and meets explicit latency and throughput expectations—while enforcing authentication before provider calls and strict secret handling.

## Initial constraints

- **v1 scope:** edge APIs; unary first; no streaming API commitment in this intent record.
- **Providers:** multiple named vendors; cloud APIs only for v1 (no local models in this record).
- **Governance:** new external LLM traffic goes through the gateway; direct SDK paths are tracked debt, not the platform story.

## Assumptions (explicit)

- Caller authentication is resolved upstream or integrated as a first-class step before provider selection (details → ledger).
- Provider failure is detectable via HTTP signals suitable for automated rerouting within policy (exact classification → ledger).
- Compute shape (serverless vs containers) remains undecided here; ADR-L records the choice after ledger alternatives.

---

## Summary

- Phase 1 models how real design sessions feel: ambiguity, tradeoffs, risks, unknowns, and explicit deferrals to governed artifacts.
- `[Trace → …]` lines show provenance from dialogue to stable requirement ids in Step 1.
- Anything not closed here must surface as ledger questions or ADRs—not hidden implementation assumptions.

---

**Previous:** [Part 11 overview](../00-overview.md) · **Next:** [Step 1 — Requirements snapshot](./01-requirements-snapshot.md)
