from pathlib import Path

from app.analyzers import analyzer_manager
from app.scanner.factory import ScannerFactory


async def test_statistics():
    scanner = ScannerFactory.create(
        Path("."),
    )

    project = scanner.scan(
        Path("."),
    )

    findings = await analyzer_manager.analyze(
        project,
    )

    assert len(findings) == 1
