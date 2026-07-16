from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class FileStatistics(BaseModel):
    """
    Basic statistics of a source file.
    """

    total_lines: int = 0

    blank_lines: int = 0

    comment_lines: int = 0

    code_lines: int = 0

    @classmethod
    def from_file(
        cls,
        path: Path,
    ) -> FileStatistics:
        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        lines = text.splitlines()

        total = len(lines)
        blank = 0
        comment = 0

        for line in lines:
            stripped = line.strip()

            if not stripped:
                blank += 1
                continue

            if stripped.startswith("#"):
                comment += 1

        return cls(
            total_lines=total,
            blank_lines=blank,
            comment_lines=comment,
            code_lines=total - blank - comment,
        )
