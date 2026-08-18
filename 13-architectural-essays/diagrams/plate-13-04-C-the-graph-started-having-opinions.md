# Plate 13-04-C - The graph started having opinions

**Plate ID:** `13-04-C`  
**Parent work:** `13-04-privacy-has-a-composition-problem.md`  
**Rendered projection:** `plate-13-04-C-the-graph-started-having-opinions.svg`  
**Status:** Engineering layout specification (canonical, revised). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Morality Guard manufactures moralized and association-based judgments from a joined graph of records, signals, places, and other people, condenses them into an operational class, and Real-Time Security can watch that class continuously under a safety justification without anyone typing a name.

**Sync rule:** When `plate-13-04-C-the-graph-started-having-opinions.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

**Lettering note:** `13-04-C` assumes this plate embeds after `13-04-B`. Plate B is the richer neutral join. This plate starts after that join exists and shows judgment, condensation, and deployment. If embed order changes, renumber IDs, filenames, captions, and SVG chrome in the same change.

**Dependence on Plate B:** Assume the richer join already exists. Do not redraw Erik as a join point. Do not climax on traversable inventory. The subject here is what a classifier can manufacture from that graph and how “safety” can subscribe to the result.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Four zones.** Left = what the world exposes. Mid-left = join and inference machinery. Mid-right = manufactured profiles and condensed class. Right = safety-style deployment. |
| Zone frames | Zone 1 x=32 w=216; Zone 2 x=264 w=240; Zone 3 x=520 w=488; Zone 4 x=1024 w=224. 16 px gutters. Zone 3 is wider so profile shafts can sit in an 80 px column gap instead of wrapping the frame. |
| Vertical structure | Header band; four zone frames; footer band. |
| Reading frame | Header → ordinary sources (including signals and other people) → Enrichment → Intelligence → Morality Guard → first-order and association judgments → condensed class → subscribers / standing watch / live alert / quiet intervention → footer. |

This is the **vile plate**. It must remain **clean, legible, and architectural**. The disgust comes from labels, graph logic, and the activation path, not from scary styling.

The four-stage progression must be unmistakable:

1. ordinary-looking source material can be joined
2. Morality Guard manufactures ugly profile claims from that graph
3. those claims condense into an operational class
4. that class drives real-time watch behavior, alerts, and quiet intervention

Do not turn this into another neutral composition diagram. Do not stop at “the graph is rich.” The plate must show **moralized inference**, **profile condensation**, and **real-time subscriber activation**.

Do not show cameras, maps, dossiers, search-box UI, facial recognition, STE stack, Holdings, BOI, Shepherd’s Keeper, government seals, sirens, warning triangles, flames, or logos.

Do not imply hacked devices, intercepted communications, defeated encryption, or a radio fingerprint that identifies a natural person.

---

## 2. Spatial arrangement

### 2.1 Coordinate system

Origin: top-left of canvas. Units: pixels. Snap: 8 px grid.

### 2.2 Full-width header band

| Element | Position | Size |
| --- | --- | --- |
| Header band | x=32, y=32 | w=1216, h=56 |
| Plate title | x=48, baseline y=68 | left-aligned |
| Plate ID | x=1232, baseline y=66, `text-anchor=end` | right-aligned |

### 2.3 Zone frames

| Element | Position | Size |
| --- | --- | --- |
| Zone 1 frame | x=32, y=104 | w=216, h=456 |
| Zone 2 frame | x=264, y=104 | w=240, h=456 |
| Zone 3 frame | x=520, y=104 | w=488, h=456 |
| Zone 4 frame | x=1024, y=104 | w=224, h=456 |

Zone titles at baseline y=128. All nodes remain inside their zone frames. Real-Time Security bottom y=556; zone frame bottom y=560. Do not overflow into the footer.

### 2.4 Absolute node positions (authoritative)

#### Zone 1: what the world exposes

Seven ordinary-looking source boxes. Height 48, vertical gap 8. The vile classifier is not working from one creepy source; it is working from a normal-looking ecosystem.

| Node | x, y, w, h |
| --- | --- |
| Plate / asset observations | 44, 148, 188, 48 |
| Observable signals | 44, 204, 188, 48 |
| Property / deed / LLC records | 44, 260, 188, 48 |
| Court / arrest / divorce dockets | 44, 316, 188, 48 |
| Social / public web traces | 44, 372, 188, 48 |
| People-search / broker context | 44, 428, 188, 48 |
| Other-people / household associations | 44, 484, 188, 48 |

Last source bottom y=532. Source right edge x=232. Collector bus at x=256 in the Zone 1/2 gutter.

Radio/signal material is conservative substrate, not interception. Permitted substrate vocabulary on this plate: `Observable signal`, `recurring proximity`, `co-occurrence`. Do not place `Later associated with` or `Repeatedly observed near` as Zone 3 opinions; those are Plate B relationship labels. Here they are implied by the signal and other-people source boxes feeding Enrichment.

#### Zone 2: join and inference machinery

| Node | x, y, w, h | Role |
| --- | --- | --- |
| ACME Enrichment | 304, 160, 176, 72 | Join identity, context, people, vehicles, signals, and records |
| ACME Intelligence | 304, 268, 176, 72 | Traverse, correlate, and assemble graph paths |
| Morality Guard | 296, 372, 192, 88 | Manufacture judgmental and association-based profile claims |
| ACME Real-Time Security | 296, 492, 192, 64 | Operationalize those claims into standing watches and alerts |

**Morality Guard is the vile classifier.** It must read that way from structure and labeling, not from theatrical styling.

Gaps: Enrichment bottom 232 → Intelligence 268 (36 px); Intelligence bottom 340 → Morality Guard 372 (32 px); Morality Guard bottom 460 → Real-Time 492 (32 px). Real-Time bottom 556. Center x=392.

#### Zone 3: what the graph can now say about you

Two-column grid. Left column = first-order habit claims plus the absurd moralizing score. Right column = association / guilt-by-graph claims plus the sanitized euphemism. Bottom = condensed deployable class.

Column headers (not boxes) at baseline y=146:

| Header | x | Anchor |
| --- | --- | --- |
| `First-order claims` | 640 | middle |
| `Association claims` | 880 | middle |

| Node | x, y, w, h | Layer |
| --- | --- | --- |
| Likely affair | 560, 172, 160, 48 | First-order |
| Associates with high-concern people | 800, 172, 160, 48 | Association |
| Gambling pattern | 560, 236, 160, 48 | First-order |
| Household linked to flagged person | 800, 236, 160, 48 | Association |
| Godliness score: 37 | 560, 300, 160, 56 | Absurd moralizing label |
| Behavioral suitability: LOW | 800, 300, 160, 56 | Sanitized euphemism |
| High concern person | 672, 420, 176, 72 | Condensed operational class |

Horizontal gap between columns: 80 px (560+160=720 → 800). Column centers: 640 and 880. Shared center spine x=760. Vertical gaps: 16 px, then 16 px, then 64 px to the condensed class.

Do not wrap a bus around the Zone 3 frame. Feed the grid from a left rail at x=528 and a center spine at x=760 in the column gap. The top crossbar travels at y=158, above the boxes (top y=172) and below the column headers (y=146).

`Godliness score: 37` and `Behavioral suitability: LOW` sit on the same row to show that renaming the output does not change the operation. `Godliness score` is an intentionally revealing example, not the whole point of the plate. `High concern person` is the class that can be watched.

Association nodes are mandatory. The evil is not only scored habits; the graph can score the people around someone and then score that person because of them.

#### Zone 4: how “safety” deploys it

| Node | x, y, w, h |
| --- | --- |
| Real-time subscribers | 1036, 164, 200, 76 |
| Quiet intervention | 1036, 256, 200, 64 |
| Live area alert | 1036, 344, 200, 72 |
| Standing conditions | 1036, 440, 200, 104 |

Stack order (top → bottom): subscribers, quiet intervention, live area alert, standing conditions. The deployment cascade matches that upward read: standing conditions → live area alert → quiet intervention. Each cascade shaft is centered on the nodes (x=1136) and spans only the 24 px gap between adjacent boxes. Standing sits at the bottom and receives Real-Time on one horizontal shaft at y=524.

Gaps: 16 px between subscribers and quiet; 24 px between quiet, live, and standing. Standing bottom y=544. Zone 4 frame bottom y=560. Center x=1136. Cascade spine x=1136.

Subscribers watch people, vehicles, profile classes, and graph-neighborhoods. Standing conditions are predicates, not name lookups. The live alert exists because the condition matched, not because anyone typed a name.

### 2.5 Footer band

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=576 | w=1216, h=112 |
| Footer line 1 | x=640, baseline y=608, `text-anchor=middle` | — |
| Footer line 2 | x=640, baseline y=632, `text-anchor=middle` | — |
| Footer authority line | x=640, baseline y=664, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest → lowest):

1. Morality Guard and Zone 3 judgments
2. `High concern person`
3. Zone 4 standing watch and activation
4. Enrichment and Intelligence
5. Zone 1 source material
6. Connectors
7. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Source material | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Enrichment / Intelligence / Real-Time | `#EEF2FF` | `#4338CA` | 1.5 | 8 |
| Morality Guard | `#FEE2E2` | `#B91C1C` | 2.5 | 8 |
| First-order / association profile outputs | `#FEF2F2` | `#DC2626` | 1.5 | 8 |
| Godliness / suitability pair | `#FEF2F2` | `#B91C1C` | 2 | 8 |
| High concern person | `#FECACA` | `#B91C1C` | 2.5 | 8 |
| Activation nodes | `#FFF7ED` | `#C2410C` | 1.5 | 8 |
| Zone 1 / 2 frames | `#FFFFFF` | `#CBD5E1` | 1.5 | 8 |
| Zone 3 frame | `#FEF2F2` | `#DC2626` | 2 | 8 |
| Zone 4 frame | `#FFF7ED` | `#C2410C` | 2 | 8 |
| Header / footer | `#F1F5F9` | `#94A3B8` | 1 | 8 |

Do not use gradients, shadows, icons, sirens, warning triangles, flames, maps, cameras, or comic villain styling. Red/warm fills mark inference and activation, not decoration.

---

## 4. Zone semantics

| Zone | Members | Visual treatment |
| --- | --- | --- |
| Zone 1 | seven source boxes: observations, signals, property records, court dockets, public web, people-search, other-people / household associations | Cool frame; title `What the world exposes` |
| Zone 2 | Enrichment, Intelligence, Morality Guard, Real-Time | Neutral frame; title `Join, infer, operationalize` |
| Zone 3 | two first-order claims, two association claims, godliness/suitability pair, condensed class | Red-tinted frame; title `What the graph can now say about you` |
| Zone 4 | subscribers, quiet intervention, live alert, standing conditions | Warm frame; title `How “safety” deploys it` |

No Holdings. No Shepherd’s Keeper. No BOI. No Plate B inventory aesthetic as the climax. No Erik node.

---

## 5. Alignment rules

- Zone 1 source boxes share x=44, width 188, height 48, and 8 px vertical gaps.
- Zone 2 uses a vertical stack with 36 px, 32 px, and 32 px gaps as specified in 2.4. Enrichment and Intelligence share x=304 and width 176. Morality Guard and Real-Time share x=296 and width 192. All four share center x=392.
- Zone 3 column headers sit at x=640 and x=880, baseline y=146.
- Zone 3 columns share left edges x=560 and x=800 and width 160, with an 80 px gap.
- Rows 1–2 share height 48. The godliness/suitability row shares height 56.
- `High concern person` is centered on x=760 (x=672, width 176).
- Zone 4 uses a vertical stack with 16 px gaps.

---

## 6. Connectors

### 6.1 Source material into Enrichment

Sources feed a collector bus, then one trunk enters Enrichment. Do not draw seven arrowheads onto the Enrichment left edge.

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| s1–s7 | Source right (232, cy) | Collector (256, cy) | Solid slate, no marker | none | 24 px stubs at y=172, 228, 284, 340, 396, 452, 508 |
| spine | Collector | Collector | Solid slate, no marker | none | (256, 172)-(256, 508) |
| t1 | Collector | Enrichment left (304, 196) | Solid slate | none | (256, 196)-(296, 196) |

Visible trunk shaft: 40 px. Do not draw Zone 1 arrows into Morality Guard. Sources feed Enrichment only.

### 6.2 Internal system flow

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| f1 | Enrichment bottom (392, 232) | Intelligence top (392, 268) | Solid blue | `joined context` | (392, 232)-(392, 260) |
| f2 | Intelligence bottom (392, 340) | Morality Guard top (392, 372) | Solid red | `inferred relationships` | (392, 340)-(392, 364) |
| f3 | Morality Guard bottom (392, 460) | Real-Time Security top (392, 492) | Solid red | `operationalize` | (392, 460)-(392, 484) |

Visible shafts: f1 28 px, f2 24 px, f3 24 px. Labels sit to the right of the shafts.

### 6.3 Morality Guard to profile outputs

Do not wrap a bus around the Zone 3 perimeter. Use a left rail in the Zone 3 padding and a center spine in the 80 px column gap. The top crossbar stays above the boxes.

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| bus | Morality Guard right (488, 400) | Center spine | Solid red, no end marker | none | (488, 400)-(528, 400)-(528, 158)-(760, 158)-(760, 328) |
| p1 | Left rail (528, 196) | Likely affair left (560, 196) | Solid red | none | (528, 196)-(552, 196) |
| p3 | Left rail (528, 260) | Gambling left (560, 260) | Solid red | none | (528, 260)-(552, 260) |
| p5 | Left rail (528, 328) | Godliness left (560, 328) | Solid red | none | (528, 328)-(552, 328) |
| p2 | Center spine (760, 196) | Associates left (800, 196) | Solid red | none | (760, 196)-(792, 196) |
| p4 | Center spine (760, 260) | Household left (800, 260) | Solid red | none | (760, 260)-(792, 260) |
| p6 | Center spine (760, 328) | Suitability left (800, 328) | Solid red | none | (760, 328)-(792, 328) |
| p7 | Morality Guard right (488, 440) | High concern left (672, 456) | Solid red | `condense` | (488, 440)-(664, 456) |

p1–p6 shafts are 24–32 px. p7 exits Morality Guard on the right edge above the profile-feed bus (y=400) and above the operationalize drop (y=460), then runs into High concern at cy=456.

### 6.4 Profiles into condensed classification

Dashed red U-bracket under both columns, including the association column. No duplicate spines on the solid rail.

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| d-bracket | Left column bottom-center (640, 356) | Right column bottom-center (880, 356) | Dashed red, no marker | none | (640, 356)-(640, 388)-(760, 388)-(880, 388)-(880, 356) |
| d-in | Bracket (760, 388) | High concern top (760, 420) | Dashed red | none | (760, 388)-(760, 412) |

Visible condensation shaft: 24 px. Both first-order and association columns participate through the bracket legs.

High concern geometry: left 672, right 848, top 420, bottom 492, cy 456.

### 6.5 Activation path

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| a1 | High concern right (848, 456) | Subscribers left (1036, 202) | Dashed orange | none | bus (848, 456)-(988, 456)-(988, 202); arrow (988, 202)-(1028, 202) |
| a2 | Real-Time right (488, 524) | Standing conditions left (1036, 524) | Solid orange | `watch people, vehicles, classes, or 2-hop neighborhoods` | bus (488, 524)-(1028, 524); arrow (1028, 524)-(1036, 524) |
| a3 | Standing conditions top (1136, 440) | Live area alert bottom (1136, 416) | Solid orange | none | (1136, 440)-(1136, 424) |
| a4 | Live area alert top (1136, 344) | Quiet intervention bottom (1136, 320) | Solid orange | none | (1136, 344)-(1136, 328) |

a1 and a2 use separate spines: a1 vertical at x=988 inside Zone 3; a2 is a single horizontal run at Real-Time center y=524 into Standing conditions on the Zone 4 left edge. a3 and a4 are short upward hops at x=1136 (node center) through the gaps between standing → live → quiet. Only terminal segments carry arrowheads.

a3 and a4 each span one 24 px inter-box gap (16 px visible shaft plus 8 px clearance). The standing-condition and intervention node copy carry the meaning.

Do not draw Zone 1 into Zone 4. Do not draw profile nodes directly to subscribers; they condense through `High concern person`, except that Real-Time can independently feed standing conditions.

Shafts end 8 px before the destination edge. Arrowheads use `refX=9` markers so the tip meets the gap and the shaft does not run through the head. Head-only connectors are a defect except a3 and a4.

### 6.6 Connector label positions

| ID | Exact text | Anchor | x, y |
| --- | --- | --- | --- |
| f1 | `joined context` | start | 404, 248 |
| f2 | `inferred relationships` | start | 404, 356 |
| f3 | `operationalize` | start | 404, 476 |
| p7 | `condense` | start | 544, 436 |
| a2 | `watch people, vehicles, classes, or 2-hop neighborhoods` | middle | 758, 512 |

Do not label a3 or a4. Standing-condition and intervention node copy already states `notify if…` and `attention, denial, rerouting, scrutiny`.

Relationship / inference labels: `#7F1D1D`. Activation labels: `#9A3412`. Labels use transparent background (no backing rects) and sit 8–20 px off the shaft. a2 uses a single centered line above its horizontal shaft (540 px corridor).

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Source / assembly | Triangle 9×7 (`refX=9`) | `#334155` or `#4338CA` | none |
| Vile inference | Triangle 9×7 (`refX=9`) | `#B91C1C` | none |
| Condensed classification | Triangle 9×7 (`refX=9`) | `#B91C1C` | `8 6` |
| Activation | Triangle 9×7 (`refX=9`) | `#C2410C` | none |

Marker IDs: `arrow-source-13-04-C`, `arrow-assembly-13-04-C`, `arrow-vile-13-04-C`, `arrow-dashed-vile-13-04-C`, `arrow-activation-13-04-C`. All markers use `markerUnits="userSpaceOnUse"`, `refX=9`, and a slightly narrowed head path (`M0,0.5 L9,4 L0,7.5 Z`) so the shaft terminates cleanly before the tip. Connectors use `stroke-linecap: butt`. Bus segments (`conn-bus`, `conn-vile-bus`, `conn-vile-dash-bus`, `conn-act-bus`, `conn-act-dash-bus`) carry no marker.

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `What the world exposes` | x=48, y=128 |
| a2 | `Join, infer, operationalize` | x=280, y=128 |
| a3 | `What the graph can now say about you` | x=536, y=128 |
| a4 | `How “safety” deploys it` | x=1040, y=128 |
| a5 | `First-order claims` | x=640, y=146, `text-anchor=middle` |
| a6 | `Association claims` | x=880, y=146, `text-anchor=middle` |

Zone 3 column headers use zone-title color `#991B1B`, size 11, weight 600.

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `The graph started having opinions` |
| Plate ID | `13-04-C` |

### Zone 1

| Node | Exact text |
| --- | --- |
| Observations | `Plate / asset` / `observations` |
| Signals | `Observable signals` / `recurring proximity` |
| Property | `Property / deed /` / `LLC records` |
| Court | `Court / arrest /` / `divorce dockets` |
| Social | `Social / public` / `web traces` |
| People-search | `People-search /` / `broker context` |
| Other people | `Other-people / household` / `associations` |

### Zone 2

| Node | Exact text |
| --- | --- |
| Enrichment | `ACME Enrichment` / `join people, vehicles,` / `signals, and records` |
| Intelligence | `ACME Intelligence` / `traverse / correlate` / `assemble graph paths` |
| Morality Guard | `Morality Guard` / `manufactures moralized` / `and association claims` |
| Real-Time Security | `ACME Real-Time Security` / `standing watches / alerts` |

### Zone 3

| Node | Exact text |
| --- | --- |
| Likely affair | `Likely affair` |
| Associates | `Associates with` / `high-concern people` |
| Gambling pattern | `Gambling pattern` |
| Household | `Household linked to` / `flagged person` |
| Godliness | `Godliness score` / `37` |
| Suitability | `Behavioral suitability` / `LOW` |
| High concern person | `High concern` / `person` |

### Zone 4

| Node | Exact text |
| --- | --- |
| Subscribers | `Real-time subscribers` / `people, vehicles, profile` / `classes, or graph-neighborhoods` |
| Intervention | `Quiet intervention` / `attention, denial,` / `rerouting, scrutiny` |
| Live alert | `Live area alert` / `condition matched nearby` / `nobody typed a name` |
| Standing conditions | `Standing conditions` / `notify if a high concern` / `person enters this area,` / `or a person within 2 hops` / `of a flagged cluster` / `appears nearby` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `Morality Guard manufactures judgments from a joined graph, including who someone associates with.` |
| 2 | `A condensed class can drive standing watches, alerts, and quiet intervention without a name search.` |
| 3 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: `camera`, `GPS`, `facial recognition`, `Bluetooth`, `TPMS`, `fingerprint`, `hacked`, `intercepted`, `search box`, `dossier`, `FinCEN`, `BOI`, `Holdings`, `Shepherd’s Keeper`, `RSS`, `MVC-D`, `Kernel`, `IR`, logos, `frequent bar patron`, `protest attendee`, `routine instability`, `religious inconsistency`, `Community risk`, `Concerning social cluster`, `employed by`, `mentioned in`, or extra profile nodes beyond the seven defined in Zone 3.

Do not use `Erik` as a node on this plate. The judgments are class-shaped. Identity is already a join in Plate B.

Do not label Zone 1 as `Available inputs`. The zone title is `What the world exposes`.

---

## 10. Typography hierarchy

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Plate title | 22 | 600 | `#0F172A` |
| Zone titles | 13 | 600 | `#334155` (Zone 3 `#991B1B`; Zone 4 `#9A3412`) |
| Zone 3 column headers | 11 | 600 | `#991B1B` |
| Morality Guard primary | 15 | 700 | `#7F1D1D` |
| High concern person primary | 15 | 700 | `#7F1D1D` |
| Godliness / suitability primary | 12 | 700 | `#7F1D1D` |
| Node primary | 12 | 600 | `#0F172A` |
| Node secondary | 11 | 400 | `#334155` |
| Connector labels | 11 | 500 | `#7F1D1D` or `#9A3412` |
| Footer lines 1–2 | 13 | 500 | `#0F172A` |
| Footer authority | 12 | 400 | `#64748B` |

Font stack: Inter, "Helvetica Neue", Arial, sans-serif.

---

## 11. Grouping (SVG semantics)

| Group id | Contents |
| --- | --- |
| `plate-header-13-04-C` | Header |
| `plate-zone1-13-04-C` | Source inputs |
| `plate-zone2-13-04-C` | Enrichment / Intelligence / Morality Guard / Real-Time |
| `plate-zone3-13-04-C` | Profile outputs, column headers, and condensed classification |
| `plate-zone4-13-04-C` | Subscriber activation |
| `plate-connectors-13-04-C` | All arrows |
| `plate-connector-labels-13-04-C` | Connector labels (transparent background) |
| `plate-footer-13-04-C` | Footer |

---

## 12. Reproduction checklist

1. Draw header, four zone frames, footer. All Zone 2 nodes stay inside the Zone 2 frame.
2. Place seven Zone 1 sources, including observable signals and other-people / household associations as separate boxes.
3. Place Enrichment, Intelligence, Morality Guard, and Real-Time with the specified subtitles.
4. Place Zone 3 column headers, the 2×3 judgment grid, and `High concern person`.
5. Place four Zone 4 activation nodes, including the 2-hop standing condition.
6. Draw source collector bus → one Enrichment trunk.
7. Draw Enrichment → Intelligence → Morality Guard → Real-Time.
8. Draw Morality Guard left-rail and center-spine feeds to all six judgments and `condense` into `High concern person`.
9. Draw the dashed U-bracket from both columns into `High concern person`.
10. Draw High concern → subscribers and Real-Time → standing conditions (horizontal at y=524) → live → quiet, with Zone 4 stacked subscribers / quiet / live / standing (top → bottom).
11. Diff all labels against Section 9.
12. Confirm no Plate B join-node climax and no Shepherd’s Keeper / Holdings / BOI.
13. Validate XML is well-formed UTF-8.

---

## 13. SVG layer order (bottom → top)

1. Canvas background  
2. Header / footer  
3. Zone frames + zone titles  
4. All boxes / nodes  
5. Connectors  
6. Connector labels  

---

## 14. Acceptance criteria

1. Cold reader can say: ordinary sources, signals, and other-people associations are joined, then judged, then watched.  
2. The plate is distinct from Plate B: it is judgmental and operational, not a neutral join graph.  
3. Zone 1 includes conservative radio/signal context, people-search/broker context, and other-people / household associations as separate source boxes.  
4. Morality Guard is visibly the vile inference engine and is labeled as manufacturing moralized and association claims.  
5. Zone 3 shows first-order claims, association/guilt-by-graph claims, an absurd moralizing score beside a sanitized euphemism, and a condensed `High concern person` class.  
6. `Godliness score` / `37` and `Behavioral suitability` / `LOW` sit on the same row.  
7. Zone 4 shows subscribers to people, vehicles, profile classes, and graph-neighborhoods; a standing 2-hop flagged-cluster condition; a live alert that did not require typing a name; and quiet intervention.  
8. The plate feels clean and architectural despite the disgusting subject matter.  
9. No dossier iconography, search-box UI, logos, sirens, or extra profile nodes.  
10. No node overflows its zone frame or the footer.  
11. Geometry is within ±8 px of this document.  
12. Plate-scoped IDs; GitHub-legible at ~640 px width.

---

## Suggested manuscript placement

Suggested placement: in **The Graph Started Having Opinions**, after the reader has Plate B’s join, or immediately before **Safety Solved the Deployment Problem**.

Suggested caption:

`**Plate 13-04-C.** The graph started having opinions. Joined records, signals, and other-people associations can be scored into moralized and social-cluster claims. Renaming godliness to behavioral suitability does not change the operation. The condensed class can drive standing watches, alerts, and quiet intervention without a name search. Explanatory projection only; the essay prose is authoritative if figure and text diverge.`
