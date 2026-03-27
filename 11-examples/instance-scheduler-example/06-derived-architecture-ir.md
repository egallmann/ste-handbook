---
title: "Example step 6 — Derived Architecture IR (Instance Scheduler)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 6 — Derived Architecture IR

## Purpose

Show **compilation** from **canonical** ADRs (steps 3–5) into a **consolidated Architecture IR** snapshot that tools can traverse. This example **adds** first-class **`requirement`** and **`invariant`** entities and **trace edges** (`enabled_by`, `constrains`, `supports`) that align with the **semantic** relationship grammar in **ste-spec** ([`STE-Architecture-Intermediate-Representation.md`](../../../ste-spec/architecture/STE-Architecture-Intermediate-Representation.md)). **adr-architecture-kit** remains the reference for **YAML authoring** shapes; **mechanical** `Compiled_IR_Document` edge enums stay **pinned** by ste-spec / ste-kernel contracts—this JSON is **handbook-illustrative**.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Architecture IR in the STE loop

- **ADRs (Steps 3a–5c)** are the **source of truth** for architecture: human-reviewed **canonical** commitments (logical, physical-system, physical-component).
- **Architecture IR** is the **compiled model** derived from those ADRs: a graph of **entities** (requirements, invariants, components, decisions, …) and **relationships** tools can **query**—not a replacement for ADRs, but the **machine-readable** shape of what they declare.
- **Projections** are **views** generated from IR **plus** explicit queries—for example Mermaid diagrams and narrative indices under [`projections/`](./projections/) (see [`projections/generated/`](./projections/generated/) and [`projections/projection-queries.md`](./projections/projection-queries.md)). Change the IR (or the query), regenerate the view; do not treat diagrams as authority on their own.
- **EDR** (Step 8) **attaches runtime and operational evidence** to **IR entities**—for example findings linked to **components** and **requirements**—so assessment is **grounded** in the same model as design.
- **Drift** (Step 9) is detected by **comparing** the **declared model** (ADRs + IR + obligations) to **observed reality** (IAM, tags, logs, config) via **linkage** and **evidence**—then **correction** flows back through **governed** change to intent or implementation.

**Diagram:** [Intent to design](./diagrams/intent-to-design.md)

## Machine-readable IR snapshot (honest projections)

- [`ir/architecture-ir.json`](./ir/architecture-ir.json) — entities and relationships across requirements, invariants, decisions, capabilities, components, interfaces, and externals.
- [`projections/generated/ir-capability-component.md`](./projections/generated/ir-capability-component.md) — Mermaid: capabilities, components, interfaces, core `implements` / `depends_on` / `exposes`.
- [`projections/generated/ir-system-context.md`](./projections/generated/ir-system-context.md) — Mermaid: components, EC2/RDS externals, cross-boundary invokes.
- [`projections/generated/ir-traceability.md`](./projections/generated/ir-traceability.md) — Mermaid: requirements, invariants, decisions, and selected trace edges.
- [`projections/projection-queries.md`](./projections/projection-queries.md) — query-shaped specs for each view.

Regenerate committed Mermaid with `python generate_projections.py` from this directory (maintainer helper; typically gitignored like the AI Gateway example).

## Illustrative excerpt (registry-shaped)

```yaml
type: entity_registry
snapshot_id: INST-IR-2026-03-27

entities:
  - entity_id: REQ-5181
    entity_type: requirement
    name: Cost-aware EC2/RDS schedule control
    introduced_by: REQ-INST-2026-03-27

  - entity_id: INV-5181
    entity_type: invariant
    name: Schedule-bound automation
    introduced_by: ADR-L-INST-001

  - entity_id: COMP-5181
    entity_type: component
    name: Scheduling orchestration Lambda suite
    introduced_by: ADR-PC-INST-001

relationships:
  - relationship_type: enabled_by
    from: REQ-5181
    to: DEC-5181
  - relationship_type: constrains
    from: INV-5181
    to: COMP-5181
  - relationship_type: implements
    from: COMP-5181
    to: CAP-5181
```

## What to read from it

- **Requirements** and **invariants** are **first-class nodes**, not only bullet rows inside Markdown—this supports **evidence subjects** and **governed trace** into components.
- **Projection** remains **pure function** of IR + query: edit the IR (or adapter config), regenerate views—do not “fix” diagrams by hand unless you intentionally accept drift.

## What this step produced and why it matters

The **Architecture IR** snapshot is the **queryable system model** for this example: it consolidates what ADRs scattered across files **mean** as a **single graph**. Tooling can traverse **trace edges** (for example from **requirements** to **decisions** to **components**) without parsing Markdown by hand. That is what enables **repeatable projections**, **evidence attachment**, and **drift checks** in the later lifecycle steps—STE is operating on a **model**, not a pile of documents.

---

**Previous:** [Step 5c](./05c-physical-component-cli.md) · **Next:** [Step 7 — Code semantic linkage](./07-code-semantic-linkage.md)
