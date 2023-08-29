import datetime

project = "randoc"
copyright = f"(c) {datetime.datetime.now().year}, Grygorii Tertychnyi"
author = "Grygorii Tertychnyi"
release = "0.1"

extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tags",
]

tags_create_tags = True

latex_engine = "xelatex"

html_theme = "pydata_sphinx_theme"
html_short_title = html_title = "RanDoc"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css"
]
html_context = {
   "default_mode": "dark"
}
# html_sidebars = {
#     "**": ["sidebar-nav-bs"]
# }
html_theme_options = {
    "footer_end": ["sphinx-version"],
    "footer_start": ["copyright"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/grembeter/randoc",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
    "navbar_end": ["navbar-icon-links"],
    "show_toc_level": 20
}

source_suffix = ".rst"
