"""Shared RochDev V3 SVG composition system. Standard library only."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = {
    "dark": dict(bg="#0B1120", surface="#101C31", raised="#16243A", border="#263A56",
                 fg="#F8FAFC", muted="#94A3B8", accent="#22D3EE", secondary="#2563EB"),
    "light": dict(bg="#F8FAFC", surface="#FFFFFF", raised="#E8EEF7", border="#CBD5E1",
                  fg="#0B1120", muted="#475569", accent="#1D4ED8", secondary="#2563EB"),
}
SPACING = (8, 16, 24, 32, 56, 80)
TYPE = dict(display=88, title=64, heading=32, body=28, meta=24)
ICONS = {
    "discover": "M5 5A11 11 0 1 1 4 6M24 24L34 34",
    "analyze": "M2 32V18H9V32M15 32V8H22V32M28 32V0H35V32",
    "architect": "M12 0H26V12H12ZM0 26H12V38H0ZM26 26H38V38H26ZM19 12V20H6V26M19 20H32V26",
    "build": "M10 3L0 18L10 33M28 3L38 18L28 33M23 0L15 36",
    "validate": "M2 19L14 31L36 4",
    "deliver": "M2 35H36M19 27V0M6 13L19 0L32 13",
    "interfaces": "M0 0H38V26H0ZM10 35H28M19 26V35",
    "data": "M0 6C0 -2 38 -2 38 6V30C38 38 0 38 0 30ZM0 6C0 14 38 14 38 6M0 18C0 26 38 26 38 18",
}


class SVG:
    def __init__(self, width, height, theme, title, description, frame=True):
        self.width, self.height = width, height
        self.c = TOKENS[theme]
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
        ]
        self.rect(1, 1, width-2, height-2, "bg", "border" if frame else "bg", 24)

    def color(self, value):
        return self.c.get(value, value)

    def rect(self, x, y, width, height, fill="surface", stroke="border", radius=16):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{self.color(fill)}" stroke="{self.color(stroke)}" stroke-width="2"/>')

    def text(self, x, y, text, size=28, color="fg", weight=400):
        self.parts.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{self.color(color)}">{escape(str(text))}</text>')

    def line(self, path, color="border", width=2):
        self.parts.append(f'<path d="{path}" fill="none" stroke="{self.color(color)}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')

    def dot(self, x, y, radius=4, color="accent"):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{self.color(color)}"/>')

    def icon(self, name, x, y, scale=1):
        self.parts.append(f'<g transform="translate({x} {y}) scale({scale})">')
        self.line(ICONS[name], "accent", 2.5)
        self.parts.append("</g>")

    def finish(self):
        return "\n".join(self.parts + ["</svg>"]) + "\n"

    def save(self, filename):
        path = ROOT / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.finish(), encoding="utf-8")


def hero(mobile=False):
    d = SVG(480 if mobile else 1200, 320 if mobile else 400, "dark",
            "RochDev / Engineering Ideas Into Reality",
            "Software Engineer, Backend Developer, Builder. A geometric R anchors connected software modules.")
    if mobile:
        d.text(28, 52, "ROCHDEV", 48, weight=700)
        d.text(28, 96, "Engineering Ideas", 27)
        d.text(28, 132, "Into Reality", 27)
        d.text(28, 209, "Software Engineer", 24, "muted")
        d.text(28, 246, "Backend Developer • Builder", 24, "muted")
        d.line("M28 283H452")
        d.line("M28 283H108", "accent", 3)
        x, y, scale = 350, 51, .65
    else:
        d.text(56, 69, "ROCHDEV / SOFTWARE & DIGITAL PRODUCTS", 24, "muted")
        d.text(51, 187, "ROCHDEV", 104, weight=700)
        d.text(56, 250, "Engineering Ideas Into Reality", 38)
        d.text(56, 326, "Software Engineer • Backend Developer • Builder", 28, "muted")
        d.line("M56 365H680")
        d.line("M56 365H168", "accent", 3)
        x, y, scale = 855, 135, 1.15
        d.line("M770 73H825V166H855M1040 81V116H997M998 218H1104V300H1058M782 310H829V246H855")
        for xx, yy in [(748,51),(1018,49),(1036,279),(760,288)]:
            d.rect(xx, yy, 44, 44, "surface")
            d.dot(xx+22, yy+22, 4, "accent" if xx in (748,1036) else "#8B5CF6")
        d.dot(825,166);d.dot(1104,218);d.dot(829,246,4,"#8B5CF6")
    d.parts.append(f'<g transform="translate({x} {y}) scale({scale})">')
    d.rect(0, 0, 126, 126, "surface", "secondary", 24)
    d.line("M35 94V32H65L86 51V65L66 77H35M65 77L89 98", "accent", 7)
    d.parts.append("</g>")
    d.save("assets/branding/banner-mobile.svg" if mobile else "assets/branding/banner.svg")


def facteo_art(d, x, y, mobile):
    d.parts.append(f'<g transform="translate({x} {y})">')
    if mobile:
        d.rect(0,0,252,106)
        d.line("M16 23H168M16 47H122M16 71H148", "muted", 3)
        d.line("M185 86V58H201V32H220V18", "accent", 3)
        d.rect(276,0,144,106)
        d.icon("data",294,20,.7)
        d.line("M294 78H396", "muted",3)
    else:
        d.rect(0,0,540,278)
        d.text(24,39,"BILLING / CONCEPT",22,"muted",700)
        d.line("M0 60H540")
        d.icon("analyze",28,83,1.2)
        d.line("M102 98H230M102 123H188", "muted", 5)
        for yy in (172,209,246):
            d.line(f"M26 {yy}H280", "border", 7)
            d.dot(334,yy,5)
        d.rect(374,84,140,168,"bg")
        d.line("M399 198V111H464L489 136V198M464 111V136H489", "accent",2.5)
        d.line("M412 157H469M412 177H459", "muted",3)
        d.dot(70,300,9,"muted");d.dot(110,300,9,"muted");d.dot(150,300,9,"muted")
        d.text(186,309,"CLIENTS / DOCUMENTS",22,"muted")
    d.parts.append("</g>")


def quiz_art(d, x, y, mobile):
    d.parts.append(f'<g transform="translate({x} {y})">')
    if mobile:
        d.text(4,50,"?",52,"accent",700)
        d.line("M51 38H94V21H121M94 38V76H121", "accent")
        d.rect(121,0,296,44); d.rect(121,62,296,44)
        d.text(138,29,"Question → Evaluate",22)
        d.text(138,91,"Explain → Learn",22)
    else:
        d.rect(0,16,210,268)
        d.text(24,68,"?",48,"accent",700)
        d.line("M76 44H184M76 65H164", "muted",3)
        for yy in (112,166,220):
            d.rect(24,yy,24,24,"bg","accent" if yy==166 else "border",6)
            d.line(f"M65 {yy+12}H181", "accent" if yy==166 else "border",4)
        d.line("M210 150H248V48H280M248 150H280M248 150V252H280","accent")
        for yy,label,num in [(14,"Generate","01"),(116,"Evaluate","02"),(218,"Explain","03")]:
            d.rect(280,yy,260,68)
            d.text(298,yy+43,num,22,"accent",700)
            d.text(344,yy+44,label,28,weight=700)
        d.line("M540 48H554V252H540")
        d.dot(248,150,4,"#8B5CF6")
    d.parts.append("</g>")


def project(name, theme, mobile):
    fact = name == "facteo"
    d = SVG(480 if mobile else 1200,420,theme,
            "Facteo / Business invoicing" if fact else "QuizLy / AI learning experiment",
            "Original conceptual product illustration, not a screenshot. No real financial figures are depicted.")
    title, category = ("Facteo","01 / BUSINESS SOFTWARE") if fact else ("QuizLy","02 / AI LEARNING EXPERIMENT")
    if mobile:
        d.text(28,40,category,20,"muted",700)
        d.text(28,92,title,42,weight=700)
        lines = ["Invoices, clients and documents.", "One business workflow."] if fact else ["Generate questions.", "Evaluate answers. Explain why."]
        for i,line in enumerate(lines): d.text(28,138+i*34,line,24)
        d.text(28,212,"Django / DRF • React • TypeScript" if fact else "Python • FastAPI • LangGraph",22,"muted")
        (facteo_art if fact else quiz_art)(d,28,240,True)
        d.text(28,389,"View public repository →",24,"accent",700)
    else:
        d.text(56,64,category,24,"muted",700)
        d.text(56,143,title,64,weight=700)
        lines = ["Invoicing, without the scatter.", "Clients, suppliers and documents."] if fact else ["Questions that lead to learning.", "Generate. Evaluate. Explain."]
        for i,line in enumerate(lines): d.text(56,201+i*40,line,28)
        d.text(56,296,"Django / DRF • React" if fact else "Python • FastAPI",24,"muted")
        d.text(56,329,"TypeScript • Tailwind CSS" if fact else "LangGraph • LangChain",24,"muted")
        d.text(56,382,"View public repository →",26,"accent",700)
        (facteo_art if fact else quiz_art)(d,604,68,False)
    suffix = f"{'mobile-' if mobile else ''}{theme}"
    d.save(f"assets/projects/{name}-{suffix}.svg")


def stack(theme,mobile):
    d = SVG(480 if mobile else 1200,510 if mobile else 450,theme,"Engineering stack / Technical domains",
            "Product interfaces: React, React Native, Expo, TypeScript. Backend engineering: Python, Django, Django REST Framework and Celery. Data and delivery: PostgreSQL, MySQL, Redis, Linux, Docker and CI/CD. Technical domains, not a single project architecture or equal proficiency.")
    if mobile:
        d.text(28,42,"ENGINEERING / TECHNICAL DOMAINS",20,"muted",700)
        data=[("interfaces","Product interfaces",["React • React Native","Expo • TypeScript"]),
              ("build","Backend engineering",["Python • Django • DRF","Celery • REST APIs"]),
              ("data","Data & delivery",["PostgreSQL • MySQL • Redis","Linux • Docker • CI/CD"])]
        for i,(icon,title,lines) in enumerate(data):
            y=66+i*140
            d.rect(28,y,424,120,stroke="accent" if i==1 else "border")
            d.icon(icon,45,y+21,.65)
            d.text(86,y+38,title,25,weight=700)
            for j,line in enumerate(lines):d.text(45,y+75+j*29,line,23,"muted")
            if i<2:d.line(f"M240 {y+121}V{y+139}","accent")
    else:
        d.text(56,58,"ENGINEERING / TECHNICAL DOMAINS",24,"muted",700)
        for i,(label,title,icon) in enumerate([("PRODUCT","Interfaces","interfaces"),("BACKEND","Engineering","build"),("DATA &","Delivery","data")]):
            x=56+i*373
            d.rect(x,91,342,303,stroke="accent" if i==1 else "border")
            d.text(x+24,137,label,24,"muted",700)
            d.text(x+24,180,title,34,weight=700)
            d.icon(icon,x+273,118,.85)
            if i<2:d.line(f"M{x+343} 247H{x+372}","accent")
        for x,items in [(80,["React","React Native","Expo","TypeScript"]),(453,["Python","Django","Django REST Framework","Celery"])]:
            for j,item in enumerate(items):d.text(x,231+j*45,item,24 if len(item)>20 else 28)
        for j,(left,right) in enumerate([("PostgreSQL","MySQL"),("Redis","Linux"),("Docker","CI/CD")]):
            d.text(826,237+j*58,left,27)
            d.text(1014,237+j*58,right,27)
        d.text(56,430,"Also in practice: JavaScript • Vite • Tailwind CSS • Git • Ubuntu • Nginx",24,"muted")
    d.save(f"assets/branding/stack-{'mobile-' if mobile else ''}{theme}.svg")


def approach(theme,mobile):
    d = SVG(480 if mobile else 1200,360 if mobile else 260,theme,
            "Discover → Analyze → Architect → Build → Validate → Deliver",
            "Understand the need, map constraints, define boundaries, implement, test behavior and release with care.",False)
    steps=[("Discover","Find the need","discover"),("Analyze","Map constraints","analyze"),("Architect","Set boundaries","architect"),("Build","Implement","build"),("Validate","Test behavior","validate"),("Deliver","Release safely","deliver")]
    if mobile:
        for i,(title,subtitle,icon) in enumerate(steps):
            col,row=i%2,i//2
            x,y=28+col*226,26+row*112
            d.text(x,y+23,f"0{i+1}",20,"accent",700)
            d.icon(icon,x+147,y+1,.65)
            d.text(x,y+62,title,27,weight=700)
            d.text(x,y+88,subtitle,20,"muted")
        d.line("M240 24V330")
    else:
        d.line("M80 104H1120","accent")
        for i,(title,subtitle,icon) in enumerate(steps):
            x=56+i*184
            d.icon(icon,x+9,28,.85)
            d.dot(x+24,104,20,"surface")
            d.dot(x+24,104,5,"accent")
            d.text(x+53,78,f"0{i+1}",24,"accent",700)
            d.text(x,168,title,30,weight=700)
            d.text(x,209,subtitle,22,"muted")
    d.save(f"assets/branding/approach-{'mobile-' if mobile else ''}{theme}.svg")


def activity(snapshot, dark, mobile=False):
    """Render the same exact data at two compositions without additional API calls."""
    theme="dark" if dark else "light"
    rows=list(snapshot["language_counts"].items())
    rows.sort(key=lambda row:(row[0]=="Not classified",-row[1],row[0]))
    height=max(400,218+len(rows)*28) if mobile else max(340,112+len(rows)*34)
    d=SVG(480 if mobile else 1200,height,theme,
          "Public GitHub / Repository snapshot",
          f'Updated {snapshot["updated"]} UTC. {snapshot["repositories"]} original public repositories, forks excluded; {snapshot["primary_languages"]} primary languages. Counts by one primary language per repository, not proficiency or code volume.')
    if mobile:
        d.text(28,38,"PUBLIC GITHUB / SNAPSHOT",22,"muted",700)
        d.text(28,94,snapshot["repositories"],44,weight=700)
        d.text(258,94,snapshot["primary_languages"],44,weight=700)
        d.text(28,126,"Original public repos",21,"muted")
        d.text(258,126,"Primary languages",21,"muted")
        d.line("M28 148H452")
        d.text(28,183,"Repositories by primary language",23)
        maximum=max(snapshot["language_counts"].values(),default=1)
        for i,(name,count) in enumerate(rows):
            y=214+i*28
            d.text(28,y,name,21)
            d.rect(203,y-14,197,9,"raised","raised",4)
            d.rect(203,y-14,197*count/maximum,9,"accent","accent",4)
            d.text(428,y,count,21)
        d.text(28,height-18,f'Updated {snapshot["updated"]} UTC · Forks excluded',18,"muted")
    else:
        d.text(56,51,"PUBLIC GITHUB / SNAPSHOT",24,"muted",700)
        d.text(56,131,snapshot["repositories"],64,weight=700)
        d.text(288,131,snapshot["primary_languages"],64,weight=700)
        d.text(56,173,"Original public",26,"muted")
        d.text(56,207,"repositories",26,"muted")
        d.text(288,173,"Primary",26,"muted")
        d.text(288,207,"languages",26,"muted")
        d.line(f"M521 48V{height-60}")
        d.text(565,51,"REPOSITORIES BY PRIMARY LANGUAGE",24,"muted",700)
        maximum=max(snapshot["language_counts"].values(),default=1)
        for i,(name,count) in enumerate(rows):
            y=95+i*34
            d.text(565,y,name,25)
            d.rect(778,y-16,310,12,"raised","raised",6)
            d.rect(778,y-16,310*count/maximum,12,"accent","accent",6)
            d.text(1113,y,count,25)
        d.text(56,height-26,f'Updated {snapshot["updated"]} UTC • Forks excluded',24,"muted")
        d.text(778,height-26,"Details linked below ↘",24,"accent")
    return d.finish()


def main():
    hero();hero(True)
    for theme in TOKENS:
        for mobile in (False,True):
            for name in ("facteo","quizly"):project(name,theme,mobile)
            stack(theme,mobile);approach(theme,mobile)
    print("Built V3 covers, unified project cards, technical landscapes and process timelines")
