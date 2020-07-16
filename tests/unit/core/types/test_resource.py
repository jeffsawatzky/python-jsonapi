"""Test cases for the python_jsonapi.core.types.resource module."""
from python_jsonapi.core.types.resource import Resource


def test_init() -> None:
    """Can init a new Resource."""
    sut = Resource()
    assert sut is not None
