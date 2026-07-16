from pathlib import Path

import yaml


class CapabilityRegistry:
    def __init__(
        self,
        path: str = "config/capabilities.yaml",
    ) -> None:
        self._path = Path(path)

        self._capabilities: dict = {}

    def load(self) -> None:
        with self._path.open(
            "r",
            encoding="utf-8",
        ) as f:
            self._capabilities = yaml.safe_load(f)["capabilities"]

    @property
    def capabilities(self):
        return self._capabilities
