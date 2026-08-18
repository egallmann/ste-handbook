# Plate 13-03-C - Expected shape without inventing the edge

**Plate ID:** `13-03-C`  
**Parent work:** `13-03-the-shape-of-sufficient-context.md`  
**Rendered projection:** `plate-13-03-C-expected-shape-no-invented-edge.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Under a loaded MVC-D, ordinary depth-bounded traversal is validated against the expected shape; gaps trigger a second bounded supplemental traversal - same task, same expected shape, same depth discipline - that can reach missing context the primary walk could not, as independently resolved or unresolved packets, without inventing an authoritative graph edge.

**Sync rule:** When `plate-13-03-C-expected-shape-no-invented-edge.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Three swimlanes.** Left = primary ordinary walk under expectation. Middle = MVC-D validation. Right = supplemental walk that **repeats the left stack** (task entry, expected shape, depth-bounded) and then reaches context the primary walk missed. |
| Vertical structure | Header band; three column frames; footer band. |
| Reading frame | Header → left stack → middle validation → right mirrored stack → newly reached packets → footer. |

This plate is a **near-term direction**, not a claim that current RSS already ships MVC-D mitigation. Do not invent a Decision→Requirement edge. Prefer essay vocabulary: expected shape, validation, supplemental traversal, independently resolved, unresolved.

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
| Middle frame (validation) | x=456, y=124 | w=240, h=428 |
| Right frame | x=720, y=124 | w=528, h=428 |

Column titles sit at baseline y=120 (about 32 px below the header band bottom at y=88). Content inside frames is offset +20 px from the pre-padding layout (SVG `translate(0,20)` on the content group).

### 2.4 Absolute node positions (authoritative)

**Left (primary walk):**

| Node | x, y, w, h |
| --- | --- |
| Task entry | 48, 128, 368, 48 |
| MVC-D expected shape (purple) | 48, 188, 368, 72 |
| Depth-bounded walk | 48, 276, 368, 48 |
| Reached A (implementation) | 48, 344, 160, 72 |
| Reached B (decision) | 256, 344, 160, 72 |
| Reached-set label band | 48, 432, 368, 40 |

**Middle:**

| Node | x, y, w, h |
| --- | --- |
| Validation box | 468, 208, 216, 240 |

**Right (supplemental walk - mirrors left, then new reaches):**

| Node | x, y, w, h |
| --- | --- |
| Task entry (supp) | 744, 128, 480, 48 |
| MVC-D expected shape (supp, purple) | 744, 188, 480, 72 |
| Depth-bounded walk (supp) | 744, 276, 480, 40 |
| New reach A (Requirement) | 744, 332, 480, 72 |
| New reach B (Frontend) | 744, 420, 480, 64 |
| Supplemental label band | 744, 500, 480, 32 |

Derived:

| Edge | Value |
| --- | --- |
| Left intra-reached | Implementation right (208, 380) to Decision left (256, 380) - 48 px |
| Validation center | (576, 328) |

No vertical arrows in left/right stacks (compact). Solid only on left Implementation→Decision. Dashed: left → validation → right supplemental stack / new reaches.

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

1. Purple expected-shape boxes (both lanes) and middle validation
2. Right newly reached packets (Requirement / Frontend)
3. Left primary reached pair
4. Task / depth-bounded boxes on both sides
5. Dashed validation arrows
6. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Task entry | `#EEF2FF` | `#4338CA` | 2 | 8 |
| MVC-D expected shape | `#F5F3FF` | `#6D28D9` | 2 | 8 |
| Depth-bounded walk | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Primary reached | `#ECFDF5` | `#047857` | 1.5 | 8 |
| Validation (middle) | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Independently resolved packet | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Unresolved packet | `#F8FAFC` | `#64748B` | 1.5 | 8 |
| Label bands | `#F8FAFC` / `#FFF7ED` | `#94A3B8` / `#EA580C` | 1 / 1.5 | 8 |
| Frames / header / footer | as Plates A/B | — | — | 8 |

---

## 4. Swimlanes / grouping

| Group | Members | Visual treatment |
| --- | --- | --- |
| Left: primary walk | Task, purple expected, depth-bounded, Impl+Decision, label | `Ordinary walk under expectation` |
| Middle: validation | Validation box | `MVC-D validation` |
| Right: supplemental walk | Same stack as left, then Requirement + Frontend as newly reached | `Supplemental traversal (bounded)` |

Right is intentionally the left box grammar again: task → expected shape → depth-bounded → reaches. The difference is **what** it reaches.

---

## 5. Alignment rules

- Left and right share the same vertical rhythm for task / expected / walk (y=128 / 188 / 276).
- Right newly reached packets stack full-width under the mirrored walk (Requirement, then Frontend) so each gets a clean left-edge dashed arrow.
- No solid Decision→Requirement edge.
- All boxes snap to 8 px grid.

---

## 6. Connectors

| ID | From | To | Style | Notes |
| --- | --- | --- | --- | --- |
| c1 | Implementation right (208, 380) | Decision left (256, 380) | Solid | Primary credible hop |
| c2 | Decision right (416, 380) | Validation left (468, 328) | Dashed | Primary result enters validation |
| c3 | Validation right (684, 268) | Supp task left (744, 152) | Dashed | Triggers supplemental stack |
| c4 | Validation right (684, 340) | Requirement left (744, 368) | Dashed | Newly reached via supplemental |
| c5 | Validation right (684, 400) | Frontend left (744, 452) | Dashed, thinner | Unresolved after supplemental; full-width stack so arrow does not cross Requirement |

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Solid | Triangle 10×8 | `#334155`, 2 px | none |
| Dashed primary | Filled triangle | `#B45309`, 2 px | `8 6` |
| Dashed thin | Filled triangle | `#D97706`, 1.5 px | `8 6` |

Marker IDs: `arrow-solid-13-03-C`, `arrow-miss-13-03-C`.

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `Ordinary walk under expectation` | x=48, y=120 |
| a2 | `MVC-D validation` | x=576, y=120, `text-anchor=middle`, warm |
| a3 | `Supplemental traversal (bounded)` | x=736, y=120 |

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `Expected shape without inventing the edge` |
| Plate ID | `13-03-C` |

### Left lane

| Node | Exact text |
| --- | --- |
| Task entry | `Task entry` / `Change a field on the payments API` |
| MVC-D expected shape | `MVC-D expected shape` / `Implementation - Decision - Requirement` / `Frontend consumer` |
| Depth-bounded walk | `Depth-bounded traversal` / `Stop at declared depth` |
| Reached A | `Reached` / `Implementation` / `API handler` |
| Reached B | `Reached` / `Decision` / `ADR on the field` |
| Label | `Primary walk returned these` |

### Middle lane

| Node | Exact text |
| --- | --- |
| Validation | `MVC-D validation` / `Compare expected` / `shape vs realized` / `Gap: Domain -` / `Requirement, Frontend` / `Trigger supplemental walk` / `Near-term direction` |

### Right lane

| Node | Exact text |
| --- | --- |
| Task entry (supp) | `Task entry` / `Same task - same declaration` |
| MVC-D expected shape (supp) | `MVC-D expected shape` / `Same loaded definition` / `Gaps still required` |
| Depth-bounded walk (supp) | `Depth-bounded traversal` / `Still bounded - gap-directed` |
| New reach A | `Independently resolved` / `Requirement` / `Primary walk could not reach` |
| New reach B | `Unresolved` / `Frontend consumer` / `Still no qualifying material` |
| Label | `New context for gaps - not an invented graph edge` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `Supplemental traversal repeats task, expected shape, and depth bound - then reaches context the primary walk missed.` |
| 2 | `Independently resolved is not graph-connected. Unresolved stays unresolved. Near-term direction - not current RSS.` |
| 3 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: production MVC-D-in-RSS claim, invented Decision→Requirement edges, unbounded supplemental crawl, silent repair, `gene`, `GA`, `Kernel`, `IR`, vendor logos.

---

## 10. Typography hierarchy

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Plate title | 22 | 600 | `#0F172A` |
| Column titles | 13 | 600 | `#334155` (middle: `#B45309`) |
| Primary / validation | 13–14 | 600 | `#0F172A` |
| Secondary | 11–12 | 400 | `#334155` |
| Small labels | 11 | 500 | `#334155` |
| Footer 1–2 | 13–14 | 500 | `#0F172A` |
| Footer 3 | 12 | 400 | `#64748B` |

Font stack: Inter, "Helvetica Neue", Arial, sans-serif.

---

## 11. Grouping (SVG semantics)

| Group id | Contents |
| --- | --- |
| `plate-header-13-03-C` | Header |
| `plate-left-13-03-C` | Primary walk |
| `plate-mid-13-03-C` | Validation |
| `plate-right-13-03-C` | Supplemental mirrored walk + new reaches |
| `plate-connectors-13-03-C` | Solid primary hop |
| `plate-miss-path-13-03-C` | Dashed validation/supplemental paths |
| `plate-footer-13-03-C` | Footer |

---

## 12. Reproduction checklist

1. Three frames + column titles.
2. Left stack: task, purple expected, depth-bounded, Impl+Decision, label.
3. Middle validation box.
4. Right stack mirrors left (task, purple expected, depth-bounded), then Requirement + Frontend as newly reached.
5. Solid only Implementation→Decision on left.
6. Dashed left→validation→right.
7. No Decision→Requirement solid edge.
8. Diff Section 9 labels; validate UTF-8 XML.

---

## 13. SVG layer order (bottom → top)

1. Canvas background  
2. Header / footer  
3. Frames + titles  
4. Boxes  
5. Solid connectors  
6. Dashed connectors  

---

## 14. Acceptance criteria

1. Right column visibly repeats left grammar: task / expected shape / depth-bounded.  
2. Right then shows context primary walk could not reach (Requirement independently resolved; Frontend unresolved).  
3. Middle is MVC-D validation that triggers the supplemental walk.  
4. Purple expected-shape boxes on both left and right.  
5. No invented authoritative edge; near-term marked.  
6. Geometry within ±8 px; plate-scoped IDs; GitHub-legible at ~640 px.

---

## Notes for later essay embed (not part of the drawing)

Suggested placement: **Near-term RSS enhancement**, after the four-state block.

Suggested caption:

`**Plate 13-03-C.** MVC-D validation triggers a second bounded walk - same task, same expected shape, same depth discipline - that can reach missing context the primary walk could not, without inventing an authoritative edge. Near-term direction; explanatory projection only; the essay prose is authoritative if figure and text diverge.`

Do not embed until review sign-off.
