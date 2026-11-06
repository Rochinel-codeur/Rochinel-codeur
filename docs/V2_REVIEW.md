# RochDev V2 review

## Changes

The seven principal sections now cover identity, background, projects, stack, approach, activity and contact. Visible Markdown prose is reduced from 468 to 266 whitespace-separated words, approximately 43%, using the same tag-stripped word count on V1 and V2. SVG labels are excluded from that count; the technical domains and method have moved into graphics.

The banner retains the original monogram and architecture motif, with corrected text alignment and a more explicit backend identity. Facteo and QuizLy have distinct conceptual illustrations in light and dark palettes. The project layouts stack vertically to preserve mobile readability. The illustrations do not claim to show an actual product interface.

The engineering stack uses five connected layers. The approach has horizontal desktop and vertical mobile versions. Both share the same palette, local font fallback, rounded panels and stroke widths. All essential diagram content is also available in image alternative text.

The statistics retain exact original-public-repository and primary-language counts with a smaller 440 px composition, clearer labels and a date. Their scope excludes forks, includes archived originals, and keeps unclassified repositories separate from language totals. No total-public-repository count is presented as an original-repository count. The working snake, static calendars and both workflows are preserved.

## Verification

The V2 checks passed all seven existing Python tests, the SVG/resource validator (20 SVGs and 18 image source references), Markdown lint and actionlint. Chrome checks cover 320, 390, 768 and 1280 px, both themes, and reduced-motion source selection. All seven displayed images load and no horizontal document overflow was detected. Mobile dark and desktop light captures were visually inspected. Previews use GitHub's Markdown API output with a local stylesheet, rather than a published V2 profile.

Chrome also checked text bounds in all 14 branding/project SVGs, with no labels extending beyond their view boxes. Seven principal foreground/background pairs were measured, with contrast ratios from 6.70:1 to 18.00:1. This covers the text palette; decorative borders intentionally have lower contrast. GitHub's public API reconfirmed both project repositories are public and that the linked Facteo architecture document exists. Workflows and snake assets have no V2 diff.

Publication of V2 was explicitly authorized by the repository owner after local review. Hosted workflow results are available in the repository's Actions tab. Screenshots and temporary inspection tools are in the ignored `.local/` folder.
