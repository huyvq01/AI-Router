from app.router_engine.detector import (
    Capability,
    capability_detector,
)


def test_review():
    capability = capability_detector.detect("Review Java source code")

    assert capability == Capability.CODE_REVIEW


def test_optimize():
    capability = capability_detector.detect("Tối ưu hiệu năng Mendix")

    assert capability == Capability.CODE_OPTIMIZE
