"""Build the voiced JEV explainer HTML from scene specs + narration durations."""
import json
D = {x["id"]: x["audio"] for x in json.load(open("durations.json"))}
ORDER = [x["id"] for x in json.load(open("durations.json"))]
GAP, LEAD = 0.45, 0.3
starts, t = {}, 0.0
for sid in ORDER:
    starts[sid] = t
    dur = 2.6 if sid == "cover" else D[sid] + LEAD + GAP + (2.2 if sid == "end" else 0)
    t += dur
ends = {sid: (starts[ORDER[i + 1]] if i + 1 < len(ORDER) else t) for i, sid in enumerate(ORDER)}
TOTAL = t

els = []
def E(sid, frac, html, cls="", style="", extra="", keepx=False, instant=False):
    a = starts[sid] + (0 if sid == "cover" else LEAD + frac * D[sid])
    o = 999 if sid == "end" else ends[sid]
    attrs = f'data-in="{a:.2f}" data-out="{o:.2f}"' + (" data-keepx" if keepx else "") + (" data-instant" if instant else "")
    els.append(f'<div class="a {cls}" style="{style}" {attrs} {extra}>{html}</div>')
def H(sid, l1, l2, col="gt", top=190, size=70):
    E(sid, 0.0, f'{l1}<br><span class="{col}">{l2}</span>', "c h", f"top:{top}px;font-size:{size}px")

# cover
E("cover", 0, "NEW MODEL CLASS · JEV", "pill", "top:240px;transform:translateX(-50%)", keepx=True, instant=True)
E("cover", 0, 'Decisions,<br><span class="gp">not sentences.</span>', "c h", "top:520px;font-size:104px;line-height:1.08", instant=True)
E("cover", 0, "Jev &amp; System One models, explained", "c sub", "top:850px", instant=True)
E("cover", 0, '<div class="k" style="text-align:center">TYPED DECISION</div><div class="mini">urgency: high <b>0.82</b></div><div class="mini y">team: billing <b>0.91</b></div>',
  "box", "top:1000px;left:240px;width:600px;border-color:#19e3d1;filter:drop-shadow(0 0 5px #19e3d1)", instant=True)
E("cover", 0, 'No parsing. <span style="color:#ffd166">A confidence score.</span>', "c", "top:1450px;font-weight:700;font-size:36px;color:#fff", instant=True)
# hook
H("hook", "Inside your code,", "you're asking it to decide.")
for k, q in enumerate(["Is this ticket urgent?", "Which team gets it?", "How risky is it?"]):
    E("hook", 0.55 + 0.12 * k, q, "row", f"top:{620 + k * 130}px")
# ticket
H("ticket", "A real example:", "a support ticket", "gy")
E("ticket", 0.12, '<div class="k">SUPPORT TICKET</div><div class="v">“I was charged twice<br>for my ride.”</div>', "box", "top:560px")
E("ticket", 0.55, "How urgent? <b>?</b>", "row", "top:1000px")
E("ticket", 0.78, "Which team? <b>?</b>", "row", "top:1120px")
# llm
H("llm", "A normal LLM", "answers in sentences.", "gp")
E("llm", 0.1, '<div class="k" style="color:#ff4fa3">LLM OUTPUT · WORD BY WORD</div><div class="v" data-type="“This seems fairly urgent, probably the finance team…”"></div>',
  "box", "top:540px;border-color:#ff4fa3")
E("llm", 0.42, "“fairly urgent” <b>→ high? medium?</b>", "row", "top:960px;left:90px;width:900px")
E("llm", 0.55, "“finance team” <b>→ which team?</b>", "row", "top:1080px;left:90px;width:900px")
E("llm", 0.72, 'parse → validate → <span class="gp">repeat</span>', "c", "top:1250px;font-weight:800;font-size:54px;color:#fff")
E("llm", 0.86, "and the wording changes every time", "c sub", "top:1350px")
# problems
H("problems", "Three problems", "with LLMs in code", "gp")
for k, (a, b, f) in enumerate([("A string to parse", "not a value your code can use", 0.2), ("Slow and costly", "written word by word", 0.45), ("Overconfident", "wrong without warning", 0.7)]):
    E("problems", f, f"<b>{a}</b><span>{b}</span>", "card", f"top:{560 + k * 190}px" + (";border-color:#ff4fa3" if k == 2 else ""))
# system one
H("system1", "Why", "“System One”?", "gt")
E("system1", 0.25, '<div class="k" style="color:#19e3d1">SYSTEM 1</div><div class="v">fast · intuitive</div>', "box", "top:580px;border-color:#19e3d1")
E("system1", 0.42, '<div class="k">SYSTEM 2</div><div class="v">slow · step by step<br><span style="font-size:30px;color:#cbd5e1;font-weight:500">← reasoning LLMs</span></div>', "box", "top:860px")
E("system1", 0.85, 'System One models: <span style="color:#19e3d1">built for fast decisions</span>', "c", "top:1230px;font-weight:700;font-size:36px;color:#fff")
E("system1", 0.25, "names from Kahneman's “Thinking, Fast and Slow”", "c", "top:1330px;font-weight:500;font-size:26px;color:#64748b")
# input
H("input", "Jev takes", "two inputs", "gt")
E("input", 0.12, '<div class="k" style="color:#19e3d1">1 · PROGRAM STATE</div><div class="v" style="font-size:34px">ticket text · customer info · history<br><span style="font-size:28px;color:#cbd5e1;font-weight:500">doesn\'t need to be clean</span></div>', "box", "top:520px;border-color:#19e3d1")
E("input", 0.52, '<div class="k" style="color:#ffd166">2 · SCHEMA · DEFINED FIRST</div><div class="v mono" style="font-size:34px">urgency: low | medium | high<br>team: billing | safety | support</div>', "box", "top:880px;border-color:#ffd166")
E("input", 0.66, "every allowed answer, listed before you ask", "c sub", "top:1230px;font-size:32px")
# output
H("output", "Jev picks", "from your options only.", "gt")
E("output", 0.3, "one pass, not word by word ↓", "c", "top:560px;font-weight:700;font-size:32px;color:#64748b")
E("output", 0.62, "urgency: high <b>82%</b>", "row", "top:660px")
E("output", 0.78, "team: billing <b>91%</b>", "row", "top:780px;border-color:#ffd166;color:#ffd166")
E("output", 0.5, "every answer comes with a confidence score", "c sub", "top:960px;font-size:32px")
E("output", 0.62, "example values", "c", "top:1040px;font-weight:500;font-size:24px;color:#64748b")
# branch
H("branch", "Your code", "doesn't have to guess.", "gy")
E("branch", 0.35, '<div class="k" style="color:#19e3d1">CONFIDENT</div><div class="v">→ act automatically</div>', "box", "top:600px;border-color:#19e3d1")
E("branch", 0.6, '<div class="k" style="color:#ff4fa3">UNSURE</div><div class="v">→ hand off to a human<br>or a full LLM</div>', "box", "top:880px;border-color:#ff4fa3")
# numbers
H("numbers", "What TypeSafe", "reports", "gp", size=64)
E("numbers", 0.1, "<b>70–500 ms</b><span>end-to-end latency</span>", "card", "top:520px")
E("numbers", 0.35, "<b>Very low cost</b><span>$0.042 per million input tokens</span>", "card", "top:710px")
E("numbers", 0.6, 'Company-reported, early access.<br><span style="color:#fff;font-weight:700">Wait for independent tests.</span>', "c sub", "top:960px;font-size:34px")
# limits
H("limits", "To be", "clear", "gp")
E("limits", 0.15, "<b>No free text</b><span>no chat · no code · no writing</span>", "card", "top:540px")
E("limits", 0.45, "<b>“Can't hallucinate”</b><span>= always matches your schema, not always right</span>", "card", "top:730px;border-color:#ffd166")
# end
E("end", 0.0, 'It replaces the LLM<br><span class="gt">as a classifier.</span>', "c h", "top:420px;font-size:76px")
E("end", 0.55, 'Not a chat model.<br><span class="gp">A decision model.</span>', "c h", "top:760px;font-size:76px")
E("end", 1.0, "FOLLOW FOR MORE", "pill", "top:1150px;transform:translateX(-50%)", keepx=True)

import os
if os.path.exists("captions.json"):
    for c in json.load(open("captions.json")):
        b = starts[c["scene"]] + LEAD
        els.append(f'<div class="cap" data-cin="{b + c["t0"]:.2f}" data-cout="{b + c["t1"] + 0.12:.2f}">{c["text"]}</div>')
css = open("/home/claude/post/jev_short.html").read().split("<style>")[1].split("</style>")[0]
css += """.mini{width:480px;margin:18px auto 0;height:80px;border:3px solid #334155;border-radius:40px;display:flex;align-items:center;justify-content:space-between;padding:0 30px;font-weight:700;font-size:32px;color:#fff}
.mini b{color:#19e3d1;font-size:28px}.mini.y{border-color:#ffd166;color:#ffd166}
.cap{position:absolute;left:70px;width:940px;top:1590px;text-align:center;font-weight:700;font-size:46px;line-height:1.3;color:#fff;opacity:0}"""
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="a c foot" data-in="0" data-out="999" data-instant>BACKEND &amp; AGENTIC SYSTEMS</div>
{chr(10).join(els)}
<script>
const els=[...document.querySelectorAll('.a')];
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
const types=[...document.querySelectorAll('[data-type]')];\nconst caps=[...document.querySelectorAll('.cap')];
const TS={starts["llm"] + LEAD + 0.22 * D["llm"]:.2f}, TE={starts["llm"] + LEAD + 0.40 * D["llm"]:.2f};
window.setT=function(t){{
  for(const e of els){{
    const i=+e.dataset.in,o=+e.dataset.out;
    let p=e.hasAttribute('data-instant')?(t>=i?1:0):ease((t-i)/0.45);
    let q=ease((t-(o-0.35))/0.35);
    e.style.opacity=Math.max(0,p-q);
    const kx=e.hasAttribute('data-keepx')?'translateX(-50%) ':'';
    e.style.transform=kx+'translateY('+((1-p)*28)+'px)';
  }}
  for(const c of caps){{c.style.opacity=(t>=+c.dataset.cin&&t<+c.dataset.cout)?1:0;}}\n  for(const e of types){{
    const s=e.dataset.type, k=Math.max(0,Math.min(s.length,Math.round((t-TS)/(TE-TS)*s.length)));
    e.textContent=s.slice(0,k)+(t>=TS&&t<TE+0.6?'▌':'');
  }}
}};
setT(0);
</script></body></html>"""
open("jev_voice.html", "w").write(html)
json.dump(dict(starts=starts, total=TOTAL, lead=LEAD), open("timeline.json", "w"), indent=1)
print(TOTAL)
