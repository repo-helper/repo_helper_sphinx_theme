#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import



setup(
		description="Sphinx Theme for repo_helper.",
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		entry_points={"sphinx.html_themes": ["repo_helper_sphinx_theme = repo_helper_sphinx_theme"]},
		)
