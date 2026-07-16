from pathlib import Path

from app.analyzers import statistics_analyzer
from app.scanner.factory import ScannerFactory


def test_statistics_analyzer():

    scanner = ScannerFactory.create(
        Path("."),
    )

    project = scanner.scan(
        Path("."),
    )

    result = statistics_analyzer.analyze(
        project,
    )

    assert result.total_files > 0
    assert result.total_imports >= 0