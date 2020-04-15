# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
import json
import textwrap
from docutils.parsers.rst import Directive
from pkgutil import get_data

import sphinxemoji

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sphinx Emoji Codes'
copyright = '2019, Miguel Sánchez de León Peque'
author = 'Miguel Sánchez de León Peque'

# The full version, including alpha/beta/rc tags.
release = sphinxemoji.__version__
# The short X.Y version.
version = release.split('-')[0]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxemoji.sphinxemoji',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme_options = {
    'logo_name': 'true',
    'logo_text_align': 'center',
    'description': 'An extension to use emoji codes in your Sphinx documentation!',
    'description_font_style': 'text-align: center',
    'github_banner': 'true',
    'github_user': 'sphinx-contrib',
    'github_repo': 'emojicodes',
    'github_type': 'star',
    'github_count': 'true',
    'show_related': 'true',
    'note_bg': '#e4f2fb',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


class SphinxEmojiTable(Directive):
    """Directive to display all supported emoji codes in a table"""
    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    def run(self):
        doc_source_name = self.state.document.attributes['source']

        codes = get_data('sphinxemoji', 'codes.json')
        codes = json.loads(codes)

        lines = []
        lines.append('.. csv-table:: Supported emoji codes')
        lines.append('   :header: "Emoji", "Code"')
        lines.append('   :widths: 10, 40')
        lines.append('')
        for code in codes.items():
            lines.append('   {1},``{0}``'.format(*code))
        lines.extend(['', ''])
        self.state_machine.insert_input(lines, source=doc_source_name)

        return []

def setup(app):
    app.add_directive('sphinxemojitable', SphinxEmojiTable)
