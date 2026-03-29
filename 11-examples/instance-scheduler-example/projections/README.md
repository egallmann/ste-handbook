# IR-driven projections (Instance Scheduler example)

This folder shows how **Architecture IR** feeds **repeatable projections** — here, **Mermaid** diagrams aligned to the consolidated IR snapshot for the **second** Part 11 walkthrough.

## Source of truth

- IR snapshot: [`../ir/architecture-ir.json`](../ir/architecture-ir.json)

## Committed outputs

Files under [`generated/`](generated/) are **structural projections** of that IR. They are **checked in** as reader-visible illustrations.

- `ir-capability-component.md` — capabilities, components, interfaces; `implements` / `depends_on` / `exposes`.
- `ir-system-context.md` — orchestration component, EC2/RDS externals, `invokes_provider`.
- `ir-traceability.md` — requirements, invariants, decisions, capabilities, components; `enabled_by`, `constrains`, `supports`, selected `implements`.

## Fidelity note

This IR **includes requirement and invariant entities** and **trace edges** that the AI Gateway example omits in JSON form — on purpose, to show a **richer** STE compilation story. Production adapters still **collapse** to pinned compiled edge sets per **ste-spec** / **ste-kernel**; see narrative in [Step 6](../06-derived-architecture-ir.md).

**Do not hand-edit generated files** in normal authoring. Change [`architecture-ir.json`](../ir/architecture-ir.json), then **regenerate**.

## Regeneration

From `instance-scheduler-example/`:

```bash
python generate_projections.py
```

The script is a **local maintainer helper** (gitignored policy matches the AI Gateway example — see repository `.gitignore`).

## Composite projection (rules + invariants + physical context)

[`rules-invariants-system-context.md`](rules-invariants-system-context.md) joins **IR** (`constrains` edges, components, externals) with **Phase 6** [rules activation](../05d-rules-activation.md) for a **per-component** view of **invariants** and **activated rule families**. Spec: **Query D** in [`projection-queries.md`](projection-queries.md).

## Query-shaped projection specs

See [`projection-queries.md`](projection-queries.md).
