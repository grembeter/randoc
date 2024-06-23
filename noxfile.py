import nox

nox.options.reuse_existing_virtualenvs = True


@nox.session()
def bump(session: nox.Session) -> None:
    """Upgrade versions in requirements.txt"""

    session.install("pip-tools")
    session.run("pip-compile", "--upgrade", "--strip-extras",
                "requirements.in")


@nox.session()
def html(session: nox.Session) -> None:
    """Build HTML pages"""

    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "-M", "html",
                "docs/source", "docs/build",
                "--fresh-env",
                "--write-all",
                "--nitpicky",
                external=True)
