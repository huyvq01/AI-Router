from pathlib import Path

from app.analyzers import analyzer_manager
from app.scanner.factory import ScannerFactory


async def test_manager():

    scanner = ScannerFactory.create(
        Path("."),
    )

    project = scanner.scan(
        Path("."),
    )

    results = await analyzer_manager.analyze(
        project,
    )

    assert len(results) >= 1