---
title: "Illustrative artifact walkthrough"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Illustrative artifact walkthrough

> **Illustrative only.** The YAML-shaped fragments below are **pedagogical stubs**. They are **not** normative schema documentation. Field names and shapes follow patterns seen in STE workspace tooling; precise contracts live in **ste-spec** and your organization’s generators.

## The Problem

Reading about **intent**, **Architecture IR**, and **projections** in the abstract leaves a gap: what do the **artifacts** actually look like at the boundary between “a decision” and “something a machine can traverse”? A tiny, end-to-end slice answers that question without turning the handbook into a specification appendix.

## The Reframe

Think of the following fragments as one **story** moving down the **ADR refinement ladder** and outward into **derived** registries: **logical** commitment → **physical-system** topology → **physical-component** responsibility → rows a compiler could emit for **entities** and **relationships**, plus a synthetic **gap** entry of the kind **unresolved** registries carry.

## The Model

### 1. Logical ADR fragment (intent)

A **logical** ADR states semantics and decisions above any single module layout. Capabilities and decision IDs give compilation something stable to anchor.

```yaml
# Illustrative logical ADR (trimmed)
adr_type: logical
id: ADR-L-0007
title: Graph freshness and obligation projection semantics
capabilities:
  - id: CAP-0007
    name: Surface graph freshness and obligation projection semantics
    description: >-
      Canonical freshness, invalidation, and obligation semantics for runtime consumers.
decisions:
  - id: DEC-0007
    summary: Freshness and obligation projection are logical runtime semantics
```

### 2. Physical-system ADR fragment (subsystem boundary)

A **physical-system** ADR names boundaries and component **topology** that realize the logical commitments—**where** major parts sit and how they relate, not every function body.

```yaml
# Illustrative physical-system ADR (trimmed)
adr_type: physical-system
id: ADR-PS-0001
title: Runtime orchestration and assistant integration
implements_logical:
  - ADR-L-0007
system_boundaries:
  - id: SYSBOUND-0001
    name: Runtime orchestration boundary
    description: >-
      Assistant-facing operations over fresh semantic graph state.
component_topology:
  components:
    - name: Preflight freshness gate
      implements_adr: ADR-PC-0003
```

### 3. Physical-component ADR fragment (implementable responsibility)

A **physical-component** ADR ties the system picture to **interfaces** and implementation anchors (paths are illustrative).

```yaml
# Illustrative physical-component ADR (trimmed)
adr_type: physical-component
id: ADR-PC-0003
title: Preflight freshness and reconciliation gating
implements_system:
  - ADR-PS-0001
implements_logical:
  - ADR-L-0007
component_specifications:
  - id: COMP-0003
    name: Preflight freshness and reconciliation gate
    responsibilities: |
      - Evaluate graph freshness
      - Gate work when reconciliation is required
    interfaces:
      - id: IFACE-0003
        type: library_api
        specification: |
          checkFreshness, preflightReconciliation
```

### 4. Derived registry entry (entity)

Registries are **compiled rows**—handy for tools, wrong to “fix by hand” when the bug is upstream **intent**.

```yaml
# Illustrative entity_registry row (trimmed)
entities:
  - entity_id: COMP-0003
    entity_type: component
    name: Preflight freshness and reconciliation gate
    introduced_by: ADR-PC-0003
    lifecycle_stage: active
    source_artifact_type: physical_component_adr
```

### 5. Derived relationship entry

**Relationships** make the graph traversable: here, a capability is **declared in** its owning logical ADR.

```yaml
# Illustrative relationship_registry row (trimmed)
relationships:
  - relationship_id: declared_in:CAP-0007:ADR-L-0007
    relationship_type: declared_in
    from_entity_id: CAP-0007
    to_entity_id: ADR-L-0007
    provenance_classification: explicit
    canonical_source_ref: ADR-L-0007#CAP-0007
```

### 6. Unresolved / gap entry (synthetic)

Live repositories often keep this list empty while healthy; the **shape** still matters for **governance** visibility.

```yaml
# Illustrative unresolved_registry row (synthetic)
unresolved:
  - id: GAP-ILLU-001
    summary: Reconciliation backoff policy not yet aligned with ADR-L-0007
    severity: non_blocking
    owning_artifact_hint: ADR-PC-0003
```

### 7. Freshness and obligations (conceptual tie-in)

| Logical commitment (illustrative) | Where it shows up in the story |
|-----------------------------------|--------------------------------|
| CAP-0007 / DEC-0007 | Declared in **logical** ADR; traced into PS/PC ADRs |
| Preflight gate | **Physical-component** responsibility before assistant-facing work |
| `declared_in` edge | **Relationship registry** makes ownership queryable |

This table is not a runtime API; it shows how **obligations** and **freshness** semantics link layers readers already saw in [Runtime evidence](../08-runtime/08-00-runtime-evidence.md).

## The Implications

When you adopt STE-shaped tooling, expect the same division of labor: **govern** and version **intent** and published IR; **generate** manifests and registries; **never** let a derived file become the silent source of truth. If a walkthrough fragment disagrees with **ste-spec**, the specification wins.

## Relationship to STE system

- **ADR ladder diagram:** [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md).
- **Canonical versus derived diagram:** [Projections overview](04-08-projections-overview.md).
- **Projection bundle:** [IR as a graph](04-07-ir-as-a-graph.md).
- **Reading discipline:** [How to read diagrams and projections](../02-overview/02-05-how-to-read-diagrams-and-projections.md).
- **Closed loop:** [System overview](../02-overview/02-03-system-overview.md).

## Summary

- **Logical** ADRs carry semantic **decisions** and capabilities; **physical-system** and **physical-component** ADRs **refine** them into topology and implementable responsibility.
- **Manifests** and **registries** are **derived**; treat compilation failures and stale outputs as **governance** signals.
- **Unresolved** entries make **gaps** visible without pretending they are **canonical** structure.

**Next:** Continue to Part 5 — [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md).
