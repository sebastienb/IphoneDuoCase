"""
Parametric iPhone Duo two-shell case generator for Blender (5.x, headless).

Run:
    blender --background --python case/duo_case.py -- --out build

Geometry source: Apple "iPhone Duo Dimensional Drawings" (2026-09-09), see research/iphone-duo-specs.md.

Frame used for the phone (closed):
    x: 0 at the hinge spine exterior  ->  84.10 at the free edge
    y: 0 at the bottom edge           ->  117.80 at the top edge   (helper yt() converts "from top" values)
Each shell is built in its own local frame where z = 0 is the shell's OUTER surface (the print bed) and
+z points toward the phone's inner (folding) face. Both shells therefore come out print-ready, bed-side down.
The camera collar (camera_ring.stl) is printed on its flat top and glued onto shell A around the plateau.
"""
import bpy, bmesh, math, sys, os
from mathutils import Vector

# ----------------------------------------------------------------------------- parameters (mm)
P = dict(
    # phone
    W=84.10, L=117.80, half_T=5.48, gap=0.34,
    corner_a=17.31, corner_n=3.0,       # free-side squircle corners
    hinge_r=3.2,                        # hinge-side plan corners
    roll=2.74,                          # edge roll on each face
    # case
    wall=1.6,                           # side wall thickness
    back_T=1.8,                         # shell A back panel (<= 2.1 for MagSafe)
    lip_T=1.0,                          # shell B bezel thickness above the display glass
    lip_W=2.4,                          # shell B bezel width over the display (<= 3.06)
    clearance=0.15,                     # radial clearance phone <-> cavity
    cavity_chamfer=1.05,                # printable 45deg fill of the phone's edge roll (must be <= ~1.1)
    outer_chamfer=0.8,                  # chamfer on the bed-side outer edge
    rim_chamfer=0.4,                    # chamfer at the wall rim
    rim_setback=0.25,                   # wall stops this far short of the phone's inner face
    hinge_clear=2.7,                    # shells end this far from the spine exterior
    # feature clearances
    cut_clr=0.30,                       # clearance on cut-outs, also the vertical margin over the camera blend
    notch_r=2.0,                        # corner radius of the speaker / mic notches
    port_bridge=1.0,                    # wall material kept on the floor side under port notches
    hinge_edge_chamfer=0.7,             # relief chamfer on the hinge-side cut edge (bed side); keep != outer_chamfer
    lip_chamfer=0.6,                    # 45deg chamfer on the inside edge of shell B's bezel (gestures)
    adhesive_recess=0.3,                # depth of pockets for reusable nano-tape / microsuction pads
    adhesive_pad=(10.0, 18.0),          # pad pocket size (x, y)
    # retention
    grip_rib=dict(proud=0.25, length=8.0),              # ribs inside the walls; interference = proud - clearance
    magsafe_ring=dict(od=55.6, id=44.4, depth=0.7),     # recess for a stick-on MagSafe ring: 55 OD / 45 ID / 0.6 thick + 0.3 radial, 0.1 depth clearance (None = off)
    # camera collar (separate part, glued on)
    camera_ring=True,
    ring_lip=0.6,                       # collar top stands this far above the plateau top face
    ring_out=7.0,                       # collar outer edge, from the plateau top edge (keep < 7.5: MagSafe puck)
    ring_chamfer=0.5,
    coupon_h=10.0,                      # height of the fit-test coupon cut from the bottom of each shell
    N_corner=28,                        # points per corner curve
)

# -------- feature positions (phone frame, "yt" = from top edge, "xf" = from free edge)
F = dict(
    # Shell A (camera half). The plateau TOP face is a stadium; a blend ~8.8 wide slopes down to the glass
    # on the sides facing the phone centre (Detail D: top face x 4.94..60.56, toe x ..69.37, y ..34.62).
    plateau=dict(xf0=4.94, xf1=60.56, yt0=4.70, yt1=25.80, h=3.64, blend=8.8, lens_h=5.72),
    lenses=[(15.25, 15.25), (32.98, 15.25)], lens_d=16.20,                 # (xf, yt)
    side_button=dict(yt=42.87, length=18.67, r=3.10),                      # Touch ID keep-out, must stay open
    camera_control=dict(yt=84.97, length=28.26, r=2.44),                   # thin-case keep-out
    volume=dict(x0=44.35, x1=68.61, r=2.0),                                # both buttons, one slot (x from hinge)
    bottom_ports_A=[dict(x0=16.4, x1=25.9), dict(x0=59.5, x1=69.0)],       # mic + 8 ports, mic + 3 speaker ports
    magsafe=dict(xf=41.30, yt=61.31, d=61.50),
    ribs_A=dict(top=[15.0, 33.0], bottom=[10.0, 33.0, 50.0], free=[8.0, 56.0, 95.0]),
    # Shell B (display half)
    usb_c=dict(x=42.70, width=12.45),
    receiver=dict(x0=44.0, x1=54.5, r=1.5),
    ribs_B=dict(top=[15.0, 33.0, 62.0], bottom=[10.0, 25.0, 60.0], free=[8.0, 40.0, 60.0, 95.0]),
)

# ----------------------------------------------------------------------------- outline helpers
def yt(v):  # "from top" -> frame y
    return P['L'] - v

def dedupe(pts):
    out = []
    for p in pts:
        if not out or abs(p[0] - out[-1][0]) > 1e-6 or abs(p[1] - out[-1][1]) > 1e-6:
            out.append(p)
    if len(out) > 1 and abs(out[0][0] - out[-1][0]) < 1e-6 and abs(out[0][1] - out[-1][1]) < 1e-6:
        out.pop()
    return out

def superellipse_arc(cx, cy, a, n, t0, t1, k):
    pts = []
    for i in range(k + 1):
        t = math.radians(t0 + (t1 - t0) * i / k)
        c, s = math.cos(t), math.sin(t)
        x = cx + a * math.copysign(abs(c) ** (2.0 / n), c)
        y = cy + a * math.copysign(abs(s) ** (2.0 / n), s)
        pts.append((x, y))
    return pts

def base_outline():
    """Closed-phone plan outline, CCW, starting on the bottom edge just right of the hinge corner."""
    W, L, a, n, r, k = P['W'], P['L'], P['corner_a'], P['corner_n'], P['hinge_r'], P['N_corner']
    pts = []
    pts += superellipse_arc(W - a, a, a, n, 270, 360, k)          # bottom-right squircle
    pts += superellipse_arc(W - a, L - a, a, n, 0, 90, k)         # top-right squircle
    pts += superellipse_arc(r, L - r, r, 2.0, 90, 180, k // 2)    # top-left round
    pts += superellipse_arc(r, r, r, 2.0, 180, 270, k // 2)       # bottom-left round
    return dedupe(pts)

BASE = base_outline()

def offset_outline(d):
    """Normal offset of the base outline by d (positive = outward)."""
    pts = BASE
    m = len(pts)
    res = []
    for i in range(m):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[(i + 1) % m]
        tx, ty = x1 - x0, y1 - y0
        ln = math.hypot(tx, ty)
        nx, ny = ty / ln, -tx / ln            # outward normal for CCW
        px, py = pts[i]
        res.append((px + nx * d, py + ny * d))
    return res

def rrect_pts(u0, u1, v0, v1, r, segs=12):
    """Rounded rectangle, CCW in (u, v). r is clamped so a full radius gives a stadium."""
    r = max(0.0, min(r, (u1 - u0) / 2.0, (v1 - v0) / 2.0))
    pts = []
    for cu, cv, a0 in ((u1 - r, v0 + r, 270), (u1 - r, v1 - r, 0), (u0 + r, v1 - r, 90), (u0 + r, v0 + r, 180)):
        if r == 0:
            pts.append((cu, cv)); continue
        for i in range(segs + 1):
            t = math.radians(a0 + 90.0 * i / segs)
            pts.append((cu + r * math.cos(t), cv + r * math.sin(t)))
    return dedupe(pts)

def stadium_pts(x0, x1, y0, y1, d=0.0):
    """Full-radius stadium filling the box, grown by d on every side."""
    r = min(x1 - x0, y1 - y0) / 2.0 + d
    return rrect_pts(x0 - d, x1 + d, y0 - d, y1 + d, r, segs=16)

def circle_pts(cx, cy, r, segs=72):
    return [(cx + r * math.cos(2 * math.pi * i / segs), cy + r * math.sin(2 * math.pi * i / segs)) for i in range(segs)]

# ----------------------------------------------------------------------------- mesh helpers
def mesh_from_bm(name, bm):
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob

def sweep(name, rings, closed=False):
    """rings: list of (z, pts) with equal point counts. Open sweeps are capped at both ends; a closed
    sweep joins the last ring back to the first (a torus-like solid from a closed (offset, z) polygon)."""
    bm = bmesh.new()
    vr = [[bm.verts.new((x, y, z)) for (x, y) in pts] for (z, pts) in rings]
    m = len(vr[0])
    pairs = list(zip(vr[:-1], vr[1:])) + ([(vr[-1], vr[0])] if closed else [])
    for r0, r1 in pairs:
        for i in range(m):
            bm.faces.new((r0[i], r0[(i + 1) % m], r1[(i + 1) % m], r1[i]))
    if not closed:
        bm.faces.new(list(reversed(vr[0]))); bm.faces.new(vr[-1])
    return mesh_from_bm(name, bm)

def loft(name, levels):
    """levels: list of (z, outline offset). Closed solid lofted from the phone outline."""
    return sweep(name, [(z, offset_outline(d)) for z, d in levels])

def prism(name, pts, w0, w1, plane='xy'):
    """Extrude a 2D polygon (u, v) from w0 to w1. plane 'xy': u=x v=y w=z; 'xz': u=x v=z w=y; 'yz': u=y v=z w=x."""
    def to3(u, v, w):
        return {'xy': (u, v, w), 'xz': (u, w, v), 'yz': (w, u, v)}[plane]
    bm = bmesh.new()
    a = [bm.verts.new(to3(u, v, w0)) for u, v in pts]
    b = [bm.verts.new(to3(u, v, w1)) for u, v in pts]
    m = len(pts)
    for i in range(m):
        bm.faces.new((a[i], a[(i + 1) % m], b[(i + 1) % m], b[i]))
    bm.faces.new(list(reversed(a))); bm.faces.new(b)
    return mesh_from_bm(name, bm)

def box(name, x0, x1, y0, y1, z0, z1):
    return prism(name, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], z0, z1)

def cylinder(name, cx, cy, d, z0, z1, segs=72):
    return prism(name, circle_pts(cx, cy, d / 2.0, segs), z0, z1)

def boolean(target, cutter, op='DIFFERENCE'):
    mod = target.modifiers.new('bool', 'BOOLEAN')
    mod.operation = op
    mod.solver = 'EXACT'
    mod.object = cutter
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)

# ----------------------------------------------------------------------------- camera plateau model
def blend_h(d):
    """Height of the plateau surface above the back glass, d mm outward from the edge of the flat top.
    Apple does not dimension the blend; its toe is 8.8 from the top edge and the side view shows an
    S-curve, modelled here as a smoothstep (max slope ~32 deg)."""
    pl = F['plateau']; B, H = pl['blend'], pl['h']
    if d <= 0: return H
    if d >= B: return 0.0
    u = d / B
    return H * (1.0 - (3 * u * u - 2 * u * u * u))

def h_cut(d):
    """blend_h plus a safety margin (cut_clr at the top edge, fading to 0 at the toe)."""
    return blend_h(d) + P['cut_clr'] * max(0.0, 1.0 - d / F['plateau']['blend'])

def solve_d(target):
    """Smallest d with h_cut(d) <= target."""
    lo, hi = 0.0, F['plateau']['blend']
    for _ in range(60):
        mid = (lo + hi) / 2
        if h_cut(mid) > target: lo = mid
        else: hi = mid
    return hi

def plateau_pts(d):
    pl = F['plateau']; W = P['W']
    return stadium_pts(W - pl['xf1'], W - pl['xf0'], yt(pl['yt1']), yt(pl['yt0']), d)

def camera_cutter(T):
    """Opening through the floor: tight around the blend where it is T high, and a ramp on the cavity side
    that follows the blend out to its toe. Face-down the ramp is fully supported (each layer is narrower)."""
    c = P['cut_clr']; B = F['plateau']['blend']
    d0 = solve_d(T)
    rings = [(-1.0, plateau_pts(d0 + c)), (0.0, plateau_pts(d0 + c))]
    n = 14
    for i in range(1, n + 1):
        d = d0 + (B - d0) * i / n
        z = T - h_cut(d) if i < n else T + 0.02
        rings.append((z, plateau_pts(d + c)))
    rings.append((T + 0.05, plateau_pts(B + c + 0.3)))
    cut = sweep('camcut', rings)
    # never touch the walls: keep 0.4 of floor against them (the ring covers that strip at the top/free edge)
    boolean(cut, loft('camclip', [(-2.0, -0.4), (T + 1.0, -0.4)]), 'INTERSECT')
    return cut, d0

def camera_ring(T):
    """Glue-on collar: underside follows the blend, top flush with (plateau top + ring_lip), flange sits on
    the shell's outer surface. Clipped flush with the shell's outer edge on the top / free edge sides."""
    c = P['cut_clr']; H = F['plateau']['h']
    d0 = solve_d(T)
    z_top = T - H - P['ring_lip']
    ro, ch = P['ring_out'], P['ring_chamfer']
    poly = [(c, z_top), (ro - ch, z_top), (ro, z_top + ch), (ro, 0.0), (d0 + c, 0.0)]
    n = 12
    for i in range(1, n + 1):
        d = d0 * (1.0 - i / n)
        poly.append((d + c, T - h_cut(d)))
    ring = sweep('camera_ring', [(z, plateau_pts(off)) for off, z in poly], closed=True)
    oe = P['wall'] - P['outer_chamfer']              # shell outline offset at the bed surface
    boolean(ring, loft('ringclip', [(z_top - 1.0, oe - ch), (z_top, oe - ch), (z_top + ch, oe), (1.0, oe)]), 'INTERSECT')
    return ring

def plateau_solid(zf):
    """Plateau for the phone dummy: blend + flat top (lenses added separately)."""
    B = F['plateau']['blend']
    rings = [(zf - 0.5, plateau_pts(B + 0.01))]
    n = 14
    for i in range(n + 1):
        d = B * (1.0 - i / n)
        rings.append((zf + blend_h(d), plateau_pts(d)))
    return sweep('plateau', rings)

# ----------------------------------------------------------------------------- shells
def shell_common(name, floor_T):
    """Outer solid minus phone cavity. z=0 at outer surface; phone outer face at z=floor_T."""
    wall, oc, rc = P['wall'], P['outer_chamfer'], P['rim_chamfer']
    rim = floor_T + P['half_T'] - P['rim_setback']
    outer = loft(name, [
        (0.0, wall - oc),
        (oc, wall),
        (rim - rc, wall),
        (rim, wall - rc),
    ])
    clr, cc = P['clearance'], P['cavity_chamfer']
    cav = loft(name + '_cav', [
        (floor_T, clr - cc),
        (floor_T + cc, clr),
        (rim + 1.0, clr),
    ])
    boolean(outer, cav)
    # cut away everything on the hinge side, then relieve the cut edge with a 45deg chamfer on the bed side
    hc = P['hinge_clear']
    boolean(outer, box(name + '_hinge', -10, hc, -10, P['L'] + 10, -10, rim + 10))
    ch = P['hinge_edge_chamfer']
    wedge = box(name + '_wedge', -10, 10, -10, P['L'] + 10, -10, 10)
    # 20 mm cube rotated 45deg about Y: its face x + z = const removes the triangle x + z < hc + ch
    wedge.rotation_euler = (0, math.radians(45), 0)
    wedge.location = (hc + ch - 10 * math.sqrt(2), 0, 0)
    bpy.context.view_layer.update()
    boolean(outer, wedge)
    return outer, rim

def rounded_notch(ob, name, wall, u0, u1, z0, r, rim):
    """Rounded-bottom notch through a wall, open at the rim. u is x for top/bottom walls, y for the free wall."""
    W, L, w = P['W'], P['L'], P['wall']
    pts = rrect_pts(u0, u1, z0, rim + 2.0 + r, r)
    if wall == 'top':
        cut = prism(name, pts, L - 1.0, L + w + 2, 'xz')
    elif wall == 'bottom':
        cut = prism(name, pts, -w - 2, 1.0, 'xz')
    else:
        cut = prism(name, pts, W - 1.0, W + w + 2, 'yz')
    boolean(ob, cut)

def grip_ribs(ob, floor_T, rim, spots):
    """Low ribs on the inside of the walls, chamfered at the rim for lead-in. They sit on the cavity chamfer
    so they print face-down without support. Interference per side = proud - clearance."""
    g = P['grip_rib']; p, ln = g['proud'], g['length']
    if p <= 0: return
    clr, cc, rc = P['clearance'], P['cavity_chamfer'], P['rim_chamfer']
    z0, z1 = floor_T + cc - p, rim - rc - 0.2
    W, L = P['W'], P['L']
    for wall, positions in spots.items():
        for i, pos in enumerate(positions):
            if wall == 'top':
                f = L + clr
                prof = [(f + 0.5, z0), (f - p, z0), (f - p, z1 - p), (f, z1), (f + 0.5, z1)]
                rib = prism('rib_%s%d' % (wall, i), prof, pos - ln / 2, pos + ln / 2, 'yz')
            elif wall == 'bottom':
                f = -clr
                prof = [(f - 0.5, z0), (f + p, z0), (f + p, z1 - p), (f, z1), (f - 0.5, z1)]
                rib = prism('rib_%s%d' % (wall, i), prof, pos - ln / 2, pos + ln / 2, 'yz')
            else:
                f = W + clr
                prof = [(f + 0.5, z0), (f - p, z0), (f - p, z1 - p), (f, z1), (f + 0.5, z1)]
                rib = prism('rib_%s%d' % (wall, i), prof, pos - ln / 2, pos + ln / 2, 'xz')
            boolean(ob, rib, 'UNION')

def magsafe_recess(ob):
    """Annular recess in the outer surface for a stick-on MagSafe magnet ring (the phone's own magnets then
    hold the shell on through the floor, chargers and grips sit on the ring). Sized for a 55 OD / 45 ID / 0.6 ring."""
    m = P['magsafe_ring']
    if not m: return
    ms = F['magsafe']; cx, cy = P['W'] - ms['xf'], yt(ms['yt'])
    ri, ro, dep = m['id'] / 2.0, m['od'] / 2.0, m['depth']
    poly = [(ri, -1.0), (ro, -1.0), (ro, dep), (ri, dep)]
    boolean(ob, sweep('magsafe', [(z, circle_pts(cx, cy, r)) for r, z in poly], closed=True))

def adhesive_pockets(ob, floor_T, spots):
    """Shallow pockets in the cavity floor for reusable adhesive pads."""
    d = P['adhesive_recess']; px, py = P['adhesive_pad']
    for i, (cx, cy) in enumerate(spots):
        boolean(ob, box('pad%d' % i, cx - px / 2, cx + px / 2, cy - py / 2, cy + py / 2, floor_T - d, floor_T + 0.5))

def build_shell_A():
    T = P['back_T']
    ob, rim = shell_common('ShellA_camera_half', T)
    W, L, c = P['W'], P['L'], P['cut_clr']
    # camera plateau opening with blend-following ramp
    cut, d0 = camera_cutter(T)
    boolean(ob, cut)
    print('CAMERA opening at bed surface: plateau top + %.2f mm (%.1f x %.1f mm)' % (
        d0 + c, F['plateau']['xf1'] - F['plateau']['xf0'] + 2 * (d0 + c),
        F['plateau']['yt1'] - F['plateau']['yt0'] + 2 * (d0 + c)))
    # side button (Touch ID) and camera control notches in the free-side wall
    for key in ('side_button', 'camera_control'):
        f = F[key]
        y0, y1 = yt(f['yt']) - f['length'] / 2 - c, yt(f['yt']) + f['length'] / 2 + c
        rounded_notch(ob, key, 'free', y0, y1, T, f['r'], rim)
    # volume buttons slot in the top wall
    v = F['volume']
    rounded_notch(ob, 'volume', 'top', v['x0'] - c, v['x1'] + c, T, v['r'], rim)
    # bottom mic/speaker port notches
    for i, s in enumerate(F['bottom_ports_A']):
        rounded_notch(ob, 'ports%d' % i, 'bottom', s['x0'], s['x1'], T + P['port_bridge'], P['notch_r'], rim)
    magsafe_recess(ob)
    grip_ribs(ob, T, rim, F['ribs_A'])
    # adhesive pad pockets: clear of the MagSafe recess and of the thinned camera ramp
    ms = F['magsafe']; my, mr = yt(ms['yt']), ms['d'] / 2
    adhesive_pockets(ob, T, [(P['hinge_clear'] + 8, my - mr - 9), (P['hinge_clear'] + 8, 80.0),
                             (W - 9, 12.0), (W - 7, 70.0)])
    return ob, rim

def build_shell_B():
    T = P['lip_T']
    ob, rim = shell_common('ShellB_display_half', T)
    W, L, c = P['W'], P['L'], P['cut_clr']
    # display window: everything inside the bezel ring is open; 45deg chamfer on the bed-side inner edge
    lc = min(P['lip_chamfer'], T)
    win = loft('window', [(-1.0, -P['lip_W'] + lc + 1.0), (0.0, -P['lip_W'] + lc),
                          (lc, -P['lip_W']), (T + 1.0, -P['lip_W'])])
    boolean(ob, win)
    # adhesive pad pockets on the underside of the bezel (over the glass, where every commercial case tapes)
    px, py = P['adhesive_pad']
    for i, (cx, cy) in enumerate([(W - P['lip_W'] / 2 - 0.1, 25.0), (W - P['lip_W'] / 2 - 0.1, L - 25.0)]):
        boolean(ob, box('padB%d' % i, cx - 1.0, cx + 1.0, cy - py / 2, cy + py / 2, T - P['adhesive_recess'], T + 0.5))
    # USB-C notch, full height of the wall (Apple's keep-out is taller than the half)
    u = F['usb_c']
    boolean(ob, box('usbc', u['x'] - u['width'] / 2 - c, u['x'] + u['width'] / 2 + c, -P['wall'] - 2, 1.0, -1, rim + 2))
    # receiver / front mic slot in the top wall
    r = F['receiver']
    rounded_notch(ob, 'receiver', 'top', r['x0'], r['x1'], T + P['port_bridge'], r['r'], rim)
    grip_ribs(ob, T, rim, F['ribs_B'])
    return ob, rim

def build_phone_dummy():
    """Closed phone, both halves, for fit renders. Frame: z=0 at the mid-plane between halves."""
    hT, g = P['half_T'], P['gap']
    roll = P['roll']
    prof = [(0.0, roll), (0.02, 1.80), (0.24, 0.89), (0.89, 0.23), (1.80, 0.02), (roll, 0.0)]  # (height below face, inset)
    def half(name, sign):
        lv = [(sign * (g / 2), 0.0), (sign * (hT + g / 2 - roll), 0.0)]
        for h, ins in reversed(prof[:-1]):
            lv.append((sign * (hT + g / 2 - h), -ins))
        if sign < 0:
            lv = list(reversed(lv))
        return loft(name, lv)
    A = half('PhoneA', +1)
    B = half('PhoneB', -1)
    zf = hT + g / 2
    plat = plateau_solid(zf)
    boolean(plat, loft('platclip', [(zf - 1.0, -0.6), (zf + 6.0, -0.6)]), 'INTERSECT')  # real blend is a short cove at the edges
    boolean(A, plat, 'UNION')
    pl = F['plateau']
    for xf, ytv in F['lenses']:
        boolean(A, cylinder('lens', P['W'] - xf, yt(ytv), F['lens_d'], zf + pl['h'] - 0.2, zf + pl['lens_h']), 'UNION')
    return A, B

# ----------------------------------------------------------------------------- export / render
def export_stl(ob, path):
    bpy.ops.object.select_all(action='DESELECT')
    ob.select_set(True)
    bpy.context.view_layer.objects.active = ob
    bpy.ops.wm.stl_export(filepath=path, export_selected_objects=True, ascii_format=False)

def render(path, objs, cam_from, look_at, ortho=None, res=(1600, 1200)):
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'OBJECT'
    scene.display.shading.show_cavity = True
    scene.render.resolution_x, scene.render.resolution_y = res
    scene.render.film_transparent = False
    scene.world = scene.world or bpy.data.worlds.new('W')
    scene.world.color = (0.9, 0.9, 0.9)
    cam_data = bpy.data.cameras.new('cam')
    cam = bpy.data.objects.new('cam', cam_data)
    scene.collection.objects.link(cam)
    scene.camera = cam
    cam.location = Vector(cam_from)
    direction = Vector(look_at) - cam.location
    cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
    if ortho:
        cam_data.type = 'ORTHO'; cam_data.ortho_scale = ortho
    else:
        cam_data.lens = 50
    cam_data.clip_end = 5000
    for o in bpy.data.objects:
        if o.type == 'MESH':
            o.hide_render = o not in objs
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam, do_unlink=True)

def section_render(path, objs, ys):
    cuts = []
    for ob in objs:
        cp = ob.copy(); cp.data = ob.data.copy(); bpy.context.collection.objects.link(cp)
        cp.color = ob.color
        slab = box('slab', -20, P['W'] + 20, ys - 0.5, ys + 0.5, -40, 40)
        bpy.context.view_layer.update()
        boolean(cp, slab, 'INTERSECT')
        cuts.append(cp)
    W = P['W']
    render(path, cuts, (W / 2, ys - 300, 0), (W / 2, ys, 0), ortho=W + 10, res=(2400, 600))
    for cp in cuts:
        bpy.data.objects.remove(cp, do_unlink=True)

def cleanup(ob):
    """Merge coincident vertices and drop degenerate geometry left by the booleans."""
    bm = bmesh.new(); bm.from_mesh(ob.data)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=2e-3)
    bmesh.ops.dissolve_degenerate(bm, edges=bm.edges, dist=2e-3)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(ob.data); bm.free()

def check(ob, label):
    cleanup(ob)
    bm = bmesh.new(); bm.from_mesh(ob.data)
    nonman = sum(1 for e in bm.edges if not e.is_manifold)
    vol = bm.calc_volume(signed=True)
    xs = [v.co.x for v in bm.verts]; ys = [v.co.y for v in bm.verts]; zs = [v.co.z for v in bm.verts]
    bm.free()
    print('CHECK %-28s verts=%6d faces=%6d nonmanifold_edges=%d volume=%.0f mm3 (~%.1f g PLA) '
          'bbox x %.2f..%.2f y %.2f..%.2f z %.2f..%.2f' % (
              label, len(ob.data.vertices), len(ob.data.polygons), nonman, vol, vol * 1.24e-3,
              min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)))

def coupon(src, name, y0, y1, out):
    cp = src.copy(); cp.data = src.data.copy(); bpy.context.collection.objects.link(cp)
    boolean(cp, box('keep', -10, P['W'] + 10, y0, y1, -10, 50), 'INTERSECT')
    export_stl(cp, os.path.join(out, name + '.stl'))
    bpy.data.objects.remove(cp, do_unlink=True)

def main():
    argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    out = 'build'
    if '--out' in argv:
        out = argv[argv.index('--out') + 1]
    os.makedirs(out, exist_ok=True)

    bpy.ops.wm.read_factory_settings(use_empty=True)

    A, rimA = build_shell_A()
    B, rimB = build_shell_B()
    A.color = (0.85, 0.35, 0.15, 1); B.color = (0.15, 0.45, 0.85, 1)
    check(A, 'ShellA_camera_half'); check(B, 'ShellB_display_half')
    export_stl(A, os.path.join(out, 'shellA_camera_half.stl'))
    export_stl(B, os.path.join(out, 'shellB_display_half.stl'))
    R = None
    if P['camera_ring']:
        R = camera_ring(P['back_T'])
        R.color = (0.25, 0.25, 0.28, 1)
        check(R, 'camera_ring')
        # the collar prints on its flat top: flip it so that face is on the bed
        R.scale = (1, 1, -1); bpy.context.view_layer.update()
        export_stl(R, os.path.join(out, 'camera_ring.stl'))   # exporter applies the transform
        R.scale = (1, 1, 1)

    # fit coupons: bottom band of each shell (ports + corner + ribs) and the camera band of shell A
    coupon(A, 'couponA_bottom', -10, P['coupon_h'], out)
    coupon(B, 'couponB_bottom', -10, P['coupon_h'], out)
    coupon(A, 'couponA_camera_top', P['L'] - 40, P['L'] + 10, out)

    # ---- assembled view: move shells into the phone frame (z=0 mid-plane) and add the dummy
    hT, g = P['half_T'], P['gap']
    PA, PB = build_phone_dummy()
    PA.color = PB.color = (0.75, 0.75, 0.78, 1)
    # A: local z=0 outer surface -> world z = hT + g/2 + back_T, local +z must point to -world z (mirror z only)
    A.scale = (1, 1, -1); A.location = (0, 0, hT + g / 2 + P['back_T'])
    # B: local z=0 outer surface -> world z = -(hT + g/2 + lip_T), local +z = +world z
    B.location = (0, 0, -(hT + g / 2 + P['lip_T']))
    objs = [A, B, PA, PB]
    if R:
        R.scale = A.scale; R.location = A.location; objs.append(R)
    bpy.context.view_layer.update()

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, 'duo_case.blend'))

    W, L = P['W'], P['L']
    ctr = (W / 2, L / 2, 0)
    shells = [A, B] + ([R] if R else [])
    render(os.path.join(out, 'render_iso_back.png'), objs, (W / 2 + 160, L / 2 - 200, 170), ctr)
    render(os.path.join(out, 'render_iso_front.png'), objs, (W / 2 + 160, L / 2 - 200, -170), ctr)
    render(os.path.join(out, 'render_back.png'), [o for o in objs if o is not B], (W / 2, L / 2, 300), ctr, ortho=140)
    render(os.path.join(out, 'render_front.png'), [B, PA, PB], (W / 2, L / 2, -300), ctr, ortho=140)
    render(os.path.join(out, 'render_shells_print.png'), shells, (W / 2 + 160, L / 2 - 200, 170), ctr)
    render(os.path.join(out, 'render_camera_closeup.png'), objs, (W - 10 + 90, L - 15 - 110, 90), (W - 35, L - 18, 5))
    render(os.path.join(out, 'render_inside_A.png'), [A], (W / 2 + 60, L / 2 - 120, -200), (W / 2, L / 2, 5))
    # cross sections (1 mm slabs) to check wall / roll / lip / ramp fit
    for nm, ys in (('magsafe', 61.0), ('camera', yt(15.25)), ('ramp', yt(30.0)),
                   ('side_button', yt(42.87)), ('usb_c', 4.0), ('ribs', 33.0)):
        section_render(os.path.join(out, 'section_%s.png' % nm), objs, ys)
    print('DONE', out)

if __name__ == '__main__':
    main()
