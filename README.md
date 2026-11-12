# Emberfield

A warm-rustic resource pack for Minecraft Java 26.3 / Horizon, built from scratch on the
`26.3.x-Template.zip` skeleton (pack_format 16). **Every texture is original programmatic
pixel art generated with Python + Pillow — zero copied vanilla art.**

## Theme

**Emberfield — hearth-lit rustic.** Honey-oak wood, warm hearth browns, ember-orange
accents, and soft warm stone. One shared palette discipline per material family: warm
grays for stone, honey tones for wood, muted olive-gold for grass, ember accents only
where things burn or shine (torch, furnace fire, gold). Noise style is smooth two-octave
value noise with light speckle; edges are hard (alpha 0/255 cutouts) everywhere except
glass, which keeps its semi-transparent streaks.

## Palette

| Family | Colors |
|---|---|
| Hearth browns (dirt/coarse dirt) | `#9a7148` `#8a5f3d` `#7d5437` `#6e4830` `#5e3c29` `#543726` |
| Honey oak (planks/log/tools) | `#c89a5b` `#b98d55` `#a97c48` `#9c7040` `#8a663a` `#6b4a2a` `#644626` |
| Warm stone | `#8f887c` `#837c70` `#777064` `#6b6459` `#5d574d` `#524c46` `#45413b` |
| Deepslate | `#54504b` `#4c4845` `#43403d` `#3a3734` `#322f2c` |
| Sand / gravel warmth | `#e2d3a4` `#d8c896` `#cdbc85` `#b7a770` |
| Grass fringe (olive-gold) | `#a3a94e` `#8f9440` `#6e7a30` |
| Clay bricks | `#a05f45` `#96553c` `#8c4d36` `#aa6a4e` mortar `#c7b299` |
| Ember accents (fire/torch/gold) | `#d97a34` `#e89a3a` `#f2c23e` `#f8dd7a` `#ffe9a0` |
| Iron | `#e8e4dc` `#d0cbc2` `#c9c4ba` `#a8a29a` `#968f84` |
| Diamond | `#aef0ea` `#7de0d8` `#4fb8ac` `#35918a` `#2f7a72` |
| Coal / bedrock darks | `#45423e` `#2e2c2a` `#262422` `#1e1c1a` `#151412` |

`grass_block_top` and `grass_block_side_overlay` are intentionally grayscale so the game's
biome tint colors them, exactly like vanilla convention.


## Verification against the template

All 4,192 model JSONs in the extracted template (`models/block` + `models/item`) were
scanned for texture references (2,169 distinct refs, including glass's
`{"sprite": ...}` form). **All 217 generated textures are referenced by at least one
template model/blockstate** (min 1, max 40 references each) and land at the exact paths
the models point to (singular `block/` / `item/` dirs, verified against the template's
own JSONs).

## What was intentionally skipped

The template references 2,169 textures in total; everything outside the drawn set falls
back to the template's placeholder art. After the rounds two and three (podzol/mycelium
caps and paths, farmland, sandstone and ice, andesite/diorite/granite, stone-brick
variants, deepslate bricks, obsidian, nether and end stones, birch/spruce/dark oak,
pumpkins/melons/hay, six wools, cobweb, TNT; then jungle/acacia/mangrove/cherry, the
deepslate ore set plus the four missing stone ores, fifteen colored terracottas,
quartz, ancient debris, netherite, magma, soul soil, basalt, blackstone, crimson and
warped stems) the drawn set
is 217 textures. Still skipped: the glazed-terracotta patterns, wool beyond the base colors, concrete,
netherite tools, chests (entity textures, different path scheme), and most
painting/particle/environment art. Quality over exhaustive coverage.

> Note: the template ships every vanilla texture as a 16x16 magenta/black placeholder
> checker, so anything not overridden above will show that placeholder in-game — that is
> the template's designed behavior, not a bug in this pack.

## Install

- **Horizon:** copy `dist/emberfield.zip` into `~/.local/share/horizon/resourcepacks/`
  (or the game's resourcepacks folder if it differs on your setup) and enable it in
  Options > Resource Packs.
- **Vanilla Minecraft:** copy `dist/emberfield.zip` into `.minecraft/resourcepacks/` and
  enable it in-game.

The zip is built from inside `pack/`, so `pack.mcmeta` sits at the zip root (verified
with `unzip -l`).

## Files

- `pack/` — full pack tree (template skeleton + this pack's art)
- `dist/emberfield.zip` — the distributable pack
- `preview/contact-sheet.png` — labeled contact sheet of every generated texture
- `scripts/` — the deterministic generation scripts (texlib + gen1..gen6)

## License / provenance

All art in this pack is original programmatic pixel art, generated from scratch by
scripts in `scripts/` using Python 3 + Pillow. No vanilla or third-party texture was
copied or traced. `pack.mcmeta` and the folder skeleton come from the provided template
and are kept byte-for-byte as shipped.
