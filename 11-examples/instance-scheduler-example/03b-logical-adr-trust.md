---
title: "Example step 3b — Logical ADR trust and multi-account (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 3b — Logical ADR (trust and multi-account)

## Purpose

Isolate **cross-account** and **trust** commitments: hub account identity, spoke registration, Organizations vs manual patterns. Resolves **LDEC-5183** and reinforces **RQINV-5182**.

> **Illustrative only.** Pedagogical stub; align deployment parameters with the **[solution deployment guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/deployment.html)** and README.

## Illustrative excerpt

```yaml
adr_type: logical
id: ADR-L-INST-002
title: Instance Scheduler — trust and multi-account (logical)

context: |
  Some estates are single-account; others standardize on AWS Organizations. The scheduler must support
  explicit hub→spoke trust without granting unnecessary APIs in member accounts.

capabilities:
  - id: CAP-5182
    name: Cross-account scheduling
    description: >-
      Register spoke accounts (or organization units) and allow the hub scheduler principal to act
      only within declared regions and schedule semantics.
    enabled_by_decisions: [DEC-5183]

interaction_contracts:
  - id: CONTRACT-5181
    parties: [hub_control_plane, spoke_account]
    protocol: aws_iam_assume_role_and_tagging_apis
    guarantees: |
      Spoke roles trust only the hub scheduler principal (plus documented solution conditions).
      Registration flows publish spoke metadata the hub can reconcile.

invariants:
  - id: INV-5182
    statement: Spoke IAM permissions are least-privilege relative to hub orchestration needs (no admin wildcard).
    scope: cross_account_trust
    enforcement_level: must
    enforcement_mechanism: policy
    verification_method: audit
    rationale: Matches RQINV-5182.
    upheld_by_decisions: [DEC-5183]

decisions:
  - id: DEC-5183
    resolves_ledger: LDEC-5183
    summary: >-
      Deploy a dedicated spoke/remote stack template in member accounts that establishes the scheduler role
      and registration hooks; pair with hub parameters Namespace, InstanceSchedulerAccount, UsingAWSOrganizations
      consistent with the official solution.

constraints:
  - id: CONST-5182
    type: security
    description: >-
      Cross-account enablement must be explicit per spoke; default single-account mode remains supported.
    rationale: Avoids silent trust expansion.
```

## What to read from it

- **CONTRACT-5181** names the **integration shape** the physical-system ADRs will refine (IAM + AWS APIs).
- **DEC-5183** is the logical **anchor** for **ADR-PS-INST-002** (remote topology).

## What this step produced and why it matters

Together with [Step 3a](./03a-logical-adr-scheduling.md), this ADR completes the **logical architecture** for the example: **trust**, **cross-account enablement**, and **contracts** are now **fixed commitments** that physical-system ADRs must **refine**, not reinterpret. After 3a–3b, you should be able to answer “**what did we decide at the logical layer?**” without opening CloudFormation or CDK—yet those decisions are **specific enough** to drive **deployable** shape next.

---

**Previous:** [Step 3a](./03a-logical-adr-scheduling.md) · **Next:** [Step 4a — Physical-system ADR (hub)](./04a-physical-system-hub.md)
