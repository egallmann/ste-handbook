# Plate 13-01-B - Reconstruction that dies vs understanding that participates

**Plate ID:** `13-01-B`  
**Parent work:** `13-01-when-machines-stopped-waiting.md`  
**Rendered projection:** `plate-13-01-B-reconstruction-vs-participation.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Successful reconstruction usually ends with the task unless deliberately represented; preserved understanding can participate in later reasoning without the same reconstruction.

**Sync rule:** When `plate-13-01-B-reconstruction-vs-participation.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | Shared vertical stem (task -> reconstruction), then a two-column fork (dies with task vs durable representation that participates later). |
| Vertical structure | Header band, shared stem, fork columns, shared footer band. |
| Reading frame | Top stem top-to-bottom, then left fork, then right fork, then footer. |

Do not draw financial ROI or compounding-as-finance metaphors. Do not show storage products or STE tooling.

---

## 2. Spatial arrangement

### 2.1 Coordinate system

Origin: top-left of canvas. Units: pixels. Snap: 8 px grid.

### 2.2 Full-width header band

| Element | Position | Size |
| --- | --- | --- |
| Header band | x=32, y=32 | w=1216, h=56 |
| Plate title (text) | x=48, baseline y=68 | left-aligned |
| Plate ID (text) | x=1232, baseline y=66, `text-anchor=end` | right-aligned |

### 2.3 Absolute node positions (authoritative)

| Node | x, y, w, h |
| --- | --- |
| Engineering task | 440, 112, 400, 72 |
| Reconstruction event | 440, 216, 400, 88 |
| Dies with the task | 48, 368, 520, 96 |
| Next task repeats inference | 48, 500, 520, 88 |
| Durable represented understanding | 664, 368, 520, 96 |
| Later tasks reuse / participate | 664, 500, 520, 88 |

Derived edges:

| Edge | Value |
| --- | --- |
| Task bottom | y=184 |
| Reconstruct top | y=216 |
| Reconstruct bottom | y=304 |
| Reconstruct midline x | x=640 |
| Left column midline | x=308 |
| Right column midline | x=924 |
| Fork destination tops | y=368 |
| Lower fork tops | y=500 |

### 2.4 Column titles (Band above fork boxes)

| Element | Position |
| --- | --- |
| Left title baseline | x=48, y=348 |
| Left underline | x1=48, y1=354, x2=280, y2=354 |
| Right title baseline | x=664, y=348 |
| Right underline | x1=664, y1=354, x2=980, y2=354 |

### 2.5 Footer band (shared)

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=616 | w=1216, h=72 |
| Footer line 1 | x=640, y=646, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=668, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest -> lowest):

1. Fork outcome boxes (dies vs durable / participate)
2. Reconstruction event (shared costly step)
3. Engineering task
4. Connectors
5. Column titles
6. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Engineering task | `#F4F4F5` | `#52525B` | 1.5 | 6 |
| Reconstruction event | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Dies with the task | `#FEE2E2` | `#B91C1C` | 2 | 6 |
| Next task repeats | `#F4F4F5` | `#52525B` | 1.5 | 6 |
| Durable represented understanding | `#ECFDF5` | `#047857` | 2.5 | 6 |
| Later tasks reuse / participate | `#E8F0FE` | `#1D4ED8` | 2 | 6 |
| Header / footer | `#FAFAFA` | `#D4D4D8` | 1 | 0 |

Do not use gradients, shadows, glow, 3D bevels, or icons.

Dark theme optional via `prefers-color-scheme: dark`; geometry and labels unchanged.

---

## 4. Swimlanes

Two fork lanes only (after the shared stem):

| Lane | Title text | Semantic role |
| --- | --- | --- |
| L | `Without durable representation` | Understanding dies with the task |
| R | `With durable representation under care` | Understanding participates later |

---

## 5. Alignment

| Rule | Specification |
| --- | --- |
| Stem boxes | Centered on canvas midline x=640; width 400 |
| Fork box tops | Align across columns at y=368 and y=500 |
| Left text x | box.x + 14 |
| Right text x | box.x + 14 |
| Stem connectors | x=640 |
| Fork drop connectors | left x=308; right x=924 |

---

## 6. Connectors

| ID | Line coordinates (x1,y1)-(x2,y2) | Meaning |
| --- | --- | --- |
| S1 | (640,184)-(640,208) | Task -> Reconstruction |
| F1a | (640,304)-(640,328) | Stem into fork junction |
| F1b | (640,328)-(308,328) | Junction to left midline |
| F1c | (308,328)-(308,360) | Drop into Dies box |
| F1d | (640,328)-(924,328) | Junction to right midline |
| F1e | (924,328)-(924,360) | Drop into Durable box |
| L2 | (308,464)-(308,492) | Dies -> Next task repeats |
| R2 | (924,464)-(924,492) | Durable -> Later tasks participate |

Marker: `arrow-down` on S1, F1c, F1e, L2, R2 only (vertical drops). Horizontal F1b/F1d have no arrowheads.

Connector style: solid 2 px `#3F3F46`.

---

## 7. Arrow styles

### 7.1 Marker definition (authoritative)

```
id: arrow-down
viewBox: 0 0 8 8
refX: 8
refY: 4
markerWidth: 8
markerHeight: 8
orient: auto
path: M0,0 L8,4 L0,8 Z
fill: #3F3F46
```

Same marker pattern as Plate 13-01-A (path points +x; `orient=auto` aligns to stroke). Dark theme marker fill `#C9D1D9`.

Bidirectional / dashed / curved connectors forbidden.

---

## 8. Grouping

| Group | Contains | Visual treatment |
| --- | --- | --- |
| Shared stem | Task + Reconstruction | Two separate boxes on midline |
| Left fork | Dies + Next repeats | Two stacked boxes |
| Right fork | Durable + Later participate | Two stacked boxes |

No enclosing column frames on this plate (unlike Plate 13-01-A).

---

## 9. Annotations

### 9.1 Footer annotation (exact text)

Line 1: `Recurrence matters more than any single reconstruction.`  
Line 2: `Left: inference repeats. Right: validated understanding participates in later reasoning.`

### 9.2 No connector side labels

Column titles carry the fork contrast.

---

## 10. Labels (exact node text)

### 10.1 Header

| Field | Exact text |
| --- | --- |
| Title | `When reconstruction survives the task` |
| Plate ID | `Plate 13-01-B` |

### 10.2 Engineering task

- Title: `Engineering task`
- Body: `Discovery, planning, implementation, review, incidents, modernization, governance, AI-assisted work`

### 10.3 Reconstruction event

- Title: `Reconstruction / inference event`
- Body line 1: `Recover enough architectural understanding`
- Body line 2: `to reason safely about what may change`

### 10.4 Dies with the task

- Title: `Understanding dies with the task`
- Body line 1: `Recovery may succeed`
- Body line 2: `Without deliberate representation under care, it usually ends here`

### 10.5 Next task repeats inference

- Title: `Next reasoning event`
- Body line 1: `Repeats much of the same inference`
- Body line 2: `from tickets, memory, and conflicting documents`

### 10.6 Durable represented understanding

- Title: `Durable represented understanding`
- Body line 1: `Recovered understanding survives the event`
- Body line 2: `Kept under care beyond the task that produced it`

### 10.7 Later tasks reuse / participate

- Title: `Later reasoning events`
- Body line 1: `Begin from what was previously represented`
- Body line 2: `Validated understanding participates without the same reconstruction`

### 10.8 Forbidden labels

Do not add: STE, Architecture IR, substrate, Kernel, Runtime, ROI, capital, compounding-as-finance, storage products, vendor names.

### 10.9 Text baselines (authoritative for SVG)

| Node | Title y | Body y | Text x |
| --- | --- | --- | --- |
| Task | 140 | 162, 178 | 454 |
| Reconstruction | 244 | 268, 288 | 454 |
| Dies | 396 | 420, 440 | 62 |
| Next repeats | 528 | 552, 572 | 62 |
| Durable | 396 | 420, 440 | 678 |
| Later participate | 528 | 552, 572 | 678 |
| Left column title | 348 | — | 48 |
| Right column title | 348 | — | 664 |

Task body wrap (exact):

- `Discovery, planning, implementation, review,`
- `incidents, modernization, governance, AI-assisted work`

---

## 11. Typography hierarchy

| Role | Font | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| Header title | Inter, Helvetica Neue, Arial, sans-serif | 20 px | 600 | `#18181B` |
| Plate ID | same | 12 px | 500 | `#71717A` |
| Column title | same | 13 px | 600 | `#27272A` |
| Node title | same | 13 px | 600 | `#18181B` |
| Node body | same | 12 px | 400 | `#3F3F46` |
| Footer line 1 | same | 13 px | 600 | `#18181B` |
| Footer line 2 | same | 12 px | 400 | `#52525B` |

Column-title underline: 2 px `#A1A1AA`.

---

## 12. Reproduction checklist

1. Create 1280x720 page, grid 8 px, no shadows.
2. Place header, six content boxes, footer per §2.
3. Place column titles and underlines per §2.4.
4. Enter exact labels from §10.
5. Add connectors per §6 with marker per §7.
6. Apply fills/strokes per §3.
7. Verify fork contrast: left dies/repeats vs right durable/participates.
8. Verify no forbidden labels (§10.8).
9. Save UTF-8 without BOM; validate XML parse.

---

## 13. SVG layer order (bottom -> top)

1. Canvas background
2. Header band
3. Content boxes (stem, then fork)
4. Footer band chrome
5. Connectors and arrowheads
6. Column titles and underlines
7. Node text
8. Header and footer text

---

## 14. Acceptance criteria

1. Reader can state the one-sentence insight after stem-then-left-then-right reading.
2. Left path shows successful reconstruction that does not survive.
3. Right path shows representation under care enabling later participation.
4. No STE stack, ROI, or storage-product imagery.
5. Vertical shafts visible on stem and fork drops.
6. `plate-13-01-B-reconstruction-vs-participation.svg` matches this document within +/- 8 px.
7. SVG is well-formed UTF-8 XML.
