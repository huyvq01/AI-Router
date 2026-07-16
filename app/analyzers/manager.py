from __future__ import annotations

from app.analyzers.statistics import statistics_analyzer
from app.scanner.project import Project


class AnalyzerManager:
    async def analyze(
        self,
        project: Project,
    ) -> list:
        return [
            statistics_analyzer.analyze(
                project,
            )
        ]


analyzer_manager = AnalyzerManager()
