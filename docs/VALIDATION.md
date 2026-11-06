# Audit and delivery record

Verified locally on 6 November 2026. No changes were pushed to GitHub.

## Initial audit

The repository was on `main`, with a clean working tree and one initial commit containing the default profile README. It had no existing SVGs, workflows or application dependencies. Its origin points to `Rochinel-codeur/Rochinel-codeur`.

The public GitHub API listed 13 owned repositories, including one fork. Facteo and QuizLy were selected after examining their public files. Facteo's invoice workflow and Python/React stack are supported by its README, backend requirements, frontend package and repository tree. QuizLy's experimental generation/evaluation/explanation flow is supported by its FastAPI entry point, LangGraph definition and requirements. Their applications were not deployed or runtime-tested for this portfolio task. No verified live demos were found.

The public profile supplies the GitHub link and published email used in the README. No LinkedIn or portfolio was listed. No private repository content or local files from other projects were inspected.

## Executed checks

- Seven Python unit tests passed: public/owner/fork filtering, pagination and deduplication, unclassified language handling, empty accounts and XML escaping, API failures, static calendar levels, and rejection of unsupported SVG structures.
- The offline validator passed for 10 SVGs, 9 README image references, local resource paths, statistic totals and immutable action references.
- `actionlint` 1.7.12 passed for both workflows, with its optional external ShellCheck integration disabled.
- Markdown lint passed for README, customization guide and generated text snapshot. `git diff --check` passed.
- GitHub's Markdown API rendered the README successfully. Chrome rendered that HTML with a local GitHub Markdown stylesheet at 320, 390, 768 and 1280 px, in light and dark themes. All eight cases loaded the four displayed images, had no horizontal document overflow, and selected a static contribution calendar when reduced motion was enabled.
- Full-page captures were saved in the ignored `.local/` folder. Mobile dark and desktop light captures were visually inspected. These previews approximate the profile content area; they do not reproduce GitHub's surrounding profile interface.

Public repository metadata and inspected file trees verify the project destinations and Facteo architecture-document path. A final HTTP link sweep encountered DNS resolution failures in this environment, so a successful final HTTP status check is not claimed. The hosted GitHub Actions workflow has not been executed; its first remote run remains to be checked after an authorized push.

## Maintained files

`README.md` contains the public presentation. `assets/branding/` contains the original banner variants, monogram and engineering map. `assets/generated/` contains dated statistics, animated snakes and static calendars in both themes. `scripts/`, `tests/` and `.github/workflows/` provide generation and validation. `profile.json` records verified metadata; the customization guide explains manual edits and workflow operation.
