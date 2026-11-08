# iPhone Duo — case design spec sheet

Primary source: Apple's official **iPhone Duo Dimensional Drawings** (7 sheets, dated 2026-09-09, published 2026-10-23)
from https://developer.apple.com/accessories/dimensional-drawings/ →
https://developer.apple.com/download/files/accessories/dimensional-drawings/iphone-duo.pdf
(local copy: `research/apple/iphone-duo-dimensional-drawings.pdf`, page renders alongside; gitignored because
Apple's notice says not to redistribute). Secondary sources listed at the bottom. All numbers in mm.

## Coordinate conventions used below

* **Closed-phone front view** (outer display facing you): hinge spine on the **left** (x = 0), free edge on the
  right (x = 84.10). y = 0 at the top edge, positive downward. This is how the Apple front view is drawn.
* **Back view** (camera facing you): mirrored, so the **free edge is x = 0 on the left** and the hinge is at
  x = 84.10 on the right. Apple's Detail D camera dims use this frame.
* The device is two halves. **Half A = "camera half"** (back glass, cameras, MagSafe, all buttons).
  **Half B = "display half"** (outer display on its outside face, USB-C on its bottom edge).

## Overall envelope

| Item | Value | Source |
|---|---|---|
| Closed W × L × T | 84.10 × 117.80 × 11.30 | Sheet 1 |
| Open W × L × T | 164.60 × 117.80 × 5.2 (Apple spec page); drawing shows each half 5.48 thick at the glass | Sheet 1, 4 |
| Per-half thickness | 2 × 5.48 → gap between halves when closed ≈ 0.34 | Sheet 1 "2x 5.48 PRODUCT THICKNESS" |
| Weight | 254 g | Apple specs |
| Frame | Grade 5 titanium, mirror polished; hinge cover 3D-printed titanium, micro-blasted | Apple / MacRumors |
| Back | Ceramic Shield glass (Apple logo centered at x 41.40 from free edge, y 59.62..79.62) | Sheet 1 |
| Outer display glass | 79.93 × 115.04, inset 1.33 all around from housing (hinge side: see below) | Sheet 1 |
| Outer display active area | 77.17 × 112.28, inset 2.71 from housing; 4.13 from hinge exterior | Sheet 1 |
| Max case occlusion on display face | **3.06 all around**, **5.23 on the hinge side** (how far a lip may come in over the display face) | Sheet 1 |
| Max case thickness on back | **2.1 mm** (note 8; needed for MagSafe/Qi2 function) | Sheet 1 note 8 |
| Edge roll (each half, both faces) | starts 2.91 from the half's outer face… i.e. side flat ends 2.74 below the face; round-over is 2.74 wide × 2.74 tall (slightly super-elliptical). Points from mid-plane: (0.00, 2.91) (0.02, 3.85) (0.23, 4.76) (0.89, 5.41) (1.80, 5.63) (2.74, 5.65) | Sheet 1 Detail B |

## Plan-view corners

**Free-side corners (the 4 corners of the open device, Detail A "all four corners")** — a super-ellipse, not a circle.
Measured from the corner's horizontal tangent (top edge, y = 0) and vertical tangent (x = 84.10 in front view):

| x from hinge | y from top |
|---|---|
| 66.80 | 0.00 |
| 71.66 | -0.06 |
| 76.42 | -1.00 |
| 80.48 | -3.63 |
| 83.10 | -7.68 |
| 84.08 | -12.44 |
| 84.10 | -17.31 |

So the corner blends over ~17.3 mm in each direction. Apple's antenna sheet labels the corner outline "4x R11.52"
with "4x R5.00" (probably the inner/outer approximation). A circular R≈11.5–12 corner is a decent approximation;
a squircle through the points above is exact.

**Hinge-side corners (Detail AY, "hinge corner profile")** — tight: blends over 3.03 (along top edge) × 3.72
(down the spine). Points (x from spine exterior, y from top): (3.03, 0) (2.52, -0.02) (2.06, -0.23) (1.80, -0.67)
(1.82?, -1.19) (0.92, -1.36)…(0.26, -1.96) (0.01, -2.82) (0.00, -3.72). Treat as ≈ R3.2.

**Spine (hinge exterior) cross-section (Detail E, viewed from the bottom)**: the closed spine is a continuous
rounded edge, flat only between y = ±1.56 about the mid-plane, rolling to the faces over 2.67–2.74 mm, i.e. it
looks like the other rounded edges. Points (x inward from spine exterior, z from mid-plane): (0.00, ±1.56)
(0.01, ±2.46) (0.26, ±3.32) (0.92, ±3.92) (1.80, ±4.09)… (2.67, ±5.65). The hinge cover is a separate part that is
*exposed* when closed; its ends are ~1.23 from the top/bottom edges (left view: 0.00/-1.23 and -116.57/-117.80).

## Camera plateau (on Half A back; back-view frame, free edge x = 0, top y = 0)

| Item | Value |
|---|---|
| Plateau height above back glass | **3.64** |
| Lens glass height above back glass | **5.72** |
| Rear camera 1 (main) center | (15.25, -15.25), Ø16.20 |
| Rear camera 2 (ultra wide) center | (32.98, -15.25), Ø16.20 |
| Flash center | (≈49.58, -19.70), Ø3.75 |
| Rear mic | (49.58, -10.95), slot 3.32 × 1.50 |
| Plateau TOP face (flat, 3.64 high) | stadium x 4.94 → 60.56, y -4.70 → -25.80 (55.6 × 21.1, R10.55 ends). The lens glass stands on it (5.72). |
| Blend to the back glass | On the two sides facing the phone centre the top face runs out through an S-shaped slope ~8.8 wide: toe at x 69.37 and y -34.62 (the crosses at x 60.56 / 69.37 on y -15.25 mark the end of the flat top and the toe). Side view: the slope reaches 1.8 above the glass ~4.4 from the top edge, max slope ~30°. On the sides facing the top edge and the free edge it is a short concave cove (3.5 and ~2.9 wide) down to the edge roll, with the plateau face starting 1.23 from the top edge. **A case opening drawn at the toe (70 × 33) is far too big; design to the top face + blend.** |
| Keep-out cones | camera 1: 123°, camera 2: 84°, flash inner 121° / outer 155° (Sheet 3). With a 2 mm back and lens at 5.72 the cones are only an issue if the lip is taller than the lens; keep the camera-opening wall ≤ 45° chamfer outward. |
| Apple logo | 20.00 wide box at x 41.40 (center), y 59.62..79.62 |

## MagSafe / magnets / sensors (Half A back; back-view frame)

| Item | Value |
|---|---|
| MagSafe keep-out circle | **Ø61.50 centered at (41.30, 61.31)** — i.e. essentially centered on the width (84.10/2 = 42.05) |
| Standard MagSafe ring (if you add magnets) | Apple ring: 16 magnets, ring ≈ Ø46 inner / Ø56 outer, N45SH, coplanar; removal force 800–1100 gf; alignment within 1.55 mm radial |
| Taptic engine keep-out (no magnetic/permeable material) | rect x 44.05 → 70.93, y 98.87 → 110.14 |
| Compass | Ø4.35 at (68.04, 29.06) — keep magnets away |
| Hinge Hall sensor | Ø4.40 at x 133.65 (open-device frame), y -105.64; Folio Hall sensor Ø4.40 at (142.78, -103.21) → both on Half B near its bottom-outer corner. A magnet here puts the phone to sleep (folio behaviour). |
| Closure magnets (both halves, near free edges) | 2 stadium magnets per half at y -55.67→-60.80 and -65.83→-72.56, 1.53 wide, 3.69 from edge; corner magnets at y -24.99→-30.52 and -103.21→-108.61, x 3.50→10.40 from free edge |
| Case rules | note 7: **no magnets on the back except MagSafe magnets**; note 5: any metal μr ≤ 1.05; note 1: no metal contact with product |

## Buttons & ports

All buttons are on **Half A (camera half)**. Positions along the length are from the **top edge**.

| Feature | Edge | Center from top | Size | Keep-out |
|---|---|---|---|---|
| Side button w/ Touch ID | right (free) edge | **42.87** | 15.67 long, protrudes 0.45 | 18.67 long × 5.67 wide (= whole half thickness), R3.10 ends, 25° chamfer all around measured from surface; the button must be **uncovered** (Touch ID) |
| Camera Control | right (free) edge | **84.97** | 17.44 long at surface, protrudes 0.075 (flush) | typical: 25.00 long × 4.90 wide (2×2.45), R1.00; thin-case: 28.26 long measured 0.4 mm from surface, Ø4.88 ends; 25° chamfer, "avoid narrow edges or acute angles to preserve tactile feel" |
| Volume (−) | top edge | **centre** x 44.35 from hinge → spans 38.91 → 49.79 | 10.88 long, protrudes 0.45 | Sheet 1 dimensions the button centres, not the ends (v2 slot was 5.4 off because of this) |
| Volume (+) | top edge | **centre** x 57.73 from hinge → spans 52.29 → 63.17 | 10.88 long, protrudes 0.45 | 2.5 gap between buttons |
| Top ports (receiver, front mic) | top edge, Half B | 13.14 wide slot centred on the half, x ≈ 36.1 → 49.3 from hinge (measured on Detail A; sits directly under the volume (−) button) | 0.25 deep | do not obstruct |
| No Action button, no SIM tray, no Camera button on Half B | | | | |

**Bottom edge** (Detail C; x from hinge exterior):

| Feature | Half | Position |
|---|---|---|
| USB-C | **Half B (display half)** | center x = **42.70**; recommended keep-out 12.45 × 6.60, R3.30, centered on the half; mating connector area must stay flush for 14.0 mm outward |
| Bottom mic | Half A | x = 17.78 (Ø1.53) |
| Ports (8 × Ø1.53) | Half A | x = 20.03, 22.29, 24.54 and 63.10, 65.36, 67.61 (+ mic holes at 17.78, 60.85) |
| Speaker ports (3) | Half A | x ≈ 63.10–67.61 |
| Screws (4 × Ø1.50) | both | x = 35.35, 50.04 — do not cover (serviceability, not functional) |

**Front (outer display) features** (front-view frame, x from hinge): front camera Ø6.07 hole-punch at
(73.39, 10.62); ALS/proximity sensor keep-out cones base around x 56–73, y ≈ 6.5–11.3 (Sheet 3 Detail M).
Keep any screen lip ≤ 3.06 wide (5.23 on hinge side) and it will not touch these.

## Antenna keep-out (no metal/conductive material, full product volume incl. sidewalls)

Band antenna zones (open-device back frame, x from Half A free edge): y 0 → 30.40 and y 95.15 → 117.80 across
x 0 → 14.43 and 76.41 → 88.01 and 150.00 → 164.60 plus the full top/bottom strips. In short: **the whole top and
bottom ~30 mm/22 mm bands and the outer corners are antenna windows** — a PLA case is fine; do not add metal
plates, metal buttons or carbon-fibre there.

## Hinge sweep (Sheet 7)

Fold envelope: the halves rotate about the hinge center; the outer corner of each half traces a circle of
R ≈ 82.21 (half width from the fold axis) and the faces sweep through 0–90° with the gap opening as a teardrop.
The spine outer surface is at ≈2.73 either side of the fold axis when closed. Practical consequence: a case on the
hinge spine must be **≤ ~1.5 mm thick over the spine** or hinged/flexible, otherwise it collides with the
halves at ~90°. Most Fold-style cases leave the spine bare, which Apple's own case also does.

## Numbers for the case model (derived)

* Shell per half: inner cavity 84.10 × 117.80 × 5.48 (+clearance), two cavities stacked with a 0.34 gap.
* Clearance for PLA (Bambu P1S, 0.4 nozzle, 0.2 layer): 0.15–0.20 per side on walls, 0.25 at the camera opening
  and button cut-outs. The thin-case keep-outs (28.26 long Camera Control etc.) are what a 1.6–2.0 mm wall needs.
* Back wall ≤ 2.0 over the MagSafe circle; the camera plateau will stand 3.64 − 2.0 = 1.64 proud of a 2.0 mm back.
  A face-down print cannot raise the back around the plateau, so a collar must be a separate part; its outer
  edge must stay ≥ ~0.5 clear of the Ø56 MagSafe puck (puck top edge at y ≈ 33.3 from the top).
* Lip over the display face ≤ 3.06 (≤ 5.23 on the hinge side).

## Secondary sources

* Apple tech specs: https://www.apple.com/iphone-duo/specs/
* MacRumors roundup (half assignment, materials, hinge cover): https://www.macrumors.com/roundup/iphone-duo/
* iFixit teardown (screen cracks cluster near hinge cable gap; dust ingress into hinge): https://www.ifixit.com/News/119895/iphone-duo-teardown
* 9to5Mac review: https://9to5mac.com/2026/10/21/iphone-duo-review/
* MagSafe accessory rules (2020 guidelines recap): https://www.macrumors.com/2020/11/02/apple-magsafe-design-guidelines-accessory-makers
* Existing community models (MakerWorld; pages block scrapers, open in a browser):
  - Accurate iPhone Duo dummy with magnetic clasp: https://makerworld.com/en/models/3296598-accurate-iphone-duo-dummy-with-magnetic-clasp
  - Open-edge slim case: https://makerworld.com/en/models/3426379-iphone-duo-open-edge-case-slim-2-piece
  - Two-shell case with sliding hinge protector: https://makerworld.com/en/models/3345469-iphone-duo-case
  - Customisable TPU case: https://makerworld.com/en/models/3450347-iphone-duo-tpu-phone-case-customisable
