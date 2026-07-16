from pathlib import Path

from app.scanner.ast.python_ast import (
    PythonASTParser,
)


def test_python_ast():
    parser = PythonASTParser()

    module = parser.parse(
        Path("app/main.py"),
    )

    assert module.path

    assert isinstance(
        module.imports,
        list,
    )
