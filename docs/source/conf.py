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

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css"
]
html_short_title = html_title = "RanDoc"
html_context = {
    "default_mode": "light"
}
html_theme_options = {
    "repository_provider": "github",
    "repository_url": "https://github.com/grembeter/randoc",
    "repository_branch": "gh-pages",
    "use_source_button": True,
    "use_repository_button": True,
    "path_to_docs": "_sources/",
    "show_toc_level": 20,
    "show_navbar_depth": 2
}

source_suffix = ".rst"
