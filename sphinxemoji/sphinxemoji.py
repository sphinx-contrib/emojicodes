import os
import json
from pkg_resources import resource_filename

from docutils import nodes
from docutils.utils import new_document

from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter
from sphinx.util.fileutil import copy_asset

from . import __version__


def load_emoji_codes():
    """
    Load emoji codes from the JSON file.

    This function tweaks some emojis to avoid Sphinx warnings when generating
    the documentation. See:

    - Original issue: https://github.com/sphinx-doc/sphinx/issues/8276
    - New issue: https://sourceforge.net/p/docutils/feature-requests/79/
    """
    fname = resource_filename(__name__, 'codes.json')
    with open(fname, encoding='utf-8') as fp:
        codes = json.load(fp)

    # Avoid unexpected warnings
    warning_keys = []
    for key, value in codes.items():
        if value.startswith("*"):
            warning_keys.append(key)
    for key in warning_keys:
        codes[key] = "\\" + codes[key]

    return codes


class EmojiSubstitutions(SphinxTransform):
    default_priority = 211

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        self.parser = self.app.registry.create_source_parser(self.app, 'rst')

    def apply(self):
        config = self.document.settings.env.config
        settings, source = self.document.settings, self.document['source']

        codes = load_emoji_codes()

        to_handle = (set(codes.keys()) -
                     set(self.document.substitution_defs))

        for ref in self.document.traverse(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = codes[refname]

                doc = new_document(source, settings)
                doc.reporter = LoggingReporter.from_reporter(doc.reporter)
                self.parser.parse(text, doc)

                substitution = doc.next_node()
                # Remove encapsulating paragraph
                if isinstance(substitution, nodes.paragraph):
                    substitution = substitution.next_node()
                ref.replace_self(substitution)


def copy_asset_files(app, exc):
    asset_files = [
        resource_filename(__name__, 'twemoji.js'),
        resource_filename(__name__, 'twemoji.css'),
    ]
    if exc is None:  # build succeeded
        for path in asset_files:
            copy_asset(path, os.path.join(app.outdir, '_static'))


def setup(app):
    app.connect('build-finished', copy_asset_files)
    style = app.config._raw_config.get('sphinxemoji_style')
    if style == 'twemoji':
        app.add_js_file('https://twemoji.maxcdn.com/v/latest/twemoji.min.js')
        app.add_js_file('twemoji.js')
        app.add_css_file('twemoji.css')
    app.add_transform(EmojiSubstitutions)
    return {'version': __version__, 'parallel_read_safe': True}
