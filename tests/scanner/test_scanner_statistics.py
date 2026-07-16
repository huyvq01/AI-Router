from pathlib import Path

from app.scanner.statistics import FileStatistics


def test_statistics():
    stats = FileStatistics.from_file(
        Path("app/main.py"),
    )

    assert stats.total_lines > 0

    assert stats.code_lines > 0
