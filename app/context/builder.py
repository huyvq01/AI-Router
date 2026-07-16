from app.context.models import AnalysisContext
from app.scanner.project import Project
from app.analyzers.models import Finding


class ContextBuilder:
    def build(
        self,
        project: Project,
        findings: list[Finding],
    ) -> AnalysisContext:
        return AnalysisContext(
            language=project.language,
            framework=project.framework,
            dependencies=project.dependencies,
            files=[file.path for file in project.files],
            findings=[finding.description for finding in findings],
        )
