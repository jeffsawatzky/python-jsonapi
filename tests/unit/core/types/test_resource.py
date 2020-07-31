"""Test cases for the python_jsonapi.core.types.resource module."""
from python_jsonapi.core.types.resource import Resource


def test_resource_init() -> None:
    """Can init a new resource."""
    sut = Resource(type="type", id="id")
    assert sut is not None
    assert sut.type == "type"
    assert sut.id == "id"

    attributes = Resource.Attributes()
    sut = Resource(type="type", id="id", attributes=attributes)
    assert sut is not None
    assert sut.attributes == attributes


def test_resource_attribute_init() -> None:
    """Can init a new attributes."""
    sut = Resource.Attributes()
    assert sut is not None
