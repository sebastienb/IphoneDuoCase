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

Outputs: `shellA_camera_half.stl`, `shellA_camera_collar.stl`, `shellB_display_half.stl` (print-ready,
bed side down), three fit coupons, `duo_case.blend` (assembled with a phone dummy), renders and cross-sections.
Every dimension lives in the `P` (case) and `F` (phone features) dicts at the top of the script.

## Design (v2)

* **Shell A, camera half** — two prints: the shell and a camera collar. Full back panel 1.8 mm (Apple allows
  2.1 max over MagSafe), 1.6 mm walls on the top, bottom and free edges, open on the hinge side. The camera
  opening in the shell looks oversized on its own (65.5 × 31 mm at the surface) and that is deliberate: Apple's
  plateau does not have a vertical side, it slopes out over 8.8 mm, and a 1.8 mm back meets that slope 5 mm from
  the flat top. The shell floor is ramped on the inside to follow the slope so it prints face-down with no
  overhang, and the collar below closes the opening to 0.3 mm around the flat top. Rounded notches: Touch ID side
  button (R3.1, must stay uncovered), Camera Control (thin-case keep-out, Ø4.9 ends), both volume buttons as one
  slot (Apple dimensions the button *centres*, 44.35 and 57.73 from the hinge), two bottom mic/speaker notches
  (R2). 0.7 mm deep ring recess on the back face for a stick-on MagSafe ring (sized for 55 OD / 45 ID / 0.6
  thick, 0.3 mm radial clearance). Eight 0.45 mm grip ribs inside the walls. Four 0.3 mm pockets in the floor
  for reusable nano-tape pads. ~19 g.
* **Camera collar** (`shellA_camera_collar.stl`, ~2 g) — not optional: it is the visible edge of the camera
  opening. Glued onto shell A. Its underside follows the plateau slope at 0.3 mm clearance, its top sits 0.6 mm
  above the plateau's flat face, 0.3 mm from its edge, and it runs out flush with the shell at the top and free
  edges. Outer edge 7 mm from the plateau top so a MagSafe puck still sits flat. Print it in a contrast colour
  if you like.
* **Shell B, display half** — 2.4 mm bezel over the outer display (Apple's limit 3.06), 1.0 mm proud of
  the glass with a 45° inner chamfer for edge gestures, same walls and grip ribs, USB-C notch (Apple's
  12.45 × 6.6 keep-out), rounded receiver/mic slot at the top. Two tape pockets under the bezel on the free
  edge. ~4 g.
* **Hinge** — bare, like Apple's own case. Both shells stop 2.7 mm from the spine with a relief chamfer.
* The cavity follows the phone's 2.74 mm edge roll with a printable 45° fill (1.05 mm), and the outer
  bed-side edge has a 0.8 mm chamfer so nothing overhangs.

## How it stays on

Nothing on a rigid PLA shell can snap over the Duo. Each half's only undercut is the edge roll on its outer
face, the inner (folding) faces are flat, and the two halves close to a 0.34 mm gap, so a lip over the inner
face would be crushed by the other half. The shell without a ring or tape just sits there, which is what the
first print showed.

The commercial cases confirm it (see `research/case-design-inspiration.md`): Apple, Spigen, Pitaka, Thinborne,
Benks and dbrand all use adhesive strips plus the phone's magnets; Nomad's back-only case uses magnets plus
microsuction pads; the only snap-on case (Ridge) is a flexible TPU-bumper unibody. The printed PLA fold cases on
MakerWorld all end up with tape or a magnet-ring recess. So this design does the same, in layers:

1. **MagSafe ring (shell A, main hold).** Stick a MagSafe ring sticker (the kind bundled with MagSafe grips,
   Ø55 OD / Ø45 ID / 0.6 mm) into the recess on the back face; it self-centres and ends up 0.1 mm below the
   surface. The phone's magnet array pulls the ring, and so the shell, on through the 1.1 mm floor, and
   chargers and grips snap to the ring on the outside. Apple's note 7 allows MagSafe magnets on the back.
   Other ring sizes: edit `magsafe_ring` in `P` (ring OD + 0.6, ID − 0.6, thickness + 0.1).
2. **Grip ribs (both shells).** 0.45 mm ribs with 0.15 mm wall clearance give 0.3 mm interference on the
   titanium rails, enough for a firm push-on in PLA. Too tight: sand the ribs. Too loose: raise
   `grip_rib.proud` or lower `clearance`.
3. **Plateau key.** The collar and opening lock shell A in x/y.
4. **Tape pockets.** Shell B has no magnets to use, so like every commercial Duo case its frame relies on the
   ribs plus reusable nano-tape or microsuction pads in the two pockets under the bezel. Shell A has four
   pockets in the floor if you want it tape-mounted as well.

## Print

1. Print the coupons first: `couponA_camera_top.stl` (plateau opening + ramp, volume slot, Touch ID notch),
   `couponA_bottom.stl` / `couponB_bottom.stl` (ports, corner, ribs) and `shellA_camera_collar.stl` (drop it
   on the phone to check the fit). Adjust `clearance`, `cut_clr`, `grip_rib` in `P`, regenerate.
2. Shells face-down on the textured plate, no supports. Collar flat-top-down (the STL is already oriented).
   0.12–0.16 mm layers, 4 walls, 100 % infill, matte PLA. Add 0.2 mm elephant-foot compensation.
3. Glue the collar: put the shell on the phone, drop the collar over the plateau (it self-centres with 0.3 mm
   clearance), then tack it with a few drops of CA on the flange. Remove the phone and let it cure.
4. Insert the phone open: hook the camera plateau into shell A first, press the bottom corners in, then seat
   shell B. Check the fold at 0°, 90°, 120°, 180° before taping.

## Known limitations / v2 ideas

* The blend profile of the plateau is modelled as a smoothstep from Apple's side view (not dimensioned);
  the 0.3 mm margin covers a reasonable error. If the collar rocks, increase `cut_clr`.
* The collar top is 0.6 mm above the plateau, 1.5 mm below the lens glass: it frames the plateau, it does not
  protect the lenses. Raise `ring_lip` if you want a taller guard.
* Rigid PLA cannot snap over the phone; see "How it stays on".
