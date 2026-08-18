# Plate 13-04-B - Composition: the person becomes the join point

**Plate ID:** `13-04-B`  
**Parent work:** `13-04-privacy-has-a-composition-problem.md`  
**Rendered projection:** `plate-13-04-B-the-person-becomes-the-join-point.svg`  
**Status:** Engineering layout specification (canonical, revised). Not artwork.  
**Reproduce in:** SVG or draw.io without additional design decisions.  
**Authority:** Explanatory aid only. Essay prose remains interpretive authority if figure and text diverge during drafting.

**Insight (one sentence):** Enrichment makes Erik the join point where otherwise separate observations, ambient signals, assets, places, public context, and other people become mutually traversable, without a dossier, a name search, or any moral classification.

**Sync rule:** When `plate-13-04-B-the-person-becomes-the-join-point.svg` is refined for layout or rendering, update this file in the same change so SVG and specification remain identical.

**Lettering note:** `13-04-B` assumes this plate embeds after `13-04-A` (semantic retroactivity) and before `13-04-C`. If embed order changes, renumber IDs, filenames, captions, and SVG chrome in the same change.

---

## 1. Overall composition

| Property | Specification |
| --- | --- |
| Orientation | Landscape |
| Canvas size | 1280 x 720 px (16:9). Safe margin 32 px from all edges. |
| Content grid | **Four semantic zones.** Left = materials permitted separately. Mid-left = ordinary processing boxes. Mid-right = the person as join point and traversable relationships. Right = resulting capability. |
| Column frames | Zone 1: x=32 w=216; Zone 2: x=264 w=248; Zone 3: x=528 w=488; Zone 4: x=1032 w=216. 16 px gutters. Zone 3 is wider so labeled join edges have ~80 px horizontal shafts. |
| Vertical structure | Header band; four zone frames; footer band. |
| Reading frame | Header → left top-to-bottom → ordinary boxes → Enrichment introduces join → person/relationship graph → resulting capability → footer. |

The plate must remain **architectural, calm, and non-dramatic**. The **person/relationship graph is the visual center of meaning**. Enrichment is the hinge that makes the relationships mutually traversable. The discomfort is the richness of the join, not a judgment about Erik.

Do not show STE stack, RSS, MVC, Kernel, IR, cameras, maps, facial recognition, a stored dossier, a search box UI, Morality Guard, Shepherd’s Keeper, Holdings, BOI, behavioral scores, profile judgments, subscribers, live alerts, or quiet intervention.

Do not imply hacked devices, intercepted communications, defeated encryption, a radio fingerprint that identifies a natural person, or that a signal observation is itself an identity.

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
| Zone 2 frame | x=264, y=104 | w=248, h=456 |
| Zone 3 frame | x=528, y=104 | w=488, h=456 |
| Zone 4 frame | x=1032, y=104 | w=216, h=456 |

Zone titles at baseline y=128.

### 2.4 Absolute node positions (authoritative)

#### Zone 1: permitted separately

Four inventory nodes. Zone 1 is materials, not a pipeline.

| Node | x, y, w, h |
| --- | --- |
| Permitted observations | 44, 148, 192, 72 |
| Permitted observable signals | 44, 236, 192, 72 |
| Permitted public / professional / commercial context | 44, 324, 192, 88 |
| Permitted identity relationship | 44, 432, 192, 72 |

Vertical gaps: 16 px, then 16 px, then 20 px. 12 px inset from the Zone 1 frame.

#### Zone 2: ordinary processing

Unchanged processing field. These boxes remain ordinary and boring.

| Node | x, y, w, h |
| --- | --- |
| ACME Vision | 276, 152, 108, 68 |
| ACME Analytics | 392, 152, 108, 68 |
| ACME Enrichment | 316, 260, 144, 88 |
| ACME Intelligence | 276, 396, 108, 68 |
| ACME Real-Time Security | 392, 396, 108, 68 |

Vision and Analytics occupy the upper tier, Intelligence and Real-Time occupy the lower tier, Enrichment sits centered between them (center x=388) and becomes the hinge. Do not restyle Enrichment as a moral climax. Analytics and Intelligence wrap the company name to two primary lines so 108 px boxes do not clip.

#### Zone 3: the person becomes the join point

Erik is the center. Surrounding nodes are relationship-bearing context, not classifications.

| Node | x, y, w, h |
| --- | --- |
| Employer | 540, 148, 96, 44 |
| Public mention | 716, 148, 112, 44 |
| Property | 908, 148, 96, 44 |
| Erik join node | 716, 248, 112, 48 |
| Observable signal A | 540, 324, 96, 52 |
| Person B | 908, 260, 96, 56 |
| Observable signal B | 540, 392, 96, 52 |
| Vehicle X | 716, 392, 112, 52 |
| Household / address context | 908, 392, 96, 52 |
| Place / time history | 656, 504, 232, 36 |

Derived centers: Public mention, Erik, and Vehicle X share x=772. Employer / Signal A / Signal B share x=588. Property / Person B / household share x=956.

Horizontal gaps: Signal A right (636) to Erik left (716) = 80 px; Erik right (828) to Person B left (908) = 80 px. Same 80 px gaps on the Vehicle X row.

Vertical corridors: top row bottom (192) to Erik top (248) = 56 px; Erik bottom (296) to Signal A top (324) = 28 px; Signal A bottom (376) to Signal B top (392) = 16 px; Vehicle X top (392) aligns with Signal B; Vehicle X bottom (444) to Place / time top (504) = 60 px. Signal A and Signal B share height 52. Person B stays beside Erik at y=260. Signal A sits lower at y=324 so the y=272 corridor stays clear for the Enrichment dashed join.

Zone 3 is the intellectual center of the plate. The join is not merely a destination; it is where otherwise separate relationships become mutually traversable, including assets, ambient signals, places, and other people.

#### Zone 4: resulting capability

Three resulting properties, not extra products.

| Node | x, y, w, h |
| --- | --- |
| Reconstructable view | 1044, 160, 192, 80 |
| No canonical dossier required | 1044, 288, 192, 80 |
| No name search required | 1044, 416, 192, 80 |

### 2.5 Footer band

| Element | Position | Size |
| --- | --- | --- |
| Footer contrast bar | x=32, y=576 | w=1216, h=112 |
| Footer line 1 | x=640, baseline y=614, `text-anchor=middle` | — |
| Footer line 2 | x=640, baseline y=638, `text-anchor=middle` | — |
| Footer authority line | x=640, baseline y=668, `text-anchor=middle` | — |

---

## 3. Visual hierarchy

Priority order (highest → lowest):

1. Erik join node and the Zone 3 relationship graph
2. ACME Enrichment
3. Zone 4 capability statements
4. Other ordinary company boxes
5. Zone 1 inputs
6. Connectors
7. Header / footer

Fill hierarchy:

| Node class | Fill | Stroke | Stroke width | Corner radius |
| --- | --- | --- | --- | --- |
| Zone 1 input | `#F8FAFC` | `#475569` | 1.5 | 8 |
| Ordinary company | `#EEF2FF` | `#4338CA` | 1.5 | 8 |
| Enrichment | `#FEF3C7` | `#B45309` | 2.5 | 8 |
| Erik join | `#FEF3C7` | `#B45309` | 2.5 | 24 (pill) |
| Zone 3 relationship nodes | `#FFFBEB` | `#D97706` | 1.5 | 8 |
| Zone 4 capability | `#EEF2FF` | `#4338CA` | 1.5 | 8 |
| Zone 1 / 2 / 4 frames | `#FFFFFF` | `#CBD5E1` | 1.5 | 8 |
| Zone 3 frame | `#FFFBEB` | `#D97706` | 2 | 8 |
| Header / footer | `#F1F5F9` | `#94A3B8` | 1 | 8 |

Do not use gradients, shadows, glows, icons, cameras, maps, dossier glyphs, sirens, warning triangles, or red scare styling. Signal and Person B nodes use the same Zone 3 relationship fill as Employer and Vehicle X. They are not vile outputs.

---

## 4. Zone semantics

| Zone | Members | Visual treatment |
| --- | --- | --- |
| Zone 1 | observations, observable signals, public/professional/commercial context, identity | Cool frame; title `Permitted separately` |
| Zone 2 | Vision, Analytics, Enrichment, Intelligence, Real-Time | Cool frame; title `Ordinary processing` |
| Zone 3 | Erik, Employer, Property, Public mention, Vehicle X, Signal A, Signal B, Person B, household/address context, Place/time history | Warm frame; title `The person becomes the join point` |
| Zone 4 | three capability statements | Cool frame; title `Resulting capability` |

No Holdings. No Shepherd’s Keeper. No Morality Guard. No profile judgments.

---

## 5. Alignment rules

- Zone 1 uses vertical stacking with 16–20 px gaps.
- Zone 2 boxes align to an 8 px grid and form a balanced field around Enrichment (center x=388).
- Zone 3 top relationship nodes share top y=148 and height 44.
- Erik is centered beneath Public mention (center x=772); single-line label `Erik` only (no subtitle).
- Signal A is left of Erik at y=324 (height 52, matching Signal B) so the dashed Enrichment join can traverse y=272 in Signal A's former slot.
- Person B is right of Erik at y=260 (12 px below Erik top) so labeled elbows at y=252 do not clip it.
- Vehicle X is centered beneath Erik.
- Signal B is left of Vehicle X; household/address context is right of Vehicle X; those three share top y=392.
- Place / time history is centered beneath Vehicle X (center x=772).
- Zone 4 uses vertical stacking with 48 px gaps.

---

## 6. Connectors

### 6.1 Zone 2 ordinary-processing connectors

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| c1 | Vision bottom (330, 220) | Enrichment top (330, 260) | Solid | none | (330, 220)-(330, 252) |
| c2 | Analytics bottom (446, 220) | Enrichment top (446, 260) | Solid | none | (446, 220)-(446, 252) |
| c3 | Enrichment bottom-left (360, 348) | Intelligence top (330, 396) | Amber | none | (360, 348)-(330, 388) |
| c4 | Enrichment bottom-right (416, 348) | Real-Time top (446, 396) | Amber | none | (416, 348)-(446, 388) |

c1 and c2 are straight vertical drops from each upper-tier box center into Enrichment. c3 and c4 are straight diagonals into the lower tier; each shaft ends 8 px before the destination top edge (388 = 396 − 8).

### 6.2 Enrichment to join

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| c5 | Enrichment right (460, 304) | Erik left (716, 272) | Dashed amber | `identity + context joined` | bus (460, 304)-(512, 304)-(512, 272); arrow (512, 272)-(708, 272) |

c5 exits Enrichment horizontally, climbs in the Zone 2/3 gutter at x=512, runs at y=272 through the corridor vacated by lowering Signal A, and enters Erik's left side at vertical center. Only the final horizontal segment carries the arrowhead.

### 6.3 Join graph connectors (explanatory; must be labeled)

Conservative wording only. Do not upgrade co-observation into identity, ownership, or a moral claim.

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| j1 | Erik top (772, 248) | Public mention bottom (772, 192) | Amber | `mentioned in` | (772, 248)-(772, 200) |
| j2 | Erik upper-left (716, 248) | Employer bottom (588, 192) | Amber | `employed by` | (716, 248)-(588, 200) |
| j3 | Erik upper-right (828, 248) | Property bottom (956, 192) | Amber | `associated with` | (828, 248)-(956, 200) |
| j4 | Erik bottom (772, 296) | Vehicle X top (772, 392) | Amber | `associated with` | (772, 296)-(772, 384) |
| j5 | Vehicle X bottom (772, 444) | Place / time history top (772, 504) | Amber | `observed at` | (772, 444)-(772, 496) |
| j6 | Signal A right center (636, 350) | Erik bottom-left (716, 296) | Amber | `later associated with` | (636, 350)-(708, 296) |
| j7 | Signal A right lower (636, 368) | Vehicle X top-left (716, 392) | Amber | `repeatedly observed near` | (636, 368)-(708, 384) |
| j8 | Signal B right center (636, 418) | Vehicle X left (716, 418) | Amber | `recurring co-observation` | (636, 418)-(708, 418) |

Signal arrows must attach to edge midpoints on the right side (or horizontal center for row peers), never to rounded corners. j6 exits Signal A at vertical center; j7 exits lower on the right edge; j8 exits Signal B at vertical center.
| j9 | Erik right (828, 272) | Person B left (908, 272) | Amber | `repeatedly co-located with` | (828, 272)-(900, 272) |
| j10 | Person B bottom (956, 316) | Household / address top (956, 392) | Amber | `associated with` | (956, 316)-(956, 384) |

Prefer straight shafts wherever node clearance allows. j2, j3, and j7 are straight diagonals. j1, j4, j5, j6, j8, j9, and j10 are straight vertical or horizontal segments.

`later associated with` means a permitted identity or continuity relationship arrived after the signal observation existed. It does not mean the signal identified Erik at collection time.

`repeatedly observed near` and `recurring co-observation` are continuity relationships. They do not assert that Signal A or Signal B belongs to Erik, Person B, or the registered owner of Vehicle X.

`repeatedly co-located with` is a recurring association. It does not assert household membership, partnership, or any behavioral category. Household / address context attaches to Person B as onward context, not as a judgment about Erik.

### 6.4 Capability connectors

| ID | From | To | Style | Label | Line drawn |
| --- | --- | --- | --- | --- | --- |
| k1 | Join-graph field right (1004, 200) | Reconstructable view left (1044, 200) | Dashed slate | none | (1004, 200)-(1036, 200) |
| k2 | Join-graph field right (1004, 368) | No canonical dossier required left (1044, 328) | Dashed slate | none | (1004, 368)-(1016, 368)-(1016, 328)-(1036, 328) |
| k3 | Join-graph field right (1004, 456) | No name search required left (1044, 456) | Dashed slate | none | (1004, 456)-(1036, 456) |

The capability statements are properties of the whole traversable join graph, not outputs of an individual relationship node. k1 and k3 remain horizontal 46 px shafts on their capability rows. k2 exits at y=368 in the open corridor below Person B (bottom y=316) and above Vehicle X (top y=392), then turns in the Zone 3/4 gutter to enter the middle capability box at y=328 so it does not cross j9, j10, or household/address labels.

Do not draw arrows from Zone 1 directly into Zone 2. Zone 1 is inventory, not a visible graph pipeline.

Do not draw Vision or Real-Time directly to Erik.

Do not draw Signal A or Signal B to Person B. Ambient signals attach to observations, vehicles, or later-permitted identity, not to an implied interpersonal device-ownership story.

Do not use a search-box icon or UI element.

Shafts end 8 px before the destination edge. Arrowheads use `refX=9` markers so the tip meets the gap and the shaft does not run through the head. Head-only connectors are a defect.

### 6.5 Connector label positions

Relationship labels sit 8–20 px off the shaft with transparent background (no backing rect). Color `#92400E`. Short shafts wrap to two lines rather than truncating the conservative wording.

| ID | Exact text | Anchor | x, y |
| --- | --- | --- | --- |
| c5 | `identity + context joined` | middle | 610, 288 |
| j1 | `mentioned in` | start | 798, 224 |
| j2 | `employed by` | start | 658, 206 |
| j3 | `associated with` | start | 916, 236 |
| j4 | `associated with` | start | 786, 354 |
| j5 | `observed at` | start | 786, 478 |
| j6 | `later associated` / `with` | start | 604, 308 and 604, 320 |
| j7 | `repeatedly observed` / `near` | middle | 702, 364 and 702, 376 |
| j8 | `recurring` / `co-observation` | middle | 676, 396 and 676, 408 |
| j9 | `repeatedly` / `co-located with` | middle | 884, 246 and 884, 258 |
| j10 | `associated` / `with` | start | 968, 342 and 968, 354 |

Labels sit in open corridors above horizontal shafts or beside vertical shafts, positioned off the stroke. No backing rects.

---

## 7. Arrow styles / markers

| Style | Marker | Stroke | Dash |
| --- | --- | --- | --- |
| Ordinary process | Triangle 9×7 (`refX=9`) | `#334155`, 2 px | none |
| Join / relationship | Triangle 9×7 (`refX=9`) | `#B45309`, 2.5 px | none |
| Joined / capability | Triangle 9×7 (`refX=9`) | `#64748B` or `#B45309` as specified | `8 6` |

Marker IDs: `arrow-solid-13-04-B`, `arrow-join-13-04-B`, `arrow-dashed-13-04-B`. All markers use `markerUnits="userSpaceOnUse"`, `refX=9`, and a slightly narrowed head path (`M0,0.5 L9,4 L0,7.5 Z`) so the shaft terminates cleanly before the tip. Connectors use `stroke-linecap: butt`.

---

## 8. Annotations

| ID | Exact text | Placement |
| --- | --- | --- |
| a1 | `Permitted separately` | x=48, y=128 |
| a2 | `Ordinary processing` | x=280, y=128 |
| a3 | `The person becomes the join point` | x=544, y=128 |
| a4 | `Resulting capability` | x=1048, y=128 |

---

## 9. Labels (exact node text)

### Header

| Element | Exact text |
| --- | --- |
| Plate title | `The person becomes the join point` |
| Plate ID | `13-04-B` |

### Zone 1

| Node | Exact text |
| --- | --- |
| Observations | `Permitted` / `observations` |
| Signals | `Permitted` / `observable signals` |
| Context | `Permitted public /` / `professional /` / `commercial context` |
| Identity | `Permitted identity` / `relationship` |

### Zone 2

| Node | Exact text |
| --- | --- |
| Vision | `ACME Vision` / `observation` |
| Analytics | `ACME` / `Analytics` / `continuity` |
| Enrichment | `ACME Enrichment` / `identity + context` |
| Intelligence | `ACME` / `Intelligence` / `traversal` |
| Real-Time | `ACME Real-Time` / `Security` / `predicate / alert` |

### Zone 3

| Node | Exact text |
| --- | --- |
| Erik | `Erik` |
| Employer | `Employer` |
| Public mention | `Public mention` |
| Property | `Property` |
| Signal A | `Signal A` / `observable` |
| Signal B | `Signal B` / `observable` |
| Vehicle X | `Vehicle X` |
| Person B | `Person B` |
| Household | `Household /` / `address context` |
| Place / time | `Place / time history` |

### Zone 4

| Node | Exact text |
| --- | --- |
| Reconstructable view | `Reconstructable view` / `The picture can be` / `assembled from paths` |
| No dossier | `No canonical dossier` / `required` / `Relationships can be` / `traversed together` |
| No name search | `No name search` / `required` / `Identity can unify` / `older observations` |

### Footer

| Line | Exact text |
| --- | --- |
| 1 | `Each box still sounds ordinary when described by itself.` |
| 2 | `Identity can join context, observations, signals, places, and other people without assembling a dossier.` |
| 3 | `Explanatory projection only; essay prose is authoritative if figure and text diverge.` |

### Forbidden labels

Do not use: `search box`, `camera`, `GPS`, `facial recognition`, `Bluetooth`, `TPMS`, `fingerprint`, `hacked`, `intercepted`, `anonymous`, `unresolved`, `grep`, `RSS`, `MVC-D`, `Kernel`, `IR`, `FinCEN`, `BOI`, `Morality Guard`, `Shepherd’s Keeper`, `Holdings`, `likely affair`, `gambling`, `protest attendee`, `religious inconsistency`, `godliness`, `behavioral scoring`, `high concern`, `subscriber`, `live area alert`, `quiet intervention`, logos, or extra profile-judgment nodes.

Do not name Person B as a spouse, suspect, accomplice, or other role. Person B is an associated person.

---

## 10. Typography hierarchy

| Role | Size | Weight | Color |
| --- | --- | --- | --- |
| Plate title | 22 | 600 | `#0F172A` |
| Zone titles | 13 | 600 | `#334155` (Zone 3: `#B45309`) |
| Erik primary | 16 | 600 | `#0F172A` |
| Enrichment primary | 14 | 600 | `#0F172A` |
| Company primary | 12 | 600 | `#0F172A` |
| Secondary / relationship label | 11 | 400 / 500 | `#334155` or `#92400E` |
| Capability primary | 12 | 600 | `#0F172A` |
| Footer lines 1–2 | 13 | 500 | `#0F172A` |
| Footer authority line | 12 | 400 | `#64748B` |

Font stack: Inter, "Helvetica Neue", Arial, sans-serif.

---

## 11. Grouping (SVG semantics)

| Group id | Contents |
| --- | --- |
| `plate-header-13-04-B` | Header |
| `plate-zone1-13-04-B` | Permitted materials |
| `plate-zone2-13-04-B` | Ordinary processing |
| `plate-zone3-13-04-B` | Join-point relationship graph |
| `plate-zone4-13-04-B` | Resulting capability |
| `plate-connectors-13-04-B` | All arrows |
| `plate-connector-labels-13-04-B` | Relationship labels (transparent background) |
| `plate-footer-13-04-B` | Footer |

---

## 12. Reproduction checklist

1. Draw header, four zone frames, footer.
2. Place Zone 1 inventory: observations, observable signals, public/professional/commercial context, identity.
3. Place Zone 2 ordinary boxes as a balanced field around Enrichment.
4. Place Zone 3 with Erik centered; Employer / Public mention / Property above; Signal A and Person B beside Erik; Signal B / Vehicle X / household below; Place / time history beneath Vehicle X.
5. Place Zone 4 capability statements.
6. Draw restrained process arrows in Zone 2.
7. Draw dashed Enrichment → Erik join arrow with label.
8. Draw labeled Zone 3 relationship edges, including signal and Person B edges.
9. Draw dashed explanatory links into Zone 4 using the specified corridors.
10. Diff all labels against Section 9.
11. Confirm no Morality Guard, profile-judgment, or subscriber-activation labels.
12. Validate XML is well-formed UTF-8.

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

1. Cold reader can say: Enrichment makes Erik the point where otherwise separate relationships become mutually traversable.  
2. Cold reader can also say: those relationships can include observed assets, ambient signals, places, and other people.  
3. The plate feels calm and architectural, not dramatic or moralized.  
4. Erik is visually central as the join point.  
5. Signal A / Signal B read as observable radio context, not as device identity or interception.  
6. Person B reads as a conservative interpersonal association with onward household/address context, not as a profile judgment.  
7. Enrichment is visibly important but not more important than the join itself.  
8. Zone 4 reads as resulting properties, not as more companies and not as safety activation.  
9. No search-box UI, no dossier iconography, no camera iconography, no red scare styling, and no Plate C concepts.  
10. Geometry is within ±8 px of this document.  
11. Plate-scoped IDs; GitHub-legible at ~640 px width.

---

## Suggested caption

`**Plate 13-04-B.** The person becomes the join point. Ordinary processing boxes still sound ordinary, but Enrichment joins identity and context that already existed for other reasons. The traversable graph can include observations, ambient signals, assets, places, and other people without a canonical dossier, a name search, or a moral classification. Explanatory projection only; the essay prose is authoritative if figure and text diverge.`
