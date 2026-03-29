---
title: "Part 5: Implementation and Operation"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Implementation and operation

This stage is where **embodiment** exists: repositories, builds, infrastructure, configuration, releases, and live behavior. In STE vocabulary, **implementation** names code-level and adjacent realization; **embodiment** is the broader running and configured whole that **evidence** observes.

## Purpose of this stage

Turn declared structure and **intent** into a system that actually runs, scales, fails, and changes in production or equivalent environments, while remaining connectable back to **Architecture IR** and **trace** expectations.

## Artifacts involved

**Implementation** artifacts: source code, infrastructure definitions, configuration, deployment manifests, and operational runbooks where they are treated as durable records. Bindings from these artifacts to **scopes** and IR elements matter for later **evidence** and **conformance**. See [Architecture model and IR](../03-artifacts/03-04-architecture-model-and-ir.md) and [Evidence](../03-artifacts/03-05-evidence.md).

## Human responsibility

Engineering and operations teams implement features and fixes, own service health and change risk, decide local tactics inside **constraints**, and escalate when **intent** and reality conflict. Humans remain accountable for what ships and how it is operated.

## STE system responsibility

STE records or ingests references to **implementation** artifacts, maintains links between **embodiment** **scopes** and the canonical model where policy requires, supports automated collection hooks for observations, and surfaces **drift** signals when configured expectations and recorded reality diverge.

## Transitions to the next stage

The loop moves toward **evidence and observation** when the system (or a defined **scope** of it) is observable: tests can run, telemetry can flow, or audits can inspect behavior. Observation is often continuous. Return to this stage from **governance** decisions that authorize remediation or feature work.

**Next stage chapter:** [Evidence and observation](05-04-evidence-and-observation.md).

## Relationship to intent, implementation, and evidence

- **Intent:** **Embodiment** should realize **intent** and the structural commitments in **Architecture IR**; tension here is the subject of later **conformance**.
- **Implementation:** This stage is where **implementation** artifacts and operational practice live.
- **Evidence:** Observable **embodiment** is the input to **evidence** production in the next stage.

## Relationship to other chapters

- [Intent versus implementation](../00-problem/00-03-intent-vs-implementation.md)
- [Implementation to evidence](../06-governance/06-10-implementation-to-evidence.md)
- [Kernel overview](../07-kernel/07-00-overview.md) (admission and runtime perspective)
- **ste-spec** for binding and observation interfaces where defined.

**Next:** [Evidence and observation](05-04-evidence-and-observation.md).
