---
name: "lightboard-diagram"
description: "Animated ByteByteGo-style explainer diagram in Pegah's Lightboard look: one full 4:5 diagram with numbered flow steps and moving dashed arrows, exported as an autoplaying GIF for LinkedIn."
---

# Lightboard diagram (animated GIF)

One complete diagram, visible all at once, where only the dashed connectors move ("marching ants"). It autoplays in the LinkedIn feed as an image, with no play button. Look = Lightboard (black, neon outlines, subtle glow). Structure = a ByteByteGo-style explainer: numbered steps on arrows, boxed sections, a takeaway line. Never use ByteByteGo's or any third-party logo, name or wordmark.

Reference output: "TOKENS · EP. 01 / 5-hour limit reached" (top: what every message sends; bottom: 9 tips in a 3×3 grid).

## 1. Before building

1. Collect the content: a title, one flow (4 to 6 numbered steps), and optionally a grid of 6 to 9 tips. Check every claim against its source (Rewind rules: no internal names, metric names or numbers from her work).
2. If the title quotes a real UI message (an error or limit text), copy the exact wording from the official help page and cite it.
3. If the post text is needed too, write it with the `rewind` skill (LinkedIn format), so text and image say the same things.

## 2. Canvas and palette

- 1080 × 1350 px (4:5), the size LinkedIn shows full-width in the feed. For a 9:16 Reel/Short of the same content, make a separate scene-by-scene video instead.
- Palette from `lightboard`: background `#000000`; teal `#19e3d1` (flow, section 1, steps); pink `#ff4fa3` (title, problem, section 2, the "expensive" step); yellow `#ffd166` (the key item and the takeaway phrase); text `#cbd5e1`; muted `#64748b`; borders `#334155`; white for bold labels.
- Glow: `filter: drop-shadow(0 0 4-5px currentColor)` only on the title and on section/box outlines. Never on body text, labels or small text.
- Font: Inter 500 / 700 / 800 via `npm install @fontsource/inter` (Google Fonts may be blocked). Point `@font-face` at `node_modules/@fontsource/inter/files/inter-latin-{500,700,800}-normal.woff2`.

## 3. Layout (top to bottom)

1. **Pill tag** at the top: series + episode, e.g. `TOKENS · EP. 01` (2px `#334155` border, radius 40px, uppercase, letter-spacing ~0.22em).
2. **Title**: one line, 56 to 64px, weight 800, pink with glow. **Subtitle** below: one line, 24 to 26px, `--txt`.
3. **Section 1: the flow.** A rounded frame (rx 30, 3px teal stroke, soft glow) with a small uppercase label in the top-left (e.g. `WHAT EVERY MESSAGE SENDS`).
   - Nodes: rounded boxes (2px stroke, rx 20, near-black fill such as `#06100f`), white bold text 26px, an optional muted sub-label. Use a simple outline icon (circle head + shoulders) for "User".
   - One highlighted container (pink outline) for the key concept, holding stacked pill rows (`text` left, small uppercase tag right, e.g. `GROWS`, `STAY`). The most important row gets a yellow outline.
   - Connectors: SVG `line`/`polyline`, stroke 2.5, `stroke-dasharray="12 8"`, open chevron arrowheads via `<marker>`. Use pink for the costly or critical path and `#cbd5e1` for the rest.
   - Step labels: filled circles (34px, teal; pink for the critical step; black number, weight 800) next to a short label, 18 to 20px.
   - Close the section with one bold takeaway line: white with the key phrase in yellow.
4. **Section 2: the grid** (optional). A pink-outlined frame with a label (e.g. `HOW NOT TO HIT IT`). 3 columns × up to 3 rows of cards (320 × 112, 2px `#334155`, rx 20). Each card: number circle + bold title (22px white) + one short sub-line (17px). Colour-code the groups (teal numbers for group A, yellow for group B).
5. **Footer**: `PEGAH DAVARI · BACKEND & AGENTIC SYSTEMS`, 15px, `--mut`, uppercase, letter-spacing 0.3em.

Keep 40+ px margins and generous black space. One idea per diagram. Text must fit in one line per pill; shorten the tag rather than wrap.

## 4. Animation

Only the connectors move. Put every dashed connector in one `<g class="flow">` and expose a frame setter:

```html
<script>
const g = document.querySelector('.flow');
window.setF = (f, N) => g.setAttribute('stroke-dashoffset', String(-20 * f / N)); // 20 = dash period (12+8)
setF(0, 1);
</script>
```

A full dash period per loop makes the GIF loop seamlessly. Nothing else animates: no fades, no scene changes.

## 5. Render and export

```python
from playwright.sync_api import sync_playwright
N = 20
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto("file:///ABS/PATH/diagram.html"); pg.wait_for_timeout(800)
    for f in range(N):
        pg.evaluate(f"setF({f},{N})")
        pg.screenshot(path=f"gf/g{f:03d}.png")
    b.close()
```

```bash
ffmpeg -y -framerate 20 -i gf/g%03d.png -vf "palettegen=max_colors=64:stats_mode=full" pal.png
ffmpeg -y -framerate 20 -i gf/g%03d.png -i pal.png -lavfi "paletteuse=dither=none" -loop 0 diagram.gif
```

Expected size is roughly 100 to 300 KB, because the background is flat black and only the lines change.

## 6. Check before sending

Open frame 0 as an image and look at it:
- [ ] No text wraps inside a pill or card, and nothing crosses a border or touches the edges
- [ ] Arrows start and end at box edges, step numbers sit next to their own arrow, and labels don't overlap lines
- [ ] Glow only on the title and outlines, soft; palette colours only
- [ ] Inter loaded (not a fallback font)
- [ ] Facts and quoted UI text match the sources

Fix layout with exact Python string replacements in the HTML, re-render, and check again.

## 7. Deliver

- Send the GIF with a one-line caption.
- Tell her to upload it on LinkedIn with **Photo**, not Video, so it autoplays as an image.
- If a post text is needed, give it inline in chat, written with `rewind`, with the same points as the diagram.
- A Persian version of the diagram only if she asks; then follow the Persian direction rules from `rewind`/`lightboard` (Vazirmatn font, `dir="rtl"`, English terms isolated).