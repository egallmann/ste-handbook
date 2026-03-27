# Illustrative projection queries (Arch DSL sketch)

These snippets express **what** a projection selects from **Architecture IR**. They are **handbook pedagogy**—a readable stand-in for a machine-facing **projection specification** (graph query, internal DSL, or adapter config), not normative syntax.

## Conversation first, DSL as an internal seam

STE’s **conversation engine** includes an **architecture projection subsystem** whose job is to **transpile** natural discussion into whatever **architecture DSL** (or structured projection spec) the toolchain needs. The design stance here is deliberate: **human operators should not be forced to learn a new language or syntax** just to ask for a view, a slice, or a diagram. The **human–computer interface** is biased toward what people already do well—**having a conversation**—while the system **materializes** durable, reviewable structure on the other side of the boundary ([Conversation engine overview](../../../09-human-interface/09-00-conversation-engine-overview.md), [Conversation interface](../../../09-human-interface/09-01-conversation-interface.md)).

The blocks below are **not** “what authors type.” They are **explainability**: they show the **selection semantics** a projection adapter must honor so engineers, auditors, and tools agree on **what** was projected from **which** IR snapshot.

The IR snapshot is [`../ir/architecture-ir.json`](../ir/architecture-ir.json). A **projection adapter** in your STE toolchain implements equivalent selections; treat these blocks as **documentation of intent** for that adapter (the handbook does not ship generator source).

---

## Query A — Capability / component structure

**Intent:** Review routing and failover capabilities, how the gateway component implements them, and platform auth dependencies.

```text
ARCH.PROJECT mermaid_flowchart "capability_component" {
  SOURCE ir_snapshot "../ir/architecture-ir.json"
  ENTITIES WHERE entity_type IN ("component", "capability", "interface")
  RELATIONSHIPS WHERE relationship_type IN ("implements", "depends_on", "exposes")
  INCLUDE_ENTITY_IDS [ "COMP-0010", "COMP-0003", "CAP-0015", "CAP-0016", "CAP-0001", "IFACE-0012" ]
}
```

**Equivalent idea (Cypher-flavored pseudocode):**

```text
MATCH (n)
WHERE n.id IN ['COMP-0010','COMP-0003','CAP-0015','CAP-0016','CAP-0001','IFACE-0012']
MATCH (a)-[r:implements|depends_on|exposes]->(b)
WHERE a.id IN [...] AND b.id IN [...]
RETURN a, r, b
```

**Output:** [`generated/ir-capability-component.md`](generated/ir-capability-component.md)

---

## Query B — System context (externals)

**Intent:** Show the gateway against **third-party** and **organizational** dependencies for threat and routing discussions.

```text
ARCH.PROJECT mermaid_flowchart "system_context" {
  SOURCE ir_snapshot "../ir/architecture-ir.json"
  ENTITIES WHERE entity_type IN ("component", "external_system")
  RELATIONSHIPS WHERE relationship_type IN ("depends_on", "invokes_provider", "realizes_external")
}
```

**Output:** [`generated/ir-system-context.md`](generated/ir-system-context.md)

---

## Why this matters

- **Projection = function(IR snapshot, query/spec, layout)**. The IR stays **canonical**; Mermaid is a **derived view**.
- A mature STE toolchain compiles a **projection spec**—often **reached via conversation**, then stored for repeatability—to Mermaid, SVG, C4, or tabular reports from the **same** IR. This example uses a small JSON file and committed outputs to show the **shape** of that pipeline only.
