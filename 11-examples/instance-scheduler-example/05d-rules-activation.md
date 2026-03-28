---
title: "Example step 5d — Rules activation (Instance Scheduler)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5d — Rules activation (Phase 6)

## Purpose

Show **which rules would activate** after **physical-component** ADRs (**5a–5c**) fix deployment shapes: **Lambda**, **DynamoDB**, **EventBridge**, **cross-account IAM**, and **operator CLI**. **ste-rules-library** owns real packs; this file lists **illustrative** rule families and **reasons** so Phase 6 is **legible** in the full lifecycle.

> **Illustrative only.** Rule **names** are pedagogical, not normative library ids.

## Signal → rule activation (illustrative)

| Signal (from design / ADR-PC) | Rule activated (illustrative family) | Reason |
|------------------------------|--------------------------------------|--------|
| **Uses AWS** | AWS security / landing-zone baselines | Shared responsibility; org-wide guardrails |
| **Uses Lambda** for orchestration | Serverless operational rules | Execution roles, concurrency, timeout/retry discipline |
| **Uses EventBridge / scheduling** | Scheduled / batch control rules | Periodic evaluation; idempotent orchestration |
| **Stores state in DynamoDB** | Data protection / encryption rules | Encryption at rest, key management, table IAM |
| **Cross-account IAM** (hub ↔ spoke) | Least-privilege / trust-boundary rules | AssumeRole patterns; no mega-role |
| **EC2/RDS control-plane calls** | Workload power-management rules | Destructive APIs; safety and audit expectations |
| **Operator CLI** | Supply-chain / distribution rules | Packaging, signing, least privilege for operators |

## What to read from it

- **Signals** aggregate from **technology_stack**, **deployment_unit**, and **interaction** fields across **5a–5c**—not from a single sentence in Step 0.
- **Personas** (FinOps, Security, Cloud, Ops) in full STE often **map** to projections of these same families; the table states the **engineering reason** each family would engage.

## What this step produced and why it matters

Phase 6 answers “**what pressure** does this design invite?” before **compilation** produces the **Architecture IR** graph ([Step 6](./06-derived-architecture-ir.md)). That ordering mirrors real programs: **canonical ADRs** first, **rule activation** explodes from **declared** facts, then the **compiler** emits **entities and obligations** tools can traverse.

**Projection:** See [Query D](./projections/projection-queries.md#query-d--rules-invariants-and-physical-system-context) and [`rules-invariants-system-context.md`](./projections/rules-invariants-system-context.md) for a **per-component** view of **invariants** (`constrains` in IR) **and** **activated rule families**.

---

**Previous:** [Step 5c — Physical-component ADR (CLI)](./05c-physical-component-cli.md) · **Next:** [Step 6 — Derived Architecture IR](./06-derived-architecture-ir.md)
