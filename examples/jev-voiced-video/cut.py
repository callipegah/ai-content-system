import subprocess, json
R = [("hook",0.16,9.60),("ticket",10.52,19.35),("llm",21.66,42.08),("problems",44.26,57.74),
     ("system1",59.97,73.83),("input",75.70,97.52),("output",99.39,112.37),("branch",114.14,122.07),
     ("numbers",123.91,134.64),("limits",136.19,146.23),("end",147.82,155.55)]
out=[]
for sid,a,b in R:
    a=max(0,a-0.08); b=b+0.15
    for src,dst,extra in [("voice.mp3",f"clips/{sid}.wav",["-ar","44100"]),("voice16.wav",f"clips/{sid}16.wav",["-ar","16000","-ac","1"])]:
        subprocess.run(["ffmpeg","-y","-loglevel","error","-ss",f"{a:.3f}","-to",f"{b:.3f}","-i",src,*extra,dst],check=True)
    out.append(dict(id=sid,src_start=a,audio=round(b-a,3)))
json.dump(out,open("clips.json","w"),indent=1); print(sum(x["audio"] for x in out))
