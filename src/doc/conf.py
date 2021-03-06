#set($package = $namespace.substring(0, $namespace.indexOf(".")))
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import json
from datetime import datetime
import recommonmark
from recommonmark.transform import AutoStructify

sys.path.insert(0, 'src/python')


# -- Project information -----------------------------------------------------

# this assumes the git.mk has been included in zenbuild to create this file
with open('../../build.json') as f:
    build = json.load(f)

project = build['short_description']
author = build['author']
copyright = f'{datetime.now().year}, {author}'

# the full version, including alpha/beta/rc tags
version = build['build']['tag']
release = build['build']['tag']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',

    # markdown
    'recommonmark',
    # auto-generate section labels.
    'sphinx.ext.autosectionlabel',

    # pdf
    'rst2pdf.pdfbuilder',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['api/${package}.rst']

# The master toctree document.
master_doc = 'top'


# PDF

pdf_documents = [('index', 'rst2pdf', build['name'], author)]
latex_engine = 'xelatex'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# markdown

# Prefix document path to section labels, otherwise autogenerated labels would
# look like 'heading' rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

github_doc_root = 'https://github.com/plandes/util/tree/master/doc'


def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Table of Contents',
        'auto_toc_maxdepth': 4,
    }, True)
    app.add_transform(AutoStructify)
