---
title: "Example step 7 — Code semantic linkage (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 7 — Code semantic linkage

## Purpose

Anchor **Architecture IR** identities to **embodiment** in the **[Instance Scheduler on AWS](https://github.com/aws-solutions/instance-scheduler-on-aws)** repository layout. Claims use **path-level** references—no vendored code—so evidence tooling can resolve Lambdas, tables, and CLI packages deterministically.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Upstream layout (reference)

| Path (upstream repo) | Role |
|----------------------|------|
| `source/app/` | Python Lambda implementation |
| `source/instance-scheduler/lib/` | CDK constructs (hub, data layer, Lambdas, IAM) |
| `source/cli/` | Operator CLI sources |
| `source/pipeline/` | Solution pipeline (out of scope for minimal linkage claims) |

Maintainers may keep a **local clone** under the workspace (for example `STE-workspace/reference/instance-scheduler-on-aws`) that is **not** committed inside `ste-handbook`.

## Illustrative excerpt

```yaml
type: implementation_linkage_bundle

claims:
  - claim_id: CLM-5181
    architecture_entity_id: COMP-5181
    embodiment_kind: aws_lambda_functions
    embodiment_ref: >-
      repo:instance-scheduler-on-aws path:source/app + CDK wiring in
      source/instance-scheduler/lib/lambda-functions/*.ts
    authority: semantic_extraction_v3
    confidence: high

  - claim_id: CLM-5182
    architecture_entity_id: COMP-5182
    embodiment_kind: dynamodb_tables
    embodiment_ref: >-
      InstanceSchedulerDataLayer — ConfigTable, StateTable, MaintenanceWindowTable, ResourceRegistry
      (source/instance-scheduler/lib/instance-scheduler-data-layer.ts)
    authority: infrastructure_extraction
    confidence: high

  - claim_id: CLM-5183
    architecture_entity_id: COMP-5183
    embodiment_kind: python_distribution
    embodiment_ref: repo:instance-scheduler-on-aws path:source/cli
    authority: recon_static_analysis
    confidence: medium

  - claim_id: CLM-5184
    architecture_entity_id: IFACE-5182
    embodiment_kind: aws_sdk_dynamodb
    embodiment_ref: boto3 DynamoDB client usage from Lambdas in source/app
    authority: recon_static_analysis
    confidence: medium
```

## What to read from it

- **Linkage** is how an **EDR** attaches CloudWatch findings or IAM simulator results to **COMP-5181** instead of “some Lambda somewhere.”
- **Confidence** stays honest: CLI packaging varies by release artifact—treat as **medium** until your pipeline proves tighter attribution.

## What this step produced and why it matters

**Semantic linkage** anchors **IR entities** (components, interfaces) to **concrete embodiment**: repository paths, Lambda wiring, CLI packages, SDK usage. That bridge is what lets evidence and drift tooling ask “**does reality still match what we declared?**” instead of guessing from org folklore. Without linkage, the IR remains **abstract**; with it, STE can **verify** implementation against architecture **deterministically** (subject to claim **confidence** and pipeline maturity).

---

**Previous:** [Step 6](./06-derived-architecture-ir.md) · **Next:** [Step 8 — EDR example](./08-edr-example.md)
