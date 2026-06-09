---
title: "STE Research Index"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# STE Research Index

## The Problem

Research programs need a stable publication home. Without one, theories, methods, findings, reproductions, and open questions drift into unrelated documents or operational repositories.

## The Reframe

This directory is the canonical publication area for STE research programs. It contains human-readable theories, methodologies, experiment designs, findings, reproductions, and open questions.

It does not contain operational harnesses, task-bank contents, generated execution records, continuation state, raw results, scoring systems, or executable reproducibility assets. Those belong in the owning repositories or reproducibility packages.

## The Model

Every research program should follow this structure unless a justified exception exists:

```text
research/<program>/
├── README.md
├── 01-thesis/
├── 02-methodology/
├── 03-experiment-design/
├── 04-findings/
├── 05-reproductions/
└── 06-open-questions.md
```

Every `research/<program>/README.md` should declare informational metadata:

```yaml
program_id:
title:
status:
lead_authors:
created:
last_reviewed:
research_state:
  candidate|active|reproduced|dormant|retired
related_theories:
related_methodologies:
```

Metadata supports indexing, cataloging, discovery, and governance. It does not imply authority or maturity.

Current research programs:

- [MVC](mvc/README.md) - representation ceiling, viable context, substrate completeness, and context-assembly research.

## The Implications

Each research program must maintain open questions as a living artifact. Open questions include unvalidated assumptions, competing explanations, candidate theories, unresolved validity concerns, and future evidence needs.

## Relationship to STE system

The research index is a handbook publication surface. It does not replace `ste-spec`, `ste-runtime`, `adr-architecture-kit`, or any authority-bearing artifact.

## Summary

- `14-research/research/` is the publication home for STE research programs.
- Research programs use a common numbered lifecycle structure.
- Research metadata is informational, not authoritative.
- Open questions are required living artifacts.
