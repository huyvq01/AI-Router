from pathlib import Path

from app.scanner.base import BaseScanner
from app.scanner.file import SourceFile
from app.scanner.project import Project


class PythonScanner(BaseScanner):
    def scan(
        self,
        root: Path,
    ) -> Project:
        files = []

        for file in root.rglob("*.py"):
            files.append(
                SourceFile.from_path(
                    file,
                    "python",
                )
            )

        return Project(
            language="python",
            root=str(root),
            files=files,
        )
