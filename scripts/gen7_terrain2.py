"""Emberfield gen 7: terrain round two — snowy/capped grass, podzol, mycelium,
paths, farmland, sandstone, ice, stone variants, deepslate bricks, obsidian,
nether and end stones. 40 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


def speckle(px, rng, n=10, f=0.82):
    for _ in range(n):
        x, y = rng.randrange(16), rng.randrange(16)
        px[x, y] = T.P(T.shade(px[x, y], f))


def noise_ramp(rng, colors, jitter=0.04, cells=(4, 2)):
    return T.ramp(T.fbm(rng, cells=cells), colors, rng, jitter)


def top_band(img, band_colors, depth, rng, ragged=True):
    """Recolor the top rows with a ragged band (grass-snow/podzol/mycelium sides)."""
    px = img.load()
    for y in range(depth):
        for x in range(16):
            edge = depth - (1 if ragged and rng.random() < 0.4 else 0)
            if y < edge:
                px[x, y] = T.P(band_colors[rng.randrange(len(band_colors))])


# --- snow and capped grass ---
rng = random.Random("snow")
img = noise_ramp(rng, ["#eef2f4", "#e2e9ec", "#d8e0e5"], 0.02)
speckle(img.load(), rng, 4, 1.06)
save(img, "snow")

rng = random.Random("grass_block_snow")
img = T.ramp(T.fbm(rng), ["#9a7148", "#8a5f3d", "#7d5437", "#6e4830"], rng, 0.05)
top_band(img, [T.hx(c) for c in ["#eef2f4", "#e2e9ec", "#dfe6ea"]], 4, rng)
save(img, "grass_block_snow")

# --- podzol and mycelium ---
rng = random.Random("podzol_top")
img = noise_ramp(rng, ["#7a4f22", "#6a421c", "#5a3a18", "#4f3214"], 0.05)
speckle(img.load(), rng, 8, 1.15)
save(img, "podzol_top")
rng = random.Random("podzol_side")
img = T.ramp(T.fbm(rng), ["#9a7148", "#8a5f3d", "#7d5437", "#6e4830"], rng, 0.05)
top_band(img, [T.hx(c) for c in ["#7a4f22", "#6a421c", "#5f3a1a"]], 4, rng)
save(img, "podzol_side")

rng = random.Random("mycelium_top")
img = noise_ramp(rng, ["#7a6a82", "#6f5f75", "#5f5266", "#54485a"], 0.06)
speckle(img.load(), rng, 9, 1.12)
save(img, "mycelium_top")
rng = random.Random("mycelium_side")
img = T.ramp(T.fbm(rng), ["#9a7148", "#8a5f3d", "#7d5437", "#6e4830"], rng, 0.05)
top_band(img, [T.hx(c) for c in ["#7a6a82", "#6f5f75", "#655a6e"]], 4, rng)
save(img, "mycelium_side")

# --- paths and farmland ---
rng = random.Random("dirt_path_top")
img = noise_ramp(rng, ["#a8845c", "#9c7850", "#8a6a44", "#7d5f3c"], 0.03)
speckle(img.load(), rng, 6, 0.9)
save(img, "dirt_path_top")
rng = random.Random("dirt_path_side")
img = T.ramp(T.fbm(rng), ["#9a7148", "#8a5f3d", "#7d5437"], rng, 0.05)
top_band(img, [T.hx(c) for c in ["#a8845c", "#9c7850", "#8f6d48"]], 3, rng)
save(img, "dirt_path_side")

rng = random.Random("farmland")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#8a5f3d", "#7d5437", "#6e4830", "#5e3c29"]]
for y in range(16):
    for x in range(16):
        row = (y % 4) < 2
        px[x, y] = T.P(cols[(x * 2 + y) % 4 if row else 3])
save(img, "farmland")
rng = random.Random("farmland_moist")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#6e4830", "#5e3c29", "#52331f", "#452a18"]]
for y in range(16):
    for x in range(16):
        row = (y % 4) < 2
        px[x, y] = T.P(cols[(x * 2 + y) % 4 if row else 3])
save(img, "farmland_moist")

# --- sandstone family ---
rng = random.Random("sandstone_top")
img = noise_ramp(rng, ["#e2d3a4", "#d8c898", "#cdbc85"], 0.02)
speckle(img.load(), rng, 5, 0.94)
save(img, "sandstone_top")
rng = random.Random("sandstone")
img = T.new_img()
px = img.load()
bands = [T.hx(c) for c in ["#e2d3a4", "#d8c898", "#cdbc85", "#c2b179"]]
for y in range(16):
    b = bands[min(3, y // 4)] if y != 5 and y != 11 else bands[3]
    for x in range(16):
        px[x, y] = T.P(T.shade(b, 1.0 + rng.uniform(-0.02, 0.02)))
save(img, "sandstone")
rng = random.Random("sandstone_bottom")
img = noise_ramp(rng, ["#d0c094", "#c4b488", "#b8a97e"], 0.02)
save(img, "sandstone_bottom")

rng = random.Random("red_sand")
img = noise_ramp(rng, ["#c1734a", "#b26840", "#a25c38"], 0.03)
speckle(img.load(), rng, 5, 0.92)
save(img, "red_sand")
rng = random.Random("red_sandstone_top")
img = noise_ramp(rng, ["#c1734a", "#b56740", "#a85e3a"], 0.02)
save(img, "red_sandstone_top")
rng = random.Random("red_sandstone")
img = T.new_img()
px = img.load()
bands = [T.hx(c) for c in ["#c1734a", "#b26840", "#a25c38", "#955334"]]
for y in range(16):
    b = bands[min(3, y // 4)] if y != 5 and y != 11 else bands[3]
    for x in range(16):
        px[x, y] = T.P(T.shade(b, 1.0 + rng.uniform(-0.02, 0.02)))
save(img, "red_sandstone")

# --- clay, terracotta, ice ---
rng = random.Random("clay")
img = noise_ramp(rng, ["#9aa3ab", "#8f98a0", "#7f8890"], 0.03)
save(img, "clay")
rng = random.Random("terracotta")
img = noise_ramp(rng, ["#9c5b43", "#8f5138", "#7f4632"], 0.03)
speckle(img.load(), rng, 6, 0.92)
save(img, "terracotta")

rng = random.Random("ice")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#9fc4e8", "#8ab4dc", "#7fa8d4"]]
for y in range(16):
    for x in range(16):
        v = (x * 2 + y * 3) % 7
        c = cols[v % 3]
        px[x, y] = (c[0], c[1], c[2], 225)
for (x0, y0, l) in [(2, 1, 6), (9, 4, 7), (4, 10, 8), (11, 11, 4)]:
    for i in range(l):
        x, y = (x0 + i) % 16, (y0 + (i // 2)) % 16
        px[x, y] = T.P(T.shade(cols[2], 1.12))
save(img, "ice")
rng = random.Random("packed_ice")
img = noise_ramp(rng, ["#7fa8d4", "#6f9ac8", "#5f88b4"], 0.04)
save(img, "packed_ice")
rng = random.Random("blue_ice")
img = noise_ramp(rng, ["#4f78a8", "#476c98", "#3f608c"], 0.05)
save(img, "blue_ice")

# --- stone variants ---
def gray_ramp(name, colors, seed_extra=0):
    r = random.Random(name + str(seed_extra))
    img = noise_ramp(r, colors, 0.03)
    speckle(img.load(), r, 8, 0.93)
    save(img, name)
    return img

gray_ramp("andesite", ["#8a8a86", "#7f7f7b", "#71716d"])
rng = random.Random("diorite")
img = noise_ramp(rng, ["#b8b6b0", "#aca9a3", "#a09d97"], 0.04)
px = img.load()
for _ in range(14):
    x, y = rng.randrange(16), rng.randrange(16)
    px[x, y] = T.P(T.hx("#6f6d68"))
save(img, "diorite")
gray_ramp("granite", ["#9a7a6e", "#8f7264", "#7f6458"])

def bricks(name, base, mortar, seed, moss=False, crack=False):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    cols = [T.hx(c) for c in base]
    for y in range(16):
        off = 4 if (y // 4) % 2 else 0
        for x in range(16):
            if y % 4 == 3 or (x + off) % 8 == 7:
                c = T.hx(mortar)
            else:
                c = cols[(x + off) // 8 % len(cols)]
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.04, 0.04)))
    if moss:
        for _ in range(5):
            cx, cy = r.randrange(16), r.randrange(16)
            for dy in range(-1, 2):
                for dx in range(-2, 3):
                    if math.hypot(dx, dy * 1.4) < 1.9:
                        px[(cx + dx) % 16, (cy + dy) % 16] = T.P(T.hx("#6f8a50"))
    if crack:
        x = r.randrange(3, 13)
        for y in range(16):
            px[x, y] = T.P(T.shade(T.hx(mortar), 0.8))
            if r.random() < 0.3:
                x = max(0, min(15, x + r.choice((-1, 1))))
    save(img, name)

bricks("stone_bricks", ["#8a8a86", "#7f7f7b", "#84847f"], "#5d5d59", "sb1")
bricks("mossy_stone_bricks", ["#8a8a86", "#7f7f7b", "#84847f"], "#5d5d59", "sb2", moss=True)
bricks("cracked_stone_bricks", ["#8a8a86", "#7f7f7b", "#84847f"], "#5d5d59", "sb3", crack=True)
r = random.Random("mossy_cobblestone")
img = noise_ramp(r, ["#8f887c", "#837c70", "#777064"], 0.05)
px = img.load()
for _ in range(6):
    cx, cy = r.randrange(16), r.randrange(16)
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            if math.hypot(dx, dy) < 2.0:
                px[(cx + dx) % 16, (cy + dy) % 16] = T.P(T.hx("#6f8a50"))
save(img, "mossy_cobblestone")

# --- deepslate family ---
DS = ["#4c4845", "#3a3734", "#302e2b", "#282624"]
rng = random.Random("cobbled_deepslate")
img = noise_ramp(rng, DS, 0.05)
px = img.load()
for _ in range(10):
    x, y = rng.randrange(16), rng.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 0.86))
save(img, "cobbled_deepslate")
bricks("deepslate_bricks", DS, "#211f1d", "db1")
r = random.Random("deepslate_tiles")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in DS]
for y in range(16):
    off = 4 if (y // 2) % 2 else 0
    for x in range(16):
        if y % 2 == 1 or (x + off) % 8 == 7:
            c = cols[3]
        else:
            c = cols[(x + off) // 8 % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "deepslate_tiles")
r = random.Random("polished_deepslate")
img = noise_ramp(r, DS[:3], 0.02)
px = img.load()
for i in range(16):
    px[i, 0] = T.P(T.shade(T.hx(DS[0]), 1.08))
    px[0, i] = T.P(T.shade(T.hx(DS[0]), 0.94))
save(img, "polished_deepslate")

gray_ramp("calcite", ["#e8e6df", "#dedcd4", "#d6d4cc"])
r = random.Random("tuff")
img = noise_ramp(r, ["#8a8570", "#7f7a66", "#6f6b58"], 0.05)
speckle(img.load(), r, 10, 0.9)
save(img, "tuff")

# --- obsidian, nether, end ---
r = random.Random("obsidian")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#1a1424", "#221a30", "#2a2038"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x * 3 + y * 5 + (x ^ y)) % 3])
for _ in range(5):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.hx("#5f4a8a"))
save(img, "obsidian")
r = random.Random("crying_obsidian")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#1a1424", "#221a30", "#2a2038"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x * 3 + y * 5 + (x ^ y)) % 3])
for (x0, y0) in [(3, 2), (11, 5), (6, 10), (13, 12)]:
    for i in range(r.randrange(4, 8)):
        x, y = x0, (y0 + i) % 16
        px[x, y] = T.P(T.hx("#c46ac4" if i % 3 else "#8a4a9a"))
save(img, "crying_obsidian")

r = random.Random("netherrack")
img = noise_ramp(r, ["#7a2a24", "#6a2420", "#5a1c18", "#4a1614"], 0.06)
speckle(img.load(), r, 12, 1.14)
save(img, "netherrack")
bricks("nether_bricks", ["#5a1c18", "#4a1614", "#55201a"], "#2c0e0c", "nb1")
r = random.Random("soul_sand")
img = noise_ramp(r, ["#4f3a2c", "#453224", "#3a2a20"], 0.05)
px = img.load()
for (x0, y0) in [(4, 6), (10, 4), (7, 11)]:
    for dy in (-1, 0):
        px[x0, y0 + dy] = T.P(T.hx("#241a12"))
        px[x0 + 1, y0 + dy] = T.P(T.hx("#241a12"))
save(img, "soul_sand")
r = random.Random("glowstone")
img = T.new_img()
px = img.load()
base = [T.hx(c) for c in ["#d97a34", "#c26a2c", "#b25f28"]]
bright = [T.hx(c) for c in ["#f2c23e", "#f8dd7a"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(base[(x + y) % 3])
for _ in range(9):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(bright[r.randrange(2)])
save(img, "glowstone")

r = random.Random("end_stone")
img = noise_ramp(r, ["#e8dfb0", "#ddd4a4", "#d0c898"], 0.04)
speckle(img.load(), r, 8, 0.94)
save(img, "end_stone")
r = random.Random("purpur_block")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#a97ca8", "#9a6d99", "#8f648f"]]
for y in range(16):
    off = 0 if (y // 4) % 2 else 2
    for x in range(16):
        c = cols[((x + off) // 4 + y // 4) % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "purpur_block")
bricks("end_stone_bricks", ["#e8dfb0", "#ddd4a4", "#d8cf9e"], "#b8b088", "esb1")

print("gen7 done: 40 terrain textures")
