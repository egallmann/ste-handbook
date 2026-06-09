---
title: "MVC Reproducibility Model"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# MVC Reproducibility Model

## The Problem

Reproduction depends on knowing which research condition is being reproduced. Without configuration identity, reruns and reproductions cannot be compared safely.

## The Reframe

MVC reproducibility is organized around research configurations. A research configuration identifies the study condition, evidence boundary, and publication version under evaluation.

## The Model

Research configuration fields:

```yaml
research_program: mvc
methodology_version:
benchmark_version:
candidate_version:
repository_commits:
reasoner_condition:
experiment_generation:
experiment_fingerprint:
assembly_definition:
assembly_algorithm_version:
assembly_configuration_id:
assembly_configuration_fingerprint:
fixed_configuration_fields:
varied_configuration_fields:
configuration_equivalence:
configuration_drift_status:
```

An MVC reproducibility package should identify:

- research question,
- hypothesis,
- methodology version,
- benchmark or task-bank version,
- candidate version,
- reasoner or participant condition,
- generation and fingerprint boundary,
- scoring or observation method,
- HSCA evidence class when used,
- evidence package identity,
- finding or publication version under test.

Configuration-control fields are required because assembly configuration is part of the research condition. A reproduction cannot safely compare two runs if it does not know which assembly definition, algorithm version, fixed fields, varied fields, defaults, equivalence class, and drift status were in effect.

Before interpreting a result, reviewers should confirm:

- the research configuration is declared,
- the generation boundary matches the evidence under analysis,
- candidate context identities are distinct when discrimination is claimed,
- instrument health and context health are acceptable,
- HSCA claims distinguish synthetic mechanics checks from live observations,
- substrate affordances and admissible assembly space are declared where substrate comparison is claimed,
- configuration identity, fingerprint, and drift status are declared,
- generated outputs remain evidence, not canonical authority.

## The Implications

- A score without a research configuration is weak evidence.
- A task-bank change creates a new comparison boundary.
- A reasoner or scoring change creates a new research configuration.
- An assembly definition, assembly algorithm, or configuration change creates a new research configuration unless the study declares and justifies equivalence.
- Reproductions should cite both the finding and the research configuration.
- Executable assets and raw outputs remain in the owning repositories or package locations.

## Relationship to STE system

The reproducibility model connects to [Evidence and Reproducibility](../../../14-05-evidence-and-reproducibility.md), [MVC experimental design](mvc-experimental-design.md), and [MVC reproductions](../reproductions/README.md). It is evidence metadata, not architecture authority.

## Summary

- MVC reproducibility is organized around research configurations.
- Generation and fingerprint boundaries protect comparison.
- Reproducibility packages identify the study condition and publication version.
- Generated outputs remain evidence, not authority.
