from __future__ import annotations

from pathlib import Path

from app.scanner.base import BaseScanner
from app.scanner.models import SourceFile
from app.scanner.project import Project

from .parser import PythonParser
from .visitor import PythonVisitor
from app.scanner.statistics import FileStatistics


class PythonScanner(BaseScanner):
    """
    Python project scanner.
    """

    def __init__(self) -> None:
        self._parser = PythonParser()

    def scan(
        self,
        root: Path,
    ) -> Project:

        project = Project(
            root=root,
            language="python",
        )

        for file_path in root.rglob("*.py"):

            if any(
                part in ("__pycache__", ".venv", "venv")
                for part in file_path.parts
            ):
                continue

            source = SourceFile(
                path=file_path,
                language="python",
            )

            source.statistics = FileStatistics.from_file(
                file_path,
            )

            try:
                tree = self._parser.parse(
                    file_path.read_text(
                        encoding="utf-8",
                    )
                )

                visitor = PythonVisitor()

                visitor.visit(tree)

                source.imports = visitor.imports
                source.classes = visitor.classes
                source.functions = visitor.functions

            except Exception:
                # Sẽ thay bằng logging ở PR sau
                pass

            project.files.append(source)

        return project