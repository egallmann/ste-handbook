<!--
  Generated projection — do not hand-edit.
  Source: ../../ir/architecture-ir.json
  Regenerated via STE projection adapter (see ../projection-queries.md).
-->

# System context projection (from Architecture IR)

```mermaid
flowchart LR
  E_COMP_5181["Scheduling orchestration Lambda suite"]
  E_COMP_5182["Scheduler DynamoDB tables"]
  E_COMP_5183["Instance Scheduler CLI"]
  E_EXT_5181["Amazon EC2"]
  E_EXT_5182["Amazon RDS"]
  E_COMP_5181 -->|"depends on"| E_COMP_5182
  E_COMP_5181 -->|"invokes provider"| E_EXT_5181
  E_COMP_5181 -->|"invokes provider"| E_EXT_5182
```
