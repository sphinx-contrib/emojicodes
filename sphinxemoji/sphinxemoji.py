import json
from pkg_resources import resource_filename

from docutils import nodes
from docutils.utils import new_document

from sphinx.transforms import SphinxTransform
from sphinx.util.docutils import LoggingReporter


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
        to_handle = (set(replacements.keys())
            - set(self.document.substitution_defs))

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


def setup(app):
    app.add_transform(EmojiSubstitutions)
    return {'version': '0.1.0', 'parallel_read_safe': True}
