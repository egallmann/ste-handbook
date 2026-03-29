# Diagram C — Design to embodiment

**How to read this:** The derived architecture model is linked to code and infrastructure through semantic extraction and reconciliation; the result is **embodied** structure you can observe and assess, not intent floating alone.

```mermaid
flowchart LR
  IR[Architecture_IR]
  EXT[Semantic_extraction]
  SG[Code_infra_semantic_graph]
  CL[Linkage_to_IR_entities]
  EDR[EDR_shaped_evidence]
  IR --> EXT
  EXT --> SG
  SG --> CL
  CL --> IR
  SG --> EDR
```

See [Step 7](../07-code-semantic-linkage.md) and [Step 8](../08-edr-example.md).
