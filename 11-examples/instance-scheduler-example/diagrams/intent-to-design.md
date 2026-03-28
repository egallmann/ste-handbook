# Diagram — STE pipeline (Instance Scheduler example)

**How to read this:** Top to bottom is the **canonical eight-phase** spine, then the **extension** (embodiment linkage, EDR, drift). This walkthrough uses **split** logical and physical ADRs where the real solution has **natural seams** (scheduling vs trust; hub vs spoke; orchestration vs data vs CLI).

**Customization for this system:** **Hub/spoke** AWS deployment, **Lambda** orchestration, **DynamoDB** state, **EventBridge** scheduling, **cross-account IAM**.

```mermaid
flowchart TB
  p1["Phase1_Conversation_Step0"]
  p2["Phase2_Requirements_plus_ledger"]
  p3["Phase3_ADR_L_split"]
  p4["Phase4_ADR_PS_hub_spoke"]
  p5["Phase5_ADR_PC_3up"]
  p6["Phase6_Rules_activation_5d"]
  p7["Phase7_Architecture_IR"]
  p8["Phase8_Runtime_system"]
  e1["Extension_Embodiment_linkage"]
  e2["Extension_EDR"]
  e3["Extension_Drift_correction"]
  p1 --> p2 --> p3 --> p4 --> p5 --> p6 --> p7 --> p8
  p8 --> e1 --> e2 --> e3
```

**Refinement ladder (split ADRs):**

```mermaid
flowchart LR
  CONV[Conversation]
  REQ[Requirements_snapshot]
  LED[Decision_ledger]
  L1[Logical_ADR_scheduling]
  L2[Logical_ADR_trust]
  PS1[Physical_system_hub]
  PS2[Physical_system_remote]
  PC1[PC_orchestration]
  PC2[PC_data]
  PC3[PC_CLI]
  RULES[Rules_activation_5d]
  CONV --> REQ
  REQ --> LED
  LED --> L1
  LED --> L2
  L1 --> PS1
  L2 --> PS2
  PS1 --> PC1
  PS1 --> PC2
  PS1 --> PC3
  PS2 --> PC1
  PC1 --> RULES
  PC2 --> RULES
  PC3 --> RULES
```

## Files (reading order)

- [Step 0 — Phase 1 conversation](../00-ste-conversation.md)
- [Step 1](../01-requirements-snapshot.md) through [Step 5c](../05c-physical-component-cli.md)
- [Step 5d — Rules activation](../05d-rules-activation.md)
- [Step 6 — Derived Architecture IR](../06-derived-architecture-ir.md)
- [Step 7 — Runtime + linkage](../07-code-semantic-linkage.md)
- [Step 8 — EDR](../08-edr-example.md) · [Step 9 — Drift](../09-drift-and-correction.md)

See [Part 11 overview](../../00-overview.md) for the full **phase map** and **artifact lineage** table.
