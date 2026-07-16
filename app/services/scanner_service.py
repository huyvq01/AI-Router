from __future__ import annotations

from pathlib import Path

from app.scanner.factory import ScannerFactory
from app.scanner.project import Project


class ScannerService:
    """
    High-level service for project scanning.
    """

    def scan(
        self,
        root: str | Path,
    ) -> Project:

        root = Path(root)

        scanner = ScannerFactory.create(root)

        return scanner.scan(root)


scanner_service = ScannerService()