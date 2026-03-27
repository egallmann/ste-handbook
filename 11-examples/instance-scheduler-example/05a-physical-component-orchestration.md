---
title: "Example step 5a — Physical-component ADR orchestration (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5a — Physical-component ADR (orchestration)

## Purpose

Specify **implementable** orchestration: Python Lambdas under **`source/app`**, CDK factories under **`source/instance-scheduler/lib/lambda-functions/`** (for example `main.ts`, `scheduling-orchestrator.ts`, `scheduling-request-handler.ts`, `spoke-registration.ts`). This is **documentation-state** for STE, not a substitute for reading upstream code.

> **Illustrative only.** Pedagogical stub.

## Illustrative excerpt

```yaml
adr_type: physical-component
id: ADR-PC-INST-001
title: Instance Scheduler — orchestration Lambdas

implements_system:
  - ADR-PS-INST-001
  - ADR-PS-INST-002
implements_logical:
  - ADR-L-INST-001
  - ADR-L-INST-002

context: |
  Python functions packaged as Lambdas perform schedule evaluation, EC2/RDS API calls, registration,
  and supporting metrics/log forwarding per CDK wiring.

technology_stack:
  - category: language
    name: Python
    version: "3.x (per solution)"
    rationale: Matches source/app runtime in upstream repository.
  - category: infrastructure
    name: AWS Lambda
    version: managed
    rationale: Serverless orchestration backbone.

component_specifications:
  - id: COMP-5181
    name: Scheduling orchestration Lambda suite
    type: scheduler
    responsibilities: |
      - Evaluate schedules on interval and drive start/stop against EC2/RDS APIs
      - Handle scheduling requests and cross-region/event rules as defined by the solution
      - Register spokes and hub resources; emit operational metrics when enabled
    generation_context:
      purpose: Maintain deterministic schedule outcomes with strong IAM boundaries.
      key_responsibilities:
        - Invoke AWS APIs only through roles defined by hub/spoke stacks
        - Read/write scheduler state via the data layer ADR
      constraints:
        - No hard-coded account IDs; use stack parameters and environment configuration
      success_criteria:
        - Integration tests in upstream repo continue to pass (`npm run test` pattern)
    interfaces:
      - id: IFACE-5181
        type: internal_lambda_invoke
        specification: Internal invokes between main, orchestrator, and handler functions per CDK graph.
    invariants:
      - id: PCINV-5181
        statement: No path bypasses schedule/trust checks before EC2/RDS mutations.
      - id: PCINV-5182
        statement: Structured logs exclude long-lived secrets; include correlation fields for audit.
```

## What to read from it

- **Dual `implements_system`** reflects **shared** orchestration code paths that **participate** in both hub and spoke stacks.
- **PCINV-5181** specializes **INV-5181** / **RQINV-5181** at the **component** layer for EDR linkage.

---

**Previous:** [Step 4b](./04b-physical-system-remote.md) · **Next:** [Step 5b — Physical-component ADR (data layer)](./05b-physical-component-data-layer.md)
