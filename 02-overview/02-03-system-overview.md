---
title: "System Overview"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-24"
---

# System Overview

## The Problem

You can know the words and still lack a picture. **Intent**, **Architecture IR**, **Kernel**, **projections**, and **evidence** each sound plausible alone. Without a composed story, readers guess edges: what feeds what, what is canonical, where humans decide, where automation assists, and where **governance** intervenes.

## The Reframe

STE is one system with multiple layers. Some layers record commitments. Some layers describe built reality. Some layers assess claims. Some layers publish views. The handbook presents them as cooperating parts of a loop, not as a bag of tools tied together by branding.

## The Model

### Major conceptual components

These are roles, not a repo checklist:

1. **Intent plane.** Humans and agents author and revise structured **intent** **artifacts** (including **ADRs** and **invariants**). Conversation interfaces and editing workflows live here at the human boundary.
2. **Compilation to Architecture IR.** Structured **intent** compiles into a canonical **Architecture IR**: the shared machine-addressable model used for inspection, diff, graph traversal, and downstream tooling.
3. **Projections.** **Projections** render **Architecture IR** and related material into diagrams, documents, and other human-facing views. Multiple projections should track the same underlying commitments when the system is healthy.
4. **Embodiment sources.** Repositories, builds, infrastructure definitions, and runtime systems realize **embodiment**. This is not a passive archive. It is what actually runs.
5. **Evidence collection.** Tests, telemetry, analysis outputs, and similar observations become **evidence** records (**EDR**s in handbook language) with provenance suitable for assessment.
6. **Assessment and admission.** The **Kernel** role consumes **evidence**, published contracts, and policy inputs to orchestrate deterministic assessment where that is honest and to surface structured outcomes for **governance** where judgment remains.
7. **Governance loop.** People and policy close the loop: approve or reject changes, update **intent**, grant bounded exceptions with owners, and schedule re-evaluation.

### Primary artifacts (what moves between boxes)

- **Intent artifacts:** decisions, invariants, constraints, capability maps, and related structured records.
- **Architecture IR:** canonical compiled architecture model.
- **Projections:** derived views for communication and review.
- **Evidence artifacts:** **EDR**-shaped records tying observations to **scopes** and systems under test.

### Flows you should be able to trace

**Flow A: commit and compile.** Author **intent** → compile → **Architecture IR** updates → **projections** refresh for review and teaching.

**Flow B: assess.** Build or change **embodiment** → produce **evidence** → **Kernel** assesses **conformance** claims under **rules** → outcomes feed **governance**.

**Flow C: govern change.** **Governance** revises **intent** or **embodiment** plans → loop returns to Flow A and Flow B.

### The same API example, structurally

A backward-compatibility **decision** lives in **intent** **artifacts**. Compilation reflects it in **Architecture IR** elements that interfaces and dependents relate to. CI and canary telemetry become **evidence**. Assessment asks whether **embodiment** matches the compatibility **intent** for the declared **scope**. If not, **governance** chooses between repair, revised **intent**, or a governed exception. None of that requires every team to use the same toolchain; it requires the responsibilities to exist.

### Humans and AI in the diagram

Humans remain accountable for **decisions**, **governance**, and judgment-shaped acceptance. Agents and automation help author structured **intent**, maintain **Architecture IR**, gather **evidence**, and execute mechanical checks. The boundary is not “human good, machine bad.” The boundary is which steps require explicit **governance** and which steps can be delegated safely when **intent** is machine-readable and **rules** are clear.

### Diagram companion

A companion Mermaid sketch lives at [`diagrams/system-overview.mmd`](../diagrams/system-overview.mmd). It may evolve independently; this chapter’s prose is the orientation authority if they diverge during drafting.

```mermaid
flowchart LR
  subgraph intentPlane ["Intent plane"]
    A["Intent artifacts"]
  end
  subgraph canonical ["Canonical model"]
    B["Architecture IR"]
  end
  subgraph views ["Projections"]
    C["Human-readable views"]
  end
  subgraph built ["Embodiment"]
    D["Running system"]
  end
  subgraph proof ["Evidence"]
    E["EDRs and tests"]
  end
  subgraph assess ["Assessment"]
    F["Kernel role"]
  end
  subgraph gov ["Governance"]
    G["Policy loop"]
  end
  A --> B
  B --> C
  B --> F
  D --> E
  E --> F
  F --> G
  G --> A
  G --> D
```

## The Implications

If you can sketch the loop, later chapters become “zoom into this region.” If you cannot, every new term feels like another attachment. The whiteboard test matters: boxes, labeled edges, and a path that returns to **governance** and revised **intent**.

## Relationship to STE system

Deeper treatment appears in the part overviews for intent, Architecture IR, kernel, control loop, projections, conversation, and lifecycle. Useful next anchors:

- [Intent layer overview](../03-intent/03-00-intent-layer-overview.md)
- [Architecture IR overview](../04-architecture-ir/04-00-architecture-ir-overview.md)
- [Kernel overview](../05-kernel/05-00-kernel-overview.md)
- [Control loop overview](../06-control-loop/06-00-control-loop-overview.md)
- [Projections overview](../07-projections/07-00-projections-overview.md)
- [Conversation engine overview](../08-conversation-engine/08-00-conversation-engine-overview.md)
- [Lifecycle and governance overview](../09-lifecycle-governance/09-00-lifecycle-overview.md)

Normative interfaces and behavior belong to **ste-spec** and the implementing repositories named in the handbook README, not to this sketch.

## Summary

- STE composes **intent** **artifacts**, **Architecture IR**, **projections**, **embodiment**, **evidence**, **Kernel**-shaped assessment, and **governance** into one loop.
- Three flows cover compile, assess, and govern; real work cycles among them.
- Humans own **governance** and judgment; automation expands where **intent** and **rules** are explicit.
- Later parts deepen each region; **ste-spec** defines exact contracts.
