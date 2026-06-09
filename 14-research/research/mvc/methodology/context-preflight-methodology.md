---
title: "Context Preflight Methodology"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Context Preflight Methodology

## The Problem

Required context can exist and still be absent from the reasoning context. A grounded answer can be wrong if it satisfies the sampled evidence while missing the intended validation target.

MVC research therefore needs a preflight step before methodology assessment, ablation design, or reasoning-quality evaluation.

## The Reframe

Context preflight is the research record of what the study attempted to assemble before drawing conclusions. It states the task, the consumer or persona, the intended validation authority, the required context classes, the discovery strategy, and the stop or degrade criteria.

Preflight is not authority. It is evidence about whether the study assembled enough context to make its own conclusions interpretable.

## The Model

A preflight record should declare:

- task intent,
- intended purpose,
- intended validation authority,
- intended outcome,
- current research configuration,
- context definition or assembly definition,
- discovery strategy,
- stop or degrade criteria,
- declared scope,
- consumer or persona,
- required output.

It should distinguish:

- existing artifact state,
- intended methodology purpose,
- intended validation target,
- current embodiment,
- planned but incomplete research surfaces,
- experimental observation purpose.

### Required Context Classes

For MVC methodology work, preflight should classify whether these context classes were assembled:

| Context Class | Purpose |
|---------------|---------|
| Authority artifacts | Identify contracts, ADRs, invariants, and accepted governance surfaces relevant to the claim. |
| Experimental contracts | Identify draft or experimental MVC, persona, context-domain, and graph-domain material used only as research substrate. |
| Operational workspace evidence | Identify the derived operational model used for observability, topology, source linkage, projection, validation, and attribution questions. |
| Manifest discovery evidence | Identify discovery entry points before sampling repository files or research artifacts. |
| Prior research planning | Identify pre-authority concepts and classify whether they are promoted, draft, implementation-backed, or still speculative. |
| Thesis alignment | Identify the originating claim, prediction, falsification condition, and objections being tested. |
| Benchmark and observation instrumentation | Identify the evidence boundary, candidate set, scoring or observation method, and instrument health without embedding operational records in handbook prose. |
| Known unknowns | Identify unresolved assumptions that may require stop, degrade, or explicit scoping. |

### Negative Space

Preflight should record available context that was not inspected, why it was excluded, and how the exclusion limits conclusions.

Examples of preflight negative space include:

- available authority artifacts not inspected,
- available operational evidence not assembled,
- manifests skipped before file sampling,
- attribution evidence omitted from blast-radius claims,
- intended validation target not assembled,
- known unknowns listed but not dispositioned,
- configuration identity or drift not captured,
- substrate affordances not declared,
- assembly definition or algorithm version not established.

### Viability Decision

Preflight should end with one of three decisions:

| Decision | Meaning |
|----------|---------|
| Viable | Required context was assembled for the declared task. |
| Degraded | Some context was missing or uninspected; conclusions must be scoped. |
| Invalid | Required context was available but not assembled, or unavailable without mitigation. |

## The Implications

- A study without context preflight may still produce evidence, but interpretation is weaker.
- Context preflight prevents guessed relevance from masquerading as viable context assembly.
- Missing context is a research signal, not merely a documentation gap.
- Preflight supports negative findings because it explains whether failure came from theory, instrument, assembly, or missing authority.

## Relationship to STE system

Context preflight is part of MVC research methodology. It connects to [MVC methodology](mvc-methodology.md), [MVC experimental design](../experiment-design/mvc-experimental-design.md), [Evidence and Reproducibility](../../../14-05-evidence-and-reproducibility.md), and [MVC open questions](../open-questions.md).

The operational workspace model may provide evidence for preflight, but generated graph state remains derived evidence and is not canonical architecture authority.

## Summary

- Context preflight makes context assembly explicit before evaluation.
- It records inspected context, excluded context, and negative space.
- It declares whether the study condition is viable, degraded, or invalid.
- It is evidence about research quality, not STE authority.
