from pathlib import Path

from app.scanner.factory import ScannerFactory


def test_python_scanner():
    scanner = ScannerFactory.create(
        Path("."),
    )

    project = scanner.scan(
        Path("."),
    )

    assert project.language == "python"

    assert len(project.files) > 0

    first = project.files[0]

    assert first.path

    assert first.extension == ".py"

    assert first.size > 0

    assert first.checksum
