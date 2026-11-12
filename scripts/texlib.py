"""Shared helpers for Emberfield pack texture generation (Pillow, 16x16 RGBA)."""
import math
from PIL import Image


def hx(s):
    """'#rrggbb' -> (r, g, b)"""
    s = s.lstrip('#')
    return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))


def P(c, a=255):
    return (c[0], c[1], c[2], a)


def shade(c, f):
    return (max(0, min(255, round(c[0] * f))),
            max(0, min(255, round(c[1] * f))),
            max(0, min(255, round(c[2] * f))))


def new_img():
    return Image.new('RGBA', (16, 16), (0, 0, 0, 0))


def smooth_noise(w, h, cell, rng):
    """Tileable-ish smooth value noise in [0,1] on a w*h grid."""
    gw, gh = w // cell + 2, h // cell + 2
    g = [[rng.random() for _ in range(gw)] for _ in range(gh)]
    out = [[0.0] * w for _ in range(h)]
    for y in range(h):
        fy = y / cell
        y0 = int(fy)
        ty = fy - y0
        ty = ty * ty * (3 - 2 * ty)
        r0 = g[y0]
        r1 = g[y0 + 1]
        for x in range(w):
            fx = x / cell
            x0 = int(fx)
            tx = fx - x0
            tx = tx * tx * (3 - 2 * tx)
            a = r0[x0] * (1 - tx) + r0[x0 + 1] * tx
            b = r1[x0] * (1 - tx) + r1[x0 + 1] * tx
            out[y][x] = a * (1 - ty) + b * ty
    return out


def fbm(rng, cells=(4, 2), weights=(0.65, 0.35), w=16, h=16):
    acc = [[0.0] * w for _ in range(h)]
    for cell, wt in zip(cells, weights):
        n = smooth_noise(w, h, cell, rng)
        for y in range(h):
            row = n[y]
            arow = acc[y]
            for x in range(w):
                arow[x] += row[x] * wt
    lo = min(min(r) for r in acc)
    hi = max(max(r) for r in acc)
    span = (hi - lo) or 1.0
    for y in range(h):
        for x in range(w):
            acc[y][x] = (acc[y][x] - lo) / span
    return acc


def quant(noise, stops):
    """stops: ascending [(threshold, '#hex'), ...]; v < threshold -> color."""
    img = new_img()
    px = img.load()
    cols = [(t, hx(c)) for (t, c) in stops]
    for y in range(16):
        for x in range(16):
            v = noise[y][x]
            c = cols[-1][1]
            for (t, col) in cols:
                if v < t:
                    c = col
                    break
            px[x, y] = P(c)
    return img


def ramp(noise, colors, rng=None, jitter=0.0):
    """Map noise [0,1] onto an ordered color band with optional speckle jitter."""
    img = new_img()
    px = img.load()
    cols = [hx(c) for c in colors]
    n = len(cols)
    for y in range(16):
        row = noise[y]
        for x in range(16):
            v = row[x]
            if rng is not None and jitter:
                v += rng.uniform(-jitter, jitter)
            i = int(v * n)
            if i < 0:
                i = 0
            elif i >= n:
                i = n - 1
            c = cols[i]
            px[x, y] = P(c)
    return img


def wd(a, b, size=16):
    """Wrapped axis distance (for tileable patterns)."""
    d = abs(a - b) % size
    return min(d, size - d)


def voronoi(rng, nseeds, colors, mortar, edge=1.1, jitter=0.08):
    """Wrapped voronoi cells (cobbles, gravel)."""
    img = new_img()
    px = img.load()
    cols = [hx(c) for c in colors]
    mc = hx(mortar)
    pts = [(rng.uniform(0, 16), rng.uniform(0, 16), rng.randrange(len(cols)))
           for _ in range(nseeds)]
    for y in range(16):
        for x in range(16):
            best = []
            for (sx, sy, ci) in pts:
                dx = wd(x, sx)
                dy = wd(y, sy)
                best.append((math.hypot(dx, dy), ci))
            best.sort(key=lambda t: t[0])
            d1, c1 = best[0]
            d2 = best[1][0]
            if d2 - d1 < edge:
                c = mc
            else:
                c = cols[c1]
                if rng.random() < 0.4:
                    c = shade(c, 1.0 + rng.uniform(-jitter, jitter))
            px[x, y] = P(c)
    return img


def blob_mask(rng, specs):
    """specs: [(cx, cy, radius), ...] -> bool mask with ragged wrapped blobs."""
    mask = [[False] * 16 for _ in range(16)]
    for (cx, cy, r) in specs:
        for y in range(16):
            for x in range(16):
                d = math.hypot(wd(x, cx), wd(y, cy))
                if d <= r - 0.35 + rng.random() * 0.7:
                    mask[y][x] = True
    return mask


def paint_blob(img, mask, palette, rng):
    """palette: (outline, dark, mid, light)"""
    px = img.load()
    oc, dc, mc, lc = [hx(c) for c in palette]

    def m(x, y):
        if 0 <= x <= 15 and 0 <= y <= 15:
            return mask[y][x]
        return False

    for y in range(16):
        for x in range(16):
            if not mask[y][x]:
                continue
            if (not m(x + 1, y)) or (not m(x - 1, y)) or (not m(x, y + 1)) or (not m(x, y - 1)):
                c = oc
            else:
                r = rng.random()
                if r < 0.28:
                    c = lc
                elif r < 0.50:
                    c = dc
                else:
                    c = mc
            px[x, y] = P(c)
