---
title: "Example step 5 — Physical-component ADR (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5 — Physical-component ADR

## Purpose

Tie topology to **implementable** units: named **components**, **responsibilities**, **interfaces**, **component-level invariants**, and a **deployment unit** (for example a Lambda). This is the layer where tooling and engineers (including AI-assisted workflows) can **ground** work: concrete enough to build, still **governed** by upstream ADRs.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
# Simplified physical-component ADR (trimmed)
adr_type: physical-component
id: ADR-PC-AIGW-001
title: AI Gateway Lambda — responsibilities and interfaces

implements_system:
  - ADR-PS-AIGW-001
implements_logical:
  - ADR-L-AIGW-001

component_specifications:
  - id: COMP-0010
    name: AI Gateway Lambda
    deployment_unit: aws_lambda
    responsibilities: |
      - Authenticate caller via auth service before routing
      - Resolve provider route; apply health-check policy (DEC-0026)
      - Load provider secrets from Secrets Manager at cold start (DEC-0027)
    interfaces:
      - id: IFACE-0012
        type: rest_api
        specification: POST /v1/ai/complete — requires Bearer token
    invariants:
      - id: PCINV-0001
        statement: No code path forwards to a provider without prior auth success
      - id: PCINV-0002
        statement: Structured logs include request_id; never log secret material
```

## What to read from it

- **Dual `implements_*` links** keep the ladder explicit: physical component realizes **system** topology and **logical** semantics.
- **Interfaces** are concrete enough to **test** and **observe** (REST path, token expectation).
- **Invariants** specialize **RQINV-0001** and **RQINV-0002** for this deployable unit—still **canonical** statements, not informal code comments.
- **Deployment unit** (`aws_lambda`) connects policy (**serverless**) to something CI/CD and runtime can target.

The **code semantic graph** in later steps will attach **evidence** to **COMP-0010** and **IFACE-0012**; until then, this ADR remains **intent** for embodiment, not proof of behavior.

---

**Previous:** [Step 4](./04-physical-system-adr.md) · **Next:** [Step 6 — Derived Architecture IR](./06-derived-architecture-ir.md)
