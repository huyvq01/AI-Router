from app.analyzers.base import BaseAnalyzer


class AnalyzerRegistry:
    def __init__(self) -> None:
        self._analyzers: list[BaseAnalyzer] = []

    def register(
        self,
        analyzer: BaseAnalyzer,
    ) -> None:
        self._analyzers.append(
            analyzer,
        )

    @property
    def analyzers(
        self,
    ) -> list[BaseAnalyzer]:
        return self._analyzers
