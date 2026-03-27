# Illustrative projection queries (Arch DSL sketch)

These snippets express **what** a projection selects from **Architecture IR**. They are **handbook pedagogy**—a readable stand-in for a real graph query or STE **projection specification DSL**, not normative syntax.

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

**Output:** [`generated/ir-capability-component.mmd`](generated/ir-capability-component.mmd)

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

**Output:** [`generated/ir-system-context.mmd`](generated/ir-system-context.mmd)

---

## Why this matters

- **Projection = function(IR snapshot, query/spec, layout)**. The IR stays **canonical**; Mermaid is a **derived view**.
- A mature STE toolchain might compile a **projection spec** to Mermaid, SVG, C4, or tabular reports from the **same** IR—this example only demonstrates the **shape** of that pipeline with a small JSON file and a tiny generator.
