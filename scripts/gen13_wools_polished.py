"""Emberfield gen 13: the ten missing wool colors, the cut-copper oxidation
set, chiseled stone bricks and the polished stone trio. 18 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


# --- the ten missing wools (same weave as gen8's six) ---
WOOLS = [
    ("orange", "#d9822c", "#c97426", "#b96822"),
    ("magenta", "#b03aa0", "#a03490", "#902e80"),
    ("light_blue", "#6aa8d4", "#5c9ac6", "#4f8cb8"),
    ("lime", "#8ac03c", "#7cb036", "#6ea030"),
    ("pink", "#e8a0b0", "#d990a2", "#ca8494"),
    ("gray", "#4a4a48", "#3f3f3d", "#363634"),
    ("light_gray", "#9a9a94", "#8c8c86", "#7f7f79"),
    ("cyan", "#3c8a9c", "#357c8e", "#2e707f"),
    ("purple", "#8a4ab0", "#7d429f", "#703a8f"),
    ("brown", "#6f4a2c", "#624226", "#553a20"),
]
for (name, c0, c1, c2) in WOOLS:
    r = random.Random("wool_" + name)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in (c0, c1, c2)]
    for y in range(16):
        for x in range(16):
            v = (x // 2 + y) % 3
            px[x, y] = T.P(T.shade(pal[v], 1.0 + r.uniform(-0.02, 0.02)))
    save(img, name + "_wool")

# --- cut-copper oxidation (same cut pattern as gen11's cut_copper) ---
def cut_copper(name, cols, seed, spots=None):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        off = 4 if (y // 4) % 2 else 0
        for x in range(16):
            c = pal[(x + off) // 8 % 3]
            if y % 4 == 3 or (x + off) % 8 == 7:
                c = T.shade(c, 0.85)
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
    if spots:
        for _ in range(9):
            x, y = r.randrange(1, 15), r.randrange(1, 15)
            px[x, y] = T.P(T.hx(spots))
    save(img, name)


cut_copper("exposed_cut_copper", ["#b98d72", "#a8805f", "#9c7455"], "ecc", spots="#5f8a6a")
cut_copper("weathered_cut_copper", ["#6fa878", "#62986a", "#568a5e"], "wcc", spots="#3f6e50")
cut_copper("oxidized_cut_copper", ["#4f9e82", "#449173", "#3a8265"], "occ", spots="#2c6e54")

# --- chiseled stone bricks ---
r = random.Random("chiseled_stone_bricks")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#8a8a86", "#7f7f7b", "#84847f"]]
for y in range(16):
    for x in range(16):
        c = cols[(x + y) % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
for i in range(1, 15):
    px[i, 2] = T.P(T.shade(cols[0], 1.15))
    px[i, 13] = T.P(T.shade(cols[0], 1.15))
    px[2, i] = T.P(T.shade(cols[2], 0.9))
    px[13, i] = T.P(T.shade(cols[2], 0.9))
for (x0, y0) in [(5, 6), (9, 8)]:
    px[x0, y0] = T.P(T.shade(cols[2], 0.78))
    px[x0 + 1, y0] = T.P(T.shade(cols[2], 0.78))
save(img, "chiseled_stone_bricks")

# --- polished stone trio (bevel-framed smooth slabs) ---
def polished(name, cols, seed):
    r = random.Random(seed)
    img = T.ramp(T.fbm(r, cells=(6, 3)), cols, r, 0.02)
    px = img.load()
    for i in range(16):
        px[i, 0] = T.P(T.shade(T.hx(cols[0]), 1.1))
        px[0, i] = T.P(T.shade(T.hx(cols[0]), 1.05))
        px[i, 15] = T.P(T.shade(T.hx(cols[-1]), 0.82))
        px[15, i] = T.P(T.shade(T.hx(cols[-1]), 0.88))
    save(img, name)


polished("polished_andesite", ["#8a8a86", "#7f7f7b", "#71716d"], "pa")
polished("polished_diorite", ["#b8b6b0", "#aca9a3", "#a09d97"], "pd")
polished("polished_granite", ["#9a7a6e", "#8f7264", "#7f6458"], "pg")
r = random.Random("polished_basalt")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#5f5f62", "#545457", "#4a4a4d"]]
for y in range(16):
    for x in range(16):
        c = cols[(x + y * 2) % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for i in range(16):
    px[i, 0] = T.P(T.shade(cols[0], 1.1))
    px[i, 15] = T.P(T.shade(cols[2], 0.85))
save(img, "polished_basalt")

print("gen13 done: 18 wool/polished textures")
