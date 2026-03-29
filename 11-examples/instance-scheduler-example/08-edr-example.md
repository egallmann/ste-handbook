---
title: "Example step 8 — EDR example (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 8 — Embodied Design Record (EDR)

## Purpose

Show how **runtime and operational evidence** attach to **IR entities** and **requirement/invariant** ids for **governed** assessment. Findings below are **fictional but realistic** for AWS operations (CloudWatch, IAM Access Analyzer patterns, Config rules).

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
type: embodied_design_record
edr_id: EDR-INST-2026-03-27
scope:
  system: Instance Scheduler (hub + sample spoke)
  architecture_snapshot_ref: INST-IR-2026-03-27

findings:
  - id: F-5181
    kind: conformance
    text: Orchestration Lambdas mapped to source/app + CDK graph (CLM-5181)
    linked_entities: [COMP-5181]
    posture: upheld

  - id: F-5182
    kind: conformance
    text: DynamoDB tables encrypted with CMK; deletion protection follows stack condition (CLM-5182)
    linked_entities: [COMP-5182, PCINV-5183]
    posture: upheld

  - id: F-5183
    kind: conformance
    text: Spoke role trust policy allows only hub scheduler principal (sample account)
    linked_entities: [INV-5182, COMP-5181]
    posture: upheld

  - id: F-5184
    kind: violation
    text: >-
      Emergency break-glass IAM policy attached to orchestration role grants ec2:* in spoke test account
    linked_entities: [COMP-5181, INV-5182, REQ-5182]
    posture: violated

  - id: F-5185
    kind: risk
    text: >-
      CloudWatch Logs subscription filter for scheduler logs points to shared aggregator; retention < finance policy
    linked_entities: [COMP-5181, RQNFR-5182]
    posture: at_risk

assessment:
  score: 58
  band: conditional
  summary: >-
    Data plane and trust basics hold; break-glass IAM violates least-privilege invariant until removed

obligations:
  - OBL-5181: Detach ec2:* break-glass policy from scheduler role; re-run IAM simulator evidence
  - OBL-5182: Align log retention / subscription with observability policy or record exception

governance:
  review_required: security_architecture_office
  due_date: "2026-04-10"
```

## What to read from it

- **F-5184** shows how **requirements** (`REQ-5182`) and **invariants** (`INV-5182`) participate in **scoring**, not only component ids.
- **Obligations** close the loop toward **remediation**—picked up narratively in [Step 9](./09-drift-and-correction.md).

## What this step produced and why it matters

The **EDR** packages **runtime and operational evidence**—conformance or violations—**against IR entities** and **requirement/invariant ids**. That answers how **observed behavior** connects back to **Step 0–1 intent**: findings are not free-floating tickets; they **cite** the same **graph** the architecture uses. **Scores** and **obligations** turn evidence into **governed** action: promotion, review, or remediation, still tied to the **declared** model.

---

**Previous:** [Step 7](./07-code-semantic-linkage.md) · **Next:** [Step 9 — Drift and correction](./09-drift-and-correction.md)
