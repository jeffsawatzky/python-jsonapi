"""Test cases for the python_jsonapi.core.types.error module."""
from python_jsonapi.core.types.error import Error


def test_init() -> None:
    """Can init a new Error."""
    sut = Error()
    assert sut is not None
