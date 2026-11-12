"""Emberfield gen 9: jungle/acacia/mangrove/cherry wood families and the
deepslate ore set (incl. the four ores the pack had never drawn on stone).
24 deepslate/wood + 8 stone ores = 32 textures."""
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


# --- jungle (warm mid-brown, big leaves) ---
log_side("jungle_log", ["#8a6a3a", "#7d5f34", "#6f542c"], "jungle_log")
log_top("jungle_log_top", ["#7a5c2e", "#8f6c38", "#7d5f34", "#856536", "#6f542c", "#856536", "#7d5f34"],
        ["#5a4423", "#6f542c", "#7d5f34", "#6b5028"], "jungle_log_top")
planks("jungle_planks", ["#b08a5a", "#a67f50", "#9c744a"], "jungle_planks")
leaves("jungle_leaves", ["#5fae3c", "#54a034", "#488f2c", "#3e7f25"], "#2c5e1a", "jungle_leaves")

# --- acacia (gray-brown bark, orange wood) ---
log_side("acacia_log", ["#6f6258", "#645a50", "#584f46"], "acacia_log")
log_top("acacia_log_top", ["#a85c2c", "#b86632", "#a25a2a", "#ae6230", "#985226", "#ae6230", "#a25a2a"],
        ["#52463c", "#584f46", "#645a50", "#5e544a"], "acacia_log_top")
planks("acacia_planks", ["#b86632", "#aa5f2e", "#9c562a"], "acacia_planks")
leaves("acacia_leaves", ["#8aa03c", "#7d9434", "#6f862c", "#617a25"], "#4a601c", "acacia_leaves")

# --- mangrove (red-brown, muddy leaves) ---
log_side("mangrove_log", ["#7a3c2c", "#6f3626", "#643020"], "mangrove_log")
log_top("mangrove_log_top", ["#94513c", "#a25a44", "#8f4c38", "#98503c", "#844632", "#98503c", "#8f4c38"],
        ["#5a2c20", "#643020", "#6f3626", "#683324"], "mangrove_log_top")
planks("mangrove_planks", ["#94513c", "#884834", "#7d402e"], "mangrove_planks")
leaves("mangrove_leaves", ["#5f9440", "#548638", "#4a7830", "#406a28"], "#2e501c", "mangrove_leaves")

# --- cherry (rosy bark, pink leaves) ---
log_side("cherry_log", ["#3a2a2c", "#322426", "#2a1e20"], "cherry_log")
log_top("cherry_log_top", ["#c98a94", "#d89aa4", "#c28490", "#d094a0", "#b87c88", "#d094a0", "#c28490"],
        ["#2e2124", "#2a1e20", "#322426", "#2e2122"], "cherry_log_top")
planks("cherry_planks", ["#e0b0b8", "#d4a4ac", "#c89aa2"], "cherry_planks")
leaves("cherry_leaves", ["#f0b8c8", "#e4a8ba", "#d898ac", "#cc889e"], "#b0728a", "cherry_leaves")

# --- deepslate base + ore blobs ---
DS = ["#4c4845", "#3a3734", "#302e2b", "#282624"]


def ds_ore(name, palette, seed, n_clusters=3):
    r = random.Random(seed)
    img = noise_ramp(r, DS, 0.04)
    specs = [(r.randrange(3, 13), r.randrange(3, 13), r.uniform(1.4, 2.0)) for _ in range(n_clusters)]
    mask = T.blob_mask(r, specs)
    T.paint_blob(img, mask, palette, r)
    save(img, name)


ds_ore("deepslate_coal_ore", ("#151412", "#262422", "#2e2c2a", "#45423e"), "ds_coal", n_clusters=4)
ds_ore("deepslate_iron_ore", ("#7d5c46", "#b98d72", "#d8af93", "#e6c4a8"), "ds_iron")
ds_ore("deepslate_copper_ore", ("#8a5c34", "#c98244", "#e09a54", "#f0b472"), "ds_copper")
ds_ore("deepslate_gold_ore", ("#8a6a1e", "#c99f2f", "#f2c94c", "#f8dd7a"), "ds_gold")
ds_ore("deepslate_redstone_ore", ("#7a1c14", "#a82a1e", "#c93a2a", "#e8563c"), "ds_redstone")
ds_ore("deepslate_lapis_ore", ("#1e3a8a", "#2c4fb0", "#3f66cc", "#5f85e0"), "ds_lapis")
ds_ore("deepslate_emerald_ore", ("#1f7a3c", "#2c9e50", "#3cc064", "#5fd884"), "ds_emerald")
ds_ore("deepslate_diamond_ore", ("#2f7a72", "#4fb8ac", "#7de0d8", "#aef0ea"), "ds_diamond")

# --- the four stone ores the pack had never drawn (same blob code on stone) ---
STONE = ["#8f887c", "#837c70", "#777064", "#6b6459", "#5d574d"]


def st_ore(name, palette, seed, n_clusters=3):
    r = random.Random(seed)
    img = noise_ramp(r, STONE, 0.03)
    specs = [(r.randrange(3, 13), r.randrange(3, 13), r.uniform(1.4, 2.0)) for _ in range(n_clusters)]
    mask = T.blob_mask(r, specs)
    T.paint_blob(img, mask, palette, r)
    save(img, name)


st_ore("copper_ore", ("#8a5c34", "#c98244", "#e09a54", "#f0b472"), "st_copper")
st_ore("redstone_ore", ("#7a1c14", "#a82a1e", "#c93a2a", "#e8563c"), "st_redstone")
st_ore("lapis_ore", ("#1e3a8a", "#2c4fb0", "#3f66cc", "#5f85e0"), "st_lapis")
st_ore("emerald_ore", ("#1f7a3c", "#2c9e50", "#3cc064", "#5fd884"), "st_emerald")

print("gen9 done: 32 wood/ore textures")
