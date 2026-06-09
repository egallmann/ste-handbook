---
title: "Evolution Methodology"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Evolution Methodology

## The Problem

Evolution research can optimize candidates without making those candidates authoritative. If search pressure, candidate promotion, and fitness signals are not separated, a successful search artifact can be mistaken for accepted STE semantics.

## The Reframe

MVC evolution methodology studies how candidate context definitions or policies may improve under controlled selection pressure. It treats candidate generation, screening, promotion, and full evaluation as research activities.

## The Model

The current public methodology distinguishes a candidate search scaffold from a full evolutionary system.

A candidate search scaffold may include:

- a fixed candidate population,
- candidate-to-context mappings,
- a cheap screening signal,
- top-k promotion by the screening signal,
- a fuller evaluation pass over promoted candidates,
- generation-scoped continuation state,
- reports for later comparison.

The cheap screening signal, `F_sim`, is not a reasoning-quality score. It is a pre-screening signal that decides which fixed candidates enter fuller evaluation.

The fuller evaluation signal, `F_full`, is still experimental evidence. It remains constrained by the reasoner condition, benchmark design, scoring method, and research configuration.

A future full evolution method may add mutation, recombination, population replacement, convergence criteria, candidate generation, and governed fitness weighting. Those features must not be inferred from a scaffold unless the research configuration explicitly includes them.

### Candidate Search Space

MVC evolution treats candidate search dimensions as research variables. The dimensions are classified before use:

| Class | Meaning |
|-------|---------|
| Observed experimental dimensions | Present in the research substrate or evidence package and available for controlled variation. |
| Derived dimensions | Computed from observed dimensions under a declared method. |
| Inferred policy dimensions | Plausible search policies that require executable policy authority before they can be treated as governed behavior. |

Observed dimensions include:

- context-domain inclusion and exclusion,
- context-domain selector set,
- operational repo or slice selection,
- graph-domain and graph-type inclusion,
- source locator preservation,
- attribution and embodiment preservation,
- ADR-to-implementation and invariant-to-implementation inclusion,
- attribution confidence filtering,
- blast-radius traversal mode,
- substrate identity,
- substrate affordance set,
- admissible assembly configuration space,
- prohibited assembly mechanisms,
- assembly configuration identity, version, and fingerprint,
- fixed, varied, and defaulted configuration fields,
- configuration provenance, equivalence, non-equivalence, and drift status,
- evidence boundary and experiment fingerprint,
- candidate context artifact identity, scope, hash, metrics, and mapping,
- manifest inclusion and filtering,
- assembly definition identity,
- assembly algorithm identity and version,
- projection level and projection family,
- persona set, required domains, optional domains, and domain weights,
- traversal, projection, and admission policy references,
- candidate entity, relationship, evidence, and constraint inclusion.

Derived dimensions include:

- relationship-family preservation ratio,
- evidence-to-component coverage,
- decision-to-capability coverage,
- invariant-to-component coverage,
- negative-space preservation threshold,
- source locator coverage threshold,
- attribution and embodiment coverage thresholds,
- blast-radius expansion threshold,
- projection compression level,
- topology budget profile,
- manifest freshness and integrity thresholds,
- assembly reproducibility threshold,
- configuration drift and equivalence thresholds,
- configuration fingerprint preservation threshold.

Inferred policy dimensions include:

- traversal ranking strategy,
- projection ranking strategy,
- compression strategy,
- context ordering strategy,
- relationship weighting strategy,
- assembly algorithm selection when a definition admits more than one valid algorithm,
- substrate-specific assembly configuration discovery,
- cross-substrate configuration fairness,
- configuration equivalence mapping,
- configuration drift attribution.

Inferred policy dimensions should remain research questions until a governing artifact or executable policy version exists.

### Assembly and Configuration Rules

Evolution methodology treats assembly as definition-specific. Each assembly definition should name its input surfaces, output surface, validation or admission expectations, algorithm identity, algorithm version, and partial-state behavior.

Assembly is also representation-specific. A full graph-shaped architecture representation, an ADR-style decision corpus, and a legacy document corpus do not admit the same assembly mechanisms. The comparison is fair only when each substrate is searched within its own admissible assembly space under the same tasks, personas, known outcomes, and evaluation protocol.

Configuration is a first-order experimental control. Each run should preserve configuration identity, version, fingerprint, fixed fields, varied fields, defaulted fields, provenance, equivalence or non-equivalence class, and drift status. If these are not known, the study may be measuring uncontrolled configuration drift rather than representation quality.

## The Implications

- Candidate promotion is not authority promotion.
- Evolved candidates remain research artifacts until separately reviewed.
- Search behavior cannot be claimed from a fixed-population scaffold.
- Fitness signals must identify what they measure and what they do not.
- Negative and inconclusive evolution outcomes must be retained.
- Search dimensions should be classified before being used as genes.
- Substrate effects and configuration effects should be separated where the study design permits.

## Relationship to STE system

Evolution methodology connects to [MVC methodology](mvc-methodology.md), [MVC candidate equation variables](candidate-equation-variables.md), [Benchmark methodology](benchmark-methodology.md), and [MVC reproducibility model](../experiment-design/mvc-reproducibility-model.md). It does not define production MVC-D, MVC-S, MVC-M, or Kernel admission.

## Summary

- Evolution research studies candidate improvement under controlled selection pressure.
- `F_sim` is a screening signal, not reasoning quality.
- `F_full` is evidence, not authority.
- Full evolutionary claims require a research configuration that actually includes evolution operators.
