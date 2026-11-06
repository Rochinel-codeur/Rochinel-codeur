# RochDev V3 / Delivery review

## Structural changes

The audit identified mixed display widths as the cause of V2's empty right-hand space: projects were limited to 680 px, and stack and statistics to 440 px. Project information followed the illustration in separate blocks, repeating a documentation-like rhythm.

V3 uses a common 1200-unit desktop grid and 100% README image widths. The 1200 × 400 cover sets an asymmetric identity. Each 1200 × 420 project panel integrates its name, category, value, technologies and repository invitation beside a distinct conceptual illustration. Short native Markdown summaries retain accessible project information and verified links.

The 1200 × 450 stack uses three connected domains. The approach is an open 1200 × 260 timeline with distinct icons and brief descriptions. Statistics occupy a 1200 × 340 split dashboard: original repository/language counts on the left, exact primary-language distribution on the right. No unsupported activity metric was added. The existing data snapshot and date are unchanged.

Dedicated mobile compositions use 480-unit view boxes and reduce decorative detail. Native picture sources switch up to 760 px. No README layout depends on CSS, JavaScript, tables or remote fonts. The about paragraph has four sentences and 47 words. The footer uses the requested personal invitation and verified email/GitHub links.

## Design-first evidence

The [composition brief](V3_DESIGN.md) records the grid, dimensions, token system and editorial hierarchy. A local HTML composition board was created, captured and visually inspected before the README was rewritten. Its files are in the ignored `.local/` folder: `v3-composition.html` and `v3-composition.png`.

The final palette and drawing helpers live in `scripts/artwork.py`. `scripts/build_editorial_assets.py` rebuilds covers and editorial artwork. `scripts/generate_activity.py` now writes synchronized desktop/mobile and light/dark dashboards from the same API snapshot. The existing workflow already publishes the entire generated folder, so its configuration remains unchanged.

## Executed validation

- Eight Python tests passed, including a new refresh test checking that all four dashboard variants use the same snapshot and date.
- Offline validation passed for 28 SVGs and 26 README image source references. Every displayed image declares 100% width. Local image and text-snapshot paths resolve.
- Markdown lint, actionlint and `git diff --check` passed. The workflow configuration, snake generator and snake assets have no V3 changes.
- GitHub's public API reconfirmed Facteo and QuizLy are public and the linked Facteo architecture document exists. No links or metrics were invented.
- Chrome rendered GitHub Markdown API output at 1440, 1280, 768, 390 and 320 px in light and dark themes. All ten cases loaded all seven displayed images at full content width, without horizontal document overflow. Reduced-motion preference selected the static calendar.
- Chrome checked text bounds in all 24 non-animated branding, project and statistics SVGs. No text extended beyond its view box. The desktop timeline descriptions have at least 16 units of clearance before the next step.
- Eighteen foreground/background text pairs were measured; minimum contrast was 5.75:1. Decorative borders are not intended as text or information-bearing lines.
- Desktop light/dark, tablet light and mobile dark full-page captures were visually inspected. The first inspection found crowded timeline descriptions; these were shortened and the captures and clearance checks were repeated.

Final local captures are `.local/v3-preview-{width}-{theme}.png`. Their surrounding content container approximates GitHub using a local stylesheet; these captures do not represent the live profile interface. The owner subsequently authorized publication of V3. Hosted workflow results are available in the repository's Actions tab.
