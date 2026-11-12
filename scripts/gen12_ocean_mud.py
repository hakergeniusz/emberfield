"""Emberfield gen 12: prismarine family, mud, warts, shroomlight, slime,
kelp, target — the last everyday gameplay surfaces. 16 textures."""
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


def speckle(px, rng, n=10, f=0.9):
    for _ in range(n):
        x, y = rng.randrange(16), rng.randrange(16)
        px[x, y] = T.P(T.shade(px[x, y], f))


# --- prismarine family ---
r = random.Random("prismarine")
img = noise_ramp(r, ["#5f9c8a", "#548e7d", "#497f70"], 0.06)
px = img.load()
for _ in range(8):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 1.12))
save(img, "prismarine")
r = random.Random("prismarine_bricks")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#5f9c8a", "#548e7d", "#4c8474"]]
for y in range(16):
    row = y // 2
    off = 2 if row % 2 else 0
    for x in range(16):
        if y % 2 == 1:
            c = T.shade(cols[2], 0.85)
        else:
            c = cols[(x + off) // 4 % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "prismarine_bricks")
r = random.Random("dark_prismarine")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#2c5e50", "#255246", "#1f473d"]]
for y in range(16):
    row_border = y % 4 == 3
    for x in range(16):
        c = cols[(x // 4 + y // 4) % 3]
        if row_border:
            c = T.shade(c, 0.82)
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "dark_prismarine")
r = random.Random("sea_lantern")
img = T.new_img()
px = img.load()
base = [T.hx(c) for c in ["#cfe4d8", "#c0d8cc", "#b2ccbe"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(base[(x * 2 + y) % 3])
for _ in range(10):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.hx("#eef8f2"))
save(img, "sea_lantern")

# --- moss and mud ---
r = random.Random("moss_block")
img = noise_ramp(r, ["#5a8a34", "#4f7c2c", "#447026"], 0.06)
px = img.load()
for _ in range(12):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 1.15))
save(img, "moss_block")
r = random.Random("mud")
img = noise_ramp(r, ["#3f3226", "#372c22", "#30261e"], 0.05)
px = img.load()
for _ in range(6):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 1.1))
save(img, "mud")
r = random.Random("packed_mud")
img = noise_ramp(r, ["#8a6a4a", "#7d5f42", "#715639"], 0.04)
speckle(img.load(), r, 8, 0.92)
save(img, "packed_mud")
r = random.Random("mud_bricks")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#8a6a4a", "#7d5f42", "#75583c"]]
for y in range(16):
    off = 4 if (y // 4) % 2 else 0
    for x in range(16):
        if y % 4 == 3 or (x + off) % 8 == 7:
            c = T.hx("#5f4830")
        else:
            c = cols[(x + off) // 8 % 3]
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "mud_bricks")

# --- dripstone ---
r = random.Random("dripstone_block")
img = noise_ramp(r, ["#8a6a54", "#7d5f4a", "#715542"], 0.05)
speckle(img.load(), r, 10, 0.9)
save(img, "dripstone_block")

# --- warts and shroomlight ---
r = random.Random("nether_wart_block")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#7a1014", "#6a0e12", "#5a0c0e"]]
bumps = [T.hx(c) for c in ["#8f1c1c", "#a22422"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x * 3 + y * 5) % 3])
for _ in range(16):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(bumps[r.randrange(2)])
save(img, "nether_wart_block")
r = random.Random("warped_wart_block")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#1c5c50", "#16504a", "#124540"]]
bumps = [T.hx(c) for c in ["#2c7a66", "#3c8a74"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x * 3 + y * 5) % 3])
for _ in range(16):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(bumps[r.randrange(2)])
save(img, "warped_wart_block")
r = random.Random("shroomlight")
img = T.new_img()
px = img.load()
base = [T.hx(c) for c in ["#d98a3c", "#c97a30", "#b86e2a"]]
glow = [T.hx(c) for c in ["#f2c23e", "#f8dd7a"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(base[(x + y) % 3])
for _ in range(12):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(glow[r.randrange(2)])
save(img, "shroomlight")

# --- slime and kelp ---
r = random.Random("slime_block")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#7ac26a" if (x + y) % 3 else "#6cb25c")
        px[x, y] = (c[0], c[1], c[2], 200)
for (x0, y0) in [(4, 4), (11, 9)]:
    for i in range(3):
        px[(x0 + i) % 16, (y0 + i) % 16] = T.P((230, 250, 225, 210))
save(img, "slime_block")
r = random.Random("dried_kelp_side")
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ["#3a4a2c", "#324226", "#2a3a20"]]
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(cols[(x + y * 3) % 3])
for _ in range(9):
    x, y = r.randrange(16), r.randrange(16)
    px[x, y] = T.P(T.shade(cols[0], 1.25))
save(img, "dried_kelp_side")
r = random.Random("dried_kelp_bottom")
img = noise_ramp(r, ["#324226", "#2a3a20"], 0.04)
speckle(img.load(), r, 8, 1.15)
save(img, "dried_kelp_bottom")

# --- target block ---
r = random.Random("target_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        ring = max(abs(x - 7.5), abs(y - 7.5))
        if ring < 2.5:
            c = T.hx("#e03c3c")
        elif ring < 4.5:
            c = T.hx("#e8e2d6")
        elif ring < 6.5:
            c = T.hx("#c9342c")
        else:
            c = T.hx("#d8d2c6" if (x + y) % 3 else "#c4beb2")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "target_side")
r = random.Random("target_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        if d < 2.5:
            c = T.hx("#e03c3c")
        elif d < 5:
            c = T.hx("#e8e2d6")
        else:
            c = T.hx("#c9342c")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "target_top")

print("gen12 done: 16 ocean/mud/redstone-surround textures")
