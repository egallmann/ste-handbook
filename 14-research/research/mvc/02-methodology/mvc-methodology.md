---
title: "MVC Methodology"
status: draft
maturity: L1
diagrams: true
last_reviewed: "2026-06-09"
---

# MVC Methodology

## The Problem

The MVC thesis is not useful as research unless it can be tested without confusing evidence, authority, implementation detail, and interpretation. A methodology is needed because the thesis states the claim, but does not by itself define controls, baselines, reproducibility packages, HSCA treatment, evidence boundaries, threats to validity, or interpretation rules.

## The Reframe

The MVC methodology turns the representation ceiling thesis into a controlled research protocol. It tests whether structured architectural representation and structure-guided context assembly produce stronger measured signals than degraded, unstructured, or inference-guided context under named comparison metrics.

This methodology remains explanatory and experimental. It does not prove STE, MVC, RSS, any runtime implementation, production MVC-M, Kernel admission, or benchmark answer authority.

## The Model

### Research question

The central question is:

> Can structure-guided context assembly preserve more of the reasoning-relevant architectural world than inference-guided reconstruction over weaker representations?

The methodology tests representation and context assembly, not reasoner capability in isolation. A stronger reasoner may still perform poorly if the relationships, constraints, provenance, freshness, and authority boundaries required by the task are absent from the context it receives.

```mermaid
flowchart LR
  Theory[Representation_ceiling_theory]
  Equation[Candidate_equation]
  Config[Research_configuration]
  Study[Study_design]
  Evidence[Evidence_package]
  Finding[Bounded_finding]

  Theory -->|formalized_as| Equation
  Equation -->|tested_under| Config
  Config -->|instantiates| Study
  Study -->|generates| Evidence
  Evidence -->|supports_or_challenges| Finding
```

### Claim under test

The claim is not that more context is always better. The claim is that viable context is structurally sufficient for the question. A context packet, MVC-S candidate surface, or admitted MVC-M that includes many relevant artifacts can still be nonviable if it omits the relationship that explains why those artifacts matter.

For this methodology, context quality depends on:

- task-relevant entities,
- relationships among those entities,
- provenance and authority status,
- constraints and invariants,
- inclusion and exclusion rationale,
- negative space,
- source freshness and integrity,
- task and persona fit.

The candidate equation remains:

```text
Reasoning Quality =
  f(Reasoner Capability, Representation Quality, Context Assembly Quality)
```

### Operational definitions

**Representation** is the structured substrate available to context assembly. In STE terms, the richest target representation is Architecture IR and its derived graph or domain surfaces. In current MVC research, controlled candidate context artifacts approximate representation differences until production MVC-S and MVC-M pathways are mature enough to study directly.

**Representation quality** describes what the substrate preserves. **Assembly quality** describes whether the task-relevant portion of that representation is selected and presented. **Reasoning quality** describes what the reasoner or human participant does with the assembled context.

**MVC** is a task-scoped architectural reality bundle: the smallest faithful representation of the portion of modeled architectural reality required to answer a declared question. Viable means sufficient for the question, not merely small.

**RSS** is the structure-guided assembly process that identifies the candidate world view required for the task. Current research treats production RSS as future work unless explicitly named in a research configuration.

**Candidate context artifacts** are controlled experimental evidence inputs. They are not MVC-M, not Kernel-admitted, and not production MVC representations. They exist to test whether different context structures can be detected by the research instrument before production assembly is complete.

**HSCA** records human and AI observations to identify substrate gaps, assembly gaps, memory drift, representation gaps, authority gaps, and unresolved evidence. Details live in [HSCA methodology](hsca-methodology.md).

**Candidate equation variables** name observed, derived, and future measurements used to formalize the representation-ceiling claim. They are research notation, not STE contract fields. Details live in [MVC candidate equation variables](candidate-equation-variables.md).

**Context preflight** records the context assembled before evaluation: task intent, intended validation authority, required context classes, discovery strategy, known unknowns, exclusions, and stop or degrade criteria. Details live in [Context preflight methodology](context-preflight-methodology.md).

### Research unit

The research unit is not a response alone. It is:

```text
substrate_or_candidate_context
+ assembly_condition
+ evidence_generation_boundary
+ research_configuration
+ candidate_identity
+ task_or_scenario
+ scoring_or_observation_method
+ reasoner_or_participant_condition
```

This unit matters because a change in task bank, scoring method, reasoner profile, candidate context, or generation boundary changes the experimental condition.

### Variables and controls

Independent variables include representation condition, candidate context condition, assembly condition, reasoner/runtime condition, and human observation condition.

Dependent variables include local task discrimination, task-level variance, unsupported assertions, HSCA substrate completeness classifications, HSCA assembly completeness classifications, memory drift classifications, representation gap classifications, unresolved counts, and authority-gap counts.

Controlled variables include generation boundary, experiment fingerprint, task-bank identity, scoring identity, reasoner identity, temperature or sampling condition, prompt-template identity, candidate-context identity, task fingerprint, and participant blinding status.

For representation comparisons, controlled variables also include substrate identity, substrate affordances, admissible assembly configuration space, prohibited assembly mechanisms, assembly definition, assembly algorithm version, configuration identity, configuration fingerprint, fixed fields, varied fields, defaulted fields, configuration provenance, equivalence or non-equivalence class, and drift status.

### Evidence boundary

The methodology uses generation and fingerprint boundaries to prevent false comparison. Results from different generations are not comparable unless a later cross-generation study explicitly opts into that analysis.

This is methodology protection, not cleanup. Without the generation and fingerprint boundary, a score change could be caused by a reasoner change, task change, scoring change, candidate-context change, or prompt change while being incorrectly interpreted as an MVC effect.

### Authority boundaries

Research evidence includes reasoner responses, human observations, candidate context artifacts, HSCA disagreement records, evaluation reports, packet metrics, instrument health, and context health.

Authority remains with benchmark governance, adjudication protocols, accepted ADRs, invariants, contracts, canonical architecture artifacts, and Kernel admission where those surfaces exist.

Human memory cannot become architecture substrate without an explicit authority artifact. AI output cannot become answer authority without adjudication. Candidate context artifacts cannot become production MVC representations without an explicit promotion path through schema, runtime, and Kernel authority.

### Threats to validity

The methodology keeps these threats visible:

- same-designer bias,
- local reasoner confound,
- mechanical scoring limits,
- candidate-context artificiality,
- missing hosted or rubric authority,
- human memory contamination,
- synthetic fixture limits,
- overfitting of tasks to expected outcomes.

These threats do not invalidate the method. They bound what current evidence can support.

### Context assembly and configuration failure modes

The methodology treats context assembly as a possible source of failure, not merely a preparation step. Required context may exist in the workspace, research package, authority corpus, or operational evidence and still not be assembled into the study condition.

The study should therefore report:

- what context was required,
- what discovery entry points were used,
- what available context was not inspected,
- what was excluded and why,
- what effect exclusions have on conclusions,
- whether the study condition is viable, degraded, or invalid.

Configuration is similar. A study that does not preserve assembly definition, algorithm version, configuration identity, fixed and varied fields, defaults, equivalence, and drift cannot make strong causal claims about substrate quality.

### Interpretation rules

If candidate identities collapse to the same context condition, the configuration is invalid, not nondiscriminating.

If local scores are tied while candidate contexts differ and controls pass, the local instrument may be nondiscriminating for that task set. The next investigation target is task design, scoring sensitivity, or gold quality.

If human and AI observations disagree, the methodology classifies the disagreement instead of silently resolving it.

If a human answer contains knowledge absent from the substrate, the record may indicate human memory, external knowledge, substrate missingness, or authority gap. It does not automatically make the human answer authoritative.

If a candidate context artifact performs well, the result supports the experimental context condition. It does not prove production MVC-M or Kernel admission correctness.

## The Implications

- MVC methodology can publish enough protocol detail to be reviewable without publishing operational harness internals.
- Evidence boundaries must be explicit before results are interpreted.
- Local signals must be distinguished from general reasoner behavior.
- Candidate context artifacts must be distinguished from production MVC-S and MVC-M.
- Near-term progress means tightening the evidence chain: live blinded HSCA observations, hosted or rubric validation, packet-to-MVC-S fixture mapping, repeated stable discrimination, and governed evolution operators.
- Stronger evidence would show richer representations improving measured task performance under fixed reasoner conditions, or degraded representations failing on omitted structural relationships.

## Relationship to STE system

This methodology is connected to [MVC Representation Ceiling Thesis](../01-thesis/mvc-representation-ceiling-thesis.md), [MVC candidate equation variables](candidate-equation-variables.md), [Context preflight methodology](context-preflight-methodology.md), [HSCA methodology](hsca-methodology.md), [Benchmark methodology](benchmark-methodology.md), [Evolution methodology](evolution-methodology.md), [MVC experimental design](../03-experiment-design/mvc-experimental-design.md), and [MVC reproducibility model](../03-experiment-design/mvc-reproducibility-model.md).

Runtime candidate boundaries make future production experiments more plausible, but this methodology does not treat them as production RSS or MVC-M unless a research configuration explicitly brings those surfaces under test.

## Summary

- The methodology tests representation and context assembly, not STE as a whole.
- Candidate context artifacts are evidence inputs, not production MVC representations.
- Generation and fingerprint boundaries protect interpretation.
- Evidence does not become authority without separate governance.
- Current methodology supports controlled local research and HSCA; it does not claim scientific proof of the thesis.

Read next: the next chapter instantiates this method as a concrete study design.

**Next:** [MVC experimental design](../03-experiment-design/mvc-experimental-design.md).
