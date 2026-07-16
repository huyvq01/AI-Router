from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field

from app.scanner.models import SourceFile


class Project(BaseModel):
    """
    Represents a scanned source project.
    """

    root: Path

    # Primary language of the project.
    # Hiện tại Scanner chỉ hỗ trợ Python.
    # Sau này ScannerFactory sẽ tự phát hiện Java/Mendix/TypeScript.
    language: str = "python"

    files: list[SourceFile] = Field(default_factory=list)

    @property
    def total_files(self) -> int:
        return len(self.files)

    @property
    def total_classes(self) -> int:
        return sum(
            len(source_file.classes)
            for source_file in self.files
        )

    @property
    def total_functions(self) -> int:
        return sum(
            len(source_file.functions)
            for source_file in self.files
        )

    @property
    def total_imports(self) -> int:
        return sum(
            len(source_file.imports)
            for source_file in self.files
        )