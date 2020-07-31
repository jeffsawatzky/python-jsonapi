"""Test cases for the python_jsonapi.core.types.resource_identifier module."""
from python_jsonapi.core.types.resource_identifier import ResourceIdentifiableMixin
from python_jsonapi.core.types.resource_identifier import ResourceIdentifier


def test_resource_identifiable_mixin_init() -> None:
    """Can init a new resource identifiable mixin."""
    sut = ResourceIdentifiableMixin(type="type", id="id")
    assert sut is not None
    assert sut.type == "type"
    assert sut.id == "id"


def test_resource_identifier_init() -> None:
    """Can init a new resourcer identifer."""
    sut = ResourceIdentifier(type="type", id="id")
    assert sut is not None
    assert sut.type == "type"
    assert sut.id == "id"
