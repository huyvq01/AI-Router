from __future__ import annotations

from pydantic import BaseModel


class AnalysisResult(BaseModel):
    """
    Summary of a scanned project.
    """

    total_files: int
    total_classes: int
    total_functions: int
    total_imports: int