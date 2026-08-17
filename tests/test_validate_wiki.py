from __future__ import annotations

import hashlib
import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "validate_wiki.py"
SPEC = importlib.util.spec_from_file_location("validate_wiki", MODULE_PATH)
assert SPEC and SPEC.loader
validate_wiki = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_wiki
SPEC.loader.exec_module(validate_wiki)


SCHEMA = """# Wiki Schema

## Directory roles

| Path | Role |
| --- | --- |
| `raw/official-docs/` | Official sources. |
| `raw/assets/` | Attachments. |
| `entities/` | Entity pages. |
| `concepts/` | Concept pages. |
| `comparisons/` | Comparison pages. |
| `queries/` | Query pages. |

## Tag taxonomy

### Registered tags

- `aidd`: AIDD.
- `workflow`: Workflow.
- `requirements`: Requirements.
- `architecture`: Architecture.
- `story`: Story.
- `implementation`: Implementation.
- `review`: Review.
- `testing`: Testing.
- `automation`: Automation.
- `human-gate`: Human gate.

## AIDD source-record contract
"""


def canonical(slug: str, page_type: str, links: list[str], source: str, tags: list[str] | None = None) -> str:
    tag_lines = "\n".join(f"  - {tag}" for tag in (tags or ["aidd", "workflow"]))
    link_text = " ".join(f"[[{link}]]" for link in links)
    return f"""---
title: "{slug}"
created: 2026-08-04
updated: 2026-08-04
type: {page_type}
tags:
{tag_lines}
sources:
  - {source}
confidence: medium
contested: false
contradictions: []
---
# {slug}

{link_text}

Claim.^[{source}]
"""


class FixtureWiki:
    def __init__(self, root: Path) -> None:
        self.root = root
        for directory in ("entities", "concepts", "comparisons", "queries", "raw/official-docs"):
            (root / directory).mkdir(parents=True, exist_ok=True)
        (root / "SCHEMA.md").write_text(SCHEMA, encoding="utf-8", newline="\n")
        body = b"Official body.\n"
        digest = hashlib.sha256(body).hexdigest()
        self.source = "raw/official-docs/source.md"
        (root / self.source).write_bytes(
            f"---\nsource_url: \"https://example.com/source\"\nsha256: {digest}\n---\n".encode() + body
        )
        pages = (
            ("entities/alpha.md", "entity", ["beta", "gamma"]),
            ("concepts/beta.md", "concept", ["alpha", "gamma"]),
            ("queries/gamma.md", "query", ["alpha", "beta"]),
        )
        for relative, page_type, links in pages:
            (root / relative).write_text(
                canonical(Path(relative).stem, page_type, links, self.source),
                encoding="utf-8",
                newline="\n",
            )
        (root / "index.md").write_text(
            """# Wiki Index

> Total pages: 3

## Entities

- [[alpha]] — Alpha.

## Concepts

- [[beta]] — Beta.

## Comparisons

## Queries

- [[gamma]] — Gamma.
""",
            encoding="utf-8",
            newline="\n",
        )
        (root / "log.md").write_text(
            "# Wiki Log\n\n## [2026-08-04] create | Fixture\n\n- Created fixture.\n",
            encoding="utf-8",
            newline="\n",
        )


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.wiki = FixtureWiki(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self):
        return validate_wiki.WikiValidator(self.root, check_git=False).validate()

    def codes(self, validator, severity="ERROR") -> set[str]:
        return {item.code for item in validator.findings if item.severity == severity}

    def test_valid_wiki(self) -> None:
        validator = self.validate()
        self.assertEqual(validator.counts()[0], 0, validator.render())

    def test_missing_source_path(self) -> None:
        page = self.root / "entities/alpha.md"
        page.write_text(page.read_text(encoding="utf-8").replace(self.wiki.source, "raw/official-docs/missing.md"), encoding="utf-8", newline="\n")
        self.assertIn("SOURCE_MISSING", self.codes(self.validate()))

    def test_broken_wikilink(self) -> None:
        page = self.root / "entities/alpha.md"
        page.write_text(page.read_text(encoding="utf-8").replace("[[beta]]", "[[missing-page]]"), encoding="utf-8", newline="\n")
        self.assertIn("WIKILINK_BROKEN", self.codes(self.validate()))

    def test_missing_index_entry(self) -> None:
        index = self.root / "index.md"
        index.write_text(index.read_text(encoding="utf-8").replace("- [[gamma]] — Gamma.\n", ""), encoding="utf-8", newline="\n")
        self.assertIn("INDEX_ENTRY_MISSING", self.codes(self.validate()))

    def test_hash_mismatch(self) -> None:
        source = self.root / self.wiki.source
        source.write_bytes(source.read_bytes() + b"drift\n")
        self.assertIn("RAW_HASH_MISMATCH", self.codes(self.validate()))

    def test_unregistered_tag(self) -> None:
        page = self.root / "entities/alpha.md"
        page.write_text(page.read_text(encoding="utf-8").replace("  - workflow", "  - unregistered"), encoding="utf-8", newline="\n")
        self.assertIn("TAG_UNREGISTERED", self.codes(self.validate()))

    def test_duplicate_slug(self) -> None:
        duplicate = self.root / "comparisons/alpha.md"
        duplicate.write_text(canonical("alpha", "comparison", ["beta", "gamma"], self.wiki.source), encoding="utf-8", newline="\n")
        self.assertIn("DUPLICATE_SLUG", self.codes(self.validate()))

    def test_exit_code_contract(self) -> None:
        with redirect_stdout(io.StringIO()):
            self.assertEqual(validate_wiki.main([str(self.root), "--no-git"]), 0)
        source = self.root / self.wiki.source
        source.write_bytes(source.read_bytes() + b"drift\n")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(validate_wiki.main([str(self.root), "--no-git"]), 1)


if __name__ == "__main__":
    unittest.main()
