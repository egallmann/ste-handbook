# Projection queries (Instance Scheduler example)

Illustrative **projection specs** — pedagogy only; not a normative **ste-spec** language.

## Query A — Capability / component graph

**Intent:** Show how **components** realize **capabilities** and expose **interfaces**, including **depends_on** between orchestration and data.

**Select**

- Entities where `entity_type` ∈ {`capability`, `component`, `interface`}
- Relationships where `relationship_type` ∈ {`implements`, `depends_on`, `exposes`}

**Layout**

- Layer capabilities above components; interfaces adjacent to owning component.

**Output**

- [`generated/ir-capability-component.md`](generated/ir-capability-component.md)

---

## Query B — System context (AWS services)

**Intent:** Show **orchestration** touching **EC2/RDS** as externals (plus optional hub/spoke omission for clarity).

**Select**

- Entities where `entity_type` ∈ {`component`, `external_system`}
- Relationships where `relationship_type` ∈ {`invokes_provider`, `depends_on`} and `to_entity` is `external_system` OR both ends are components

**Layout**

- Left: `COMP-5181`; right: `EXT-5181`, `EXT-5182`.

**Output**

- [`generated/ir-system-context.md`](generated/ir-system-context.md)

---

## Query C — Traceability slice

**Intent:** Show **requirements** and **invariants** tied to **decisions** and **components** (`enabled_by`, `constrains`, `supports`).

**Select**

- Entities where `entity_type` ∈ {`requirement`, `invariant`, `decision`, `component`, `capability`}
- Relationships where `relationship_type` ∈ {`enabled_by`, `constrains`, `supports`, `implements`}

**Layout**

- Requirements and invariants on the left; decisions center; components/capabilities right.

**Output**

- [`generated/ir-traceability.md`](generated/ir-traceability.md)

---

## Query D — Rules, invariants, and physical-system context

**Intent:** Project **ADR-PS** topology and **ADR-PC** deployables together with **invariants** (from IR `constrains` edges) and **Phase 6** **rule activation** rows from [Step 5d](../05d-rules-activation.md)—one place to see **what the system must satisfy** and **what rule pressure applies** per component.

**Natural language (operator):**

> For **hub** **physical** components, show **invariants** that **constrain** them and **rule families** activated from **signals** in the **physical** ADRs.

**Architecture projection DSL (sketch):**

```text
ARCH.PROJECT tabular_report "rules_invariants_ps_pc_context" {
  SOURCE ir_snapshot "../ir/architecture-ir.json"
  SOURCE rule_activation "../05d-rules-activation.md"

  LET pc = ENTITIES WHERE entity_type == "component" AND introduced_by STARTS_WITH "ADR-PC-INST-"
  LET inv = ENTITIES WHERE entity_type == "invariant"
  LET ext = ENTITIES WHERE entity_type == "external_system"

  JOIN invariant_bind ON (inv)-[:constrains]->(pc)

  JOIN ps_context ON REACHABLE(pc, ext,
    THROUGH relationship_type IN ("invokes_provider", "depends_on"))

  ATTACH rule_families FROM rule_activation
    WHERE signal SATISFIED_BY_DEPLOYMENT_TRAITS(pc, interfaces, data_stores)

  OUTPUT markdown_table "rules-invariants-system-context.md"
}
```

**Rendered illustration:** [`rules-invariants-system-context.md`](rules-invariants-system-context.md)
