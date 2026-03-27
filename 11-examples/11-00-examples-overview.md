# Part 11 — Examples Overview

This chapter explains the examples part: end-to-end walkthroughs that illustrate how STE artifacts chain together. Examples are illustrative; they do not define normative requirements.

## Canonical end-to-end example (AI Gateway)

The primary walkthrough is **[Canonical example: one system through STE](00-overview.md)**, followed in order by the steps under `ai-gateway-example/` (requirements snapshot → ledger → ADR ladder → derived IR → code linkage → EDR → drift and correction) and the companion diagrams in `ai-gateway-example/diagrams/`.

For **Architecture IR → projection**, the same example includes [`ai-gateway-example/ir/architecture-ir.json`](ai-gateway-example/ir/architecture-ir.json) and **regenerated** Mermaid under [`ai-gateway-example/projections/generated/`](ai-gateway-example/projections/generated/), with [`projection-queries.md`](ai-gateway-example/projections/projection-queries.md) as illustrative query-shaped specs.

## Why this matters

Examples bridge abstraction to practice. Readers use them to sanity-check understanding of earlier parts.

## Planned coverage

- How to read examples
- Assumptions and simplifications
- Pointers to spec for real constraints

## Relationship to other chapters

- Example system ([chapter](11-01-example-system.md))
