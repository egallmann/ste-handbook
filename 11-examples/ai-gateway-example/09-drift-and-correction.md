---
title: "Example step 9 — Drift and correction (AI Gateway)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 9 — Drift and correction

## Purpose

Close the loop: **systems drift under design pressure** (scale, shortcuts, new paths). STE makes drift **visible** through linkage and invariants, **assessable** through **EDR** posture, and **correctable** through **obligations** and **revised intent**. This step is the **payoff** for the whole walkthrough.

> **Illustrative only.** Narrative + stub shapes; **ste-spec** is normative.

**Diagram:** [Feedback loop](./diagrams/feedback-loop.md)

## Scenario (story)

The gateway **scaled quickly**. A **new engineer** added a **direct provider call** behind `POST /v1/ai/direct` to unblock a demo. That path **skips** the shared `verify_bearer` step used by the primary route. **Architecture** still describes **one** authenticated edge; **embodiment** now has **two** behaviors. **RQINV-0001** and **PCINV-0001** are **violated** in practice.

## How STE surfaces it (detection chain)

1. **Semantic graph / linkage:** Reconciliation shows the new handler **not** linked through the **auth dependency** claim pattern that **CLM-0003** established for the primary route—or shows a **missing** `depends_on` edge to **CAP-0001** for that path.
2. **Invariant evaluation:** The **invariant** “no provider forward without auth success” fails for the new route.
3. **EDR:** **Score drops** (as in [Step 8](./08-edr-example.md)); **violation** findings reference **IFACE-0012**, **RQINV-0001**, **PCINV-0001**.
4. **Obligations:** Promotion **blocked**; **security/architecture review** scheduled.
5. **Corrective action (governance):** Options include **remove** the path, **gate** it behind the same auth module, or **record** a governed exception with owners and expiry—plus an **ADR** or **logical** amendment if the organization intentionally changes the invariant (rare and explicit).

**Runtime** chapters describe **freshness** and **preflight** gating on projections: stale IR or unreconciled embodiment can **amplify** drift. The structural lesson is the same: **do not reason or ship on silent mismatch**.

## What this teaches

- **Drift** is not only “docs out of date”; it is **divergence between governed intent and embodied behavior**.
- **Self-correction** means **assessment outputs** return to **authorized change**: update **intent**, **structure**, or **embodiment** under policy—not unowned patches.

STE is not “just MBSE” or “just an assistant”: it is a **governed lifecycle** where **evidence** forces **decisions** when reality moves.

---

**Previous:** [Step 8](./08-edr-example.md) · **Return:** [Part 11 overview](../00-overview.md)
