<!--
  Generated projection — do not hand-edit.
  Source: ../../ir/architecture-ir.json
  Regenerated via STE projection adapter (see ../projection-queries.md).
-->

# Capability / component projection (from Architecture IR)

```mermaid
flowchart TB
  E_CAP_5181["Scheduled EC2/RDS power management"]
  E_CAP_5182["Cross-account scheduling"]
  E_CAP_5183["Configuration and run state persistence"]
  E_COMP_5181["Scheduling orchestration Lambda suite"]
  E_COMP_5182["Scheduler DynamoDB tables"]
  E_COMP_5183["Instance Scheduler CLI"]
  E_IFACE_5181["Internal Lambda orchestration invokes"]
  E_IFACE_5182["DynamoDB access from Lambdas"]
  E_IFACE_5183["Operator CLI commands"]
  E_COMP_5181 -->|"implements"| E_CAP_5181
  E_COMP_5181 -->|"implements"| E_CAP_5182
  E_COMP_5182 -->|"implements"| E_CAP_5183
  E_COMP_5183 -->|"implements"| E_CAP_5181
  E_CAP_5181 -->|"depends on"| E_CAP_5183
  E_COMP_5181 -->|"depends on"| E_COMP_5182
  E_COMP_5181 -->|"exposes"| E_IFACE_5181
  E_COMP_5182 -->|"exposes"| E_IFACE_5182
  E_COMP_5183 -->|"exposes"| E_IFACE_5183
```
