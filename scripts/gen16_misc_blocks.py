"""Emberfield gen 16: smooth stone/basalt, bone block, mushroom blocks,
sponges, cake, chiseled bookshelf, nylium, the blackstone family, tuff
bricks, chorus, end rod, respawn anchor and lodestone. 35 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def planks_like(r, cols):
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        for x in range(16):
            c = pal[(x // 5 + y // 4) % len(pal)]
            if y % 4 == 3:
                c = T.shade(c, 0.82)
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
    return img


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")


def noise_ramp(rng, colors, jitter=0.04):
    return T.ramp(T.fbm(rng), colors, rng, jitter)


def speckle(px, rng, n=10, f=0.9):
    for _ in range(n):
        x, y = rng.randrange(16), rng.randrange(16)
        px[x, y] = T.P(T.shade(px[x, y], f))


# --- smooth stone and basalt ---
r = random.Random("smooth_stone")
img = T.ramp(T.fbm(r, cells=(8, 4)), ["#9a9a94", "#8e8e88", "#84847e"], r, 0.015)
px = img.load()
for i in range(16):
    px[i, 15] = T.P(T.shade(px[i, 15], 0.92))
save(img, "smooth_stone")
r = random.Random("smooth_basalt")
img = noise_ramp(r, ["#3f3f42", "#363639", "#2e2e31"], 0.03)
save(img, "smooth_basalt")

# --- bone block ---
r = random.Random("bone_block_side")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#e0dbca", "#d6d1c0", "#cbc6b5"]]
for y in range(16):
    for x in range(16):
        c = cols[(x + y * 2) % 3]
        if x % 5 == 4:
            c = T.shade(c, 0.92)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.015, 0.015)))
save(img, "bone_block_side")
r = random.Random("bone_block_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        px[x, y] = T.P(cols[int(d) % 3])
for (x0, y0) in [(4, 5), (10, 8), (6, 11)]:
    px[x0, y0] = T.P(T.shade(cols[2], 0.85))
save(img, "bone_block_top")

# --- mushroom blocks ---
def mushroom(name, cap_cols, stem=False):
    r = random.Random(name)
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cap_cols]
    if stem:
        for y in range(16):
            for x in range(16):
                c = pal[(x + y) % 2]
                px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
    else:
        for y in range(16):
            for x in range(16):
                px[x, y] = T.P(pal[(x * 2 + y) % len(pal)])
        for _ in range(5):
            x, y = r.randrange(16), r.randrange(16)
            px[x, y] = T.P(pal[-1])
    save(img, name)


mushroom("brown_mushroom_block", ["#96674a", "#8a5d42", "#7d533a"])
mushroom("red_mushroom_block", ["#c93a34", "#b8322c", "#a82c26"])
r = random.Random("red_mushroom_block")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(T.hx("#c93a34"))
for (x0, y0, w, h) in [(2, 2, 3, 3), (9, 4, 4, 3), (4, 9, 3, 4), (11, 10, 3, 3)]:
    for y in range(y0, min(16, y0 + h)):
        for x in range(x0, min(16, x0 + w)):
            px[x, y] = T.P(T.hx("#e8e2d6"))
save(img, "red_mushroom_block")
mushroom("mushroom_stem", ["#d8d2c6", "#cbc6b8"])

# --- sponges ---
r = random.Random("sponge")
img = noise_ramp(r, ["#c9c34a", "#bcb63e", "#afa832"], 0.06)
px = img.load()
for _ in range(12):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 0.78))
save(img, "sponge")
r = random.Random("wet_sponge")
img = noise_ramp(r, ["#a8a23c", "#9a9434", "#8c862c"], 0.06)
px = img.load()
for _ in range(10):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.hx("#6f8a50"))
save(img, "wet_sponge")

# --- cake ---
r = random.Random("cake_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        if y < 3:
            c = T.hx("#e8e2d6" if (x + y) % 3 else "#f4efe6")
        elif y < 6:
            c = T.hx("#b03c30" if x % 3 else "#a83228")
        else:
            c = T.hx("#d4a44c" if (x + y) % 4 else "#c49642")
        px[x, y] = T.P(c)
save(img, "cake_side")
r = random.Random("cake_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#e8e2d6" if (x + y) % 3 else "#f4efe6")
        px[x, y] = T.P(c)
for _ in range(8):
    x, y = r.randrange(2, 14), r.randrange(2, 14)
    px[x, y] = T.P(T.hx("#b03c30"))
save(img, "cake_top")
r = random.Random("cake_top_inner")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#f4efe6" if (x + y) % 3 else "#e8e2d6")
        px[x, y] = T.P(c)
save(img, "cake_top_inner")
r = random.Random("cake_bottom")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#c49642" if (x + y) % 4 else "#b88a3c")
        px[x, y] = T.P(c)
save(img, "cake_bottom")

# --- chiseled bookshelf ---
r = random.Random("chiseled_bookshelf_top")
img = planks_like(r, ["#c89a5b", "#b98d55", "#a97c48"])
save(img, "chiseled_bookshelf_top")
r = random.Random("chiseled_bookshelf_side")
img = planks_like(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for y in range(2, 14):
    for x in range(2, 14):
        if (x // 4 + y // 4) % 2:
            px[x, y] = T.P(T.shade(T.hx("#a97c48"), 0.85))
save(img, "chiseled_bookshelf_side")
r = random.Random("chiseled_bookshelf_empty")
img = planks_like(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for y in range(3, 13):
    for x in range(2, 14):
        px[x, y] = T.P(T.hx("#5a3c1e"))
save(img, "chiseled_bookshelf_empty")
r = random.Random("chiseled_bookshelf_occupied")
img = planks_like(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
BOOK = [T.hx(c) for c in ["#b03c30", "#3c54b0", "#5c8a34", "#e8cc3c", "#8a4ab0"]]
for shelf in range(3):
    y0 = 3 + shelf * 4
    x = 2
    while x < 13:
        w = r.randrange(1, 3)
        col = BOOK[r.randrange(5)]
        for dy in range(3):
            for dx in range(w):
                if x + dx < 13:
                    px[x + dx, y0 + dy] = T.P(T.shade(col, 1.0 - dy * 0.08))
        x += w + 1
save(img, "chiseled_bookshelf_occupied")


def planks_like(r, cols):
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        for x in range(16):
            c = pal[(x // 5 + y // 4) % len(pal)]
            if y % 4 == 3:
                c = T.shade(c, 0.82)
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
    return img


# --- nylium ---
def nylium(name, top_cols, side_top_cols):
    r = random.Random(name)
    img = noise_ramp(r, top_cols, 0.06)
    px = img.load()
    for _ in range(10):
        x, y = r.randrange(16), r.randrange(16)
        px[x, y] = T.P(T.shade(px[x, y], 1.18))
    save(img, name)
    r = random.Random(name + "_side")
    img2 = noise_ramp(r, ["#7a2a24", "#6a2420", "#5a1c18"], 0.06)
    px2 = img2.load()
    topc = [T.hx(c) for c in side_top_cols]
    for x in range(16):
        edge = 3 + (1 if r.random() < 0.4 else 0)
        for y in range(edge):
            px2[x, y] = T.P(topc[r.randrange(len(topc))])
    save(img2, name + "_side")


nylium("crimson_nylium", ["#8a1c30", "#7a1828", "#6a1422"], ["#8a1c30", "#7a1828", "#a82838"])
nylium("warped_nylium", ["#1c6a5c", "#165a50", "#124a42"], ["#1c6a5c", "#2c7a68", "#165a50"])

# --- blackstone family ---
BS = ["#2c2926", "#262422", "#1f1d1b"]
r = random.Random("polished_blackstone")
img = noise_ramp(r, BS[:2], 0.02)
px = img.load()
for i in range(16):
    px[i, 0] = T.P(T.shade(px[i, 0], 1.08))
    px[i, 15] = T.P(T.shade(px[i, 15], 0.85))
save(img, "polished_blackstone")


def black_bricks(name, seed, crack=False):
    r = random.Random(seed)
    img = T.new_img()
    px = img.load()
    cols = [T.hx(c) for c in ["#2c2926", "#262422", "#2a2724"]]
    for y in range(16):
        off = 4 if (y // 4) % 2 else 0
        for x in range(16):
            if y % 4 == 3 or (x + off) % 8 == 7:
                c = T.hx("#181614")
            else:
                c = cols[(x + off) // 8 % 3]
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
    if crack:
        x = r.randrange(4, 12)
        for y in range(16):
            px[x, y] = T.P(T.hx("#181614"))
            if r.random() < 0.3:
                x = max(0, min(15, x + r.choice((-1, 1))))
    save(img, name)


black_bricks("polished_blackstone_bricks", "pbb")
black_bricks("cracked_polished_blackstone_bricks", "cpbb", crack=True)
r = random.Random("chiseled_polished_blackstone")
img = T.new_img()
px = img.load()
pal = [T.hx(c) for c in BS]
for y in range(16):
    for x in range(16):
        c = pal[(x + y) % 2]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for i in range(1, 15):
    px[i, 3] = T.P(T.shade(pal[0], 1.3))
    px[i, 12] = T.P(T.shade(pal[0], 1.3))
save(img, "chiseled_polished_blackstone")
r = random.Random("gilded_blackstone")
img = noise_ramp(r, BS, 0.04)
px = img.load()
gold = [T.hx(c) for c in ["#c99f2f", "#f2c94c"]]
for _ in range(10):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(gold[r.randrange(2)])
save(img, "gilded_blackstone")

# --- tuff bricks ---
r = random.Random("tuff_bricks")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#8a8570", "#7f7a66", "#76715e"]]
for y in range(16):
    off = 4 if (y // 4) % 2 else 0
    for x in range(16):
        if y % 4 == 3 or (x + off) % 8 == 7:
            c = T.hx("#5f5c4c")
        else:
            c = cols[(x + off) // 8 % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "tuff_bricks")
r = random.Random("polished_tuff")
img = noise_ramp(r, ["#8a8570", "#7f7a66"], 0.02)
px = img.load()
for i in range(16):
    px[i, 15] = T.P(T.shade(px[i, 15], 0.85))
save(img, "polished_tuff")

# --- chorus plant and flower ---
r = random.Random("chorus_plant")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#6a5a78", "#5f5070", "#544664"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x + y) % 3])
for i in range(16):
    px[i, 7] = T.P(T.shade(cols[0], 0.8))
    px[7, i] = T.P(T.shade(cols[0], 0.8))
save(img, "chorus_plant")
r = random.Random("chorus_flower")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x + y) % 3])
for _ in range(9):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(cols[1], 1.18))
save(img, "chorus_flower")

# --- end rod (transparent) ---
img = T.new_img()
px = img.load()
rod = [T.hx("#e8dfb0"), T.hx("#d8cf9e")]
for y in range(1, 15):
    for x in (7, 8):
        px[x, y] = T.P(rod[y % 2])
px[6, 14] = T.P(T.hx("#968f84"))
px[9, 14] = T.P(T.hx("#968f84"))
px[7, 15] = T.P(T.hx("#968f84"))
px[8, 15] = T.P(T.hx("#968f84"))
save(img, "end_rod")

# --- respawn anchor (sides 0-2, top, bottom) ---
def anchor_side(name, fill_rows):
    r = random.Random(name)
    img = T.new_img()
    px = img.load()
    for y in range(16):
        for x in range(16):
            c = T.hx("#2c2926" if (x + y) % 3 else "#242220")
            px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
    glow = [T.hx(c) for c in ["#c93a8a", "#e85ca8", "#8a2c5c"]]
    for row in range(fill_rows):
        y = 15 - row * 2
        for x in range(16):
            if x % 4 != 3:
                px[x, y] = T.P(glow[min(row, 2)])
    save(img, name)


anchor_side("respawn_anchor_side0", 0)
anchor_side("respawn_anchor_side1", 1)
anchor_side("respawn_anchor_side2", 2)
r = random.Random("respawn_anchor_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(T.hx("#2c2926" if (x + y) % 3 else "#242220"))
for _ in range(8):
    x, y = r.randrange(3, 13), r.randrange(3, 13)
    px[x, y] = T.P(T.hx("#e85ca8"))
save(img, "respawn_anchor_top")
r = random.Random("respawn_anchor_bottom")
img = noise_ramp(r, BS, 0.03)
save(img, "respawn_anchor_bottom")

# --- lodestone ---
r = random.Random("lodestone_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#5a5a58" if (x + y) % 3 else "#4f4f4d")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
for i in range(1, 15):
    px[i, 0] = T.P(T.hx("#968f84"))
    px[i, 15] = T.P(T.hx("#968f84"))
    px[0, i] = T.P(T.hx("#968f84"))
    px[15, i] = T.P(T.hx("#968f84"))
save(img, "lodestone_side")
r = random.Random("lodestone_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(T.hx("#5a5a58" if (x + y) % 3 else "#4f4f4d"))
for i in range(3, 13):
    px[i, 3] = T.P(T.hx("#968f84"))
    px[i, 12] = T.P(T.hx("#968f84"))
    px[3, i] = T.P(T.hx("#968f84"))
    px[12, i] = T.P(T.hx("#968f84"))
save(img, "lodestone_top")

print("gen16 done: 35 misc textures")
