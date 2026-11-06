#!/usr/bin/env python3
"""Generate dated public-repository statistics using only Python's standard library."""
import json
import os
import re
import time
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/generated"


def api_get(path):
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "RochDev-profile"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(3):
        try:
            with urlopen(Request(f"https://api.github.com/{path}", headers=headers),
                         timeout=30) as response:
                return json.load(response)
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f"GitHub API returned HTTP {error.code}") from None
        except (URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError("GitHub API unavailable; previous snapshot retained") from None
        time.sleep(2 ** attempt)


def public_repositories(username, fetch=api_get):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", username):
        raise ValueError("Invalid GitHub username")
    repositories = {}
    page = 1
    while True:
        batch = fetch(f"users/{username}/repos?type=owner&per_page=100&page={page}")
        if not isinstance(batch, list):
            raise ValueError("Expected a repository list")
        for repo in batch:
            if (repo["private"] is False and not repo["fork"]
                    and repo["owner"]["login"].lower() == username.lower()):
                repositories[repo["id"]] = {
                    "name": repo["name"],
                    "language": repo["language"],
                }
        if len(batch) < 100:
            break
        page += 1
    return sorted(repositories.values(), key=lambda repo: repo["name"].lower())


def summarize(repositories, updated):
    counts = Counter(repo["language"] or "Not classified" for repo in repositories)
    return {
        "updated": updated,
        "scope": "Public owned repositories, excluding forks; archived repositories included.",
        "repositories": len(repositories),
        "primary_languages": len({r["language"] for r in repositories if r["language"]}),
        "language_counts": dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))),
    }


def render_svg(snapshot, dark):
    background, foreground, muted, border, track, accent = (
        ("#0B1120", "#F8FAFC", "#B8C5D6", "#26354B", "#1E293B", "#22D3EE")
        if dark else
        ("#F8FAFC", "#0B1120", "#475569", "#CBD5E1", "#E2E8F0", "#2563EB")
    )
    rows = snapshot["language_counts"]
    height = 236 + max(1, len(rows)) * 36
    title = f'{snapshot["repositories"]} original public repositories; {snapshot["primary_languages"]} primary languages'
    result = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="{height}" viewBox="0 0 480 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">Updated {snapshot["updated"]}. Counts of repositories by primary language, not skill levels or code volume. Forks excluded.</desc>',
        f'<rect x="0.5" y="0.5" width="479" height="{height-1}" rx="12" fill="{background}" stroke="{border}"/>',
        f'<g font-family="Arial, Helvetica, sans-serif" fill="{foreground}">',
        f'<text x="24" y="36" font-size="18" font-weight="700">PUBLIC / REPOSITORY SNAPSHOT</text>',
        f'<text x="24" y="95" font-size="40" font-weight="700">{snapshot["repositories"]}</text>',
        f'<text x="254" y="95" font-size="40" font-weight="700">{snapshot["primary_languages"]}</text>',
        f'<g fill="{muted}" font-size="18"><text x="24" y="123">Original repositories</text><text x="254" y="123">Primary languages</text></g>',
        f'<path d="M24 145H456" stroke="{border}"/>',
        f'<text x="24" y="177" font-size="18">Repositories by primary language</text>',
    ]
    maximum = max(rows.values(), default=1)
    for index, (language, count) in enumerate(rows.items()):
        y = 210 + index * 36
        result.extend([
            f'<text x="24" y="{y}" font-size="18">{escape(language)}</text>',
            f'<rect x="208" y="{y-13}" width="198" height="10" rx="5" fill="{track}"/>',
            f'<rect x="208" y="{y-13}" width="{198*count/maximum:.2f}" height="10" rx="5" fill="{accent}"/>',
            f'<text x="452" y="{y}" font-size="18" text-anchor="end">{count}</text>',
        ])
    if not rows:
        result.append(f'<text x="24" y="210" fill="{muted}" font-size="18">No public repositories yet.</text>')
    result.append(f'<text x="24" y="{height-22}" fill="{muted}" font-size="17">Updated {snapshot["updated"]} UTC · Forks excluded</text></g></svg>')
    return "\n".join(result) + "\n"


def main():
    config = json.loads((ROOT / "profile.json").read_text())
    repos = public_repositories(config["username"])
    snapshot = summarize(repos, datetime.now(timezone.utc).date().isoformat())
    # Fetching and rendering finish before any existing snapshot is replaced.
    files = {f"activity-{theme}.svg": render_svg(snapshot, theme == "dark")
             for theme in ("light", "dark")}
    files["activity.json"] = json.dumps(snapshot, indent=2) + "\n"
    lines = [
        "# Public repository snapshot", "",
        f'Updated **{snapshot["updated"]} UTC** from the GitHub REST API.', "",
        f'- Original public repositories: **{snapshot["repositories"]}**.',
        f'- Distinct primary languages: **{snapshot["primary_languages"]}**.', "",
        "| Primary language | Repositories |", "| --- | ---: |",
        *[f"| {language} | {count} |" for language, count in snapshot["language_counts"].items()],
        "", snapshot["scope"], "",
        "GitHub assigns one primary language per repository. Unclassified repositories are shown explicitly. "
        "These counts do not measure proficiency, all languages used, lines of code, or project completion.", "",
        f'[Source](https://api.github.com/users/{config["username"]}/repos?type=owner&per_page=100). '
        "The generator follows all pages. A failed refresh retains the previous snapshot.", "",
    ]
    files["activity.md"] = "\n".join(lines)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        temporary = OUTPUT / f".{name}.tmp"
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(OUTPUT / name)
    print(f'Updated public snapshot: {snapshot["repositories"]} repositories')


if __name__ == "__main__":
    main()
