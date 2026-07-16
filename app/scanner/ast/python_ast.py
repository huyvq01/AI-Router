import ast
from pathlib import Path

from app.scanner.ast.models import (
    ModuleNode,
    ClassNode,
    FunctionNode,
)


class PythonASTParser:
    def parse(
        self,
        path: Path,
    ) -> ModuleNode:
        tree = ast.parse(
            path.read_text(
                encoding="utf-8",
            )
        )

        module = ModuleNode(
            path=str(path),
        )

        for node in tree.body:
            if isinstance(
                node,
                ast.Import,
            ):
                module.imports.extend(alias.name for alias in node.names)

            elif isinstance(
                node,
                ast.ImportFrom,
            ):
                if node.module:
                    module.imports.append(
                        node.module,
                    )

            elif isinstance(
                node,
                ast.FunctionDef,
            ):
                module.functions.append(
                    FunctionNode(
                        name=node.name,
                        line=node.lineno,
                    )
                )

            elif isinstance(
                node,
                ast.ClassDef,
            ):
                clazz = ClassNode(
                    name=node.name,
                    line=node.lineno,
                )

                for child in node.body:
                    if isinstance(
                        child,
                        ast.FunctionDef,
                    ):
                        clazz.methods.append(
                            FunctionNode(
                                name=child.name,
                                line=child.lineno,
                            )
                        )

                module.classes.append(
                    clazz,
                )

        return module
