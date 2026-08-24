from pathlib import Path
import urllib.request
from PIL import Image, ImageOps

USERNAME = "MohammedTawfikEldeeb"
AVATAR_URL = f"https://github.com/{USERNAME}.png?size=512"
CHARS = " .:-=+*#%@"
WIDTH, HEIGHT = 42, 42

def make_ascii():
    raw = urllib.request.urlopen(AVATAR_URL, timeout=30).read()
    Path("avatar.png").write_bytes(raw)
    img = Image.open("avatar.png").convert("L")
    img = ImageOps.fit(img, (WIDTH, HEIGHT))
    px = img.load()
    lines = []
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            v = px[x, y]
            idx = min(len(CHARS) - 1, v * len(CHARS) // 256)
            line += CHARS[idx]
        lines.append(line)
    return lines

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def make_svg(dark=False):
    bg = "#0d1117" if dark else "#ffffff"
    fg = "#f0f6fc" if dark else "#111827"
    muted = "#8b949e" if dark else "#4b5563"
    accent = "#58a6ff" if dark else "#0969da"
    border = "#30363d" if dark else "#d0d7de"

    art = make_ascii()
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">',
        f'<rect width="1200" height="900" rx="28" fill="{bg}"/>',
        f'<rect x="22" y="22" width="1156" height="856" rx="22" fill="none" stroke="{border}" stroke-width="2"/>',
        f'<text x="70" y="105" font-family="monospace" font-size="44" font-weight="700" fill="{fg}">Mohamed Tawfik</text>',
        f'<text x="70" y="145" font-family="Arial,sans-serif" font-size="22" fill="{accent}">AI Engineer · Agentic AI · Generative AI</text>',
        f'<text x="70" y="190" font-family="Arial,sans-serif" font-size="17" fill="{muted}">Production AI systems, agents, RAG pipelines and LLM-powered workflows.</text>',
        f'<line x1="70" y1="220" x2="1130" y2="220" stroke="{border}"/>',
        f'<text x="70" y="270" font-family="monospace" font-size="18" fill="{accent}">PROFILE_ASCII</text>',
    ]

    for i, line in enumerate(art):
        out.append(f'<text x="70" y="{305+i*11}" font-family="monospace" font-size="11" xml:space="preserve" fill="{fg}">{esc(line)}</text>')

    x, y = 610, 290
    items = [
        ("FOCUS", "Multi-agent systems · LangGraph · MCP"),
        ("RAG", "Hybrid retrieval · Qdrant · re-ranking"),
        ("AI", "Machine Learning · Deep Learning · NLP"),
        ("BACKEND", "FastAPI · PostgreSQL · Redis"),
        ("DEPLOY", "Docker · AWS · production AI"),
    ]
    for title, value in items:
        out.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="{accent}">{title}</text>')
        out.append(f'<text x="{x}" y="{y+27}" font-family="Arial,sans-serif" font-size="16" fill="{fg}">{esc(value)}</text>')
        y += 82

    out += [
        f'<text x="610" y="720" font-family="Arial,sans-serif" font-size="17" font-weight="700" fill="{accent}">FEATURED WORK</text>',
        f'<text x="610" y="750" font-family="Arial,sans-serif" font-size="15" fill="{fg}">Hakeem · AI medical &amp; booking agent</text>',
        f'<text x="610" y="778" font-family="Arial,sans-serif" font-size="15" fill="{fg}">Conversational commerce · MENA e-commerce</text>',
        f'<text x="610" y="806" font-family="Arial,sans-serif" font-size="15" fill="{fg}">RAG systems · search · evaluation · automation</text>',
        f'<text x="70" y="850" font-family="monospace" font-size="14" fill="{muted}">github.com/MohammedTawfikEldeeb</text>',
        '</svg>'
    ]
    return "\n".join(out)

Path("light_mode.svg").write_text(make_svg(False), encoding="utf-8")
Path("dark_mode.svg").write_text(make_svg(True), encoding="utf-8")
