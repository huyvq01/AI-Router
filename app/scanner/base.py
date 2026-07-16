from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from app.scanner.project import Project


class BaseScanner(ABC):
    """
    Base scanner interface.
    """

    @abstractmethod
    def scan(
        self,
        root: Path,
    ) -> Project:
        """
        Scan project.

        Args:
            root: project root directory.

        Returns:
            Project model.
        """