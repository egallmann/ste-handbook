---
title: "Example step 5c — Physical-component ADR CLI (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5c — Physical-component ADR (CLI)

## Purpose

Document the **operator-facing** CLI delivered under **`source/cli`** in the upstream repository: how it **mutates** or **queries** scheduler configuration through AWS APIs, and how it **depends** on the same **configuration model** as the Lambdas.

> **Illustrative only.** Pedagogical stub.

## Illustrative excerpt

```yaml
adr_type: physical-component
id: ADR-PC-INST-003
title: Instance Scheduler — operator CLI

implements_system:
  - ADR-PS-INST-001
implements_logical:
  - ADR-L-INST-001

context: |
  The scheduler-cli package is optional for CloudFormation-only operators but is the ergonomic path
  for teams managing schedules at scale from workstations and automation accounts.

technology_stack:
  - category: language
    name: Python
    version: "3.x (per solution)"
    rationale: CLI ships alongside app sources in upstream monorepo layout.
  - category: tooling
    name: scheduler-cli
    version: solution-versioned
    rationale: README notes CLI packaging for distribution with solution builds.

component_specifications:
  - id: COMP-5183
    name: Instance Scheduler CLI
    type: library
    responsibilities: |
      - Provide commands to create/update/delete schedules and related configuration artifacts
      - Authenticate via standard AWS credential chain; respect least-privilege IAM roles
    generation_context:
      purpose: Give operators a governed alternative to hand-editing templates for routine changes.
      key_responsibilities:
        - Validate inputs against the same conceptual model Lambdas consume
        - Fail closed when hub endpoints/tables are unreachable
      constraints:
        - Must not embed hub account secrets; rely on ambient credentials
      success_criteria:
        - Documented in AWS implementation guide CLI sections
    interfaces:
      - id: IFACE-5183
        type: aws_cli_style_commands
        specification: CLI entrypoints published by solution documentation.
    invariants:
      - id: PCINV-5184
        statement: CLI mutations are auditable via CloudTrail like other AWS API usage.

deployment_topology:
  hosting: customer_workstation_or_ci
  notes: Not deployed as Lambda; distributed as artifact per solution packaging guidance.
```

## What to read from it

- **COMP-5183** completes the **three-way** split: **compute** (5181), **data** (5182), **operator tooling** (5183).

---

**Previous:** [Step 5b](./05b-physical-component-data-layer.md) · **Next:** [Step 6 — Derived Architecture IR](./06-derived-architecture-ir.md)
