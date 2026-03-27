---
title: "Example step 3 — Logical ADR (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 3 — Logical ADR

## Purpose

Show the **logical** ADR as the record that **answers** the ledger’s questions: pattern, failover strategy, and secrets handling, while naming **capabilities** and a **boundary** that later physical ADRs will refine. This step should feel like **closure of the decision space the ledger opened**—not a parallel decision process.

> **Illustrative only.** Pedagogical stub; **ste-spec** is normative.

## Illustrative excerpt

```yaml
# Simplified logical ADR (trimmed)
adr_type: logical
id: ADR-L-AIGW-001
title: AI Gateway — logical architecture

capabilities:
  - id: CAP-0015
    name: AI Request Routing
    description: Route authenticated traffic to providers per policy
  - id: CAP-0016
    name: Provider Failover
    description: Shift traffic when primary provider is unhealthy

decisions:
  - id: DEC-0025
    resolves_ledger: LDEC-0001
    summary: Use serverless compute for the gateway entrypoint
  - id: DEC-0026
    resolves_ledger: LDEC-0002
    summary: >-
      Combine health-check-based routing with bounded retries for failover
  - id: DEC-0027
    resolves_ledger: LDEC-0003
    summary: Store provider credentials in AWS Secrets Manager

system_boundaries:
  - id: BOUND-0008
    name: AI Gateway Boundary
    description: >-
      Public edge for AI traffic; must enforce auth before provider access
```

## What to read from it

- **Capabilities** express **logical** responsibilities aligned with the snapshot (routing, failover).
- Each **decision** references **`resolves_ledger`**, tying back to **LDEC-0001…0003**. That is the concrete pattern for “**resolve, don’t invent**.”
- **Serverless**, **health checks + retries**, and **Secrets Manager** are the **chosen** alternatives from the ledger lists.
- **BOUND-0008** states a **trust-relevant** edge: authentication before provider access echoes **RQINV-0001**.

### Where these commitments reappear

The same capability, boundary, and decision ids are not trapped in prose—they propagate:

- In **[Step 4](./04-physical-system-adr.md)** and **[Step 5](./05-physical-component-adr.md)** as **physical** topology and component responsibility.
- In **[Step 6](./06-derived-architecture-ir.md)** as **rows** in a derived **entity registry** (part of **Architecture IR** in handbook terms).

**Architecture IR** is still **downstream**: the logical ADR is **canonical intent**, not the compiled graph.

---

**Previous:** [Step 2](./02-decision-ledger.md) · **Next:** [Step 4 — Physical-system ADR](./04-physical-system-adr.md)
