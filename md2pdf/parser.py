# coding=utf8

"""
    md2pdf.parser
    ~~~~~~~~~~~~~

    Usage::

        >>> from md2pdf.parser import parser
        >>> parser.parse('# markdown string')
        '<h1>markdown string</h1>'
"""

import os

import houdini
import misaka
from misaka import HtmlRenderer, smartypants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from . import charset


class MarkdownRenderer(HtmlRenderer):
    """misaka renderer with color codes feature"""

    source_path = None

    def _code_no_lexer(self, text):
        # encoding to utf8 string
        text = text.encode(charset).strip()
        return ("""<div class="highlight">
                <pre><code>%s</code></pre>
                </div>""" % houdini.escape_html(text))

    def block_code(self, text, lang):
        """text: unicode text to render"""
        if not lang:
            return self._code_no_lexer(text)

        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            return self._code_no_lexer(text)

        formatter = HtmlFormatter()
        return highlight(text, lexer, formatter)

    def image(self, link, title, alt):
        """return abs path of images"""
        if not link.startswith(('http://', 'https://')):
            source_dir = os.path.dirname(self.source_path)
            link = os.path.abspath(os.path.join(source_dir, link))
        return '<img src="%s" title="%s" alt="%s" />' % (link, title, alt)


class Parser(object):
    """Usage::

        parser = Parser()
        parser.parse(markdown_string)  # return html string
    """

    def __init__(self):
        renderer = MarkdownRenderer()
        extensions = (misaka.EXT_FENCED_CODE |
                      misaka.EXT_NO_INTRA_EMPHASIS |
                      misaka.EXT_AUTOLINK)
        self.renderer = renderer
        self.markdown = misaka.Markdown(renderer, extensions=extensions)

    def parse(self, markdown_string):
        return self.markdown(markdown_string)

    def set_source_path(self, filepath):
        self.renderer.source_path = filepath


parser = Parser()
