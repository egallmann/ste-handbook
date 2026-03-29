<!--
  Generated projection — do not hand-edit.
  Source: ../../ir/architecture-ir.json
  Regenerated via STE projection adapter (see ../projection-queries.md).
-->

# Traceability projection (from Architecture IR)

```mermaid
flowchart LR
  E_CAP_5181["Scheduled EC2/RDS power management\n(capability)"]
  E_CAP_5182["Cross-account scheduling\n(capability)"]
  E_CAP_5183["Configuration and run state persistence\n(capability)"]
  E_COMP_5181["Scheduling orchestration Lambda suite\n(component)"]
  E_COMP_5182["Scheduler DynamoDB tables\n(component)"]
  E_COMP_5183["Instance Scheduler CLI\n(component)"]
  E_DEC_5181["Tag-bound schedule selection\n(decision)"]
  E_DEC_5182["Interval-based orchestration backbone\n(decision)"]
  E_DEC_5183["Dedicated spoke stack for trust\n(decision)"]
  E_DEC_5184["DynamoDB persistence layer\n(decision)"]
  E_INV_5181["Schedule-bound automation\n(invariant)"]
  E_INV_5182["Least-privilege spoke trust\n(invariant)"]
  E_REQ_5181["Cost-aware EC2/RDS schedule control\n(requirement)"]
  E_REQ_5182["Explicit multi-account scheduling mode\n(requirement)"]
  E_REQ_5181 -->|"enabled by"| E_DEC_5181
  E_REQ_5182 -->|"enabled by"| E_DEC_5183
  E_INV_5181 -->|"constrains"| E_COMP_5181
  E_INV_5182 -->|"constrains"| E_COMP_5181
  E_COMP_5181 -->|"implements"| E_CAP_5181
  E_COMP_5181 -->|"implements"| E_CAP_5182
  E_COMP_5182 -->|"implements"| E_CAP_5183
  E_COMP_5183 -->|"implements"| E_CAP_5181
  E_DEC_5181 -->|"supports"| E_CAP_5181
  E_DEC_5183 -->|"supports"| E_CAP_5182
```
