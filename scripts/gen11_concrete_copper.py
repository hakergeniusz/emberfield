"""Emberfield gen 11: the concrete and concrete-powder families, copper
oxidation, nether-brick variants, quartz pillar and bricks. 42 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


BASE = [
    ("white", "#e8e8e6", "#dcdcd9"), ("orange", "#e08a2c", "#d07f26"),
    ("magenta", "#c04a9c", "#b04390"), ("light_blue", "#7aa8d4", "#6f9cc6"),
    ("yellow", "#e8cc3c", "#d9bd35"), ("lime", "#8ac03c", "#7fb036"),
    ("pink", "#e8a0b0", "#d990a2"), ("gray", "#5a5a58", "#4f4f4d"),
    ("light_gray", "#a8a8a2", "#9c9c96"), ("cyan", "#3c8a9c", "#357c8e"),
    ("purple", "#8a4ab0", "#7d429f"), ("blue", "#3c54b0", "#34499f"),
    ("brown", "#7a5434", "#6e4a2e"), ("green", "#5c8a34", "#517c2e"),
    ("black", "#2c2c2a", "#242422"), ("red", "#b03c30", "#a03529"),
]
POWDER = [(n, c0, c1) for (n, c0, c1) in BASE]

# --- concrete: flat, faint mottle, 1px darker border every block edge row ---
for (name, c0, c1) in BASE:
    r = random.Random("concrete_" + name)
    img = T.ramp(T.fbm(r, cells=(6, 3)), [c0, c1], r, 0.015)
    px = img.load()
    edge = T.shade(T.hx(c1), 0.94)
    for i in range(16):
        px[i, 15] = T.P(edge)
        px[15, i] = T.P(edge)
    save(img, name + "_concrete")

# --- concrete powder: grainy, no border ---
for (name, c0, c1) in POWDER:
    r = random.Random("powder_" + name)
    img = T.ramp(T.fbm(r, cells=(2, 2)), [c0, c1], r, 0.07)
    px = img.load()
    for _ in range(14):
        x, y = r.randrange(16), r.randrange(16)
        px[x, y] = T.P(T.shade(T.hx(c0), 0.9))
    save(img, name + "_concrete_powder")

# --- copper oxidation ---
COPPER = [
    ("copper_block", ["#c9804a", "#b8733f", "#a8683a"], None),
    ("exposed_copper", ["#b98d72", "#a8805f", "#9c7455"], "#5f8a6a"),
    ("weathered_copper", ["#6fa878", "#62986a", "#568a5e"], "#3f6e50"),
    ("oxidized_copper", ["#4f9e82", "#449173", "#3a8265"], "#2c6e54"),
]
for (name, cols, tint) in COPPER:
    r = random.Random("copper_" + name)
    img = T.ramp(T.fbm(r, cells=(5, 3)), cols, r, 0.03)
    px = img.load()
    # bevel: light top/left, dark bottom/right, orange metal core
    for i in range(16):
        px[i, 0] = T.P(T.shade(T.hx(cols[0]), 1.12))
        px[0, i] = T.P(T.shade(T.hx(cols[0]), 1.06))
        px[i, 15] = T.P(T.shade(T.hx(cols[2]), 0.8))
        px[15, i] = T.P(T.shade(T.hx(cols[2]), 0.86))
    if tint is None:
        for _ in range(6):
            x, y = r.randrange(1, 14), r.randrange(1, 14)
            px[x, y] = T.P(T.hx("#e09a54"))
    else:
        for _ in range(9):
            x, y = r.randrange(1, 15), r.randrange(1, 15)
            px[x, y] = T.P(T.hx(tint))
    save(img, name)
r = random.Random("cut_copper")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#c9804a", "#b8733f", "#a8683a"]]
for y in range(16):
    off = 4 if (y // 4) % 2 else 0
    for x in range(16):
        c = cols[(x + off) // 8 % 3]
        if y % 4 == 3 or (x + off) % 8 == 7:
            c = T.shade(c, 0.85)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "cut_copper")

# --- nether brick variants ---
def nether_bricks(name, seed, crack=False, chisel=False, red=False):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    base = [T.hx(c) for c in (["#8a2c28", "#7d2622", "#9c3230"] if red else ["#5a1c18", "#4a1614", "#55201a"])]
    mortar = T.hx("#2c0e0c" if not red else "#4a1410")
    for y in range(16):
        off = 4 if (y // 4) % 2 else 0
        for x in range(16):
            if y % 4 == 3 or (x + off) % 8 == 7:
                c = mortar
            else:
                c = base[(x + off) // 8 % 3]
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.04, 0.04)))
    if crack:
        x = r.randrange(4, 12)
        for y in range(16):
            px[x, y] = T.P(mortar)
            if r.random() < 0.3:
                x = max(0, min(15, x + r.choice((-1, 1))))
    if chisel:
        for i in range(1, 15):
            px[i, 2] = T.P(T.shade(base[0], 1.25))
            px[i, 13] = T.P(T.shade(base[0], 1.25))
        for i in range(3, 13):
            px[2, i] = T.P(T.shade(base[0], 1.1))
            px[13, i] = T.P(T.shade(base[0], 1.1))
    save(img, name)

nether_bricks("cracked_nether_bricks", "cnb", crack=True)
nether_bricks("chiseled_nether_bricks", "chnb", chisel=True)
nether_bricks("red_nether_bricks", "rnb", red=True)

# --- quartz pillar and bricks ---
r = random.Random("quartz_pillar_side")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#efe8e2", "#e4dcd4", "#d8d0c8"]]
for y in range(16):
    for x in range(16):
        c = cols[(x + y * 2) % 3]
        if x in (0, 15):
            c = T.shade(c, 0.92)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.015, 0.015)))
for x in (3, 8, 12):
    for y in range(16):
        px[x, y] = T.P(T.shade(cols[2], 0.95))
save(img, "quartz_pillar_side")
r = random.Random("quartz_pillar_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        px[x, y] = T.P([T.hx("#efe8e2"), T.hx("#e4dcd4"), T.hx("#d8d0c8")][int(d) % 3])
save(img, "quartz_pillar_top")
r = random.Random("quartz_bricks")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#efe8e2", "#e4dcd4", "#d8d0c8"]]
for y in range(16):
    off = 4 if (y // 4) % 2 else 0
    for x in range(16):
        c = cols[(x + off) // 8 % 3]
        if y % 4 == 3 or (x + off) % 8 == 7:
            c = T.shade(cols[2], 0.9)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "quartz_bricks")

print("gen11 done: 42 concrete/copper/nether/quartz textures")
