---
title: "Example step 1 — Requirements snapshot (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 1 — Requirements snapshot

## Purpose

Show how STE starts by making **expectations explicit** before design choices harden. A **requirements snapshot** bounds the **design space**: it states what must be true and what capabilities matter; it is **intent**, not a finished architecture.

> **Illustrative only.** The fragment below is a **pedagogical stub**. Field names follow patterns seen in STE workspace tooling; normative contracts live in **ste-spec**.

## Provenance

- **Conversation seed:** [Phase 1 — STE conversation](./00-ste-conversation.md) — **Stakeholder + Architect** simulation; full STE may add CE, Steelman, persona-routed probes, and toolchain-generated ADRs.

Requirement-class rows use **`RQCAP-*` / `RQCONST-*` / `RQINV-*` / `RQNFR-*`** ids—the handbook’s analogue of a flat **REQ-XXXX** list. Each id is one traceable row in the snapshot below.

## Traceability — requirement rows derived from conversation

| Requirement row | Derived from conversation segment |
|-----------------|-------------------------------------|
| RQCAP-0001 | §1 — single funnel / mandatory gateway for new edge traffic; §3 routing policy; §9 governed path ([§1](./00-ste-conversation.md#1-problem-fragmentation-and-platform-bar), [§3](./00-ste-conversation.md#3-routing-intent-versus-failover), [§9](./00-ste-conversation.md#9-operations-posture-and-single-funnel)) |
| RQCAP-0002 | §3–4 — automatic failover, bounded retries, failure classification deferred to ledger ([§3](./00-ste-conversation.md#3-routing-intent-versus-failover), [§4](./00-ste-conversation.md#4-failure-modes-ambiguity-and-iteration)) |
| RQCONST-0001 | §6–8 — multiple named cloud LLM providers; compute choice deferred ([§6](./00-ste-conversation.md#6-authentication-boundary-secrets-discipline-blast-radius), [§8](./00-ste-conversation.md#8-latency-throughput-and-honest-unknowns)) |
| RQCONST-0002 | §4–5 — normalized success contract; honest errors; unary v1 ([§4](./00-ste-conversation.md#4-failure-modes-ambiguity-and-iteration), [§5](./00-ste-conversation.md#5-response-contract-errors-and-streaming-deferral)) |
| RQINV-0001 | §2 — authenticate before provider routing; §9 reinforced ([§2](./00-ste-conversation.md#2-scope-edge-first-callers-and-deferrals), [§9](./00-ste-conversation.md#9-operations-posture-and-single-funnel)) |
| RQINV-0002 | §6–7 — central secrets; no keys in logs; no prompt/response in prod INFO logs ([§6](./00-ste-conversation.md#6-authentication-boundary-secrets-discipline-blast-radius), [§7](./00-ste-conversation.md#7-data-handling-logging-risk-observability-bar)) |
| RQNFR-0001 | §8 — P95 gateway hop ([§8](./00-ste-conversation.md#8-latency-throughput-and-honest-unknowns)) |
| RQNFR-0002 | §8 — sustained RPS soak ([§8](./00-ste-conversation.md#8-latency-throughput-and-honest-unknowns)) |

## Illustrative excerpt

```yaml
# Simplified requirements snapshot (AI gateway)
type: requirements_snapshot
snapshot_id: REQ-0001

conversation_ref: ./00-ste-conversation.md

required_capabilities:
  - req_item_id: RQCAP-0001
    name: AI Request Routing
    description: Route requests to LLM providers by type and availability
  - req_item_id: RQCAP-0002
    name: Provider Failover
    description: Fail over when the primary provider is unhealthy

required_constraints:
  - req_item_id: RQCONST-0001
    statement: Support multiple providers (OpenAI, Anthropic, local models)
  - req_item_id: RQCONST-0002
    statement: Normalize response format across providers

required_invariants:
  - req_item_id: RQINV-0001
    statement: All AI requests are authenticated before routing
  - req_item_id: RQINV-0002
    statement: Provider API keys are never logged or exposed

required_nfrs:
  - req_item_id: RQNFR-0001
    statement: Gateway P95 latency under 500ms under normal load
  - req_item_id: RQNFR-0002
    statement: Sustain 1000 RPS for sustained load tests

technology_signals:
  language: python
  infrastructure: aws
  architecture_pattern: serverless   # signal, not a decided design yet

feeds_logical_adr: ADR-L-AIGW-001
```

## What to read from it

- **Capabilities** name **what the system must do** (route, fail over).
- **Constraints** shrink **allowed shapes** (multi-provider, normalized responses).
- **Invariants** are **non-negotiable properties** unless governance revises them (auth before routing, key handling).
- **NFRs** bind **measurable expectations** (latency, throughput).
- **Technology signals** hint at context; they are **not** the same as a recorded **decision**. The snapshot points forward to a **logical ADR** id (`ADR-L-AIGW-001`) that will later hold **decisions**.

This step defines **intent** and the **design space**. It does not yet decide serverless versus containers, exact failover mechanics, or secrets tooling—that comes next.

**Architecture IR** does not appear here; nothing is **derived** yet. STE is not “just documentation”: these items are **governable expectations** that later compilation and evidence will trace.

---

**Previous:** [Phase 1 — Conversation](./00-ste-conversation.md) · **Next:** [Step 2 — Decision ledger](./02-decision-ledger.md)
