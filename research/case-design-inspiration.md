# iPhone Duo case — design inspiration research

Research date: 2026-11-08. Target: a PLA case for Apple's foldable, printed on a Bambu Lab P1S.

## 0. Product name and the facts that drive a case design

**The product is officially the "iPhone Duo."** "iPhone Ultra" was Apple's internal name (reported Aug 2026) and "iPhone Fold" was the rumor name; Apple announced it on 9 Sept 2026 as iPhone Duo, pre-orders 16 Oct, in stores 23 Oct 2026, from $1,999. Apple's spec page and newsroom release use "iPhone Duo" exclusively.

Physical facts (Apple spec page unless noted):

| Item | Value |
|---|---|
| Open | 164.6 W x 117.8 H x 5.2 mm D ("thinnest iPhone when open") |
| Closed | 84.1 W x 117.8 H x 11.3 mm D (passport-sized, wide and short) |
| Weight | 254 g (vs Galaxy Z Fold 8: 201 g, 9.7 mm closed — Engadget) |
| Frame | Grade 5 titanium, mirror-polished. Hinge cover is 3D-printed recycled titanium with a contrasting micro-blasted matte finish (Apple newsroom, Yanko Design) |
| Glass | Ceramic Shield 2 on outer display, Ceramic Shield on the camera-half back; both displays have rounded corners |
| Hinge | >100 components, variable torque (two-handed to open per 9to5Mac), magnet array holds it closed, holds "tent"/"seated" angles |
| Displays | 5.4" outer, 7.6" inner (nano-texture matte) |
| Rear cameras | Dual 48 MP (Main + Ultra Wide) in a horizontal plateau at the top of the camera half. Engadget: the module "spans the phone's full width so it sits on a table without rocking"; Apple's site places it in the top corner (landscape). Bump height is not published anywhere I could find — measure it. |
| Buttons (closed, portrait) | Volume up/down on the **top edge**; **side button with Touch ID** and **Camera Control** on the **right edge**; no Action button, no mute switch (MacRumors, TechPP, Apple spec diagram). USB-C bottom; speakers/mics top and bottom. |
| Magnets | Built-in MagSafe/Qi2 array (25 W) plus alignment magnet and accessory-ID NFC — a case does not need its own ring, it must only not block the phone's |
| Edge profile | Engadget: "rounded edges that make the phone easy to open." Yanko: asymmetric footprint — rounded corners on the opening edge, squared geometry at the hinge spine |
| Colors | Night Sky (deep navy), Star White |

Two facts that constrain a case more than anything else:

1. **Touch ID lives in the side button.** PetaPixel's reviewer: "you can't use a case that covers that button." Apple's own case has "a large notch for the Touch ID sensor and Camera Control" (The Verge via Daring Fireball). Your right edge needs an open notch, not button covers.
2. **The outer-display half is only ~5.2 mm thick and the hinge side has nothing to grab.** This is why nearly every commercial case (including Apple's) uses adhesive on the front frame. A community spreadsheet of 62 Duo cases found only about a dozen confirmed adhesive-free (PetaPixel).

A printed dummy exists: MOSS 3D's "iPhone Duo Replica with Magnetic Clasp" on MakerWorld (2,483 downloads) was built specifically to test case designs. rtkane's dimension mockup explicitly warns its camera/radii are approximated from press images and should **not** be used for case design. Treat both as go/no-go checks, not CAD truth; measure a real phone.

---

## 1. Existing iPhone Duo cases

Legend — Form: **2P** = two independent pieces, hinge open; **HC** = hinge cover (type noted); **1P-back** = back half only; **Folio**. Attach: **Adh** = adhesive strips; **Mag** = magnets; **Snap** = friction/clip. Prices USD list unless noted. "n/s" = not stated by any source found.

| Brand / model | Form | Materials | Attach | MagSafe | Thickness / weight | Stand | What reviewers say | Source |
|---|---|---|---|---|---|---|---|---|
| **Apple iPhone Duo Case** ($79, Sand / Navy Blue) | 2P, hinge exposed | Polycarbonate, matte coating (9to5Mac/The Shortcut call it silicone — PC per MacRumors/Macworld; feels grippy) | Adh strips inside both pieces + built-in alignment magnets | Yes, Qi2 25 W | n/s ("thin and light") | No | Adhesive area is "small and not aggressively sticky," no residue (PetaPixel hands-on). Reader backlash about adhesive; Apple's listing only mentions magnets, which caused confusion. Front piece is very thin on the hinge side. Large notch for Touch ID + Camera Control "looks like it belongs at the bottom" (Verge). Lip protects the dual cameras. | MacRumors, PetaPixel, Macworld, Verge/DF |
| **Apple iPhone Duo Folio with Kickstand** ($129, Taupe / Navy) | Folio, covers outer display | TechWoven fabric, metal kickstand hinges | Mag only, no adhesive | Yes, charges with stand open | "thick" enough that PetaPixel's EIC kept taking it off | Yes | Protects front/back glass but not the edges; front flap makes one-handed use impossible (MacRumors forum owner). | PetaPixel, MacRumors forum |
| **Spigen Air Fit Pro MagFit** ($59.99 on spigen.com; $34.99 at retail) | HC — rotating spring-loaded hinge cover that "automatically follows the folding motion"; **SecuLink** steel links anchor front and rear halves | PC/TPU, Air Cushion | Adh (ships with spare stickers — PetaPixel) | Yes | Spigen's thinnest full-hinge case; listing weight 74 g | No | Vortex Gaming 8-case test: good protection, passed drop test, all buttons cut out, but "plasticky" and a slight friction sound from the hinge cover. | spigen.com, iThinkDiff, Vortex |
| **Spigen Ultra Hybrid Pro (MagFit) / Pro S** ($39.99–44.99 retail; $59.99+ spigen.com) | HC (same spring hinge + SecuLink) | Clear PC + TPU, anti-yellowing | Adh | Yes (non-Mag version exists) | n/s | Pro S: 360° aluminum ring stand | Cheapest hinge-covered clear option. | iThinkDiff, The Shortcut |
| **Spigen Slim Armor Pro (S) MagFit** ($89.99 / $99.99) | HC + SecuLink | PC/TPU, raised camera edges | Adh | Yes, but Spigen warns some magnetic chargers may charge intermittently with the stand | 83 g listing | S: 360° stand | The Gadgeteer called it "the most coherent design" among rugged Duo cases ("looks like a small equipment case") but says the hinge bar and squared edges emphasise depth. 45-business-day lead time. | Gadgeteer, iThinkDiff |
| **Spigen Tough Armor Pro MagFit** ($69.99) | HC, raised edges | PC + TPU | Adh | Yes; hinge cover can block some magnetic accessories | 79 g listing | No | Bulkier; dedicated hinge protector "lies flat when open." | iGeeksBlog |
| **Spigen Nano Pop MagFit** ($54.99 spigen.com / $29.99 retail) | 2P, **open hinge** | PC insert under flexible TPU, dot-pattern side grip, two-tone | n/s (likely adh) | Yes | 57 g listing | No | Only Spigen Duo case without hinge cover; cheapest. | iThinkDiff |
| **dbrand Grip** ($54.90–59.90) | HC — **single strip of elastic polymer**, friction-welded to the back; "opens like a door, springs back on its own, magnets hold it shut"; no springs/screws so no "bulge" | Textured polymer, thousands of micro-dots | Front piece still uses adhesive (dbrand admits) | Yes | **2 mm** | No | Chamfered front lip for gesture navigation; dedicated Camera Control cutout usable when folded; camera bump protection. Praised as slim for a hinge case; marketing-only so far, no independent review. | dbrand.com, Android Headlines |
| **Mous Limitless Fold** ($94.99–98.99) | HC — **one-piece TPU bridge** spans the hinge joining both halves (a hinge-free version also exists) | Interlocking TPU + PC, aramid-reinforced front frame and back, microfibre lining, AiroShock corners | n/s | Yes, Qi2; magnets "70% stronger" | Back 1.65 mm; **41.5 g**; closed 85.7 x 119.9 x **18.15 mm** → adds ~6.9 mm folded | No | Positioned as middle ground between slim and rugged; no independent test found. Pre-order, ships Nov. | Mous, Man of Many, Macworld |
| **Mous Ultra Thin (aramid)** ($84.99) | 2P | Pure aramid, rigid | n/s | Yes | 1.65 mm back, 0.7 mm sides | No | Hinge coverage not confirmed by Mous. | Thinborne comparison |
| **Pitaka Edge** (back $59.99, front frame $54.99, bundle $109.99) | 2P (back + front frame sold separately) | 1500D aramid, "Mammoth Resin" | **Pre-installed anti-slip adhesive strips** | Yes (Amber magnet film) | 0.95–1.3 mm depending on source; 15.9–21 g | No | Very thin, strong magnets, separate Camera Control button. One Reddit owner had adhesive alignment problems; Macworld: hinge exposed; Vortex: weak MagSafe hold, no front protection on back-only SKU. One forum buyer received only the back piece. | Pitaka, Macworld, Vortex, Thinborne |
| **Thinborne 600D aramid** ($89.69) | 2P | 600D aramid, matte | Adh strips (extras included) | Yes | **0.9 mm**, ~22 g; adds ~1.8 mm folded | No | Vortex: premium feel, excellent grip, wide USB-C cutout, exposed buttons; no hinge protection. Includes glass protector. Thinborne says repeated removal weakens strips. | Vortex, Thinborne |
| **Latercase MagLock** ($69) | 2P or back-only | aramid (weave unspecified) | front uses adhesive; some owners use back only | Yes | ~1 mm, ~20 g | No | Chosen by owners who want to avoid adhesive by running back-only. | MacRumors forum, Thinborne |
| **Ridge iPhone Duo (Carbon/Kevlar)** ($99) | Unibody incl. hinge (Vortex: "front, back and hinge") | Kevlar/carbon weave + TPU bumpers, aluminum buttons | **Snaps on, no adhesive** | Yes | "adds little thickness"; n/s | No | Vortex: smooth folding, passed drop test, slim, good grip — but "plasticky." Ridge's own reviews: "can be slippery," some accidental Camera Control activation. 8 ft drop rating, 99-day trial. | Vortex, ridge.com, MacRumors forum |
| **Benks ArmorGrid Air Grand Combo** ($99.99–119.99) | 2P; "Hinge Protection" version adds an integrated magnet-guided hinge cover on the back shell | Kevlar back, PC front frame, glass protector | Adh strips (replacements included) | Yes | back 1.3 mm, 23.5 g | optional $29 ring | Vortex: very thin, good bezel height, passed drop test, priciest of the 2P set. Benks FAQ: check hinge cover "moves freely," don't force. | Macworld, Benks, Vortex |
| **Benks Grand Combo Crystal** | HC | Clear PC, corner airbags | n/s | Yes | 1.3 mm | No | Hinge protected, anti-yellowing. | Macworld |
| **OtterBox Lumen** ($69.99) | 2P clear (Macworld: "ports and hinge open"; Android Headlines says hinge protection — conflicting) | PC + TPU | Mag | Yes | 58 g | No | Not shipping yet at time of writing. | Macworld, Android Headlines |
| **OtterBox Defender Pro XT** ($64.96–89.99) | HC, articulating hinge, port covers | mostly TPU, rubber edges | n/s | Yes | 74 g | No | "Chunky"; max drop/dust protection. | Macworld, Android Headlines |
| **ESR Classic Hybrid / Atelier / Cyber Tough with Flex Stand** ($42.99–59.99) | HC | Hybrid PC/TPU; Atelier = silicone-leather | Mag (Cyber Tough) | Yes | back 1.5 / 2.3 / 2.5 mm | 180° metal Flex Stand | Gadgeteer: Atelier's big metallic camera collar "dominates the design." 40-business-day lead time. | Macworld, Gadgeteer |
| **Torras Ostand Q3 VegSkin / Q3 Spin** ($69.99–79.99) | HC (full hinge guard, black) | PC + silicone/VegSkin, aluminum ring stand | n/s | Yes, 18 N | **3.35 mm**, 46–53.7 g | 360° stand, folds flush | Gadgeteer: gold camera border + large ring + black hinge guard "pull the design in three directions." 1.2 mm screen/camera lips. | Gadgeteer, Man of Many |
| **UAG Mouve / Mouve XTE** ($64.95 / $84.95) | 2P translucent, open hinge | PC + TPU, air-soft corners | n/s | Yes | n/s | XTE: rotating ring | Gadgeteer: mix of rounded/flat/angular shapes "looks busy." | Macworld, Gadgeteer |
| **Zagg Crystal Palace Snap KS / Lite / Sedona Snap** ($69.99–89.99) | HC — Sedona has a **"magnetic stop-short hinge cover"** | graphene-reinforced clear | Snap + Mag | Yes | 2–3.5 mm | KS/Sedona | Lifetime replacement. | Macworld, The Shortcut |
| **UNIQ Keva Edge Slimline** ($89.90) | HC, magnetic hinge | aramid | n/s | Yes | 1.5 mm; camera bump 5.4 mm tall | No | — | Macworld |
| **Nomad Traditional Leather Folio** ($129) / **Mag Leather Back** ($59) | Folio / **1P-back** | Horween leather | Folio snaps; Back uses magnets + **reusable microsuction pads** | Yes | back 2.2 mm (folio 3.8) | No | Back-only is the most minimal; "not a drop-protection case." | Macworld, Android Headlines |
| **MOFT Dynamic Folio / MOVAS Modular** ($69.99) | Folio / 3-part (front frame, hinge, backplate — swappable colors) | origami fabric | Adh front frame + magnetic hinge/back | Yes | 1.9 mm | origami stand | Unique; no corner protection. | Macworld, Wallpaper |
| **Speck Presidio Perfect-Clear Fold** ($64.99) | 1P with **automatic hinge cover** | clear | n/s | Yes | n/s | No | — | Man of Many |
| **Casetify Impact** ($88) | HC | n/s | n/s | Yes | n/s | — | 100+ designs; no review. | Macworld, T3 |
| **Rokform Rugged** ($89.99) | HC, full-length | rugged PC/TPU | RokLock twist mount | — | **~86 g** | — | Gadgeteer: heavy, but bulk "serves a function." | Gadgeteer |
| **Mkeke Clear (one-piece) / TechWoven** ($19.99–35.99) | 1P joined through hinge / 2P | clear PC; woven fabric + PC front | TechWoven front frame uses **reusable 3M strips**; clear version has **no front adhesive** and Vortex says it "might feel a bit loose" | Yes | n/s | No | Cheapest; passed drop test. | Vortex, iThinkDiff |
| **Budget hinge-magnet designs** — BENTOBEN, SUPFINE, ORNARTO, STORMTAL, Raptic, FNTCASE, SPIDERCASE, MOBOSI, NINKI ($13–30) | HC — magnetic hinge cover that "attaches as the phone closes" (BENTOBEN tested 5,000 cycles) or reinforced guard joining both sides | PC + TPU | n/s | 38x N52 | 1.5 mm screen / 2.5 mm camera lips (FNTCASE, BENTOBEN); 1.8 mm TPU edges (BENTOBEN) | often | SUPFINE: magnetic chargers may not work when fully unfolded. Raptic: ratchet stand rated 3,000 openings. | iThinkDiff, iGeeksBlog |

Market-level takeaways from the Duo roundups:
- Two camps, cleanly split: **slim two-piece with the titanium hinge exposed** (Apple, Pitaka, Thinborne, Latercase, Benks Air, UAG, Nano Pop, Lumen) versus **hinge-covered** (Spigen spring/SecuLink, dbrand elastic polymer, Mous TPU bridge, ESR/Zagg/BENTOBEN magnetic covers, OtterBox articulating). Nobody has a rigid hinge cover that isn't bulky.
- **Adhesive is the norm, not the exception.** Apple, Spigen, Pitaka, Thinborne, Benks, dbrand (front piece), Mkeke TechWoven all use strips. Only Ridge (snap unibody), Zagg Snap, Nomad (microsuction) and Apple's Folio are confirmed adhesive-free among well-known brands.
- Reviewers' consistent complaints: bulk on an already 11.3 mm / 254 g phone; "plasticky" feel on PC; hinge-cover friction noise; magnetic wallets/batteries overhanging the short body; design incoherence (competing collars, rings and guards); long pre-order lead times. Macworld's roundup was done on a dummy — nobody has long-term adhesive or hinge-cover wear data yet.
- Macworld's checklist: precise fit, shock-absorbing corners, raised lips for both screens and camera, uncovered Touch ID and Camera Control, hinge covers trap grit so the case must come off for cleaning, adhesive may not re-stick.

---

## 2. What matters in a foldable case (lessons from the Galaxy Z Fold market)

Prioritized. The Z Fold market has 7 generations of case failures to learn from; the Duo is its first.

### P1 — Front-frame retention is the failure mode. Design for it first.
- 9to5Google's Fold 2 long-term diary: Spigen Thin Fit and Ultra Hybrid front pieces "won't stay put on the left [hinge] side of the screen even with adhesive"; frequent removal scratched the metal frame.
- Samsung Community (Fold 4 Slim Standing Case): "front part keeps coming off and is now damaging my phone." Best Buy/Walmart reviewers on several Fold cases: front half falls off; adhesive only on the inner part.
- Samsung's own support page admits "the adhesive side of the front left pad is relatively small" and strong force "may cause the adhesive side to fall off"; it recommends leaving the phone untouched after installation so the pad bonds.
- Spigen's answer on Fold 7 and Duo is **SecuLink**: steel links tying the front frame to the back shell through the hinge cover so the front can't separate on impact. dbrand still uses adhesive on the front even with its polymer hinge.
- MakerWorld designers converge on the same fix: Nyg's Fold 5 case "fits tight but like most fold cases benefits from a small piece of double-sided tape on the front screen portion"; ProjectSkyDroid "highly recommends thin double-sided 3M tape inside"; Yukizo's Fold 8 case is deliberately tape-mounted "instead of snap-fit edges, which is what keeps it this slim."
- Why: the front half is ~5 mm thick, three of its edges are glass-to-titanium with a sub-millimetre bezel, and the fourth edge is the hinge. A rigid frame has nowhere to hook.

**Implication for a PLA design:** either (a) skip the front frame entirely (Pitaka back-only, Nomad Mag Leather Back, Latercase users), (b) accept a reusable adhesive (3M 9448 / Command-type strips or Nano tape, with the recess for it modelled in), or (c) make the front frame flexible enough to clip — which means TPU, not PLA.

### P2 — Hinge strategy decides everything else
- Benks' (vendor) summary is fair: hinges are rated 200k cycles and long-term owners report no hinge failures without covers; early hinge guards "were bulky, created friction, or restricted the opening angle"; a cover's cutout "must match the exact device geometry or it restricts fold angle or leaves the spine uncovered." Out-of-warranty hinge repairs are $350–500.
- Independent reviewers treat an exposed hinge as an acceptable trade for thinness (Tom's Guide on Thinborne; Android Central on Spigen Thin Fit P — "no hinge protection at all" listed as the one caveat on an otherwise top pick).
- Working hinge-cover mechanisms in the wild: (1) spring-loaded rotating cover (Spigen) — too many parts for a print; (2) single elastic polymer flap held shut by magnets (dbrand) — needs TPU; (3) TPU bridge joining both halves (Mous) — needs TPU; (4) magnetic "stop-short" or "attaches as the phone closes" floating covers (Zagg Sedona, BENTOBEN, ESR, ORNARTO, Benks Grand Combo) — a rigid plate guided by magnets, **the only type that is realistic in PLA**; (5) rigid full-wrap articulating (OtterBox) — bulky.
- A Cults3D user summarised the rigid-cover problem: a full hinge guard "will be a hard case and if unfolded it will still be there and make bulk."

### P3 — Thickness and weight budget
- The Duo is already the thickest, heaviest foldable in its class (11.3 mm / 254 g vs Fold 8 9.7 mm / 201 g). The Gadgeteer: "the Duo's short, thick body leaves case makers little room." Every slim roundup leads with thickness: Thinborne 0.9 mm, Pitaka ~1 mm, Benks 1.3 mm, Mous 1.65 mm, dbrand 2 mm; Mous's full case brings closed thickness to 18.15 mm.
- Tom's Guide (Fold 7): "durability is usually directly proportional to thickness"; UAG/OtterBox criticized for weight; rugged Duo cases 46–86 g.
- Realistic PLA target: 1.2–1.6 mm back (3–4 perimeters at 0.42 mm), 1.6–2.0 mm side rails, total weight 20–30 g for a back shell.

### P4 — Lips: enough to protect, not enough to block gestures or the outer display
- Reported values: screen lip 1.2 mm (Torras), 1.5 mm (FNTCASE, BENTOBEN); camera lip 2.5 mm above back (FNTCASE/BENTOBEN); Pitaka's 0.38 mm camera lip criticized as too small; UNIQ's 5.4 mm camera bump noted as tall.
- Android Central: "I immediately dismiss any case that makes it difficult to use gestural navigation." dbrand solves this with a **chamfered front lip**; the Fold 7 Slim remix on MakerWorld adds "functional nubs making opening the inside screen much easier" and widened the screen cutout "for better fitment of tempered glass."
- Duo-specific: Thinborne notes a front frame can overhang the cover display and obscure content; iOS has a "Shift Left Edge" setting as a workaround. Keep the front bezel overlap ≤ the physical bezel.

### P5 — Buttons, Touch ID, Camera Control, ports
- Touch ID side button must be fully exposed (PetaPixel). Camera Control needs a cutout or a capacitive insert (dbrand Ghost uses a PCB; Ridge uses an "access button"; Ridge users report accidental activations). Apple's case: one large notch covering both.
- Volume rocker sits on the **top edge** when closed, so the top rail of a back shell is interrupted; Vortex praised cases with cutouts for all buttons and criticized none for exposed buttons.
- USB-C: 9to5Google found Spigen's Fold cutout "too small for many plugs"; the Fold 7 remix and Thinborne widened theirs. Allow ≥ 0.5–1 mm clearance beyond the plug body, and 2 mm extra around speaker/mic openings (Formlabs/Qidi guidance).

### P6 — Two-piece alignment and closing
- A 2P case closes onto itself: the hinge-side edges of the front frame and back shell meet when folded. Yukizo keeps the pieces "fully independent, so nothing interferes with the hinge"; littlelayerr's Voronoi shell has "clip height tuned to give the hinge room, so it doesn't strain the fold"; ProjectSkyDroid "fine-tuned to not interfere at all with the opening and closing" and tapered the front casing near the fingerprint sensor.
- rtkane's mockup models a "perimeter seam" between halves — the real phone's halves meet flush with magnets; any case material on the hinge-side edges stacks up in the closed gap. Relieve (chamfer or stop short) both hinge-side edges so the case never becomes the thing the magnets close onto.

### P7 — Grip and surface
- Praised: dbrand micro-dot texture; Spigen Nano Pop dot grip; Thinborne/Pitaka matte aramid weave; Android Central on Thin Fit P: "grippy rubber… yet not grippy enough to pull my pocket lining out." Criticized: Ridge "can be slippery"; plasticky PC (Spigen Air Fit Pro, Ridge).
- Several owners say the phone itself is "slippery" metal and glass (Android Headlines) — grip is a reason people case the Duo.

### P8 — MagSafe and accessories
- The phone carries its own magnet array; cases only need to stay thin over it. Yukizo's printed case adds a 0.5 mm recess for an optional magnet ring. Note that magnetic wallets/batteries "may hang off the bottom" of the short Duo (9to5Mac, Pitaka). Hinge covers can collide with some mounts (Tough Armor Pro).

### P9 — Camera plateau as a mechanical anchor (the thing PLA can do well)
- The Fold 7 QuadLock case: "push your phone in from the top till it clicks into the camera array, then click the bottom part of the phone in"; removal is the reverse. MOSS 3D's Duo case uses "a small retaining lip on the camera bump" to lock an insert. The Duo's full-width camera plateau at the top of the camera half is the biggest positive feature on the phone — a rigid shell can key on it.

### P10 — Kickstands
- Popular on Duo (Apple Folio, Spigen S, Torras, ESR, UAG XTE) but every reviewer counts them as bulk; Tom's Guide found Samsung's rounded stand "wobbles." Tent/tabletop modes already give the Duo its own stand. Skip unless the case is explicitly a desk accessory (eMotor's "tablet shell" on MakerWorld holds the Duo flat on a desk).

### Z Fold cases considered best-designed, and why
- **Spigen Thin Fit (P)** — Android Central's top pick for Fold 4/5: thin, grippy rubber, lips that protect without blocking gestures, side S Pen slot that doubles as a grip, adhesive strips pre-installed on the front frame; downside: no hinge cover, and 9to5Google saw the front piece fail on the Fold 2 version.
- **Thinborne 600D aramid** — Tom's Guide's slim pick: 0.9–1.0 mm, matte grip, two covers, glass protector, exposed hinge accepted as the trade.
- **Spigen Slim Armor Pro / Ultra Hybrid Pro (SecuLink)** — the reference for a full hinge cover that stays slim; Tom's Guide pick for drop protection; TechPP: Tough Armor Pro for max protection.
- **Samsung Carbon Shield (0.8 mm) / Clear Case (1 mm)** — OEM fit, anti-reflection films, but back-only, no magnets, and "reviews aren't that great" (TechPP).
- **UAG Mouve** — two-piece open-hinge with air-soft corners and MIL-STD rating; lighter than OtterBox.
- Mous and Ringke: no independent Z Fold reviews surfaced; Ringke is a budget clear 2P with no hinge coverage.

---

## 3. Shortlist: cases to steal from

1. **Apple iPhone Duo Case** — borrow: the proportions and split (a conventional back shell covering everything but the camera plateau, plus a narrow front bezel frame), matte low-sheen finish, two neutral colors that complement Night Sky / Star White, one generous notch for Touch ID + Camera Control, camera lip. Avoid: adhesive-only retention and the notch's "belongs at the bottom" look — align your notch's radii with the shell's corner radii so it reads as intentional.
2. **dbrand Grip (Duo)** — borrow: 2 mm total thickness as the ceiling, chamfered front lip for gestures, "seamless back plate" with no hinge bulge, micro-texture on the back and sides (in PLA: fuzzy skin on the side rails or a modelled dot/hex relief on the back), Camera Control cutout that works folded. The elastic-polymer hinge flap is only reproducible if you print a TPU strap on the AMS (MOSS 3D already mechanically interlocks TPU and PLA on the Duo).
3. **Ridge iPhone Duo** — borrow: the only well-known adhesive-free snap-on; proves a rigid-ish shell can grip the Duo by its corners/edges. Avoid: the slipperiness and "plasticky" surface (lesson: texture matters more than material).
4. **Spigen Air Fit Pro / Slim Armor Pro (SecuLink + rotating spring hinge)** — borrow: the principle of tying the front frame to the back so it cannot walk off, and the idea that a hinge cover should "lie flat when open" and follow the fold on its own. Also the most coherent rugged look per the Gadgeteer: one material, squared, equipment-case vibe. Avoid copying the mechanism — springs and steel pins don't print.
5. **Printed references: Yukizo's Galaxy Z Fold 8 case and littlelayerr's Duo Voronoi shell (MakerWorld)** — borrow: the two-piece, fully independent layout with nothing near the hinge; 18 g total; 0.5 mm magnet-ring recess; mic hole and **speaker alignment tabs** that locate the shell during installation; four low-profile clips (two hinge-side tabs, two rounded corner clips) with clip height tuned for hinge clearance; 100 % infill where ribs are thin. Yukizo's lesson that tape beats snap edges for thinness, and littlelayerr's that "thin PLA prints are fragile" (he pulled his two-piece front frame until he could refine it) are the two most honest data points about PLA foldable cases.

Honourable mentions: Mous Limitless Fold's single TPU bridge (if you go multi-material); Zagg Sedona/BENTOBEN magnetic "stop-short" hinge plates (the only rigid-hinge-cover concept that could print in PLA with embedded magnets); Thinborne for what a 0.9 mm shell looks like.

---

## 4. Visual design language takeaways

- **The phone's own language:** mirror-polished titanium rails, matte micro-blasted hinge band, rounded corners on the opening edge, squared spine, horizontal camera plateau across the top of the camera half, two sober colors. Yanko Design reads the asymmetry as a cue for which edge opens — keep the asymmetry visible (don't square the open edge or round the spine).
- **Coherence beats features.** The Gadgeteer's critique of the five "ugliest" Duo cases is the clearest design brief available: ESR's metallic camera collar "dominates," UAG's mix of "rounded, flattened and angular shapes looks busy," Torras' gold camera border + ring + black hinge guard "pull the design in three directions." The winner was Spigen's single-material, squared "equipment case." Rule: one material read, one color, one radius family, and let the camera plateau be the only accent.
- **Edge radii:** match the shell's outer corner radius to the phone's corner radius plus wall thickness (constant offset) so the case looks like a thicker phone, not a box around one. Reviewers reward "fits like a glove / feels like no case" (Ridge reviews, Android Central).
- **Flat vs rounded sides:** the Duo's rounded edges "make it easy to open" (Engadget). A full-round side rail hides layer lines poorly in FDM; a flat side with a 1–1.5 mm fillet top and bottom prints cleanly, reads as deliberate, and echoes the squared spine. dbrand's chamfer is the gesture-friendly version of this.
- **Camera framing:** follow the plateau's own outline at a constant 1–1.5 mm offset, raised 0.5–1 mm above the lens glass; avoid a contrasting metal-look collar. A full-width plateau cutout also lets the case sit flat on a table like the bare phone does.
- **Finish:** matte everywhere. Matte PLA (Bambu Matte, Polyterra) in Sand/greige, navy, or charcoal pairs with both Duo colors; the glossy frame peeking through the notch provides contrast for free. Textured build plate for the back face, fuzzy skin or a modelled micro-dot field on the side rails for grip.
- **Small details reviewers notice:** button cutouts with the same radius as the shell corners; a USB-C opening wide enough for any plug; speaker grille slots aligned with the phone's; no seam on the back (print the back shell as one part).

---

## 5. 3D-printing-specific findings

### Existing open designs (state of the art as of Nov 2026)
| Design | Platform | Approach | Notes |
|---|---|---|---|
| MOSS 3D — iPhone Duo TPU Phone Case, Customisable | MakerWorld 3450347 (541 dl, 39 comments) | Single back shell; **TPU 68D (AMS) + PLA** backplate with a modelled "structural weave" that mechanically locks the two plastics; volume buttons attached to a camera-bump insert that locks into the camera hole; SVG modifiers for patterns; optional MagSafe cutout | 0.2 mm layers, 100 % infill, 2 walls, dry TPU; "only tested on a dummy… may fit a little tight or loose on the actual device." Insert the phone **open**, press each corner. |
| littlelayerr — Duo Hex Case PLA, Open Side Design | MakerWorld 3452741 | Single-piece PLA back shell | "My initial version used a two-piece layout, but thin PLA prints are fragile, so I removed it… Small adhesive may be best, but not required." 9 g. |
| littlelayerr — Duo Voronoi Shell | MakerWorld 3500319 | PLA back-half only; **two hinge-side tabs + two rounded corner clips**, no glue; clip height tuned for hinge clearance | Print flat, clips up, no supports, 100 % infill ("ribs are thin"), ~10 g. "If the clips are tight, try a slightly lower first-layer squish." |
| 王的A1 — iPhone Duo TPU 95A case | MakerWorld 3338982 | Full-wrap TPU 95A from a 3D scan of a dummy | Author: needs double-sided tape to stay on. 42 g. |
| Andres B — iPhone Duo Case (prototype) | MakerWorld 3345469 | 2P shells joined by a **sliding hinge protector** with hinge barrels, internal sliding guides, separate pins | Needs supports, test fit samples first; "designed around a user-supplied dummy, not official Apple CAD… fit on a production phone is not confirmed." |
| Byron Coughlin — iPhone Duo Quad Lock Case | MakerWorld 3525593 | Back shell with QuadLock tab | PETG, 8 walls, 100 % infill, tree supports, 67 g. |
| MOSS 3D — iPhone Duo Replica with Magnetic Clasp | MakerWorld 3296598 (2,483 dl) | Folding dummy with 6x3 mm magnets, built "as I've been working on a case for the Duo" | Best available test article short of a phone. |
| rtkane — Duo Size & Dimension Mockups | MakerWorld 3285874 | Solid open/folded blocks from Apple's published dims | Explicitly **not** for case design. |
| Yukizo — Galaxy Z Fold 8 Case | MakerWorld 3162392 (528 dl, 505 prints) | Slim 2P (back + cover-screen frame), **tape-mounted**, 18 g total, 0.5 mm magnet-ring recess, raised camera area, mic hole, speaker alignment tabs | 0.08 mm layers, 2 walls, 100 % infill, no supports. |
| quickfixrepairs.nl — Z Fold 7 QuadLock case | MakerWorld 2172095 | PLA back shell that **clicks onto the camera array first, then the bottom snaps in** | 0.16 mm, 2 walls, 5 % honeycomb "for drop protection." |
| ucdbadboy — Fold 7 Front Case Slim remix | MakerWorld 1791536 | PLA front frame | "The lip is not easy to print due to the overhang"; 0.4 mm nozzle, print slow, +5 °C, PETG as support interface for PLA; 4 walls; widened screen cutout for glass; nubs to help open; thickened the left (hinge-side) edge 15 % "to enhance durability." |
| ProjectSkyDroid — Fold 5 case with S Pen | MakerWorld 179837 | Full front + back, PLA-CF / PETG-CF | "Very tight tolerances"; recommends thin 3M tape inside; tapered front near fingerprint sensor; expanded screen opening 1 mm in v2.1; used daily for months in PLA-CF. |
| Nyg — Fold 5 slim case | MakerWorld 166302 (1,885 dl) | Slim PLA, 6 walls | "Fits tight but… benefits from a small piece of double-sided tape on the front screen portion." |
| JernejP — Galaxy Fold 3 case MK3 (top + bot STLs) | Printables 77055 | 2P PETG with stand and car-mount plate | PETG 0.2 mm, 0.4 nozzle. |
| tryptech / catly1 — Fold 3 case with stand + S Pen | Printables 139457 | back.stl + cover.stl | PLA, 20 % infill; front cover needs supports, back doesn't; bottom edge cut away for gesture nav, top for earpiece. |

No Printables/Thingiverse/Cults3D iPhone Duo case was found; the Duo work is all on MakerWorld (Bambu-centric community, which suits a P1S).

### Geometry and tolerance numbers to start from (then calibrate with a fit coupon)
- FDM parts come out 0.1–0.3 mm larger than nominal; PLA dimensional tolerance ≈ ±0.15 mm (PrintPal). Fit classes per side, 0.4 mm nozzle: press 0.05–0.10, snug 0.10–0.20, sliding 0.20–0.30, moving 0.30–0.50 mm (PrintPal). Phone-case vendors suggest 0.2–0.3 mm/side for snap-fit TPU and 0.3–0.5 for friction-fit TPU; a rigid PLA shell wants the tight end (0.1–0.2) over the glass back and a hair more around the titanium rails.
- Walls: one line ≈ 0.45 mm; two perimeters ≈ 0.9 mm minimum for shape; four ≈ 1.8 mm for functional parts (PrintPal). Reinforce corners to 3–4 mm where impacts land (Qidi). The printed Fold cases that lasted used 4–8 walls or 100 % infill in thin regions.
- Lips: 0.5–1.0 mm proud of the lens glass for the camera; 1.0–1.5 mm around the outer display (commercial 1.2–1.5 mm), chamfered 30–45° on the inside for gestures. Port: +0.5–1 mm clearance around a USB-C plug body; +2 mm around speaker/mic (Formlabs).
- Snap clips (Formlabs, Markforged, Fictiv): make the cantilever long and low with a tapered (trapezoidal) profile and a curved root; engagement 1.2 mm is typical, 2 mm for a firmer lock; add a lead-in chamfer (≈ 0.4 mm on a 0.4 mm interference lip in PrintPal's generic example); **print snap features lying flat so the flex is in the XY plane** — a cantilever printed along Z loses about half its elongation at break and 20–30 % tensile strength and will shear after repeated use. Keep PLA clips to the minimum strain that still retains (littlelayerr's "four low-profile clips"); PETG "bends before it breaks" and is the safer choice for the clip-bearing part if you can tolerate a slightly glossier look.
- Hinge-side edges: the two shells' hinge-side rails must stop short of the hinge cover and be chamfered so they never contact the titanium cover at any fold angle; test at 0°, ~90° (tent), ~120° (seated) and 180°.
- Printability: back shells print face-down on a textured plate without supports; the front frame's inward lip is the hard part (overhang) — orient it lip-up and print slow, or split the lip into a separate thin ring. Use 0.08–0.16 mm layers for the thin regions. Elephant's foot: 0.3–0.5 mm chamfer on the plate-side edge.
- Materials on a P1S: PLA Matte for the look; PLA-CF prints cleanest and has held up months in daily use on a Fold 5 (ProjectSkyDroid), but it's abrasive (hardened nozzle) and stiffer/more brittle for clips. PETG for the clip-bearing piece. TPU 68D–95A via AMS (slow, must be dry) if you want a flexible hinge strap or a soft inner liner like MOSS 3D's hybrid.
- Protecting the phone: line clip tips and the inside of the rails with 0.3–0.5 mm of flocking/felt or a TPU insert; several owners report rigid cases scratching the frame on removal (9to5Google, Reddit on eBay cases). The polished titanium will show every PLA burr — deburr and consider a microfibre liner (Mous does this).

### A split-line plan that follows the evidence
1. **Back shell (PLA, the hero part):** one-piece, wraps the camera half's back and three rails, keyed to the camera plateau (click top in first, QuadLock-style), two low corner clips at the bottom, hinge-side edge stopped 0.5 mm short of the hinge cover and chamfered. Volume-button cutouts in the top rail, Touch ID/Camera Control notch in the right rail with shell-matching radii, oversize USB-C and speaker slots. 1.2–1.5 mm back, 1.8 mm rails. Optional 0.5 mm MagSafe ring recess.
2. **Front frame (optional, PETG or TPU):** thin bezel frame with a chamfered lip, two hinge-side tabs and two corner clips à la littlelayerr, plus a modelled 0.3 mm recess for a reusable adhesive strip on the long edge opposite the hinge — because every source says the front frame will migrate otherwise. Or omit it and ship as a back-only design like Pitaka's and Nomad's.
3. **Hinge:** leave exposed in v1. If a cover is wanted later, a floating rigid PLA plate held by two embedded 6x3 mm magnets (Zagg/BENTOBEN pattern) is the only variant that doesn't need TPU or springs.
4. **Fit coupons first:** print the bottom 8 mm of the back shell and the camera key as a test ring before any full print; the Instructables PLA case author's method was to undersize and sand to fit.

---

## 6. Sources

iPhone Duo product facts
- Apple — iPhone Duo Technical Specifications: https://www.apple.com/iphone-duo/specs/
- Apple — iPhone Duo product page: https://www.apple.com/iphone-duo/
- Apple Newsroom — Apple unveils iPhone Duo: https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/
- Tech Advisor — final name of Apple's foldable: https://www.techadvisor.com/article/3216596/what-is-the-final-name-for-apples-iphone-ultra-foldable.html
- Gigazine — internally called iPhone Ultra: https://www.gigazine.net/gsc_news/en/20260812-iphone-ultra
- MacRumors — iPhone Duo doesn't have an Action Button: https://www.macrumors.com/2026/09/09/iphone-duo-doesnt-have-an-action-button/
- TechPP — iPhone Duo hidden details: https://techpp.com/2026/09/13/iphone-duo-hidden-details/
- TapSmart — iPhone Duo volume buttons: https://www.tapsmart.com/tips-and-tricks/iphone-duo-volume-buttons/
- 9to5Mac — iPhone Duo review: https://www.9to5mac.com/2026/10/21/iphone-duo-review/
- PetaPixel — iPhone Duo review: https://petapixel.com/2026/10/21/iphone-duo-review-a-compromise-but-not-compromised/
- Engadget — iPhone Duo hands-on: https://engadget.com/2254389/iphone-duo-hands-on-apple-s-most-exciting-device-in-a-decade/
- Yanko Design — iPhone Duo design analysis: https://www.yankodesign.com/2026/09/09/the-iphone-duo-just-killed-the-dynamic-island-the-sim-tray-and-the-demand-for-an-ipad-mini/
- Daring Fireball — The Verge's Duo review (quotes): https://daringfireball.net/linked/2026/10/23/the-verge-iphone-duo-review
- iCulture — eerste indruk iPhone Duo: https://www.iculture.nl/nieuws/eerste-indruk-iphone-duo/
- 3D Printing Industry — Apple's 3D-printed hinge: https://3dprintingindustry.com/news/apple-brings-two-distinct-3d-printing-processes-to-the-hinge-of-its-first-foldable-iphone-254601/

Apple's cases
- MacRumors — Apple's $79 iPhone Duo Case sticks on with adhesive: https://macrumors.com/2026/10/16/iphone-duo-case-adhesive/
- PetaPixel — Apple's iPhone Duo case has adhesives and that's normal: https://petapixel.com/2026/10/22/apples-iphone-duo-case-has-adhesives-and-thats-actually-normal/
- PCGuide — Apple unveils official iPhone Duo cases: https://www.pcguide.com/news/apple-unveils-official-iphone-duo-cases-with-two-designs-and-two-colors-each-starting-from-79/
- PhoneArena — Apple case requires glue: https://www.phonearena.com/news/Apples-new-79-iPhone-Duo-case-requires-actual-glue-to-stay-on-your-phone_id184121
- GSMArena — two official first-party cases: https://www.gsmarena.com/iphone_duo_gets_two_official_firstparty_cases_here_they_are-news-74547.php
- Thinborne (competitor) — Apple iPhone Duo case review: https://thinborne.com/blogs/buyers-guide/apple-iphone-duo-case-review-is-it-worth-your-80

iPhone Duo third-party case roundups and reviews
- Macworld — Best iPhone Duo cases (tested on dummy): https://macworld.com/article/3239288/best-iphone-duo-cases-slim-protective-and-kickstand-options.html
- Macworld — The perfect iPhone Duo case doesn't exist (Spigen iBook concept): https://www.macworld.com/article/3232659/the-perfect-iphone-duo-case-doesnt-exis.html
- Vortex Gaming — 8 iPhone Duo cases compared (drop tests): https://vortexgaming.io/en/postdetail/1295832
- The Gadgeteer — the ugliest iPhone Duo cases (design critique): https://the-gadgeteer.com/?p=533767
- iGeeksBlog — Best iPhone Duo cases: https://www.igeeksblog.com/best-iphone-duo-cases/
- iThinkDiff — Best iPhone Duo cases 2026: https://www.ithinkdiff.com/best-iphone-duo-cases-2026/
- iThinkDiff — 4 best Spigen iPhone Duo cases (hinge/SecuLink explained): https://www.ithinkdiff.com/best-spigen-iphone-duo-cases-2026/
- The Shortcut — Best iPhone Duo cases: https://www.theshortcut.com/p/best-iphone-duo-cases
- Android Headlines — Best Apple iPhone Duo cases: https://www.androidheadlines.com/best-apple-iphone-duo-cases
- Man of Many — Best iPhone Duo cases (Mous Limitless Fold detail): https://manofmany.com/tech/smartphones/best-iphone-duo-cases-australia
- Wallpaper — seven accessories for the iPhone Duo: https://www.wallpaper.com/tech/these-seven-accessories-for-the-new-apple-iphone-duo-make-the-most-of-the-folding-form
- Tom's Guide — 9 iPhone Duo cases: https://www.tomsguide.com/phones/iphones/your-iphone-duo-deserves-better-than-a-cheap-case-here-are-9-life-savers
- T3 — iPhone Duo cases: https://www.t3.com/tech/iphones/iphone-duo-cases-that-make-your-folding-phone-look-mighty-fine
- Gizmochina — 7 cases for the iPhone Duo: https://www.gizmochina.com/2026/10/22/7-cases-for-the-iphone-duo-from-slim-to-rugged/
- TechRadar — best iPhone Duo cases: https://www.techradar.com/phones/phone-accessories/best-iphone-duo-cases
- Smartish — iPhone Duo case guidance (not Duo-tested): https://smartish.com/blogs/news/best-iphone-duo-case-top-picks-for-protection-hinge-coverage-and-magsafe
- MacRumors forum — iPhone Duo: using a case or not (owner reports): https://forums.macrumors.com/threads/iphone-duo-using-a-case-or-not.2491996/
- 9to5Mac — dbrand's iPhone Duo lineup (sponsored): https://9to5mac.com/2026/09/15/dbrand-has-iphone-duo-iphone-18-pro-covered-with-huge-range-of-designs/
- GadgetReview — PITAKA's Duo case (promotional): https://www.gadgetreview.com/?p=411715
- Thinborne (competitor) — Pitaka Duo case review: https://thinborne.com/blogs/buyers-guide/pitaka-iphone-duo-case-review-features-what-people-say-honest-verdict
- Thinborne (competitor) — Thinborne vs Mous Duo: https://thinborne.com/blogs/buyers-guide/thinborne-vs-mous-iphone-duo-case-what-makes-the-ultra-thin-cases-different
- Thinborne (competitor) — Latercase Duo review: https://thinborne.com/blogs/buyers-guide/latercase-iphone-duo-case-review-features-what-people-say-honest-take

Manufacturer pages (marketing — verify claims)
- Spigen — iPhone Duo page (SecuLink, rotating hinge cover): https://www.spigen.com/pages/iphone-duo
- Spigen — iPhone Duo collection: https://www.spigen.com/collections/iphone-duo-cases
- Spigen — Air Fit Pro Mag Fit: https://www.spigen.com/products/iphone-duo-case-air-fit-pro-mag-fit
- Spigen — Nano Pop Mag Fit (open hinge): https://www.spigen.com/products/iphone-duo-case-nano-pop-mag-fit
- dbrand — iPhone Duo Grip Case (elastic polymer hinge, 2 mm, chamfered lip): https://dbrand.com/shop/grip/iphone-duo-cases
- Ridge — iPhone Duo Case Carbon: https://ridge.com/products/iphone-duo-case-carbon
- Mous — Limitless (Fold) product page: https://eu.mous.co/en-at/products/limitless-phone-case-aramid-fibre
- Benks — ArmorGrid Air Grand Combo with hinge protection: https://www.benks.com/en-fr/products/grand-combo-hinge-protection-armorgrid-air-obsidian-black-case-built-with-kevlar%C2%AE-for-iphone-duo
- Benks — do you need hinge protection (vendor blog): https://www.benks.com/ko-au/blogs/benks-blog/foldable-phone-hinge-protection-do-you-actually-need-it
- OtterBox — Lumen Series iPhone Duo: https://www.otterbox.ca/products/iphone-duo-lumen-series-case
- ESR — iPhone Duo cases: https://www.esrtech.com/en-fr/collections/iphone-duo-cases
- Pitaka Edge (retail listing): https://gadgetandgear.com/product/pitaka-edge-ultra-slim-case-for-iphone-duo

Galaxy Z Fold case lessons
- Tom's Guide — Best Galaxy Z Fold 7 cases: https://www.tomsguide.com/phones/samsung-phones/best-samsung-galaxy-z-fold-7-cases
- TechPP — Galaxy Z Fold 7 cases: https://techpp.com/2025/08/06/galaxy-z-fold-7-cases/
- Android Central — Spigen Thin Fit P for Galaxy Z Fold review: https://androidcentral.com/accessories/spigen-thin-fit-p-for-galaxy-z-fold-review
- Android Central — Spigen Thin Fit for Z Flip review (hinge exposed): https://androidcentral.com/spigen-thin-fit-galaxy-flip-review
- 9to5Google — Galaxy Z Fold 2 cases diary (front piece failures): https://9to5google.com/2021/05/11/galaxy-z-fold-2-cases-diary/
- 9to5Google — Spigen's Z Fold 7 cases / SecuLink (sponsored): https://9to5google.com/2025/07/09/spigens-new-galaxy-z-fold-7-cases-might-be-the-perfect-option/
- Samsung Support — remove the case on Galaxy Z Fold (front-left pad is small): https://www.samsung.com/sg/support/mobile-devices/remove-the-case-or-cover-on-the-galaxy-z-flip-and-z-fold-series/
- Samsung Community — Z Fold 4 Slim Standing Case front keeps coming off: https://eu.community.samsung.com/t5/galaxy-z-fold-z-flip/z-fold-4-slim-standing-case/td-p/8255925
- Spigen — Galaxy Z Fold 7 Ultra Hybrid Pro MagFit: https://www.spigen.com/products/galaxy-z-fold-7-case-ultra-hybrid-pro-magfit
- Thinborne (vendor) — best Z Fold 7 case: https://thinborne.com/blogs/buyers-guide/whats-the-best-samsung-galaxy-z-fold-7-case
- The Z Fold Case (vendor) — top 10 Z Fold 7 brands compared: https://thezfoldcase.com/blogs/news/top-10-z-fold-7-case-brands-compared-spigen-pitaka-the-z-fold-case-amp-more
- Foldify (vendor) — hinge cover cases: https://foldifycase.com/blogs/news/best-galaxy-z-fold-7-hinge-cover-case-2026
- Android Authority — official Z Fold 7 case renders (back-only lineup): https://www.androidauthority.com/galaxy-z-fold-7-official-case-renders-leak-3573719

3D-printed designs
- MakerWorld — MOSS 3D, iPhone Duo TPU Phone Case – Customisable: https://makerworld.com/en/models/3450347
- MakerWorld — littlelayerr, Duo Hex Case PLA – Open Side Design: https://makerworld.com/en/models/3452741
- MakerWorld — littlelayerr, iPhone Duo Case – Voronoi Shell: https://makerworld.com/en/models/3500319
- MakerWorld — 王的A1, iPhone Duo TPU 95A case: https://makerworld.com/en/models/3338982
- MakerWorld — Andres B, iPhone Duo Case (sliding hinge protector prototype): https://makerworld.com/en/models/3345469
- MakerWorld — Byron Coughlin, iPhone Duo Quad Lock Case: https://makerworld.com/en/models/3525593
- MakerWorld — MOSS 3D, iPhone Duo Replica with Magnetic Clasp (test dummy): https://makerworld.com/en/models/3296598
- MakerWorld — rtkane, iPhone Duo Size & Dimension Mockups: https://makerworld.com/en/models/3285874
- MakerWorld — logikal, iPhone Duo folding mockup: https://makerworld.com/en/models/3286427
- MakerWorld — eMotor, iPhone Duo flat "tablet" shell: https://makerworld.com/en/models/3506117
- MakerWorld — Yukizo, Galaxy Z Fold 8 Case (tape-mounted 2P, 18 g): https://makerworld.com/en/models/3162392
- MakerWorld — quickfixrepairs.nl, Z Fold 7 QuadLock case (clicks onto camera array): https://makerworld.com/models/2172095
- MakerWorld — ucdbadboy, Fold 7 Front Case Slim remix: https://makerworld.com/en/models/1791536
- MakerWorld — ProjectSkyDroid, Fold 5 case with slim pen holder: https://makerworld.com/models/179837
- MakerWorld — Nyg By Design, Galaxy Fold 5 case: https://makerworld.com/models/166302
- MakerWorld — The Printing Pilot, Z Fold 7/8 charging dock (hinge-cover variant): https://makerworld.com/models/1702979
- Printables — JernejP, Galaxy Fold 3 case MK3: https://www.printables.com/model/77055-samsung-galaxy-fold-3-case-mk3-with-a-built-in-sta
- Printables — tryptech, Galaxy Z Fold 3 case with stand and S Pen slot: https://printables.com/model/139457-samsung-galaxy-z-fold-3-case-with-built-in-stand-a
- Printables — rainbowvcd, Z Fold 6 cover (TPU): https://www.printables.com/model/971587-z-fold-6-cover
- Cults3D — user comment on rigid hinge guards: https://cults3d.com/en/users/PTMN/comments

3D-printing design guidance
- PrintPal — Designing for 3D printing (fit classes, walls, chamfers): https://printpal.io/docs/3d-printing-design-guide
- Formlabs — Designing 3D-printed snap-fit enclosures: https://formlabs.com/blog/designing-3d-printed-snap-fit-enclosures/
- Markforged — 3D printed joinery (print snap fits lying down): https://markforged.com/resources/blog/joinery-onyx
- Fictiv — plastic hinge with snap-fit pin: https://www.fictiv.com/articles/fictivmade-7-hinge-design
- Qidi — printing TPU phone cases (clearances, lips): https://qidi3d.com/de/blogs/print-lab/tpu-phone-cases
- Instructables — 3D Printed Smartphone Case (PLA, undersize and sand): https://www.instructables.com/3D-Printed-Smartphone-Case
- GrabCAD — iPhone case interference fit discussion: https://grabcad.com/questions/iphone-case-interference-fit
- Printables — snap-fit hinge wallet (PLA flex lesson): https://www.printables.com/model/142692-snap-fit-hinge-wallet-card-case
