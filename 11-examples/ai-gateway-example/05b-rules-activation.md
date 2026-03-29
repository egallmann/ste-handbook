---
title: "Example step 5b — Rules activation (AI Gateway)"
status: structured
maturity: L2
diagrams: false
last_reviewed: "2026-03-27"
---

# Step 5b — Rules activation (Phase 6)

## Purpose

Show **which rules would activate** in a full STE program once **physical-component** intent and **technology signals** are known. **ste-rules-library** (workspace sibling) owns real rule packs and activation mechanics; this step is **handbook illustration**: plausible **rule family names** tied to **signals** surfaced in [Step 5](./05-physical-component-adr.md) and the [requirements snapshot](./01-requirements-snapshot.md).

> **Illustrative only.** Rule **names** below are pedagogical; they are **not** normative ste-rules-library ids.

## Signal → rule activation (illustrative)

| Signal (from design / snapshot) | Rule activated (illustrative family) | Reason |
|--------------------------------|--------------------------------------|--------|
| **Uses AWS** | AWS security / landing-zone baselines | Cloud environment and shared responsibility boundary |
| **Uses Lambda** (`aws_lambda` deployment unit) | Serverless operational rules | Cold start, concurrency limits, IAM execution role |
| **Exposes REST API** at the edge | API edge / authentication rules | Untrusted callers; token validation before backend |
| **Uses Secrets Manager** | Secrets and data-protection rules | Credential lifecycle; forbid logging secret material |
| **Calls external LLM providers** | Third-party / egress rules | Off-VPC HTTP, provider contracts, data handling |
| **Multi-provider routing** | Resilience / throttling rules | Failover, retry budgets, provider-specific error mapping |

## What to read from it

- **Activation** is **signal-driven**: the same conversation would not fire “Lambda rules” before the ADR ladder commits **serverless** and **deployment_unit** facts.
- In production, **Steelman** and the rules engine consume **canonical ADRs** and **snapshots**, not free-form chat—Phase 6 makes that hand-off **visible** between **ADR-PC** and **Architecture IR** compilation.

## What this step produced and why it matters

**Governed pressure** (obligations, gaps, waivers) stays **explainable** when readers can see **why** a rule family turned on. Downstream **compilation** ([Step 6](./06-derived-architecture-ir.md)) assumes those obligations are either **satisfied** in ADRs or **explicitly waived**—the activation table is the **bridge** from “we use AWS Lambda” to “serverless rules apply.”

**Projection:** [Query D — rules, invariants, and physical-system context](./projections/projection-queries.md#query-d--rules-invariants-and-physical-system-context) and the tabular illustration [`rules-invariants-system-context.md`](./projections/rules-invariants-system-context.md) show how operators **explore** “what applies” per **physical** component once IR and activation exist.

---

**Previous:** [Step 5 — Physical-component ADR](./05-physical-component-adr.md) · **Next:** [Step 6 — Derived Architecture IR](./06-derived-architecture-ir.md)
