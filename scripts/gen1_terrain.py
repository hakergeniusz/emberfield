"""Emberfield gen 1: terrain blocks (dirt/grass/stone family). 12 textures."""
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"
open(MAN, "w").close()


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")
    print("wrote", name)


def dirt_base(rng):
    n = T.fbm(rng)
    img = T.ramp(n, ['#9a7148', '#8a5f3d', '#7d5437', '#6e4830', '#5e3c29'], rng, 0.05)
    px = img.load()
    for _ in range(10):
        x = rng.randrange(16)
        y = rng.randrange(16)
        px[x, y] = T.P(T.shade(px[x, y], 0.82))
    return img


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


# dirt
save(dirt_base(random.Random('dirt')), 'dirt')

# coarse_dirt
rng = random.Random('coarse_dirt')
img = dirt_base(rng)
px = img.load()
for _ in range(6):
    x = rng.randrange(1, 14)
    y = rng.randrange(1, 14)
    px[x, y] = T.P(T.hx('#8f7f66'))
    px[x + 1, y] = T.P(T.hx('#7b6c58'))
    if rng.random() < 0.7:
        px[x, y + 1] = T.P(T.hx('#6b5d4c'))
save(img, 'coarse_dirt')

# grass_block_top (kept grayscale -> biome tint colors it)
rng = random.Random('grass_block_top')
n = T.fbm(rng, cells=(5, 2))
for x in range(16):
    off = rng.uniform(-0.06, 0.06)
    for y in range(16):
        n[y][x] += off
img = T.ramp(n, ['#a6a6a6', '#9a9a9a', '#8c8c8c', '#7e7e7e', '#707070'], rng, 0.04)
px = img.load()
for _ in range(9):
    x = rng.randrange(16)
    y = rng.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 1.10))
save(img, 'grass_block_top')

# grass_block_side (baked dirt + warm olive fringe)
rng = random.Random('grass_block_side')
img = dirt_base(rng)
px = img.load()
grl = T.hx('#a3a94e')
grm = T.hx('#8f9440')
grd = T.hx('#6e7a30')
shd = T.hx('#543726')
for x in range(16):
    d = rng.choice((2, 3, 3, 3, 4))
    for y in range(d):
        c = grl if y == 0 else (grd if y == d - 1 else grm)
        px[x, y] = T.P(c)
    px[x, d] = T.P(shd)
    if rng.random() < 0.3:
        px[x, d + 1] = T.P(grd)
save(img, 'grass_block_side')

# grass_block_side_overlay (grayscale fringe, tinted by biome)
rng = random.Random('grass_block_side_overlay')
img = T.new_img()
px = img.load()
for x in range(16):
    d = rng.choice((2, 3, 3, 3, 4))
    for y in range(d):
        g = '#cfcfcf' if y == 0 else ('#8f8f8f' if y == d - 1 else '#ababab')
        px[x, y] = T.P(T.hx(g))
save(img, 'grass_block_side_overlay')

# stone
save(stone_base(random.Random('stone')), 'stone')

# cobblestone
rng = random.Random('cobblestone')
img = T.voronoi(rng, 9, ['#8f887c', '#837c70', '#777064', '#6b6459'], '#45413b',
                edge=1.15, jitter=0.07)
px = img.load()
for _ in range(8):
    x = rng.randrange(16)
    y = rng.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 0.88))
save(img, 'cobblestone')

# deepslate (vertical striation)
rng = random.Random('deepslate')
n = T.fbm(rng, cells=(6, 2))
for x in range(16):
    off = rng.uniform(-0.08, 0.08)
    for y in range(16):
        n[y][x] += off
save(T.ramp(n, ['#4c4845', '#43403d', '#3a3734', '#322f2c'], rng, 0.03), 'deepslate')

# deepslate_top
rng = random.Random('deepslate_top')
n = T.fbm(rng, cells=(3, 2))
save(T.ramp(n, ['#54504b', '#4c4845', '#43403d', '#3a3734'], rng, 0.04), 'deepslate_top')

# sand
rng = random.Random('sand')
n = T.fbm(rng, cells=(5, 3))
img = T.ramp(n, ['#e2d3a4', '#d8c896', '#cdbc85', '#c2b17b', '#b7a770'], rng, 0.03)
px = img.load()
for _ in range(14):
    x = rng.randrange(16)
    y = rng.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 0.92))
save(img, 'sand')

# gravel
rng = random.Random('gravel')
save(T.voronoi(rng, 11, ['#9a9187', '#8d867d', '#7b7168', '#6e675e', '#8f7f6a', '#5f5952'],
                '#524c46', edge=0.95, jitter=0.10), 'gravel')

# bedrock
rng = random.Random('bedrock')
n = T.fbm(rng, cells=(3, 2), weights=(0.6, 0.4))
img = T.quant(n, [(0.34, '#262421'), (0.52, '#38352f'), (0.72, '#4a463f'), (1.01, '#5c574e')])
px = img.load()
for _ in range(6):
    x = rng.randrange(16)
    y = rng.randrange(16)
    px[x, y] = T.P(T.shade(px[x, y], 0.85))
save(img, 'bedrock')

print("gen1 done: 12 textures")
