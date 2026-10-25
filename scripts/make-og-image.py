#!/usr/bin/env python3
"""Generate the 1200x630 social preview for Lakshman Shanmugam.

Pillow-only, byte-reproducible. Clean academic card matching the template:
white ground, #36c link-blue accent (the site's favicon/icon color), the site's
actual favicon logo (images/favicon-512x512.png, the OOjs "academic-progressive"
icon used across the template), title + subtitle + content pills + domain chip.

Usage:
    python3 scripts/make-og-image.py

The script writes images/og-image.png. Requires Pillow and a TrueType font
(default DejaVu Sans; override the font directory with FONT_DIR).
"""
import os
from PIL import Image, ImageDraw, ImageFont

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

W, H = 1200, 630
BG = (255, 255, 255)          # white
BLUE = (51, 102, 204)         # #36c accent
DARK = (51, 51, 51)           # #333 text
GREY = (110, 110, 110)        # #6e6e6e subtitle
LIGHTBLUE = (235, 240, 250)   # chip backing

FONT_DIR = os.environ.get("FONT_DIR", "/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    p = os.path.join(FONT_DIR, name)
    if not os.path.exists(p):
        p = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf")
    if not os.path.exists(p):
        p = os.path.join(FONT_DIR, "arialbd.ttf" if bold else "arial.ttf")
    return ImageFont.truetype(p, size)


def rounded(d, box, r, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    f_title = font(56, bold=True)
    f_sub = font(36)
    f_pill = font(28, bold=True)
    f_domain = font(30, bold=True)

    # Title + subtitle (left). Vertical rhythm: 44px padding above the title
    # matches the 44px padding below the footer domain chip (maintainer review
    # 2026-10-18). Content band 44..586 (542px) split into even 58px gaps.
    d.text((70, 32), "Lakshman Shanmugam", font=f_title, fill=DARK)
    d.text((70, 164), "AI/ML Engineer", font=f_sub, fill=GREY)
    d.text((70, 258), "LLMs, agentic workflows, and RAG", font=f_sub, fill=GREY)

    # separator
    d.line([70, 362, W - 70, 362], fill=(230, 230, 230), width=2)

    # content pills
    pills = ["Experience", "Publications", "Skills", "Resume"]
    x = 70
    y = 422
    for p_ in pills:
        fw = d.textlength(p_, font=f_pill) + 44
        if x + fw > 1130:
            x = 70
            y += 74
        rounded(d, [x, y, x + fw, y + 58], 29, fill=LIGHTBLUE)
        d.text((x + 22, y + 12), p_, font=f_pill, fill=BLUE)
        x += fw + 18

    # footer domain chip
    d.textlength("lakshmans27.github.io", font=f_domain)  # measure
    d.rounded_rectangle([70, H - 92, 592, H - 44], 24, fill=DARK)
    d.text((104, H - 84), "lakshmans27.github.io", font=f_domain, fill=(255, 255, 255))

    out = os.path.join(REPO_ROOT, "images", "og-image.png")
    img.save(out, "PNG")
    print("wrote", os.path.normpath(out), img.size)


if __name__ == "__main__":
    main()
