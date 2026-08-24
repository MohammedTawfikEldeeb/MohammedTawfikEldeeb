from pathlib import Path
import urllib.request
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

USERNAME = "MohammedTawfikEldeeb"
AVATAR_URL = f"https://github.com/{USERNAME}.png?size=512"

# Mosaic grid resolution — square cells, so no aspect-ratio compensation needed.
GRID = 46          # 46x46 color cells
CELL = 9.4          # px size of each cell in the final SVG
GAP = 1.1           # px gap between cells (creates the "pixel mosaic" look)
CORNER = 2.2         # rounded corner radius of each cell


def get_avatar():
    req = urllib.request.Request(AVATAR_URL, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=30).read()
    Path("avatar.png").write_bytes(data)


def build_mosaic():
    get_avatar()

    image = Image.open("avatar.png").convert("RGB")
    image = ImageOps.fit(
        image,
        (GRID, GRID),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )

    # Slight contrast/saturation boost so the mosaic reads clearly at small size.
    image = ImageEnhance.Contrast(image).enhance(1.12)
    image = ImageEnhance.Color(image).enhance(1.15)

    pixels = []
    for y in range(GRID):
        row = []
        for x in range(GRID):
            r, g, b = image.getpixel((x, y))
            row.append((r, g, b))
        pixels.append(row)
    return pixels


def escape(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def create_svg(dark=False):
    bg = "#0d1117" if dark else "#ffffff"
    card = "#0d1117" if dark else "#ffffff"
    text = "#f0f6fc" if dark else "#1b1f24"
    muted = "#8b949e" if dark else "#59636e"
    blue = "#58a6ff" if dark else "#0969da"
    green = "#3fb950" if dark else "#1a7f37"
    border = "#21262d" if dark else "#e6e9ec"
    accent_bg = "#161b22" if dark else "#f6f8fa"

    pixels = build_mosaic()

    W, H = 1200, 720
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect width="{W}" height="{H}" fill="{bg}"/>',

        # top hairline bar — flat, no drop shadows, no skeuomorphic card
        f'<circle cx="46" cy="40" r="5" fill="#ff5f56"/>',
        f'<circle cx="66" cy="40" r="5" fill="#ffbd2e"/>',
        f'<circle cx="86" cy="40" r="5" fill="#27c93f"/>',
        f'<text x="112" y="45" font-family="monospace" font-size="13" fill="{muted}">mohamed@ai-engineer:~$ ./profile</text>',
        f'<text x="{W-52}" y="45" text-anchor="end" font-family="monospace" font-size="12" font-weight="700" fill="{green}">AI + SOFTWARE</text>',
        f'<line x1="0" y1="66" x2="{W}" y2="66" stroke="{border}" stroke-width="1"/>',

        f'<text x="52" y="128" font-family="Arial,sans-serif" font-size="40" font-weight="800" fill="{text}">Mohamed Tawfik</text>',
        f'<text x="52" y="160" font-family="Arial,sans-serif" font-size="18" font-weight="600" fill="{blue}">AI Engineer &amp; Software Engineer</text>',
        f'<text x="52" y="186" font-family="Arial,sans-serif" font-size="14" fill="{muted}">Generative AI · Agentic Systems · Retrieval · Backend Engineering</text>',
    ]

    # ---- Mosaic portrait + skills panel, vertically centered together ----
    mosaic_size = GRID * (CELL + GAP)
    section_top = 220

    out.append(f'<line x1="0" y1="{section_top-30}" x2="{W}" y2="{section_top-30}" stroke="{border}" stroke-width="1"/>')

    mosaic_x0 = 52
    panel_x = mosaic_x0 + mosaic_size + 60
    panel_w = W - panel_x - 52

    sections = [
        ("AGENTIC AI", ["LangGraph · LangChain · MCP · Tool Calling", "Memory · State · Human Approval"]),
        ("RETRIEVAL & RAG", ["Dense · BM25 · RRF · Qdrant · PGVector", "Cross-Encoder · Semantic Search · Caching"]),
        ("SOFTWARE ENGINEERING", ["FastAPI · Flask · Node.js · Express.js", "JavaScript · TypeScript · REST · WebSockets"]),
        ("PRODUCTION & MLOPS", ["Docker · AWS · SageMaker · GitHub Actions", "MLflow · DVC · ZenML · Observability"]),
    ]

    # Height of the text block: title line + rule + (per-section: title + N lines + gap)
    text_h = 40  # "What I Build" title + rule
    for _, lines in sections:
        text_h += 24 + len(lines) * 22 + 16

    row_h = max(mosaic_size, text_h)
    mosaic_y0 = section_top + (row_h - mosaic_size) / 2
    text_y0 = section_top + (row_h - text_h) / 2

    out.append(f'<text x="{mosaic_x0}" y="{mosaic_y0-16}" font-family="monospace" font-size="13" fill="{green}">~/identity/portrait.mosaic</text>')

    for y, row in enumerate(pixels):
        for x, (r, g, b) in enumerate(row):
            px = mosaic_x0 + x * (CELL + GAP)
            py = mosaic_y0 + y * (CELL + GAP)
            out.append(
                f'<rect x="{px:.1f}" y="{py:.1f}" width="{CELL}" height="{CELL}" '
                f'rx="{CORNER}" fill="rgb({r},{g},{b})"/>'
            )

    out.append(f'<text x="{panel_x}" y="{text_y0+18}" font-family="Arial,sans-serif" font-size="22" font-weight="800" fill="{text}">What I Build</text>')
    out.append(f'<line x1="{panel_x}" y1="{text_y0+34}" x2="{panel_x+panel_w}" y2="{text_y0+34}" stroke="{border}"/>')

    sy = text_y0 + 70
    for title, lines in sections:
        out.append(f'<text x="{panel_x}" y="{sy}" font-family="Arial,sans-serif" font-size="14" font-weight="800" fill="{blue}" letter-spacing="0.5">{escape(title)}</text>')
        sy += 24
        for line in lines:
            out.append(f'<text x="{panel_x}" y="{sy}" font-family="Arial,sans-serif" font-size="14" fill="{text}">{escape(line)}</text>')
            sy += 22
        sy += 16

    out.append(f'<text x="{mosaic_x0}" y="{section_top+row_h+34}" font-family="monospace" font-size="12" fill="{muted}">github.com/{USERNAME}</text>')

    out.append('</svg>')
    return "\n".join(out)


if __name__ == "__main__":
    Path("light_mode.svg").write_text(create_svg(False), encoding="utf-8")
    Path("dark_mode.svg").write_text(create_svg(True), encoding="utf-8")
