#!/usr/bin/env python3
"""Build original, self-contained editorial SVGs; no network or dependencies."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    "dark": ("#0B1120", "#101D32", "#263B55", "#F8FAFC", "#B8C5D6", "#22D3EE"),
    "light": ("#F8FAFC", "#FFFFFF", "#CBD5E1", "#0B1120", "#475569", "#1D4ED8"),
}


class Drawing:
    def __init__(self, width, height, theme, title, description):
        self.bg, self.panel, self.line, self.fg, self.muted, self.accent = PALETTES[theme]
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>']
        self.rect(1, 1, width-2, height-2, self.bg, self.line, 16)

    def rect(self, x, y, width, height, fill=None, stroke=None, radius=10):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill or self.panel}" stroke="{stroke or self.line}" stroke-width="1.5"/>')

    def text(self, x, y, text, size=22, color=None, weight=400):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color or self.fg}">{escape(text)}</text>')

    def path(self, data, color=None, width=1.5):
        self.parts.append(f'<path d="{data}" fill="none" stroke="{color or self.line}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')

    def dot(self, x, y, radius=3, color=None):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color or self.accent}"/>')

    def save(self, path):
        destination = ROOT / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text("\n".join(self.parts + ["</svg>"]) + "\n")


def projects(theme):
    d = Drawing(680, 260, theme, "Facteo / Business operations",
                "Concept illustration, not a screenshot: billing records, financial indicators and customer management.")
    d.text(28, 37, "01 / BUSINESS OPERATIONS", 18, d.muted, 700)
    d.rect(28, 58, 410, 174)
    d.path("M28 94H438")
    d.dot(47, 76, 3); d.dot(59, 76, 3, d.line); d.dot(71, 76, 3, d.line)
    d.rect(46, 111, 110, 45, d.bg); d.rect(167, 111, 110, 45, d.bg)
    d.path("M60 139H79V124H89V139H111V120H126", d.accent, 2)
    d.path("M182 139L199 128L215 133L238 119L259 123", d.accent, 2)
    for y, length in [(177, 150), (195, 198), (213, 126)]:
        d.path(f"M47 {y}H{47+length}", d.line, 4)
        d.dot(400, y, 3)
    d.rect(461, 58, 191, 174)
    d.path("M484 126V79H586L607 100V126M586 79V100H607", d.accent, 2)
    d.path("M495 103H551M495 116H570")
    for x in (490, 526, 562):
        d.dot(x, 161, 7, d.muted)
        d.path(f"M{x-11} 188V183Q{x} 169 {x+11} 183V188", d.muted, 2)
    d.text(484, 216, "CLIENTS / INVOICES", 15, d.muted)
    d.save(f"assets/projects/facteo-{theme}.svg")

    d = Drawing(680, 260, theme, "QuizLy / Learning loop",
                "Concept illustration, not a screenshot: a question card connects to generation, evaluation and explanation modules.")
    d.text(28, 37, "02 / LEARNING SYSTEMS", 18, d.muted, 700)
    d.rect(28, 58, 245, 174)
    d.text(48, 99, "?", 32, d.accent, 700)
    d.path("M88 82H245M88 98H210")
    for y, width in [(126, 156), (158, 116), (190, 140)]:
        d.rect(48, y, 20, 20, d.bg, d.accent if y == 158 else d.line, 5)
        d.path(f"M84 {y+10}H{84+width}", d.accent if y == 158 else d.line, 4)
    d.path("M273 145H317V86H350M317 145H350M317 145V204H350", d.accent)
    for y, name, number in [(62, "GENERATE", "01"), (121, "EVALUATE", "02"), (180, "EXPLAIN", "03")]:
        d.rect(350, y, 240, 48)
        d.text(366, y+30, number, 16, d.accent, 700)
        d.text(408, y+31, name, 20, d.fg, 700)
    d.path("M590 86H625V204H590")
    d.dot(317, 145, 4); d.dot(625, 145, 4, "#8B5CF6")
    d.save(f"assets/projects/quizly-{theme}.svg")


def stack(theme):
    d = Drawing(440, 554, theme, "Engineering stack / Technical domains",
                "Interfaces, APIs, business logic, data and infrastructure. A map of technical interests and practice, not equal proficiency or a specific project's architecture.")
    d.text(24, 36, "FROM INTERFACE TO DELIVERY", 18, d.muted, 700)
    layers = [
        ("INTERFACES", "React • React Native • Expo"),
        ("APPLICATION / API", "Django • DRF • REST APIs"),
        ("BUSINESS LOGIC", "Services • Celery tasks"),
        ("DATA", "PostgreSQL • MySQL • Redis"),
        ("INFRASTRUCTURE", "Linux • Docker • Nginx • CI/CD"),
    ]
    icons = ["M0 0H26V20H0ZM7 25H19M13 20V25",
             "M4 2L0 12L4 22M22 2L26 12L22 22M16 0L10 24",
             "M0 4H20V12H0ZM6 17H26V25H6ZM5 0V4M21 25V29",
             "M0 5C0 -2 26 -2 26 5V23C26 30 0 30 0 23ZM0 5C0 12 26 12 26 5M0 14C0 21 26 21 26 14",
             "M0 0H26V10H0ZM0 17H26V27H0ZM5 5H8M5 22H8"]
    for i, (label, technologies) in enumerate(layers):
        y = 54 + i * 100
        d.rect(20, y, 400, 78, stroke=d.accent if i == 1 else d.line)
        d.parts.append(f'<g transform="translate(36 {y+24})">')
        d.path(icons[i], d.accent, 1.8)
        d.parts.append("</g>")
        d.text(82, y+27, label, 18, d.muted, 700)
        d.text(82, y+57, technologies, 21, d.fg)
        if i < 4:
            d.path(f"M220 {y+79}V{y+97}M216 {y+93}L220 {y+97}L224 {y+93}", d.accent)
    d.save(f"assets/branding/stack-{theme}.svg")


def approach(theme, mobile):
    steps = ["Problem", "Analysis", "Architecture", "Implementation", "Testing", "Deployment"]
    d = Drawing(440 if mobile else 960, 378 if mobile else 184, theme,
                "Engineering approach", "Problem → Analysis → Architecture → Implementation → Testing → Deployment.")
    d.text(24, 36, "UNDERSTAND / DESIGN / DELIVER", 18, d.muted, 700)
    for i, step in enumerate(steps):
        x = 24 if mobile else 24+i*154
        y = 56+i*51 if mobile else 64
        d.rect(x, y, 392 if mobile else 142, 42 if mobile else 92)
        d.text(x+14, y+28, f"0{i+1}", 18, d.accent, 700)
        d.text(x+64 if mobile else x+14, y+28 if mobile else y+65,
               step, 23 if mobile else 16, d.fg, 700)
        if i < 5:
            if mobile:
                d.path(f"M{220} {y+43}V{y+50}", d.accent)
            else:
                d.path(f"M{x+143} {y+46}H{x+153}", d.accent)
    d.save(f"assets/branding/approach-{'mobile-' if mobile else ''}{theme}.svg")


def main():
    for theme in PALETTES:
        projects(theme)
        stack(theme)
        approach(theme, False)
        approach(theme, True)
    print("Built 10 themed project illustrations and engineering infographics")


if __name__ == "__main__":
    main()
