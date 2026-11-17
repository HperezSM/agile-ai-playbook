"""Tests for scripts/check_docs.py. Run with: python3 -m unittest discover -s tests"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import check_docs  # noqa: E402


def make_repo(files):
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    for rel, text in files.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return tmp, root


class SlugTests(unittest.TestCase):
    def test_github_style_slugs(self):
        self.assertEqual(check_docs.slugify("Sprint Planning"), "sprint-planning")
        self.assertEqual(check_docs.slugify("Sprint Goal — Did We Achieve It?"), "sprint-goal--did-we-achieve-it")
        self.assertEqual(check_docs.slugify("1. Problem Statement"), "1-problem-statement")
        self.assertEqual(check_docs.slugify("Start / Stop / Continue"), "start--stop--continue")
        self.assertEqual(check_docs.slugify("`code` and **bold**"), "code-and-bold")

    def test_duplicate_headings_get_suffixes(self):
        text = "# A\n## Notes\n## Notes\n"
        self.assertEqual(check_docs.anchors(text), {"a", "notes", "notes-1"})

    def test_headings_inside_code_blocks_are_ignored(self):
        text = "# Real\n```\n# not a heading\n```\n"
        self.assertEqual(check_docs.anchors(text), {"real"})


class LinkTests(unittest.TestCase):
    def test_valid_relative_link_and_anchor_pass(self):
        tmp, root = make_repo({
            "README.md": "[guide](./docs/guide.md#step-two)\n",
            "docs/guide.md": "# Guide\n## Step Two\n",
        })
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])

    def test_missing_file_is_reported(self):
        tmp, root = make_repo({"README.md": "[x](./nope.md)\n"})
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("nope.md", problems[0])

    def test_missing_anchor_is_reported(self):
        tmp, root = make_repo({
            "README.md": "[x](./a.md#missing)\n",
            "a.md": "# Present\n",
        })
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("#missing", problems[0])

    def test_same_file_anchor(self):
        tmp, root = make_repo({"README.md": "# Top\n[up](#top) [bad](#nowhere)\n"})
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("#nowhere", problems[0])

    def test_external_links_and_mailto_are_skipped(self):
        tmp, root = make_repo({"README.md": "[a](https://example.com/x.md) [b](mailto:a@b.c)\n"})
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])

    def test_links_inside_code_are_ignored(self):
        tmp, root = make_repo({"README.md": "```\n[x](./nope.md)\n```\nand `[y](./nope.md)`\n"})
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])

    def test_reference_style_links_are_checked(self):
        tmp, root = make_repo({
            "README.md": "[ok][a] [bad][b]\n\n[a]: ./a.md\n[b]: ./missing.md \"title\"\n",
            "a.md": "# A\n",
        })
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("missing.md", problems[0])

    def test_relative_image_links_are_checked(self):
        tmp, root = make_repo({"README.md": "![diagram](./img/missing.png)\n"})
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)

    def test_directory_link_must_exist(self):
        tmp, root = make_repo({"README.md": "[t](./templates/)\n", "templates/a.md": "# A\n"})
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])


class ContentTests(unittest.TestCase):
    def test_todo_marker_is_reported(self):
        tmp, root = make_repo({"README.md": "# R\nTODO: write this\n"})
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("TODO", problems[0])

    def test_template_with_filled_author_is_reported(self):
        tmp, root = make_repo({
            "README.md": "# R\n",
            "templates/prd.md": "# PRD\n**Author:** Jane Doe\n",
        })
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("Author", problems[0])

    def test_template_with_blank_author_passes(self):
        tmp, root = make_repo({
            "README.md": "# R\n",
            "templates/prd.md": "# PRD\n**Author:**\n**Owner:** \n",
        })
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])


class TemplateIndexTests(unittest.TestCase):
    def test_template_missing_from_index_is_reported(self):
        tmp, root = make_repo({
            "templates/README.md": "# T\n[A](./a.md)\n",
            "templates/a.md": "# A\n",
            "templates/b.md": "# B\n",
        })
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)
        self.assertIn("b.md", problems[0])
        self.assertIn("templates/README.md", problems[0])

    def test_all_templates_indexed_passes(self):
        tmp, root = make_repo({
            "templates/README.md": "# T\n[A](./a.md) [B](b.md#b)\n",
            "templates/a.md": "# A\n",
            "templates/b.md": "# B\n",
        })
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])

    def test_link_inside_code_does_not_count_as_indexed(self):
        tmp, root = make_repo({
            "templates/README.md": "# T\n`[A](./a.md)`\n",
            "templates/a.md": "# A\n",
        })
        with tmp:
            problems = check_docs.check_repo(root)
        self.assertEqual(len(problems), 1)

    def test_no_templates_folder_is_fine(self):
        tmp, root = make_repo({"README.md": "# R\n"})
        with tmp:
            self.assertEqual(check_docs.check_repo(root), [])


class MainTests(unittest.TestCase):
    def test_exit_codes(self):
        tmp, root = make_repo({"README.md": "[x](./nope.md)\n"})
        with tmp:
            self.assertEqual(check_docs.main([str(root)]), 1)
        tmp, root = make_repo({"README.md": "# fine\n"})
        with tmp:
            self.assertEqual(check_docs.main([str(root)]), 0)


if __name__ == "__main__":
    unittest.main()
