import json, os, sys
from playwright.sync_api import sync_playwright
T=json.load(open("timeline.json")); FPS=30; N=int(T["total"]*FPS)+1
os.makedirs("fr",exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport=dict(width=1080,height=1920))
    pg.goto("file://"+os.path.abspath("jev_voice.html")); pg.wait_for_timeout(800)
    for i in range(N):
        pg.evaluate(f"setT({i/FPS})"); pg.screenshot(path=f"fr/{i:05d}.jpg",type="jpeg",quality=92)
    b.close()
print(N)
