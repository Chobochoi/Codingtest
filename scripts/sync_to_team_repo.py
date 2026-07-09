#!/usr/bin/env python3
"""Sync a local CS-Study/<YYYY-MM>.md log into the '## 미수' section of
SooyeonJ/team_CS-Study's matching CS-Study/<YYYY-MM>.md, then push.

Invoked automatically by the post-commit hook (.githooks/post-commit)
whenever a CS-Study/YYYY-MM.md file changes in a commit.
"""
import re
import subprocess
import sys
from pathlib import Path

TEAM_REPO_URL = "https://github.com/SooyeonJ/team_CS-Study.git"
SECTION_HEADER = "## 미수"


def sh(*args, cwd=None):
    subprocess.run(args, cwd=cwd, check=True)


def ensure_sync_clone(sync_dir: Path) -> Path:
    repo_dir = sync_dir / "team_CS-Study"
    if not repo_dir.exists():
        sync_dir.mkdir(parents=True, exist_ok=True)
        sh("git", "clone", TEAM_REPO_URL, str(repo_dir))
    else:
        sh("git", "checkout", "main", cwd=repo_dir)
        sh("git", "pull", "--ff-only", "origin", "main", cwd=repo_dir)
    return repo_dir


def _looks_like_csv_row(line: str) -> bool:
    # Real CSV cells are joined with a bare "," (no trailing space), e.g.
    # "요일,학습 영역,,,". Prose sentences use ", " (comma + space), e.g.
    # "단어, 회화, 독해 등". This tells the two apart.
    return re.search(r",(?!\s)", line) is not None


def parse_local_blocks(text: str) -> str:
    """Convert comma-separated pseudo-table blocks into real markdown tables."""
    blocks = re.split(r"\n\s*\n", text.strip())
    out_blocks = []
    for block in blocks:
        lines = [l for l in block.splitlines() if l.strip() != ""]
        table_start = next((i for i, l in enumerate(lines) if _looks_like_csv_row(l)), None)
        if table_start is None:
            out_blocks.append("\n".join(lines))
            continue
        preamble = lines[:table_start]
        table_lines = lines[table_start:]
        rows = [[c.strip() for c in l.split(",")] for l in table_lines]
        header = rows[0]
        sep = ["---"] * len(header)
        md_rows = [header, sep] + rows[1:]
        table_md = "\n".join("| " + " | ".join(r) + " |" for r in md_rows)
        out_blocks.append("\n".join(preamble + [table_md]))
    return "\n\n".join(out_blocks)


def replace_section(target_text: str, new_content: str) -> str:
    lines = target_text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == SECTION_HEADER)
    except StopIteration:
        sep = "" if target_text.endswith("\n") else "\n"
        return target_text + f"{sep}\n{SECTION_HEADER}\n\n{new_content}\n"

    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            end = i
            break

    new_lines = lines[: start + 1] + ["", new_content, ""] + lines[end:]
    return "\n".join(new_lines) + "\n"


def main():
    dry_run = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    if len(args) != 1:
        print("usage: sync_to_team_repo.py [--dry-run] <local-md-path>", file=sys.stderr)
        sys.exit(1)

    local_path = Path(args[0]).resolve()
    month = local_path.stem  # e.g. "2026-07"

    local_text = local_path.read_text(encoding="utf-8")
    converted = parse_local_blocks(local_text)

    sync_dir = local_path.parents[1] / ".sync"
    repo_dir = ensure_sync_clone(sync_dir)

    target_path = repo_dir / "CS-Study" / f"{month}.md"
    if not target_path.exists():
        print(f"[sync] {target_path} not found in team repo, skipping.", file=sys.stderr)
        return

    target_text = target_path.read_text(encoding="utf-8")
    updated_text = replace_section(target_text, converted)
    target_path.write_text(updated_text, encoding="utf-8")

    diff = subprocess.run(
        ["git", "diff", "--quiet", "--", f"CS-Study/{month}.md"], cwd=repo_dir
    )
    if diff.returncode == 0:
        print(f"[sync] no changes for {month}, nothing to push.")
        return

    if dry_run:
        subprocess.run(["git", "diff", "--", f"CS-Study/{month}.md"], cwd=repo_dir)
        subprocess.run(["git", "checkout", "--", f"CS-Study/{month}.md"], cwd=repo_dir)
        print(f"[sync] (dry-run) would have pushed updated {month}.md")
        return

    sh("git", "add", f"CS-Study/{month}.md", cwd=repo_dir)
    sh("git", "commit", "-m", f"study: {month} 미수 학습 기록 업데이트", cwd=repo_dir)
    sh("git", "push", "origin", "main", cwd=repo_dir)
    print(f"[sync] pushed updated {month}.md to team_CS-Study")


if __name__ == "__main__":
    main()
