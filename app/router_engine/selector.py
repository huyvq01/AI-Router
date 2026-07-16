from __future__ import annotations

from app.router_engine.enums import Capability
from app.router_engine.registry import ModelRegistry
from app.router_engine.runtime import RuntimeManager
from app.router_engine.scorer import ModelScorer
from app.router_engine.selection import SelectionResult


class ModelSelector:
    """
    Select the highest scored model.
    """

    def __init__(
        self,
        registry: ModelRegistry,
        runtime: RuntimeManager,
        scorer: ModelScorer,
    ) -> None:
        self._registry = registry
        self._runtime = runtime
        self._scorer = scorer

    def select(
        self,
        capability: Capability,
    ) -> SelectionResult:
        candidates: list[tuple[int, object]] = []

        for model in self._registry.all():
            runtime = self._runtime.get(
                model.name,
            )

            score = self._scorer.score(
                capability,
                model,
                runtime,
            )

            candidates.append(
                (
                    score,
                    model,
                )
            )

        candidates.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        best_score, best_model = candidates[0]

        return SelectionResult(
            model=best_model,
            score=best_score,
            reason="Highest score",
        )
