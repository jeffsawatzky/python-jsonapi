"""Test cases for the python_jsonapi.core.types.links module."""
from uri import URI

from python_jsonapi.core.types.links import Link
from python_jsonapi.core.types.links import LinksMixin


def test_link_init() -> None:
    """Can init a new link."""
    sut = Link(href=URI("/test"))
    assert sut is not None
    assert sut.href == URI("/test")

    sut = Link(href=URI("/test"), rel=["self"])
    assert sut is not None
    assert sut.href == URI("/test")
    assert sut.rel == ["self"]


def test_mixin_init() -> None:
    """Can init a new mixin."""
    sut = LinksMixin()
    assert sut is not None

    link = Link(href=URI("/test"))
    sut = LinksMixin(links={"self": link})
    assert sut is not None
    assert sut.links is not None
    assert sut.links["self"] == link


def test_mixin_add_link() -> None:
    """Can add a new entry."""
    sut = LinksMixin()
    sut.add_link(key="link1", link=Link(href=URI("/test1")))
    sut.add_link(key="link2", link=Link(href=URI("/test2")))
    assert sut.links is not None
    assert sut.links["link1"] is not None
    assert sut.links["link1"].href == URI("/test1")
    assert sut.links["link2"] is not None
    assert sut.links["link2"].href == URI("/test2")
