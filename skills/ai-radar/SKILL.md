---
name: "ai-radar"
description: "Build the author's AI Radar: search a fixed list of sources for recent AI, agents, backend, AI video/image, health tech, psychology and startup news plus 3-month durable lessons, compile numbered items with tick boxes, repos, videos and links as a bilingual (English and Persian) Claude Doc."
---

# AI Radar

The radar is the input of the author's content system:
Radar (English + Persian, every 3 days) → she ticks items in the doc → she says "go through the ticked ones" in a new chat → the `radar-deep-dive` skill teaches each ticked item and produces posts and images (with `rewind` and `lightboard`).

The radar has two jobs: what is new (trends) and what is worth learning (durable lessons). Never only trends.

## 1. Windows

- **Trends (A, V, H):** since the last radar (usually 3 days). First run or on request: last month.
- **Lessons (L):** the last 3 months, because good teaching posts stay useful.
- **Fundamentals (F):** no window; an evergreen backlog carried from run to run (drop items she already deep-dived).
- State the windows in the doc title and section leads.

## 2. Fixed sources (search these first)

News:
- Latent Space / AINews: https://www.latent.space/feed
- Simon Willison: https://simonwillison.net/
- Hugging Face trending papers: https://huggingface.co/papers/trending
- Artificial Analysis: https://artificialanalysis.ai/
- AI release tracker: https://www.nocode.mba/ai-release-tracker/ (current year/month)

Lessons and fundamentals (backend + AI engineering):
- Ahead of AI, Sebastian Raschka: https://magazine.sebastianraschka.com/feed
- Anthropic Engineering: https://www.anthropic.com/engineering
- ByteByteGo: https://blog.bytebytego.com/archive
- InfoQ architecture and distributed systems: https://www.infoq.com/architecture/articles/
- MCP blog: https://blog.modelcontextprotocol.io/
- Simon Willison guides: https://simonwillison.net/guides/
- roadmap.sh AI Engineer: https://roadmap.sh/ai-engineer

Health tech, psychology, startups (H) — starting list, confirm quality on the first run and keep the good ones:
- Health tech: STAT News (statnews.com), Rock Health (rockhealth.com)
- Psychology: PsyPost (psypost.org), APA Monitor (apa.org/monitor)
- Startups and builders: Y Combinator Launches (ycombinator.com/launches), Show HN on Hacker News, Product Hunt, TechCrunch

YouTube channels: AI Engineer, AI Explained, ByteByteGo, Fireship, AI Jason, Hussein Nasser (backend); Matt Wolfe, Curious Refuge, Theoretically Media (video/image).
GitHub trackers: GitHub Trending, OSS Insight, Trendshift (use star growth in the window, not total stars).
X accounts: @_akhaliq, @karpathy, @simonw, @swyx, @minchoi.

Substack homepages need JavaScript; fetch the `/feed` URL. Feeds can be very large: prefer WebSearch restricted to the domain (`allowed_domains`) when you only need titles and dates. If the previous radar doc has a "Fixed sources" table she edited, follow her version.

## 3. Find links per item

- **Video:** WebSearch with `allowed_domains: ["youtube.com"]`; prefer a channel from the fixed list, then a clear explainer or hands-on test. Never invent a URL.
- **Repo:** GitHub or Hugging Face link from the paper page or official post.
- **News / source:** the original post you actually opened.

## 4. Sections and numbering

- **A. AI & Agents trends** (A1 ...): 8 to 10 items for a month, 4 to 6 for 3 days. Include 1 to 2 items not on her known topic list, marked "(new for you)".
- **F. Fundamentals backlog** (F1 ...): table of evergreen concepts: concept, one line, learn-from video, read/repo.
- **L. Lessons from the last 3 months** (L1 ...): 6 to 10 posts that TEACH a durable backend or AI-engineering lesson. Table: lesson as a one-line rule, area, why it sticks, source. Only posts whose date you confirmed inside the window. Each is a candidate YouTube tutorial.
- **V. AI Video, Image & Editing** (V1 ...): 5 to 7 items; note relevance to her YouTube vlog, AI dubbing and Reels pipeline.
- **H. Health tech, Psychology & Startups** (H1 ...): 5 to 7 items: new research, products, and interesting builders whose project could spark an idea for her. "Why it matters" says what idea it gives her.

## 5. Item format (A, V, H) with tick boxes

```
### A1. <short title>
- [ ] Deep dive this
- Hook: the curiosity moment, one or two lines
- What happened: facts, numbers, dates
- Why it matters: ideally tied to their work (LLM analytics agent at work, skill/tool layers, Reels pipeline, AI twin, side projects)
- Deep-dive keyword: terms she can search
- Repo / Video / News: links
```

The `- [ ] Deep dive this` line is a real checkbox she ticks in the doc. For the F and L tables, add a checklist right under each table, one per row: `- [ ] F1 <concept>`.

Tick boxes live only in the EN tabs; the Persian tabs mirror the same numbers, so ticking once in English is enough. Say this in one line at the top of each Persian tab.

## 6. Output: bilingual Claude Doc

Create a Claude Doc (load the docs skill and follow the docs connector instructions) named `AI Radar — <window>`, with six tabs:
1. `EN · AI & Agents` (how-to-use line + A + F + L + Fixed sources table)
2. `EN · AI Video, Image & Editing` (V)
3. `EN · Health, Psychology & Startups` (H)
4. `FA · AI و ایجنت‌ها` (A + F + L)
5. `FA · ویدیو، عکس و ادیت` (V)
6. `FA · سلامت، روان‌شناسی و استارتاپ` (H)

How-to-use line (top of EN tab 1): "Tick the items you want, then open a new chat and say: go through the ticked ones in <this doc link>."

Persian tabs are natural Persian (not literal translation), technical terms kept in English, same numbering and links. Dates in Persian tabs use the Persian calendar.

### Persian text direction (mandatory)

Persian lines that contain English words get their word order scrambled when shown left-to-right. In every Persian tab:
- Wrap the content of every heading, paragraph, list item and table cell as: `U+200F` (RLM) + `U+2067` (RLI) + text + `U+2069` (PDI). Write them as the actual characters in the markdown you send.
- Prefer starting each line with a Persian word («مدل Gemini 4» not «Gemini 4 مدل»).
- Join two English terms with «و», not «،».
- Link text inside Persian lines: prefer Persian words.

In chat (or a scheduled run's message): one short line with the doc link and the reminder to tick items.

## 7. Verification rules

- Only state facts from pages you opened. A search snippet is not a source.
- Single-tweet or rumored claims: label "reportedly" or leave out.
- Health and psychology items: state research limits (sample, preprint vs peer-reviewed); no medical advice.
- Claims carried over from earlier sessions are re-checked before they go into the radar.

## 8. Deep dives

Deep dives do not happen in the radar run. They happen in a separate chat with the `radar-deep-dive` skill, after she ticks items.

## 9. Keep it lean

This work is token heavy. Fetch only what each item needs and keep chat replies to a line or two; the content lives in the doc.