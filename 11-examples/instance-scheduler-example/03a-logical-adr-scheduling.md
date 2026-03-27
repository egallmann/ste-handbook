---
title: "Example step 3a — Logical ADR scheduling domain (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 3a — Logical ADR (scheduling domain)

## Purpose

Record **logical** commitments for **what** the solution does for EC2/RDS: schedule binding, periodic evaluation, and **where configuration/state** conceptually lives. This ADR **resolves** ledger rows **LDEC-5181**, **LDEC-5182**, and **LDEC-5184** for the scheduling surface.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative; field names follow **[adr-architecture-kit](../../../adr-architecture-kit)** patterns where shown.

## Illustrative excerpt

```yaml
adr_type: logical
id: ADR-L-INST-001
title: Instance Scheduler — scheduling domain (logical)

context: |
  Operational cost is dominated by idle EC2/RDS. The organization requires
  governed, repeatable start/stop behavior tied to declared schedules—not ad hoc scripts.

capabilities:
  - id: CAP-5181
    name: Scheduled EC2/RDS power management
    description: >-
      Evaluate declared clock-based schedules and start/stop EC2 and RDS accordingly—including
      off nights and weekends and configurable weekday on/off windows.
    enabled_by_decisions: [DEC-5181, DEC-5182]

  - id: CAP-5183
    name: Configuration and run state persistence
    description: >-
      Persist schedules, service state, maintenance windows, and cross-region/account registry
      records in a managed data plane suitable for concurrent orchestration Lambdas.

architectural_boundaries:
  - id: BOUND-5181
    name: Scheduling control plane
    description: >-
      Components that evaluate time policy and call AWS control-plane APIs on behalf of customers.
    rationale: Separates schedule intelligence from optional multi-account trust (ADR-L-INST-002).

invariants:
  - id: INV-5181
    statement: Schedule-driven mutations only — no undocumented automation path may stop/start covered resources.
    scope: scheduling_control_plane
    enforcement_level: must
    enforcement_mechanism: policy
    verification_method: audit
    rationale: Matches RQINV-5181.
    upheld_by_decisions: [DEC-5181]

decisions:
  - id: DEC-5181
    resolves_ledger: LDEC-5181
    summary: Bind schedules primarily via customer-defined resource tags (schedule key) interpreted by the solution.
  - id: DEC-5182
    resolves_ledger: LDEC-5182
    summary: >-
      Use periodic orchestration (interval-based evaluation) as the backbone, complemented by
      region/event hooks as required by the solution design.
  - id: DEC-5184
    resolves_ledger: LDEC-5184
    summary: >-
      Persist configuration, state, maintenance windows, and registration metadata in encrypted DynamoDB tables
      (conceptual model; physical tables named in physical ADRs / CDK).

constraints:
  - id: CONST-5181
    type: technical
    description: Customer schedule vocabulary (periods, time zones) remains stable and documented for operators.
    rationale: Reduces support burden and supports CLI/automation (RQCONST-5182).

non_functional_requirements:
  - id: NFR-5181
    category: performance
    requirement: Orchestration interval is configurable at deploy time within documented bounds.
    acceptance_criteria: Hub evaluates schedules at least as frequently as the chosen interval minutes setting.
```

## What to read from it

- **Capabilities** **CAP-5181** and **CAP-5183** split **user-visible scheduling** from **persistence**—both land in the hub’s logical scope before physical decomposition.
- **INV-5181** is the **logical** counterpart to **RQINV-5181** for IR traceability.

## What this step produced and why it matters

This logical ADR **closes the scheduling domain** for ledger rows **LDEC-5181**, **LDEC-5182**, and **LDEC-5184**: how schedules bind, how **periodic evaluation** is conceived, and where **configuration and state** conceptually live. **Trust and multi-account** packaging is **not** finished here—it is intentionally carried in [Step 3b](./03b-logical-adr-trust.md). Treat this step as **half** of logical closure for the example: scheduling commitments are now **canonical** inputs to physical design.

---

**Previous:** [Step 2](./02-decision-ledger.md) · **Next:** [Step 3b — Logical ADR (trust and multi-account)](./03b-logical-adr-trust.md)
