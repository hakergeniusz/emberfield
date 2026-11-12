"""Emberfield gen 15: the sixteen glazed-terracotta motifs (two-tone
geometric interpretations), cut/chiseled sandstone, chiseled quartz,
purpur pillar, iron bars, lanterns and the lightning rod. 28 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


# --- glazed terracotta: per-color two-tone geometric motif ---
GLAZED = [
    ("white", "#d8cfc2", "#b0a695"), ("orange", "#e08a2c", "#9c5c1e"),
    ("magenta", "#c04a9c", "#6e2c5a"), ("light_blue", "#7aa8d4", "#446a94"),
    ("yellow", "#e8cc3c", "#a68620"), ("lime", "#8ac03c", "#527a22"),
    ("pink", "#e8a0b0", "#a85c70"), ("gray", "#5a5a58", "#2c2c2a"),
    ("light_gray", "#a8a8a2", "#6e6e68"), ("cyan", "#3c8a9c", "#22525e"),
    ("purple", "#8a4ab0", "#4e2a66"), ("blue", "#3c54b0", "#22306a"),
    ("brown", "#7a5434", "#46301c"), ("green", "#5c8a34", "#34511e"),
    ("black", "#2c2c2a", "#121210"), ("red", "#b03c30", "#6e221a"),
]
for (name, hi, lo) in GLAZED:
    r = random.Random("glazed_" + name)
    img = T.new_img()
    px = img.load()
    H, L = T.hx(hi), T.hx(lo)
    for y in range(16):
        for x in range(16):
            px[x, y] = T.P(H)
    d = math.hypot
    # concentric diamond + corner wedges, the motif family glazed tiles share
    for y in range(16):
        for x in range(16):
            dm = abs(x - 7.5) + abs(y - 7.5)
            if dm > 12.5:
                px[x, y] = T.P(L)
            elif dm > 9.5:
                px[x, y] = T.P(T.shade(H, 0.9))
            elif dm < 3.5:
                px[x, y] = T.P(L)
            elif abs(x - y) < 1.2 and 2 < x < 14:
                px[x, y] = T.P(T.shade(L, 1.25))
    # accent dots on the diagonals
    for (x0, y0) in [(3, 3), (12, 3), (3, 12), (12, 12)]:
        px[x0, y0] = T.P(H if r.random() < 0.5 else T.shade(L, 1.3))
    save(img, name + "_glazed_terracotta")

# --- cut and chiseled sandstone ---
def cut(name, cols, seed):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        off = 0 if (y // 4) % 2 else 2
        for x in range(16):
            c = pal[(x + off) // 8 % 2]
            if y % 4 == 3 or (x + off) % 8 == 7:
                c = T.shade(pal[1], 0.85)
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.015, 0.015)))
    save(img, name)


def chiseled(name, cols, seed, band_y=(4, 12)):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        for x in range(16):
            c = pal[(x + y) % 2]
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
    for i in range(1, 15):
        px[i, band_y[0]] = T.P(T.shade(pal[0], 0.86))
        px[i, band_y[1]] = T.P(T.shade(pal[0], 0.86))
    for i in range(band_y[0] + 1, band_y[1]):
        px[3, i] = T.P(T.shade(pal[1], 1.1))
        px[8, i] = T.P(T.shade(pal[1], 1.1))
        px[12, i] = T.P(T.shade(pal[1], 1.1))
    save(img, name)


SAND = ["#e2d3a4", "#d4c494", "#c4b484"]
RSAND = ["#c1734a", "#b26840", "#a25c38"]
cut("cut_sandstone", SAND, "cut_sand")
cut("cut_red_sandstone", RSAND, "cut_rsand")
chiseled("chiseled_sandstone", SAND, "chi_sand")
chiseled("chiseled_red_sandstone", RSAND, "chi_rsand")

# --- chiseled quartz ---
r = random.Random("chiseled_quartz_block")
img = T.new_img()
px = img.load()
pal = [T.hx(c) for c in ["#efe8e2", "#e4dcd4", "#d8d0c8"]]
for y in range(16):
    for x in range(16):
        c = pal[(x + y) % 2]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.015, 0.015)))
for i in range(1, 15):
    px[i, 5] = T.P(T.shade(pal[2], 0.9))
    px[i, 11] = T.P(T.shade(pal[2], 0.9))
for i in range(6, 11):
    px[4, i] = T.P(T.shade(pal[1], 1.08))
    px[11, i] = T.P(T.shade(pal[1], 1.08))
save(img, "chiseled_quartz_block")
r = random.Random("chiseled_quartz_block_top")
img = T.ramp(T.fbm(r, cells=(6, 3)), ["#efe8e2", "#e4dcd4"], r, 0.015)
save(img, "chiseled_quartz_block_top")

# --- purpur pillar ---
r = random.Random("purpur_pillar_side")
img = T.new_img()
px = img.load()
pal = [T.hx(c) for c in ["#a97ca8", "#9a6d99", "#8f648f"]]
for y in range(16):
    for x in range(16):
        c = pal[(x + y) % 3]
        if x in (0, 15):
            c = T.shade(c, 0.88)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for x in (4, 7, 11):
    for y in range(16):
        px[x, y] = T.P(T.shade(pal[2], 0.94))
save(img, "purpur_pillar_side")
r = random.Random("purpur_pillar_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        px[x, y] = T.P(pal[int(d) % 3])
save(img, "purpur_pillar_top")

# --- iron bars (transparent lattice) ---
img = T.new_img()
px = img.load()
iron_hi, iron_lo = T.hx("#c9c4ba"), T.hx("#968f84")
for i in range(16):
    px[i, 7] = T.P(iron_lo)
    px[i, 8] = T.P(iron_lo)
for i in range(2, 14):
    px[7, i] = T.P(iron_hi)
    px[8, i] = T.P(iron_hi)
for (x0, y0) in [(7, 7), (8, 7), (7, 8), (8, 8)]:
    px[x0, y0] = T.P(T.hx("#e8e4dc"))
for y in range(16):
    for x in range(16):
        if px[x, y][3] == 0 and y in (3, 12) and x % 4 == 2:
            px[x, y] = T.P(iron_lo)
save(img, "iron_bars")

# --- lanterns (metal cage + glow core, transparent gaps) ---
def lantern(name, core_hi, core_lo, soul=False):
    r = random.Random(name)
    img = T.new_img()
    px = img.load()
    metal = T.hx("#968f84") if not soul else T.hx("#5f7a72")
    metal_d = T.shade(metal, 0.8)
    glow = [T.hx(core_hi), T.hx(core_lo)]
    for y in range(3, 13):
        for x in range(5, 11):
            px[x, y] = T.P(glow[(x + y) % 2])
    # the cage: top cap, bottom tray, corner ribs
    for x in range(4, 12):
        px[x, 2] = T.P(metal)
        px[x, 13] = T.P(metal_d)
    for y in range(3, 13):
        px[4, y] = T.P(metal)
        px[11, y] = T.P(metal)
    px[7, 0] = T.P(metal)
    px[7, 1] = T.P(metal_d)
    for y in range(1, 3):
        px[6, y] = T.P(metal)
        px[8, y] = T.P(metal)
    for _ in range(6):
        x, y = r.randrange(6, 10), r.randrange(4, 12)
        px[x, y] = T.P(glow[0])
    save(img, name)


lantern("lantern", "#f8dd7a", "#f2c23e")
lantern("soul_lantern", "#5fd884", "#3cc0a0", soul=True)

# --- lightning rod (copper rod on transparent) ---
img = T.new_img()
px = img.load()
cu = [T.hx("#c9804a"), T.hx("#b8733f"), T.hx("#a8683a")]
for y in range(2, 14):
    for x in (7, 8):
        px[x, y] = T.P(cu[(x + y) % 3])
for x in (6, 9):
    px[x, 13] = T.P(cu[1])
px[7, 1] = T.P(T.shade(cu[0], 1.12))
px[8, 1] = T.P(T.shade(cu[0], 1.12))
px[7, 0] = T.P(T.hx("#e09a54"))
save(img, "lightning_rod")

print("gen15 done: 28 glazed/decor textures")
