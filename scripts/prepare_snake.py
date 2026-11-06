#!/usr/bin/env python3
"""Add accessible metadata and derive a static calendar from Platane's SVG."""
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def prepare(source, updated):
    root = ET.fromstring(source)
    style = root.find(f"{{{NS}}}style")
    if style is None or not style.text:
        raise ValueError("Snake SVG has no stylesheet")
    css = style.text
    variables = dict(re.findall(r"--([a-z0-9]+):([^;}]+)", css))
    fills = dict(re.findall(r"\.c\.([a-z0-9]+)\{fill:var\(--([a-z0-9]+)\)", css))
    grid = [el for el in root if el.tag == f"{{{NS}}}rect"
            and "c" in el.get("class", "").split()]
    if not 350 <= len(grid) <= 378 or "ce" not in variables:
        raise ValueError("Unexpected contribution grid format; keep the last valid image")
    for el in list(root):
        if el.tag in (f"{{{NS}}}title", f"{{{NS}}}desc"):
            root.remove(el)
    root.set("role", "img")
    root.set("aria-labelledby", "title desc")
    title = ET.Element(f"{{{NS}}}title", {"id": "title"})
    title.text = "RochDev's GitHub contribution calendar"
    desc = ET.Element(f"{{{NS}}}desc", {"id": "desc"})
    desc.text = (f"Updated {updated} UTC. Daily contribution levels from GitHub. "
                 "Generated with https://github.com/Platane/snk. "
                 "May include anonymized private activity if enabled on the public profile.")
    root.insert(0, title)
    root.insert(1, desc)
    # Also respect reduced motion when the SVG is opened directly.
    if "prefers-reduced-motion" not in css:
        style.text += ("@media(prefers-reduced-motion:reduce){"
                       ".c{animation:none!important}.s,.u{display:none}}")
    static = ET.Element(f"{{{NS}}}svg", root.attrib)
    static.extend([deepcopy(title), deepcopy(desc)])
    for cell in grid:
        result = deepcopy(cell)
        classes = cell.get("class", "").split()
        variable = fills.get(classes[1], "ce") if len(classes) > 1 else "ce"
        if variable not in variables:
            raise ValueError("Missing contribution color")
        result.attrib.pop("class", None)
        result.set("width", "12")
        result.set("height", "12")
        result.set("fill", variables[variable])
        result.set("stroke", variables.get("cb", "none"))
        result.set("stroke-width", "1")
        static.append(result)
    return tuple(ET.tostring(svg, encoding="unicode") + "\n" for svg in (root, static))


def main():
    folder = ROOT / "assets/generated"
    updated = datetime.now(timezone.utc).date().isoformat()
    outputs = {}
    for theme in ("light", "dark"):
        source = folder / f"snake-{theme}.svg"
        animated, static = prepare(source.read_text(), updated)
        outputs[source] = animated
        outputs[folder / f"contributions-{theme}.svg"] = static
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
    print("Prepared light/dark snakes and reduced-motion calendars")


if __name__ == "__main__":
    main()
