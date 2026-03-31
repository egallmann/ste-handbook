---
title: "The Runtime Model"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-30"
---

# The Runtime Model

## The Problem

Architecture discussions mix four different authorities—ADRs, **Architecture IR**, evidence, and projections—into one mental bucket labeled “the model.” When that happens, observation is mistaken for decision, **derived** files for **canonical** intent, and tooling for governance. No layer is left responsible for legible inputs to assessment, so the control loop degrades into informal opinion.

## The Reframe

**Runtime** is a named system role in STE. It sits between embodiment (actual systems) and **Kernel** (deterministic assessment and **Admission**), alongside compilation (intent → **Architecture IR**). Its mandate is observation, **ArchitectureEvidence**, surfacing freshness and validity, preflight, and context assembly—so compare and decide operate on legible state.

## Why this matters

If **Runtime** is unnamed, teams reinvent partial solutions: ad hoc logs, unscoped tests, stale graph caches, and prompts that assume current structure. Naming the model lets you review pipelines the same way you review ADRs and invariants: as parts of one control system.

## The Model

### Runtime in the feedback loop (observe → compare → decide → act)

| Loop phase | STE assignment (handbook level) |
|------------|----------------------------------|
| Observe | **Runtime** collects observations and packages evidence; tracks projection freshness and validity prerequisites. |
| Compare | **Kernel** evaluates **Architecture IR** against evidence and rules—not informal narrative. |
| Decide | **Kernel** emits machine-readable outcomes (**Admission** where defined); governance records policy decisions and exceptions. |
| Act | Delivery changes embodiment; intent and **Architecture IR** change through governed artifact workflows. |

**Runtime** makes the observe phase accountable; it does not substitute for compare or decide.

### Canonical vs derived vs observed (Runtime’s lens)

- **Canonical** intent (ADRs, invariants, requirements): **Runtime** does not author or supersede.
- **Architecture IR**: compiled from intent; **Runtime** binds **ArchitectureEvidence** to identities and traverses **Architecture IR** for context; **Runtime** does not replace compilation.
- **Observed** (evidence): what embodiment did under scope; **Runtime** structures and provenances it.
- **Derived** (projections, graph exports): **Runtime** enforces freshness and invalidation discipline so they are not mistaken for **canonical** records.

### Responsibilities (Runtime)

| Responsibility | Outcome |
|----------------|---------|
| Observation | Structured facts about embodiment and pipelines ([Evidence and Observation](08-02-evidence-and-observation.md)). |
| Evidence | EDR-shaped **ArchitectureEvidence**, addressable to **Architecture IR** and trace where policy requires. |
| Freshness and validity | Classification and bundle validity ([Freshness and Validity](08-03-freshness-and-validity.md)). |
| Preflight | Readiness gate before high-stakes reasoning ([Preflight and the Reasoning Gate](08-04-preflight-and-reasoning-gate.md)). |
| Context assembly | **MVC** bundles ([Context Assembly and Minimally Viable Context](08-05-context-assembly-and-mvc.md)). |

### Runtime data products (outputs)

**Runtime** emits typed outputs consumed by **Kernel**, governance tooling, humans, and AI tools. Exact envelopes are ste-spec; the handbook names roles.

| Data product | Handbook role | Typical consumers |
|--------------|-----------------|---------------------|
| **ArchitectureEvidence** | Observed facts about embodiment, **Architecture IR**-addressable; non-decision-bearing | **Kernel**, governance audit, humans, AI tools |
| Freshness and validity classification | Whether evidence and bundles are usable together for an operation | **Kernel**, preflight, **MVC** path, humans, AI tools |
| Change and drift signals | Observation-side invalidation and reconciliation hints—not policy decisions | **Kernel**, governance, humans, AI tools |
| Preflight and readiness results | Outcome of the reasoning safety gate | **MVC** path, humans, AI tools; **Kernel** via handoff |
| **MVC** bundles | Minimal **Architecture IR** slice, projection and evidence pointers, readiness metadata | **Kernel**, humans, AI tools |
| Projection and semantic graph updates | **Derived** views with lineage—not **canonical** **Architecture IR** | Humans, AI tools, **Kernel** as inputs, governance process |
| Runtime health and observation coverage | Pipeline health and whether scopes are observed | Preflight, **MVC** path, humans, governance, **Kernel** when bundled |

Components and internal flow from embodiment to emission: [Runtime Architecture Components and Flow](08-09-runtime-architecture-components-and-flow.md). Authority summary: [Runtime Overview](08-00-runtime-overview.md).

### What Runtime does not do

- Emit **Kernel** verdicts or **Admission** assessments ([Runtime–Kernel Contract](08-06-runtime-kernel-contract.md)).
- Act as compiler of record for **Architecture IR** ([Compilation](../04-architecture-model/04-04-compilation.md)).
- Replace governance policy or human accountability for intent.

### Consumers: humans and AI

Deterministic services and stochastic assistants consume **Runtime** outputs. Neither should be fed structural state that is stale or invalid under policy; **Runtime** supplies metadata and gates so violations are fail-visible where policy demands.

```mermaid
flowchart TB
  subgraph desired [Desired_state]
    ADR[Intent_artifacts]
    IR[Architecture_IR]
  end
  subgraph actual [Actual_state]
    Emb[Embodiment]
  end
  subgraph rt [Runtime_role]
    Obs[Observations]
    Ev[Evidence]
    Fresh[Freshness_validity]
    PF[Preflight]
    Ctx[MVC_context]
  end
  Kern[Kernel_assessment]
  ADR --> IR
  Emb --> Obs
  Obs --> Ev
  IR --> Fresh
  Ev --> Fresh
  Fresh --> PF
  IR --> PF
  PF --> Ctx
  Ev --> Kern
  IR --> Kern
  Ctx --> Kern
```

## The Implications

- Draw **Runtime** on architecture diagrams as a first-class block.
- Tie review criteria to evidence channels, freshness policy, and preflight—not only ADRs.
- Treat blur between **Runtime** and **Kernel** as an architecture smell.

## Relationship to STE system

- [Kernel overview](../07-kernel/07-00-overview.md), [Kernel and runtime](../07-kernel/07-08-kernel-and-runtime.md)
- [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md)
- [Artifact layer overview](../03-artifacts/03-00-artifact-layer-overview.md)
- [Runtime Architecture Components and Flow](08-09-runtime-architecture-components-and-flow.md)

## Summary

- **Runtime** is the observation-and-readiness layer: **ArchitectureEvidence**, classification, preflight, **MVC**, and the data products above.
- It enables **Kernel** determinism with typed, scoped inputs; it does not decide **Admission** or enforce governance policy.
- **Canonical**, compiled, **observed**, and **derived** stay distinct; **Runtime** guards the last two against silent drift.

The next chapter narrows to observation channels and how they become **ArchitectureEvidence**—before classification and gates.

**Next:** [Evidence and Observation](08-02-evidence-and-observation.md).
