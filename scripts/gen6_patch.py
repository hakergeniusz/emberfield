"""Emberfield patch: solidify item/coal lump, thicken item/bread loaf."""
import random
import texlib as T

OUTI = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft/textures/item"


def put(px, x, y, c):
    if 0 <= x <= 15 and 0 <= y <= 15:
        px[x, y] = T.P(c)


# coal: merged chunky lump
rng = random.Random('coal_item_v2')
img = T.new_img()
mask = T.blob_mask(rng, [(6.5, 7.5, 2.7), (9, 8.5, 2.6), (7.5, 10.5, 2.3), (9.5, 5.5, 1.9)])
T.paint_blob(img, mask, ('#151412', '#262422', '#2e2c2a', '#45423e'), rng)
img.save(OUTI + "/coal.png")
print("patched coal")

# bread: 4px-thick loaf
img = T.new_img()
px = img.load()
tl = T.hx('#e0b268')
tm = T.hx('#c9974a')
td = T.hx('#9c6a30')
sc = T.hx('#a87c3c')
for t in range(10):
    put(px, 2 + t, 9 - t, tl)
    put(px, 2 + t, 10 - t, tm)
    put(px, 2 + t, 11 - t, tm)
    put(px, 2 + t, 12 - t, td)
for (x, y, c) in ((1, 9, tl), (1, 10, tm), (1, 11, tm), (1, 12, td),
                  (12, 1, tl), (12, 2, tm), (12, 3, tm), (12, 4, td)):
    put(px, x, y, c)
for (x, y) in ((5, 6), (5, 7), (5, 8), (8, 3), (8, 4), (8, 5)):
    put(px, x, y, sc)
img.save(OUTI + "/bread.png")
print("patched bread")
