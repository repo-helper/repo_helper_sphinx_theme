=================
Installation
=================

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			python3 -m pip install repo_helper_sphinx_theme --user


	.. tab:: from GitHub

		.. prompt:: bash

			python3 -m pip install git+https://github.com/domdfcoding/repo_helper_sphinx_theme@master --user

.. end installation

The theme can then be enabled by setting it in your ``conf.py`` file:

.. code-block:: python

	html_theme = 'repo_helper_sphinx_theme'



Customisation
-----------------

``repo_helper_sphinx_theme`` is based on the `alabaster <https://github.com/bitprophet/alabaster/>`_ theme.
See https://alabaster.readthedocs.io/en/latest/customization.html for information on customising the theme.



Static path for images and/or custom stylesheet
-----------------------------------------------

If you're using any of the image-related options (``logo`` or ``touch-icon``) or a custom stylesheet,
you'll also want to tell Sphinx where to get these files from. If so, add a
line like this (changing the path if necessary; see `the Sphinx docs for
'html_static_path'
<http://sphinx-doc.org/config.html?highlight=static#confval-html_static_path>`_) to your ``conf.py``:

.. code-block:: python

    html_static_path = ['_static']
