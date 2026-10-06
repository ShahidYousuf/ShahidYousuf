"""Generate the profile banners: wide and compact (phone) variants, light and dark. Run: python3 make_banners.py"""

FONT = "Inter, -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    "light": dict(bg="#F8FAFC", grid="#E2E8F0", ink="#0F172A", sub="#475569", teal="#0F766E", glow="#CCFBF1"),
    "dark": dict(bg="#0B1120", grid="#1E293B", ink="#F8FAFC", sub="#94A3B8", teal="#2DD4BF", glow="#134E4A"),
}
TAGLINE = [
    "Senior Software Engineer building secure, scalable web applications,",
    "AI solutions and cloud infrastructure for businesses worldwide.",
]
TAGLINE_COMPACT = [
    "Senior Software Engineer building secure,",
    "scalable web applications, AI solutions",
    "and cloud infrastructure for businesses",
    "worldwide.",
]


def svg(theme: str, compact: bool) -> str:
    t = THEMES[theme]
    w, h = (640, 330) if compact else (1200, 260)
    name_size, name_y = (52, 100) if compact else (64, 128)
    sub_size, sub_y, sub_gap = (25, 152, 34) if compact else (24, 182, 32)
    lines = TAGLINE_COMPACT if compact else TAGLINE
    tagline = "\n".join(
        f'  <text x="42" y="{sub_y + i * sub_gap}" font-family="{FONT}" font-size="{sub_size}" fill="{t["sub"]}">{line}</text>'
        for i, line in enumerate(lines)
    )
    x = 40 if compact else 64
    domain = (
        f'<circle cx="{w - 222}" cy="44" r="6" fill="{t["teal"]}"/>'
        f'<text x="{w - 40}" y="50" text-anchor="end" font-family="{FONT}" font-size="18" fill="{t["sub"]}">shahidyousuf.com</text>'
    )
    if not compact:
        tagline = tagline.replace('x="42"', 'x="66"')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Shahid Yousuf, Senior Software Engineer">
  <defs>
    <pattern id="g" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{t["grid"]}" stroke-width="1"/></pattern>
    <radialGradient id="r" cx="85%" cy="10%" r="60%"><stop offset="0" stop-color="{t["glow"]}" stop-opacity="0.9"/><stop offset="1" stop-color="{t["bg"]}" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="{w}" height="{h}" rx="20" fill="{t["bg"]}"/>
  <rect width="{w}" height="{h}" rx="20" fill="url(#g)" opacity="0.7"/>
  <rect width="{w}" height="{h}" rx="20" fill="url(#r)"/>
  <text x="{x}" y="{name_y}" font-family="{FONT}" font-size="{name_size}" font-weight="700" letter-spacing="-2" fill="{t["ink"]}"><tspan fill="{t["teal"]}" font-weight="500">&lt;</tspan>ShahidYousuf<tspan fill="{t["teal"]}" font-weight="500" dx="12">/&gt;</tspan></text>
{tagline}
  {domain}
</svg>
"""


if __name__ == "__main__":
    for theme in THEMES:
        for compact, suffix in ((False, ""), (True, "-compact")):
            with open(f"banner-{theme}{suffix}.svg", "w", encoding="utf-8") as f:
                f.write(svg(theme, compact))
