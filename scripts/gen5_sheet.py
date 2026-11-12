"""Emberfield contact sheet: labeled grid of every generated texture + pack icon."""
from math import ceil
from PIL import Image, ImageDraw, ImageFont

ROOT = "/home/hakergeniusz/Projects/emberfield"
TEXROOT = ROOT + "/pack/assets/minecraft/textures"

names = sorted(set(open(ROOT + "/scripts/manifest.txt").read().split()))
cols = 8
cell_w, cell_h = 150, 94
tex = 64

rows = ceil((len(names) + 1) / cols)  # +1 cell for pack.png
img = Image.new('RGB', (cols * cell_w, rows * cell_h), (36, 31, 28))
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSans.ttf', 11)
except Exception:
    try:
        font = ImageFont.load_default(size=11)
    except Exception:
        font = ImageFont.load_default()


def cell_bg(cx, cy):
    for yy in range(0, tex, 8):
        for xx in range(0, tex, 8):
            c = (72, 66, 61) if ((xx // 8 + yy // 8) % 2) else (54, 49, 45)
            d.rectangle([cx + xx + 6, cy + yy + 4, cx + xx + 13, cy + yy + 11], fill=c)


allcells = names + ["PACK_ICON"]
for i, name in enumerate(allcells):
    cx = (i % cols) * cell_w
    cy = (i // cols) * cell_h
    cell_bg(cx, cy)
    if name == "PACK_ICON":
        sub = Image.open(ROOT + "/pack/pack.png").convert('RGBA').resize((tex, tex), Image.NEAREST)
        label = "pack.png (128)"
    else:
        sub = Image.open(TEXROOT + "/" + name + ".png").convert('RGBA').resize((tex, tex), Image.NEAREST)
        label = name.split('/')[1] + "  [" + name[0] + "]"
    img.paste(sub, (cx + 6, cy + 4), sub)
    d.text((cx + 6, cy + tex + 8), label, fill=(232, 222, 200), font=font)
    d.rectangle([cx, cy, cx + cell_w - 1, cy + cell_h - 1], outline=(58, 52, 48))

out = ROOT + "/preview/contact-sheet.png"
img.save(out)
print("contact sheet:", out, img.size, "cells:", len(allcells))
