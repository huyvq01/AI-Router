from __future__ import annotations

from app.router_engine.enums import Capability


class CapabilityDetector:
    """
    Detect capability from prompt.

    Hiện tại dùng keyword.
    Sau này sẽ thay bằng AI classifier.
    """

    def detect(
        self,
        prompt: str,
    ) -> Capability:

        text = prompt.lower()

        review_keywords = (
            "review",
            "analyze",
            "phân tích",
            "đánh giá",
        )

        optimize_keywords = (
            "optimize",
            "optimization",
            "performance",
            "tối ưu",
            "hiệu năng",
            "refactor",
        )

        if any(keyword in text for keyword in review_keywords):
            return Capability.CODE_REVIEW

        if any(keyword in text for keyword in optimize_keywords):
            return Capability.CODE_OPTIMIZE

        return Capability.GENERAL


capability_detector = CapabilityDetector()

__all__ = [
    "Capability",
    "CapabilityDetector",
    "capability_detector",
]