---
title: "Part 11: STE examples — AI Gateway and Instance Scheduler"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-27"
---

# STE examples: systems through the full lifecycle

## The Problem

STE is easy to describe as layers and loops, yet still feel abstract: readers may understand the vocabulary and still struggle to see **one thread** from bounded expectations to a **governed**, **self-correcting** lifecycle. Without worked systems, **Architecture IR**, **embodiment linkage**, and **EDR**-shaped evidence can sound like parallel buzzwords instead of one operational story.

## The Reframe

Part 11 provides **two** walkthroughs. Start with the **AI Gateway** example—**small**, one logical ADR and one physical-system / physical-component pair—then optionally read the **Instance Scheduler** example for **higher fidelity**: a **single-user convergent design chat** (conversation engine + **Architect agent** with **personas**; full STE: **ste-rules-library** projections drive activation and later **ADR** projection), **split logical and physical ADRs**, **requirement and invariant nodes** in Architecture IR, and **path-level** linkage to a **real AWS Solutions** repository layout.

The YAML-shaped fragments in the steps are **illustrative** and **handbook-grade**. **ste-spec** is normative for **semantic** Architecture IR meaning; **adr-architecture-kit** (workspace sibling) is the reference for **ADR YAML field shapes** and **ID patterns**. **AWS documentation and the upstream GitHub repository** are authoritative for **Instance Scheduler product behavior**—the handbook **does not** vendor upstream code; it **synthesizes** STE-shaped artifacts for pedagogy.

## The Model

### What this section is for

- It follows **one or two systems** through STE end to end.
- The **goal** is the **full lifecycle**: intent → bounded decisions → architecture commitments → derived model → embodiment linkage → evidence → assessment → corrective feedback.
- The **AI Gateway** example is **intentionally small** but **structurally realistic** (patterns aligned with workspace example shapes, not toy prose).
- You should read **[AI Gateway step 1](./ai-gateway-example/01-requirements-snapshot.md) through [step 9](./ai-gateway-example/09-drift-and-correction.md) in order** first, using the companion diagrams as you go.

### Diagram A — Intent to design

See [Intent to design flow](./ai-gateway-example/diagrams/intent-to-design.md).

### Step map (reading order)

| Step | File | Lifecycle beat |
|------|------|----------------|
| 1 | [Requirements snapshot](./ai-gateway-example/01-requirements-snapshot.md) | Bounded expectations: capabilities, constraints, invariants, NFRs, technology signals |
| 2 | [Decision ledger](./ai-gateway-example/02-decision-ledger.md) | Explicit design questions and alternatives, tied to requirements |
| 3 | [Logical ADR](./ai-gateway-example/03-logical-adr.md) | Logical commitments that **resolve** the ledger (not ad hoc invention) |
| 4 | [Physical-system ADR](./ai-gateway-example/04-physical-system-adr.md) | Deployable topology, boundaries, trust, externals |
| 5 | [Physical-component ADR](./ai-gateway-example/05-physical-component-adr.md) | Implementable components, interfaces, deployment units |
| 6 | [Derived Architecture IR](./ai-gateway-example/06-derived-architecture-ir.md) | Compiled entities and relationships machines traverse |
| 7 | [Code semantic linkage](./ai-gateway-example/07-code-semantic-linkage.md) | Architecture linked to code and infrastructure |
| 8 | [EDR example](./ai-gateway-example/08-edr-example.md) | Embodied evidence, scoring, obligations |
| 9 | [Drift and correction](./ai-gateway-example/09-drift-and-correction.md) | Drift scenario and closing the self-correction loop |

### What Part 11 teaches (concept → where you learn it)

| Concept | Where you learn it |
|---------|-------------------|
| Intent vs design | Steps 1–2 |
| Decision governance (ledger bounds logical ADR) | Steps 2–3 |
| Logical vs physical | Step 3 vs Steps 4–5 |
| Canonical vs derived | ADRs (Steps 3–5) vs registry / graph (Step 6) |
| Architecture IR | Step 6 (derived model tooling may call it “registry”) |
| Embodiment | Step 7 |
| Evidence | Step 8 (EDR) |
| Governance | Step 8 (score, obligations, review) |
| Drift | Step 9 |
| Self-correction | Step 9 |

### Other diagrams

- [Canonical vs derived](./ai-gateway-example/diagrams/canonical-vs-derived.md) (Diagram B)
- [Design to embodiment](./ai-gateway-example/diagrams/design-to-embodiment.md) (Diagram C)
- [Feedback loop](./ai-gateway-example/diagrams/feedback-loop.md) (Diagram D)

### IR snapshot and IR-generated Mermaid

The **AI Gateway** example includes a consolidated [`architecture-ir.json`](./ai-gateway-example/ir/architecture-ir.json) and **regenerable** Mermaid under [`projections/generated/`](./ai-gateway-example/projections/generated/) (see [`projections/README.md`](./ai-gateway-example/projections/README.md)). Illustrative **projection-query** sketches live in [`projection-queries.md`](./ai-gateway-example/projections/projection-queries.md).

The **Instance Scheduler** example adds [`instance-scheduler-example/ir/architecture-ir.json`](./instance-scheduler-example/ir/architecture-ir.json) with **requirement** and **invariant** entities plus trace edges, and **three** generated views under [`instance-scheduler-example/projections/generated/`](./instance-scheduler-example/projections/generated/) (see [`instance-scheduler-example/projections/README.md`](./instance-scheduler-example/projections/README.md) and [`projection-queries.md`](./instance-scheduler-example/projections/projection-queries.md)).

### Second walkthrough — Instance Scheduler on AWS (higher fidelity)

Use this path after the AI Gateway steps when you want a **production-shaped** AWS **hub / spoke** story grounded in the public **[Instance Scheduler on AWS](https://github.com/aws-solutions/instance-scheduler-on-aws)** repository and **[implementation guide](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html)**.

**Diagram:** [Intent to design (Instance Scheduler)](./instance-scheduler-example/diagrams/intent-to-design.md)

| Step | File | Lifecycle beat |
|------|------|----------------|
| 0 | [Mock STE conversation](./instance-scheduler-example/00-ste-conversation.md) | Single-user chat: CE + **Architect agent** personas (FinOps, Security, AWS Cloud, Ops); rules project into ADRs in full STE → bounded REQ/INV ids |
| 1 | [Requirements snapshot](./instance-scheduler-example/01-requirements-snapshot.md) | Expectations tied to conversation + AWS references |
| 2 | [Decision ledger](./instance-scheduler-example/02-decision-ledger.md) | Questions spanning scheduling, persistence, multi-account |
| 3a–3b | [Logical ADR — scheduling](./instance-scheduler-example/03a-logical-adr-scheduling.md), [Logical ADR — trust](./instance-scheduler-example/03b-logical-adr-trust.md) | Split logical commitments |
| 4a–4b | [Physical-system — hub](./instance-scheduler-example/04a-physical-system-hub.md), [Physical-system — remote](./instance-scheduler-example/04b-physical-system-remote.md) | Hub vs spoke topology |
| 5a–5c | [Physical-component — orchestration](./instance-scheduler-example/05a-physical-component-orchestration.md), [data layer](./instance-scheduler-example/05b-physical-component-data-layer.md), [CLI](./instance-scheduler-example/05c-physical-component-cli.md) | Implementable units |
| 6 | [Derived Architecture IR](./instance-scheduler-example/06-derived-architecture-ir.md) | IR with requirements, invariants, trace edges |
| 7–9 | [Code linkage](./instance-scheduler-example/07-code-semantic-linkage.md), [EDR](./instance-scheduler-example/08-edr-example.md), [Drift](./instance-scheduler-example/09-drift-and-correction.md) | Embodiment, evidence, correction |

## The Implications

Treat this part as **pedagogy**, not a schema appendix: when a fragment disagrees with **ste-spec**, the specification wins. Use the same discipline in real programs: fix **canonical** intent or ADRs, then **regenerate** derived registries and graphs—do not “patch” derived files as if they were authority.

A **minimal reading path** that still conveys the whole STE shape is: **Part 0 (foundations)**, **Part 3 (intent artifacts)**, **Part 5 (lifecycle) together with runtime/evidence chapters you use as your “05” anchor**, and **this Part 11**. Earlier parts supply vocabulary and boundaries; **Part 11 is what makes the system concrete**: one thread from idea to drift and correction.

## Relationship to STE system

- **Closed loop and layers:** [System overview](../02-overview/02-03-system-overview.md)
- **Artifact types:** [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md)
- **Architecture IR and graph:** [IR as a graph](../04-architecture-model/04-07-ir-as-a-graph.md), [Projections overview](../04-architecture-model/04-08-projections-overview.md)
- **Narrow ladder/registry slice (complementary):** [Illustrative artifact walkthrough](../04-architecture-model/04-15-illustrative-walkthrough.md)
- **Lifecycle staging:** [Lifecycle overview](../05-lifecycle/05-00-lifecycle-overview.md)
- **Runtime evidence and freshness:** [Runtime evidence](../08-runtime/08-00-runtime-evidence.md)

**Begin the first walkthrough:** [AI Gateway — Step 1](./ai-gateway-example/01-requirements-snapshot.md). **Second walkthrough:** [Instance Scheduler — Step 0](./instance-scheduler-example/00-ste-conversation.md).

## Summary

- A **Requirements Snapshot** bounds expectations; a **Decision Ledger** states the design questions; a **Logical ADR** **resolves** those questions—it does not invent a separate decision list.
- **Physical-system** and **physical-component** ADRs refine logical commitments into topology and implementable responsibility.
- **Architecture IR** is the **derived**, machine-reasonable architecture model; registries and indices are **projections** of that model.
- **Semantic linkage** connects the model to **embodiment**; an **EDR** packages observable evidence for **assessment**, **scoring**, and **obligations**.
- Under pressure, **drift** shows up as broken linkage or violated invariants; STE’s loop makes that **visible** and drives **governed** correction back into **intent** and structure.
