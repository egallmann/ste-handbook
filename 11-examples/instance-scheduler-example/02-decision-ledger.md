---
title: "Example step 2 — Decision ledger (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 2 — Decision ledger

## Purpose

Bound the **logical** decision space before ADRs claim closure. Each question links to **snapshot items** so reviewers see **why** a topic is in scope. The **logical ADRs** in steps 3a–3b **resolve** these rows—they do not invent a parallel decision list.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
type: decision_ledger
ledger_id: LEDGER-INST-2026-03-27
source_requirements_snapshot: REQ-INST-2026-03-27

target_logical_adrs:
  - ADR-L-INST-001
  - ADR-L-INST-002

required_decisions:
  - ledger_decision_id: LDEC-5181
    question: How are schedules attached to resources?
    alternatives: [resource_tags, external_registry_only, hybrid]
    related_snapshot_items: [RQCAP-5181, RQCONST-5182]
    resolves_in_adr: ADR-L-INST-001

  - ledger_decision_id: LDEC-5182
    question: What is the unit of orchestration for periodic evaluation?
    alternatives: [fixed_interval_lambda, streaming_events_only, mixed]
    related_snapshot_items: [RQCAP-5181, RQNFR-5181]
    resolves_in_adr: ADR-L-INST-001

  - ledger_decision_id: LDEC-5183
    question: How is multi-account trust established?
    alternatives: [dedicated_spoke_stack, central_assume_role_only, org_service_linked]
    related_snapshot_items: [RQCAP-5182, RQINV-5182]
    resolves_in_adr: ADR-L-INST-002

  - ledger_decision_id: LDEC-5184
    question: Where do configuration, state, and registry records live?
    alternatives: [dynamodb_tables, rds, s3_manifests]
    related_snapshot_items: [RQCONST-5181, RQNFR-5182]
    resolves_in_adr: ADR-L-INST-001

constraints:
  snapshot_items:
    - RQINV-5181
    - RQINV-5182
    - RQCONST-5181
```

## What to read from it

- **LDEC-5183** is the bridge to the **remote / spoke** stack parameters described in the solution README (`InstanceSchedulerAccount`, `Namespace`, `UsingAWSOrganizations`).
- **LDEC-5184** anticipates the **DynamoDB** data layer in the CDK (`ConfigTable`, `StateTable`, `MaintenanceWindowTable`, `ResourceRegistry` in `instance-scheduler-data-layer.ts` in the upstream repository).

---

**Previous:** [Step 1](./01-requirements-snapshot.md) · **Next:** [Step 3a — Logical ADR (scheduling domain)](./03a-logical-adr-scheduling.md) · **Diagram:** [Intent to design](./diagrams/intent-to-design.md)
