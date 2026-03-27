---
title: "Example step 8 — Embodied Design Record (AI Gateway)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 8 — Embodied Design Record (EDR)

## Purpose

Introduce the **Embodied Design Record (EDR)** as the **evidence artifact** that states what the running system **actually embodies** relative to declared **intent** and **Architecture IR**. An EDR is **not** a casual review comment; it is structured, **scorable**, and able to drive **obligations** and **governance**.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

**Diagram:** [Feedback loop](./diagrams/feedback-loop.md)

## Illustrative excerpt

```yaml
# Simplified EDR-shaped record (trimmed)
type: embodied_design_record
edr_id: EDR-AIGW-2026-03-27
scope:
  system: AI Gateway
  architecture_snapshot_ref: ir-snapshot-2026-03-27T0900Z

findings:
  - id: F-001
    kind: conformance
    text: Lambda COMP-0010 implements gateway entry (CLM-0001)
    linked_entities: [COMP-0010]
    posture: upheld

  - id: F-002
    kind: conformance
    text: Auth dependency present on primary route (CLM-0003)
    linked_entities: [CAP-0001, IFACE-0012]
    posture: upheld

  - id: F-003
    kind: conformance
    text: Provider secrets loaded via Secrets Manager per DEC-0027
    linked_entities: [COMP-0010, DEC-0027]
    posture: upheld

  - id: F-004
    kind: conformance
    text: Failover uses health checks plus bounded retries per DEC-0026
    linked_entities: [COMP-0010, DEC-0026]
    posture: upheld

  - id: F-005
    kind: conformance
    text: Structured logs include request_id; no secret fields in log schema sample
    linked_entities: [COMP-0010, PCINV-0002]
    posture: upheld

  - id: F-006
    kind: violation
    text: >-
      Secondary entry path /v1/ai/direct bypasses auth gate (new handler)
    linked_entities: [IFACE-0012, RQINV-0001, PCINV-0001]
    posture: violated

  - id: F-007
    kind: risk
    text: Debug logging path may print provider headers containing API key material
    linked_entities: [RQINV-0002, PCINV-0002]
    posture: at_risk

assessment:
  score: 62
  band: conditional
  summary: >-
    Primary route conforms; ungated path and debug logging create governed exceptions

obligations:
  - OBL-901: Block promotion until /v1/ai/direct is removed or gated
  - OBL-902: Open security review on debug logger configuration

governance:
  review_required: architecture_board
  due_date: "2026-04-03"
```

## What to read from it

- **Findings** mix **upheld**, **violated**, and **at-risk** observations; each ties to **IR entities** and **requirement/invariant** ids where relevant.
- **Score / band** express an **assessment posture** suitable for policy gates—not vanity metrics, but **governance signals**.
- **Obligations** and **review_required** show the system becoming **governed**: modeled structure is no longer enough; **authorized response** is required.

This is how STE stays **more than documentation**: **evidence** meets **rules**, and outcomes feed **authorized change**.

---

**Previous:** [Step 7](./07-code-semantic-linkage.md) · **Next:** [Step 9 — Drift and correction](./09-drift-and-correction.md)
