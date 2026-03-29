# Rules, invariants, and physical-system context (illustrative projection)

This file is a **reader-facing illustration** of a **composite projection**: it combines **Architecture IR** ([`../ir/architecture-ir.json`](../ir/architecture-ir.json)) with **Phase 6 — rules activation** ([Step 5b](../05b-rules-activation.md)) and **component invariants** declared in [ADR-PC-AIGW-001](../05-physical-component-adr.md). In production STE, a **projection adapter** may materialize similar rows from a **single** compiled graph once **rule evaluation subjects** and **enforces** edges are normalized—**ste-spec** is normative for semantics; mechanical edge enums are pinned by **ste-kernel**.

**Not** a committed auto-generated Mermaid file: this is a **tabular view** suited to “**what applies to this deployable unit?**” questions. See the query-shaped spec in [`projection-queries.md`](projection-queries.md) (Query D).

---

## Physical-system context (ADR-PS-AIGW-001)

| Element | Role (summary) |
|---------|----------------|
| **AI Gateway Lambda** (`COMP-0010`) | Deployable unit at the edge; implements routing/failover capabilities. |
| **Auth Service** (`COMP-0003`) | Platform dependency; realizes organization auth (`EXT-AUTH`). |
| **OpenAI API** (`EXT-OPENAI`) | External LLM provider invoked by the gateway. |
| **Organization auth service** (`EXT-AUTH`) | External identity/validation surface at the system boundary. |

Topology and trust-zone detail live in [Step 4 — Physical-system ADR](../04-physical-system-adr.md); the rows above are the **IR ids** that projection joins against.

---

## Physical components (ADR-PC) — interfaces and deployment

| Component | Introduced by | Deployment target | Key interface |
|-----------|---------------|-------------------|---------------|
| `COMP-0010` | ADR-PC-AIGW-001 | `aws_lambda` | `IFACE-0012` — REST `POST /v1/ai/complete` |

---

## Invariants on components (ADR-PC + snapshot intent)

These are the **executable** component invariants from the ADR excerpt; they **specialize** snapshot items **RQINV-0001** / **RQINV-0002** for the gateway Lambda.

| Invariant id | Statement | Constrains |
|--------------|-----------|------------|
| **PCINV-0001** | No code path forwards to a provider without prior auth success | `COMP-0010` |
| **PCINV-0002** | Structured logs include `request_id`; never log secret material | `COMP-0010` |

*Mechanical IR note:* a full compiler might emit `invariant_constrains_component` edges for these after ADR-PC ingestion; this example keeps them **visible in the projection narrative** without expanding [`architecture-ir.json`](../ir/architecture-ir.json).

---

## Activated rule families → components (Phase 6 join)

**Source of rule rows:** signal → rule table in [Step 5b](../05b-rules-activation.md). **Join logic (illustrative):** match **signals** implied by ADR-PC (`aws_lambda`, REST API, Secrets Manager, multi-provider egress) to **components** and **interfaces** that realize those signals.

| Rule family (illustrative) | Applies to (ids) | Reason (short) |
|----------------------------|------------------|----------------|
| AWS security / landing-zone baselines | `COMP-0010`, `IFACE-0012` | Cloud-hosted edge surface |
| Serverless operational rules | `COMP-0010` | Lambda execution role, concurrency, timeouts |
| API edge / authentication rules | `IFACE-0012`, `COMP-0010` | Untrusted callers; bearer expectation |
| Secrets and data-protection rules | `COMP-0010` | Provider credentials lifecycle |
| Third-party / egress rules | `COMP-0010` | Off-VPC calls to LLM APIs |
| Resilience / throttling rules | `COMP-0010` | Failover and retry policy surface |

---

## Natural language → projection predicate (sketch)

Operators typically **do not** author raw DSL for this view. In STE, the **conversation / projection subsystem** turns prompts such as:

> “Show rules and invariants for each Lambda in the AI gateway **physical** design, in **system** context.”

into a **stored projection spec** (graph query, adapter config, or internal DSL—see [`projection-queries.md`](projection-queries.md)) that:

1. Selects entities with `introduced_by` ∈ {ADR-PC-AIGW-001, ADR-PS-AIGW-001} or reachable via `implements` / `exposes` / `invokes_provider` / `depends_on` from those components.
2. Attaches **invariant** rows **declared_in** ADR-PC (or compiled invariant nodes).
3. **Joins** **rule activation** rows produced when **Phase 6** evaluated **signals** from the same ADRs and snapshot.

**Complex predicates** (“only components that both **invoke** an external LLM **and** **expose** a public REST route”) are **where** an internal **Architecture DSL** (or equivalent query language) earns its keep: the NL prompt compiles to a **conjunction** of typed predicates over IR, not a one-off script.

---

## See also

- [Projection queries — Query D](projection-queries.md#query-d--rules-invariants-and-physical-system-context)
- [Projections overview — handbook](../../../04-architecture-model/04-08-projections-overview.md) (Part 4)
- [IR as a graph](../../../04-architecture-model/04-07-ir-as-a-graph.md)
