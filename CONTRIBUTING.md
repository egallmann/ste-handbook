# Contributing to the STE Handbook

Thank you for helping improve explanatory documentation for System of Thought Engineering (STE).

## Branching strategy

This repository uses a long-lived integration branch and feature branches:

| Branch | Purpose |
|--------|---------|
| **`main`** | **Production / stable** documentation—what readers should trust as the current published handbook. |
| **`develop`** | **Integration** branch for completed features that have been reviewed and merged. |
| **`feature/*`** | **Feature branches** created **from `develop`** (not from `main`). |

**Workflow:** `feature/*` (from `develop`) → pull request into **`develop`** → pull request **`develop`** into **`main`**.

`main` should only move forward via pull request from `develop`, and `develop` should receive work through feature PRs.

## Pull request expectations

- Keep changes focused: one logical improvement or chapter per PR when practical.
- Link related issues or discussion threads when your host supports it.
- Prefer incremental depth: establish structure and correct links before large narrative rewrites.
- Ensure new diagrams follow the Mermaid rule below.

## Documentation writing standards

- Use clear headings and short sections; prefer linking to **`ste-spec`** for normative statements instead of restating specification text as if this repo were authoritative.
- When describing behavior that is specified elsewhere, point readers to the relevant **`ste-spec`** areas or contracts.
- Avoid presenting handbook prose as the single source of truth for STE semantics—the handbook **explains**; **`ste-spec`** **defines** requirements.

## Diagrams

- All diagrams in this repository must be written in **Mermaid** (for example `.mmd` files under `diagrams/` or fenced `mermaid` blocks in Markdown).
- Diagrams are **derived projections** of ADRs, Architecture IR, and implementation artifacts. They aid understanding and communication.
- Diagrams are **not** authoritative architecture definitions. If a diagram and **`ste-spec`** or published contracts conflict, the specification and contracts win.

## License

By contributing, you agree that your contributions are licensed under the same license as the project (Apache License 2.0). See [LICENSE](LICENSE).
