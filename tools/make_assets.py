"""Draws the EloGlobal logo, the app icon and every store graphic into assets/ (run with the app's runtime).

    runtime\\python.exe -s tools\\make_assets.py [--screenshots <folder with app screenshots>]

The logo is an original drawing: two speech bubbles linked like the links of a chain ("elo" means "link" in
Portuguese) - one for each side of a conversation. The SVG sources are written first; every PNG / ICO is rendered
from them with QtSvg. The wordmark's letters are outlines of Poppins SemiBold (SIL Open Font License 1.1, downloaded
once into tools/.cache - the font file itself is not shipped). Colours: teal and amber, never Discord's blurple.

Sizes (checked 2026-10): Steam store capsules 920x430 / 462x174 / 1232x706 / 748x896, page background 1438x810,
library 600x900 / 920x430 / 3840x1240 hero / logo 1280x720, shortcut icon 256 (ICO/PNG), app icon 184 JPG,
screenshots 1920x1080; Microsoft Store tile icon 300x300, box art 1080x1080, poster 720x1080, super hero 1920x1080,
MSIX package logos (Square44x44 / Square150x150 / Wide310x150 / Square71x71 / Square310x310 / StoreLogo /
SplashScreen) in every scale.
"""
from __future__ import annotations

import math
import struct
import sys
import urllib.request
from pathlib import Path

from PySide6.QtCore import QByteArray, QPointF, QRectF, Qt
from PySide6.QtGui import (QBrush, QColor, QFont, QFontDatabase, QGuiApplication, QImage, QLinearGradient, QPainter,
                           QPainterPath, QPen, QRadialGradient)
from PySide6.QtSvg import QSvgRenderer

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
CACHE = Path(__file__).resolve().parent / ".cache"
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/Poppins-SemiBold.ttf"

TEAL_DARK, TEAL, TEAL_LIGHT = "#0B5F58", "#14A698", "#2EC4B6"
AMBER = "#FFB547"
NAVY, NAVY2 = "#0C1A22", "#12313A"
WHITE = "#F7FBFC"


# ----------------------------------------------------------------------------------------------- logo mark (SVG)
def _ring_tail(cx, cy, r_out, a1, a2, tip):
    """Path of a speech-bubble tail leaving a ring between the angles a1..a2 (degrees, y down) towards `tip`."""
    p1 = (cx + r_out * math.cos(math.radians(a1)), cy + r_out * math.sin(math.radians(a1)))
    p2 = (cx + r_out * math.cos(math.radians(a2)), cy + r_out * math.sin(math.radians(a2)))
    return f"M{p1[0]:.1f},{p1[1]:.1f} L{tip[0]:.1f},{tip[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} Z"


def _intersections(c1, c2, r):
    (x1, y1), (x2, y2) = c1, c2
    d = math.hypot(x2 - x1, y2 - y1)
    a = d / 2
    h = math.sqrt(r * r - a * a)
    mx, my = x1 + (x2 - x1) * a / d, y1 + (y2 - y1) * a / d
    ox, oy = -(y2 - y1) * h / d, (x2 - x1) * h / d
    return (mx + ox, my + oy), (mx - ox, my - oy)


def mark_svg(background: bool = True, size: int = 256) -> str:
    """The logo mark. background=True: on the rounded teal square (app icon); False: transparent."""
    A, B, R, W = (98, 112), (158, 144), 52, 21          # ring centres, centre-line radius, stroke width
    p_top, p_bot = _intersections(A, B, R)
    over = p_top if p_top[1] < p_bot[1] else p_bot      # amber goes over white here, white over amber at the other
    tail_a = _ring_tail(A[0], A[1], R + W / 2 - 1, 112, 150, (A[0] - 60, A[1] + 84))
    tail_b = _ring_tail(B[0], B[1], R + W / 2 - 1, 30, 68, (B[0] + 62, B[1] + 80))
    ring_a = f'<circle cx="{A[0]}" cy="{A[1]}" r="{R}" fill="none" stroke="{WHITE}" stroke-width="{W}"/>'
    ring_b = f'<circle cx="{B[0]}" cy="{B[1]}" r="{R}" fill="none" stroke="{AMBER}" stroke-width="{W}"/>'
    bg = ""
    if background:
        bg = ('<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
              f'<stop offset="0" stop-color="{TEAL_DARK}"/><stop offset="1" stop-color="{TEAL_LIGHT}"/>'
              '</linearGradient></defs>'
              '<rect x="8" y="8" width="240" height="240" rx="58" fill="url(#bg)"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 256 256">'
            f'{bg}'
            f'<defs><clipPath id="over"><circle cx="{over[0]:.1f}" cy="{over[1]:.1f}" r="{W * 0.95:.1f}"/>'
            '</clipPath></defs>'
            f'<path d="{tail_b}" fill="{AMBER}"/>{ring_b}'
            f'<path d="{tail_a}" fill="{WHITE}"/>{ring_a}'
            f'<g clip-path="url(#over)">{ring_b}</g>'
            '</svg>')


# ----------------------------------------------------------------------------------------------- wordmark
_font_family = None


def _font() -> str:
    global _font_family
    if _font_family is None:
        f = CACHE / "Poppins-SemiBold.ttf"
        if not f.exists():
            CACHE.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(FONT_URL, f)
        fid = QFontDatabase.addApplicationFont(str(f))
        fams = QFontDatabase.applicationFontFamilies(fid)
        if not fams:
            raise SystemExit("could not load the Poppins font")
        _font_family = fams[0]
    return _font_family


def text_path(text: str, px: float) -> QPainterPath:
    f = QFont(_font())
    f.setPixelSize(int(px))
    f.setWeight(QFont.DemiBold)
    p = QPainterPath()
    p.addText(0, 0, f, text)
    return p


def path_to_svg_d(path: QPainterPath, dx=0.0, dy=0.0) -> str:
    out, i, n = [], 0, path.elementCount()
    while i < n:
        e = path.elementAt(i)
        if e.type == QPainterPath.MoveToElement:
            out.append(f"M{e.x + dx:.2f},{e.y + dy:.2f}")
        elif e.type == QPainterPath.LineToElement:
            out.append(f"L{e.x + dx:.2f},{e.y + dy:.2f}")
        elif e.type == QPainterPath.CurveToElement:
            c2, end = path.elementAt(i + 1), path.elementAt(i + 2)
            out.append(f"C{e.x + dx:.2f},{e.y + dy:.2f} {c2.x + dx:.2f},{c2.y + dy:.2f} {end.x + dx:.2f},{end.y + dy:.2f}")
            i += 2
        i += 1
    return " ".join(out)


def logo_svg(dark_bg: bool = True) -> tuple[str, float, float]:
    """Mark + 'EloGlobal' wordmark side by side, transparent background. Returns (svg, width, height)."""
    px = 150
    elo, glo = text_path("Elo", px), text_path("Global", px)
    w_elo = elo.boundingRect().right()
    gap = px * 0.02
    full_h = 256
    base = 128 + px * 0.36                                   # baseline: the letters' x-height centred on the mark
    x0 = 256 + 40
    c1, c2 = (WHITE, TEAL_LIGHT) if dark_bg else (NAVY2, TEAL)
    d1 = path_to_svg_d(elo, x0, base)
    d2 = path_to_svg_d(glo, x0 + w_elo + gap, base)
    width = x0 + w_elo + gap + glo.boundingRect().right() + 16
    mark = mark_svg(background=True).split(">", 1)[1].rsplit("</svg>", 1)[0]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{full_h}" '
           f'viewBox="0 0 {width:.0f} {full_h}">{mark}'
           f'<path d="{d1}" fill="{c1}"/><path d="{d2}" fill="{c2}"/></svg>')
    return svg, width, full_h


# ----------------------------------------------------------------------------------------------- rendering
def render(svg: str, w: int, h: int, bg: str | None = None) -> QImage:
    img = QImage(w, h, QImage.Format_ARGB32_Premultiplied)
    img.fill(QColor(bg) if bg else Qt.transparent)
    r = QSvgRenderer(QByteArray(svg.encode("utf-8")))
    p = QPainter(img)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    r.render(p, QRectF(0, 0, w, h))
    p.end()
    return img


def draw_svg(p: QPainter, svg: str, rect: QRectF):
    QSvgRenderer(QByteArray(svg.encode("utf-8"))).render(p, rect)


def save(img: QImage, rel: str, fmt: str | None = None, quality: int = 95):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "JPG":
        img = img.convertToFormat(QImage.Format_RGB32)
    img.save(str(path), fmt, quality if fmt == "JPG" else -1)       # PNG: Qt's default (full) compression
    return path


def write_ico(images: list[QImage], path: Path):
    """Multi-size .ico with PNG-compressed entries (Windows Vista and newer)."""
    blobs = []
    for img in images:
        ba = QByteArray()
        from PySide6.QtCore import QBuffer, QIODevice
        buf = QBuffer(ba)
        buf.open(QIODevice.WriteOnly)
        img.save(buf, "PNG")
        blobs.append((img.width(), img.height(), bytes(ba)))
    head = struct.pack("<HHH", 0, 1, len(blobs))
    offset = 6 + 16 * len(blobs)
    entries, data = b"", b""
    for w, h, png in blobs:
        entries += struct.pack("<BBBBHHII", w % 256, h % 256, 0, 0, 1, 32, len(png), offset + len(data))
        data += png
    path.write_bytes(head + entries + data)


# ----------------------------------------------------------------------------------------------- artwork
def backdrop(w: int, h: int, glow=(0.5, 0.45), seed: int = 7) -> QImage:
    """Dark navy background with a soft teal glow, sound-wave lines and faint bubble rings (no text)."""
    import random
    rnd = random.Random(seed)
    img = QImage(w, h, QImage.Format_ARGB32_Premultiplied)
    p = QPainter(img)
    p.setRenderHint(QPainter.Antialiasing)
    g = QLinearGradient(0, 0, w, h)
    g.setColorAt(0, QColor(NAVY))
    g.setColorAt(1, QColor("#0F2A33"))
    p.fillRect(0, 0, w, h, g)
    rg = QRadialGradient(QPointF(w * glow[0], h * glow[1]), max(w, h) * 0.55)
    c = QColor(TEAL)
    c.setAlpha(110)
    rg.setColorAt(0, c)
    c.setAlpha(0)
    rg.setColorAt(1, c)
    p.fillRect(0, 0, w, h, rg)
    # sound waves across the picture
    for k, (col, alpha, amp, freq, phase, ypos) in enumerate([
            (TEAL_LIGHT, 70, 0.10, 2.2, 0.0, 0.62), (AMBER, 55, 0.07, 3.1, 1.3, 0.66),
            (TEAL_LIGHT, 40, 0.13, 1.6, 2.1, 0.58), (WHITE, 25, 0.05, 4.0, 0.7, 0.70)]):
        path = QPainterPath()
        for i in range(0, 401):
            x = w * i / 400
            env = math.sin(math.pi * i / 400) ** 1.5
            y = h * ypos + h * amp * env * math.sin(freq * 2 * math.pi * i / 400 + phase) * \
                (0.6 + 0.4 * math.sin(7 * math.pi * i / 400 + k))
            path.moveTo(x, y) if i == 0 else path.lineTo(x, y)
        col = QColor(col)
        col.setAlpha(alpha)
        p.setPen(QPen(col, max(2.0, h / 260), Qt.SolidLine, Qt.RoundCap))
        p.drawPath(path)
    # faint bubble rings
    for _ in range(14):
        r = rnd.uniform(0.03, 0.09) * min(w, h) * 2
        x, y = rnd.uniform(0, w), rnd.uniform(0, h)
        col = QColor(rnd.choice([TEAL_LIGHT, AMBER, WHITE]))
        col.setAlpha(rnd.randint(14, 30))
        p.setPen(QPen(col, max(2.0, r / 7)))
        p.setBrush(Qt.NoBrush)
        p.drawEllipse(QPointF(x, y), r, r)
    p.end()
    return img


def capsule(w: int, h: int, logo_height_ratio: float = 0.42, mark_only: bool = False, vertical: bool = False,
            seed: int = 7) -> QImage:
    img = backdrop(w, h, seed=seed)
    p = QPainter(img)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    if mark_only:
        s = min(w, h) * 0.6
        draw_svg(p, mark_svg(True), QRectF((w - s) / 2, (h - s) / 2 - h * 0.04, s, s))
    elif vertical:                                      # mark above the wordmark
        s = w * 0.42
        draw_svg(p, mark_svg(True), QRectF((w - s) / 2, h * 0.16, s, s))
        svg, lw, lh = word_only_svg()
        tw = w * 0.82
        th = tw * lh / lw
        draw_svg(p, svg, QRectF((w - tw) / 2, h * 0.16 + s + h * 0.05, tw, th))
    else:
        svg, lw, lh = logo_svg(True)
        th = h * logo_height_ratio
        tw = th * lw / lh
        if tw > w * 0.86:
            tw = w * 0.86
            th = tw * lh / lw
        draw_svg(p, svg, QRectF((w - tw) / 2, (h - th) / 2, tw, th))
    p.end()
    return img


def word_only_svg(dark_bg: bool = True) -> tuple[str, float, float]:
    px = 150
    elo, glo = text_path("Elo", px), text_path("Global", px)
    w_elo = elo.boundingRect().right()
    top = min(elo.boundingRect().top(), glo.boundingRect().top())
    bottom = max(elo.boundingRect().bottom(), glo.boundingRect().bottom())
    c1, c2 = (WHITE, TEAL_LIGHT) if dark_bg else (NAVY2, TEAL)
    d1 = path_to_svg_d(elo, 4, -top + 4)
    d2 = path_to_svg_d(glo, 4 + w_elo + px * 0.02, -top + 4)
    width = 8 + w_elo + px * 0.02 + glo.boundingRect().right()
    height = bottom - top + 8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
            f'viewBox="0 0 {width:.0f} {height:.0f}"><path d="{d1}" fill="{c1}"/><path d="{d2}" fill="{c2}"/></svg>',
            width, height)


def hero(w: int, h: int, seed: int = 11) -> QImage:
    """No text at all (Steam library hero, Microsoft super hero art): backdrop + big linked bubbles in the centre."""
    img = backdrop(w, h, glow=(0.5, 0.42), seed=seed)
    p = QPainter(img)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    s = h * 0.55
    draw_svg(p, mark_svg(False), QRectF((w - s) / 2, h * 0.08, s, s))
    p.end()
    return img


def fit_screenshot(src: Path, w: int, h: int) -> QImage:
    img = QImage(str(src))
    canvas = backdrop(w, h, seed=3)
    p = QPainter(canvas)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    scaled = img.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    p.drawImage((w - scaled.width()) // 2, (h - scaled.height()) // 2, scaled)
    p.end()
    return canvas


# ----------------------------------------------------------------------------------------------- main
def main():
    app = QGuiApplication.instance() or QGuiApplication(sys.argv)  # noqa: F841 - fonts and painting need it
    OUT.mkdir(exist_ok=True)
    src = OUT / "logo"
    src.mkdir(exist_ok=True)
    (src / "eloglobal-icon.svg").write_text(mark_svg(True), encoding="utf-8")
    (src / "eloglobal-mark.svg").write_text(mark_svg(False), encoding="utf-8")
    svg, lw, lh = logo_svg(True)
    (src / "eloglobal-logo-dark-bg.svg").write_text(svg, encoding="utf-8")
    svg_l, _, _ = logo_svg(False)
    (src / "eloglobal-logo-light-bg.svg").write_text(svg_l, encoding="utf-8")

    icon = mark_svg(True)
    # app icon
    sizes = [16, 20, 24, 32, 40, 48, 64, 96, 128, 256]
    write_ico([render(icon, s, s) for s in sizes], OUT / "icon.ico")
    save(render(icon, 256, 256), "icon.png")
    save(render(icon, 512, 512), "logo/eloglobal-icon-512.png")
    save(render(svg, int(lw * 2), int(lh * 2)), "logo/eloglobal-logo-dark-bg.png")
    save(render(svg_l, int(lw * 2), int(lh * 2)), "logo/eloglobal-logo-light-bg.png")

    # Steam
    save(capsule(920, 430), "steam/store/header_capsule_920x430.png")
    save(capsule(462, 174, 0.62), "steam/store/small_capsule_462x174.png")
    save(capsule(1232, 706, 0.34, seed=5), "steam/store/main_capsule_1232x706.png")
    save(capsule(748, 896, vertical=True, seed=9), "steam/store/vertical_capsule_748x896.png")
    save(backdrop(1438, 810, glow=(0.3, 0.3), seed=4), "steam/store/page_background_1438x810.png")
    save(capsule(600, 900, vertical=True, seed=12), "steam/library/library_capsule_600x900.png")
    save(capsule(920, 430, seed=13), "steam/library/library_header_920x430.png")
    save(hero(3840, 1240), "steam/library/library_hero_3840x1240.png")
    lg = render(svg, 1280, int(1280 * lh / lw))
    canvas = QImage(1280, 720, QImage.Format_ARGB32_Premultiplied)
    canvas.fill(Qt.transparent)
    p = QPainter(canvas)
    p.drawImage(0, (720 - lg.height()) // 2, lg)
    p.end()
    save(canvas, "steam/library/library_logo_1280x720.png")
    (OUT / "steam/icons").mkdir(parents=True, exist_ok=True)
    write_ico([render(icon, s, s) for s in (16, 32, 48, 256)], OUT / "steam/icons/shortcut_icon_256.ico")
    save(render(icon, 512, 512), "steam/icons/shortcut_icon_512.png")
    save(render(icon, 184, 184, bg=TEAL_DARK), "steam/icons/app_icon_184.jpg", "JPG")

    # Microsoft Store listing
    save(render(icon, 300, 300), "msstore/listing/app_tile_icon_300x300.png")
    save(capsule(1080, 1080, vertical=True, seed=21), "msstore/listing/box_art_1080x1080.png")
    save(capsule(720, 1080, vertical=True, seed=22), "msstore/listing/poster_art_720x1080.png")
    save(hero(1920, 1080, seed=23), "msstore/listing/super_hero_art_1920x1080.png")

    # MSIX package logos (Assets\ in the package)
    scales = {100: 1, 125: 1.25, 150: 1.5, 200: 2, 400: 4}
    for name, (bw, bh) in {"Square44x44Logo": (44, 44), "Square150x150Logo": (150, 150),
                           "Square71x71Logo": (71, 71), "Square310x310Logo": (310, 310), "StoreLogo": (50, 50),
                           "Wide310x150Logo": (310, 150), "SplashScreen": (620, 300)}.items():
        for sc, f in scales.items():
            w, h = round(bw * f), round(bh * f)
            if w == h:
                img = render(icon, w, h) if name in ("Square44x44Logo", "StoreLogo") else \
                    _tile(icon, w, h, 0.66)
            else:
                img = _wide(w, h)
            save(img, f"msstore/package/{name}.scale-{sc}.png")
    for t in (16, 24, 32, 48, 256):
        save(render(icon, t, t), f"msstore/package/Square44x44Logo.targetsize-{t}.png")
        save(render(icon, t, t), f"msstore/package/Square44x44Logo.targetsize-{t}_altform-unplated.png")

    # screenshots (taken from the running app: main.py --smoke 5 --shots <folder>)
    if "--screenshots" in sys.argv:
        shots = Path(sys.argv[sys.argv.index("--screenshots") + 1])
        for i, f in enumerate(sorted(shots.glob("*.png"))):
            img = QImage(str(f))
            if img.width() == 1920 and img.height() == 1080:
                save(img, f"screenshots/{f.name}")
            else:
                save(fit_screenshot(f, 1920, 1080), f"screenshots/{f.name}")
    print("assets written to", OUT)


def _tile(icon: str, w: int, h: int, ratio: float) -> QImage:
    """MSIX tiles: transparent, the icon centred at `ratio` of the tile."""
    img = QImage(w, h, QImage.Format_ARGB32_Premultiplied)
    img.fill(Qt.transparent)
    p = QPainter(img)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    s = min(w, h) * ratio
    draw_svg(p, icon, QRectF((w - s) / 2, (h - s) / 2, s, s))
    p.end()
    return img


def _wide(w: int, h: int) -> QImage:
    """Wide tile / splash screen: the full logo centred on a transparent background."""
    svg, lw, lh = logo_svg(True)
    img = QImage(w, h, QImage.Format_ARGB32_Premultiplied)
    img.fill(Qt.transparent)
    p = QPainter(img)
    p.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
    tw = w * 0.8
    th = tw * lh / lw
    draw_svg(p, svg, QRectF((w - tw) / 2, (h - th) / 2, tw, th))
    p.end()
    return img


if __name__ == "__main__":
    main()
    _ = QBrush  # noqa: F841 (kept for experiments with fills)
