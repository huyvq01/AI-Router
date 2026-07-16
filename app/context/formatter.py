from app.context.models import AnalysisContext


class PromptFormatter:
    def format(
        self,
        context: AnalysisContext,
    ) -> str:
        lines = []

        lines.append(f"Language: {context.language}")

        if context.framework:
            lines.append(f"Framework: {context.framework}")

        if context.dependencies:
            lines.append("Dependencies:")

            for dep in context.dependencies:
                lines.append(f"- {dep}")

        if context.findings:
            lines.append("Project Metadata:")

            for finding in context.findings:
                lines.append(f"- {finding}")

        return "\n".join(lines)
