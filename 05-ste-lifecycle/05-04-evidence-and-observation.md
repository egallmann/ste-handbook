---
title: "Part 5: Evidence and Observation"
status: structured
maturity: L1
diagrams: false
last_reviewed: "2026-03-25"
---

# Evidence and observation

**Evidence** is structured observation of **embodiment**: what ran, what failed, what was measured, and under which conditions. STE treats **evidence** as a durable artifact class with provenance, not as anecdote or screenshots without anchors.

## Purpose of this stage

Make reality legible for **validation**: tie observations to **scopes**, time ranges, and the **intent** and IR claims they are meant to support or refute.

## Artifacts involved

Tests, continuous integration results, telemetry, logs, experiment outputs, audit artifacts, and **EDR**-shaped records. **Traceability** links connect **evidence** to requirements, **invariants**, and model elements where policy demands it. See [Evidence](../03-artifact-layer/03-05-evidence.md) and [Traceability](../03-artifact-layer/03-06-traceability.md).

## Human responsibility

Humans define what counts as sufficient **evidence** for a decision in policy, design meaningful checks, interpret ambiguous signals, and refuse to certify on thin proof when stakes require it. They also correct misconfigured pipelines that produce misleading **evidence**.

## STE system responsibility

STE collects or accepts observation streams, normalizes them into structured **evidence** records, attaches provenance (source, revision, environment), indexes them for retrieval alongside **intent** and IR, and protects **evidence** from casual rewriting without **governance**.

## Transitions to the next stage

Assessment begins when **evidence** exists for a declared **scope** and rule set, even if partial. The next chapter treats **conformance** and **assessment** explicitly. Return to this stage after any material **change** to **embodiment** or to the observation fabric itself.

**Next stage chapter:** [Conformance and assessment](05-05-conformance-and-assessment.md).

## Relationship to intent, implementation, and evidence

- **Intent:** **Evidence** answers whether **embodiment** matches declared **intent** for a **scope**; without **intent**, **evidence** is only telemetry.
- **Implementation:** What is built and how it runs determines which observations are possible; gaps in observability are an **engineering** risk, not only a metrics problem.
- **Evidence:** This stage produces and curates **evidence** as the bridge from **embodiment** to judgment.

## Relationship to other chapters

- [Conformance](../03-artifact-layer/03-07-conformance.md)
- [Evidence to assessment](../07-control-loop/07-04-evidence-to-assessment.md)
- [Runtime evidence](../06-kernel/06-06-runtime-evidence.md)
- **ste-spec** for **EDR** and evidence contracts.

**Next:** [Conformance and assessment](05-05-conformance-and-assessment.md).
