from pydantic import BaseModel, Field


class AnalysisContext(BaseModel):
    language: str

    framework: str | None = None

    dependencies: list[str] = Field(default_factory=list)

    statistics: dict = Field(default_factory=dict)

    files: list[str] = Field(default_factory=list)

    findings: list[str] = Field(default_factory=list)
