import unittest
import xml.etree.ElementTree as ET
from scripts.generate_activity import public_repositories, summarize, render_svg
from scripts.prepare_snake import prepare, NS


def repository(identifier, **changes):
    result = {"id": identifier, "name": f"repo-{identifier}", "private": False,
              "fork": False, "owner": {"login": "Rochinel-codeur"}, "language": "Python"}
    result.update(changes)
    return result


class PublicSnapshotTests(unittest.TestCase):
    def test_only_public_owned_original_repositories_are_counted(self):
        data = [repository(1), repository(2, private=True), repository(3, fork=True),
                repository(4, owner={"login": "someone-else"})]
        self.assertEqual(public_repositories("Rochinel-codeur", lambda _: data),
                         [{"name": "repo-1", "language": "Python"}])

    def test_pagination_and_duplicate_repository_ids(self):
        pages = [[repository(i) for i in range(100)], [repository(99), repository(100)]]
        calls = []
        def fetch(path):
            calls.append(path)
            return pages[len(calls) - 1]
        self.assertEqual(len(public_repositories("Rochinel-codeur", fetch)), 101)
        self.assertIn("page=2", calls[1])

    def test_unclassified_is_not_a_language(self):
        result = summarize([{"language": "Python"}, {"language": "Python"},
                            {"language": None}], "2026-11-06")
        self.assertEqual(result["repositories"], 3)
        self.assertEqual(result["primary_languages"], 1)
        self.assertEqual(result["language_counts"], {"Python": 2, "Not classified": 1})

    def test_empty_account_and_xml_escaping(self):
        for repos in ([], [{"language": "A&B"}]):
            result = summarize(repos, "2026-11-06")
            for dark in (True, False):
                ET.fromstring(render_svg(result, dark))

    def test_api_error_is_not_treated_as_zero_repositories(self):
        def unavailable(_):
            raise RuntimeError("Service unavailable")
        with self.assertRaises(RuntimeError):
            public_repositories("Rochinel-codeur", unavailable)


class AccessibleSnakeTests(unittest.TestCase):
    def test_static_calendar_preserves_initial_levels_without_moving_objects(self):
        cells = '<rect class="c c0" x="2" y="2"/>' + '<rect class="c"/>' * 364
        source = (f'<svg xmlns="{NS}" viewBox="0 0 880 192">'
                  '<style>:root{--ce:#111111;--c1:#22D3EE}'
                  '.c.c0{fill:var(--c1);animation-name:c0}</style>'
                  + cells + '<rect class="s"/><rect class="u"/></svg>')
        animated, static = prepare(source, "2026-11-06")
        root = ET.fromstring(static)
        self.assertEqual(len(root.findall(f"{{{NS}}}rect")), 365)
        self.assertEqual(root.findall(f"{{{NS}}}rect")[0].get("fill"), "#22D3EE")
        self.assertNotIn("animation", static)
        self.assertIn("prefers-reduced-motion", animated)
        self.assertIn("Generated with https://github.com/Platane/snk", static)

    def test_unknown_upstream_format_fails_instead_of_publishing_empty_calendar(self):
        with self.assertRaises(ValueError):
            prepare(f'<svg xmlns="{NS}"/>', "2026-11-06")
