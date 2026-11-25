"""Compose the final 1024x1024 entry image from the chosen candidate (A).
Run: python3 compose.py  -> writes entry.png in this repo dir.
All text is drawn with PIL (real fonts), so nothing is garbled.
Text is measured and shrunk/wrapped to fit its box; nothing may overflow."""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/home/hatch/workspace/makefun/news-image-20261125-candidates/media-generation-news25-candidate-a-0-33367517-b20c-4c03-b6cb-47d6cc230c42.png"

NAVY = (20, 38, 61)
GOLD = (201, 162, 75)
CREAM = (246, 240, 226)
WHITE = (255, 255, 255)
BAND = (13, 27, 45)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

def fit_font(draw, text, name, start, max_w):
    size = start
    f = font(name, size)
    while size > 10 and draw.textlength(text, font=f) > max_w:
        size -= 1
        f = font(name, size)
    return f

def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

base = Image.open(SRC).convert("RGB")
base = base.resize((1024, 1024), Image.LANCZOS)  # source is 1600x1600; scale first
grid = base.crop((0, 23, 1024, 891))  # 1024x868, keeps all four quadrants
assert grid.size == (1024, 868)

canvas = Image.new("RGB", (1024, 1024), CREAM)
draw = ImageDraw.Draw(canvas)

# --- Masthead: 0..100 ---
draw.rectangle([0, 0, 1024, 100], fill=NAVY)
f_date = fit_font(draw, "WEDNESDAY 25 NOVEMBER 2026", "DejaVuSans-Bold.ttf", 56, 980)
draw.text((512, 48), "WEDNESDAY 25 NOVEMBER 2026", font=f_date, fill=CREAM, anchor="mm")
draw.rectangle([0, 100, 1024, 104], fill=GOLD)

# --- Grid: 104..972 ---
canvas.paste(grid, (0, 104))

# --- Caption bands at the bottom of each quadrant (512x434 each) ---
panels = [
    (0,   "UKRAINE SINKS RUSSIAN SHIP", "Drones hit ships off Libya and in the Baltic"),
    (512, "RIYADH TOWER HIT AGAIN", "Houthi strike wounds 11; second in five days"),
    (0,   "COP31 ENDS WITH NO DEAL", "Climate talks collapse over fossil fuels"),
    (512, "HUAWEI FOUND GUILTY", "US jury: 10 counts, trade secrets and fraud"),
]
for i, (x0, head, sub) in enumerate(panels):
    y0 = 104 + (i // 2) * 434
    band_y0 = y0 + 434 - 104
    overlay = Image.new("RGBA", (512, 104), BAND + (218,))
    canvas.paste(overlay, (x0, band_y0), overlay)
    d = ImageDraw.Draw(canvas)
    fh = fit_font(d, head, "DejaVuSans-Bold.ttf", 27, 480)
    d.text((x0 + 16, band_y0 + 28), head, font=fh, fill=WHITE, anchor="lm")
    fs = fit_font(d, sub, "DejaVuSans.ttf", 21, 480)
    sub_lines = wrap(d, sub, fs, 480)
    d.text((x0 + 16, band_y0 + 62), sub_lines[0], font=fs, fill=(214, 224, 235), anchor="lm")
    if len(sub_lines) > 1:
        d.text((x0 + 16, band_y0 + 88), sub_lines[1], font=fs, fill=(214, 224, 235), anchor="lm")

# --- Footer strip: 972..1024 ---
draw.rectangle([0, 972, 1024, 1024], fill=CREAM)
draw.rectangle([0, 972, 1024, 975], fill=GOLD)
foot = "Also: CIA system breached  •  China probes Chen Jining  •  Chess title Game 1 drawn"
f_foot = fit_font(draw, foot, "DejaVuSans.ttf", 21, 1000)
draw.text((512, 998), foot, font=f_foot, fill=NAVY, anchor="mm")

canvas.save(os.path.join(HERE, "entry.png"), "PNG", optimize=True)
print("saved", os.path.join(HERE, "entry.png"), canvas.size)
