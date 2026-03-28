# Diagram — STE pipeline (AI Gateway example)

**How to read this:** Top to bottom is the **canonical eight-phase** spine used across Part 11, then the **extension** (embodiment, EDR, drift). The AI Gateway walkthrough is **small** (one logical ADR, one physical-system / physical-component pair) but follows the **same** phases as the Instance Scheduler example.

**Customization for this system:** edge **REST** AI gateway, **serverless** compute, **multi-provider** routing and failover.

```mermaid
flowchart TB
  p1["Phase1_Conversation"]
  p2["Phase2_Requirements_plus_ledger"]
  p3["Phase3_ADR_L"]
  p4["Phase4_ADR_PS"]
  p5["Phase5_ADR_PC"]
  p6["Phase6_Rules_activation"]
  p7["Phase7_Architecture_IR"]
  p8["Phase8_Runtime_system"]
  e1["Extension_Embodiment_linkage"]
  e2["Extension_EDR"]
  e3["Extension_Drift_correction"]
  p1 --> p2 --> p3 --> p4 --> p5 --> p6 --> p7 --> p8
  p8 --> e1 --> e2 --> e3
```

**Refinement ladder (steps 1–5 detail):** bounded expectations and ledger through layered ADRs.

```mermaid
flowchart LR
  REQ[Requirements_snapshot]
  LED[Decision_ledger]
  LADR[Logical_ADR]
  PSADR[Physical_system_ADR]
  PCADR[Physical_component_ADR]
  RULES[Rules_activation_5b]
  REQ --> LED
  LED --> LADR
  LADR --> PSADR
  PSADR --> PCADR
  PCADR --> RULES
```

## Files (reading order)

- [Phase 1 — Conversation](../00-ste-conversation.md)
- [Step 1](../01-requirements-snapshot.md) through [Step 5](../05-physical-component-adr.md)
- [Step 5b — Rules activation](../05b-rules-activation.md)
- [Step 6 — Derived Architecture IR](../06-derived-architecture-ir.md)
- [Step 7 — Runtime + linkage](../07-code-semantic-linkage.md)
- [Step 8 — EDR](../08-edr-example.md) · [Step 9 — Drift](../09-drift-and-correction.md)

See [Part 11 overview](../../00-overview.md) for the full **phase map** and **artifact lineage** table.
