"""Emberfield gen 3: ores, metal/gem/coal blocks, crafting table, furnace. 15 textures."""
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")
    print("wrote", name)


def stone_base(rng):
    n = T.fbm(rng)
    img = T.ramp(n, ['#8f887c', '#837c70', '#777064', '#6b6459', '#5d574d'], rng, 0.03)
    px = img.load()
    for _ in range(2):
        x = rng.randrange(3, 13)
        y = rng.randrange(2, 12)
        for _ in range(4):
            px[x, y] = T.P(T.shade(px[x, y], 0.85))
            x = min(15, x + rng.choice((0, 1, 1)))
            y = min(15, y + rng.choice((0, 1)))
    return img


def ore(rng, palette, n_clusters=3, rmin=1.4, rmax=2.0):
    img = stone_base(rng)
    specs = [(rng.randrange(3, 13), rng.randrange(3, 13), rng.uniform(rmin, rmax))
             for _ in range(n_clusters)]
    mask = T.blob_mask(rng, specs)
    T.paint_blob(img, mask, palette, rng)
    return img


# ores on warm stone
save(ore(random.Random('coal_ore'), ('#151412', '#262422', '#2e2c2a', '#45423e'),
         n_clusters=4, rmin=1.5, rmax=2.1), 'coal_ore')
save(ore(random.Random('iron_ore'), ('#7d5c46', '#b98d72', '#d8af93', '#e6c4a8')), 'iron_ore')
save(ore(random.Random('gold_ore'), ('#8a6a1e', '#c99f2f', '#f2c94c', '#f8dd7a')), 'gold_ore')
save(ore(random.Random('diamond_ore'), ('#2f7a72', '#4fb8ac', '#7de0d8', '#aef0ea')), 'diamond_ore')

# coal_block: charcoal facets
rng = random.Random('coal_block')
n = T.fbm(rng, cells=(3, 2), weights=(0.6, 0.4))
img = T.quant(n, [(0.3, '#1e1c1a'), (0.55, '#262422'), (0.8, '#2e2c2a'), (1.01, '#38352f')])
px = img.load()
for _ in range(5):
    x = rng.randrange(1, 13)
    y = rng.randrange(1, 13)
    for i in range(rng.choice((2, 3))):
        xx = min(15, x + i)
        yy = max(0, y - i)
        px[xx, yy] = T.P(T.hx('#45423e'))
for i in range(16):
    px[i, 15] = T.P(T.shade(px[i, 15], 0.9))
    px[15, i] = T.P(T.shade(px[15, i], 0.92))
save(img, 'coal_block')


def metal_panel(rng, base, light, dark, deep):
    img = T.new_img()
    px = img.load()
    b = T.hx(base)
    for y in range(16):
        for x in range(16):
            px[x, y] = T.P(T.shade(b, 1.0 + rng.uniform(-0.015, 0.015)))
    for i in range(16):
        px[i, 0] = T.P(T.hx(light))
        px[0, i] = T.P(T.shade(T.hx(light), 0.96))
        px[i, 15] = T.P(T.hx(dark))
        px[15, i] = T.P(T.shade(T.hx(dark), 0.94))
    for (x, y) in ((0, 0), (15, 0), (0, 15), (15, 15)):
        px[x, y] = T.P(T.hx(deep))
    return img


# iron_block
rng = random.Random('iron_block')
img = metal_panel(rng, '#d0cbc2', '#e8e4dc', '#a8a29a', '#8a847c')
save(img, 'iron_block')

# gold_block with diagonal shine
rng = random.Random('gold_block')
img = metal_panel(rng, '#f2c94c', '#fbe98e', '#c99f2f', '#a87f24')
px = img.load()
for (x, y) in ((3, 3), (4, 4), (5, 5), (4, 3), (5, 4), (6, 5)):
    px[x, y] = T.P(T.shade(T.hx('#fbe98e'), 1.05))
save(img, 'gold_block')

# diamond_block with corner facet glints
rng = random.Random('diamond_block')
img = metal_panel(rng, '#7de0d8', '#aef0ea', '#4fb8ac', '#35918a')
px = img.load()
for (x, y) in ((2, 2), (3, 2), (2, 3), (13, 2), (13, 3), (2, 13), (3, 13), (13, 13)):
    px[x, y] = T.P(T.hx('#d4faf6'))
save(img, 'diamond_block')


def planks(rng, dark=False):
    tones = (['#b08a50', '#a37e46', '#957040', '#8a663a'] if dark
             else ['#c89a5b', '#b98d55', '#a97c48', '#9c7040'])
    img = T.new_img()
    px = img.load()
    seam = T.hx('#6b4a2a')
    for r in range(4):
        base = T.hx(tones[rng.randrange(4)])
        for y in range(r * 4, r * 4 + 3):
            for x in range(16):
                c = base
                rr = rng.random()
                if rr < 0.10:
                    c = T.shade(c, 0.92)
                elif rr < 0.18:
                    c = T.shade(c, 1.06)
                if y % 4 == 0:
                    c = T.shade(c, 1.05)
                px[x, y] = T.P(c)
        for x in range(16):
            px[x, r * 4 + 3] = T.P(seam)
        if r % 2 == 0:
            for y in range(r * 4, r * 4 + 3):
                px[7, y] = T.P(seam)
        else:
            for y in range(r * 4, r * 4 + 3):
                px[3, y] = T.P(seam)
                px[11, y] = T.P(seam)
    return img


# crafting_table_top: bordered honey planks + 3x3 work grid
rng = random.Random('crafting_table_top')
img = planks(rng)
px = img.load()
border = T.hx('#6b4a2a')
grid = T.hx('#5c4026')
for i in range(16):
    for (x, y) in ((i, 0), (i, 15), (0, i), (15, i)):
        px[x, y] = T.P(border)
for i in (5, 10):
    for j in range(1, 15):
        px[i, j] = T.P(grid)
        px[j, i] = T.P(grid)
for cx in (2, 7, 12):
    for cy in (2, 7, 12):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x = cx + dx
                y = cy + dy
                if 1 <= x <= 14 and 1 <= y <= 14 and x not in (5, 10) and y not in (5, 10):
                    px[x, y] = T.P(T.shade(px[x, y], 1.07))
save(img, 'crafting_table_top')

# crafting_table_side: darker planks + heavy skirt
rng = random.Random('crafting_table_side')
img = planks(rng, dark=True)
px = img.load()
for y in (13, 14, 15):
    for x in range(16):
        px[x, y] = T.P(T.shade(px[x, y], 0.85))
save(img, 'crafting_table_side')

# crafting_table_front: work grid panel
rng = random.Random('crafting_table_front')
img = planks(rng)
px = img.load()
panel_o = T.hx('#3e2c1c')
panel_i = T.hx('#5c4026')
sq = T.hx('#d9c49a')
for y in range(4, 13):
    for x in range(3, 13):
        px[x, y] = T.P(panel_o)
for y in range(5, 12):
    for x in range(4, 12):
        px[x, y] = T.P(panel_i)
for (sx, sy) in ((5, 6), (9, 6), (5, 9), (9, 9)):
    for dy in (0, 1):
        for dx in (0, 1):
            px[sx + dx, sy + dy] = T.P(sq)
save(img, 'crafting_table_front')


def furnace_base(rng):
    n = T.fbm(rng, cells=(4, 2))
    img = T.ramp(n, ['#8a8378', '#7e786e', '#726c62', '#66605a', '#5a544e'], rng, 0.03)
    px = img.load()
    for i in range(16):
        px[i, 0] = T.P(T.shade(px[i, 0], 1.08))
        px[0, i] = T.P(T.shade(px[0, i], 1.04))
        px[i, 15] = T.P(T.shade(px[i, 15], 0.90))
        px[15, i] = T.P(T.shade(px[15, i], 0.94))
    return img


# furnace_side
save(furnace_base(random.Random('furnace_side')), 'furnace_side')

# furnace_top: beveled stone + center vent plate
rng = random.Random('furnace_top')
img = furnace_base(rng)
px = img.load()
for y in range(5, 11):
    for x in range(5, 11):
        if x in (5, 10) or y in (5, 10):
            px[x, y] = T.P(T.hx('#45413c'))
        else:
            px[x, y] = T.P(T.hx('#5a544e'))
for (x, y) in ((7, 7), (8, 7), (7, 8), (8, 8)):
    px[x, y] = T.P(T.hx('#262422'))
save(img, 'furnace_top')


def furnace_front(rng, lit):
    img = furnace_base(rng)
    px = img.load()
    for y in range(7, 14):
        for x in range(3, 13):
            px[x, y] = T.P(T.hx('#3e3a36'))
    for y in range(8, 13):
        for x in range(4, 12):
            px[x, y] = T.P(T.hx('#1a1816'))
    if not lit:
        for x in range(4, 12):
            if rng.random() < 0.4:
                px[x, 12] = T.P(T.hx('#5a2a18'))
            if rng.random() < 0.25:
                px[x, 12] = T.P(T.hx('#3a3230'))
    else:
        for x in range(4, 12):
            px[x, 12] = T.P(T.hx('#c25a24') if rng.random() < 0.6 else T.hx('#e89a3a'))
            rr = rng.random()
            if rr < 0.75:
                px[x, 11] = T.P(T.hx('#d97a34') if rng.random() < 0.6 else T.hx('#e89a3a'))
            rr = rng.random()
            if rr < 0.5:
                px[x, 10] = T.P(T.hx('#f2c23e') if rng.random() < 0.7 else T.hx('#e89a3a'))
            rr = rng.random()
            if rr < 0.28:
                px[x, 9] = T.P(T.hx('#f2c23e') if rng.random() < 0.5 else T.hx('#f8dd7a'))
            rr = rng.random()
            if rr < 0.12:
                px[x, 8] = T.P(T.hx('#f8dd7a'))
    return img


save(furnace_front(random.Random('furnace_front'), False), 'furnace_front')
save(furnace_front(random.Random('furnace_front_on'), True), 'furnace_front_on')

print("gen3 done: 15 textures")
