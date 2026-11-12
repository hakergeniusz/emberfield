"""Verify Emberfield textures: referenced by template models? correct size? (stdlib+PIL only)"""
import json
import os
from PIL import Image

ROOT = "/home/hakergeniusz/Projects/emberfield/pack/assets/minecraft"
gen = set()
with open("/home/hakergeniusz/Projects/emberfield/scripts/manifest.txt") as f:
    for line in f.read().split():
        gen.add(line)

texrefs = {}


def norm(v):
    return v[10:] if v.startswith("minecraft:") else v


def collect(obj, path):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "textures" and isinstance(v, dict):
                for tv in v.values():
                    if isinstance(tv, str) and not tv.startswith("#"):
                        texrefs.setdefault(norm(tv), set()).add(path)
                    elif isinstance(tv, dict) and isinstance(tv.get("sprite"), str):
                        texrefs.setdefault(norm(tv["sprite"]), set()).add(path)
            collect(v, path)
    elif isinstance(obj, list):
        for it in obj:
            collect(it, path)


nmod = 0
for sub in ("block", "item"):
    sd = ROOT + "/models/" + sub
    for fn in sorted(os.listdir(sd)):
        if not fn.endswith(".json"):
            continue
        p = sd + "/" + fn
        nmod += 1
        with open(p) as f:
            collect(json.load(f), p)

covered = [g for g in sorted(gen) if g in texrefs]
not_referenced = [g for g in sorted(gen) if g not in texrefs]
uncovered_refs = [t for t in sorted(texrefs) if t not in gen]

print("model files scanned:", nmod)
print("distinct texture refs in models:", len(texrefs))
print("generated:", len(gen), "| referenced:", len(covered), "| NOT referenced:", not_referenced)

# refcount per generated texture (min/avg for reporting)
counts = [len(texrefs[g]) for g in covered]
print("refs per texture: min", min(counts), "max", max(counts))

# sanity: all 16x16 RGBA on disk, alpha conventions for opaque blocks
bad = []
for g in sorted(gen):
    im = Image.open(ROOT + "/textures/" + g + ".png")
    if im.size != (16, 16):
        bad.append((g, im.size, im.mode))
print("bad size/mode:", bad)

# transparency check: leaves/glass must have transparent px, opaque blocks must not
for g in covered:
    im = Image.open(ROOT + "/textures/" + g + ".png").convert("RGBA")
    alphas = set(px[3] for px in im.get_flattened_data()) if hasattr(im, "get_flattened_data") else set(p[3] for p in im.getdata())
    has_t = 0 in alphas
    half = any(0 < a < 255 for a in alphas)
    if g in ("block/oak_leaves", "block/glass", "block/torch", "block/grass_block_side_overlay"):
        if not has_t:
            print("WARN expected transparency but none:", g)
    elif has_t:
        print("WARN unexpected transparency:", g)
    if half and g not in ("block/glass",):
        print("WARN half-alpha on hard-edged art:", g)

with open("/home/hakergeniusz/Projects/emberfield/scripts/uncovered_refs.txt", "w") as f:
    f.write("\n".join(uncovered_refs))
print("uncovered refs (template textures I did not draw):", len(uncovered_refs),
      "-> scripts/uncovered_refs.txt")
print("VERIFY DONE")
