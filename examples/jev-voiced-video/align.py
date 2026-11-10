import sys, json, re, wave
sys.path.insert(0,"/home/claude/post/jev2")
from script import SCENES
from pocketsphinx import Decoder
EXTRA={"llm":"EH L EH L EH M","llms":"EH L EH L EH M Z","jev":"JH EH V","typesafe":"T AY P S EY F",
       "kahneman":"K AA N AH M AH N","classifier":"K L AE S AH F AY ER","eighty-two":"EY T IY T UW",
       "ninety-one":"N AY N T IY W AH N"}
d=Decoder(samprate=16000)
for w,p in EXTRA.items():
    try: d.add_word(w,p,True)
    except Exception as e: print("skip",w)
res={}; raw_all={}
for sc in SCENES:
    if not sc["say"]: continue
    words=sc["say"].split()
    norm=[re.sub(r"[^a-z'\-]","",w.lower()) for w in words]
    norm=[n.replace("’","'") for n in norm]
    data=wave.open(f"clips/{sc['id']}16.wav","rb").readframes(10**9)
    try:
        d.set_align_text(" ".join(norm))
        d.start_utt(); d.process_raw(data,full_utt=True); d.end_utt()
        al=[(s.word,s.start_frame/100,(s.end_frame+1)/100) for s in d.seg() if s.word not in ("<sil>","<s>","</s>","[NOISE]")]
    except Exception as e:
        print(sc["id"],"ERR",e); al=[]
    raw_all[sc['id']]=al
    ok=len(al)==len(words)
    print(sc["id"],len(words),len(al),ok, al[:3], al[-2:] if al else None)
    res[sc["id"]]=[dict(w=words[i],t0=al[i][1],t1=al[i][2]) for i in range(len(words))] if ok else None
json.dump(res,open("align.json","w"),indent=1)


json.dump(raw_all,open("raw_align.json","w"))
