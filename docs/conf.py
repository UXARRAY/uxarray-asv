# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

import os
import sys

sys.path.insert(0,
                os.path.abspath('../'))  # Source code dir relative to this file

import uxarray

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import Mock as MagicMock


class Mock(MagicMock):

    @classmethod
    def __getattr__(cls, name):
        return MagicMock()


MOCK_MODULES = ["xarray", "dask", "dask.array", "dask.array.core"]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'myst_nb',
    "sphinxext.opengraph",
    "sphinx_design",
    "nbsphinx",
]

extlinks = {
    "issue": ("https://github.com/uxarray/uxarray/issues/%s", "GH"),
    "pull": ("https://github.com/uxarray/uxarray/pull/%s", "PR"),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "iris": ("https://scitools-iris.readthedocs.io/en/latest", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "numba": ("https://numba.pydata.org/numba-doc/latest", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "dask": ("https://docs.dask.org/en/latest", None),
    "cftime": ("https://unidata.github.io/cftime", None),
    "rasterio": ("https://rasterio.readthedocs.io/en/latest", None),
    "sparse": ("https://sparse.pydata.org/en/latest/", None),
    'xarray': ('http://xarray.pydata.org/en/stable/', None),
}

napoleon_use_admonition_for_examples = True
napoleon_include_special_with_doc = True

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'uxarray'

import datetime

current_year = datetime.datetime.now().year
copyright = u'{}, Uxarray'.format(current_year)
author = u'UXARRAY'


# The version info for the project being documented
def read_version():
    for line in open('../meta.yaml').readlines():
        index = line.find('set version')
        if index > -1:
            return line[index + 15:].replace('\" %}', '').strip()


# The short X.Y version.
version = read_version()

# The full version, including alpha/beta/rc tags.
release = read_version()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "sphinx_book_theme"
html_title = ""

autosummary_imported_members = True

html_context = {
    "github_user": "uxarray",
    "github_repo": "uxarray",
    "github_version": "main",
    "doc_path": "docs",
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = dict(
    # analytics_id=''  this is configured in rtfd.io
    # canonical_url="",
    repository_url="https://github.com/uxarray/uxarray",
    repository_branch="main",
    path_to_docs="doc",
    use_edit_page_button=True,
    use_repository_button=True,
    use_issues_button=True,
    home_page_in_toc=False,
    navbar_footer_text="",
    #extra_footer="""<p></p>""",
)

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
# html_title = u'uxarray v0.0.1'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/images/logos/uxarray_temp_logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/images/logos/uxarray_temp_logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["theme_overrides.css"]

# Output file base name for HTML help builder.
htmlhelp_basename = 'uxarraydoc'

autodoc_typehints = 'none'


# Allow for changes to be made to the css in the theme_overrides file
def setup(app):
    app.add_css_file('theme_overrides.css')
