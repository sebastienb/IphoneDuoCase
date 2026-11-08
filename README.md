# iPhone Duo case (PLA, Bambu Lab P1S)

Parametric two-shell case for Apple's foldable iPhone Duo, generated with Blender from Apple's official
dimensional drawings.

```
case/duo_case.py                 parametric generator (Blender 5.x python, headless)
research/iphone-duo-specs.md     every dimension a case needs, extracted from Apple's drawing
research/case-design-inspiration.md   market survey + design principles + 3D-print lessons
build/                           STLs, fit coupons, .blend, renders (regenerate with the command below)
```

## Regenerate

```
blender --background --python case/duo_case.py -- --out build
```

Outputs: `shellA_camera_half.stl`, `shellB_display_half.stl` (print-ready, bed side down),
three fit coupons, `duo_case.blend` (assembled with a phone dummy), renders and cross-sections.
Every dimension lives in the `P` (case) and `F` (phone features) dicts at the top of the script.

## Design (v1)

* **Shell A, camera half** — full back panel 1.8 mm (Apple allows 2.1 max over MagSafe), 1.6 mm walls on
  the top, bottom and free edges, open on the hinge side. The camera plateau opening hugs Apple's plateau
  outline with 0.3 mm clearance, so the plateau keys the shell in x/y. Notches: Touch ID side button (must stay
  uncovered), Camera Control (thin-case keep-out, 28.3 mm), both volume buttons as one top slot, two bottom
  mic/speaker groups. Four 0.3 mm pockets in the floor for reusable nano-tape pads. ~19 g.
* **Shell B, display half** — 2.4 mm bezel over the outer display (Apple's limit 3.06), 1.0 mm proud of
  the glass with a 45° inner chamfer for edge gestures, same walls, USB-C notch (Apple's 12.45 × 6.6 keep-out),
  receiver/mic slot at the top. Two tape pockets under the bezel on the free edge. ~4 g. Every commercial
  Duo case, Apple's included, tapes this piece; the research report recommends PETG for it if you want clips.
* **Hinge** — bare, like Apple's own case. Both shells stop 2.7 mm from the spine with a relief chamfer.
* The cavity follows the phone's 2.74 mm edge roll with a printable 45° fill (1.05 mm), and the outer
  bed-side edge has a 0.8 mm chamfer so nothing overhangs.

## Print

1. Print `couponA_camera_top.stl` and `couponA_bottom.stl` first. They test the plateau key, the Touch ID
   notch and the wall fit in 20 minutes. Adjust `clearance` (0.15) and `cut_clr` (0.30) in `P`, regenerate.
2. Shells face-down on the textured plate, no supports. 0.12–0.16 mm layers, 4 walls, 100 % infill (the parts
   are nearly all wall anyway), matte PLA. Add 0.2 mm elephant-foot compensation. Fuzzy skin on the rails for grip
   if you like the dbrand look.
3. Insert the phone open: hook the camera plateau into shell A first, press the bottom corners in, then seat
   shell B. Check the fold at 0°, 90°, 120°, 180° before taping.

## Known limitations / v2 ideas

* No camera lip: the plateau stands 1.8 mm proud of the back and the lenses 3.9 mm. A raised camera ring is
  not printable face-down without supports; a separate snap-in ring is the v2 answer.
* Retention is plateau key + wall friction + optional tape. Rigid PLA cannot snap over the phone because the
  inner (folding) faces have no roll to hook.
* Optional: 0.5 mm MagSafe ring recess at (42.8, 61.3) from the hinge/top if you want to add a magnet ring.
* The camera plateau outline (x 2.0–72.4, y 1.5–34.6 from the free edge / top) is read from the drawing's
  plan view at ±0.3 mm; the other numbers are dimensioned by Apple. Verify on a real phone with the coupon.
