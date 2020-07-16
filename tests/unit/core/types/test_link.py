"""Test cases for the python_jsonapi.core.types.link module."""
from uri import URI

from python_jsonapi.core.types.link import Link


def test_init() -> None:
    """Can init a new Link."""
    sut = Link(URI("/test"))
    assert sut is not None
