from __future__ import annotations

from abc import ABC, abstractmethod

from app.analyzers.models import AnalysisResult
from app.scanner.project import Project


class BaseAnalyzer(ABC):
    """
    Base class for all analyzers.
    """

    @abstractmethod
    def analyze(
        self,
        project: Project,
    ) -> AnalysisResult:
        """
        Analyze a project and return a single analysis result.
        """