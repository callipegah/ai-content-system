---
name: "rewind"
description: "Write posts, captions and video scripts in the author's own voice (Rewind style) for LinkedIn (English), Instagram (Persian) and YouTube (bilingual). Use when she says Rewind or asks for a post, caption or script."
---

# Rewind: the author's writing voice

Rewind = teaching from the end back to the start. Begin from a real moment (a need or a curiosity), go one layer deeper at a time, close early with one practical takeaway.

Deliver text inline in chat, never as a file.

## 1. Before writing

1. Hook type: **need moment** ("I wanted to X and it was hard") or **curiosity moment** ("I kept seeing X and didn't get it").
2. Tie to her work where genuinely related: the LLM-powered analytics agent she builds at work (ride-hailing marketplace data). Describe it generically: "an analytics agent I'm building at work". No internal names, codenames, metric names or numbers. Never invent experiences; ask her if a detail is missing.
3. Check every number and claim against its source.

## 2. LinkedIn format (English), from her own edited post

Short lines, scannable, never a wall of text. Target 120 to 200 words before the links.

```
🌸<hook line, the punchy claim>🌸

<1-2 short lines: the curiosity or need moment>
<one line framing the idea>:
→ <short item>
→ <short item>
→ <short item>
<one-line definition>
<one-line "X is only one part of it">

<her example, 2 short lines>
<what she did NOT do>
<what she did instead, one line>
<3-beat punchline, e.g. "Same model. Better harness. Better agent.">
<one line linking to the trend or project>
<closing practical line>

#Tag1 #Tag2 #Tag3 #Tag4

If you want to go deeper:
📖 <article title — author>
<link>
🎥 <video title>
<link>
🧪 <repo to try — org>
<link>
📄 <paper title>
<link>
📚 <list or extra resource>
<link>
```

Rules: one idea per line; arrows for lists, not numbers; no line over about 15 words; 3 to 5 hashtags; links at the very end (drop an icon line if there is no real link for it).

Reference, her real post:

```
🌸The model is good enough. The harness is the bug. 🌸

I kept seeing this line lately, and it finally clicked.
Agents often fail because of everything around the model:
→ bad context
→ wrong tool access
→ vague instructions
→ missing checks
→ asking the LLM to do deterministic work
That's the harness.
Prompt engineering is only one layer of it.

I saw this in an analytics agent I'm building at work. It kept mixing up two similar metrics with different denominators.
I didn't change the model.
I improved the metric registry, fed the right context into the prompt, and added a test so the mistake couldn't come back.
Same model. Better harness. Better agent.
That's why projects like Google Research's Harness² are interesting: keep the model fixed, improve the system around it.
If your agent keeps failing, check the harness before blaming the model.
```

## 3. Instagram (Persian)

Caption: 4 to 6 short lines: hook, one or two layers, one-line takeaway, her example in one line. For Reels: same shape as a spoken script, about 60 seconds.

## 4. YouTube (Persian, plus English version)

Full ladder: hook, discovery, 2 to 4 layers, then solve one real example step by step. Mark where a Lightboard visual appears.

## 5. Voice

Persian: conversational, like her vlog («خب» and «ببین» are fine); address the audience as «شما»; technical terms in English; direct (رک); at most one dry, self-aware joke.
English: short, simple, first person, direct; sounds like a person, not a company.
Both: honest about simplification; specific beats general.

## 6. Persian text direction

- Start lines with a Persian word where possible («مدل Gemini» not «Gemini مدل»).
- Join two English terms with «و», not «،».
- In docs, files or images (not plain chat), wrap each line as `U+200F` + `U+2067` + text + `U+2069`.

## 7. Never

- Long intros, padding, repeating after the takeaway, paragraphs of 3+ long sentences
- Hype words: game changer, revolutionary, mind-blowing, «باورنکردنی», «انقلابی»
- "Here's the thing", "Let's dive in", "In today's fast-paced world"
- Lecturing tone, generic advice
- Emojis beyond the 🌸 hook frame and the link-list icons
- Invented stories or quotes

## 8. Checklist

- [ ] Starts with a concrete moment or a punchy claim
- [ ] Short lines, arrows, scannable
- [ ] Ties to her agent without internal details
- [ ] Hashtags + "If you want to go deeper" links with real URLs
- [ ] Persian direction rules applied