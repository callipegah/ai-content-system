---
name: "radar-deep-dive"
description: "Go through the items the author ticked in their AI Radar doc: teach each one in Persian, step by step and tied to their work, then produce an English LinkedIn post with links, a Persian Instagram caption, and a Lightboard image. Use when she says go through the ticked ones, تیکخوردهها را برو, or deep dive."
---

# Radar deep dive

Step 2 of her content system: `ai-radar` makes the radar → she ticks items → this skill turns each ticked item into understanding first, then content. Uses `rewind` for text and `lightboard` for images.

It is interactive on purpose: her best posts came from back-and-forth corrections ("allowed" → "can do", adding guardrails, softening an absolute claim). Never run it as an unattended scheduled task.

## 1. Find the ticked items

1. She gives the radar doc link, or find the latest "AI Radar" doc in her artifact list.
2. Read the EN tabs with the docs tools and collect checked items. Ignore Persian tabs for ticks.
3. Reply with one line listing what you found (e.g. "A6, L3, V5") and start with the first. One item at a time.

## 2. Teach it (Persian, step by step)

Load the `learn` skill's approach. For each item:

1. Diagnose in one question if needed, otherwise start.
2. **One-sentence idea**, then a small table mapping the concept onto her own work: her LLM analytics agent at work (planner, tool layer, metric registry, deterministic protocol engine, judge, regression tests) or her side projects. This mapping is the most valuable part.
3. **Sources in order:** short read, video, repo she can try (quickstart command, and whether it needs an API key), paper.
4. **One question** that makes her think one step further. Wait for her answer.
5. When she understands it (explains it back, applies it), confirm in one line and move to content.

Explanation in Persian, technical terms in English, Persian direction rules from `rewind`.

## 3. Content for the item

After the teaching, produce inline in chat:

1. **LinkedIn post (English):** exactly the LinkedIn format in `rewind`: short scannable lines, tie to her analytics agent, hashtags, then the "If you want to go deeper" link block.
2. **Instagram caption (Persian):** 4 to 6 short lines, Rewind voice.
3. **Lightboard image:** 1080 × 1350, English for LinkedIn (Persian version only if she asks), built with `lightboard`. Look at the render before sending.

Then iterate on her corrections. When a technical claim is corrected, fix the image and the post together so they stay consistent.

## 4. Accuracy checks before handing over

- Every technical label is precise (e.g. "what it can do" for tools; "allowed" means permissions).
- An absolute claim is fine as a hook, but the body acknowledges the exception.
- A simplified diagram gets one honest line ("in a real system these are components, not neat rings").
- Her work example uses no internal names, metric names or numbers.
- All links opened and real.

## 5. Finish

One line on what is ready for this item, then move to the next ticked item. Suggest a fresh chat after 2 to 3 items to keep it light.