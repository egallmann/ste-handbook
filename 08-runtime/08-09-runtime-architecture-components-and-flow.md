---
title: "Runtime Architecture Components and Flow"
status: structured
maturity: L2
diagrams: true
last_reviewed: "2026-03-30"
---

# Runtime Architecture Components and Flow

## The Problem

Teams implement observation piecemeal—one CI job, one graph export, one assistant plugin—without a logical architecture that shows how embodiment becomes **ArchitectureEvidence**, how readiness is classified, and how products reach the **Kernel**. The result is hidden coupling, duplicate classification logic, and handoffs that mix facts with verdicts.

## The Reframe

**Runtime** is an observation and readiness subsystem with named components. This chapter maps ingestion through emission for implementers, aligned with Embodiment → **Runtime** → Evidence → **Kernel** → Decision → Governance. ste-spec defines contracts; the handbook defines responsibilities and flow.

The **Runtime** role, responsibility table, and data product catalog are in [The Runtime Model](08-01-the-runtime-model.md); they are not repeated here.

## Why this matters

Implementability requires stable boundaries between components and consumers. Without that map, preflight, **MVC**, and **Kernel** integration become one-off integrations that drift from policy.

## The Model

### Logical components

| Component | Responsibility |
|-----------|----------------|
| Observation channels / ingestion | Collect structured observations from embodiment and toolchains (tests, telemetry, reconciliation, health probes—illustrative). |
| Evidence builder / normalization | Promote observations to **ArchitectureEvidence** with provenance, scope, and **Architecture IR** bindings ([Evidence and Observation](08-02-evidence-and-observation.md)). |
| Freshness and validity classifier | Assign evidence states and evaluate bundle validity ([Freshness and Validity](08-03-freshness-and-validity.md)). |
| Change detection | Detect events that require re-observation, invalidation, or reclassification; emit change and drift signals (observation-side, not policy decisions). |
| Projection / semantic graph builder | Rebuild and publish **derived** views from declared **Architecture IR** lineage ([Governance Signals and Semantic Graph Lifecycle](08-07-governance-signals-and-semantic-graph-lifecycle.md)). |
| Preflight gate | Run reasoning safety checks before **MVC** assembly ([Preflight and the Reasoning Gate](08-04-preflight-and-reasoning-gate.md)). |
| Context (**MVC**) builder | Assemble minimally viable context when preflight permits ([Context Assembly and Minimally Viable Context](08-05-context-assembly-and-mvc.md)). |
| Contract / data product emission | Publish typed outputs to **Kernel**, governance tooling, humans, and AI consumers per ste-spec ([Runtime–Kernel Contract](08-06-runtime-kernel-contract.md)). |

**Runtime** is not a decision or policy enforcement node: it emits products and governance signals; **Kernel** and governance own assessment and control.

### Main internal data flow

For a typical scoped operation:

Embodiment → Observation → **ArchitectureEvidence** → Classification → Preflight → **MVC** → **Kernel** handoff

- Embodiment feeds ingestion and channels.
- The evidence builder produces durable **ArchitectureEvidence**.
- The classifier and change detection label readiness and emit signals.
- The projection builder refreshes **derived** views when invalidation requires it.
- The preflight gate blocks unsafe assembly.
- The **MVC** builder packages context for consumers.
- Emission delivers products to **Kernel** and others without **Admission** verdicts.

```mermaid
flowchart LR
  Emb[Embodiment]
  Ing[Ingestion_channels]
  EvB[Evidence_builder]
  Cls[Classifier]
  Chg[Change_detection]
  Prj[Projection_builder]
  PF[Preflight_gate]
  MVCb[MVC_builder]
  Out[Emission_to_consumers]

  Emb --> Ing
  Ing --> EvB
  EvB --> Cls
  Chg --> Cls
  Chg --> Prj
  Cls --> PF
  Prj --> PF
  PF --> MVCb
  MVCb --> Out
```

### Consumers (downstream)

| Consumer | Typical inputs from **Runtime** |
|----------|--------------------------------|
| **Kernel** | **ArchitectureEvidence**, classifications, **MVC**, projection pointers, readiness metadata, plus **Architecture IR** from compilation |
| Governance | Governance signals (staleness, observation coverage gaps, invalidation), audit-friendly evidence pointers |
| Humans | **MVC**, projections, diagnostics from preflight |
| AI tools | **MVC** and labeled readiness metadata under the same gates as humans |

## The Implications

- Implement each component behind clear APIs so policy can move without rewriting pipelines end to end.
- Centralize classification and preflight ordering per policy version to preserve determinism claims.
- Test emission schemas against ste-spec fixtures before shipping **Kernel** integrations.

## Relationship to STE system

- [The Runtime Model](08-01-the-runtime-model.md), [Runtime Overview](08-00-runtime-overview.md)
- [Kernel and runtime](../07-kernel/07-08-kernel-and-runtime.md)
- [Architecture model (Architecture IR) overview](../04-architecture-model/04-00-architecture-ir-overview.md)

## Summary

- **Runtime** decomposes into ingestion, evidence building, classification, change detection, projection build, preflight, **MVC** assembly, and emission.
- Internal flow runs Embodiment → Observation → Evidence → Classification → Preflight → **MVC** → **Kernel** handoff, aligned with Embodiment → **Runtime** → Evidence → **Kernel** → Decision → Governance.
- ste-spec owns wire formats; **Runtime** owns observation and readiness products, not **Admission** or policy enforcement.

For Part 8 reading order return to [Runtime Overview](08-00-runtime-overview.md); for assessment mechanics outside this part, continue to [Kernel overview](../07-kernel/07-00-overview.md).

**Next:** [Runtime Overview](08-00-runtime-overview.md).
