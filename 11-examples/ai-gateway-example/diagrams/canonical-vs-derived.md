# Diagram B — Canonical artifacts to derived model

**How to read this:** Humans govern canonical intent and ADR records; compilation produces **Architecture IR** (the machine-reasonable architecture model). Registries, indices, and graph exports are **derived projections**—rebuildable views, not alternate sources of truth.

```mermaid
flowchart TB
  subgraph canon [Canonical_authority]
    SNAP[Requirements_snapshot]
    LED[Decision_ledger]
    ADRS[ADR_ladder_logical_PS_PC]
  end
  subgraph pipeline [Compile_normalize]
    C[Compilation]
  end
  subgraph ir [Architecture_IR]
    IR[Canonical_architecture_model]
  end
  subgraph deriv [Derived_projections]
    REG[Entity_registry]
    REL[Relationship_registry]
    IDX[Graph_index]
  end
  SNAP --> C
  LED --> C
  ADRS --> C
  C --> IR
  IR --> REG
  IR --> REL
  IR --> IDX
```

See [Step 6](../06-derived-architecture-ir.md).
