#!/usr/bin/env python3
"""Deterministic validator for the Markdown wiki described by SCHEMA.md."""

from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


CANONICAL_DIRS = {
    "entities": "entity",
    "concepts": "concept",
    "comparisons": "comparison",
    "queries": "query",
}
INDEX_SECTIONS = {
    "Entities": "entities",
    "Concepts": "concepts",
    "Comparisons": "comparisons",
    "Queries": "queries",
}
REQUIRED_FIELDS = (
    "title",
    "created",
    "updated",
    "type",
    "tags",
    "sources",
    "confidence",
    "contested",
    "contradictions",
)
CONFIDENCE_VALUES = {"high", "medium", "low"}
LOG_ACTIONS = {
    "ingest",
    "create",
    "update",
    "query",
    "lint",
    "archive",
    "delete",
    "map",
    "repair",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
CLAIM_RE = re.compile(r"\^\[([^\]\r\n]+)\]")
INDEX_ENTRY_RE = re.compile(r"^- \[\[([^\]]+)\]\](?:\s+—\s+.*)?$")
LOG_HEADING_RE = re.compile(
    r"^## \[(\d{4}-\d{2}-\d{2})\] ([a-z]+) \| (.+)$"
)
PATH_TOKEN_RE = re.compile(r"`([^`]+)`")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SOURCE_ASSET_SUFFIXES = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".zip",
}


@dataclass(order=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


@dataclass
class Stats:
    raw_sources: int = 0
    canonical_pages: int = 0
    canonical_by_type: dict[str, int] = field(
        default_factory=lambda: {value: 0 for value in CANONICAL_DIRS.values()}
    )
    index_entries: int = 0
    wikilinks: int = 0
    source_references: int = 0
    claim_markers: int = 0


@dataclass
class Frontmatter:
    data: dict[str, Any]
    body_start: int
    errors: list[str]


@dataclass
class CanonicalPage:
    path: Path
    relative: str
    slug: str
    directory: str
    text: str
    metadata: dict[str, Any]
    sources: list[str]
    links: list[str]


def posix_path(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item.strip()) for item in inner.split(",")]
    if value == "{}":
        return {}
    if value == "true":
        return True
    if value == "false":
        return False
    if value in {"null", "~"}:
        return None
    if value.startswith(("\"", "'")):
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value
        return parsed
    return value


def parse_frontmatter(content: bytes) -> Frontmatter | None:
    if not content.startswith(b"---\n"):
        return None
    closing = content.find(b"\n---\n", 4)
    if closing < 0:
        return Frontmatter({}, -1, ["closing frontmatter delimiter is missing"])
    try:
        header = content[4:closing].decode("utf-8")
    except UnicodeDecodeError as exc:
        return Frontmatter({}, closing + 5, [f"frontmatter is not UTF-8: {exc}"])

    data: dict[str, Any] = {}
    errors: list[str] = []
    active_list: str | None = None
    for number, line in enumerate(header.split("\n"), start=2):
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if active_list is None:
                errors.append(f"line {number}: list item has no parent key")
                continue
            data[active_list].append(parse_scalar(line[4:]))
            continue
        if line.startswith((" ", "\t")):
            errors.append(f"line {number}: unsupported nested YAML structure")
            continue
        match = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?", line)
        if not match:
            errors.append(f"line {number}: unsupported YAML syntax")
            active_list = None
            continue
        key, raw_value = match.group(1), match.group(2) or ""
        if key in data:
            errors.append(f"line {number}: duplicate key {key!r}")
        if raw_value == "":
            data[key] = []
            active_list = key
        else:
            data[key] = parse_scalar(raw_value)
            active_list = None
    return Frontmatter(data, closing + 5, errors)


def valid_calendar_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE_RE.fullmatch(value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def extract_schema_tags(schema_text: str) -> list[str]:
    match = re.search(
        r"(?ms)^### Registered tags\s*$\n(.*?)(?=^##\s)", schema_text
    )
    if not match:
        return []
    return re.findall(r"(?m)^- `([^`]+)`: ", match.group(1))


def extract_registered_raw_dirs(schema_text: str) -> set[str]:
    directories: set[str] = set()
    for value in re.findall(r"(?m)^\| `?(raw/[^`|]+/?)`? \|", schema_text):
        directories.add(value.rstrip("/"))
    return directories


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip("/")


def link_slug(target: str) -> str:
    return PurePosixPath(target).name


def path_is_under(path: str, directory: str) -> bool:
    return path == directory or path.startswith(directory.rstrip("/") + "/")


def run_git(root: Path, *args: str) -> subprocess.CompletedProcess[bytes] | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except OSError:
        return None
    return result


def git_changes(root: Path) -> dict[str, str] | None:
    inside = run_git(root, "rev-parse", "--is-inside-work-tree")
    if inside is None or inside.returncode != 0 or inside.stdout.strip() != b"true":
        return None
    status = run_git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    if status is None or status.returncode != 0:
        return None
    changes: dict[str, str] = {}
    fields = status.stdout.split(b"\0")
    index = 0
    while index < len(fields):
        field = fields[index]
        index += 1
        if not field:
            continue
        decoded = field.decode("utf-8", errors="surrogateescape")
        code, path = decoded[:2], decoded[3:]
        if "R" in code or "C" in code:
            if index < len(fields) and fields[index]:
                old_path = fields[index].decode("utf-8", errors="surrogateescape")
                changes[old_path.replace("\\", "/")] = "D"
                index += 1
        changes[path.replace("\\", "/")] = code
    return changes


class WikiValidator:
    def __init__(self, root: Path, check_git: bool = True) -> None:
        self.root = root.resolve()
        self.check_git = check_git
        self.findings: list[Finding] = []
        self.stats = Stats()
        self.schema_text = ""
        self.registered_tags: list[str] = []
        self.registered_raw_dirs: set[str] = set()
        self.pages: list[CanonicalPage] = []
        self.pages_by_slug: dict[str, list[CanonicalPage]] = defaultdict(list)
        self.used_tags: set[str] = set()
        self.inbound: Counter[str] = Counter()

    def add(self, severity: str, code: str, path: str, message: str) -> None:
        self.findings.append(Finding(severity, code, path, message))

    def error(self, code: str, path: str, message: str) -> None:
        self.add("ERROR", code, path, message)

    def warning(self, code: str, path: str, message: str) -> None:
        self.add("WARNING", code, path, message)

    def info(self, code: str, path: str, message: str) -> None:
        self.add("INFO", code, path, message)

    def validate(self) -> "WikiValidator":
        schema_path = self.root / "SCHEMA.md"
        if not schema_path.is_file():
            self.error("SCHEMA_MISSING", "SCHEMA.md", "authoritative schema is missing")
            return self
        try:
            self.schema_text = schema_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            self.error("SCHEMA_ENCODING", "SCHEMA.md", f"invalid UTF-8: {exc}")
            return self
        self.registered_tags = extract_schema_tags(self.schema_text)
        self.registered_raw_dirs = extract_registered_raw_dirs(self.schema_text)
        if not self.registered_tags:
            self.error("TAG_REGISTRY_MISSING", "SCHEMA.md", "Registered tags section is missing or empty")
        elif not 10 <= len(self.registered_tags) <= 20:
            self.error("TAG_REGISTRY_SIZE", "SCHEMA.md", "active tag taxonomy must contain 10 to 20 tags")
        if not self.registered_raw_dirs:
            self.error("RAW_REGISTRY_MISSING", "SCHEMA.md", "no raw directories are registered")

        self.validate_canonical()
        self.validate_tags()
        self.validate_sources_and_markers()
        self.validate_raw()
        self.validate_wikilinks()
        self.validate_index()
        self.validate_log()
        self.validate_sensitive_information()
        return self

    def markdown_files(self, directory: Path) -> list[Path]:
        if not directory.is_dir():
            return []
        return sorted(
            (path for path in directory.rglob("*.md") if path.name != ".gitkeep"),
            key=lambda path: path.as_posix(),
        )

    def validate_canonical(self) -> None:
        for directory, expected_type in CANONICAL_DIRS.items():
            folder = self.root / directory
            if not folder.is_dir():
                self.error("CANONICAL_DIR_MISSING", directory, "canonical directory is missing")
                continue
            for path in self.markdown_files(folder):
                relative = posix_path(path, self.root)
                slug = path.stem
                self.stats.canonical_pages += 1
                self.stats.canonical_by_type[expected_type] += 1
                if not SLUG_RE.fullmatch(slug):
                    self.error("CANONICAL_FILENAME", relative, "filename is not lowercase kebab-case")
                content = path.read_bytes()
                self.validate_markdown_format(relative, content, legacy_allowed=False)
                try:
                    text = content.decode("utf-8")
                except UnicodeDecodeError as exc:
                    self.error("CANONICAL_ENCODING", relative, f"invalid UTF-8: {exc}")
                    continue
                frontmatter = parse_frontmatter(content)
                if frontmatter is None:
                    self.error("FRONTMATTER_MISSING", relative, "frontmatter must start at byte zero")
                    metadata: dict[str, Any] = {}
                else:
                    metadata = frontmatter.data
                    for problem in frontmatter.errors:
                        self.error("FRONTMATTER_INVALID", relative, problem)
                for field_name in REQUIRED_FIELDS:
                    if field_name not in metadata:
                        self.error("FIELD_MISSING", relative, f"required field {field_name!r} is missing")
                if metadata.get("type") != expected_type:
                    self.error(
                        "TYPE_DIRECTORY_MISMATCH",
                        relative,
                        f"type must be {expected_type!r} in {directory}/",
                    )
                for field_name in ("created", "updated"):
                    if field_name in metadata and not valid_calendar_date(metadata[field_name]):
                        self.error("DATE_INVALID", relative, f"{field_name} must be a valid YYYY-MM-DD date")
                if "confidence" in metadata and metadata["confidence"] not in CONFIDENCE_VALUES:
                    self.error("CONFIDENCE_INVALID", relative, "confidence must be high, medium, or low")
                if "contested" in metadata and not isinstance(metadata["contested"], bool):
                    self.error("CONTESTED_INVALID", relative, "contested must be a YAML boolean")
                if "contradictions" in metadata and not isinstance(metadata["contradictions"], list):
                    self.error("CONTRADICTIONS_INVALID", relative, "contradictions must be a list")
                elif isinstance(metadata.get("contradictions"), list):
                    for contradiction in metadata["contradictions"]:
                        if not isinstance(contradiction, str):
                            self.error("CONTRADICTIONS_INVALID", relative, "contradiction entries must be strings")
                for list_field in ("tags", "sources"):
                    if list_field in metadata and not isinstance(metadata[list_field], list):
                        self.error("LIST_FIELD_INVALID", relative, f"{list_field} must be a list")
                    elif isinstance(metadata.get(list_field), list):
                        values = metadata[list_field]
                        if len(values) != len({str(value) for value in values}):
                            self.warning("LIST_DUPLICATE", relative, f"{list_field} contains duplicate entries")
                if re.search(r"<[A-Za-z][^>\n]*>", text):
                    self.error("ANGLE_PLACEHOLDER", relative, "unresolved angle-bracket token is present")
                line_count = len(text.splitlines())
                if line_count > 200:
                    self.warning("PAGE_LENGTH", relative, f"page has {line_count} lines; consider splitting near 200")

                sources = metadata.get("sources", [])
                if not isinstance(sources, list):
                    sources = []
                links = [match.group(1) for match in WIKILINK_RE.finditer(text)]
                page = CanonicalPage(path, relative, slug, directory, text, metadata, sources, links)
                self.pages.append(page)
                self.pages_by_slug[slug].append(page)

        for slug, pages in sorted(self.pages_by_slug.items()):
            if len(pages) > 1:
                paths = ", ".join(page.relative for page in pages)
                self.error("DUPLICATE_SLUG", paths, f"slug {slug!r} is duplicated")

    def validate_tags(self) -> None:
        registered = set(self.registered_tags)
        for page in self.pages:
            tags = page.metadata.get("tags", [])
            if not isinstance(tags, list):
                continue
            for tag in tags:
                if not isinstance(tag, str):
                    self.error("TAG_INVALID", page.relative, "each tag must be a string")
                    continue
                self.used_tags.add(tag)
                if tag not in registered:
                    self.error("TAG_UNREGISTERED", page.relative, f"tag {tag!r} is not registered in SCHEMA.md")
        for tag in sorted(registered - self.used_tags):
            self.warning("TAG_UNUSED", "SCHEMA.md", f"registered tag {tag!r} is unused")

    def validate_markdown_format(self, relative: str, content: bytes, legacy_allowed: bool) -> None:
        if content.startswith(b"\xef\xbb\xbf"):
            self.error("FORMAT_BOM", relative, "UTF-8 BOM is not allowed")
        try:
            content.decode("utf-8")
        except UnicodeDecodeError as exc:
            self.error("FORMAT_UTF8", relative, f"file is not valid UTF-8: {exc}")
        if b"\r" in content:
            self.error("FORMAT_LINE_ENDING", relative, "Markdown must use LF line endings")
        if content and not content.endswith(b"\n"):
            if legacy_allowed:
                self.warning("FORMAT_LEGACY_EOF", relative, "documented legacy source lacks a final LF")
            else:
                self.error("FORMAT_FINAL_LF", relative, "Markdown must end with LF")

    def validate_sources_and_markers(self) -> None:
        disallowed_dirs = {"raw/assets", "raw/papers/files"}
        for page in self.pages:
            source_set: set[str] = set()
            for source in page.sources:
                self.stats.source_references += 1
                if not isinstance(source, str):
                    self.error("SOURCE_INVALID", page.relative, "source entries must be strings")
                    continue
                normalized = source.replace("\\", "/").lstrip("./")
                source_set.add(normalized)
                suffix = PurePosixPath(normalized).suffix.lower()
                if suffix != ".md":
                    code = "SOURCE_ASSET" if suffix in SOURCE_ASSET_SUFFIXES else "SOURCE_NOT_MARKDOWN"
                    self.error(code, page.relative, f"source is not a raw Markdown record: {source}")
                    continue
                if not normalized.startswith("raw/"):
                    self.error("SOURCE_OUTSIDE_RAW", page.relative, f"source is outside raw/: {source}")
                    continue
                if any(path_is_under(normalized, item) for item in disallowed_dirs):
                    self.error("SOURCE_ASSET", page.relative, f"attachment/asset cannot be a source: {source}")
                    continue
                if not any(path_is_under(normalized, item) for item in self.registered_raw_dirs):
                    self.error("SOURCE_DIR_UNREGISTERED", page.relative, f"raw directory is not registered: {source}")
                source_path = self.root / PurePosixPath(normalized)
                if not source_path.is_file():
                    self.error("SOURCE_MISSING", page.relative, f"source path does not exist: {source}")

            for marker_match in CLAIM_RE.finditer(page.text):
                marker = marker_match.group(1).replace("\\", "/").lstrip("./")
                if not marker.startswith("raw/"):
                    continue
                self.stats.claim_markers += 1
                marker_path = self.root / PurePosixPath(marker)
                if not marker_path.is_file():
                    self.error("CLAIM_SOURCE_MISSING", page.relative, f"claim marker does not resolve: {marker}")
                if marker not in source_set:
                    self.error("CLAIM_NOT_LISTED", page.relative, f"claim marker is absent from sources: {marker}")

    def validate_raw(self) -> None:
        raw_root = self.root / "raw"
        if not raw_root.is_dir():
            self.error("RAW_DIR_MISSING", "raw", "raw directory is missing")
            return
        log_text = ""
        log_path = self.root / "log.md"
        if log_path.is_file():
            log_text = log_path.read_text(encoding="utf-8", errors="replace")
        for path in self.markdown_files(raw_root):
            relative = posix_path(path, self.root)
            self.stats.raw_sources += 1
            content = path.read_bytes()
            frontmatter = parse_frontmatter(content)
            sha_value: Any = None
            if frontmatter is not None:
                for problem in frontmatter.errors:
                    self.error("RAW_FRONTMATTER_INVALID", relative, problem)
                sha_value = frontmatter.data.get("sha256")
            if sha_value is None or sha_value == "":
                location = log_text.find(relative)
                context = log_text[max(0, location - 600) : location + len(relative) + 600] if location >= 0 else ""
                documented = location >= 0 and re.search(
                    r"(?i)(legacy|hash.{0,30}gap|missing.{0,20}sha256|no recorded.{0,20}sha256)",
                    context,
                )
                self.validate_markdown_format(relative, content, legacy_allowed=bool(documented))
                if documented:
                    self.warning("RAW_HASH_GAP", relative, "legacy source lacks sha256 and is documented in log.md")
                else:
                    self.error("RAW_HASH_MISSING", relative, "sha256 is missing and no documented legacy gap was found")
                continue
            self.validate_markdown_format(relative, content, legacy_allowed=False)
            if frontmatter is None or frontmatter.body_start < 0:
                self.error("RAW_HASH_BOUNDARY", relative, "cannot locate the post-frontmatter body boundary")
                continue
            if not isinstance(sha_value, str) or not SHA256_RE.fullmatch(sha_value):
                self.error("RAW_HASH_INVALID", relative, "sha256 must be 64 lowercase hexadecimal characters")
                continue
            actual = hashlib.sha256(content[frontmatter.body_start :]).hexdigest()
            if actual != sha_value:
                self.error("RAW_HASH_MISMATCH", relative, f"recorded {sha_value}, calculated {actual}")

        if self.check_git:
            changes = git_changes(self.root)
            if changes is not None:
                for path, status in sorted(changes.items()):
                    if path.startswith("raw/") and path.endswith(".md") and status != "??" and "M" in status:
                        self.error("RAW_BODY_CHANGE_SUSPECTED", path, "tracked raw record was modified; inspect immutable body bytes")

    def classify_noncanonical_link(self, target: str) -> str | None:
        normalized = target.lower()
        if normalized.startswith(("raw/", "raw\\")):
            return "raw"
        if normalized.startswith(("_archive/", "_archive\\")):
            return "archived"
        if normalized.startswith(("templates/", "templates\\")):
            return "template"
        slug = link_slug(normalize_link_target(target))
        for directory, label in (("raw", "raw"), ("_archive", "archived"), ("templates", "template")):
            folder = self.root / directory
            if folder.is_dir() and any(path.stem == slug for path in folder.rglob("*.md")):
                return label
        return None

    def validate_wikilinks(self) -> None:
        active_slugs = set(self.pages_by_slug)
        for page in self.pages:
            distinct_targets: set[str] = set()
            for raw_target in page.links:
                normalized = normalize_link_target(raw_target)
                slug = link_slug(normalized)
                distinct_targets.add(normalized)
                if slug == page.slug:
                    self.error("WIKILINK_SELF", page.relative, f"self-link is not allowed: [[{raw_target}]]")
                    continue
                if slug in active_slugs and len(self.pages_by_slug[slug]) == 1:
                    self.inbound[slug] += 1
                    continue
                kind = self.classify_noncanonical_link(raw_target)
                if kind:
                    self.error("WIKILINK_NONCANONICAL", page.relative, f"{kind} document used as canonical link: [[{raw_target}]]")
                else:
                    self.error("WIKILINK_BROKEN", page.relative, f"target is not an active canonical page: [[{raw_target}]]")
            self.stats.wikilinks += len(distinct_targets)
            valid_outbound = {
                link_slug(normalize_link_target(target))
                for target in page.links
                if link_slug(normalize_link_target(target)) in active_slugs
                and link_slug(normalize_link_target(target)) != page.slug
                and len(self.pages_by_slug[link_slug(normalize_link_target(target))]) == 1
            }
            if self.pages and len(valid_outbound) < 2:
                self.error("WIKILINK_MINIMUM", page.relative, f"has {len(valid_outbound)} distinct valid outbound links; minimum is 2")
        for page in self.pages:
            if self.inbound[page.slug] == 0:
                self.warning("WIKILINK_ORPHAN", page.relative, "page has no inbound canonical links")

    def validate_index(self) -> None:
        index_path = self.root / "index.md"
        if not index_path.is_file():
            self.error("INDEX_MISSING", "index.md", "index file is missing")
            return
        text = index_path.read_text(encoding="utf-8", errors="replace")
        declared_match = re.search(r"(?m)^> Total pages: (\d+)\s*$", text)
        declared = int(declared_match.group(1)) if declared_match else None
        if declared is None:
            self.error("INDEX_COUNT_MISSING", "index.md", "Total pages declaration is missing")

        entries: list[tuple[str | None, str, int]] = []
        current_section: str | None = None
        section_slugs: dict[str, list[str]] = defaultdict(list)
        for number, line in enumerate(text.splitlines(), start=1):
            heading = re.fullmatch(r"## (.+)", line)
            if heading:
                current_section = INDEX_SECTIONS.get(heading.group(1))
                continue
            match = INDEX_ENTRY_RE.fullmatch(line)
            if match:
                target = normalize_link_target(match.group(1))
                slug = link_slug(target)
                entries.append((current_section, slug, number))
                if current_section:
                    section_slugs[current_section].append(slug)
                else:
                    self.error("INDEX_SECTION", "index.md", f"line {number}: entry is outside a canonical type section")
        self.stats.index_entries = len(entries)
        counts = Counter(slug for _, slug, _ in entries)
        active = {page.slug: page for page in self.pages if len(self.pages_by_slug[page.slug]) == 1}
        for slug, page in sorted(active.items()):
            count = counts[slug]
            if count == 0:
                self.error("INDEX_ENTRY_MISSING", "index.md", f"active page is not indexed: {page.relative}")
            elif count > 1:
                self.error("INDEX_ENTRY_DUPLICATE", "index.md", f"active slug {slug!r} appears {count} times")
        for section, slug, number in entries:
            if slug not in active:
                self.error("INDEX_TARGET_INVALID", "index.md", f"line {number}: {slug!r} is not an active canonical page")
                continue
            expected_section = active[slug].directory
            if section != expected_section:
                self.error("INDEX_TYPE_SECTION", "index.md", f"line {number}: {slug!r} belongs under {expected_section}")
        for section, slugs in sorted(section_slugs.items()):
            if slugs != sorted(slugs, key=str.casefold):
                self.error("INDEX_ORDER", "index.md", f"entries under {section} are not alphabetically ordered")
        if declared is not None and declared != len(self.pages):
            self.error("INDEX_COUNT_MISMATCH", "index.md", f"declares {declared}, filesystem has {len(self.pages)} canonical pages")
        if len(entries) != len(self.pages):
            self.error("INDEX_ENTRY_COUNT", "index.md", f"contains {len(entries)} entries for {len(self.pages)} canonical pages")

    def parse_log_entries(self, text: str, path: str) -> list[tuple[str, str, str, str]]:
        headings = list(re.finditer(r"(?m)^## .+$", text))
        entries: list[tuple[str, str, str, str]] = []
        for index, heading in enumerate(headings):
            line = heading.group(0)
            match = LOG_HEADING_RE.fullmatch(line)
            if not match:
                self.error("LOG_HEADING_INVALID", path, f"invalid heading: {line}")
                continue
            date_text, action, subject = match.groups()
            if not valid_calendar_date(date_text):
                self.error("LOG_DATE_INVALID", path, f"invalid date in heading: {line}")
            if action not in LOG_ACTIONS:
                self.error("LOG_ACTION_INVALID", path, f"unsupported action {action!r}")
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            entries.append((date_text, action, subject, text[heading.end() : end]))
        return entries

    def looks_like_repo_path(self, value: str) -> bool:
        value = value.replace("\\", "/")
        prefixes = tuple(CANONICAL_DIRS) + ("raw", "_archive", "templates", "docs", "scripts", "tests")
        names = {"index.md", "log.md", "SCHEMA.md", "AGENTS.md", "README.md", "README.ko.md"}
        return value in names or any(value == prefix or value.startswith(prefix + "/") for prefix in prefixes)

    def affected_log_paths(self, entries: list[tuple[str, str, str, str]]) -> set[str]:
        affected: set[str] = set()
        action_words = re.compile(
            r"(?i)\b(created|updated|deleted|archived|removed|moved|created canonical pages)\b"
        )
        label = re.compile(
            r"^- (?:Created|Updated|Deleted|Archived|Removed|Moved|Created canonical pages)"
        )
        for _, _, _, body in entries:
            in_path_block = False
            for line in body.splitlines():
                if label.match(line):
                    in_path_block = line.rstrip().endswith(":")
                    candidates = PATH_TOKEN_RE.findall(line)
                elif in_path_block and line.startswith("  - "):
                    candidates = PATH_TOKEN_RE.findall(line)
                else:
                    if line.startswith("- "):
                        in_path_block = False
                    candidates = PATH_TOKEN_RE.findall(line) if action_words.search(line) else []
                for candidate in candidates:
                    normalized = candidate.replace("\\", "/").strip()
                    if self.looks_like_repo_path(normalized):
                        affected.add(normalized)
        return affected

    def validate_log(self) -> None:
        log_path = self.root / "log.md"
        if not log_path.is_file():
            self.error("LOG_MISSING", "log.md", "append-only log is missing")
            return
        current_bytes = log_path.read_bytes()
        current_text = current_bytes.decode("utf-8", errors="replace")
        self.parse_log_entries(current_text, "log.md")
        if not self.check_git:
            return
        changes = git_changes(self.root)
        if changes is None:
            self.info("GIT_UNAVAILABLE", "log.md", "git diff checks skipped because root is not a Git worktree")
            return
        baseline = run_git(self.root, "show", "HEAD:log.md")
        if baseline is None or baseline.returncode != 0:
            self.warning("LOG_BASELINE_MISSING", "log.md", "cannot load HEAD:log.md; append-only comparison skipped")
            return
        baseline_bytes = baseline.stdout
        if not current_bytes.startswith(baseline_bytes):
            self.error("LOG_NOT_APPEND_ONLY", "log.md", "content from HEAD was deleted or modified")
            appended_text = ""
        else:
            appended_text = current_bytes[len(baseline_bytes) :].decode("utf-8", errors="replace")
        appended_entries = self.parse_log_entries(appended_text, "log.md (appended)") if appended_text.strip() else []
        changed_canonical = sorted(
            path for path in changes if path.split("/", 1)[0] in CANONICAL_DIRS and path.endswith(".md") and not path.endswith("/.gitkeep")
        )
        changed_raw = sorted(path for path in changes if path.startswith("raw/") and path.endswith(".md") and not path.endswith("/.gitkeep"))
        actions = {entry[1] for entry in appended_entries}
        appended_body = "\n".join(entry[3] for entry in appended_entries)
        tokens = {
            token.replace("\\", "/").strip()
            for token in PATH_TOKEN_RE.findall(appended_body)
            if self.looks_like_repo_path(token.strip())
        }
        affected_tokens = self.affected_log_paths(appended_entries)

        canonical_actions = {"create", "update", "query", "archive", "delete", "repair"}
        if changed_canonical and not actions.intersection(canonical_actions):
            self.error("LOG_CANONICAL_ENTRY_MISSING", "log.md", "canonical changes exist without an appended canonical log action")
        for path in changed_canonical:
            if path not in tokens:
                self.error("LOG_CANONICAL_PATH_MISSING", "log.md", f"changed canonical path is not recorded: {path}")
        if changed_raw and not actions.intersection({"ingest", "repair"}):
            self.error("LOG_INGEST_ENTRY_MISSING", "log.md", "raw Markdown changes exist without an appended ingest/repair entry")
        for path in changed_raw:
            covered = path in tokens or any(token.endswith("/") and path.startswith(token) for token in tokens)
            if not covered:
                self.error("LOG_RAW_PATH_MISSING", "log.md", f"changed raw path is not covered by an affected path: {path}")

        changed_paths = set(changes)
        for token in sorted(affected_tokens):
            if token == "log.md":
                continue
            exact = token.rstrip("/")
            covered = exact in changed_paths or any(path.startswith(exact + "/") for path in changed_paths)
            if not covered:
                self.warning("LOG_PATH_UNVERIFIABLE", "log.md", f"recorded affected path is not verifiable from current diff: {token}")

    def iter_text_files(self) -> Iterable[Path]:
        ignored_parts = {".git", ".ua", "__pycache__"}
        text_suffixes = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".toml", ".env"}
        for path in sorted(self.root.rglob("*"), key=lambda item: item.as_posix()):
            if not path.is_file() or any(part in ignored_parts for part in path.parts):
                continue
            if path.suffix.lower() in text_suffixes or path.name == ".env":
                yield path

    def validate_sensitive_information(self) -> None:
        filename_pattern = re.compile(r"(?i)(?:^|[._-])(api[-_]?key|token|password|secret|session|customer|client|internal|confidential|고객|사내)(?:[._-]|$)")
        assignment_patterns = (
            re.compile(r"(?im)\b(?:api[_ -]?key|access[_ -]?token|password|secret|session[_ -]?(?:id|token)?)\b\s*[:=]\s*['\"]?([^\s'\"`]+)"),
            re.compile(r"(?im)\b(?:customer[_ -]?name|internal[_ -]?project)\b\s*[:=]\s*['\"]?([^\s'\"`]+)"),
        )
        internal_url = re.compile(r"https?://[^\s)\]>'\"]*(?:\.internal|\.corp|\.local\b|\bintranet\b)[^\s)\]>'\"]*", re.I)
        keyword_patterns = {
            "api-key": re.compile(r"(?i)\bapi[-_ ]?key\b"),
            "token": re.compile(r"(?i)\btoken\b"),
            "password": re.compile(r"(?i)\bpassword\b"),
            "secret": re.compile(r"(?i)\bsecret\b"),
            "env-file": re.compile(r"(?i)(?:^|[^A-Za-z0-9_])\.env(?:[^A-Za-z0-9_]|$)"),
            "auth-session": re.compile(r"(?i)\b(?:auth(?:entication)?[-_ ]session|session[-_ ]token)\b|인증\s*세션"),
            "customer/internal-project": re.compile(r"(?i)\b(?:customer[-_ ]name|internal[-_ ]project)\b|고객명|내부\s*프로젝트명"),
        }
        placeholder_values = {"example", "test", "dummy", "placeholder", "redacted", "none", "null", "<value>"}
        for path in self.iter_text_files():
            relative = posix_path(path, self.root)
            if path.name == ".env" or filename_pattern.search(path.name):
                self.warning("SENSITIVE_FILENAME", relative, "filename resembles credential, session, customer, or internal-project data")
            if path.stat().st_size > 2_000_000:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            if relative not in {"scripts/validate_wiki.py", "tests/test_validate_wiki.py"}:
                for label, pattern in keyword_patterns.items():
                    match = pattern.search(text)
                    if match:
                        line = text.count("\n", 0, match.start()) + 1
                        self.warning("SENSITIVE_KEYWORD", relative, f"line {line}: contains sensitive-information keyword {label!r}")
            for pattern in assignment_patterns:
                for match in pattern.finditer(text):
                    value = match.group(1).strip().lower()
                    if value not in placeholder_values and not value.startswith(("${", "{{", "<")):
                        line = text.count("\n", 0, match.start()) + 1
                        self.warning("SENSITIVE_VALUE", relative, f"line {line}: possible credential/customer/internal value")
            for match in internal_url.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                self.warning("INTERNAL_URL", relative, f"line {line}: URL resembles a private or internal host")

    def counts(self) -> tuple[int, int]:
        errors = sum(finding.severity == "ERROR" for finding in self.findings)
        warnings = sum(finding.severity == "WARNING" for finding in self.findings)
        return errors, warnings

    def render(self) -> str:
        severity_rank = {"ERROR": 0, "WARNING": 1, "INFO": 2}
        ordered = sorted(
            self.findings,
            key=lambda finding: (severity_rank[finding.severity], finding.path, finding.code, finding.message),
        )
        lines = [f"{item.severity} [{item.code}] {item.path}: {item.message}" for item in ordered]
        errors, warnings = self.counts()
        lines.extend(
            [
                "",
                "Summary",
                f"  raw source count: {self.stats.raw_sources}",
                f"  canonical page count: {self.stats.canonical_pages}",
                f"  entity count: {self.stats.canonical_by_type['entity']}",
                f"  concept count: {self.stats.canonical_by_type['concept']}",
                f"  comparison count: {self.stats.canonical_by_type['comparison']}",
                f"  query count: {self.stats.canonical_by_type['query']}",
                f"  index entry count: {self.stats.index_entries}",
                f"  wikilink count: {self.stats.wikilinks}",
                f"  source reference count: {self.stats.source_references}",
                f"  claim marker count: {self.stats.claim_markers}",
                f"  ERROR count: {errors}",
                f"  WARNING count: {warnings}",
                f"  result: {'FAIL' if errors else 'PASS'}",
            ]
        )
        return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="wiki root (default: current directory)")
    parser.add_argument("--no-git", action="store_true", help="skip git diff and append-only log checks")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    validator = WikiValidator(Path(args.root), check_git=not args.no_git).validate()
    print(validator.render())
    errors, _ = validator.counts()
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
