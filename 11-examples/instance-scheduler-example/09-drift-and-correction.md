---
title: "Example step 9 — Drift and correction (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 9 — Drift and correction

## Purpose

Close the **self-correction** loop: **governed intent** (ADRs + IR) diverged from **embodied IAM** after a break-glass change. STE makes that drift **visible** via linkage + EDR, then drives **authorized remediation** back through intent or implementation.

> **Illustrative only.** Narrative + stub shapes; **ste-spec** is normative.

## Scenario (story)

During an incident, an operator attached a **broad EC2 admin policy** to the **hub orchestration role** to unblock a bad AMI rollout. The change **was never removed**. **Architecture** still claims **least-privilege spoke trust** and **schedule-bound** automation (**INV-5182**, **PCINV-5181**). **IAM** now allows far more than the **remote stack** template intended. **EDR F-5184** ([Step 8](./08-edr-example.md)) records the violation against **COMP-5181** and **REQ-5182**.

## Detection chain

1. **Linkage:** `CLM-5181` still points Lambda code at `source/app`, but **IAM reconciliation** shows **attached policies** diverge from the **CDK-synthesized** role baseline.
2. **Evidence:** CloudTrail `AttachRolePolicy` events + IAM Access Analyzer / policy simulator **fail** the “no `ec2:*` on scheduler role” check derived from **INV-5182**.
3. **EDR:** Score drops; **obligations** block promotion of stack updates until fixed.
4. **Correction:** Remove break-glass policy; if the org **intentionally** needs wider powers, file a **governed exception** *or* amend **ADR-L-INST-002** / physical IAM ADR material—**silent** drift is not an option.

## Alternate drift pattern (tag semantics)

A second common failure mode is **tag key drift**: operators change the **schedule tag key** in spoke stacks without updating the **hub** parameter, so resources silently **stop matching** schedules. STE surfaces this as **broken linkage** between **configuration rows** (`COMP-5182`) and **observed tags** (evidence subject `CAP-5181`). The fix returns through **config reconciliation** and **updated parameters**, recorded under change control.

## What this teaches

- **Drift** spans **code, IAM, and data plane**—not only prose docs.
- **Requirements and invariants** in IR make **FinOps + security** arguments **machine-addressable** in the same artifact family as components.

## What this step produced and why it matters

This step shows **governed correction**: drift is **visible** because **linkage** and **EDR** tie **reality** to **declarations**, and **remediation** must go through **authorized** paths—revert implementation, or **change** ADRs/intent if the org truly needs a new posture. **Silent** divergence is treated as **failure**, not convenience. That is the **closing beat** of the lifecycle: the system continues to **enforce** intent after deploy, not only at design time.

## What This Example Demonstrates

Taken together, the Instance Scheduler walkthrough shows STE as a **continuous, governed loop**, not a one-time documentation exercise. It connects **requirements** (bounded intent), **decisions** (ledger and resolved ADRs), **architecture** (logical and physical commitments), **implementation** (code and infra linkage), **runtime** (observable behavior), **governance** (evidence, scoring, obligations), and **correction** (drift response back into intent or code).

STE is a **closed-loop system**: the same **model** carries from conversation through **IR** to **evidence** and **drift**—so the organization can **see** when reality diverges and **fix** it under **control**, instead of discovering gaps only through incidents or invoices.

## Example completeness (definition of done)

This walkthrough is **complete** for a reader when they can answer **yes** to each item (see also [Part 11 overview](../00-overview.md)):

1. See the **original problem** ([Phase 1 — Step 0](./00-ste-conversation.md)).
2. See the **conversation** that explored it (same).
3. See **requirements** with **trace** to dialogue ([Step 1](./01-requirements-snapshot.md)).
4. See **logical architecture** ([Step 3a](./03a-logical-adr-scheduling.md), [Step 3b](./03b-logical-adr-trust.md)).
5. See **physical system** design ([Steps 4a–4b](./04a-physical-system-hub.md)).
6. See **physical component** design ([Steps 5a–5c](./05a-physical-component-orchestration.md)).
7. See **which rules activated** ([Step 5d](./05d-rules-activation.md)).
8. See the **compiled architecture model** ([Step 6](./06-derived-architecture-ir.md)).
9. See **what system actually runs** ([Phase 8 in Step 7](./07-code-semantic-linkage.md#phase-8--runtime-system)).
10. **Trace every artifact** back to its origin (lineage table in [Part 11 overview](../00-overview.md); trace tables in Steps **1**, **3a**, and **3b**).

---

**Previous:** [Step 8](./08-edr-example.md) · **Return:** [Part 11 overview](../00-overview.md)
