---
title: "Example step 6 — Derived Architecture IR (AI Gateway)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 6 — Derived Architecture IR

## Purpose

Show that **humans** author **canonical** intent and ADRs, while **compilation** (**Phase 7**) produces a **structured architecture model** that tools traverse. Complete **Phase 6 — rules activation** ([Step 5b](./05b-rules-activation.md)) before this step so **signal → rule** context is explicit. In handbook language that model is **Architecture IR**; a concrete tool might emit an **entity registry**, **relationship registry**, or **graph index**—those files are **derived projections**, not something you “edit by hand” to fix authority problems.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

**Diagram:** [Canonical vs derived](./diagrams/canonical-vs-derived.md)

## Machine-readable IR snapshot (honest projections)

This example keeps **one consolidated IR file** so diagrams can be **regenerated** from the same ids and edges as the narrative:

- [`ir/architecture-ir.json`](./ir/architecture-ir.json) — entities and relationships (aligned with steps 3–5).
- [`projections/generated/ir-capability-component.md`](./projections/generated/ir-capability-component.md) and [`ir-system-context.md`](./projections/generated/ir-system-context.md) — **Mermaid** views produced by a **projection adapter** from that IR (selections sketched in [`projection-queries.md`](./projections/projection-queries.md)). The handbook commits these outputs; **do not hand-edit** them except via IR or adapter regeneration.
- [`projections/projection-queries.md`](./projections/projection-queries.md) — illustrative **projection-query** sketches (Arch DSL–style pedagogy) that describe **what** each view selects from IR.
- [`projections/rules-invariants-system-context.md`](./projections/rules-invariants-system-context.md) — **Query D** illustration: **ADR-PS / ADR-PC** context with **invariants** and **Phase 6** **rule families** per component (federated join; natural language compiles to **conjunctions** of predicates in full STE).

That pipeline is the handbook’s demonstration of **projection = f(IR snapshot, query/spec, layout)**: the IR stays authoritative; Mermaid is a **derived** view. Conceptual process figures under [`diagrams/`](./diagrams/) are **not** claimed to be emitted from this JSON.

## Illustrative excerpt (registry-shaped)

```yaml
# Simplified derived entity registry (trimmed) — see architecture-ir.json for full graph
type: entity_registry

entities:
  - entity_id: CAP-0015
    entity_type: capability
    name: AI Request Routing
    introduced_by: ADR-L-AIGW-001
    relationships:
      depends_on: [CAP-0001]

  - entity_id: CAP-0016
    entity_type: capability
    name: Provider Failover
    introduced_by: ADR-L-AIGW-001

  - entity_id: BOUND-0008
    entity_type: boundary
    name: AI Gateway Boundary
    introduced_by: ADR-L-AIGW-001

  - entity_id: COMP-0010
    entity_type: component
    name: AI Gateway Lambda
    introduced_by: ADR-PC-AIGW-001
    relationships:
      implements: [CAP-0015, CAP-0016]
      depends_on: [COMP-0003]

  - entity_id: COMP-0003
    entity_type: component
    name: Auth Service
    introduced_by: platform_catalog

  - entity_id: IFACE-0012
    entity_type: interface
    name: AI Gateway REST API
    introduced_by: ADR-PC-AIGW-001

  - entity_id: DEC-0025
    entity_type: decision
    name: Serverless gateway entry
    introduced_by: ADR-L-AIGW-001
  - entity_id: DEC-0026
    entity_type: decision
    name: Health checks plus bounded retries for failover
    introduced_by: ADR-L-AIGW-001
  - entity_id: DEC-0027
    entity_type: decision
    name: Secrets in AWS Secrets Manager
    introduced_by: ADR-L-AIGW-001

# Phase 7 — boundaries, contracts, deployment mappings (YAML excerpt)

boundaries:
  - boundary_id: BOUND-0008
    name: AI Gateway Boundary
    introduced_by: ADR-L-AIGW-001

contracts:
  - contract_id: CTR-AIGW-0001
    parties: [COMP-0010, External_LLM_Provider]
    protocol: https_json_provider_api
    introduced_by: ADR-PC-AIGW-001

deployment_mappings:
  - component_id: COMP-0010
    deployment_target: aws_lambda
    api_route: POST /v1/ai/complete
  - component_id: COMP-0003
    deployment_target: platform_auth_service
    note: introduced_by platform_catalog in IR JSON
```

Edges such as **`implements`**, **`depends_on`**, **`exposes`**, **`invokes_provider`**, and **`realizes_external`** are listed explicitly in [`architecture-ir.json`](./ir/architecture-ir.json) for **queryable** impact and **projection** generation.

## What to read from it

- Rows are **typed nodes**: **capabilities**, **boundaries**, **components**, **interfaces**, **decisions**, plus **external systems** in the JSON for context projections.
- **`introduced_by`** anchors each row to the **ADR** (or catalog) that authorizes it—traceability from **derived** back to **canonical**.
- **`implements` / `depends_on`** (and the other edge types in the JSON) are what a graph query or **Arch DSL** projection spec would traverse—see [projection queries](./projections/projection-queries.md).

This is **Architecture IR** in function: the **machine-reasonable system model** produced from governed artifacts. Treat exported CSV, JSON, graph views, and **Mermaid** as **disposable projections**; regenerate from canonical inputs when the pipeline is healthy.

---

**Previous:** [Step 5b — Rules activation](./05b-rules-activation.md) · **Next:** [Step 7 — Code semantic linkage](./07-code-semantic-linkage.md)
