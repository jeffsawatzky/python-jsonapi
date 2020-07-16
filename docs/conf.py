"""Sphinx configuration."""
from datetime import datetime


project = "Python JSON:API"
author = "Jeff Sawatzky"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
