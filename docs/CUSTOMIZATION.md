# Profile customization

The README, artwork and workflows live in this profile repository. Edit [README.md](../README.md) for presentation, projects and contacts. [profile.json](../profile.json) records verified identity and contact metadata; only its username is consumed by the statistics generator. Keep manual README links and the snake workflow's username in sync when changing accounts. LinkedIn and portfolio links are empty because none were present on the public profile when it was audited; add a confirmed URL before linking it. The published email was checked on that profile on 6 November 2026.

The profile links to **Facteo** and **QuizLy** because both are public repositories. The checked-in descriptions reflect their public README and source. Evento / SECO and Medicam Express did not appear in the inspected public repository list. Demo URLs and deployment status are not claimed.

## GitHub Actions

`Refresh profile artwork` runs daily at 05:23 UTC, manually with **Run workflow**, and after changes to its configuration or generators on `main`. It reads the public repository API and contribution calendar with the standard `GITHUB_TOKEN`. The workflow grants repository content write access only to its final publication job; the generation job can read. The token may include anonymized private activity in the contribution calendar, as configured by GitHub; no private repository names or private activity records are requested or published. Repository statistics explicitly exclude forks and use only public owned repository metadata.

The refresh commits only `assets/generated/`. The previous valid artwork remains available if generation or validation fails. GitHub must permit the actions bot to push to the default branch. If branch protection prevents that push, use a maintainer-approved change process for the generated artwork; do not bypass protection rules.

After publishing these files to `main`, open **Actions → Refresh profile artwork → Run workflow** to verify the first hosted run. No personal access token or custom secret is needed. GitHub may delay scheduled jobs and disables scheduled workflows in public repositories after 60 days without repository activity; re-enable the workflow if necessary. If the default branch changes, update both workflow branch filters, the generation job guard, and publication checkout/push targets.

## Regenerate locally

Python 3 and a GitHub CLI login with public access are enough to update the language and repository snapshot:

```sh
gh auth login
GH_TOKEN="$(gh auth token)" python3 scripts/generate_activity.py
```

To refresh the snake images locally, manually trigger the workflow. Its pinned Platane/snk action uses Node 24, and its GraphQL contribution calendar requires a GitHub token. Do not put a personal token into a committed file or share it in a build log.

## Art direction and scope

The palette uses midnight navy, cyan and electric blue, with violet as a small connection detail. The desktop banner and separate 480 px mobile banner share the same geometric monogram. `engineering-map.svg` expresses product relationships rather than skill rankings. Statistics show primary-language **repository counts**, not lines of code, all languages, contribution totals or proficiency. The animated snake is paired with genuinely static calendars for `prefers-reduced-motion`.

## Validation

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_profile.py
git diff --check
```

For full workflow syntax validation, run [actionlint](https://github.com/rhysd/actionlint). Markdown lint configuration allows inline HTML, the introductory role line, punctuation in the greeting, and natural paragraph lengths.

The initial artwork was generated locally from real public data, so all referenced images exist before the first hosted workflow run. The initial snake uses GitHub's anonymously visible calendar as input to the pinned Platane generator. Future runs use the action's documented GraphQL input. The generator's attribution is preserved in the SVG descriptions.

## Sources and dependency choices

- [Platane/snk documentation](https://github.com/Platane/snk): SVG-only v3 action, output customization and themed picture sources. The action is pinned to a verified commit, as are the checkout and artifact actions.
- [GitHub token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token): read access during generation, content write access only during publication.
- [Scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule): default-branch and inactivity requirements.
- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats), [Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats) and [Profile Summary Cards](https://github.com/vn7n24fzkq/github-profile-summary-cards) were considered. A small local snapshot was chosen to give the metrics explicit scope, match the branding, and retain the last valid images when a refresh fails.
