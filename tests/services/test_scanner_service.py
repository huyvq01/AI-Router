from pathlib import Path

from app.services import scanner_service


def test_scan_project():
    project = scanner_service.scan(
        Path("."),
    )

    assert project.language == "python"

    assert len(project.files) > 0