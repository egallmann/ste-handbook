<!--
  Generated projection — do not hand-edit.
  Source: ../../ir/architecture-ir.json
  Regenerated via STE projection adapter (see ../projection-queries.md).
-->

# System context projection (from Architecture IR)

```mermaid
flowchart LR
  E_COMP_0003["Auth Service"]
  E_COMP_0010["AI Gateway Lambda"]
  E_EXT_AUTH["Organization auth service"]
  E_EXT_OPENAI["OpenAI API"]
  E_COMP_0010 -->|"depends on"| E_COMP_0003
  E_COMP_0010 -->|"invokes provider"| E_EXT_OPENAI
  E_COMP_0010 -->|"depends on"| E_EXT_AUTH
  E_COMP_0003 -->|"realizes external"| E_EXT_AUTH
```
