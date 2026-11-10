---
name: "lightboard-voice-explainer"
description: "Narrated 9:16 explainer video in the author's Lightboard look: cover frame, scene animations synced to their voiceover (ElevenLabs preferred) and burned-in English subtitles."
---

# Lightboard voice explainer (9:16 narrated video)

A 1–3 minute vertical explainer for Reels, Shorts and LinkedIn: black Lightboard scenes that build up element by element, timed to a narration, with subtitles at the bottom. Reference output: the JEV / System One explainer (12 scenes: cover, hook, ticket, llm, problems, system1, input, output, branch, numbers, limits, end).

Pipeline: script → her voice → cut and align → timeline HTML → frames → mix → check → deliver.

## 1. Script (rewind rules)

1. Learn the topic from the primary source first. If the name is ambiguous (e.g. "jev" vs JEPA), confirm with her or her link before writing anything.
2. Write the narration with the `rewind` skill voice: spoken, first person, short sentences, one idea per scene, one concrete running example (e.g. a support ticket).
3. Split into 8–12 scenes. Store them as a Python list: `SCENES = [dict(id="cover", say=""), dict(id="hook", say="..."), ..., dict(id="end", say="...", tail=2.2)]`.
4. Company claims (latency, price, "can't hallucinate") are said as *reported by the company*, followed by "wait for independent tests". Say limits plainly.
5. Spell things the way they should be spoken: "eighty-two percent", "seventy to five hundred milliseconds".

## 2. Voice

Her own ElevenLabs voice is the default; synthetic TTS voices (Piper amy/lessac) were rejected as not natural enough.

- Give her the script as plain text, one paragraph per scene, in a code block.
- Ask for **one MP3 per scene named `01.mp3 … NN.mp3`** (best, no cutting needed), or one file with **no headings** in the text. Tell her explicitly: bracket headings like `[02 ticket]` get read aloud.
- Fallback only if she asks: Piper voices from GitHub releases (HuggingFace is blocked), pitch with `rubberband=pitch=1.08:formant=shifted`.

## 3. Cut and align a single-file voiceover

Always check the file before using it. In the JEV run the MP3 was 312 s for a ~150 s script: it held **two full takes**, and the scene headings were read aloud ("oh three LLM", "eleven end").

1. `ffmpeg -i voice.mp3 -ac 1 -ar 16000 voice16.wav`. Compare its duration with the expected one (~150 words/min).
2. Find pauses: `silencedetect=noise=-38dB:d=0.2`. Turn the gaps into speech chunks.
3. Rough-transcribe each chunk with PocketSphinx (`pip install pocketsphinx --break-system-packages`; Whisper/Vosk model hosts are blocked). Print `start end text`. From this list:
   - pick one take (the first, unless she says otherwise) and say which one you used;
   - drop chunks that are headings (number + scene name);
   - write the scene ranges `(id, speech_start, speech_end)`.
4. Cut each scene from the original MP3 with 0.08 s before and 0.15 s after: `clips/<id>.wav` (44.1 kHz) and `clips/<id>16.wav` (16 kHz mono, for alignment).
5. Forced-align the known scene text to each 16 kHz clip:

```python
from pocketsphinx import Decoder
d = Decoder(samprate=16000)
for w, ph in {"llm": "EH L EH L EH M", "jev": "JH EH V", "typesafe": "T AY P S EY F",
              "kahneman": "K AA N AH M AH N", "classifier": "K L AE S AH F AY ER"}.items():
    try: d.add_word(w, ph, True)
    except Exception: pass            # word already in the dictionary
# first list unknown words: d.lookup_word(w) is None → add a pronunciation
d.set_align_text(" ".join(normalised_words))
d.start_utt(); d.process_raw(pcm_bytes, full_utt=True); d.end_utt()
words = [(s.word, s.start_frame/100, (s.end_frame+1)/100) for s in d.seg()
         if s.word not in ("<sil>", "<s>", "</s>", "[NOISE]")]
```

   Strip the `(2)` variant suffixes, match to the script words with `difflib.SequenceMatcher`, and interpolate any missing words.
6. Captions: split each sentence into chunks of ≤ 6 words (balanced sizes). Each caption runs from its first word's start to its last word's end. Stretch it to the next caption when the gap is < 0.6 s, so they don't flicker. Save as `captions.json` `[{scene, t0, t1, text}]`, with times relative to the scene clip.

With per-scene files from her, skip steps 2–4 and run the alignment on each file.

## 4. Timeline HTML (`gen.py`)

- Canvas 1080 × 1920, black. `lightboard` palette and Inter 500/700/800 via `@fontsource/inter`. Glow only on titles and outlines. Footer `BACKEND & AGENTIC SYSTEMS`.
- Scene timing comes from the audio:
  - cover = 2.6 s silent;
  - every other scene = `LEAD 0.3 + clip duration + GAP 0.45`;
  - the end scene gets +2.2 s tail.
  - Write `timeline.json {starts, total, lead}`.
- Elements: `E(scene, frac, html, cls, style)`. Each appears at `start + LEAD + frac × clip_duration`, fades and slides up 28 px over 0.45 s, and fades out at the scene end. Place each element's `frac` where the narration mentions it (or key it to an aligned word time).
- Building blocks:
  - heading: two lines, the second coloured and glowing, ~70 px at top 190;
  - `box` (label + big value);
  - `row` pills (value + teal score);
  - `card` (bold title + sub-line);
  - typewriter text (`data-type`) for "the LLM writes word by word";
  - schema in monospace;
  - teal = good/fast, pink = problem/LLM, yellow = key item.
- Cover = first frames (instant, no fade): pill tag, a 2-line hook title of about 104 px, a subtitle, one visual (e.g. a typed decision card) and one tagline. It works as the thumbnail.
- Subtitles: `.cap` divs, top 1590 px, 46 px, weight 700, white, centred and 940 px wide, shown between `data-cin` and `data-cout`. Keep scene content above about 1500 px so it never collides with them.
- Everything is driven by `window.setT(t)`; no CSS animations.

## 5. Render and mix

```python
# frames: 30 fps JPEGs
pg = browser.new_page(viewport=dict(width=1080, height=1920)); pg.goto("file://.../video.html")
for i in range(int(total*30)+1): pg.evaluate(f"setT({i/30})"); pg.screenshot(path=f"fr/{i:05d}.jpg", type="jpeg", quality=92)
```

Run the frame loop in the background (about 4,500 frames take several minutes).

Audio:
- each clip is placed with `adelay=(start+LEAD)*1000`;
- optional ambient pad: `aevalsrc` with 3 soft sines → `lowpass=600, volume=0.035`, with fades;
- `amix normalize=0`, then `loudnorm=I=-16:TP=-1.5`.

Then mux:

`ffmpeg -framerate 30 -i fr/%05d.jpg -i audio.wav -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4`

Export `cover.png` = the frame at t ≈ 1.5 s.

## 6. Check before sending

- [ ] One frame per scene, plus one with a caption: no overlaps, no wrapping in pills, captions clear of content
- [ ] Scene joins: no cut words, no heading words, only one take
- [ ] Spot-check 3 captions against the audio (start of the video, middle, end)
- [ ] Duration ≈ sum of the clips + gaps; audio not truncated
- [ ] Claims labelled as company-reported

## 7. Deliver

- Send the MP4 and the cover PNG. Say which take was used and anything that was cut.
- LinkedIn: 9:16 shows narrow in the feed. Offer a 4:5 version (1080 × 1350, same scenes re-laid out), or a `lightboard-diagram` GIF for an image-like autoplay post.
- Post text, if needed: write it with `rewind`, with the same points as the video.