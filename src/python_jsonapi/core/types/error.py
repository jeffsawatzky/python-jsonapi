"""Python JSON:API core error dataclass."""
from dataclasses import dataclass
from typing import List
from typing import Optional
from typing import TypedDict

from python_jsonapi.core.types.link import Link
from python_jsonapi.core.types.meta import Meta


class ErrorLinks(TypedDict):
    """Class to represent a JSON:API error links object."""

    about: Optional[Link]
    type: Optional[List[Link]]


class ErrorSource(TypedDict):
    """Class to represent a JSON:API error link object."""

    pointer: Optional[str]
    parameter: Optional[str]


@dataclass
class Error:
    """Class to represent a JSON:API error object."""

    id: Optional[str] = None
    links: Optional[ErrorLinks] = None
    status: Optional[str] = None
    code: Optional[str] = None
    title: Optional[str] = None
    detail: Optional[str] = None
    source: Optional[ErrorSource] = None
    meta: Optional[Meta] = None
