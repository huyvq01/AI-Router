from pathlib import Path

from app.scanner import (
    Project,
    SourceFile,
)


def test_project():

    project = Project(
        root=Path("."),
    )

    assert project.total_files == 0

    project.files.append(
        SourceFile(
            path=Path("main.py"),
            language="python",
        )
    )

    assert project.total_files == 1