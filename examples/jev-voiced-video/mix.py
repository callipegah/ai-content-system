import json, subprocess
T=json.load(open("timeline.json")); S=T["starts"]; L=T["lead"]
clips=[x["id"] for x in json.load(open("clips.json"))]
inp=[]; f=[]
for k,sid in enumerate(clips):
    inp+=["-i",f"clips/{sid}.wav"]; ms=int((S[sid]+L)*1000)
    f.append(f"[{k}:a]aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]")
n=len(clips); tot=T["total"]
f.append(f"aevalsrc='0.5*sin(2*PI*110*t)+0.4*sin(2*PI*164.8*t)+0.3*sin(2*PI*220*t)':s=44100:d={tot:.2f},lowpass=f=600,volume=0.035,aformat=channel_layouts=stereo,afade=t=in:d=2,afade=t=out:st={tot-2.5:.2f}:d=2.5[pad]")
f.append("".join(f"[a{k}]" for k in range(n))+f"[pad]amix=inputs={n+1}:normalize=0,loudnorm=I=-16:TP=-1.5[out]")
subprocess.run(["ffmpeg","-y","-loglevel","error",*inp,"-filter_complex",";".join(f),"-map","[out]","-t",f"{tot:.2f}","-ar","44100","audio.wav"],check=True)
subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate","30","-i","fr/%05d.jpg","-i","audio.wav","-c:v","libx264","-pix_fmt","yuv420p","-crf","20","-preset","medium","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart","jev_explainer_elevenlabs.mp4"],check=True)
