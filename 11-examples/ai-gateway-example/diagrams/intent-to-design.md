# Diagram A — Intent to design flow

**How to read this:** Left to right is the refinement ladder for one system: bounded expectations become explicit design questions, then layered ADR commitments from logical semantics down to implementable components.

```mermaid
flowchart LR
  REQ[Requirements_snapshot]
  LED[Decision_ledger]
  LADR[Logical_ADR]
  PSADR[Physical_system_ADR]
  PCADR[Physical_component_ADR]
  REQ --> LED
  LED --> LADR
  LADR --> PSADR
  PSADR --> PCADR
```

See [Step 1](../01-requirements-snapshot.md) through [Step 5](../05-physical-component-adr.md) in the AI Gateway example.
