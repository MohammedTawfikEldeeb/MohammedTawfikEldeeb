from pathlib import Path
import urllib.request
from PIL import Image, ImageOps

USERNAME = "MohammedTawfikEldeeb"
AVATAR_URL = f"https://github.com/{USERNAME}.png?size=512"

# Terminal characters are taller than they are wide.
# A wider grid keeps the face proportions correct.
COLS = 70
ROWS = 44

# Dense -> light character ramp.
CHARS = "@#8&o:*. "


def get_avatar():
    data = urllib.request.urlopen(AVATAR_URL, timeout=30).read()
    Path("avatar.png").write_bytes(data)


def build_ascii():
    get_avatar()

    image = Image.open("avatar.png").convert("RGB")
    image = ImageOps.fit(
        image,
        (COLS, ROWS),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )

    result = []

    for y in range(ROWS):
        row = []

        for x in range(COLS):
            r, g, b = image.getpixel((x, y))

            # Perceived brightness.
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b

            index = min(
                len(CHARS) - 1,
                int(brightness / 256 * len(CHARS))
            )

            row.append((CHARS[index], r, g, b))

        result.append(row)

    return result


def escape(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def create_svg(dark=False):
    bg = "#0b0f14" if dark else "#ffffff"
    card = "#111820" if dark else "#f6f8fa"
    text = "#f0f6fc" if dark else "#24292f"
    muted = "#8b949e" if dark else "#57606a"
    blue = "#58a6ff" if dark else "#0969da"
    green = "#3fb950" if dark else "#1a7f37"
    border = "#30363d" if dark else "#d0d7de"

    face = build_ascii()

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760">',
        f'<rect width="1200" height="760" rx="28" fill="{bg}"/>',
        f'<rect x="20" y="20" width="1160" height="720" rx="25" fill="none" stroke="{border}" stroke-width="2"/>',

        # Terminal bar
        f'<rect x="48" y="48" width="1104" height="48" rx="13" fill="{card}"/>',
        '<circle cx="75" cy="72" r="6" fill="#ff5f56"/>',
        '<circle cx="98" cy="72" r="6" fill="#ffbd2e"/>',
        '<circle cx="121" cy="72" r="6" fill="#27c93f"/>',
        f'<text x="150" y="78" font-family="monospace" font-size="14" fill="{muted}">mohamed@ai-engineer:~$ ./profile</text>',
        f'<text x="950" y="78" font-family="monospace" font-size="13" fill="{green}">AI + SOFTWARE</text>',

        f'<text x="68" y="145" font-family="Arial,sans-serif" font-size="42" font-weight="700" fill="{text}">Mohamed Tawfik</text>',
        f'<text x="68" y="179" font-family="Arial,sans-serif" font-size="19" fill="{blue}">AI Engineer &amp; Software Engineer</text>',
        f'<text x="68" y="207" font-family="Arial,sans-serif" font-size="15" fill="{muted}">Generative AI · Agentic Systems · Retrieval · Backend Engineering</text>',

        # Portrait card
        f'<rect x="55" y="235" width="535" height="455" rx="20" fill="{card}" stroke="{border}"/>',
        f'<text x="82" y="270" font-family="monospace" font-size="14" fill="{green}">~/identity/ascii_portrait</text>',
    ]

    # The portrait deliberately has more columns than rows.
    # This compensates for terminal glyph aspect ratio.
    x0 = 80
    y0 = 302
    char_width = 7.05
    char_height = 8.15

    for y, row in enumerate(face):
        for x, (char, r, g, b) in enumerate(row):
            # Slightly lift dark colors so facial details remain visible.
            rr = min(255, int(r * 0.90 + 12))
            gg = min(255, int(g * 0.90 + 12))
            bb = min(255, int(b * 0.90 + 12))

            out.append(
                f'<text x="{x0 + x * char_width:.2f}" '
                f'y="{y0 + y * char_height:.2f}" '
                f'font-family="monospace" font-size="8.4" '
                f'font-weight="700" '
                f'fill="rgb({rr},{gg},{bb})">{escape(char)}</text>'
            )

    # Right panel
    out.extend([
        f'<text x="630" y="270" font-family="Arial,sans-serif" font-size="23" font-weight="700" fill="{text}">What I Build</text>',
        f'<line x1="630" y1="285" x2="1120" y2="285" stroke="{border}"/>',

        f'<text x="630" y="320" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{blue}">AGENTIC AI</text>',
        f'<text x="630" y="344" font-family="Arial,sans-serif" font-size="14" fill="{text}">LangGraph · LangChain · MCP · Tool Calling</text>',
        f'<text x="630" y="365" font-family="Arial,sans-serif" font-size="14" fill="{text}">Memory · State · Human Approval</text>',

        f'<text x="630" y="405" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{blue}">RETRIEVAL &amp; RAG</text>',
        f'<text x="630" y="429" font-family="Arial,sans-serif" font-size="14" fill="{text}">Dense · BM25 · RRF · Qdrant · PGVector</text>',
        f'<text x="630" y="450" font-family="Arial,sans-serif" font-size="14" fill="{text}">Cross-Encoder · Semantic Search · Caching</text>',

        f'<text x="630" y="490" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{blue}">SOFTWARE ENGINEERING</text>',
        f'<text x="630" y="514" font-family="Arial,sans-serif" font-size="14" fill="{text}">FastAPI · Flask · Node.js · Express.js</text>',
        f'<text x="630" y="535" font-family="Arial,sans-serif" font-size="14" fill="{text}">JavaScript · TypeScript · REST · WebSockets</text>',

        f'<text x="630" y="575" font-family="Arial,sans-serif" font-size="15" font-weight="700" fill="{blue}">PRODUCTION &amp; MLOPS</text>',
        f'<text x="630" y="599" font-family="Arial,sans-serif" font-size="14" fill="{text}">Docker · AWS · SageMaker · GitHub Actions</text>',
        f'<text x="630" y="620" font-family="Arial,sans-serif" font-size="14" fill="{text}">MLflow · DVC · ZenML · Observability</text>',

        f'<text x="630" y="660" font-family="monospace" font-size="13" fill="{muted}">github.com/{USERNAME}</text>',
        '</svg>'
    ])

    return "\n".join(out)


Path("light_mode.svg").write_text(create_svg(False), encoding="utf-8")
Path("dark_mode.svg").write_text(create_svg(True), encoding="utf-8")
