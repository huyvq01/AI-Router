from pathlib import Path

from app.scanner.factory import ScannerFactory


def test_python_visitor():

    scanner = ScannerFactory.create(
        Path("."),
    )

    project = scanner.scan(
        Path("."),
    )

    source = next(
        file
        for file in project.files
        if file.filename == "main.py"
    )

    assert isinstance(source.imports, list)
    assert isinstance(source.classes, list)
    assert isinstance(source.functions, list)