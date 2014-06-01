# coding=utf8

"""
    md2pdf.generator
    ~~~~~~~~~~~~~~~~

    Usage::

        >>> from md2pdf.generator import generator
        >>> generator.generate('sample.md', stylesheet='style.css')
"""

import os
import sys
import time
import subprocess

from md2pdf import default_stylesheet, charset
from md2pdf.parser import parser
from md2pdf.renderer import renderer
from md2pdf.utils import path_to


class Generator(object):

    def __init__(self):
        self.commands = ['wkhtmltopdf', '-']
        self.default_stylesheet = path_to('res', default_stylesheet)

    def generate(self, filepath, stylesheet=None, output=None):
        if stylesheet is None:
            stylesheet = self.default_stylesheet

        style = open(stylesheet).read()
        style = style.decode(charset)

        # update the output path if not output
        if output is None:
            # default: filename.pdf
            filename = os.path.basename(filepath)
            output = os.path.splitext(filename)[0] + '.pdf'
        self.commands.append(output)

        start_time = time.time()  # record execute duration

        # open and read source file
        markdown = open(filepath).read()

        # cast to unicode, jinja eats only unicode
        markdown = markdown.decode(charset)

        # parse markdown
        html = parser.parse(markdown)

        # render with template
        html = renderer.render(html=html, style=style)

        # open a process to generate pdf
        proc = subprocess.Popen(self.commands, stdin=subprocess.PIPE,
                                stdout=sys.stdout, stderr=sys.stderr)
        stdout, stderr = proc.communicate(input=html.encode(charset))
        # calc execute time
        end_time = time.time()
        duration = end_time - start_time
        return (output, duration)


generator = Generator()
