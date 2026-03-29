---
title: "Example step 1 — Requirements snapshot (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-28"
---

# Step 1 — Requirements snapshot

## Purpose

Freeze **bounded expectations** for a **realistic** AWS operational solution: reduce cost by **starting and stopping** EC2 and RDS instances on **schedules**, with optional **multi-account** deployment. Factual product behavior is described by AWS in the **[implementation guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html)** and **[repository](https://github.com/aws-solutions/instance-scheduler-on-aws)**; this snapshot is **STE-shaped pedagogy** aligned to **[adr-architecture-kit](../../../adr-architecture-kit)** patterns.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Provenance

- **Canonical STE flow (Parts 1–8):** [00-canonical-ste-flow.md](./00-canonical-ste-flow.md) — **Human + AI (Architecture Partner)** design session; **conversation → extracted artifacts → ADR → ADR steelman → gaps/deferrals → architecture view → traceability**.
- **Phase 1 entry:** [Step 0](./00-ste-conversation.md) links the walkthrough into that canonical flow. **Full STE** may add a **conversation engine**, **Steelman** as a separate voiced role, **persona-routed** probes, and toolchain-generated ADRs (`declared_in` analogue).
- **Product references:** [Instance Scheduler on AWS — README](https://github.com/aws-solutions/instance-scheduler-on-aws/blob/main/README.md) (hub stack, remote/spoke stack, `source/app`, `source/instance-scheduler`, `source/cli`).

Requirement-class rows use **`RQCAP-*` / `RQCONST-*` / `RQINV-*` / `RQNFR-*`** ids (handbook analogue of a flat **REQ-XXXX** list).

## Traceability — requirement rows derived from conversation

| Requirement row | Derived from canonical flow |
|-----------------|----------------------------|
| RQCAP-5181 | [Part 1 — Problem statement](./00-canonical-ste-flow.md#part-1--problem-statement); [Part 2 — Design conversation](./00-canonical-ste-flow.md#part-2--design-conversation); [Part 3 — Extracted artifacts](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation) |
| RQCAP-5182 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation); [Part 3](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation); [Part 4 — ADR](./00-canonical-ste-flow.md#part-4--architectural-decision-record) |
| RQCONST-5181 | [Part 4 — ADR](./00-canonical-ste-flow.md#part-4--architectural-decision-record) (managed hub control plane); [Part 6](./00-canonical-ste-flow.md#part-6--gap-resolution-and-deferrals) (resolved posture) |
| RQCONST-5182 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation) (stable operator vocabulary); [Part 3](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation) |
| RQINV-5181 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation) (invariant listing, classification, lock-in); [Part 3](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation) |
| RQINV-5182 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation) (hub/spoke trust); [Part 4](./00-canonical-ste-flow.md#part-4--architectural-decision-record) (centralized control plane) |
| RQNFR-5181 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation) (evaluation cadence); [Part 3](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation) |
| RQNFR-5182 | [Part 2](./00-canonical-ste-flow.md#part-2--design-conversation); [Part 3](./00-canonical-ste-flow.md#part-3--extracted-artifacts-from-the-conversation); [Part 5](./00-canonical-ste-flow.md#part-5--adr-steelman-review) (observability gaps) |

## Illustrative excerpt

```yaml
# Requirements snapshot (Instance Scheduler – handbook illustration)
type: requirements_snapshot
snapshot_id: REQ-INST-2026-03-27

conversation_ref: ./00-canonical-ste-flow.md

required_capabilities:
  - req_item_id: RQCAP-5181
    name: Scheduled EC2/RDS power management
    description: >-
      Start and stop EC2 and RDS in non-production accounts on declared clock-based schedules—including off nights
      and weekends and configurable weekday windows—to reduce idle cost. Only resources explicitly opted in may be
      affected. Always-on carve-outs and backup/maintenance windows must be respected. When safety-relevant inputs
      are ambiguous or unavailable, the automation must fail closed (no stop/start) rather than guess.
  - req_item_id: RQCAP-5182
    name: Cross-account scheduling
    description: >-
      A centralized hub in a tools account orchestrates schedules across member (spoke) non-production accounts using
      explicit cross-account trust. Account eligibility is aligned to the organization’s environment registry so
      production-class accounts are never in scope for this automation.

required_constraints:
  - req_item_id: RQCONST-5181
    statement: >-
      Control plane implemented with AWS-managed primitives (e.g., Lambda, DynamoDB, EventBridge) per solution design.
  - req_item_id: RQCONST-5182
    statement: >-
      Customer-facing configuration uses stable concepts (schedules, periods, time zones) documented in the implementation guide.

required_invariants:
  - req_item_id: RQINV-5181
    statement: >-
      No instance stop/start outside declared schedule bindings, registered trust, and explicit opt-in enrollment;
      no silent ad-hoc automation path. Production workloads must never be stopped by this system. Only accounts
      classified as non-production per the environment registry may be targeted. Always-on resources must not be
      stopped. Backup and maintenance windows must be honored for stop decisions. Execution must be idempotent and
      safe under duplicate runs. Each execution must cap how many resources it may mutate (blast-radius control).
      When classification, registry data, or safety checks are ambiguous or unavailable, default to no mutation.
  - req_item_id: RQINV-5182
    statement: >-
      IAM roles in spoke accounts grant only the actions required for the hub scheduler principal (least privilege);
      no org-wide generic power role. Trust and registration must be explicit per spoke and reviewable.

required_nfrs:
  - req_item_id: RQNFR-5181
    statement: >-
      Orchestration runs on a configurable interval (minutes granularity) suitable for batch schedule evaluation.
  - req_item_id: RQNFR-5182
    statement: >-
      Operational visibility — durable logs, metrics, and alarm hooks sufficient for platform owners to audit
      automation actions and material schedule or policy changes, including correlation adequate to answer “why did
      this resource change state?” across hub and spokes.

technology_signals:
  language: python
  infrastructure: aws
  iac: aws_cdk
  architecture_pattern: hub_spoke_lambda

feeds_logical_adrs:
  - ADR-L-INST-001
  - ADR-L-INST-002
```

## What to read from it

- **Capabilities** mirror the **problem statement** in the official solution (EC2/RDS; cross-account is a **first-class** optional mode).
- **Invariants** carry **security and governance** posture from the conversation into **traceable** ids for the ledger and IR.
- **`feeds_logical_adrs`** splits **domain scheduling** (`ADR-L-INST-001`) from **trust/account** concerns (`ADR-L-INST-002`)—a deliberate **higher-fidelity** split than a single logical ADR.

## What this step produced and why it matters

The **requirements snapshot** freezes **intent** into **stable ids** (capabilities, constraints, invariants, NFRs) with explicit **provenance** back to [Parts 1–8](./00-canonical-ste-flow.md) (via [Step 0](./00-ste-conversation.md)). Reviewers and tooling can ask “**where did this expectation come from?**” without relying on memory or chat logs. From here forward, **ledger rows** and **ADRs** must **cite** these items—so the design space stays **traceable** rather than a parallel story invented in later documents.

---

**Previous:** [Step 0](./00-ste-conversation.md) · [Canonical STE flow](./00-canonical-ste-flow.md) · **Next:** [Step 2 — Decision ledger](./02-decision-ledger.md) · **Diagram:** [Intent to design](./diagrams/intent-to-design.md)
