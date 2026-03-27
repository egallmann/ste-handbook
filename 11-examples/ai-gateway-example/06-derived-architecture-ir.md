---
title: "Example step 6 — Derived Architecture IR (AI Gateway)"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# Step 6 — Derived Architecture IR

## Purpose

Show that **humans** author **canonical** intent and ADRs, while **compilation** produces a **structured architecture model** that tools traverse. In handbook language that model is **Architecture IR**; a concrete tool might emit an **entity registry**, **relationship registry**, or **graph index**—those files are **derived projections**, not something you “edit by hand” to fix authority problems.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

**Diagram:** [Canonical vs derived](./diagrams/canonical-vs-derived.md)

## Illustrative excerpt

```yaml
# Simplified derived entity registry (trimmed)
type: entity_registry

entities:
  - entity_id: CAP-0015
    entity_type: capability
    name: AI Request Routing
    introduced_by: ADR-L-AIGW-001
    lifecycle_stage: active
    relationships:
      depends_on: [CAP-0001]   # User Authentication (shared platform capability)

  - entity_id: BOUND-0008
    entity_type: boundary
    name: AI Gateway Boundary
    introduced_by: ADR-L-AIGW-001

  - entity_id: COMP-0010
    entity_type: component
    name: AI Gateway Lambda
    introduced_by: ADR-PC-AIGW-001
    relationships:
      implements: [CAP-0015]
      depends_on: [COMP-0003]  # Auth Service

  - entity_id: IFACE-0012
    entity_type: interface
    name: AI Gateway REST API
    introduced_by: ADR-PC-AIGW-001

  - entity_id: DEC-0025
    entity_type: decision
    name: Serverless pattern for gateway entry
    introduced_by: ADR-L-AIGW-001
```

A companion **relationship registry** (not expanded here) would materialize edges such as **`declared_in`**, **`implements`**, and **`depends_on`** with **provenance** back to canonical sources—making the graph **queryable** for impact and assessment.

## What to read from it

- Rows are **typed nodes**: **capabilities**, **boundaries**, **components**, **interfaces**, **decisions**.
- **`introduced_by`** anchors each row to the **ADR** that authorizes it—traceability from **derived** back to **canonical**.
- **`implements` / `depends_on`** preview **relationships** machines need for path queries (for example “what must change if auth changes?”).

This is **Architecture IR** in function: the **machine-reasonable system model** produced from governed artifacts. Treat exported CSV, JSON, or graph views as **disposable projections**; regenerate from canonical inputs when the pipeline is healthy.

---

**Previous:** [Step 5](./05-physical-component-adr.md) · **Next:** [Step 7 — Code semantic linkage](./07-code-semantic-linkage.md)
