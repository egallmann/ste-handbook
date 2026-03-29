# AI Gateway example — consolidated Architecture IR

This folder holds a **single machine-readable snapshot** of the illustrative **Architecture IR** used across [Step 6](../06-derived-architecture-ir.md) and the [generated projections](../projections/README.md).

- [`architecture-ir.json`](architecture-ir.json) lists **entities** and **relationships** with stable ids aligned to the ADR excerpts in steps 3–5 (`ADR-L-AIGW-001`, `ADR-PS-AIGW-001`, `ADR-PC-AIGW-001`).
- The JSON is **handbook pedagogy**, not a **ste-spec** contract. It exists so **projection adapters** can emit **consistent** structural views (see [`../projections/README.md`](../projections/README.md)); committed Mermaid under `projections/generated/` illustrates the result.

**Normative truth** for real STE programs remains in **ste-spec** and your compilers.
