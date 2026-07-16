from __future__ import annotations

import ast

from app.scanner.models import (
    ClassInfo,
    FunctionInfo,
    ImportInfo,
)


class PythonVisitor(ast.NodeVisitor):
    """
    Collect symbols from a Python AST.
    """

    def __init__(self) -> None:
        self.imports: list[ImportInfo] = []
        self.classes: list[ClassInfo] = []
        self.functions: list[FunctionInfo] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.append(
                ImportInfo(
                    module=alias.name,
                    alias=alias.asname,
                )
            )

        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        module = node.module or ""

        for alias in node.names:
            self.imports.append(
                ImportInfo(
                    module=f"{module}.{alias.name}",
                    alias=alias.asname,
                )
            )

        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        methods: list[FunctionInfo] = []

        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                methods.append(
                    FunctionInfo(
                        name=child.name,
                        lineno=child.lineno,
                        end_lineno=getattr(child, "end_lineno", None),
                    )
                )

        self.classes.append(
            ClassInfo(
                name=node.name,
                lineno=node.lineno,
                end_lineno=getattr(node, "end_lineno", None),
                methods=methods,
            )
        )

        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.append(
            FunctionInfo(
                name=node.name,
                lineno=node.lineno,
                end_lineno=getattr(node, "end_lineno", None),
            )
        )

        self.generic_visit(node)
