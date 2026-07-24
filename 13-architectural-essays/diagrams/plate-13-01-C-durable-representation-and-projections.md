# Plate 13-01-C - Durable representation and selective projections

**Plate ID:** `13-01-C`  
**Parent work:** `13-01-when-machines-stopped-waiting.md`  
**Rendered projection:** `plate-13-01-C-durable-representation-and-projections.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** One durable representation of architectural state can support many projections; a single universal artifact optimized for both human narrative and machine traversal serves neither well.

**Sync rule:** When `plate-13-01-C-durable-representation-and-projections.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | Center hub (durable representation) with six projection cards around it. |
| Vertical structure | Header band, hub-and-spoke content, shared footer band. |
| Reading frame | Center hub first, then projections clockwise from decision record, then footer. |

Do not draw a database cylinder, graph UI, or STE stack. Projections are peers around the hub, not a demotion hierarchy.

---

## 2. Spatial arrangement

### 2.1 Coordinate system

Origin: top-left. Units: pixels. Snap: 8 px grid.

### 2.2 Header and footer

| Element | Position | Size |
| --- | --- | --- |
| Header band | x=32, y=32 | w=1216, h=56 |
| Plate title | x=48, y=68 | left-aligned |
| Plate ID | x=1232, y=66, `text-anchor=end` | — |
| Footer band | x=32, y=616 | w=1216, h=72 |
| Footer line 1 | x=640, y=646, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=668, `text-anchor=middle` | — |

### 2.3 Absolute node positions (authoritative)

| Node | x, y, w, h |
| --- | --- |
| Durable representation (hub) | 420, 280, 440, 152 |
| Decision record | 460, 112, 360, 72 |
| Diagram | 48, 200, 300, 88 |
| Executive view | 932, 200, 300, 88 |
| Engineer view | 48, 460, 300, 88 |
| Auditor path | 932, 460, 300, 88 |
| Computational bounded representation | 420, 500, 440, 80 |

Hub center: (640, 356).

---

## 3. Visual hierarchy

| Node class | Fill | Stroke | Stroke width | Radius |
| --- | --- | --- | --- | --- |
| Hub (durable representation) | `#E8F0FE` | `#1D4ED8` | 3 | 8 |
| Human-leaning projections (decision, diagram, executive, engineer, auditor) | `#F4F4F5` | `#52525B` | 1.5 | 6 |
| Computational projection | `#FEF3C7` | `#B45309` | 2 | 6 |
| Header / footer | `#FAFAFA` | `#D4D4D8` | 1 | 0 |

Hub is primary. Computational projection is secondary emphasis (amber). Other projections are equal peers (zinc).

No gradients, shadows, glow, icons, or 3D.

Dark theme via `prefers-color-scheme: dark`; geometry and labels unchanged.

---

## 4. Swimlanes

None. Hub-and-spoke only.

---

## 5. Alignment

| Rule | Specification |
| --- | --- |
| Hub centered on x=640 | Required |
| Top projection (decision) centered on hub | x=460 width 360 centers at 640 |
| Bottom projection (computational) same width/alignment as hub | x=420 |
| Left pair | x=48 |
| Right pair | x=932 |
| Projection text | left-aligned at box.x + 14 |
| Hub text | left-aligned at box.x + 16 |

---

## 6. Connectors

Straight lines from hub edge toward each projection. Marker on the projection end only (projection receives from hub).

| ID | Line coordinates (x1,y1)-(x2,y2) | To |
| --- | --- | --- |
| P1 | (640,280)-(640,192) | Decision record |
| P2 | (420,330)-(356,278) | Diagram |
| P3 | (860,330)-(924,278) | Executive |
| P4 | (420,400)-(356,452) | Engineer |
| P5 | (860,400)-(924,452) | Auditor |
| P6 | (640,432)-(640,492) | Computational |

Connector style: solid 2 px `#3F3F46`; marker `arrow-out-13-01-C`.

---

## 7. Arrow / marker

```
id: arrow-out-13-01-C
viewBox: 0 0 8 8
refX: 8
refY: 4
markerWidth: 8
markerHeight: 8
orient: auto
path: M0,0 L8,4 L0,8 Z
fill: #3F3F46
```

Use unique element IDs on this plate (`plate-title-13-01-C`, `plate-desc-13-01-C`, marker id above) so multiple handbook SVGs on one GitHub page do not collide.

---

## 8. Grouping

| Group | Contains |
| --- | --- |
| Hub | One durable-representation card |
| Projections | Six peer cards; computational distinguished by fill only |

---

## 9. Annotations

Footer exact text:

Line 1: `Projections are selective views, not demotions of documents and diagrams.`  
Line 2: `One universal artifact optimized for both narrative and machine traversal serves neither well.`

---

## 10. Labels (exact node text)

### 10.1 Header

| Field | Exact text |
| --- | --- |
| Title | `Durable representation and selective projections` |
| Plate ID | `Plate 13-01-C` |

### 10.2 Hub

- Title: `Durable representation of architectural state`
- Body line 1: `Identity, relationships, authority, provenance,`
- Body line 2: `scope, and lifecycle - explicit enough to survive`
- Body line 3: `changes in presentation`

### 10.3 Projections

**Decision record**

- Title: `Decision record`
- Body: `Narrative of what was decided and why`

**Diagram**

- Title: `Diagram`
- Body line 1: `Selective view`
- Body line 2: `Traceable to the elements it depicts`

**Executive view**

- Title: `Executive projection`
- Body line 1: `Capabilities, risk,`
- Body line 2: `and unresolved choices`

**Engineer view**

- Title: `Engineer projection`
- Body line 1: `Governing intent, constraints,`
- Body line 2: `affected components, evidence obligations`

**Auditor path**

- Title: `Auditor projection`
- Body line 1: `Obligation to decision to`
- Body line 2: `embodiment to evidence`

**Computational bounded representation**

- Title: `Computational projection`
- Body: `Bounded identities and relationships required for a task`

### 10.4 Forbidden labels

Do not add: STE, Architecture IR, Kernel, Runtime, CEM, Concierge, graph database, schema dump, "raw graph as UI," vendor names.

### 10.5 Text baselines (authoritative for SVG)

| Node | Title y | Body y | Text x |
| --- | --- | --- | --- |
| Hub | 312 | 336, 356, 376 | 436 |
| Decision | 140 | 164 | 474 |
| Diagram | 228 | 252, 272 | 62 |
| Executive | 228 | 252, 272 | 946 |
| Engineer | 488 | 512, 532 | 62 |
| Auditor | 488 | 512, 532 | 946 |
| Computational | 528 | 552 | 436 |

---

## 11. Typography

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Header title | 20 | 600 | `#18181B` |
| Plate ID | 12 | 500 | `#71717A` |
| Hub title | 14 | 600 | `#1D4ED8` |
| Hub body | 12 | 400 | `#3F3F46` |
| Projection title | 13 | 600 | `#18181B` |
| Projection body | 12 | 400 | `#3F3F46` |
| Footer 1 | 13 | 600 | `#18181B` |
| Footer 2 | 12 | 400 | `#52525B` |

Font stack: Inter, Helvetica Neue, Arial, sans-serif.

---

## 12. Reproduction checklist

1. 1280x720, 8 px grid, no shadows.
2. Place hub and six projections per §2.3.
3. Exact labels from §10.
4. Connectors per §6 with unique marker id.
5. Unique title/desc element ids (§7).
6. No forbidden labels.
7. UTF-8 without BOM; XML parse OK.

---

## 13. SVG layer order

1. Canvas
2. Header
3. Projection cards
4. Hub card
5. Footer chrome
6. Connectors
7. Text (nodes, then header/footer)

---

## 14. Acceptance criteria

1. Reader can state the one-sentence insight from hub-then-spokes reading.
2. Hub encodes durable state properties named in the essay.
3. All six projection types from the essay appear.
4. Documents/diagrams are not demoted; footer states that.
5. No STE implementation machinery.
6. SVG matches this document within +/- 8 px.
7. Well-formed UTF-8 XML; unique IDs to avoid multi-SVG collisions on GitHub.
