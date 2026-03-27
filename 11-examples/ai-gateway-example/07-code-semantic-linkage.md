---
title: "Example step 7 — Code semantic linkage (AI Gateway)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 7 — Code semantic linkage

## Purpose

Explain why **Architecture IR alone is not enough**. **Embodiment**—repositories, services, infrastructure—must be **linked** to IR identities so observations become **evidence** about **this** system, not generic code facts. Without that linkage, an **EDR** cannot **score** conformance in a grounded way: findings need stable architecture ids to attach to. This step states only that **linkage is required** for that scoring story; **how** your program establishes linkage in code and infra is intentionally **out of scope** here.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

**Diagram:** [Design to embodiment](./diagrams/design-to-embodiment.md)

## Illustrative excerpt

```yaml
# Simplified implementation linkage (illustrative)
type: implementation_linkage_bundle

claims:
  - claim_id: CLM-0001
    architecture_entity_id: COMP-0010
    embodiment_kind: aws_lambda_function
    embodiment_ref: arn:aws:lambda:us-east-1:111122223333:function:ai-gateway
    authority: semantic_extraction_v3
    confidence: high

  - claim_id: CLM-0002
    architecture_entity_id: IFACE-0012
    embodiment_kind: api_gateway_route
    embodiment_ref: prod-ai-gateway/POST/v1/ai/complete
    authority: infrastructure_extraction
    confidence: high

  - claim_id: CLM-0003
    architecture_entity_id: CAP-0001
    embodiment_kind: auth_dependency
    embodiment_ref: >-
      python:ai_gateway.auth.verify_bearer → https://auth.internal/validate
    authority: recon_static_analysis
    confidence: medium
```

## What to read from it

- **Components map** to **deployment artifacts** (Lambda ARN, API route).
- Each row is a **claim** with `authority` and `confidence` so assessment can treat weak or disputed linkage differently from strong linkage. The fragment illustrates **that** claims exist, not **how** your toolchain builds them.
- **Linkage is required for EDR scoring:** [Step 8](./08-edr-example.md) ties findings to entities such as `COMP-0010` and invariants such as `RQINV-0001`. Those edges only work if embodiment is **addressable** relative to the same ids—without it, “pass/fail” collapses into opinion.

The **code semantic graph** is **evidence-bearing linkage** between architecture and embodiment. It does **not** replace **intent** or **ADRs**; it makes **embodiment** inspectable against them. STE is not “just a graph database”: the graph’s value is **governed traceability** and **assessment**, not accumulation of nodes.

---

**Previous:** [Step 6](./06-derived-architecture-ir.md) · **Next:** [Step 8 — EDR example](./08-edr-example.md)
