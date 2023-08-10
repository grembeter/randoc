import datetime

project = "randoc"
copyright = f"(c) {datetime.datetime.now().year}, Grygorii Tertychnyi"
author = "Grygorii Tertychnyi"
release = "0.1"

extensions = [
    "sphinx_copybutton",
    "sphinx_tags",
    "sphinx_design"
]

tags_create_tags = True

templates_path = ["_templates"]
exclude_patterns = []
latex_engine = "xelatex"

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = [
    "css/roles.css"
]
html_short_title = html_title = "RanDoc"
html_context = {
    "default_mode": "light"
}
html_theme_options = {
    "show_toc_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/grembeter/randoc",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome"
        }
    ],
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version"]
}

source_suffix = ".rst"

rst_prolog = """
.. include:: <s5defs.txt>
.. default-role::

"""
