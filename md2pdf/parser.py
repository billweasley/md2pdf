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
from misaka import HtmlRenderer, SmartyPants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from md2pdf import charset


class MarkdownRenderer(HtmlRenderer, SmartyPants):
    """misaka renderer with color codes feature"""

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

    def image(link, title, alt):
        """return abs path of images"""
        if not link.startswith(('http://', 'https://')):
            link = os.path.abspath(link)
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
        self.markdown = misaka.Markdown(renderer, extensions=extensions)

    def parse(self, markdown_string):
        return self.markdown.render(markdown_string)


parser = Parser()
