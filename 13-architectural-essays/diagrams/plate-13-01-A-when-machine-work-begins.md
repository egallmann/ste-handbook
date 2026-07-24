# Plate 13-01-A - When machine work begins

**Plate ID:** `13-01-A`  
**Parent work:** `13-01-when-machines-stopped-waiting.md`  
**Rendered projection:** `plate-13-01-A-when-machine-work-begins.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Historical machines act after enough understanding is represented for a bounded operation; the newer computational participant is invited while architectural work is still open.

**Sync rule:** When `plate-13-01-A-when-machine-work-begins.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | Two vertical columns of equal width, separated by a 24 px gutter. Left column = historical path. Right column = earlier participation path. |
| Column width | Each column frame: 584 px (from x=32 and x=664). |
| Vertical structure | Header band, two column frames, shared footer band. Inside each column: column title, Stage 1, Stage 2, Stage 2 caption + Stage 2 to Stage 3 connector region, Stage 3. |
| Reading frame | Top banner (full width) -> left column top-to-bottom -> right column top-to-bottom -> footer contrast bar. |

Do not use a single continuous timeline across the whole canvas. The two columns are parallel comparative paths, not sequential eras that require a single chronological axis.

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

### 2.3 Column frames

| Element | Position | Size |
| --- | --- | --- |
| Left column frame | x=32, y=104 | w=584, h=488 |
| Right column frame | x=664, y=104 | w=584, h=488 |

Each column frame is a rounded rectangle (radius 8) with 1.5 px stroke. Interior content left edge = frame.x + 16.

### 2.4 Absolute stage-box positions (authoritative)

| Node | Left column (x,y,w,h) | Right column (x,y,w,h) |
| --- | --- | --- |
| Stage 1 | 48, 168, 520, 80 | 680, 168, 520, 80 |
| Stage 2 | 48, 304, 520, 80 | 680, 304, 520, 80 |
| Stage 3 | 48, 448, 520, 112 | 680, 448, 520, 112 |

Derived edges:

| Edge | Y |
| --- | --- |
| Stage 1 bottom | 248 |
| Stage 2 top | 304 |
| Stage 2 bottom | 384 |
| Stage 3 top | 448 |
| Stage 3 bottom | 560 |

Vertical gaps:

| Gap | Clearance (box bottom to next box top) | Purpose |
| --- | --- | --- |
| Stage 1 to Stage 2 | 56 px | Full arrow shaft visible (not head-only) |
| Stage 2 to Stage 3 | 64 px | Captions left of midline + shaft + side labels right of midline |

### 2.5 Column titles

| Element | Position |
| --- | --- |
| Left title baseline | x=48, y=136 |
| Left underline | x1=48, y1=142, x2=430, y2=142 |
| Right title baseline | x=680, y=136 |
| Right underline | x1=680, y1=142, x2=1070, y2=142 |

Underline: 2 px stroke `#A1A1AA` (required in rendered SVG).

### 2.6 Footer band (shared)

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=616 | w=1216, h=72 |
| Footer line 1 | x=640, y=646, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=668, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest -> lowest):

1. Stage-3 machine role boxes (largest fill contrast; primary claim nodes)
2. Stage-2 state boxes (closure boundary vs open work)
3. Stage-1 human work boxes
4. Vertical flow arrows within columns
5. Column titles
6. Header / plate chrome
7. Footer contrast annotation
8. Secondary callouts (Stage-2 captions and connector side labels)

Node size hierarchy:

| Node class | Box size (w x h) | Corner radius |
| --- | --- | --- |
| Primary (Stage 3) | 520 x 112 | 8 |
| Secondary (Stage 1, Stage 2) | 520 x 80 | 6 |
| Column title | text only + required underline 2 px | — |

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width |
| --- | --- | --- | --- |
| Stage 1 | `#F4F4F5` | `#52525B` | 1.5 |
| Stage 2 left (closed-enough product) | `#E8F0FE` | `#1D4ED8` | 2 |
| Stage 2 right (open work) | `#FEF3C7` | `#B45309` | 2 |
| Stage 3 left (historical consumers) | `#ECFDF5` | `#047857` | 2.5 |
| Stage 3 right (computational participant) | `#FEE2E2` | `#B91C1C` | 2.5 |
| Column frames | `#FFFFFF` | `#A1A1AA` | 1.5 |
| Header | `#FAFAFA` | `#D4D4D8` | 1 |
| Footer | `#FAFAFA` | `#D4D4D8` | 1 |

Do not use gradients, shadows, glow, 3D bevels, or icons.

Dark theme (optional CSS `prefers-color-scheme: dark`): remap fills/strokes/text for GitHub dark viewing. Geometry and labels unchanged.

---

## 4. Swimlanes

Two vertical swimlanes only:

| Lane ID | Title text | Semantic role |
| --- | --- | --- |
| L | `Historical path: after closure for a bounded operation` | After operation-relative closure |
| R | `Earlier path: before the architecture has fully converged` | Before architectural convergence |

No horizontal swimlanes. Do not add a third lane for humans spanning both columns; human work appears as Stage 1 inside each lane.

---

## 5. Alignment

| Rule | Specification |
| --- | --- |
| Horizontal centering | All stage boxes in a column share left edge frame.x+16 and width 520. |
| Vertical rhythm | Stage 1/2/3 tops align across columns (168 / 304 / 448). |
| Text alignment | Node titles and body: left-aligned; content start x = box.x + 14. |
| Arrow alignment | Vertical connectors on column midlines: left x=308, right x=940. |
| Header/footer text | Header title left; Plate ID right; footer text centered. |

---

## 6. Connectors

### 6.1 Within-column vertical flow (required)

Four connectors total (two per column). Straight vertical only.

| ID | Line coordinates (x1,y1)-(x2,y2) | Meaning |
| --- | --- | --- |
| L1 | (308,248)-(308,296) | Left Stage 1 bottom -> Stage 2 top |
| L2 | (308,384)-(308,440) | Left Stage 2 bottom -> Stage 3 top |
| R1 | (940,248)-(940,296) | Right Stage 1 bottom -> Stage 2 top |
| R2 | (940,384)-(940,440) | Right Stage 2 bottom -> Stage 3 top |

Shaft ends 8 px above the destination box top so the 8 px marker tip meets the box edge.

Connector style:

| Property | Value |
| --- | --- |
| Stroke | `#3F3F46` |
| Width | 2 px |
| Line type | Solid |
| Arrowhead | SVG marker `arrow-down` (see §7) |
| Labels on L1/R1 | None |
| Labels on L2/R2 | Required side labels (§9.1) |

### 6.2 Cross-column connectors

None.

### 6.3 Footer

No arrows into or out of the footer.

---

## 7. Arrow styles

| Use | Style |
| --- | --- |
| Within-column succession | Solid 2 px `#3F3F46` with marker-end |
| Bidirectional / dashed / curved | Forbidden |

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

The triangle points along +x in marker space. `orient="auto"` aligns it to the stroke direction. Do not use a downward-pointing path in marker space (that double-rotates and appears reversed).

Dark theme: marker path fill `#C9D1D9`.

---

## 8. Grouping

| Group | Contains | Visual treatment |
| --- | --- | --- |
| Left column frame | Title, stages, captions, connectors | Single rounded rectangle enclosure |
| Right column frame | Title, stages, captions, connectors | Single rounded rectangle enclosure |
| Stage 3 left | One primary box | Consumer list as text lines with middle-dot separators |
| Stage 3 right | One primary box | Participant actions as separate text lines |

Do not draw nested subgraphs around Stage 1-3 beyond the column frame. Do not iconify individual tools as separate nodes.

---

## 9. Annotations

### 9.1 Required side labels on Stage-2 to Stage-3 connectors

Exact wording (same as original single-line labels; rendered as two lines to clear the shaft):

| Connector | Line 1 | Line 2 | Placement |
| --- | --- | --- | --- |
| L2 | `Machine consumes` | `closed-enough product` | x=320; baselines y=410 and y=424 |
| R2 | `Participant enters while` | `work remains open` | x=952; baselines y=410 and y=424 |

Font: 11 px, weight 500, color `#3F3F46`. Kept to the right of the shaft so captions can occupy the left half of the gap.

### 9.2 Required Stage-2 captions

Exact wording preserved; wrapped to stay left of the column midline (does not cross x=308 / x=940):

| Column | Line 1 | Line 2 | Placement |
| --- | --- | --- | --- |
| Left | `Closure is relative to the operation,` | `not universal completeness.` | x=48; y=400 and y=414 |
| Right | `Requirements, alternatives, and governing` | `constraints may still be unsettled.` | x=680; y=400 and y=414 |

Font: 11 px, weight 400, color `#52525B`.

### 9.3 Footer annotation (exact text)

Centered, two lines:

Line 1: `Contrast: not whether machines consume architecture, but when they enter the work.`  
Line 2: `Left: after represented semantics for a bounded operation. Right: before the architecture has fully converged.`

---

## 10. Labels (exact node text)

### 10.1 Header

| Field | Exact text |
| --- | --- |
| Title | `When machine work begins` |
| Plate ID | `Plate 13-01-A` |

### 10.2 Left column nodes

**Stage 1**

- Title: `Human interpretive work`
- Body line 1: `Interpret requirements that matter for the step`
- Body line 2: `Select among alternatives that matter for the step`
- Body line 3: `Resolve competing constraints that matter for the step`

**Stage 2**

- Title: `Represented product (closed enough for the operation)`
- Body line 1: `Source, manifest, rules, model, transitions, or executable definition`
- Body line 2: `Machine may treat this input as given`

**Stage 3**

- Title: `Historical machine consumers`
- Body line 1: `Compilers · build systems · deployers · policy engines`
- Body line 2: `Analyzers · model checkers · generators · simulation`
- Body line 3: `MBSE environments · executable / composable architecture definitions`
- Body line 4: `Execute, check, generate, compose, or simulate`

In SVG, middle dots are encoded as `&#183;` (UTF-8 ASCII-safe).

### 10.3 Right column nodes

**Stage 1**

- Title: `Human interpretive work (incomplete for the change)`
- Body line 1: `Stakeholder tension may remain unresolved`
- Body line 2: `Governing constraints may still be contested`
- Body line 3: `Authors of prior decisions may be gone`

**Stage 2**

- Title: `Open architectural work`
- Body line 1: `Architecture has not fully converged`
- Body line 2: `Understanding is still being assembled and interpreted`

**Stage 3**

- Title: `Computational participant`
- Body line 1: `Assemble context from tickets, diagrams, policies, code, deployment, evidence`
- Body line 2: `Compare alternatives · recover intent · propose design`
- Body line 3: `Implement or compose a change · draft the later decision record`
- Body line 4: `May help produce understanding, or act as if it already exists`

### 10.4 Forbidden labels on this plate

Do not add: STE, Architecture IR, substrate, Kernel, Runtime, CEM, Concierge, "second consumer" as a node title, autonomy, intelligence, AGI, vendor names.

### 10.5 Node text baselines (authoritative for SVG)

| Column | Stage | Title y | Body y values |
| --- | --- | --- | --- |
| Left/Right | 1 | 192 | 210, 226, 242 |
| Left/Right | 2 | 328 | 346, 362 |
| Left/Right | 3 | 472 | 490, 506, 522, 538 |

Left text x=62; right text x=694.

---

## 11. Typography hierarchy

| Role | Font | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| Header title | Inter, Helvetica Neue, Arial, sans-serif | 20 px | 600 | `#18181B` |
| Plate ID | same | 12 px | 500 | `#71717A` |
| Column title | same | 13 px | 600 | `#27272A` |
| Node title | same | 13 px | 600 | `#18181B` |
| Node body | same | 12 px | 400 | `#3F3F46` |
| Connector side label | same | 11 px | 500 | `#3F3F46` |
| Stage-2 caption | same | 11 px | 400 | `#52525B` |
| Footer line 1 | same | 13 px | 600 | `#18181B` |
| Footer line 2 | same | 12 px | 400 | `#52525B` |

No italics. Column-title underline required (see §2.5).

File encoding: UTF-8 without BOM. Prefer ASCII plus XML entities (`&#183;`) so browsers do not hit encoding errors.

---

## 12. Reproduction checklist

1. Create page 1280x720, grid 8 px, no shadows.
2. Place header, two column frames, footer per §2.
3. Place six stage boxes at absolute positions in §2.4.
4. Enter exact labels from §10; use baselines in §10.5.
5. Add connectors per §6 with marker per §7.
6. Add side labels and captions per §9 (left-of-midline captions; right-of-shaft side labels).
7. Add footer text per §9.3.
8. Apply fills/strokes per §3.
9. Verify Stage 1 to Stage 2 gap is 56 px and shafts are fully visible.
10. Verify Stage 3 height 112 contains all four body lines without clipping.
11. Verify no cross-column arrows and no forbidden labels (§10.4).
12. Save SVG as UTF-8 without BOM; validate XML parse.

---

## 13. SVG layer order (bottom -> top)

1. Canvas background `#FFFFFF`
2. Header band
3. Left and right column frames
4. Stage boxes (Stage 1, then 2, then 3)
5. Footer band chrome
6. Connectors and arrowheads
7. Connector side labels
8. Stage-2 captions
9. Column titles and underlines
10. Node text
11. Header and footer text

---

## 14. Acceptance criteria

The plate is correct if and only if:

1. A reader can state the one-sentence insight after viewing columns left-then-right without reading the essay.
2. Left Stage 3 is recognizably "consumes after closed-enough product."
3. Right Stage 3 is recognizably "enters while work remains open."
4. Closure is annotated as operation-relative, not universal.
5. No STE implementation machinery appears.
6. Stage 1 to Stage 2 arrows show a visible shaft, not a squashed head-only glyph.
7. Stage 3 text is fully inside the box borders.
8. Stage 2 to Stage 3 shafts connect box bottoms to box tops; markers are not reversed.
9. `plate-13-01-A-when-machine-work-begins.svg` matches this document within +/- 8 px.
10. The SVG file is well-formed UTF-8 XML with no encoding error when opened outside the IDE.
