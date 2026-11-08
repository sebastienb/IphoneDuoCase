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
    cut_clr=0.30,                       # extra clearance on cut-outs
    port_bridge=1.0,                    # wall material kept on the floor side under port notches
    hinge_edge_chamfer=0.7,             # relief chamfer on the hinge-side cut edge (bed side); keep != outer_chamfer
    lip_chamfer=0.6,                    # 45deg chamfer on the inside edge of shell B's bezel (gestures)
    adhesive_recess=0.3,                # depth of pockets for reusable nano-tape / microsuction pads
    adhesive_pad=(10.0, 18.0),          # pad pocket size (x, y)
    coupon_h=10.0,                      # height of the fit-test coupon cut from the bottom of shell A
    N_corner=28,                        # points per corner curve
)

# -------- feature positions (phone frame, "yt" = from top edge, "xf" = from free edge)
F = dict(
    # Shell A (camera half)
    camera_stadium=dict(xf0=2.0, xf1=72.4, yt0=1.5, yt1=34.62),  # outer plateau, 3.64 tall
    side_button=dict(yt=42.87, length=18.67),                     # Touch ID, must stay open
    camera_control=dict(yt=84.97, length=28.26),                  # thin-case keep-out
    volume=dict(x0=44.35, x1=68.61),                              # both buttons, one slot (x from hinge)
    bottom_ports_A=[dict(x0=17.0, x1=25.3), dict(x0=60.0, x1=68.4)],
    magsafe=dict(xf=41.30, yt=61.31, d=61.50),
    # Shell B (display half)
    usb_c=dict(x=42.70, width=12.45),
    receiver=dict(x0=44.0, x1=54.5),
)

# ----------------------------------------------------------------------------- outline helpers
def yt(v):  # "from top" -> frame y
    return P['L'] - v

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
    # remove consecutive duplicates
    out = []
    for p in pts:
        if not out or (abs(p[0] - out[-1][0]) > 1e-6 or abs(p[1] - out[-1][1]) > 1e-6):
            out.append(p)
    if abs(out[0][0] - out[-1][0]) < 1e-6 and abs(out[0][1] - out[-1][1]) < 1e-6:
        out.pop()
    return out

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

# ----------------------------------------------------------------------------- mesh helpers
def loft(name, levels):
    """levels: list of (z, offset). Builds a closed solid by lofting outline rings and capping."""
    bm = bmesh.new()
    rings = []
    for z, d in levels:
        ring = [bm.verts.new((x, y, z)) for (x, y) in offset_outline(d)]
        rings.append(ring)
    m = len(rings[0])
    for r0, r1 in zip(rings[:-1], rings[1:]):
        for i in range(m):
            bm.faces.new((r0[i], r0[(i + 1) % m], r1[(i + 1) % m], r1[i]))
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    return ob

def box(name, x0, x1, y0, y1, z0, z1):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = x0 if v.co.x < 0 else x1
        v.co.y = y0 if v.co.y < 0 else y1
        v.co.z = z0 if v.co.z < 0 else z1
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob

def stadium(name, x0, x1, y0, y1, z0, z1, segs=48):
    """Rounded slot filling the box x0..x1 × y0..y1 with full-radius ends on the shorter axis."""
    w, h = x1 - x0, y1 - y0
    r = min(w, h) / 2.0
    cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    pts = []
    if w >= h:   # horizontal stadium
        for i in range(segs // 2 + 1):
            t = math.radians(-90 + 180 * i / (segs // 2))
            pts.append((cx + (w / 2 - r) + r * math.cos(t), cy + r * math.sin(t)))
        for i in range(segs // 2 + 1):
            t = math.radians(90 + 180 * i / (segs // 2))
            pts.append((cx - (w / 2 - r) + r * math.cos(t), cy + r * math.sin(t)))
    else:
        for i in range(segs // 2 + 1):
            t = math.radians(0 + 180 * i / (segs // 2))
            pts.append((cx + r * math.cos(t), cy + (h / 2 - r) + r * math.sin(t)))
        for i in range(segs // 2 + 1):
            t = math.radians(180 + 180 * i / (segs // 2))
            pts.append((cx + r * math.cos(t), cy - (h / 2 - r) + r * math.sin(t)))
    bm = bmesh.new()
    bot = [bm.verts.new((x, y, z0)) for x, y in pts]
    top = [bm.verts.new((x, y, z1)) for x, y in pts]
    m = len(pts)
    for i in range(m):
        bm.faces.new((bot[i], bot[(i + 1) % m], top[(i + 1) % m], top[i]))
    bm.faces.new(list(reversed(bot))); bm.faces.new(top)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bmesh.ops.remove_doubles(bm, verts=bm.verts, dist=1e-4)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob

def cylinder(name, cx, cy, d, z0, z1, segs=64):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=segs, radius1=d / 2, radius2=d / 2, depth=z1 - z0)
    for v in bm.verts:
        v.co.x += cx; v.co.y += cy; v.co.z += (z0 + z1) / 2
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob

def boolean(target, cutter, op='DIFFERENCE'):
    mod = target.modifiers.new('bool', 'BOOLEAN')
    mod.operation = op
    mod.solver = 'EXACT'
    mod.object = cutter
    bpy.context.view_layer.objects.active = target
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)

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

def adhesive_pockets(ob, floor_T, spots):
    """Shallow pockets in the cavity floor for reusable adhesive pads."""
    d = P['adhesive_recess']; px, py = P['adhesive_pad']
    for i, (cx, cy) in enumerate(spots):
        boolean(ob, box('pad%d' % i, cx - px / 2, cx + px / 2, cy - py / 2, cy + py / 2, floor_T - d, floor_T + 0.5))

def build_shell_A():
    T = P['back_T']
    ob, rim = shell_common('ShellA_camera_half', T)
    W, L, c = P['W'], P['L'], P['cut_clr']
    # camera plateau opening (through the floor)
    cs = F['camera_stadium']
    boolean(ob, stadium('cam', W - cs['xf1'] - c, W - cs['xf0'] + c, yt(cs['yt1']) - c, yt(cs['yt0']) + c, -1, T + 1))
    # side button (Touch ID) and camera control notches in the free-side wall
    for key in ('side_button', 'camera_control'):
        f = F[key]
        y0, y1 = yt(f['yt']) - f['length'] / 2 - c, yt(f['yt']) + f['length'] / 2 + c
        boolean(ob, box(key, W - 1.0, W + P['wall'] + 2, y0, y1, T, rim + 2))
    # volume buttons slot in the top wall
    v = F['volume']
    boolean(ob, box('volume', v['x0'] - c, v['x1'] + c, L - 1.0, L + P['wall'] + 2, T, rim + 2))
    # bottom mic/speaker port notches
    for i, s in enumerate(F['bottom_ports_A']):
        boolean(ob, box('ports%d' % i, s['x0'], s['x1'], -P['wall'] - 2, 1.0, T + P['port_bridge'], rim + 2))
    # adhesive pad pockets: two near the hinge edge, two near the free edge, clear of the MagSafe circle
    ms = F['magsafe']; mx, my, mr = W - ms['xf'], yt(ms['yt']), ms['d'] / 2
    adhesive_pockets(ob, T, [(P['hinge_clear'] + 8, my - mr - 9), (P['hinge_clear'] + 8, my + mr - 2),
                             (W - 9, 12), (W - 9, my + mr - 2)])
    return ob

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
    # USB-C notch, full height of the wall
    u = F['usb_c']
    boolean(ob, box('usbc', u['x'] - u['width'] / 2 - c, u['x'] + u['width'] / 2 + c, -P['wall'] - 2, 1.0, -1, rim + 2))
    # receiver / front mic slot in the top wall
    r = F['receiver']
    boolean(ob, box('receiver', r['x0'], r['x1'], L - 1.0, L + P['wall'] + 2, T + P['port_bridge'], rim + 2))
    return ob

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
        ob = loft(name, lv)
        return ob
    A = half('PhoneA', +1)
    B = half('PhoneB', -1)
    # camera plateau + lenses on A
    cs = F['camera_stadium']; W = P['W']
    zf = hT + g / 2
    plat = stadium('plateau', W - cs['xf1'], W - cs['xf0'], yt(cs['yt1']), yt(cs['yt0']), zf - 0.5, zf + 3.64)
    boolean(A, plat, 'UNION')
    for xf in (15.25, 32.98):
        boolean(A, cylinder('lens', W - xf, yt(15.25), 16.20, zf + 3.0, zf + 5.72), 'UNION')
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

def main():
    argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
    out = 'build'
    if '--out' in argv:
        out = argv[argv.index('--out') + 1]
    os.makedirs(out, exist_ok=True)

    bpy.ops.wm.read_factory_settings(use_empty=True)

    A = build_shell_A()
    B = build_shell_B()
    A.color = (0.85, 0.35, 0.15, 1); B.color = (0.15, 0.45, 0.85, 1)
    check(A, 'ShellA_camera_half'); check(B, 'ShellB_display_half')
    export_stl(A, os.path.join(out, 'shellA_camera_half.stl'))
    export_stl(B, os.path.join(out, 'shellB_display_half.stl'))

    # fit coupons: bottom band of each shell (ports + corner + wall fit) — print these first
    for ob, nm in ((A, 'couponA_bottom'), (B, 'couponB_bottom')):
        cp = ob.copy(); cp.data = ob.data.copy(); bpy.context.collection.objects.link(cp)
        keep = box('keep', -10, P['W'] + 10, -10, P['coupon_h'], -10, 50)
        boolean(cp, keep, 'INTERSECT')
        export_stl(cp, os.path.join(out, nm + '.stl'))
        bpy.data.objects.remove(cp, do_unlink=True)
    # camera-key coupon: top 40 mm of shell A (plateau fit + volume slot + Touch ID notch)
    cp = A.copy(); cp.data = A.data.copy(); bpy.context.collection.objects.link(cp)
    keep = box('keep', -10, P['W'] + 10, P['L'] - 40, P['L'] + 10, -10, 50)
    boolean(cp, keep, 'INTERSECT')
    export_stl(cp, os.path.join(out, 'couponA_camera_top.stl'))
    bpy.data.objects.remove(cp, do_unlink=True)

    # ---- assembled view: move shells into the phone frame (z=0 mid-plane) and add the dummy
    hT, g = P['half_T'], P['gap']
    PA, PB = build_phone_dummy()
    PA.color = PB.color = (0.75, 0.75, 0.78, 1)
    # A: local z=0 outer surface -> world z = hT + g/2 + back_T, local +z must point to -world z (mirror z only)
    A.scale = (1, 1, -1); A.location = (0, 0, hT + g / 2 + P['back_T'])
    # B: local z=0 outer surface -> world z = -(hT + g/2 + lip_T), local +z = +world z
    B.location = (0, 0, -(hT + g / 2 + P['lip_T']))
    bpy.context.view_layer.update()

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(out, 'duo_case.blend'))

    W, L = P['W'], P['L']
    ctr = (W / 2, L / 2, 0)
    render(os.path.join(out, 'render_iso_back.png'), [A, B, PA, PB], (W / 2 + 160, L / 2 - 200, 170), ctr)
    render(os.path.join(out, 'render_iso_front.png'), [A, B, PA, PB], (W / 2 + 160, L / 2 - 200, -170), ctr)
    render(os.path.join(out, 'render_back.png'), [A, PA, PB], (W / 2, L / 2, 300), ctr, ortho=140)
    render(os.path.join(out, 'render_front.png'), [B, PA, PB], (W / 2, L / 2, -300), ctr, ortho=140)
    render(os.path.join(out, 'render_shells_print.png'), [A, B], (W / 2 + 160, L / 2 - 200, 170), ctr)
    render(os.path.join(out, 'render_camera_closeup.png'), [A, B, PA, PB], (W - 10 + 90, L - 15 - 110, 90), (W - 35, L - 18, 5))
    # cross sections (1 mm slabs) to check wall / roll / lip fit
    for nm, ys in (('magsafe', 61.0), ('camera', yt(15.25)), ('side_button', yt(42.87)), ('usb_c', 4.0)):
        section_render(os.path.join(out, 'section_%s.png' % nm), [A, B, PA, PB], ys)
    print('DONE', out)

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

if __name__ == '__main__':
    main()
