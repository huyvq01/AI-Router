class ProviderError(Exception):
    """
    Base exception for provider errors.
    """


class ProviderConnectionError(ProviderError):
    """
    Cannot connect to provider.
    """


class ProviderTimeoutError(ProviderError):
    """
    Provider request timeout.
    """


class ProviderResponseError(ProviderError):
    """
    Invalid response returned by provider.
    """
