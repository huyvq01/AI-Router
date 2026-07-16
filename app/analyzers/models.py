from __future__ import annotations

from pydantic import BaseModel


class AnalysisResult(BaseModel):
    """
    Statistics of a scanned project.
    """

    total_files: int

    total_classes: int

    total_functions: int

    total_imports: int
