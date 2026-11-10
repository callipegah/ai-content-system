from playwright.sync_api import sync_playwright
FPS, DUR = 30, 46
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto("file:///home/claude/post/short45.html"); pg.wait_for_timeout(800)
    for f in range(FPS * DUR):
        pg.evaluate(f"setT({f / FPS})")
        pg.screenshot(path=f"frames45/f{f:05d}.jpg", type="jpeg", quality=92)
    b.close()
