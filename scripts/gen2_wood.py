"""Emberfield gen 2: oak wood family, leaves, glass, bricks, bookshelf, torch. 8 textures."""
import math
import random
import texlib as T

OUT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/block"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def save(img, name):
    img.save(OUT + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("block/" + name + "\n")
    print("wrote", name)


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


# oak_planks
save(planks(random.Random('oak_planks')), 'oak_planks')

# oak_log (vertical bark streaks)
rng = random.Random('oak_log')
img = T.new_img()
px = img.load()
colv = [rng.random() for _ in range(16)]
cols = [T.hx(c) for c in ['#644626', '#6f4f2e', '#7d5a36', '#825d36']]
for y in range(16):
    for x in range(16):
        v = colv[x] + rng.uniform(-0.06, 0.06)
        i = int(v * 4)
        i = 0 if i < 0 else (3 if i > 3 else i)
        px[x, y] = T.P(cols[i])
for _ in range(2):
    x = rng.randrange(2, 14)
    y = rng.randrange(2, 14)
    px[x, y] = T.P(T.hx('#4c341c'))
save(img, 'oak_log')

# oak_log_top (rings + bark border)
rng = random.Random('oak_log_top')
img = T.new_img()
px = img.load()
rings = ['#8f6a3a', '#c89a5b', '#a97c48', '#b98d55', '#9c7040', '#b98d55', '#a97c48']
bark = [T.hx(c) for c in ['#644626', '#6f4f2e', '#7d5a36', '#825d36']]
colb = [rng.randrange(4) for _ in range(16)]
for y in range(16):
    for x in range(16):
        mv = max(abs(x - 7.5), abs(y - 7.5))
        if mv >= 6.5:
            c = T.shade(bark[colb[x]], 1.0 + rng.uniform(-0.05, 0.05))
        else:
            c = T.shade(T.hx(rings[int(mv)]), 1.0 + rng.uniform(-0.04, 0.04))
        px[x, y] = T.P(c)
save(img, 'oak_log_top')

# oak_leaves (transparent cutout, bright so biome tint reads well)
rng = random.Random('oak_leaves')
img = T.new_img()
px = img.load()
cols = [T.hx(c) for c in ['#b8d494', '#a8c584', '#98b874', '#88a866']]
dark = T.hx('#6f8a50')
centers = [(rng.randrange(16), rng.randrange(16), rng.uniform(1.9, 3.0)) for _ in range(12)]
filled = [[False] * 16 for _ in range(16)]
for y in range(16):
    for x in range(16):
        for (cx, cy, r) in centers:
            d = math.hypot(T.wd(x, cx), T.wd(y, cy))
            if d <= r - 0.4 + rng.random() * 0.9:
                filled[y][x] = True
                break
n = T.fbm(rng, cells=(3, 3))
for y in range(16):
    for x in range(16):
        if filled[y][x]:
            v = n[y][x] + rng.uniform(-0.05, 0.05)
            if v < 0.18:
                c = dark
            elif v < 0.40:
                c = cols[3]
            elif v < 0.62:
                c = cols[2]
            elif v < 0.85:
                c = cols[1]
            else:
                c = cols[0]
            px[x, y] = T.P(c)
save(img, 'oak_leaves')

# glass (transparent, framed, streaks)
rng = random.Random('glass')
img = T.new_img()
px = img.load()
fr = T.hx('#e6efe9')
frd = T.hx('#c2d4cf')
for i in range(16):
    for (x, y) in ((i, 0), (i, 15), (0, i), (15, i)):
        px[x, y] = T.P(fr)
for (x, y) in ((0, 0), (15, 0), (0, 15), (15, 15)):
    px[x, y] = T.P(frd)
streak = T.hx('#dff0ea')
for (x, y) in ((3, 3), (4, 4), (5, 5), (10, 2), (11, 3), (12, 4)):
    px[x, y] = T.P(streak, 200)
for (x, y) in ((2, 2), (6, 1), (12, 6)):
    px[x, y] = T.P(T.hx('#f6fbf8'), 160)
save(img, 'glass')

# bricks (warm clay, offset rows)
rng = random.Random('bricks')
img = T.new_img()
px = img.load()
mortar = T.hx('#c7b299')
brickcols = ['#a05f45', '#96553c', '#8c4d36', '#aa6a4e']
for y in range(16):
    for x in range(16):
        px[x, y] = T.P(T.shade(mortar, 1.0 + rng.uniform(-0.04, 0.04)))
for r in range(4):
    off = 0 if r % 2 == 0 else 4
    for bx in range(-1, 3):
        x0 = off + bx * 8
        bc = T.hx(brickcols[rng.randrange(4)])
        for y in range(r * 4, r * 4 + 3):
            for x in range(x0, x0 + 7):
                if x < 0 or x > 15:
                    continue
                c = bc
                rr = rng.random()
                if rr < 0.12:
                    c = T.shade(c, 0.90)
                elif rr < 0.24:
                    c = T.shade(c, 1.07)
                if y == r * 4:
                    c = T.shade(c, 1.06)
                elif y == r * 4 + 2:
                    c = T.shade(c, 0.93)
                px[x, y] = T.P(c)
save(img, 'bricks')

# bookshelf (planks frame + two shelves of warm book spines)
rng = random.Random('bookshelf')
img = planks(rng, dark=True)
px = img.load()
bg = T.hx('#2e2014')
spines = ['#8c4d36', '#a3703f', '#5f7a45', '#3f5a6e', '#b98d3f', '#6e4a6a', '#9c5a2e']
for y in list(range(2, 8)) + list(range(9, 14)):
    for x in range(1, 15):
        px[x, y] = T.P(bg)


def shelf(y0, y1):
    x = 1
    while x < 15:
        if rng.random() < 0.16:
            for y in range(y0, y1 + 1):
                px[x, y] = T.P(bg)
            x += 1
            continue
        w = max(1, min(rng.choice((1, 1, 2, 2, 3)), 15 - x))
        c = T.hx(spines[rng.randrange(len(spines))])
        for yy in range(y0, y1 + 1):
            for xx in range(x, x + w):
                cc = c
                if yy == y0:
                    cc = T.shade(c, 1.18)
                elif yy == y1:
                    cc = T.shade(c, 0.82)
                px[xx, yy] = T.P(cc)
        x += w


shelf(2, 7)
shelf(9, 13)
for x in range(16):
    px[x, 8] = T.P(T.shade(T.hx('#957040'), 0.9))
save(img, 'bookshelf')

# torch
img = T.new_img()
px = img.load()
h1 = T.hx('#8a5f36')
h2 = T.hx('#6e4a2a')
for y in range(6, 16):
    px[7, y] = T.P(h1)
    px[8, y] = T.P(h2)
for x in range(6, 10):
    px[x, 5] = T.P(T.hx('#5c4026'))
fl_o = T.hx('#d97a34')
fl_m = T.hx('#e89a3a')
fl_y = T.hx('#f2c23e')
fl_c = T.hx('#ffe9a0')
for x in range(6, 10):
    px[x, 4] = T.P(fl_o)
px[6, 3] = T.P(fl_m)
px[7, 3] = T.P(fl_y)
px[8, 3] = T.P(fl_y)
px[9, 3] = T.P(fl_o)
px[7, 2] = T.P(fl_c)
px[8, 2] = T.P(fl_y)
px[8, 1] = T.P(fl_m)
save(img, 'torch')

print("gen2 done: 8 textures")
