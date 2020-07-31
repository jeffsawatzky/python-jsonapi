"""Test cases for the python_jsonapi.core.types.relationships module."""
from python_jsonapi.core.types.relationships import Relationship
from python_jsonapi.core.types.relationships import RelationshipsMixin


def test_relationship_init() -> None:
    """Can init a new relationships."""
    sut = Relationship()
    assert sut is not None


def test_mixin_init() -> None:
    """Can init a new mixin."""
    sut = RelationshipsMixin()
    assert sut is not None

    relationship = Relationship()
    sut = RelationshipsMixin(relationships={"self": relationship})
    assert sut is not None
    assert sut.relationships is not None
    assert sut.relationships["self"] == relationship


def test_mixin_add_relationship() -> None:
    """Can add a new entry."""
    sut = RelationshipsMixin()
    sut.add_relationship(key="relationship1", relationship=Relationship())
    sut.add_relationship(key="relationship2", relationship=Relationship())
    assert sut.relationships is not None
    assert sut.relationships["relationship1"] is not None
    assert sut.relationships["relationship2"] is not None
