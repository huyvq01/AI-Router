from enum import StrEnum


class Capability(StrEnum):
    """
    Supported routing capabilities.
    """

    GENERAL = "general"

    CODE_REVIEW = "code_review"

    CODE_OPTIMIZE = "code_optimize"

    CODE_REFACTOR = "code_refactor"

    CODE_GENERATION = "code_generation"

    DOCUMENTATION = "documentation"
