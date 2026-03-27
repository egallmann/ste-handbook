---
title: "Example step 5b — Physical-component ADR data layer (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5b — Physical-component ADR (data layer)

## Purpose

Anchor **DynamoDB** tables and **KMS** encryption choices emitted by **`InstanceSchedulerDataLayer`** (`config`, `state`, `maintenance window`, `resource registry` tables). Upstream logical IDs include `ConfigTable`, `StateTable`, `MaintenanceWindowTable`, and `ResourceRegistry`.

> **Illustrative only.** Pedagogical stub.

## Illustrative excerpt

```yaml
adr_type: physical-component
id: ADR-PC-INST-002
title: Instance Scheduler — DynamoDB data layer

implements_system:
  - ADR-PS-INST-001
implements_logical:
  - ADR-L-INST-001

context: |
  Encrypted DynamoDB tables hold schedules/config, operational state, maintenance windows, and cross-account
  registry rows. Retention and deletion protection follow stack conditions in CDK.

technology_stack:
  - category: database
    name: Amazon DynamoDB
    version: on-demand
    rationale: Fit for keyed access patterns and hub-scale concurrency.
  - category: infrastructure
    name: AWS KMS
    version: customer_managed_key
    rationale: Matches TableEncryption.CUSTOMER_MANAGED in data layer construct.

component_specifications:
  - id: COMP-5182
    name: Scheduler DynamoDB tables
    type: database
    responsibilities: |
      - Persist schedule configuration, state snapshots, maintenance windows, and registry metadata
      - Support stream keys where enabled for downstream processors
    generation_context:
      purpose: Provide durable, auditable storage for orchestration Lambdas.
      key_responsibilities:
        - Enforce encryption at rest with CMK
        - Honor retain/delete conditions from hub stack parameters
      constraints:
        - Table schemas remain compatible with existing Lambda code paths in source/app
      success_criteria:
        - CDK snapshots/tests in upstream repo validate table definitions
    interfaces:
      - id: IFACE-5182
        type: aws_sdk_dynamodb
        specification: boto3 / AWS SDK access from Lambdas within VPC-less default (per solution).
    invariants:
      - id: PCINV-5183
        statement: No plaintext schedule secrets in table attributes — use KMS + least-privilege IAM.
```

## What to read from it

- **COMP-5182** is the **embodiment target** for persistence **NFRs** and ledger decision **LDEC-5184**.

---

**Previous:** [Step 5a](./05a-physical-component-orchestration.md) · **Next:** [Step 5c — Physical-component ADR (CLI)](./05c-physical-component-cli.md)
