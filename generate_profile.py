from pathlib import Path
import urllib.request
from PIL import Image, ImageOps

USERNAME = "MohammedTawfikEldeeb"
AVATAR_URL = f"https://github.com/{USERNAME}.png?size=512"

# Character ramp: darker pixels use denser characters.
CHARS = " .,:;irsXA253hMHGS#9B&@"
W, H = 46, 42


def download_avatar():
    data = urllib.request.urlopen(AVATAR_URL, timeout=30).read()
    Path("avatar.png").write_bytes(data)


def make_ascii():
    download_avatar()
    img = Image.open("avatar.png").convert("RGB")
    # Crop to a square so the face keeps its proportions.
    img = ImageOps.fit(img, (W, H), method=Image.Resampling.LANCZOS)

    lines = []
    for y in range(H):
        row = []
        for x in range(W):
            r, g, b = img.getpixel((x, y))
            lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
            idx = min(len(CHARS) - 1, int(lum / 256 * len(CHARS)))
            row.append((CHARS[idx], r, g, b))
        lines.append(row)
    return lines


def esc(value):
    return (str(value).replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


def make_svg(dark=False):
    bg = "#0b0f14" if dark else "#ffffff"
    panel = "#111820" if dark else "#f6f8fa"
    fg = "#f0f6fc" if dark else "#17202a"
    muted = "#8b949e" if dark else "#57606a"
    accent = "#58a6ff" if dark else "#0969da"
    green = "#3fb950" if dark else "#1a7f37"
    border = "#30363d" if dark else "#d0d7de"

    ascii_art = make_ascii()

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="980" viewBox="0 0 1200 980">',
        f'<rect width="1200" height="980" rx="30" fill="{bg}"/>',
        f'<rect x="24" y="24" width="1152" height="932" rx="26" fill="none" stroke="{border}" stroke-width="2"/>',

        # Terminal-style top bar
        f'<rect x="52" y="52" width="1096" height="48" rx="14" fill="{panel}"/>',
        '<circle cx="78" cy="76" r="6" fill="#ff5f56"/>',
        '<circle cx="100" cy="76" r="6" fill="#ffbd2e"/>',
        '<circle cx="122" cy="76" r="6" fill="#27c93f"/>',
        f'<text x="150" y="82" font-family="monospace" font-size="15" fill="{muted}">mohamed@ai-engineer:~$ ./profile</text>',

        f'<text x="70" y="155" font-family="Arial,sans-serif" font-size="43" font-weight="700" fill="{fg}">Mohamed Tawfik</text>',
        f'<text x="70" y="190" font-family="Arial,sans-serif" font-size="20" fill="{accent}">AI Engineer  ·  Generative AI  ·  Agentic Systems  ·  RAG</text>',
        f'<text x="70" y="222" font-family="Arial,sans-serif" font-size="16" fill="{muted}">Building production-oriented AI applications, intelligent agents and retrieval systems.</text>',

        # Left profile card
        f'<rect x="60" y="260" width="520" height="560" rx="22" fill="{panel}" stroke="{border}"/>',
        f'<text x="90" y="300" font-family="monospace" font-size="16" fill="{green}">~/identity/ascii_portrait</text>',
    ]

    # Colored ASCII portrait
    start_x, start_y = 92, 335
    char_w, char_h = 9.6, 10.5
    for y, row in enumerate(ascii_art):
        for x, (ch, r, g, b) in enumerate(row):
            # Slightly brighten dark text so facial structure remains visible.
            rr = min(255, int(r * 0.95 + 10))
            gg = min(255, int(g * 0.95 + 10))
            bb = min(255, int(b * 0.95 + 10))
            out.append(
                f'<text x="{start_x + x*char_w:.1f}" y="{start_y + y*char_h:.1f}" '
                f'font-family="monospace" font-size="11" font-weight="700" '
                f'fill="rgb({rr},{gg},{bb})">{esc(ch)}</text>'
            )

    out += [
        f'<text x="90" y="785" font-family="monospace" font-size="14" fill="{muted}">github.com/{USERNAME}</text>',

        # Right content
        f'<text x="625" y="300" font-family="Arial,sans-serif" font-size="23" font-weight="700" fill="{fg}">What I Build</text>',
        f'<line x1="625" y1="315" x2="1120" y2="315" stroke="{border}"/>',

        f'<text x="625" y="350" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="{accent}">🤖 AGENTIC AI</text>',
        f'<text x="625" y="375" font-family="Arial,sans-serif" font-size="15" fill="{fg}">LangGraph · MCP · tool calling · memory · human approval</text>',

        f'<text x="625" y="420" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="{accent}">🔎 RETRIEVAL &amp; RAG</text>',
        f'<text x="625" y="445" font-family="Arial,sans-serif" font-size="15" fill="{fg}">Dense + BM25 · RRF · Cross-Encoder · Qdrant · PGVector</text>',

        f'<text x="625" y="490" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="{accent}">🧠 ML / DL / LLMs</text>',
        f'<text x="625" y="515" font-family="Arial,sans-serif" font-size="15" fill="{fg}">PyTorch · TensorFlow · Transformers · VLMs · fine-tuning</text>',

        f'<text x="625" y="560" font-family="Arial,sans-serif" font-size="16" font-weight="700" fill="{accent}">⚙️ PRODUCTION</text>',
        f'<text x="625" y="585" font-family="Arial,sans-serif" font-size="15" fill="{fg}">FastAPI · Docker · AWS · SageMaker · CI/CD · LLMOps</text>',

        f'<text x="625" y="635" font-family="Arial,sans-serif" font-size="23" font-weight="700" fill="{fg}">Selected Projects</text>',
        f'<line x1="625" y1="650" x2="1120" y2="650" stroke="{border}"/>',

        f'<text x="625" y="685" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{accent}">GitRAG</text>',
        f'<text x="700" y="685" font-family="Arial,sans-serif" font-size="14" fill="{fg}">Code intelligence · citable answers · dependency graphs</text>',

        f'<text x="625" y="720" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{accent}">Hakeem</text>',
        f'<text x="700" y="720" font-family="Arial,sans-serif" font-size="14" fill="{fg}">Arabic medical booking agent · stateful LangGraph</text>',

        f'<text x="625" y="755" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{accent}">Shopify Agent</text>',
        f'<text x="745" y="755" font-family="Arial,sans-serif" font-size="14" fill="{fg}">100+ Egyptian stores · Arabic/English shopping</text>',

        f'<text x="625" y="790" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{accent}">MLOps</text>',
        f'<text x="700" y="790" font-family="Arial,sans-serif" font-size="14" fill="{fg}">SageMaker · DVC · MLflow · drift monitoring</text>',

        # Bottom stats
        f'<rect x="60" y="850" width="1080" height="72" rx="18" fill="{panel}" stroke="{border}"/>',
        f'<text x="90" y="881" font-family="monospace" font-size="14" fill="{muted}">EDUCATION</text>',
        f'<text x="90" y="905" font-family="Arial,sans-serif" font-size="14" fill="{fg}">B.Sc. Computer Engineering · Tanta University · A+ Excellent</text>',
        f'<text x="520" y="881" font-family="monospace" font-size="14" fill="{muted}">LANGUAGES</text>',
        f'<text x="520" y="905" font-family="Arial,sans-serif" font-size="14" fill="{fg}">Arabic — Native · English — Fluent</text>',
        f'<text x="850" y="881" font-family="monospace" font-size="14" fill="{muted}">CONTACT</text>',
        f'<text x="850" y="905" font-family="Arial,sans-serif" font-size="13" fill="{fg}">mohamed.tawfik.eldeeb@gmail.com</text>',

        '</svg>'
    ]
    return "\n".join(out)


Path("light_mode.svg").write_text(make_svg(False), encoding="utf-8")
Path("dark_mode.svg").write_text(make_svg(True), encoding="utf-8")
