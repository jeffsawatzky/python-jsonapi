"""Test cases for the python_jsonapi.core.types.error module."""
from python_jsonapi.core.types.error import Error
from python_jsonapi.core.types.error import ErrorSource


def test_error_source_init() -> None:
    """Can init a new error source."""
    sut = ErrorSource()
    assert sut is not None

    sut = ErrorSource(pointer="/", parameter="param")
    assert sut is not None
    assert sut.pointer == "/"
    assert sut.parameter == "param"


def test_error_init() -> None:
    """Can init a new error."""
    sut = Error()
    assert sut is not None

    source = ErrorSource()
    sut = Error(
        id="id",
        status="status",
        code="code",
        title="title",
        detail="detail",
        source=source,
    )
    assert sut is not None
    assert sut.id == "id"
    assert sut.status == "status"
    assert sut.code == "code"
    assert sut.title == "title"
    assert sut.detail == "detail"
    assert sut.source == source
