---
name: "lightboard"
description: "Make visuals in Pegah's Lightboard style (clean neon on black, like her Day 0 LinkedIn cover) for LinkedIn images, Instagram posts, Reels covers, YouTube thumbnails and slides. Use when she says Lightboard."
---

# Lightboard visuals

Look: pure black background, clean bold sans-serif type, thin neon outlines, a soft glow only where it earns attention. Calm and readable, not a sign shop. Reference: her "Day 0 · Hello LinkedIn / Learning AI Agents in Public" cover. Never third-party logos or brand marks.

## 1. Sizes

| Use | Size (px) |
| --- | --- |
| LinkedIn / Instagram post | 1080 × 1350 (4:5) |
| Reels cover / story frames | 1080 × 1920 (9:16) |
| YouTube thumbnail / video frame | 1920 × 1080 (16:9) |

Render at `device_scale_factor=2`.

## 2. Palette

```
background  #000000 (flat black)
--teal  #19e3d1   systems, agents, progress, highlights in body text
--pink  #ff4fa3   main headline, the problem, outer frames
--yel   #ffd166   the key phrase or number
--txt   #cbd5e1   normal text, secondary headline
--mut   #64748b   captions, labels, footer
border  #334155   pills, connector lines
white   #ffffff   the single most important word (e.g. LLM)
```

Use 2 to 3 accent colors per image, not all of them everywhere.

## 3. Glow (keep it subtle)

- One soft glow only: `filter: drop-shadow(0 0 5px currentColor)`.
- Apply it to: the main headline and outline shapes. Nothing else.
- Body text, labels, captions and footer: no glow at all.
- Never stack multiple drop-shadows; never glow small text.

## 4. Fonts

Install from npm (Google Fonts may be blocked in the sandbox):

```
npm install @fontsource/inter @fontsource/vazirmatn
```

- English: Inter 800 (headline), 700 (labels, sub-headline), 500 (body).
- Persian: Vazirmatn 800 / 500. Page `dir="rtl"`; wrap English words in a span with `unicode-bidi:isolate; direction:ltr`. Check every mixed line in the render.
- Labels and pills: uppercase, letter-spacing 0.04em to 0.3em.

## 5. Shapes

- Clean geometry: SVG `rect` with `rx` 20 to 34, `circle`, straight `line`. Stroke width 4 for outlines, 2 for connectors.
- Nesting (concentric rounded rectangles) to show layers; simple arrows for flows.
- Small reusable elements from the reference: a pill tag at the top (`border:2px solid #334155; border-radius:40px`, uppercase, wide letter-spacing, `--txt`), a progress row of dots (first filled teal, rest outlined) above the footer, and a simple outline robot icon when the topic is agents.

## 6. Composition (4:5)

1. Pill tag at top (series or topic, e.g. `DAY 3 · HARNESS`).
2. Headline: one line `--txt` + one line accent color with glow. Centered.
3. One diagram in the middle, with generous black space around it.
4. Takeaway line in white with the key phrase in `--yel`.
5. One or two lines of body text in `--txt` (her own example).
6. Progress dots + footer `PEGAH DAVARI · BACKEND & AGENTIC SYSTEMS` in `--mut`, uppercase, wide spacing.

Center-aligned by default. One idea per image.

## 7. Build and render

1. One HTML file: `@font-face` pointing to `node_modules/@fontsource/...`, absolute positioning, inline SVG.
2. Render with Playwright:

```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
    pg.goto("file:///path/to/post.html")
    pg.wait_for_timeout(900)
    pg.screenshot(path="lightboard.png")
    b.close()
```

3. Look at the PNG before sending. Fix: text crossing a border, labels wrapping inside boxes, mixed Persian/English in the wrong order, anything touching the edges. When editing the HTML, use a Python string replace on exact snippets rather than sed, so tags are not swallowed.
4. Send the PNG with a one-line caption. Post text goes inline in chat (rewind skill).

## 8. Bilingual

When she wants both languages, build two HTML files with the same layout (`-en` and `-fa`) and send both.

## 9. Video

For Reels or YouTube, render the same scene in steps (each step reveals one layer or label) at 9:16 or 16:9; the frames are narrated over.

## 10. Checks

- [ ] Flat black background, palette colors only
- [ ] Glow only on headline and outlines, soft
- [ ] Inter / Vazirmatn loaded, not a fallback font
- [ ] Nothing overlaps, wraps badly or crosses a border
- [ ] Facts match the sources