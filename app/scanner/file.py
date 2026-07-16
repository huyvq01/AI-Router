from __future__ import annotations

from hashlib import sha256
from pathlib import Path

from pydantic import BaseModel


class SourceFile(BaseModel):
    path: str

    language: str

    extension: str

    size: int

    checksum: str

    @classmethod
    def from_path(
        cls,
        path: Path,
        language: str,
    ) -> SourceFile:
        checksum = sha256(path.read_bytes()).hexdigest()

        return cls(
            path=str(path),
            language=language,
            extension=path.suffix,
            size=path.stat().st_size,
            checksum=checksum,
        )
