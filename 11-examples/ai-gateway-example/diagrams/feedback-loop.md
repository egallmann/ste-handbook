# Diagram D — Self-correcting loop

**How to read this:** Assessment compares embodied reality to governed intent; obligations and revised decisions close the loop so **drift** becomes visible and correctable rather than silent.

```mermaid
flowchart LR
  I[Intent_and_ADRs]
  A[Architecture_IR]
  E[Embodiment]
  R[EDR_and_assessment]
  O[Obligations_and_corrective_action]
  I --> A
  A --> E
  E --> R
  R --> O
  O -->|"updated_intent"| I
  O -->|"revised_structure"| A
```

See [Step 8](../08-edr-example.md) and [Step 9](../09-drift-and-correction.md).
