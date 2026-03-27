# Part 9 — Human interface overview

This chapter introduces STE’s human-facing interface layer: interrogation, decision capture, steelmanning, reference patterns, and human-in-the-loop operation. **Agents** and **rule activation** live in Part 10. It explains how these interfaces relate to **intent** and **Architecture IR**.

## Why this matters

Most **intent** originates in human discussion. Without an interface model, tooling fragments and records diverge from reality.

## Conceptual role: intent capture boundary

Conversation and collaborative editing are the **human intent boundary**: where goals, tradeoffs, and provisional language appear first. They are not themselves the canonical architecture. Under **governance**, STE **captures**, **normalizes**, and **materializes** that discussion into structured **intent** **artifacts** (**ADRs**, requirements, **constraints**, **invariants**, and related records). Those artifacts feed **compilation**, which builds or updates **Architecture IR**—the **canonical system model** at the architecture layer for an agreed **scope**.

Read that chain as part of the **closed loop** in [System overview](../02-overview/02-03-system-overview.md): capture → **intent artifacts** → **compilation** → **Architecture IR** → **projections** and mechanical analysis → **embodiment** → **evidence** → **assessment** → **governance** → return. For lifecycle placement, see [Intent formation](../05-lifecycle/05-01-intent-formation.md).

## Planned coverage

- Major subsystems in Part 9
- Ethical and process considerations (high level)
- Boundaries with kernel automation

## Relationship to other chapters

- Conversation interface ([chapter](09-01-conversation-interface.md))
