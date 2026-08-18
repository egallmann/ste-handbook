# Plate 13-04-A - Semantic retroactivity: archive unchanged, path changed

**Plate ID:** `13-04-A`  
**Parent work:** `13-04-privacy-has-a-composition-problem.md`  
**Rendered projection:** `plate-13-04-A-semantic-retroactivity.svg` (must match this specification)  
**Status:** Engineering layout specification (canonical). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** A relationship established today can change what information collected yesterday is capable of revealing, without changing the historical information itself.

**Sync rule:** When `plate-13-04-A-semantic-retroactivity.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

**Lettering note:** `13-04-A` assumes this is the first plate embedded in the essay. If an earlier figure ships first, renumber IDs, filenames, captions, and SVG chrome in the same change.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Shared archive band** across the full width, then **two equal columns**. Left = yesterday's traversable path. Right = today's traversable path after one new identity edge. |
| Column width | Each column frame: 584 px (from x=32 and x=664). 24 px gutter. |
| Vertical structure | Header band; shared archive frame; two column frames; shared footer band. |
| Reading frame | Header → shared archive (Vision, then Analytics) → left column top-to-bottom → right column top-to-bottom → footer. |

The two columns are parallel states of the same archive, not a pipeline from left to right. Do not draw an arrow from Yesterday into Today.

Do not show STE stack, RSS, MVC, Kernel, IR, cameras, maps, a stored Erik dossier, or a query being issued. Do not answer when the privacy state changed.

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

### 2.3 Shared archive frame

| Element | Position | Size |
| --- | --- | --- |
| Archive frame | x=32, y=96 | w=1216, h=120 |
| Archive title | x=48, baseline y=120 | left-aligned |
| ACME Vision box | x=48, y=132 | w=568, h=72 |
| ACME Analytics box | x=664, y=132 | w=568, h=72 |

Archive is compressed so the path columns can keep 56 px arrow gaps inside 1280 x 720.

### 2.4 Column frames

| Element | Position | Size |
| --- | --- | --- |
| Left column frame (Yesterday) | x=32, y=228 | w=584, h=312 |
| Right column frame (Today) | x=664, y=228 | w=584, h=312 |

### 2.5 Absolute node positions (authoritative)

Vehicle X and location A share the same y across columns so the only structural difference is the new identity node and edge.

| Node | x, y, w, h |
| --- | --- |
| Left absence caption | 56, 268, 536, 48 |
| Left vehicle X | 168, 372, 312, 48 |
| Left location A | 168, 476, 312, 48 |
| Right permitted source | 680, 268, 104, 48 |
| Right Erik | 832, 268, 312, 48 |
| Right vehicle X | 832, 372, 312, 48 |
| Right location A | 832, 476, 312, 48 |

Right permitted source sits inside the Today frame, left of Erik, with a **48 px** gap (source right x=784; Erik left x=832). That gap is required so the horizontal connector has a visible shaft, not a head-only marker.

Derived edges:

| Edge | Value |
| --- | --- |
| Left vehicle midline x | x=324 |
| Left vehicle bottom | y=420 |
| Left location top | y=476 |
| Right stack midline x | x=988 |
| Right Erik bottom | y=316 |
| Right vehicle top | y=372 |
| Right vehicle bottom | y=420 |
| Right location top | y=476 |
| Source right midpoint | (784, 292) |
| Erik left midpoint | (832, 292) |

Vertical gaps:

| Gap | Clearance | Visible shaft (gap minus 8 px marker) | Purpose |
| --- | --- | --- | --- |
| Left vehicle X to location A | 56 px | 48 px | Solid arrow labeled `observed at` |
| Right Erik to vehicle X | 56 px | 48 px | New amber arrow labeled `associated with` |
| Right vehicle X to location A | 56 px | 48 px | Solid arrow labeled `observed at` (same meaning as left) |

Minimum visible shaft on every connector: **40 px**. Head-only connectors are a defect.

### 2.6 Footer band

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=556 | w=1216, h=132 |
| Footer line 1 | x=640, y=588, `text-anchor=middle` | — |
| Footer line 2 | x=640, y=616, `text-anchor=middle` | — |
| Footer line 3 | x=640, y=644, `text-anchor=middle` | — |
| Footer line 4 | x=640, y=668, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest → lowest):

1. New identity node (`Erik`) and new edge (`associated with`)
2. Shared unchanged archive boxes
3. Yesterday / Today path nodes (`vehicle X`, `location A`)
4. Path arrows
5. Column titles and absence caption
6. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Archive boxes | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Yesterday path node | `#EEF2FF` | `#4338CA` | 1.5 | 8 |
| Today path node (vehicle / location) | `#EEF2FF` | `#4338CA` | 1.5 | 8 |
| New identity (`Erik`) | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Permitted source | `#FFFBEB` | `#D97706` | 1.5 | 8 |
| Archive frame | `#FFFFFF` | `#94A3B8` | 1.5 | 8 |
| Yesterday column frame | `#FFFFFF` | `#CBD5E1` | 1.5 | 8 |
| Today column frame | `#FFFBEB` | `#D97706` | 2 | 8 |
| Header / footer bands | `#F1F5F9` | `#94A3B8` | 1 | 8 |

Today's `vehicle X` and `location A` use the same fill/stroke as Yesterday's matching nodes. They are not restyled as new. Only `Erik`, the permitted source, and the `associated with` arrow carry the "new" treatment.

Do not use gradients, shadows, glow, 3D, icons, or camera/map artwork.

Dark theme (optional CSS `prefers-color-scheme: dark`): remap fills/strokes/text for GitHub dark viewing. Geometry and labels unchanged.

---

## 4. Swimlanes / grouping

| Group | Members | Visual treatment |
| --- | --- | --- |
| Shared archive | ACME Vision, ACME Analytics | Full-width frame; title `The archive did not change` |
| Yesterday | Absence caption, vehicle X, location A, `observed at` arrow | Left frame; title `Yesterday` |
| Today | Permitted source, Erik, vehicle X, location A, both arrows | Right frame (warm stroke); title `Today` |

No third column. No timeline axis across the canvas.

---

## 5. Alignment rules

- Archive boxes share top y=132 and height 72; they sit on one row.
- Both `vehicle X` boxes share top y=372, height 48, width 312.
- Both `location A` boxes share top y=476, height 48, width 312.
- Left vehicle/location left edge x=168; right path stack (Erik, vehicle X, location A) left edge x=832.
- Left stack midline x=324. Right stack midline x=988.
- Vertical path gaps are 56 px. Source-to-Erik horizontal gap is 48 px.
- All boxes snap to 8 px grid.

---

## 6. Connectors

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| c1 | Left vehicle X bottom (324, 420) | Left location A top (324, 476) | Solid, vertical | `observed at` | (324, 420)-(324, 468) |
| c2 | Right permitted source right (784, 292) | Right Erik left (832, 292) | Solid, horizontal, thin | none | (784, 292)-(824, 292) |
| c3 | Right Erik bottom (988, 316) | Right vehicle X top (988, 372) | New, vertical | `associated with` | (988, 316)-(988, 364) |
| c4 | Right vehicle X bottom (988, 420) | Right location A top (988, 476) | Solid, vertical | `observed at` | (988, 420)-(988, 468) |

Shaft ends 8 px above the destination box (or 8 px before the destination side) so the marker tip meets the box edge. After that 8 px reservation, each shaft must still be at least 40 px.

Do not connect Yesterday to Today. Do not connect the archive boxes to the path nodes with arrows; the archive is context, not a fourth graph hop. Do not draw a query, search box, or "issue the traversal" control.

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Solid (historical path) | Triangle 10×8 | `#334155`, 2 px | none |
| New identity edge | Triangle 10×8 | `#B45309`, 2.5 px | none |
| Source to Erik | Triangle 8×6 | `#D97706`, 1.5 px | none |

Marker IDs: `arrow-solid-13-04-A`, `arrow-new-13-04-A`, `arrow-source-13-04-A`.

Edge labels sit **20 px** to the right of vertical shafts (clearance from shaft centerline to the first glyph). Each label has a backing rect in the column fill, 4 px padding around the glyphs, so the shaft does not show through the letters. No horizontal-shaft labels in this plate. 11 px, weight 600. `associated with` uses `#B45309`. `observed at` uses `#334155`.

Label geometry (authoritative):

| Label | Text x, y | Backing rect x, y, w, h | Backing fill |
| --- | --- | --- | --- |
| c1 `observed at` | 344, 448 | 340, 434, 80, 18 | `#FFFFFF` (Yesterday frame) |
| c3 `associated with` | 1008, 344 | 1004, 330, 108, 18 | `#FFFBEB` (Today frame) |
| c4 `observed at` | 1008, 448 | 1004, 434, 80, 18 | `#FFFBEB` (Today frame) |

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `The archive did not change` | x=48, y=120 |
| a2 | `Yesterday` | x=48, y=252 |
| a3 | `Today` | x=680, y=252 |

Absence caption is the left-column body at y=268, not a second title.

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `The archive did not change` |
| Plate ID | `13-04-A` |

### Shared archive

| Node | Exact text (line breaks as shown) |
| --- | --- |
| ACME Vision | `ACME Vision` / `Observations of vehicle X` / `Unchanged` |
| ACME Analytics | `ACME Analytics` / `Candidate relationships among those observations` / `Unchanged` |

### Yesterday

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Absence caption | `The archive did not contain Erik` |
| vehicle X | `vehicle X` |
| location A | `location A` |
| c1 label | `observed at` |

### Today

| Node | Exact text (line breaks as shown) |
| --- | --- |
| Permitted source | `Permitted` / `source` |
| Erik | `Erik` |
| vehicle X | `vehicle X` |
| location A | `location A` |
| c3 label | `associated with` |
| c4 label | `observed at` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `One edge appeared. The historical observation did not become more detailed.` |
| 2 | `Yesterday the path stopped at the vehicle. Today the same observations can participate in a path about Erik.` |
| 3 | `Neither ACME Vision nor ACME Analytics had to become an identity company.` |
| 4 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: `anonymous` or `unresolved` as a verdict, `dossier`, `people` table, `query`, `search box`, `grep`, `RSS`, `MVC-D`, `substrate`, `Kernel`, `IR`, `FinCEN`, `BOI`, camera icons, journalist, private investigator, `fifty observations` as a count badge, `privacy state changed at…`, any STE implementation machinery.

Do not enumerate the essay's example sources (photograph, news report, investigator, public record) as separate nodes. One box: `Permitted` / `source`.

---

## 10. Typography hierarchy

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Plate title | 22 | 600 | `#0F172A` |
| Archive / column titles | 13 | 600 | `#334155` (Today title: `#B45309`) |
| Node primary (`Erik`, `vehicle X`, `location A`) | 16 | 600 | `#0F172A` |
| Archive body / Unchanged | 12 | 400 | `#334155` |
| Absence caption | 13 | 500 | `#64748B` |
| Edge labels | 11 | 600 | see §7 |
| Footer 1–3 | 14 | 500 | `#0F172A` |
| Footer 4 | 12 | 400 | `#64748B` |

Font stack: Inter, "Helvetica Neue", Arial, sans-serif.

---

## 11. Grouping (SVG semantics)

| Group id | Contents |
| --- | --- |
| `plate-header-13-04-A` | Header |
| `plate-archive-13-04-A` | Shared archive frame and two company boxes |
| `plate-yesterday-13-04-A` | Left column boxes and caption |
| `plate-today-13-04-A` | Right column boxes |
| `plate-connectors-13-04-A` | Path arrows and source-to-Erik arrow |
| `plate-footer-13-04-A` | Footer |

---

## 12. Reproduction checklist

1. Draw header, shared archive frame, two column frames, footer.
2. Place Vision and Analytics as equal unchanged archive boxes. No arrows out of the archive.
3. Align `vehicle X` at y=372 and `location A` at y=476 in both columns, with 56 px gaps and visible arrow shafts.
4. Left column has no Erik node; it has the absence caption instead.
5. Right column adds permitted source → Erik (48 px gap) → `associated with` → vehicle X → `observed at` → location A.
6. Yesterday→Today has no connector.
7. Diff labels against Section 9.
8. Validate XML is well-formed UTF-8 (ASCII punctuation preferred).
9. Confirm no connector is head-only (visible shaft >= 40 px).
10. Edge labels sit 20 px right of shafts with 4 px padded backing rects; glyphs do not sit on the line.

---

## 13. SVG layer order (bottom → top)

1. Canvas background  
2. Header / footer  
3. Archive frame + column frames + titles  
4. Archive boxes  
5. Yesterday / Today boxes  
6. Connectors and edge labels  

---

## 14. Acceptance criteria

1. Cold reader can state: the records did not change; one identity edge made a new path traversable.  
2. `vehicle X` and `location A` align across columns and share the yesterday-path styling.  
3. `Erik` and `associated with` are the only new-path emphasis.  
4. No arrow from Yesterday into Today.  
5. No dossier, query, camera, or STE machinery.  
6. Geometry within ±8 px of this document.  
7. Plate-scoped IDs; GitHub-legible at ~640 px width.  
8. Every connector shows a visible shaft of at least 40 px, not only an arrowhead.  
9. Edge labels do not intersect arrow shafts; backing rects keep column fill behind the glyphs.

---

## Notes for later essay embed (not part of the drawing)

Suggested manuscript placement: in **The Archive Changed Without Changing**, immediately after the paragraph that names **semantic retroactivity**, before “That made me reconsider how much comfort…”.

Keep the yesterday/today text graphs in prose. The plate does not replace them.

Suggested caption:

`**Plate 13-04-A.** A relationship established today can change what yesterday's observations can reveal without rewriting the archive. Explanatory projection only; the essay prose is authoritative if figure and text diverge.`

Do not embed until the SVG exists and essay frontmatter `diagrams` remains `true`.
