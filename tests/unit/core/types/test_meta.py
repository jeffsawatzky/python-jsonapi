"""Test cases for the python_jsonapi.core.types.meta module."""
from python_jsonapi.core.types.meta import Meta
from python_jsonapi.core.types.meta import MetaMixin


def test_meta_init() -> None:
    """Can init a new entry."""
    sut = Meta()
    assert sut is not None


def test_mixin_init() -> None:
    """Can init a new mixin."""
    sut = MetaMixin()
    assert sut is not None

    sut = MetaMixin(meta={"meta": Meta()})
    assert sut is not None
    assert sut.meta is not None
    assert sut.meta["meta"] is not None


def test_mixin_add_meta() -> None:
    """Can add a new entry."""
    sut = MetaMixin()
    sut.add_meta(key="meta1", meta=Meta())
    sut.add_meta(key="meta2", meta=Meta())
    assert sut.meta is not None
    assert sut.meta["meta1"] is not None
    assert sut.meta["meta2"] is not None
