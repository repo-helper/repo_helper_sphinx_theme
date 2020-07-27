#!/usr/bin/env python3
#
#  __init__.py
"""
Sphinx Theme for repo_helper.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Based on Alabaster: https://github.com/bitprophet/alabaster/
#  Copyright (c) 2020 Jeff Forcier.
#
#  Based on original work copyright (c) 2011 Kenneth Reitz and copyright (c) 2010
#  Armin Ronacher.
#
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#
#      * Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright notice,
#        this list of conditions and the following disclaimer in the documentation
#        and/or other materials provided with the distribution.
#      * Neither the name of the copyright holder nor the names of its contributors may
#        be used to endorse or promote products derived from this software
#        without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# stdlib
import os

# 3rd party
import alabaster  # type: ignore
from alabaster import get_path, update_context  # type: ignore

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2020 Dominic Davis-Foster"

__license__: str = "BSD"
__version__: str = "0.0.1"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = ["get_path", "update_context", "setup"]


def setup(app):
	# add_html_theme is new in Sphinx 1.6+
	alabaster.setup(app)
	if hasattr(app, "add_html_theme"):
		theme_path = os.path.abspath(os.path.dirname(__file__))
		app.add_html_theme("repo_helper_sphinx_theme", theme_path)
	app.connect("html-page-context", update_context)
	return {
			"version": __version__,
			"parallel_read_safe": True,
			}
