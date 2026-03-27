#!/usr/bin/env python3
"""
Generate Mermaid projections for this AI Gateway example from ir/architecture-ir.json.

Usage (from this directory):
    python generate_projections.py

Or from ste-handbook repo root:
    python 11-examples/ai-gateway-example/generate_projections.py
"""

from __future__ import annotations

import json
from pathlib import Path


EXAMPLE_ROOT = Path(__file__).resolve().parent
IR_PATH = EXAMPLE_ROOT / "ir" / "architecture-ir.json"
OUT_DIR = EXAMPLE_ROOT / "projections" / "generated"

HEADER = """%% GENERATED FILE — do not edit by hand.
%% Source: ../../ir/architecture-ir.json
%% Generator: 11-examples/ai-gateway-example/generate_projections.py
"""


def mermaid_id(entity_id: str) -> str:
    return "E_" + entity_id.replace("-", "_")


def load_ir() -> dict:
    with IR_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def entity_index(ir: dict) -> dict[str, dict]:
    return {e["id"]: e for e in ir["entities"]}


def emit_capability_component(ir: dict) -> str:
    """Projection A: components, capabilities, interface + selected edge types."""
    allow = {
        "COMP-0010",
        "COMP-0003",
        "CAP-0015",
        "CAP-0016",
        "CAP-0001",
        "IFACE-0012",
    }
    edge_types = {"implements", "depends_on", "exposes"}
    entities = entity_index(ir)
    lines = [
        HEADER.rstrip(),
        "",
        "# Capability / component projection (from Architecture IR)",
        "",
        "```mermaid",
        "flowchart TB",
    ]
    for eid in sorted(allow):
        e = entities[eid]
        label = e["name"].replace('"', "'")
        lines.append(f'  {mermaid_id(eid)}["{label}"]')
    for rel in ir["relationships"]:
        if rel["relationship_type"] not in edge_types:
            continue
        a, b = rel["from_entity_id"], rel["to_entity_id"]
        if a not in allow or b not in allow:
            continue
        lbl = rel["relationship_type"].replace("_", " ")
        lines.append(f'  {mermaid_id(a)} -->|"{lbl}"| {mermaid_id(b)}')
    lines.extend(["```", ""])
    return "\n".join(lines)


def emit_system_context(ir: dict) -> str:
    """Projection B: components and external systems + cross-boundary edges."""
    entities = entity_index(ir)
    subset = {
        eid
        for eid, e in entities.items()
        if e["entity_type"] in ("component", "external_system")
    }
    edge_types = {"depends_on", "invokes_provider", "realizes_external"}
    lines = [
        HEADER.rstrip(),
        "",
        "# System context projection (from Architecture IR)",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for eid in sorted(subset):
        e = entities[eid]
        label = e["name"].replace('"', "'")
        lines.append(f'  {mermaid_id(eid)}["{label}"]')
    for rel in ir["relationships"]:
        if rel["relationship_type"] not in edge_types:
            continue
        a, b = rel["from_entity_id"], rel["to_entity_id"]
        if a not in subset or b not in subset:
            continue
        lbl = rel["relationship_type"].replace("_", " ")
        lines.append(f'  {mermaid_id(a)} -->|"{lbl}"| {mermaid_id(b)}')
    lines.extend(["```", ""])
    return "\n".join(lines)


def main() -> None:
    ir = load_ir()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "ir-capability-component.md").write_text(
        emit_capability_component(ir), encoding="utf-8"
    )
    (OUT_DIR / "ir-system-context.md").write_text(
        emit_system_context(ir), encoding="utf-8"
    )
    print(f"Wrote projections to {OUT_DIR}")


if __name__ == "__main__":
    main()
