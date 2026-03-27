# IR-driven projections (AI Gateway example)

This folder shows how **Architecture IR** can feed **repeatable projections**—here, **Mermaid** diagrams (in Markdown fences) aligned to the consolidated IR snapshot.

## Source of truth

- IR snapshot: [`../ir/architecture-ir.json`](../ir/architecture-ir.json)

## Committed outputs

Files under [`generated/`](generated/) are **structural projections** of that IR (capability/component view and system context). They are **checked in** as the reader-visible illustration.

- `ir-capability-component.md` — components, capabilities, `implements` / `depends_on` / `exposes` among those types.
- `ir-system-context.md` — gateway component, platform auth component, external systems, and key cross-boundary edges.

**Do not hand-edit generated files** in normal authoring. Change [`architecture-ir.json`](../ir/architecture-ir.json) (or your **projection adapter** configuration), then **regenerate** through your STE toolchain.

## Regeneration (adapter, not handbook code)

The handbook does **not** ship an executable generator. In a full STE deployment, a **projection adapter** (compiler plugin, service, or internal tool) consumes **Architecture IR** plus a **projection spec**—conceptually the selections in [`projection-queries.md`](projection-queries.md)—and emits views such as these Markdown+Mermaid files.

Readers and integrators use the **adapter interface**; they do not need to edit projection code unless they are extending the platform. Maintainers who keep a **local** helper script for this example may do so; it is **gitignored** and not part of the public manuscript (see repository `.gitignore`).

## Query-shaped projection specs

Illustrative “**architecture projection DSL**” sketches—how you might **select** subgraphs for a view—live in [`projection-queries.md`](projection-queries.md). They are **pedagogical**, not a normative **ste-spec** language.

## Pedagogical diagrams elsewhere

The narrative diagrams under [`../diagrams/`](../diagrams/) (intent ladder, canonical vs derived, feedback loop) are **conceptual** process figures. They are **not** claimed to be emitted from `architecture-ir.json`; only the `generated/` Mermaid here is **IR-faithful** in this example.
