# RochDev V3 / Composition brief

## Audit

V2 mixes 960 px banners, 680 px project illustrations, 440 px stack and activity images, and a full-width approach. On a wide profile this leaves substantial unused space beside the stack and statistics. Project information sits outside its illustration in five successive elements. Repeated titles, paragraphs and frames make the page feel like documentation. Enlarging the existing vertical diagrams would preserve their excessive height.

## Composition system

Desktop artboards use a 1200-unit grid, a 56-unit safe margin and 32-unit gutters. The content width is 1088 units. Every major README image uses width="100%"; SVG view boxes define proportions, while the image attribute controls GitHub display width. No layout depends on arbitrary CSS in the README.

| Composition | Desktop | Mobile | Purpose |
| --- | --- | --- | --- |
| Cover | 1200 × 400 | 480 × 320 | Asymmetric identity and system monogram |
| Project | 1200 × 420 | 480 × 420 | Product story and illustration together |
| Stack | 1200 × 450 | 480 × 510 | Three horizontal domains; compact mobile rows |
| Approach | 1200 × 260 | 480 × 360 | Open timeline; paired mobile steps |
| Activity | 1200 × 340 | 480 × 400 | Metrics left, language distribution right |
| Contributions | Existing 880 × 192 | Same | Working animation, natural proportions |

At viewport widths up to 760 px, picture sources select mobile SVGs. Their 480-unit grid uses 28-unit margins. Mobile compositions keep essential information and reduce decorative detail. Project text also remains in native README text and links. Theme sources follow GitHub-supported picture syntax; reduced-motion sources remain intact.

## Tokens

- Dark: background #0B1120, surface #101C31, elevated #16243A, border #263A56, primary text #F8FAFC, secondary text #94A3B8.
- Accents: cyan #22D3EE, blue #2563EB, violet #8B5CF6. Light versions use a pale background, white surface, navy text and dark blue accents.
- Type: local Arial / Helvetica fallback. Desktop display 76–88, project title 64, headings 32, body 28, metadata 24. Mobile display 48, title 38, body 24, metadata 20–22.
- Spacing: 8, 16, 24, 32, 56, 80. Outer radius 24, inner radius 16. Informational strokes 2 units; monogram 7 units.
- Icons: 32–40 desktop, 24 mobile. Connectors use 2-unit strokes with circular endpoints, distinct from decorative borders.
- Foreground/background text pairs must reach 4.5:1. Lines carrying meaning use the theme's accent, while low-contrast borders only group content.

## Reading rhythm

Cover → short identity paragraph → two integrated product panels → three-domain technical landscape → open process timeline → wide data dashboard and contribution animation → plain personal invitation.

The seven principal sections are retained. The cover carries the role and tagline, avoiding a duplicate hero paragraph. The about paragraph has four sentences and no technology inventory. Native project summaries provide accessible names, value and repository links, without duplicating long technology lists. A short learning note follows the stack.

## Data and preservation

Repository counts continue to mean original public owned repositories, excluding forks and including archived repositories. Primary languages remain GitHub's one-language-per-repository classification. The language distribution explicitly includes unclassified originals. No unreliable public-activity metric is added. The existing snapshot and its date are preserved until a successful refresh.

The snake generator and workflow remain unchanged. The activity generator must emit desktop and mobile SVGs on each refresh so both remain current. Existing historical artwork is retained but no longer displayed.
