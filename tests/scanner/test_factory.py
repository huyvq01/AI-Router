from app.scanner.factory import ScannerFactory
from app.scanner.python import PythonScanner


def test_factory():

    scanner = ScannerFactory.create(
        "python",
    )

    assert isinstance(
        scanner,
        PythonScanner,
    )