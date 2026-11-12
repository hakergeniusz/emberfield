"""Emberfield gen 14: functional-block faces (loom, cartography, smithing,
fletching, jukebox, grindstone, stonecutter, composter, enchanting) and the
coral-block family. 31 textures."""
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


def framed(img, edge_f=0.85):
    px = img.load()
    for i in range(16):
        px[i, 0] = T.P(T.shade(px[i, 0], 1.06))
        px[0, i] = T.P(T.shade(px[0, i], 1.03))
        px[i, 15] = T.P(T.shade(px[i, 15], edge_f))
        px[15, i] = T.P(T.shade(px[15, i], edge_f))


def planks_base(rng, cols):
    img = T.new_img()
    px = img.load()
    pal = [T.hx(c) for c in cols]
    for y in range(16):
        for x in range(16):
            c = pal[(x // 5 + y // 4) % len(pal)]
            if y % 4 == 3:
                c = T.shade(c, 0.82)
            px[x, y] = T.P(T.shade(c, 1.0 + rng.uniform(-0.02, 0.02)))
    return img


# --- loom (oak frame, wool lattice front) ---
r = random.Random("loom_top")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
save(img, "loom_top")
r = random.Random("loom_side")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for y in range(2, 14):
    for x in range(3, 13):
        if (x + y) % 2 == 0:
            px[x, y] = T.P(T.hx("#d8d2c6"))
save(img, "loom_side")
r = random.Random("loom_front")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for x in range(3, 13):
    px[x, 4] = T.P(T.hx("#b03c30"))
    px[x, 7] = T.P(T.hx("#3c54b0"))
    px[x, 10] = T.P(T.hx("#e8cc3c"))
for y in range(4, 11):
    px[4, y] = T.P(T.hx("#d8d2c6"))
    px[11, y] = T.P(T.hx("#d8d2c6"))
save(img, "loom_front")

# --- cartography (top = map table; sides with paper) ---
r = random.Random("cartography_table_top")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for y in range(3, 13):
    for x in range(3, 13):
        px[x, y] = T.P(T.hx("#e8e2d6" if (x + y) % 5 else "#d4cec2"))
save(img, "cartography_table_top")
r = random.Random("cartography_table_side1")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for y in range(4, 12):
    for x in range(4, 12):
        px[x, y] = T.P(T.hx("#e8e2d6"))
save(img, "cartography_table_side1")
r = random.Random("cartography_table_side2")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for x in range(2, 14):
    px[x, 6] = T.P(T.hx("#e8e2d6"))
    px[x, 7] = T.P(T.hx("#e8e2d6"))
save(img, "cartography_table_side2")
r = random.Random("cartography_table_side3")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for (x0, y0) in [(3, 4), (9, 8)]:
    for dy in range(5):
        for dx in range(4):
            px[x0 + dx, y0 + dy] = T.P(T.hx("#e8e2d6" if (dx + dy) % 4 else "#d4cec2"))
save(img, "cartography_table_side3")

# --- smithing (dark iron-ribbed) ---
r = random.Random("smithing_table_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#4a4a48" if (x + y) % 3 else "#3f3f3d")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
for i in range(2, 14):
    px[i, 3] = T.P(T.hx("#968f84"))
    px[i, 12] = T.P(T.hx("#968f84"))
save(img, "smithing_table_top")
r = random.Random("smithing_table_side")
img = planks_base(r, ["#8a663a", "#7d5c34", "#6f522c"])
px = img.load()
for i in range(2, 14):
    px[i, 2] = T.P(T.hx("#968f84"))
    px[2, i] = T.P(T.hx("#968f84"))
    px[13, i] = T.P(T.hx("#968f84"))
save(img, "smithing_table_side")
r = random.Random("smithing_table_front")
img = planks_base(r, ["#8a663a", "#7d5c34", "#6f522c"])
px = img.load()
for y in range(5, 12):
    for x in range(5, 11):
        px[x, y] = T.P(T.hx("#4a4a48" if (x + y) % 3 else "#3f3f3d"))
px[7, 8] = T.P(T.hx("#e89a3a"))
save(img, "smithing_table_front")

# --- fletching ---
r = random.Random("fletching_table_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#e8e2d6" if (x + y) % 3 else "#d4cec2")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.02, 0.02)))
save(img, "fletching_table_top")
r = random.Random("fletching_table_side")
img = planks_base(r, ["#c89a5b", "#b98d55", "#a97c48"])
px = img.load()
for i in range(2, 14):
    px[i, 8] = T.P(T.hx("#d8d2c6"))
save(img, "fletching_table_side")

# --- jukebox ---
r = random.Random("jukebox_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        if d < 3.2:
            c = T.hx("#2a1e14")
        elif d < 4.2:
            c = T.hx("#968f84")
        else:
            c = T.hx("#8a663a" if (x + y) % 3 else "#7d5c34")
        px[x, y] = T.P(c)
save(img, "jukebox_top")
r = random.Random("jukebox_side")
img = planks_base(r, ["#8a663a", "#7d5c34", "#6f522c"])
px = img.load()
for i in range(2, 14):
    px[i, 2] = T.P(T.hx("#968f84"))
    px[i, 13] = T.P(T.hx("#968f84"))
save(img, "jukebox_side")

# --- grindstone (stone round + wood pivot) ---
r = random.Random("grindstone_round")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 7.5)
        if d < 5.5:
            c = T.hx("#8f887c" if int(d) % 2 else "#837c70")
        else:
            c = None
        if d < 1.8:
            c = T.hx("#6f522c")
        px[x, y] = T.P(c) if c else (0, 0, 0, 0)
save(img, "grindstone_round")
r = random.Random("grindstone_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#8f887c" if (x + y) % 3 else "#837c70")
        px[x, y] = T.P(c)
for i in range(6, 10):
    px[i, 7] = T.P(T.hx("#6f522c"))
    px[i, 8] = T.P(T.hx("#6f522c"))
save(img, "grindstone_side")
r = random.Random("grindstone_pivot")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#6f522c" if (x + y) % 3 else "#5f4624")
        px[x, y] = T.P(c)
save(img, "grindstone_pivot")

# --- stonecutter (dark base, metal saw) ---
r = random.Random("stonecutter_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#4a4a48" if (x + y) % 3 else "#3f3f3d")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "stonecutter_side")
r = random.Random("stonecutter_bottom")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#3f3f3d" if (x * 2 + y) % 3 else "#363634")
        px[x, y] = T.P(c)
save(img, "stonecutter_bottom")
r = random.Random("stonecutter_saw")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        if 3 <= y <= 7:
            c = T.hx("#968f84" if x % 2 else "#a8a29a")
        else:
            c = None
        px[x, y] = T.P(c) if c else (0, 0, 0, 0)
save(img, "stonecutter_saw")
r = random.Random("stonecutter_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#4a4a48" if (x + y) % 3 else "#3f3f3d")
        px[x, y] = T.P(c)
for i in range(2, 14):
    px[i, 8] = T.P(T.hx("#968f84"))
save(img, "stonecutter_top")

# --- composter ---
r = random.Random("composter_top")
img = planks_base(r, ["#8a663a", "#7d5c34", "#6f522c"])
px = img.load()
for y in range(2, 14):
    for x in range(2, 14):
        c = T.hx("#3a2a18" if (x + y) % 4 else "#45331f")
        px[x, y] = T.P(c)
for _ in range(6):
    x, y = r.randrange(3, 13), r.randrange(3, 13)
    px[x, y] = T.P(T.hx("#5f7a2c"))
save(img, "composter_top")
r = random.Random("composter_side")
img = planks_base(r, ["#8a663a", "#7d5c34", "#6f522c"])
px = img.load()
for i in range(2, 14):
    px[2, i] = T.P(T.shade(T.hx("#6f522c"), 0.8))
    px[13, i] = T.P(T.shade(T.hx("#6f522c"), 0.8))
save(img, "composter_side")
r = random.Random("composter_bottom")
img = planks_base(r, ["#6f522c", "#65482a", "#5a4025"])
save(img, "composter_bottom")

# --- enchanting table ---
r = random.Random("enchanting_table_top")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#1a1424" if (x * 3 + y) % 4 else "#221a30")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.04, 0.04)))
for i in range(3, 13):
    px[i, 5] = T.P(T.hx("#c9b8b0"))
    px[i, 10] = T.P(T.hx("#c9b8b0"))
save(img, "enchanting_table_top")
r = random.Random("enchanting_table_side")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        if y < 4:
            c = T.hx("#1a1424")
        elif y < 6:
            c = T.hx("#c9b8b0")
        else:
            c = T.hx("#2a2038" if (x + y) % 3 else "#221a30")
        px[x, y] = T.P(T.shade(c, 1.0 + r.uniform(-0.03, 0.03)))
save(img, "enchanting_table_side")
r = random.Random("enchanting_table_bottom")
img = T.new_img()
px = img.load()
for y in range(16):
    for x in range(16):
        c = T.hx("#1a1424" if (x + y) % 3 else "#140f1c")
        px[x, y] = T.P(c)
save(img, "enchanting_table_bottom")

# --- coral blocks (5 alive, 5 dead) ---
CORAL = [
    ("tube", "#3c54b0", "#2c4494"), ("brain", "#e06ca0", "#c95a8c"),
    ("bubble", "#a03cc9", "#8a32b0"), ("fire", "#c93a2a", "#b02e20"),
    ("horn", "#e0c23c", "#c9ad30"),
]
for (name, c0, c1) in CORAL:
    r = random.Random("coral_" + name)
    img = T.new_img()
    px = img.load()
    hi, lo = T.hx(c0), T.hx(c1)
    bumps = T.shade(hi, 1.15)
    for y in range(16):
        for x in range(16):
            px[x, y] = T.P(hi if (x * 2 + y) % 3 else lo)
    for _ in range(14):
        x, y = r.randrange(16), r.randrange(16)
        px[x, y] = T.P(bumps)
    framed(img, 0.88)
    save(img, name + "_coral_block")
    r2 = random.Random("dead_" + name)
    img2 = T.ramp(T.fbm(r2), ["#7a7468", "#6f6a5e", "#645e54"], 0.04)
    px2 = img2.load()
    for _ in range(12):
        x, y = r2.randrange(16), r2.randrange(16)
        px2[x, y] = T.P(T.shade(px2[x, y], 0.88))
    save(img2, "dead_" + name + "_coral_block")

print("gen14 done: 31 functional/coral textures")
