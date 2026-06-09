---
title: "Research Library"
status: draft
maturity: L1
diagrams: false
last_reviewed: "2026-06-09"
---

# Research Library

## The Problem

Research programs grow over time. Without a standard publication structure, theories, methodologies, findings, reproductions, and open questions become scattered. Readers cannot tell which artifact states the theory, which artifact defines the method, and which artifact records evidence.

## The Reframe

The research library is the canonical publication area for STE research programs. It is not a code repository, benchmark store, or raw result archive. It is the human-readable record of research programs and their publication lineage.

## The Model

Every research program should use this structure unless a justified exception exists:

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

Each `research/<program>/README.md` declares informational metadata:

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

MVC is the first reference implementation of this structure.

## The Implications

- Future research programs should have the same numbered durable homes for thesis, methodology, experiment design, findings, reproductions, and open questions.
- Open questions are required living research artifacts.
- Findings and reproductions should reference the research configuration and publication versions they derive from.
- Operational artifacts remain outside the handbook unless intentionally published as prose or index entries.

## Relationship to STE system

The research library complements `ste-spec`, `ste-runtime`, and `adr-architecture-kit`. It explains and preserves research; it does not define contracts, runtime behavior, or ADR authority.

## Summary

- `14-research/research/` is the canonical research publication area.
- Research programs should follow the same structure.
- MVC is the first reference implementation.
- Research metadata is informational, not authoritative.
