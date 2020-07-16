"""Test cases for the python_jsonapi.core.types.meta module."""
from python_jsonapi.core.types.meta import Meta


def test_init() -> None:
    """Can init a new Meta."""
    sut = Meta()
    assert sut is not None
