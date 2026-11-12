"""Emberfield gen 8: birch/spruce/dark oak, pumpkins and melons, hay, wool,
cobweb, TNT. 27 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


def noise_ramp(rng, colors, jitter=0.04):
    return T.ramp(T.fbm(rng), colors, rng, jitter)


def speckle(px, rng, n=10, f=0.85):
    for _ in range(n):
        px[rng.randrange(16), rng.randrange(16)] = T.P(T.shade(px[rng.randrange(16), rng.randrange(16)], f))


def log_side(name, bark, seed, dashes=False):
    r = random.Random(seed)
    img = noise_ramp(r, bark, 0.05)
    px = img.load()
    cols = [T.hx(c) for c in bark]
    for y in range(16):
        for x in range(16):
            px[x, y] = T.P(cols[(x + y * 2) % len(bark)])
    if dashes:
        for _ in range(5):
            x, y = r.randrange(2, 13), r.randrange(1, 15)
            for i in range(r.randrange(2, 4)):
                px[(x + i) % 16, y] = T.P(T.hx("#3a3630"))
    else:
        for _ in range(3):
            x, y = r.randrange(2, 13), r.randrange(2, 14)
            px[x, y] = T.P(T.shade(T.hx(bark[-1]), 0.8))
    save(img, name)


def log_top(name, rings, bark, seed):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    barkc = [T.hx(c) for c in bark]
    colb = [r.randrange(len(barkc)) for _ in range(16)]
    for y in range(16):
        for x in range(16):
            mv = max(abs(x - 7.5), abs(y - 7.5))
            if mv >= 6.5:
                c = T.shade(barkc[colb[x]], 1.0 + r.uniform(-0.05, 0.05))
            else:
                c = T.shade(T.hx(rings[int(mv) % len(rings)]), 1.0 + r.uniform(-0.04, 0.04))
            px[x, y] = T.P(c)
    save(img, name)


def planks(name, cols, seed):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        row_border = y % 4 == 3
        for x in range(16):
            c = pal[(x // 5 + y // 4) % len(pal)]
            if row_border:
                c = T.shade(c, 0.78)
            elif (x + y) % 7 == 0:
                c = T.shade(c, 0.92)
            px[x, y] = T.P(c)
    save(img, name)


def leaves(name, cols, dark, seed):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    dk = T.hx(dark)
    centers = [(r.randrange(16), r.randrange(16), r.uniform(1.9, 3.0)) for _ in range(12)]
    filled = [[False] * 16 for _ in range(16)]
    for y in range(16):
        for x in range(16):
            for (cx, cy, rad) in centers:
                if math.hypot(T.wd(x, cx), T.wd(y, cy)) <= rad - 0.4 + r.random() * 0.9:
                    filled[y][x] = True
                    break
    n = T.fbm(r, cells=(3, 3))
    for y in range(16):
        for x in range(16):
            if filled[y][x]:
                v = n[y][x] + r.uniform(-0.05, 0.05)
                if v < 0.18:
                    c = dk
                elif v < 0.40:
                    c = pal[3]
                elif v < 0.62:
                    c = pal[2]
                elif v < 0.85:
                    c = pal[1]
                else:
                    c = pal[0]
                px[x, y] = T.P(c)
    save(img, name)


# --- birch ---
log_side("birch_log", ["#d8d3c4", "#cfc9b8", "#c4bfae", "#bab49e"], "birch_log", dashes=True)
log_top("birch_log_top", ["#c9c2a4", "#d6cfae", "#c1ba9a", "#cdc6a8", "#b5af8e", "#cdc6a8", "#c1ba9a"],
        ["#b0aa96", "#b8b29e", "#c2bcac", "#bab49e"], "birch_log_top")
planks("birch_planks", ["#d8d0b0", "#cfc7a6", "#c6bd9c"], "birch_planks")
leaves("birch_leaves", ["#c8dc96", "#b8d08a", "#a6c07c", "#96b26e"], "#7a985a", "birch_leaves")

# --- spruce ---
log_side("spruce_log", ["#5a3a26", "#4f3322", "#452c1c"], "spruce_log")
log_top("spruce_log_top", ["#5f3f28", "#6f4a30", "#5a3a26", "#674428", "#4f3322", "#674428", "#5a3a26"],
        ["#3a261a", "#452c1c", "#4f3322", "#4a2f1e"], "spruce_log_top")
planks("spruce_planks", ["#6f4a30", "#654229", "#5a3a24"], "spruce_planks")
leaves("spruce_leaves", ["#4a7a52", "#3f6f48", "#35633e", "#2c5635"], "#1f4228", "spruce_leaves")

# --- dark oak ---
log_side("dark_oak_log", ["#3a2a1c", "#32241a", "#2a1e14"], "dark_oak_log")
log_top("dark_oak_log_top", ["#4a3421", "#54391f", "#453019", "#4d3620", "#3a2a1c", "#4d3620", "#453019"],
        ["#241a10", "#2a1e14", "#32241a", "#2d2016"], "dark_oak_log_top")
planks("dark_oak_planks", ["#3a2a1a", "#322416", "#2a1e12"], "dark_oak_planks")
leaves("dark_oak_leaves", ["#4a8a3c", "#3f7d34", "#356f2c", "#2c6125"], "#1e4a1a", "dark_oak_leaves")

# --- pumpkin / melon ---
r = random.Random("pumpkin_side")
img = T.new_img()
px = img.load()
ribs = [T.hx(c) for c in ["#d97a34", "#c26a2c", "#b85f24"]]
for y in range(16):
    for x in range(16):
        c = ribs[(x // 2 + y) % 3]
        if x % 4 == 3:
            c = T.shade(c, 0.82)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "pumpkin_side")
r = random.Random("pumpkin_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        c = T.hx("#d97a34" if d < 6 else "#b85f24")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
for i in range(4):
    px[7 + (i % 2), 4 + i] = T.P(T.hx("#5a7a2c"))
save(img, "pumpkin_top")
r = random.Random("carved_pumpkin")
img = T.new_img()
px = img.load()
ribs = [T.hx(c) for c in ["#d97a34", "#c26a2c", "#b85f24"]]
for y in range(16):
    for x in range(16):
        c = ribs[(x // 2 + y) % 3]
        px[x, y] = T.P(c)
dark = T.hx("#4a2a10")
for (x0, y0, w, h) in [(3, 5, 3, 2), (10, 5, 3, 2), (4, 10, 8, 3)]:
    for y in range(y0, min(16, y0 + h)):
        for x in range(x0, min(16, x0 + w)):
            px[x, y] = T.P(dark)
save(img, "carved_pumpkin")

r = random.Random("melon_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        stripe = (x // 2) % 2
        c = T.hx("#6f8a2c" if stripe else "#a3a94e")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "melon_side")
r = random.Random("melon_top")
img = T.new_img()
px = img.load()
n = T.fbm(r, cells=(3, 2))
for y in range(16):
    for x in range(16):
        c = T.hx("#6f8a2c") if n[y][x] < 0.5 else T.hx("#a3a94e")
        px[x, y] = T.P(c)
save(img, "melon_top")

# --- hay ---
r = random.Random("hay_block_side")
img = T.new_img()
px = img.load()
straw = [T.hx(c) for c in ["#d9b34a", "#cfa63e", "#c49b38", "#b8903a"]]
for y in range(16):
    band = y % 6 == 5
    for x in range(16):
        c = straw[(x * 3 + y) % 4]
        if band:
            c = T.shade(c, 0.8)
        px[x, y] = T.P(c)
save(img, "hay_block_side")
r = random.Random("hay_block_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        cross = abs(x - y) < 2 or abs(15 - x - y) < 2
        c = straw[(x + y * 2) % 4]
        if cross:
            c = T.shade(c, 0.82)
        px[x, y] = T.P(c)
save(img, "hay_block_top")

# --- wool ---
WOOLS = [("white", "#e8e8e8", "#d8d8d4", "#cfcfc9"),
         ("red", "#b03a30", "#a33428", "#972d24"),
         ("blue", "#3a54a8", "#334894", "#2c3f80"),
         ("yellow", "#d9b32a", "#c9a524", "#b89420"),
         ("black", "#2e2e2e", "#272727", "#1f1f1f"),
         ("green", "#5a7a2c", "#4f6e25", "#44621f")]
for (name, c0, c1, c2) in WOOLS:
    r = random.Random("wool_" + name)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in (c0, c1, c2)]
    for y in range(16):
        for x in range(16):
            v = (x // 2 + y) % 3
            px[x, y] = T.P(T.shade(pal[v], 1.0 + r.uniform(-0.02, 0.02)))
    save(img, "wool_colored_" + name if False else "white_wool" if name == "white" else name + "_wool")

# --- cobweb ---
img = T.new_img()
px = img.load()
web = T.hx("#e8e8e8")
for i in range(16):
    px[i, i] = T.P(web)
    px[15 - i, i] = T.P(web)
for c in (3, 7, 12):
    for i in range(16):
        px[i, c] = T.P(web)
        px[c, i] = T.P(web)
save(img, "cobweb")

# --- TNT ---
r = random.Random("tnt_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        if 5 <= y <= 10:
            c = T.hx("#e8e2d6" if (x + y) % 3 else "#d8d2c6")
        else:
            c = T.hx("#b03a30" if (x + y) % 3 else "#9c322a")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for i, (x0, w) in enumerate([(4, 2), (7, 2), (10, 2)]):
    for y in range(6, 10):
        for x in range(x0, x0 + w):
            px[x, y] = T.P(T.hx("#2a2020"))
save(img, "tnt_side")
r = random.Random("tnt_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#b03a30" if (x + y) % 3 else "#9c322a")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for i in range(16):
    px[i, 7] = T.P(T.hx("#6a2a24"))
    px[i, 8] = T.P(T.hx("#6a2a24"))
    px[7, i] = T.P(T.hx("#6a2a24"))
    px[8, i] = T.P(T.hx("#6a2a24"))
save(img, "tnt_top")
r = random.Random("tnt_bottom")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#6a2a24" if (x + y) % 3 else "#5c2420")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "tnt_bottom")

print("gen8 done: 27 world textures")
