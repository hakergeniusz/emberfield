"""Emberfield gen 10: the colored terracotta family (15), the quartz and
ancient debris pair, netherite, magma, soul soil, basalt, blackstone and the
crimson/warped stems. 29 textures."""
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


def speckle(px, rng, n=8, f=0.92):
    for _ in range(n):
        px[rng.randrange(16), rng.randrange(16)] = T.P(T.shade(px[rng.randrange(16), rng.randrange(16)], f))


# --- colored terracotta (the base terracotta shipped in gen7) ---
TERRACOTTA = [
    ("white", "#d8cfc2", "#c9c0b2", "#bab1a3"),
    ("orange", "#c1732e", "#b06728", "#9c5c24"),
    ("magenta", "#a84886", "#973f76", "#863868"),
    ("light_blue", "#8aa8c2", "#7c98b0", "#6e88a0"),
    ("yellow", "#c9a83c", "#b89834", "#a68a2e"),
    ("lime", "#8aa03c", "#7c9034", "#6e802c"),
    ("pink", "#c28a96", "#b07c88", "#9e707a"),
    ("gray", "#4a4a48", "#3f3f3d", "#363634"),
    ("light_gray", "#9a9a94", "#8c8c86", "#7f7f79"),
    ("cyan", "#3f7a8a", "#366c7a", "#2e606e"),
    ("purple", "#7a3c9c", "#6c348a", "#5f2c78"),
    ("blue", "#3a4a9c", "#32408a", "#2a3878"),
    ("brown", "#6f4a2c", "#624226", "#553a20"),
    ("green", "#5a6e2c", "#4f6026", "#445420"),
    ("black", "#26241f", "#1f1d1a", "#181614"),
]
for (name, c0, c1, c2) in TERRACOTTA:
    r = random.Random("tc_" + name)
    img = noise_ramp(r, [c0, c1, c2], 0.03)
    speckle(img.load(), r, 6, 0.95)
    save(img, name + "_terracotta")

# --- quartz ---
r = random.Random("nether_quartz_ore")
img = noise_ramp(r, ["#7a2a24", "#6a2420", "#5a1c18"], 0.06)
specs = [(r.randrange(3, 13), r.randrange(3, 13), r.uniform(1.3, 1.9)) for _ in range(3)]
mask = T.blob_mask(r, specs)
T.paint_blob(img, mask, ("#c9b8b0", "#e0d4cc", "#efe8e2", "#f8f4f0"), r)
save(img, "nether_quartz_ore")
r = random.Random("quartz_block_side")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#efe8e2", "#e4dcd4", "#d8d0c8"]]
for y in range(16):
    for x in range(16):
        c = cols[(x * 2 + y) % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.015, 0.015)))
save(img, "quartz_block_side")
r = random.Random("quartz_block_bottom")
img = noise_ramp(r, ["#e4dcd4", "#d8d0c8"], 0.02)
save(img, "quartz_block_bottom")

# --- ancient debris / netherite ---
r = random.Random("ancient_debris_side")
img = T.new_img()
px = img.load()
base = [T.hx(c) for c in ["#4a3830", "#3f3028", "#352a22"]]
spiral = [T.hx(c) for c in ["#6a5644", "#7d664f", "#8a735a"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(base[(x * 3 + y * 5) % 3])
for (x0, y0) in [(2, 3), (9, 2), (5, 9), (12, 10)]:
    for i in range(5):
        x = (x0 + i) % 16
        y = (y0 + (i * 2) % 4) % 16
        px[x, y] = T.P(spiral[i % 3])
save(img, "ancient_debris_side")
r = random.Random("ancient_debris_top")
img = noise_ramp(r, ["#4a3830", "#3f3028", "#352a22"], 0.05)
px = img.load()
for _ in range(6):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.hx("#7d664f"))
save(img, "ancient_debris_top")
r = random.Random("netherite_block")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#3a3538", "#322e30", "#2a2628", "#443f42"]]
for y in range(16):
    off = 4 if (y // 4) % 2 else 0
    for x in range(16):
        c = cols[(x + off) // 6 % 4]
        if y % 4 == 3:
            c = T.shade(c, 0.85)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "netherite_block")

# --- magma, soul soil, basalt, blackstone ---
r = random.Random("magma")
img = T.new_img()
px = img.load()
dark = [T.hx(c) for c in ["#3a1c14", "#2c1610", "#45251a"]]
hot = [T.hx(c) for c in ["#d97a34", "#f2c23e", "#c2571e"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(dark[(x + y) % 3])
for _ in range(7):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(hot[r.randrange(3)])
    for (dx, dy) in ((0, 1), (1, 0)):
        if r.random() < 0.6:
            px[(x + dx) % 16, (y + dy) % 16] = T.P(T.shade(hot[1], 0.85))
save(img, "magma")
r = random.Random("soul_soil")
img = noise_ramp(r, ["#3f2e22", "#37281e", "#2e221a"], 0.05)
speckle(img.load(), r, 10, 1.1)
save(img, "soul_soil")
r = random.Random("basalt_side")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#4f4f52", "#464649", "#3d3d40"]]
for y in range(16):
    for x in range(16):
        col = (x + (y // 5)) % 3
        c = cols[col]
        if (x + y * 3) % 5 == 0:
            c = T.shade(c, 0.9)
        px[x, y] = T.P(c)
save(img, "basalt_side")
r = random.Random("basalt_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        ring = int(d) % 3
        px[x, y] = T.P([T.hx("#4f4f52"), T.hx("#464649"), T.hx("#3d3d40")][ring])
save(img, "basalt_top")
r = random.Random("blackstone")
img = noise_ramp(r, ["#2c2926", "#262422", "#1f1d1b"], 0.05)
px = img.load()
for _ in range(8):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 1.35))
save(img, "blackstone")

# --- crimson / warped stems ---
def stem_pair(prefix, bark, rings, seed):
    r = random.Random(seed)
    img = noise_ramp(r, bark, 0.06)
    px = img.load()
    cols = [T.hx(c) for c in bark]
    for y in range(16):
        for x in range(16):
            if (x + y * 3) % 6 == 0:
                px[x, y] = T.P(T.shade(cols[y % len(cols)], 0.85))
    save(img, prefix + "_stem")
    r = random.Random(seed + "_top")
    img = T.new_img()
    px = img.load()
    barkc = [T.hx(c) for c in bark]
    ringc = [T.hx(c) for c in rings]
    for y in range(16):
        for x in range(16):
            mv = max(abs(x - 7.5), abs(y - 7.5))
            src = barkc if mv >= 6.0 else ringc
            px[x, y] = T.P(T.shade(src[(x * 2 + y) % len(src)], 1.0 + r.uniform(-0.04, 0.04)))
    save(img, prefix + "_stem_top")


def fungus_planks(name, cols, seed):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        for x in range(16):
            c = pal[(x // 6 + y // 4) % len(pal)]
            if y % 4 == 3:
                c = T.shade(c, 0.8)
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
    save(img, name)


stem_pair("crimson", ["#7a2c3c", "#6f2635", "#63222f"], ["#9c5c48", "#b87258", "#8f5440"], "crimson")
fungus_planks("crimson_planks", ["#9c5c48", "#8f5440", "#824c3a"], "crimson_planks")
stem_pair("warped", ["#2c5a6c", "#265060", "#204654"], ["#3c7a5c", "#4c9470", "#346e52"], "warped")
fungus_planks("warped_planks", ["#3c7a5c", "#346e52", "#2c6248"], "warped_planks")

print("gen10 done: 29 terracotta/nether textures")
