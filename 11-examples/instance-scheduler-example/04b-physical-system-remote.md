---
title: "Example step 4b — Physical-system ADR remote/spoke (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 4b — Physical-system ADR (remote / spoke)

## Purpose

Capture **spoke** footprint: IAM roles, registration Lambdas, and **trust** back to the **hub** account. Aligns with the **`instance-scheduler-on-aws-remote`** / spoke stack in the solution README and CDK `remote-stack.ts` / `SpokeStack`.

> **Illustrative only.** Pedagogical stub.

## Illustrative excerpt

```yaml
adr_type: physical-system
id: ADR-PS-INST-002
title: Instance Scheduler — remote/spoke physical topology

implements_logical:
  - ADR-L-INST-002

context: |
  Member accounts deploy the remote template. Parameters Namespace, InstanceSchedulerAccount,
  ScheduleTagKey, UsingAWSOrganizations, and Regions must match hub expectations.

technology_stack:
  - category: infrastructure
    name: AWS CloudFormation_via_CDK
    version: solution-defined
    rationale: Remote stack ships as solution template/CDK stack.

system_boundaries:
  - id: SYSBOUND-5182
    name: Spoke scheduling boundary
    description: >-
      Hosts least-privilege IAM roles and registration Lambdas that allow the hub principal to schedule
      resources in selected regions.
    external_dependencies:
      - Hub scheduler principal (InstanceSchedulerAccount)
      - EC2/RDS resources tagged for schedules
    exposed_interfaces:
      - Spoke registration events to hub buses (per solution wiring)

component_topology:
  components:
    - name: Spoke registration and scheduler role
      type: worker
      purpose: Establish trust, register spoke with hub, enforce regional coverage.
      implements_adr: ADR-PC-INST-001
  relationships:
    - from: Spoke registration and scheduler role
      to: Hub control plane (ADR-PS-INST-001)
      type: depends_on
      protocol: aws_iam_and_eventbridge
      description: Trust and event flows connect spoke to hub namespace.

deployment_topology:
  platform: aws
  regions: customer_selected_list_or_current
  notes: Regions parameter may be empty for current-region-only operation (see remote stack parameters).
```

## What to read from it

- **implements_logical** ties **physical topology** directly to **ADR-L-INST-002**.
- **Orchestration** implementation is still detailed in **ADR-PC-INST-001** (shared logical component name across hub and spoke responsibilities).

---

**Previous:** [Step 4a](./04a-physical-system-hub.md) · **Next:** [Step 5a — Physical-component ADR (orchestration)](./05a-physical-component-orchestration.md)
