from __future__ import annotations

from app.analyzers.models import AnalysisResult
from app.scanner.project import Project
from app.analyzers.base import BaseAnalyzer


class StatisticsAnalyzer(BaseAnalyzer):
    """
    Analyze basic project statistics.
    """

    def analyze(
        self,
        project: Project,
    ) -> AnalysisResult:

        total_imports = sum(
            len(source.imports)
            for source in project.files
        )

        return AnalysisResult(
            total_files=project.total_files,
            total_classes=project.total_classes,
            total_functions=project.total_functions,
            total_imports=total_imports,
        )


statistics_analyzer = StatisticsAnalyzer()