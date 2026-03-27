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

---

**Previous:** [Step 8](./08-edr-example.md) · **Return:** [Part 11 overview](../00-overview.md)
