---
title: "Research Methodology"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Research Methodology

## The Problem

Research methods can be confused with operational tooling. A benchmark harness, a local model run, or a human review workflow may support research, but none of them is the research method by itself.

Without a methodology layer, results can become tied to incidental tools instead of the claim under test.

## The Reframe

Research methodology defines how STE tests claims. Experiments are one activity inside methodology. Other activities include substrate completeness analysis, frozen research configurations, benchmark governance, adjudication, reproductions, and open-question review.

## The Model

An STE methodology should state:

- The research question and candidate theory.
- The candidate equation or mechanism under test.
- The study class and method.
- The research configuration.
- Controls and baselines.
- Evidence generation process.
- Measurement and validity strategy.
- Interpretation and publication boundary.

Experiments remain important, but they do not exhaust research. A methodology may include observational studies, HSCA, design reviews, benchmark audits, reproduction studies, or comparative analyses.

The method-to-evidence path is:

```mermaid
flowchart LR
  Claim[Claim]
  Method[Methodology]
  Design[Experiment_Design]
  Evidence[Evidence]
  Finding[Finding]
  Reproduction[Reproduction]

  Claim --> Method
  Method --> Design
  Design --> Evidence
  Evidence --> Finding
  Finding --> Reproduction
```

## The Implications

- Methodology belongs in the handbook research record.
- Operational harness behavior belongs in its owning repository or reproducibility package.
- Frozen experiment states should be represented by research configurations, not by prose snapshots.
- Methodology must state what it does not establish.
- Methodology revisions should preserve publication lineage.

## Relationship to STE system

Research methodology connects handbook research to operational repositories without moving authority. `ste-runtime` may operationalize a harness; `ste-spec` may define contracts; `adr-architecture-kit` may produce substrate. The handbook explains the method and publication boundary.

## Summary

- Methodology is the research design, not the tool.
- Experiments are one research activity among several.
- Methodology should be versioned and tied to research configurations.
- Operational implementation remains outside handbook prose.

Read next: [Evidence and Reproducibility](14-05-evidence-and-reproducibility.md) explains how study conditions are preserved for review.
