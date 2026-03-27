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
