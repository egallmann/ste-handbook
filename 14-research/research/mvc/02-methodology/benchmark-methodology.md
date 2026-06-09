---
title: "Benchmark Methodology"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Benchmark Methodology

## The Problem

Benchmarks can produce persuasive numbers while hiding contamination, scoring weakness, nondiscriminating tasks, or authority gaps. MVC research needs benchmark methodology that states what the benchmark can and cannot support.

## The Reframe

The MVC benchmark methodology treats benchmark outputs as research evidence. Benchmark scores do not become answer authority, production claims, or STE validation by themselves.

## The Model

### Benchmark purpose

The benchmark asks whether candidate context conditions produce measurably different outcomes on tasks designed to require different context features. It is a discrimination instrument before it is a correctness oracle.

### Task controls

Task controls should distinguish:

- positive-control tasks expected to favor a named candidate condition,
- negative-control tasks expected to tie or remain within a variance threshold,
- baseline correctness signals,
- candidate-sensitive signals,
- missing-context signals,
- unsupported-assertion signals.

If distinct candidate conditions produce no measurable difference while instrument health passes, the result may indicate weak task design, weak gold quality, or weak scoring sensitivity rather than a failure of the representation ceiling thesis.

### Local discrimination

Local discrimination asks whether candidate context conditions produce measurably different scores under a fixed reasoner condition. Local discrimination is evidence of instrument sensitivity. It does not establish hosted equivalence or general reasoner behavior.

### Packet health

Candidate context health checks whether candidate artifacts are present, mapped correctly, identity-stable, distinct, and aligned with expected concepts. Packet metrics may be reported for later analysis of context quality versus context size, but metrics should not silently change candidate identity.

### Scoring limits

Mechanical scoring can detect expected concepts and unsupported assertions, but it cannot fully evaluate answer correctness, source fidelity, or hallucination. Rubric authority and adjudication remain future or separate governance surfaces unless explicitly included in the research configuration.

## The Implications

- Benchmark evidence must be interpreted under its research configuration.
- A benchmark improvement does not imply general capability improvement.
- A nondiscriminating benchmark may be a weak instrument.
- Benchmark contamination and reasoner familiarity must remain visible validity threats.
- Benchmark outputs do not define production MVC behavior.

## Relationship to STE system

Benchmark methodology supports [MVC methodology](mvc-methodology.md), [MVC experimental design](../03-experiment-design/mvc-experimental-design.md), and [Measurement and Validity](../../../14-06-measurement-and-validity.md). Benchmark governance remains separate from research evidence.

## Summary

- MVC benchmark outputs are research evidence.
- Task controls make discrimination interpretable.
- Local discrimination is not general reasoner validation.
- Scoring limits must be visible before findings are published.
