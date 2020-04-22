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

from . import default_stylesheet, charset
from .parser import parser
from .renderer import renderer
from .utils import path_to


class Generator(object):

    def __init__(self):
        self.commands = ['wkhtmltopdf', '-']
        self.default_stylesheet = path_to('res', default_stylesheet)
        self.convert_to_html = False

    def generate(self, filepath, stylesheet=None, output=None):
        if stylesheet is None:
            stylesheet = self.default_stylesheet

        style = open(stylesheet).read()

        # update the output path if not output
        if output is None:
            # default: filename.pdf
            filename = os.path.basename(filepath)
            output = os.path.splitext(filename)[0] + '.pdf'

        prefix, suffix = os.path.splitext(output)

        if suffix.endswith('html'):
            self.convert_to_html = True

        self.commands.append(output)

        start_time = time.time()  # record execute duration

        # convert to html
        html = self.generate_html(filepath, style=style)

        if self.convert_to_html:
            with open(output, 'w') as f:
                f.write(html)
        else:
            # open a process to generate pdf
            proc = subprocess.Popen(self.commands, stdin=subprocess.PIPE,
                                    stdout=sys.stdout, stderr=sys.stderr)
            stdout, stderr = proc.communicate(input=html)

        # calc execute time
        end_time = time.time()
        duration = end_time - start_time
        return (output, duration)

    def generate_html(self, filepath, style=None):
        # open and read source file
        markdown = open(filepath).read()
        
        # parse markdown
        parser.set_source_path(filepath)
        html = parser.parse(markdown)
        # render with template
        html = renderer.render(html=html, style=style)
        
        return html


generator = Generator()
