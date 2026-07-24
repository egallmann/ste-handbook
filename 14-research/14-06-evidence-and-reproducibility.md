---
title: "Evidence and Reproducibility"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-07-19"
---

# Evidence and Reproducibility

## The Problem

A study that cannot be reproduced is hard to interpret. A study that can be rerun but lacks versioned context is only mechanically repeatable, not scientifically inspectable.

STE research needs reproducibility packages that preserve the research condition, not only the command or output that produced a result.

## The Reframe

Research evidence is packaged around a research configuration. A research configuration identifies the frozen state of the study condition so findings and reproductions can point to the same thing.

Research configurations are evidence metadata. They are not architecture authority.

## The Model

A research configuration should identify:

```yaml
research_program:
methodology_version:
benchmark_version:
candidate_version:
repository_commits:
model_condition:
experiment_generation:
assembly_definition:
assembly_algorithm_version:
assembly_configuration:
configuration_fingerprint:
fixed_configuration_fields:
varied_configuration_fields:
configuration_equivalence:
configuration_drift_status:
```

The exact fields vary by research program. The principle is stable: the configuration should preserve the study condition well enough that a future reader can distinguish a theory effect from a substrate change, task change, scorer change, model change, assembly change, or configuration drift.

### Conceptual reproducibility controls

Beyond field lists, reproducibility depends on instrument controls:

| Control | Role | Limit |
|---------|------|-------|
| Sealed identity | Questions, answers, packages, and configurations remain addressable and tamper-evident under the study boundary. | Identity is not correctness. |
| Append-only lineage | Corrections and repairs add records; they do not silently rewrite prior observations. | Lineage is not adjudication. |
| Bounded replay | Re-checking under declared controls supports reproducibility claims. | Replay is not proof of truth. |
| Research exclusion | Synthetic and local-test artifacts remain marked and fail closed out of research-evidence paths. | Exclusion is not a finding. |

Generated projections and derived views remain non-authoritative unless the methodology explicitly admits them as evidence inputs. A reproducibility package that cannot show these controls is at best mechanically repeatable.

A reproducibility package should reference a research configuration and identify:

- Research question.
- Hypothesis.
- Protocol or methodology version.
- Benchmark or task-bank version, when applicable.
- Candidate records or representation conditions.
- HSCA records when human-assisted analysis is used.
- Scoring or observation methodology.
- Result artifacts.
- Evidence boundary and supersession status.
- Configuration identity, equivalence, and drift status when configuration affects the claim.

The package may expose only a public subset at first. If task-bank contents, scoring implementations, candidate context artifacts, reasoner identity details, generated execution records, or operational commands are withheld, the publication should say so plainly and state what would be required for independent reproduction later.

## The Implications

- A score without a research configuration is weak evidence.
- A task-bank change creates a new comparison boundary.
- A model or scoring change creates a new research configuration.
- An assembly or configuration change creates a new research configuration unless declared equivalent.
- Candidate records must be identifiable without becoming architecture authority.
- Publication readiness and reproduction readiness are related but not identical.

## Relationship to STE system

Reproducibility packages are research evidence. They are analogous to [Evidence](../03-artifacts/03-05-evidence.md) in the STE lifecycle, but they do not become canonical artifacts unless accepted through normal governance.

## Summary

- Reproducibility preserves the research condition, not only the output.
- Research configurations represent frozen study states.
- Reproducibility packages should reference research configurations.
- Research configurations are evidence metadata, not authority.

Read next: [Measurement and Validity](14-07-measurement-and-validity.md) explains how research keeps evidence limits visible.
