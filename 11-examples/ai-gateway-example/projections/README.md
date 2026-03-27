# IR-driven projections (AI Gateway example)

This folder shows how **Architecture IR** can feed **repeatable projections**—here, **Mermaid** diagrams (in Markdown fences) generated from the consolidated IR snapshot.

## Source of truth

- IR snapshot: [`../ir/architecture-ir.json`](../ir/architecture-ir.json)

## Generated outputs

Files under [`generated/`](generated/) are produced by [`../generate_projections.py`](../generate_projections.py):

- `ir-capability-component.md` — components, capabilities, `implements` / `depends_on` / `exposes` among those types.
- `ir-system-context.md` — gateway component, platform auth component, external systems, and key cross-boundary edges.

**Do not hand-edit generated files.** Change the IR JSON (or the generator), then re-run the script.

## Regenerate

From the **ste-handbook** repository root:

```bash
python 11-examples/ai-gateway-example/generate_projections.py
```

Or from `11-examples/ai-gateway-example/`:

```bash
python generate_projections.py
```

Requires **Python 3** with the standard library only (uses `json`).

## Query-shaped projection specs

Illustrative “**architecture projection DSL**” sketches—how you might **select** subgraphs for a view—live in [`projection-queries.md`](projection-queries.md). They are **pedagogical**, not a normative **ste-spec** language.

## Pedagogical diagrams elsewhere

The narrative diagrams under [`../diagrams/`](../diagrams/) (intent ladder, canonical vs derived, feedback loop) are **conceptual** process figures. They are **not** claimed to be emitted from `architecture-ir.json`; only the `generated/` Mermaid here is **IR-faithful** in this example.
