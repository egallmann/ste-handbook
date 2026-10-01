---
title: "Illustrative artifact walkthrough"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-10-01"
---

# Illustrative artifact walkthrough

> **Illustrative only.** The YAML-shaped fragments below are **pedagogical stubs** and semantic sketches. They are **not** normative schema documentation and do **not** claim completed canonical-entity / identity realization (CE-01) or compiled Architecture IR `kind` realization for Normative Propositions. Field names follow patterns seen in released ADR-Kit authoring and normalized-model contract resources. STE-wide semantic and Architecture IR authority lives in ste-spec. Concrete ADR-Kit authoring, normalized-model, interpretation, and semantic-contract shapes live in ADR-Kit’s released contract resources.

## The Problem

Reading about **intent**, **Architecture IR**, and **projections** in the abstract leaves a gap: what do the **artifacts** look like when a governed ADR declares a Normative Proposition that becomes machine-addressable without becoming independent policy? A tiny, end-to-end slice answers that question without turning the handbook into a specification appendix.

## The Reframe

Think of the following fragments as one **story**: governed ADR intent → a local normative consequence as a Normative Proposition with stable identity → structural realization → normalized representation (embodiment evidence) → projection → and the negative claim that being represented or reachable does not prove applicability or conformance.

Normalized representation is **not** automatically Architecture IR. Mapping into compiled IR remains where accepted STE semantic authority establishes it; the deferred canonical-entity / identity realization (CE-01) remains deferred, and the corresponding ste-spec mechanical / corpus integration remains deferred.

## The Model

### 1. Logical ADR intent with a Normative Proposition (authoring sketch)

A **logical** ADR states decisions above any single module layout. An ADR-local Normative Proposition is **contained** in the ADR: authority and lifecycle remain with the declaring ADR. Authoring fields include stable `id`, `alias_id`, `alias_name`, `statement`, `normative_force`, `scope`, and optional `rationale`. Do not treat this block as a complete serialized contract object.

```yaml
# Illustrative logical ADR with NP (semantic sketch — not a complete authoring object)
adr_type: logical
id: "01999999-0000-7000-8000-000000000010"  # illustrative UUIDv7-shaped id
alias_id: ADR-L-0001
alias_name: refuse-stale-graph-work-decision
title: Preflight gate must refuse stale graph work
decisions:
  - id: "01999999-0000-7000-8000-000000000011"
    alias_id: DEC-0001
    summary: Assistant-facing work requires a freshness gate before execution
normative_propositions:
  - id: "01999999-0000-7000-8000-000000000001"  # illustrative UUIDv7-shaped id
    alias_id: NP-0001
    alias_name: refuse-stale-graph-work
    statement: >
      Assistant-facing work MUST NOT proceed when graph freshness
      evaluation reports the semantic graph as stale for the requested scope.
    normative_force: MUST NOT
    scope: Assistant-facing preflight over the declared runtime orchestration boundary
    rationale: >
      Stale graph state yields lossy obligation reconstruction under time pressure.
```

### 2. Structural realization (physical-component sketch)

A **physical-component** ADR refines where the obligation is embodied—still under declaring ADR authority for the NP, not a new NP lifecycle.

```yaml
# Illustrative physical-component ADR (trimmed)
adr_type: physical-component
id: "01999999-0000-7000-8000-000000000020"
alias_id: ADR-PC-0003
title: Preflight freshness gate
implements_logical:
  - ADR-L-0001
component_specifications:
  - id: "01999999-0000-7000-8000-000000000021"
    alias_id: COMP-0003
    name: Preflight freshness and reconciliation gate
    responsibilities: |
      - Evaluate graph freshness for the requested scope
      - Refuse assistant-facing work when freshness fails
```
### 3. Normalized entity row (embodiment evidence)

This example shows a **normalized machine-facing entity row**. Registry, index, normalized, and compiled-IR surfaces retain distinct governed roles; do not treat this row as Architecture IR, Architecture Index, or `Compiled_IR_Document`. Hand-editing normalized rows when the bug is upstream **intent** is the wrong control surface.

Here a Normative Proposition appears as a typed entity. The `declaring_adr` and `source_artifact` objects are **normalized qualification**: they preserve ownership/provenance after detachment from source position; they do **not** create authority. Fields are illustrative and trimmed; omit unused contract ceremony rather than inventing scalar shapes.

```yaml
# Illustrative normalized NP entity row (semantic sketch — trimmed)
entities:
  - entity_type: normative_proposition
    id: "01999999-0000-7000-8000-000000000001"  # illustrative UUIDv7-shaped id
    alias_id: NP-0001
    alias_name: refuse-stale-graph-work
    statement: >
      Assistant-facing work MUST NOT proceed when graph freshness
      evaluation reports the semantic graph as stale for the requested scope.
    normative_force: MUST NOT
    scope: Assistant-facing preflight over the declared runtime orchestration boundary
    declaring_adr:
      provider: adr-kit.authoring
      id: "01999999-0000-7000-8000-000000000010"  # declaring ADR UUIDv7-shaped id
      alias_id: ADR-L-0001
      alias_name: refuse-stale-graph-work-decision
    source_artifact:
      source_type: logical_adr
      source_ref: ADR-L-0001
      artifact_path: adrs/logical/ADR-L-0001-refuse-stale-graph-work.yaml
      content_digest: "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
```

### 4. Structural entity and relationship rows

```yaml
# Illustrative component entity (trimmed)
entities:
  - id: "01999999-0000-7000-8000-000000000021"
    alias_id: COMP-0003
    entity_type: component
    name: Preflight freshness and reconciliation gate
    introduced_by: ADR-PC-0003

# Illustrative relationship (trimmed)
relationships:
  - relationship_type: declared_in
    from_entity_id: "01999999-0000-7000-8000-000000000011"
    to_entity_id: "01999999-0000-7000-8000-000000000010"
    provenance_classification: explicit
```

### 5. Projection excerpt (derived)

A human-facing projection may list the Normative Proposition for review. Inclusion is **selection**, not applicability.

```text
Projection: preflight-normative-candidates (illustrative)
IR / model snapshot: (declared scope)
Selected because: linked to ADR-L-0001 and COMP-0003 neighborhood

- NP-0001 refuse-stale-graph-work
  force: MUST NOT
  declaring ADR: ADR-L-0001
  scope: Assistant-facing preflight over the declared runtime orchestration boundary
  note: Included in this view ≠ proven applicable to every task; ≠ conformance.
```
### 6. Negative claim (mandatory)

Being represented on a normalized surface, reachable from a component, or visible in a projection does **not** prove:

- independent NP authority;
- effectivity for a concrete runtime moment;
- applicability to a task;
- implementation conformance.

Task-relative applicability remains later work ([Context assembly and MVC](../08-runtime/08-05-context-assembly-and-mvc.md)).

| Layer | What this walkthrough shows |
|-------|-----------------------------|
| Declaring ADR | Authority and lifecycle for the NP |
| Normative Proposition | Addressable ADR-local normative meaning |
| Structure | Component that realizes related decisions |
| Normalized surface | Detached structured `declaring_adr` / `source_artifact` qualification (embodiment evidence) |
| Projection | Derived view preserving force/authority/scope |
| Not shown as done | Deferred canonical-entity / identity realization (CE-01); compiled IR NP `kind`; applicability algorithm |

## The Implications

When you adopt STE-shaped tooling, expect the same division of labor: **govern** and version **intent** and published machine representation; maintain Index, registries, normalized, and compiled surfaces under their contracts; **never** let a derived projection become the silent source of truth or a silent applicability engine. If a walkthrough fragment disagrees with accepted STE semantic authority or with ADR-Kit’s released contract resources for ADR-Kit shapes, those authorities win in their respective domains.

## Relationship to STE system

- **ADR ladder:** [Architecture decision records](../03-artifacts/03-01-architecture-decision-records.md).
- **Canonical versus derived:** [Projections overview](04-08-projections-overview.md).
- **Semantic graph:** [IR as a semantic graph](04-07-ir-as-a-graph.md).
- **Construction boundaries:** [Compilation and semantic materialization](04-04-compilation.md).
- **Reading discipline:** [How to read diagrams and projections](../02-overview/02-05-how-to-read-diagrams-and-projections.md).
- **Explanatory consequences:** [Can architecture change what a model is likely to do?](../13-architectural-essays/13-05-can-architecture-change-what-a-model-is-likely-to-do.md).
- **Full lifecycle example (complementary):** [Part 11 — Canonical example: AI Gateway through STE](../11-examples/00-overview.md).

## Summary

- **Logical** ADRs may declare Normative Propositions with stable identity while retaining declaring authority and lifecycle.
- Normalized structured `declaring_adr` / `source_artifact` qualification preserves ownership after detachment; it does not create authority.
- Normalized, registry, index, and compiled-IR surfaces retain distinct roles; projections are derived human/task renderings—not automatic Architecture IR and not applicability engines.
- Represented or reachable ≠ applicable or conformant.

**Next:** Continue to Part 5 — [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md).
