# Plate 13-03-B - Graph failure: correct walk, incomplete neighborhood

**Plate ID:** `13-03-B`  
**Parent work:** `13-03-the-shape-of-sufficient-context.md`  
**Rendered projection:** `plate-13-03-B-graph-failure.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** A mechanically correct depth-bounded traversal can assemble a plausible reached subgraph and still miss a required artifact that exists elsewhere when the connecting relationship is missing, stale, disputed, or beyond the declared depth - a familiar incomplete-graph failure under bounded reachability, not an exotic STE pathology.

**Sync rule:** When `plate-13-03-B-graph-failure.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Three swimlanes.** Left = what the walk reached. Middle = the miss named. Right = what still exists outside reach. Dashed arrows point into the middle lane, then from the middle lane to the unreached boxes. |
| Vertical structure | Header band; three column frames; footer band. |
| Reading frame | Header → left top-to-bottom → middle fail name → right beyond-depth box → right absent-edge box → footer. |

Do not show STE stack, MVC-D, secondary resolution, invented edges, or silent graph repair. Do not use a floating callout pill in the gutter; the middle lane owns the fail naming. Prefer essay vocabulary: depth-bounded traversal, reached subgraph, graph failure.

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

### 2.3 Column frames (three swimlanes)

| Element | Position | Size |
| --- | --- | --- |
| Left frame | x=32, y=124 | w=400, h=428 |
| Middle frame (miss) | x=456, y=124 | w=240, h=428 |
| Right frame | x=720, y=124 | w=528, h=428 |

Column titles sit at baseline y=120 (about 32 px below the header band bottom at y=88). Content inside frames is offset +20 px from the pre-padding layout (SVG `translate(0,20)` on the content group).

### 2.4 Absolute node positions (authoritative)

| Node | x, y, w, h |
| --- | --- |
| Task entry | 48, 128, 368, 64 |
| Depth-bounded walk | 48, 248, 368, 72 |
| Reached A (implementation) | 48, 376, 160, 80 |
| Reached B (decision) | 256, 376, 160, 80 |
| Reached-set label band | 48, 480, 368, 48 |
| Fail name (middle) | 480, 248, 192, 160 |
| Unreached A (beyond depth) | 744, 128, 480, 128 |
| Unreached B (absent edge) | 744, 280, 480, 128 |
| Outside-reach label band | 744, 432, 480, 96 |

Derived edges:

| Edge | Value |
| --- | --- |
| Task bottom | y=192 |
| Walk top | y=248 |
| Walk bottom | y=320 |
| Reached top | y=376 |
| Left stack midline x | x=232 |
| Fail-name center | (576, 328) |
| Middle frame center x | x=576 |
| Intra-reached connector | Implementation right (208, 416) to Decision left (256, 416) - 48 px clear gap for visible arrow tail |

Vertical gaps (left stack):

| Gap | Clearance | Purpose |
| --- | --- | --- |
| Task to walk | 56 px | Vertical arrow with visible tail |
| Walk to reached pair | 56 px | Vertical arrow with visible tail |

### 2.5 Footer band

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=576 | w=1216, h=112 |
| Footer line 1 | x=640, y=616, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=648, `text-anchor=middle` | — |
| Footer line 3 | x=640, y=676, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest → lowest):

1. Middle fail-name box
2. Unreached A (beyond depth) and Unreached B (absent edge)
3. Outside-reach label band
4. Left reached pair / walk / task
5. Dashed miss arrows
6. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Task entry | `#EEF2FF` | `#4338CA` | 2 | 8 |
| Depth-bounded walk | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Reached node | `#ECFDF5` | `#047857` | 1.5 | 8 |
| Fail name (middle) | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Unreached class box | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Outside-reach label band | `#FFF7ED` | `#EA580C` | 1.5 | 8 |
| Left/right frames | `#FFFFFF` | `#CBD5E1` | 1.5 | 8 |
| Middle frame | `#FFFBEB` | `#D97706` | 2 | 8 |
| Header / footer bands | `#F1F5F9` | `#94A3B8` | 1 | 8 |

---

## 4. Swimlanes / grouping

| Group | Members | Visual treatment |
| --- | --- | --- |
| Left: reached path | Task entry, walk, reached pair, reached-set label | Left frame; title `What the walk reached` |
| Middle: the miss | Fail-name box | Middle frame (warm); title `The miss` |
| Right: unreached required | Beyond-depth box, absent-edge box, outside-reach label | Right frame; title `What still exists outside reach` |
| Miss paths | Dashed arrows left→middle and middle→right | Point at the named miss, then at unreached boxes |

---

## 5. Alignment rules

- Left stack boxes share left edge x=48 where full-width; reached pair shares top y=376.
- Stacked solid arrows are vertical at x=232 with 56 px gaps.
- Fail-name box is centered in the middle lane.
- Right lane stacks two full-width unreached class boxes (beyond depth, then absent edge), then a label band - matching left-lane density and the Reached / name / detail typography.
- All boxes snap to 8 px grid.
- Do not draw a continuous edge from Decision to Requirement. The miss is the absent hop or depth stop.

---

## 6. Connectors

| ID | From | To | Style | Notes |
| --- | --- | --- | --- | --- |
| c1 | Task bottom (232, 192) | Walk top (232, 248) | Solid, vertical | Visible tail |
| c2 | Walk bottom (232, 320) | Reached pair top (232, 376) | Solid, vertical | Visible tail |
| c3 | Implementation right (208, 416) | Decision left (256, 416) | Solid, horizontal | Credible edge inside reached set; 48 px gap |
| c4 | Decision right (416, 416) | Fail-name left (480, 328) | Dashed | Points at the named miss |
| c5 | Fail-name right (672, 280) | Beyond-depth left (744, 192) | Dashed | Points at beyond-depth class box |
| c6 | Fail-name right (672, 360) | Absent-edge left (744, 344) | Dashed, thinner | Points at absent-edge class box |

Do not draw a floating gutter callout. Do not draw an invented Decision→Requirement edge.

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Solid | Triangle 10×8 | `#334155`, 2 px | none |
| Miss (primary) | Filled triangle (no bar) | `#B45309`, 2 px | `8 6` |
| Miss (thin) | Filled triangle (no bar) | `#D97706`, 1.5 px | `8 6` |

Marker IDs: `arrow-solid-13-03-B`, `arrow-miss-13-03-B`.

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `What the walk reached` | x=48, y=120 |
| a2 | `The miss` | x=576, y=120, `text-anchor=middle`, warm color |
| a3 | `What still exists outside reach` | x=736, y=120 |

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `Correct traversal, incomplete neighborhood` |
| Plate ID | `13-03-B` |

### Left lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Task entry | `Task entry` / `Change a field on the payments API` |
| Depth-bounded walk | `Depth-bounded traversal` / `Follow credible relationships` / `Stop at declared depth` |
| Reached A | `Reached` / `Implementation` / `API handler` |
| Reached B | `Reached` / `Decision` / `ADR on the field` |
| Reached-set label | `Assembled reached subgraph` / `Walk was mechanically correct` |

### Middle lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Fail name | `Graph failure` / `Familiar incomplete-graph case` / `Absent edge or beyond depth` / `Walk cannot invent a path` |

### Right lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Unreached A (beyond depth) | `Unreached` / `Beyond declared depth` / `Frontend consumer` / `Needed - path sits past the bound` |
| Unreached B (absent edge) | `Unreached` / `Absent edge` / `Requirement` / `In the available tree - no hop from Decision` |
| Outside-reach label band | `Same visible miss: needed, present, not in the packet` / `Absent edge or beyond depth. Do not invent a path.` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `Incomplete graphs under bounded reachability routinely leave required structure outside the packet.` |
| 2 | `Graph failure names that familiar case: correct walk, incomplete neighborhood - not permission to rewrite the graph.` |
| 3 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: `MVC-D`, `secondary resolution`, `independently resolved`, `gene`, `GA`, `Kernel`, `IR`, vendor logos, invented Decision→Requirement edges, silent repair, production claim that recovery is already shipping, `grep` as sole title.

Prefer `depth-bounded traversal` over productizing `RSS` in node titles. `RSS` must not appear as a claim that current runtime already mitigates graph failure.

---

## 10. Typography hierarchy

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Plate title | 22 | 600 | `#0F172A` |
| Column titles | 13 | 600 | `#334155` (middle: `#B45309`) |
| Fail-name primary | 15 | 600 | `#0F172A` |
| Climax primary | 15 | 600 | `#0F172A` |
| Body / secondary | 11–12 | 400 | `#334155` |
| Footer 1–2 | 14 | 500 | `#0F172A` |
| Footer 3 | 12 | 400 | `#64748B` |

Font stack: Inter, "Helvetica Neue", Arial, sans-serif.

---

## 11. Grouping (SVG semantics)

| Group id | Contents |
| --- | --- |
| `plate-header-13-03-B` | Header |
| `plate-left-13-03-B` | Left lane boxes |
| `plate-mid-13-03-B` | Fail-name box |
| `plate-right-13-03-B` | Right lane boxes |
| `plate-connectors-13-03-B` | Solid arrows (vertical + intra-reached) |
| `plate-miss-path-13-03-B` | Dashed miss arrows |
| `plate-footer-13-03-B` | Footer |

---

## 12. Reproduction checklist

1. Draw three swimlane frames (left / middle miss / right).
2. Place left stack with 56 px gaps and vertical solid arrows.
3. Place horizontal solid edge between Implementation and Decision only.
4. Place middle fail-name box; no floating gutter pill.
5. Place right beyond-depth box, absent-edge box, then outside-reach label band.
6. Dashed: Decision → miss; miss → beyond-depth; miss → absent-edge.
7. Confirm no Decision→Requirement edge is drawn.
8. Diff labels against Section 9.
9. Validate XML is well-formed UTF-8 (ASCII punctuation preferred).

---

## 13. SVG layer order (bottom → top)

1. Canvas background  
2. Header / footer  
3. Three frames + column titles  
4. Left, middle, right boxes  
5. Solid connectors  
6. Dashed miss connectors  

---

## 14. Acceptance criteria

1. Cold reader sees three lanes: reached / the miss / outside reach.  
2. Fail naming lives in the middle lane, not a pill clipped by boxes.  
3. Stacked left arrows are vertical with visible tails; Implementation↔Decision has one solid hop.  
4. Right lane has two concrete unreached class boxes (beyond depth; absent edge) with Reached-mirrored typography.  
5. Label band states the shared visible miss without inventing a path.  
6. No invented edge to Requirement.  
7. Geometry within ±8 px of this document.  
8. Plate-scoped IDs; no forbidden labels; GitHub-legible at ~640 px width.

---

## Notes for later essay embed (not part of the drawing)

Suggested manuscript placement: in **From substrate to RSS**, after “That is a graph failure.” and before “Pretending the graph is complete…”.

Suggested caption:

`**Plate 13-03-B.** A correct depth-bounded walk can miss needed structure that exists elsewhere - beyond the declared depth, or across an absent edge in the available tree. Explanatory projection only; the essay prose is authoritative if figure and text diverge.`

Do not embed until ready for revision sign-off. Do not claim MVC-D mitigation on this plate (that is Plate 13-03-C).
