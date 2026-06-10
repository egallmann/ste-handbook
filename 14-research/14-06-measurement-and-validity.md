---
title: "Measurement and Validity"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Measurement and Validity

## The Problem

Measurements compress judgment into numbers or classifications. But a number can measure the wrong thing, a benchmark can reward surface cues, and a result can generalize less than the write-up implies.

## The Reframe

STE research treats validity threats as part of the method, not as fine print. A study is stronger when its limits are visible.

## The Model

Validity should be assessed in at least four dimensions:

| Validity type | Question |
|---------------|----------|
| Internal validity | Did the study isolate the claimed cause? |
| External validity | Can the finding generalize beyond the study boundary? |
| Construct validity | Did the instrument measure the concept it claims to measure? |
| Statistical validity | Are comparisons, sample sizes, and uncertainty handled honestly? |

### Apparatus and Instrument Validity

Apparatus validity asks whether the research machinery works as declared: schemas validate the intended records, fixtures exercise expected paths, hashes and fingerprints preserve identity, reports aggregate correctly, validators catch malformed states, and reproducibility plumbing can recreate the study condition.

Instrument validity asks whether the measurement instrument behaves against known inputs before it is used for broader claims. A benchmark, scorer, HSCA mechanism, or calibration run may show local discrimination or calibration while still lacking authority over the scientific construct.

"Mechanism works" does not mean the underlying scientific construct has been validated. Apparatus and instrument checks make later evidence more inspectable; they do not by themselves validate representation quality, reasoning quality, benchmark authority, or any future construct variable.

Common STE research threats include:

- Benchmark contamination.
- Model familiarity with task patterns.
- Evaluator bias.
- Selection bias in tasks, candidates, systems, or participants.
- Substrate bias from architecture material authored for the theory.
- Mechanical scoring limits.
- Human memory contamination.
- Local model or hosted model confounds.
- Overfitting of candidate representations to expected outcomes.

### Self-Reference and Instrumentation Bias

STE research can use STE infrastructure to study STE claims. That self-reference is useful because it makes the research substrate explicit, but it also creates methodological risks:

| Risk | Concern |
|------|---------|
| Same-designer bias | The people designing the theory may also design the tasks, substrate, or interpretation. |
| Instrumentation bias | The tools may measure what STE makes easy to observe rather than what the hypothesis requires. |
| Substrate bias | Architecture material authored for STE may favor STE-native representations. |
| Dogfooding bias | Using the system to study itself can hide assumptions that an external reproducer would notice. |
| Experimenter effects | Study design, task selection, or interpretation can drift toward expected outcomes. |

These are methodological concerns, not reasons to discard the research. Part 14 mitigates them by requiring publication, reproducibility packages, validity analysis, falsification-oriented designs, open questions, explicit authority separation, and promotion boundaries.

## The Implications

- Benchmark improvement does not automatically mean general capability improvement.
- A local model signal does not automatically generalize to hosted models.
- A human disagreement does not automatically mean the benchmark is wrong.
- A nondiscriminating benchmark may be a weak instrument rather than a negative result about the theory.
- Threats should be connected to interpretation rules before publication.

## Relationship to STE system

Validity language is part of evidence quality. It supports [Determinism, Provenance, and Audit](../06-governance/06-06-determinism-provenance-and-audit.md) by making uncertainty reviewable rather than implicit.

## Summary

- Measurement is not authority.
- Validity threats are part of the evidence record.
- Internal, external, construct, and statistical validity must be separated.
- Strong interpretation requires visible limits.

Read next: [Interpretation and Promotion](14-07-interpretation-and-promotion.md) explains how findings remain narrower than the evidence that supports them.
