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

- **Conversation seed:** [Step 0 — STE conversation (grounding)](./00-ste-conversation.md) — **Architect + Stakeholder** design simulation; **full STE** may add **CE**, **Steelman**, **persona-routed** Architect probes, and toolchain-generated ADRs (`declared_in` analogue).
- **Product references:** [Instance Scheduler on AWS — README](https://github.com/aws-solutions/instance-scheduler-on-aws/blob/main/README.md) (hub stack, remote/spoke stack, `source/app`, `source/instance-scheduler`, `source/cli`).

Requirement-class rows use **`RQCAP-*` / `RQCONST-*` / `RQINV-*` / `RQNFR-*`** ids (handbook analogue of a flat **REQ-XXXX** list).

## Traceability — requirement rows derived from conversation

| Requirement row | Derived from conversation segment |
|-----------------|-----------------------------------|
| RQCAP-5181 | [§1 — Problem, platform bar, and safety posture](./00-ste-conversation.md#1-problem-platform-bar-and-safety-posture); [§2 — Automation shape](./00-ste-conversation.md#2-automation-shape-clock-vs-idle-vs-manual); [§3 — Scope](./00-ste-conversation.md#3-scope-environments-and-services) |
| RQCAP-5182 | [§5 — Accounts, topology, and multi-account mechanics](./00-ste-conversation.md#5-accounts-topology-and-multi-account-mechanics) |
| RQCONST-5181 | [§1](./00-ste-conversation.md#1-problem-platform-bar-and-safety-posture) (managed platform bar); [§12 — Convergence summary](./00-ste-conversation.md#12-convergence-summary-bounded-intent) |
| RQCONST-5182 | [§8 — Human vocabulary and day-2 operations](./00-ste-conversation.md#8-human-vocabulary-and-day-2-operations) (schedules, periods, time zones); [§12](./00-ste-conversation.md#12-convergence-summary-bounded-intent) |
| RQINV-5181 | [§1](./00-ste-conversation.md#1-problem-platform-bar-and-safety-posture) (positive binding; one governed path) |
| RQINV-5182 | [§1](./00-ste-conversation.md#1-problem-platform-bar-and-safety-posture); [§5](./00-ste-conversation.md#5-accounts-topology-and-multi-account-mechanics) (least-privilege hub/spoke) |
| RQNFR-5181 | [§10 — Orchestration unit](./00-ste-conversation.md#10-orchestration-unit-interval-vs-event-driven); [§12](./00-ste-conversation.md#12-convergence-summary-bounded-intent) |
| RQNFR-5182 | [§4 — Explainability, audit, and observability](./00-ste-conversation.md#4-explainability-audit-and-observability-tradeoffs); [§11 — Drift, misconfiguration](./00-ste-conversation.md#11-drift-misconfiguration-and-evidence-hooks) |

## Illustrative excerpt

```yaml
# Requirements snapshot (Instance Scheduler – handbook illustration)
type: requirements_snapshot
snapshot_id: REQ-INST-2026-03-27

conversation_ref: ./00-ste-conversation.md

required_capabilities:
  - req_item_id: RQCAP-5181
    name: Scheduled EC2/RDS power management
    description: >-
      Start and stop EC2 and RDS instances on declared clock-based schedules—including off nights and weekends
      and configurable weekday on/off windows—to reduce idle cost.
  - req_item_id: RQCAP-5182
    name: Cross-account scheduling
    description: >-
      Optional hub in a central account orchestrates schedules in member (spoke) accounts with explicit trust.

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
      No instance stop/start outside declared schedule bindings and registered trust (no silent ad-hoc automation path).
  - req_item_id: RQINV-5182
    statement: >-
      IAM roles in spoke accounts grant only the actions required for the hub scheduler principal (least privilege).

required_nfrs:
  - req_item_id: RQNFR-5181
    statement: >-
      Orchestration runs on a configurable interval (minutes granularity) suitable for batch schedule evaluation.
  - req_item_id: RQNFR-5182
    statement: >-
      Operational visibility — logs/metrics/alarm hooks sufficient for platform owners to audit schedule actions.

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

The **requirements snapshot** freezes **intent** into **stable ids** (capabilities, constraints, invariants, NFRs) with explicit **provenance** back to [Step 0](./00-ste-conversation.md). Reviewers and tooling can ask “**where did this expectation come from?**” without relying on memory or chat logs. From here forward, **ledger rows** and **ADRs** must **cite** these items—so the design space stays **traceable** rather than a parallel story invented in later documents.

---

**Previous:** [Step 0](./00-ste-conversation.md) · **Next:** [Step 2 — Decision ledger](./02-decision-ledger.md) · **Diagram:** [Intent to design](./diagrams/intent-to-design.md)
