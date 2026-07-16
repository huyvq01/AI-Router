from __future__ import annotations

from app.analyzers.base import BaseAnalyzer
from app.analyzers.statistics import statistics_analyzer
from app.scanner.project import Project


class AnalyzerManager:
    """
    Execute all registered analyzers.
    """

    def __init__(self) -> None:

        self._analyzers: list[BaseAnalyzer] = [
            statistics_analyzer,
        ]

    async def analyze(
        self,
        project: Project,
    ) -> list:

        findings = []

        for analyzer in self._analyzers:
            findings.append(
                analyzer.analyze(project)
            )

        return findings


analyzer_manager = AnalyzerManager()