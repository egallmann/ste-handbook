# Diagram — Intent to design (Instance Scheduler example)

**How to read this:** Step 0 is a **single-user** design chat: the **conversation engine** plus **Architect agent** with **signal-activated personas** (e.g. FinOps, Security, **AWS Cloud**, Operations)—in full STE, **ste-rules-library** projections would decide which personas fire and later **project into ADRs**. Later steps **split** logical and physical ADRs where the real solution has **natural seams** (scheduling domain vs trust; hub vs spoke; orchestration vs data vs CLI).

```mermaid
flowchart LR
  CONV["CE plus Architect personas"]
  REQ[Requirements_snapshot]
  LED[Decision_ledger]
  LADR1[Logical_ADR_scheduling]
  LADR2[Logical_ADR_trust]
  PS1[Physical_system_hub]
  PS2[Physical_system_remote]
  PC1[Physical_component_orchestration]
  PC2[Physical_component_data]
  PC3[Physical_component_cli]
  CONV --> REQ
  REQ --> LED
  LED --> LADR1
  LED --> LADR2
  LADR1 --> PS1
  LADR2 --> PS2
  PS1 --> PC1
  PS1 --> PC2
  PS1 --> PC3
  PS2 --> PC1
```

See [Step 0](../00-ste-conversation.md) through [Step 5c](../05c-physical-component-cli.md).
