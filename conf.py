# docs/conf.py

from __future__ import annotations

from datetime import datetime

from turtini_sphinx_theme import get_theme_paths


# ---- Project metadata ----
project = "OpenShift VM Demo"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"


# ---- Extensions ----
extensions = [
    "myst_parser",
]


# ---- Source config ----
source_suffix = {".md": "markdown"}
root_doc = "index"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# ---- Theme ----
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}


# ---- MyST ----
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]


# ---- Shared theme assets (from turtini-sphinx-theme package) ----
_paths = get_theme_paths()

templates_path = [_paths["templates"]]
html_static_path = ["_static", _paths["static"]]

html_logo = "_static/turtini-logo-white.png"
html_favicon = "_static/favicon.ico"

html_css_files = ["turtini.css"]


# ---- Footer "Last updated" ----
html_last_updated_fmt = "%B %d, %Y"


# ---- Variables for Jinja templates ----
html_context = {
    "turtini_year": datetime.utcnow().year,
}

html_baseurl = ""
