---
title: "Part 3 — Intent Layer Overview"
status: draft
maturity: L0
diagrams: false
last_reviewed: "2026-03-22"
---

# Part 3 — Intent Layer Overview

This chapter introduces the intent layer: the structured expression of architectural decisions, constraints, invariants, and capabilities that downstream compilation and validation consume. It explains why intent is a distinct layer from IR and code.

## Why this matters

Without a clear intent layer, IR becomes a dumping ground for mixed concerns. This part separates decision semantics from canonical system modeling.

## Planned coverage

- Intent artifacts and their roles
- Relationship to ADR surfaces (L/PS/PC)
- Handoff to Architecture IR compilation

## Relationship to other chapters

- Intent model ([chapter](03-01-intent-model.md))
