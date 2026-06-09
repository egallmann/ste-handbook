---
title: "MVC Experimental Design"
status: draft
maturity: L1
diagrams: true
last_reviewed: "2026-06-09"
---

# MVC Experimental Design

## The Problem

The MVC thesis and methodology need concrete study designs so readers can see how the research program tests representation and context assembly without treating results as doctrine.

## The Reframe

An MVC experiment is one instantiation of the research program under a declared research configuration. It tests a bounded claim and produces evidence for a published finding, negative finding, inconclusive finding, or superseded finding.

## The Model

```mermaid
flowchart LR
  Thesis[Thesis]
  Method[Methodology]
  Config[Research_configuration]
  Study[Study_design]
  Evidence[Evidence_package]
  Finding[Finding]

  Thesis --> Method
  Method --> Config
  Config --> Study
  Study --> Evidence
  Evidence --> Finding
```

### Research unit

The research unit combines:

- substrate or candidate context condition,
- assembly condition,
- generation and fingerprint boundary,
- candidate identity,
- task or scenario,
- scoring or observation method,
- reasoner or participant condition.

### Protocol stages

The public protocol stages are:

| Stage | Purpose |
|-------|---------|
| Context preflight | Declare the task, intended validation authority, required context classes, discovery strategy, and stop or degrade criteria before sampling evidence. |
| Instrument readiness | Confirm the instrument can run and validate its research configuration before aggregation. |
| Candidate separation | Confirm candidate contexts are distinct and not accidental duplicates. |
| Task controls | Calibrate positive controls, negative controls, and expected signal. |
| Packet-backed context | Use versioned candidate context artifacts with explicit identity, scope, health, and metrics. |
| HSCA completeness | Classify substrate, assembly, memory, representation, and authority gaps. |
| Blinded live collection | Gather human observations without pre-exposure to answers, scores, gold answers, or disagreement classifications. |

### Controls and baselines

The design should control generation boundary, experiment fingerprint, reasoner condition, prompt-template identity, task-bank identity, scoring identity, candidate-context identity, and participant blinding status.

When representation substrates are compared, the design should also control or explicitly classify substrate affordances, admissible assembly configuration space, prohibited assembly mechanisms, assembly definition, assembly algorithm version, configuration identity, fixed fields, varied fields, defaults, equivalence or non-equivalence, and drift status.

Baselines should include degraded or weaker context conditions where the research question depends on detecting representation effects. Positive and negative controls should make nondiscrimination interpretable.

### Expected outcomes

The design should distinguish:

- invalid candidate configuration,
- insufficient evidence,
- local discrimination,
- local nondiscrimination,
- substrate incompleteness,
- assembly incompleteness,
- authority gaps,
- unresolved observations.

These are research outcomes. They are not production verdicts.

## The Implications

- A positive MVC result supports only the tested condition.
- A negative MVC result must distinguish weak theory, weak instrument, weak task bank, weak scoring, and weak representation construction.
- HSCA should classify substrate and assembly gaps before results are interpreted as reasoner success or failure.
- The design should not claim production RSS, MVC-M, Kernel admission, or STE proof unless those surfaces are actually under test.
- Historical generations may remain discoverable while default comparison is scoped to the active research configuration.
- A missing preflight record weakens interpretation because the study may not have assembled the intended validation target.

## Relationship to STE system

The design is connected to [MVC methodology](../02-methodology/mvc-methodology.md), [Context preflight methodology](../02-methodology/context-preflight-methodology.md), [Benchmark methodology](../02-methodology/benchmark-methodology.md), [HSCA methodology](../02-methodology/hsca-methodology.md), and [Evidence and Reproducibility](../../../14-05-evidence-and-reproducibility.md).

## Summary

- MVC experiments instantiate thesis and methodology under a research configuration.
- The study tests representation and context assembly, not STE as a whole.
- Protocol stages make readiness, candidate separation, controls, context health, and HSCA visible.
- Interpretation must stay bounded by protocol, controls, and evidence.
