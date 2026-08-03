# Plate 13-03-A - Lexical miss: nearby hits, related structure unreached

**Plate ID:** `13-03-A`  
**Parent work:** `13-03-the-shape-of-sufficient-context.md`  
**Rendered projection:** `plate-13-03-A-lexical-miss.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** A word search in the active workspace can return a plausible local set and still miss related structure elsewhere when the needed path is relational rather than shared vocabulary.

**Sync rule:** When `plate-13-03-A-lexical-miss.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Three swimlanes.** Left = what the search returned. Middle = the miss named. Right = what the task also needed. Dashed arrows point into the middle lane, then from the middle lane to the unreached boxes. |
| Vertical structure | Header band; three column frames; footer band. |
| Reading frame | Header → left top-to-bottom → middle fail name → right climax then siblings → footer. |

Do not show STE stack, typed substrate graphs, RSS, or MVC-D. Do not use a floating callout pill in the gutter; the middle lane owns the fail naming.

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

Column titles sit at baseline y=120 (about 32 px below the header band bottom at y=88). Content inside frames is offset +20 px from the pre-padding layout (SVG `translate(0,20)` on the content group) so boxes clear the column-title strip.

### 2.4 Absolute node positions (authoritative)

| Node | x, y, w, h |
| --- | --- |
| Task | 48, 128, 368, 64 |
| Word search | 48, 248, 368, 72 |
| Hit A | 48, 376, 112, 80 |
| Hit B | 176, 376, 112, 80 |
| Hit C | 304, 376, 112, 80 |
| Returned-set label band | 48, 480, 368, 48 |
| Fail name (middle) | 480, 248, 192, 160 |
| Miss climax (frontend) | 744, 128, 480, 120 |
| Miss sibling (contract) | 744, 304, 228, 88 |
| Miss sibling (tests) | 996, 304, 228, 88 |
| Why-missed caption box | 744, 416, 480, 104 |

Derived edges:

| Edge | Value |
| --- | --- |
| Task bottom | y=192 |
| Word-search top | y=248 |
| Word-search bottom | y=320 |
| Hits top | y=376 |
| Left stack midline x | x=232 |
| Fail-name center | (576, 328) |
| Middle frame center x | x=576 |

Vertical gaps (left stack):

| Gap | Clearance | Purpose |
| --- | --- | --- |
| Task to word search | 56 px | Vertical arrow with visible tail |
| Word search to hits | 56 px | Vertical arrow with visible tail |

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
2. Miss climax (frontend)
3. Miss siblings
4. Left hits / word search / task
5. Dashed miss arrows
6. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Task | `#EEF2FF` | `#4338CA` | 2 | 8 |
| Word search | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Hit (returned) | `#ECFDF5` | `#047857` | 1.5 | 8 |
| Fail name (middle) | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Miss climax | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Miss sibling | `#FFFBEB` | `#D97706` | 1.5 | 8 |
| Why-missed caption | `#FFF7ED` | `#EA580C` | 1.5 | 8 |
| Left/right frames | `#FFFFFF` | `#CBD5E1` | 1.5 | 8 |
| Middle frame | `#FFFBEB` | `#D97706` | 2 | 8 |
| Header / footer bands | `#F1F5F9` | `#94A3B8` | 1 | 8 |

---

## 4. Swimlanes / grouping

| Group | Members | Visual treatment |
| --- | --- | --- |
| Left: search path | Task, word search, hits, returned-set label | Left frame; title `What the search returned` |
| Middle: the miss | Fail-name box | Middle frame (warm); title `The miss` |
| Right: unreached related | Climax, siblings, why-missed | Right frame; title `What the task also needed` |
| Miss paths | Dashed arrows left→middle and middle→right | Point at the named miss, then at unreached boxes |

---

## 5. Alignment rules

- Left stack boxes share left edge x=48 where full-width; hits share top y=376.
- Stacked solid arrows are vertical at x=232 with 56 px gaps.
- Contract sibling is leftmost on the right lane (x=744); tests sibling is right (x=996).
- Fail-name box is centered in the middle lane.
- All boxes snap to 8 px grid.

---

## 6. Connectors

| ID | From | To | Style | Notes |
| --- | --- | --- | --- | --- |
| c1 | Task bottom (232, 192) | Word search top (232, 248) | Solid, vertical | Visible tail |
| c2 | Word search bottom (232, 320) | Hits top (232, 376) | Solid, vertical | Visible tail |
| c3 | Hits right (416, 416) | Fail-name left (480, 328) | Dashed | Points at the named miss |
| c4 | Fail-name right (672, 280) | Climax left (744, 188) | Dashed | Points at frontend climax |
| c5 | Fail-name right (672, 360) | Leftmost sibling left (744, 348) | Dashed, thinner | Points at Shared data contract (not Tests) |

Do not draw a floating gutter callout. Do not aim c5 at Tests.

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Solid | Triangle 10×8 | `#334155`, 2 px | none |
| Miss (primary) | Filled triangle (no bar) | `#B45309`, 2 px | `8 6` |
| Miss (thin) | Filled triangle (no bar) | `#D97706`, 1.5 px | `8 6` |

Marker IDs: `arrow-solid-13-03-A`, `arrow-miss-13-03-A`.

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `What the search returned` | x=48, y=120 |
| a2 | `The miss` | x=576, y=120, `text-anchor=middle`, warm color |
| a3 | `What the task also needed` | x=736, y=120 |

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `Nearby hits, related structure missed` |
| Plate ID | `13-03-A` |

### Left lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Task | `Task - Backend repo` / `Change a field on the payments API` |
| Word search | `Word search` / `query: "payments API"` / `Looks for matching words` |
| Hit A | `Hit` / `API handler` / `same repo` |
| Hit B | `Hit` / `README` / `same phrase` |
| Hit C | `Hit` / `Ticket` / `same phrase` |
| Returned-set label | `Plausible local set` / `Shared vocabulary in this repo` |

### Middle lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Fail name | `No shared` / `words to follow` / `Word search cannot` / `follow the relationship` |

### Right lane

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Miss climax | `Related, but unreached` / `Frontend consumer` / `Still calls the old field` / `Different repo - different words` |
| Miss sibling (contract) | `Also unreached` / `Shared data contract` / `Other systems depend on it` |
| Miss sibling (tests) | `Also unreached` / `Tests` / `Encode the real obligation` |
| Why-missed caption | `Needed by relationship to the task - consumers,` / `contracts, tests - not by matching the query words.` / `Reminding one example does not fix the class of miss.` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `Local hits can look complete while dependent structure elsewhere never appears.` |
| 2 | `Word search follows vocabulary in the neighborhood it was given. It cannot follow relationships that do not share terms.` |
| 3 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: `grep` as sole title, `RSS`, `MVC-D`, `substrate`, `gene`, `GA`, `Kernel`, `IR`, vendor logos, “just remember the frontend”, invented graph edges, org charts.

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
| `plate-header-13-03-A` | Header |
| `plate-left-13-03-A` | Left lane boxes |
| `plate-mid-13-03-A` | Fail-name box |
| `plate-right-13-03-A` | Right lane boxes |
| `plate-connectors-13-03-A` | Solid vertical arrows |
| `plate-miss-path-13-03-A` | Dashed miss arrows |
| `plate-footer-13-03-A` | Footer |

---

## 12. Reproduction checklist

1. Draw three swimlane frames (left / middle miss / right).
2. Place left stack with 56 px gaps and vertical solid arrows.
3. Place middle fail-name box; no floating gutter pill.
4. Place right climax, leftmost contract sibling, tests sibling, why box.
5. Dashed: hits → miss; miss → climax; miss → leftmost Also-unreached.
6. Diff labels against Section 9.
7. Validate XML is well-formed UTF-8 (ASCII punctuation preferred).

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

1. Cold reader sees three lanes: returned / the miss / also needed.  
2. Fail naming lives in the middle lane, not a pill clipped by boxes.  
3. Stacked left arrows are vertical with visible tails.  
4. Dashed arrows point at the miss, then at climax and the leftmost Also-unreached box.  
5. Siblings + why-box block a “just remind about frontend” reading.  
6. Geometry within ±8 px of this document.  
7. Plate-scoped IDs; no forbidden labels; GitHub-legible at ~640 px width.

---

## Notes for later essay embed (not part of the drawing)

Suggested manuscript placement: after the personal grep paragraph in **Grep was not enough**, before “Once the failure mode had a name…”.

Suggested caption:

`**Plate 13-03-A.** A local word search can look complete while related structure elsewhere — a consumer, a shared contract, tests — never appears. Explanatory projection only; the essay prose is authoritative if figure and text diverge.`

Do not embed until essay frontmatter `diagrams` is set appropriately.
