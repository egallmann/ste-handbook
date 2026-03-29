# Rules, invariants, and physical-system context (illustrative projection)

This file is a **tabular composite projection** for the Instance Scheduler example: **Architecture IR** ([`../ir/architecture-ir.json`](../ir/architecture-ir.json)) plus **Phase 6 — rules activation** ([Step 5d](../05d-rules-activation.md)) and **physical-system** topology from [Step 4a](../04a-physical-system-hub.md) / [4b](../04b-physical-system-remote.md). **ste-spec** defines invariant and trace semantics; **ste-kernel** pins how richer **rule** edges compile—this walkthrough stays **handbook-grade**.

See the query-shaped spec in [`projection-queries.md`](projection-queries.md) (Query D).

---

## Physical-system context (ADR-PS-INST-001 hub + ADR-PS-INST-002 remote)

| Element | Introduced by | Role (summary) |
|---------|---------------|----------------|
| `COMP-5181` | ADR-PC-INST-001 | Hub orchestration (Lambda suite); invokes EC2/RDS. |
| `COMP-5182` | ADR-PC-INST-002 | DynamoDB data plane (config, state, registry). |
| `COMP-5183` | ADR-PC-INST-003 | Operator CLI. |
| `EXT-5181` | ADR-PS-INST-001 | Amazon EC2 (control-plane target). |
| `EXT-5182` | ADR-PS-INST-001 | Amazon RDS (control-plane target). |

Spoke-side **remote** stack and trust packaging are detailed in the physical-system ADRs; projection queries use the same **ids** for joins.

---

## Invariants constraining components (from IR)

`constrains` edges in [`architecture-ir.json`](../ir/architecture-ir.json) (see also [traceability Mermaid](generated/ir-traceability.md)):

| Invariant | Constrains | Meaning (short) |
|-----------|------------|-----------------|
| `INV-5181` | `COMP-5181` | Schedule-bound automation on orchestration. |
| `INV-5182` | `COMP-5181` | Least-privilege cross-account trust touches orchestration. |

**Data plane and CLI** inherit obligations through **depends_on** / **implements** chains and through **Phase 6** rule mapping below—not always as duplicate `constrains` rows in this small IR.

---

## Activated rule families → components (Phase 6 join)

**Source:** [Step 5d — Rules activation](../05d-rules-activation.md). **Join (illustrative):** map each **signal** to components that realize it.

| Rule family (illustrative) | Applies to (ids) | Reason (short) |
|----------------------------|------------------|----------------|
| AWS security / landing-zone baselines | `COMP-5181`, `COMP-5182`, `COMP-5183` | All AWS-tied deployables |
| Serverless operational rules | `COMP-5181` | Lambda orchestration |
| Scheduled / batch control rules | `COMP-5181` | EventBridge / interval evaluation |
| Data protection / encryption rules | `COMP-5182` | DynamoDB persistence |
| Least-privilege / trust-boundary rules | `COMP-5181` | Hub ↔ spoke IAM |
| Workload power-management rules | `COMP-5181` | EC2/RDS stop/start APIs |
| Supply-chain / distribution rules | `COMP-5183` | Operator CLI package |

---

## Natural language → projection predicate (sketch)

Example operator request:

> “For **every** hub **physical** component, list **invariants** that **directly constrain** it and **rule families** activated by **signals** from ADR-PC **and** ADR-PS.”

A projection adapter would compile that to selections equivalent to:

- Entities: `component` where `introduced_by` matches `ADR-PC-INST-*` **or** `related_to` hub topology from ADR-PS.
- Edges: `invariant_constrains_component` (compiled) **union** activation join from **rules projection** output.
- Optional filter (DSL predicate): `component -[:invokes_provider]-> (:external_system)` **AND** `component.deployment_unit == aws_lambda`.

That **conjunction** is the sort of **complex predicate** natural language maps to—then the spec is **stored**, diffed, and re-run on the next IR snapshot.

---

## See also

- [Projection queries — Query D](projection-queries.md#query-d--rules-invariants-and-physical-system-context)
- [Traceability projection (Mermaid)](generated/ir-traceability.md)
- [Projections overview — handbook](../../../04-architecture-model/04-08-projections-overview.md)
