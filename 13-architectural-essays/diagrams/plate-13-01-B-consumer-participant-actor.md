# Plate 13-01-B - Consumer, participant, actor

**Plate ID:** `13-01-B`  
**Parent work:** `13-01-when-machines-stopped-waiting.md`  
**Rendered projection:** `plate-13-01-B.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Participation is advisory help before or around understanding; becoming an actor is permission to alter architectural or operational state inside authority boundaries, not a capability upgrade.

**Sync rule:** When `plate-13-01-B.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | One horizontal progression: three role cards plus one governance gate between participant and actor. |
| Vertical structure | Header band, main content band, shared footer band. |
| Reading frame | Left to right: Consumer -> Participant -> Gate -> Actor -> footer. |

Do not stack roles vertically. Do not draw a capability or intelligence ladder. The only emphasized transition is the governance gate into Actor.

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
| Consumer role card | 48, 168, 300, 360 |
| Participant role card | 400, 168, 300, 360 |
| Governance gate | 740, 268, 140, 160 |
| Actor role card | 924, 168, 300, 360 |

Derived edges:

| Edge | Value |
| --- | --- |
| Consumer right | x=348 |
| Participant left | x=400 |
| Participant right | x=700 |
| Gate left | x=740 |
| Gate right | x=880 |
| Actor left | x=924 |
| Role card vertical midlines | y=348 |
| Gate vertical midline | y=348 |
| Gate horizontal center | x=810 |

Horizontal gaps:

| Gap | Clearance | Purpose |
| --- | --- | --- |
| Consumer to Participant | 52 px | Full arrow shaft visible |
| Participant to Gate | 40 px | Short shaft into gate |
| Gate to Actor | 44 px | Short shaft out of gate |

### 2.4 Footer band (shared)

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=616 | w=1216, h=72 |
| Footer line 1 | x=640, y=646, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=668, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest -> lowest):

1. Governance gate (distinct fill/stroke; the claim node)
2. Actor role card
3. Participant role card
4. Consumer role card
5. Horizontal connectors and arrowheads
6. Header / footer chrome
7. Role subtitles / body lines

Node size hierarchy:

| Node class | Box size (w x h) | Corner radius |
| --- | --- | --- |
| Role card | 300 x 360 | 8 |
| Governance gate | 140 x 160 | 8 |

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width |
| --- | --- | --- | --- |
| Consumer | `#ECFDF5` | `#047857` | 2 |
| Participant | `#FEF3C7` | `#B45309` | 2.5 |
| Governance gate | `#E8F0FE` | `#1D4ED8` | 3 |
| Actor | `#FEE2E2` | `#B91C1C` | 2.5 |
| Header / footer | `#FAFAFA` | `#D4D4D8` | 1 |
| Canvas | `#FFFFFF` | — | — |

Do not use gradients, shadows, glow, 3D bevels, or icons.

Dark theme (optional CSS `prefers-color-scheme: dark`): remap fills/strokes/text for GitHub dark viewing. Geometry and labels unchanged.

---

## 4. Swimlanes

None. Single horizontal progression only.

---

## 5. Alignment

| Rule | Specification |
| --- | --- |
| Role card tops | All three role cards share y=168 |
| Role card bottoms | All three share y=528 |
| Gate vertical center | Aligned to role card vertical midline (y=348) |
| Text in role cards | Left-aligned; content start x = box.x + 14 |
| Gate text | Centered in gate box (`text-anchor=middle`) |
| Connectors | Horizontal on y=348 |

---

## 6. Connectors

Three horizontal connectors. Straight lines only. No curves. No bidirectional arrows.

| ID | Line coordinates (x1,y1)-(x2,y2) | Meaning |
| --- | --- | --- |
| C1 | (348,348)-(392,348) | Consumer -> Participant |
| C2 | (700,348)-(732,348) | Participant -> Gate |
| C3 | (880,348)-(916,348) | Gate -> Actor |

Shaft ends 8 px before the destination box left edge so the 8 px marker tip meets the box.

Connector style:

| Property | Value |
| --- | --- |
| Stroke | `#3F3F46` |
| Width | 2 px |
| Line type | Solid |
| Arrowhead | SVG marker `arrow-right` (see §7) |
| Labels on C1 | None |
| Labels on C2 / C3 | None (gate body carries the meaning) |

---

## 7. Arrow styles

| Use | Style |
| --- | --- |
| Horizontal succession | Solid 2 px `#3F3F46` with marker-end |
| Bidirectional / dashed / curved | Forbidden |

### 7.1 Marker definition (authoritative)

```
id: arrow-right
viewBox: 0 0 8 8
refX: 8
refY: 4
markerWidth: 8
markerHeight: 8
orient: auto
path: M0,0 L8,4 L0,8 Z
fill: #3F3F46
```

Dark theme: marker path fill `#C9D1D9`.

---

## 8. Grouping

| Group | Contains | Visual treatment |
| --- | --- | --- |
| Consumer card | Title + body lines | Single rounded rectangle |
| Participant card | Title + body lines | Single rounded rectangle |
| Gate | Title + two body lines | Single rounded rectangle; centered text |
| Actor card | Title + body lines | Single rounded rectangle |

Do not nest subgraphs. Do not iconify tools as separate nodes.

---

## 9. Annotations

### 9.1 Footer annotation (exact text)

Centered, two lines:

Line 1: `Participation remains advisory. Actor status is organizational permission to alter state.`  
Line 2: `The gate is a governance distinction, not a claim of greater intelligence or autonomy.`

### 9.2 No side labels on connectors

Gate text is the only transition annotation between Participant and Actor.

---

## 10. Labels (exact node text)

### 10.1 Header

| Field | Exact text |
| --- | --- |
| Title | `Consumer, participant, actor` |
| Plate ID | `Plate 13-01-B` |

### 10.2 Consumer

- Title: `Machine consumer`
- Body line 1: `Closed-enough products for a`
- Body line 2: `bounded operation`
- Body line 3: `Compilers, deployers, policy engines`
- Body line 4: `Formal tools, MBSE, executable architecture`
- Body line 5: `Execute, check, generate, compose, simulate`
- Body line 6: `Does not invent organizational intent`

### 10.3 Participant

- Title: `Computational participant`
- Body line 1: `May consume formal architecture`
- Body line 2: `when present`
- Body line 3: `May help before closed representation`
- Body line 4: `exists`
- Body line 5: `Orientation, assembly, analysis,`
- Body line 6: `validation, recommendation`
- Body line 7: `Remains advisory`

### 10.4 Governance gate

- Title line 1: `Authority`
- Title line 2: `boundaries`
- Body line 1: `Organizational`
- Body line 2: `permission`

### 10.5 Actor

- Title: `Actor`
- Body line 1: `Permitted to alter architectural`
- Body line 2: `or operational state`
- Body line 3: `Inside explicit authority`
- Body line 4: `boundaries`
- Body line 5: `Granted by the organization`
- Body line 6: `Not a capability upgrade`

### 10.6 Forbidden labels on this plate

Do not add: STE, Architecture IR, substrate, Kernel, Runtime, CEM, Concierge, agent framework names, tool chains, autonomy, intelligence, AGI, vendor names, "smarter," ladder rankings.

### 10.7 Node text baselines (authoritative for SVG)

| Node | Title y | Body y values | Text x |
| --- | --- | --- | --- |
| Consumer | 196 | 224, 244, 272, 296, 320, 344 | 62 |
| Participant | 196 | 224, 244, 272, 292, 320, 340, 368 | 414 |
| Actor | 196 | 224, 244, 272, 292, 320, 344 | 938 |
| Gate titles | 320, 338 | — | 810 (`text-anchor=middle`) |
| Gate body | — | 366, 384 | 810 (`text-anchor=middle`) |

Role titles use 14 px semibold. Role body uses 12 px. Gate title 13 px; gate body 12 px.

---

## 11. Typography hierarchy

| Role | Font | Size | Weight | Color |
| --- | --- | --- | --- | --- |
| Header title | Inter, Helvetica Neue, Arial, sans-serif | 20 px | 600 | `#18181B` |
| Plate ID | same | 12 px | 500 | `#71717A` |
| Role title | same | 14 px | 600 | `#18181B` |
| Role body | same | 12 px | 400 | `#3F3F46` |
| Gate title | same | 13 px | 600 | `#1D4ED8` |
| Gate body | same | 12 px | 500 | `#1E3A8A` |
| Footer line 1 | same | 13 px | 600 | `#18181B` |
| Footer line 2 | same | 12 px | 400 | `#52525B` |

No italics. No decorative underlines on role titles.

File encoding: UTF-8 without BOM. Prefer ASCII plus XML entities when needed.

---

## 12. Reproduction checklist

1. Create page 1280x720, grid 8 px, no shadows.
2. Place header and footer per §2.
3. Place three role cards and gate at absolute positions in §2.3.
4. Enter exact labels from §10; use baselines in §10.7.
5. Add connectors per §6 with marker per §7.
6. Apply fills/strokes per §3.
7. Verify gate is the only emphasized transition into Actor.
8. Verify no autonomy/intelligence/STE labels (§10.6).
9. Save SVG as UTF-8 without BOM; validate XML parse.

---

## 13. SVG layer order (bottom -> top)

1. Canvas background `#FFFFFF`
2. Header band
3. Role cards (Consumer, Participant, Actor)
4. Governance gate
5. Footer band chrome
6. Connectors and arrowheads
7. Node text
8. Header and footer text

---

## 14. Acceptance criteria

The plate is correct if and only if:

1. A reader can state the one-sentence insight after reading left to right without the essay.
2. Consumer is recognizably post-closure machine consumption.
3. Participant is recognizably advisory and may work before closure.
4. Actor is reachable only through the governance gate.
5. No intelligence, autonomy, or STE implementation machinery appears.
6. Horizontal shafts are visible (not head-only glyphs).
7. `plate-13-01-B.svg` matches this document within +/- 8 px.
8. The SVG file is well-formed UTF-8 XML.
