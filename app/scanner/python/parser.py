from __future__ import annotations

import ast


class PythonParser:
    """
    Thin wrapper around Python AST.
    """

    def parse(
        self,
        source: str,
    ) -> ast.AST:
        return ast.parse(source)
