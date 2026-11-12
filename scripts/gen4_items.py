"""Emberfield gen 4: item textures (17) + 128x128 pack.png icon."""
import math
import random
from PIL import Image
import texlib as T

OUTI = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/item"
OUTP = "/home/hakergeniusz/Projects/emberfield/pack/pack.png"
MAN = "/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt"


def savei(img, name):
    img.save(OUTI + "/" + name + ".png")
    with open(MAN, "a") as f:
        f.write("item/" + name + "\n")
    print("wrote item/" + name)


def put(px, x, y, c, a=255):
    if 0 <= x <= 15 and 0 <= y <= 15:
        px[x, y] = T.P(c, a)


def pickaxe(head, handle=('#8a5f36', '#6e4a2a')):
    img = T.new_img()
    px = img.load()
    hl, hm, hd = [T.hx(c) for c in head]
    hh, hd2 = T.hx(handle[0]), T.hx(handle[1])
    for t in range(10):
        put(px, 10 - t, 3 + t, hh)
        put(px, 10 - t, 4 + t, hd2)
    put(px, 0, 13, hd2)
    put(px, 0, 14, hh)
    for y in range(16):
        for x in range(16):
            d = math.hypot(x - 7.5, y - 9.5)
            if 6.6 <= d <= 9.6 and y <= 8:
                if d >= 9.0:
                    c = hd
                elif y <= 3:
                    c = hl
                else:
                    c = hm
                px[x, y] = T.P(c)
    return img


def sword(blade, guard='#4a3423', handle=('#8a5f36', '#6e4a2a')):
    img = T.new_img()
    px = img.load()
    bl, bm, bd = [T.hx(c) for c in blade]
    g = T.hx(guard)
    h1, h2 = T.hx(handle[0]), T.hx(handle[1])
    for t in range(10):
        put(px, 4 + t, 11 - t, bm)
        put(px, 5 + t, 11 - t, bl)
        put(px, 4 + t, 12 - t, bd)
    put(px, 14, 1, bm)
    for (x, y) in ((2, 9), (3, 10), (2, 10), (3, 9), (5, 12), (6, 13), (5, 13), (6, 12)):
        put(px, x, y, g)
    for s in range(3):
        put(px, 3 - s, 12 + s, h1)
        put(px, 2 - s, 12 + s, h2)
    put(px, 0, 15, h2)
    return img


MATS = {
    'wooden': ('#c89a5b', '#a97c48', '#7d5a36'),
    'stone': ('#9a9288', '#7e766c', '#5f5952'),
    'iron': ('#e8e4dc', '#c9c4ba', '#968f84'),
    'golden': ('#fbe98e', '#f2c94c', '#c99f2f'),
    'diamond': ('#8ef0e0', '#5cc9bb', '#35918a'),
}
for mat in ('wooden', 'stone', 'iron', 'golden', 'diamond'):
    savei(pickaxe(MATS[mat]), mat + '_pickaxe')
    savei(sword(MATS[mat]), mat + '_sword')

# stick
img = T.new_img()
px = img.load()
for t in range(10):
    put(px, 3 + t, 12 - t, T.hx('#8a5f36'))
    put(px, 4 + t, 12 - t, T.hx('#a97c48'))
    put(px, 3 + t, 13 - t, T.hx('#6e4a2a'))
put(px, 13, 2, T.hx('#a97c48'))
savei(img, 'stick')

# apple
img = T.new_img()
px = img.load()
mid = T.hx('#b83a2a')
lit = T.hx('#d95a3f')
drk = T.hx('#8a2a1e')
for y in range(16):
    for x in range(16):
        d = math.hypot(x - 7.5, y - 8.7)
        if d <= 4.8:
            if y < 6 and abs(x - 7.5) < 1.7:
                continue
            proj = (x - 7.5) + (y - 8.7)
            if proj > 2.6:
                c = drk
            elif d < 3.4 and proj < -2.2:
                c = lit
            else:
                c = mid
            px[x, y] = T.P(c)
px[5, 6] = T.P(T.hx('#f2d0b0'))
px[6, 5] = T.P(T.hx('#f2d0b0'))
for y in (2, 3, 4):
    px[8, y] = T.P(T.hx('#6e4a2a'))
px[9, 2] = T.P(T.hx('#5f7a45'))
px[10, 2] = T.P(T.hx('#5f7a45'))
px[10, 3] = T.P(T.hx('#4f6a38'))
savei(img, 'apple')

# bread
img = T.new_img()
px = img.load()
tl = T.hx('#e0b268')
tm = T.hx('#c9974a')
td = T.hx('#9c6a30')
sc = T.hx('#a87c3c')
for t in range(10):
    put(px, 2 + t, 10 - t, tl)
    put(px, 2 + t, 11 - t, tm)
    put(px, 2 + t, 12 - t, td)
put(px, 1, 10, tl)
put(px, 1, 11, tm)
put(px, 1, 12, td)
put(px, 12, 1, tl)
put(px, 12, 2, tm)
put(px, 12, 3, td)
for (x, y) in ((5, 7), (5, 8), (5, 9), (8, 4), (8, 5), (8, 6)):
    put(px, x, y, sc)
savei(img, 'bread')


# ingots
def ingot(l, m, d):
    img = T.new_img()
    px = img.load()
    lc, mc, dc = T.hx(l), T.hx(m), T.hx(d)
    spans = [(4, 6, 9), (5, 4, 12), (6, 3, 13), (7, 2, 13), (8, 2, 13),
             (9, 2, 13), (10, 2, 13), (11, 4, 11)]
    for (y, x0, x1) in spans:
        for x in range(x0, x1 + 1):
            if y <= 7:
                c = lc
            elif y <= 9:
                c = mc
            else:
                c = dc
            px[x, y] = T.P(c)
    for y in range(8, 10):
        px[2, y] = T.P(T.shade(mc, 1.06))
        px[13, y] = T.P(T.shade(mc, 0.90))
    return img


savei(ingot('#e8e4dc', '#c9c4ba', '#968f84'), 'iron_ingot')
savei(ingot('#fbe98e', '#f2c94c', '#c99f2f'), 'gold_ingot')

# diamond gem
img = T.new_img()
px = img.load()
dl = T.hx('#aef0ea')
dm = T.hx('#7de0d8')
dd = T.hx('#4fb8ac')
ddeep = T.hx('#2f7a72')
rows = {3: (6, 9), 4: (5, 10), 5: (4, 11), 6: (3, 12), 7: (3, 12), 8: (4, 11),
        9: (5, 10), 10: (6, 9), 11: (7, 8)}
for y, (x0, x1) in rows.items():
    c = dl if y <= 4 else (dm if y <= 7 else (dd if y <= 10 else ddeep))
    for x in range(x0, x1 + 1):
        cc = c
        if y >= 5 and (x == x0 or x == x1):
            cc = T.shade(c, 0.88)
        px[x, y] = T.P(cc)
px[6, 6] = T.P(T.hx('#e8fffb'))
px[7, 6] = T.P(T.hx('#e8fffb'))
savei(img, 'diamond')

# coal lump
rng = random.Random('coal_item')
img = T.new_img()
mask = T.blob_mask(rng, [(6, 7, 2.3), (9, 9, 2.0), (7, 11, 1.7)])
T.paint_blob(img, mask, ('#151412', '#262422', '#2e2c2a', '#45423e'), rng)
savei(img, 'coal')


# ---- pack.png (128x128, drawn at 32x32 and upscaled x4) ----
def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


c0 = T.hx('#2b2030')
c1 = T.hx('#7a3f2a')
c2 = T.hx('#e09040')
icon = Image.new('RGBA', (32, 32))
ip = icon.load()
for y in range(32):
    if y <= 21:
        t = y / 21.0
        base = lerp(c0, c1, t / 0.62) if t < 0.62 else lerp(c1, c2, (t - 0.62) / 0.38)
        for x in range(32):
            ip[x, y] = T.P(base)
for (x, y) in ((4, 3), (9, 6), (14, 2), (26, 4), (18, 5), (6, 9)):
    ip[x, y] = T.P(T.hx('#e8d8b0'))
for y in range(32):
    for x in range(32):
        d = math.hypot(x - 22.5, y - 9.5)
        if d <= 2.5:
            ip[x, y] = T.P(T.hx('#fff2c0'))
        elif d <= 4.5:
            ip[x, y] = T.P(T.hx('#f8dd7a'))
# oak silhouette
for y in range(14, 23):
    ip[13, y] = T.P(T.hx('#241a10'))
    ip[14, y] = T.P(T.hx('#241a10'))
for y in range(32):
    for x in range(32):
        d = math.hypot(x - 13.5, y - 10.5)
        if d <= 3.4:
            ip[x, y] = T.P(T.hx('#3e2c1c'))
        elif d <= 5.2:
            ip[x, y] = T.P(T.hx('#33241a'))
# far hills
for x in range(32):
    yh = round(18 + 2.2 * math.sin(x / 5.2) + 1.6 * math.sin(x / 2.1 + 1.3))
    for y in range(yh, 23):
        ip[x, y] = T.P(T.shade(T.hx('#5a3a26'), 1.0 + (0.04 if x % 3 else -0.03)))
# near ground
for y in range(23, 32):
    for x in range(32):
        ip[x, y] = T.P(T.hx('#3a2a1e'))
for x in range(32):
    ip[x, 23] = T.P(T.hx('#6b4a2a'))
for x in range(32):
    if (x * 7) % 5 < 2:
        ip[x, 22] = T.P(T.hx('#6b5a2e'))
icon = icon.resize((128, 128), Image.NEAREST)
icon.save(OUTP)
print("wrote pack.png (128x128)")

print("gen4 done: 17 items + pack icon")
