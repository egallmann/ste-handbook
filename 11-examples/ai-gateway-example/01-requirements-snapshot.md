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

## Illustrative excerpt

```yaml
# Simplified requirements snapshot (AI gateway)
type: requirements_snapshot
snapshot_id: REQ-0001

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

**Previous:** [Part 11 overview](../00-overview.md) · **Next:** [Step 2 — Decision ledger](./02-decision-ledger.md)
