import os
import json
from pkg_resources import resource_filename

from docutils import nodes
from docutils.utils import new_document

from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter
from sphinx.util.fileutil import copy_asset

from . import __version__


class EmojiSubstitutions(SphinxTransform):
    default_priority = 211

    def __init__(self, document, startnode=None):
        super().__init__(document, startnode)
        self.parser = self.app.registry.create_source_parser(self.app, 'rst')

    def apply(self):
        config = self.document.settings.env.config
        settings, source = self.document.settings, self.document['source']
        codes = resource_filename(__name__, 'codes.json')
        replacements = json.load(open(codes))
        to_handle = (set(replacements.keys()) -
                     set(self.document.substitution_defs))

        for ref in self.document.traverse(nodes.substitution_reference):
            refname = ref['refname']
            if refname in to_handle:
                text = replacements[refname]

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
        app.add_javascript('//twemoji.maxcdn.com/2/twemoji.min.js?11.3')
        app.add_javascript('twemoji.js')
        app.add_stylesheet('twemoji.css')
    app.add_transform(EmojiSubstitutions)
    return {'version': __version__, 'parallel_read_safe': True}
