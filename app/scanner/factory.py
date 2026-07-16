from __future__ import annotations

from pathlib import Path

from app.scanner.base import BaseScanner
from app.scanner.python.ast_scanner import PythonScanner


class ScannerFactory:
    """
    Scanner factory.

    Hiện tại:
        Chỉ hỗ trợ Python.

    Sau này:
        - Java
        - Mendix
        - TypeScript
    """

    @staticmethod
    def create(
        root: Path,
    ) -> BaseScanner:

        # TODO:
        # Detect project language automatically.
        # Hiện tại mặc định Python.

        return PythonScanner()