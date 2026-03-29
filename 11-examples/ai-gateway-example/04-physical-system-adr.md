---
title: "Example step 4 — Physical-system ADR (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 4 — Physical-system ADR

## Purpose

Refine the logical commitments into **deployable structure**: **where** major parts live, what sits **outside** the boundary, and how **trust** is staged. At this layer the system becomes **real**—still not every function body, but **topology** and **externals** you could sketch on a whiteboard next to an AWS account diagram.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
# Simplified physical-system ADR (trimmed)
adr_type: physical-system
id: ADR-PS-AIGW-001
title: AI Gateway — physical system topology

implements_logical:
  - ADR-L-AIGW-001

system_boundaries:
  - id: SYSBOUND-AIGW-001
    name: Internet-facing API edge
    trust_zone: dmz
    notes: TLS termination; only authenticated calls proceed inward

external_systems:
  - id: EXT-OPENAI
    name: OpenAI API
    classification: third_party_provider
  - id: EXT-AUTH
    name: Organization auth service
    classification: internal_shared_service

component_topology:
  components:
    - name: AI Gateway entry
      role: request_router
      implements_adr: ADR-PC-AIGW-001
    - name: Provider health evaluator
      role: failover_signal
      implements_adr: ADR-PC-AIGW-001

deployment_topology:
  platform: aws
  regions: [us-east-1]
  notes: Serverless entry + regional provider endpoints per DEC-0025
```

## What to read from it

- **`implements_logical`** ties this file to **ADR-L-AIGW-001** so physical structure **traces** to logical decisions.
- **External systems** name **OpenAI** and the **auth service**—the gateway is not an island.
- **Trust** language (**DMZ**, authenticated inward flow) reflects the **authentication invariant** from the snapshot.
- **Deployment topology** anchors **serverless** and **region** choices without yet specifying Lambda layers or IAM policies—that is **[Step 5](./05-physical-component-adr.md)**.

Diagrams of this topology are **projections** for human review; if they disagree with published **Architecture IR**, IR wins unless **governance** records an exception.

---

**Previous:** [Step 3](./03-logical-adr.md) · **Next:** [Step 5 — Physical-component ADR](./05-physical-component-adr.md) · **Diagram:** [Intent to design](./diagrams/intent-to-design.md)
