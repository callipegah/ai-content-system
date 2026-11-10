import sys, json, re, difflib
sys.path.insert(0,"/home/claude/post/jev2")
from script import SCENES
A=json.load(open("align.json"))
# rerun-free fix for scenes with mismatched counts: realign via difflib on raw segs saved below
raw=json.load(open("raw_align.json"))
norm=lambda w: re.sub(r"\(\d\)","",re.sub(r"[^a-z'\-()0-9]","",w.lower()))
caps=[]
for sc in SCENES:
    if not sc["say"]: continue
    words=sc["say"].split(); nw=[norm(w) for w in words]
    seg=raw[sc["id"]]; ns=[norm(s[0]) for s in seg]
    T=[None]*len(words)
    for a,b,n in difflib.SequenceMatcher(None,nw,ns,autojunk=False).get_matching_blocks():
        for k in range(n): T[a+k]=(seg[b+k][1],seg[b+k][2])
    # interpolate gaps
    for i in range(len(T)):
        if T[i] is None:
            p=T[i-1][1] if i else 0.0
            j=i
            while j<len(T) and T[j] is None: j+=1
            q=T[j][0] if j<len(T) else p+0.4
            n=j-i; T[i]=(p+(q-p)*0/n if n else p, p+(q-p)/n)
            # simple: assign sequential slices
            for k in range(i,j): T[k]=(p+(q-p)*(k-i)/n, p+(q-p)*(k-i+1)/n)
    # split into sentences, then chunks of <=6 words
    sent=[]; cur=[]
    for i,w in enumerate(words):
        cur.append(i)
        if re.search(r"[.?!]$",w): sent.append(cur); cur=[]
    if cur: sent.append(cur)
    for s in sent:
        n=len(s); k=max(1,-(-n//6)); size=-(-n//k)
        for c in range(0,n,size):
            idx=s[c:c+size]
            caps.append(dict(scene=sc["id"],t0=round(T[idx[0]][0],2),t1=round(T[idx[-1]][1],2),text=" ".join(words[i] for i in idx)))
# make each caption last until the next one in the same scene starts (no flicker), capped
for a,b in zip(caps,caps[1:]):
    if a["scene"]==b["scene"] and b["t0"]-a["t1"]<0.6: a["t1"]=b["t0"]-0.12
json.dump(caps,open("captions.json","w"),indent=1)
print(len(caps)); [print(c) for c in caps[:6]]
