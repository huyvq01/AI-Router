from __future__ import annotations

import hashlib
from pathlib import Path

from pydantic import BaseModel, Field

from app.scanner.statistics import FileStatistics


class ImportInfo(BaseModel):
    """
    Imported module.
    """

    module: str

    alias: str | None = None


class FunctionInfo(BaseModel):
    """
    Function or method.
    """

    name: str

    lineno: int

    end_lineno: int | None = None


class ClassInfo(BaseModel):
    """
    Python class.
    """

    name: str

    lineno: int

    end_lineno: int | None = None

    methods: list[FunctionInfo] = Field(default_factory=list)


class SourceFile(BaseModel):
    """
    Parsed source file.
    """

    path: Path

    language: str

    imports: list[ImportInfo] = Field(default_factory=list)

    classes: list[ClassInfo] = Field(default_factory=list)

    functions: list[FunctionInfo] = Field(default_factory=list)

    statistics: FileStatistics = Field(
        default_factory=FileStatistics,
    )

    @property
    def filename(self) -> str:
        return self.path.name

    @property
    def stem(self) -> str:
        return self.path.stem

    @property
    def extension(self) -> str:
        return self.path.suffix

    @property
    def relative_path(self) -> str:
        return self.path.as_posix()

    @property
    def size(self) -> int:
        """
        File size in bytes.
        """

        try:
            return self.path.stat().st_size
        except OSError:
            return 0

    @property
    def checksum(self) -> str:
        """
        SHA256 checksum of the file.
        """

        try:
            digest = hashlib.sha256()

            with self.path.open("rb") as file:
                for chunk in iter(lambda: file.read(8192), b""):
                    digest.update(chunk)

            return digest.hexdigest()

        except OSError:
            return ""
