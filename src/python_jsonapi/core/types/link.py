"""Python JSON:API core link dataclass."""
from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional

from uri import URI

from python_jsonapi.core.types.meta import Meta


@dataclass
class Link:
    """Class to represent a JSON:API link object."""

    href: URI
    rel: Optional[List[str]] = None
    meta: Optional[Meta] = None


Links = Dict[str, Link]
