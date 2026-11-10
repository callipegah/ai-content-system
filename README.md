# Learning AI in public: a content system built with Claude

I'm a backend and data engineer working on LLM-powered analytics. AI moves fast, and I didn't want to fall behind or only read headlines. So I built a small system that does three things:

1. **Finds** what's worth knowing (a Radar of trends, papers and repos).
2. **Teaches** it to me, one layer at a time, until I really get it.
3. **Turns** what I learned into posts and videos in my own voice and look.

This repo is that system: the skills, the visuals, and the scripts behind them. It's a work in progress and public on purpose.

## How it started

It began as a need, not a plan. I wanted to stay current on AI without drowning in links. Then I kept wanting to explain what I'd learned, and every explanation needed the same things: a voice that sounds like me, a consistent look, and a repeatable way to turn notes into a post or a video.

Each time I did something twice, it became a skill.

## The pipeline

```
Radar  →  pick what interests me  →  Deep dive (Rewind)  →  Post / Reel / Video (Lightboard)
```

| Skill | What it does |
| --- | --- |
| `ai-radar` | A periodic English/Persian digest of AI, tech and startup trends, with links and a checkbox per item |
| `radar-deep-dive` | Takes the items I tick and teaches each one step by step, then drafts the posts |
| `rewind` | My writing voice: start from the real moment of need, go one layer deeper at a time, end with one practical takeaway |
| `lightboard` | My visual style: pure black, thin neon outlines, subtle glow |
| `lightboard-diagram` | An animated, ByteByteGo-style explainer diagram, exported as an autoplaying GIF |
| `lightboard-voice-explainer` | A narrated 9:16 explainer video with a cover and burned-in subtitles, synced to my own voice |

Skills are plain `SKILL.md` files: instructions you can read, edit and reuse.

## Examples

| Folder | What it is |
| --- | --- |
| `examples/tokens` | "What does *I hit the token limit* actually mean?" A post image, a short video and an animated diagram |
| `examples/jev` | TypeSafe's Jev / System One models: typed decisions with confidence scores instead of free text |
| `examples/jev-voiced-video` | The full pipeline for a narrated video: script, cut and align a voiceover, captions, render, mix |
| `examples/ai-twins` | Can AI simulate people? Stanford's agent study vs a poll-accuracy study, as a Lightboard image |

## Things I learned building it

- **Check the audio before you trust it.** My voiceover file held the script twice and read the section headings aloud. Alignment found both.
- **Label company claims as company claims.** Speed and price numbers get "reported by the company" and a note to wait for independent tests.
- **Tie ideas back to real work, without internal details.** I describe it generically: "an analytics agent I'm building at work".
- **Simulate first, measure anyway.** True for AI digital twins, and for most ideas.

## Running the examples

```bash
npm install            # Inter + Vazirmatn fonts, Playwright
npx playwright install chromium
python3 examples/tokens/render.py
```

The HTML files load fonts from `node_modules/@fontsource`. The video scripts need `ffmpeg`. Voice alignment uses `pocketsphinx` (`pip install pocketsphinx`).

## Status

Early and evolving. Expect rough edges. Skills change as I learn what works.

*Pegah Davari · Backend & Agentic Systems*
