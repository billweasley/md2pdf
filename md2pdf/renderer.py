# coding=utf8

"""
    md2pdf.renderer
    ~~~~~~~~~~~~~~~

    Usage::

        >>> from md2pdf.renderer import renderer
        >>> renderer(**kwargs)
"""

from jinja2 import Environment, FileSystemLoader

from . import template
from .utils import path_to


class Renderer(object):

    def __init__(self, pdf_template, templates_folder):
        self.env = Environment(loader=FileSystemLoader(templates_folder))
        self.pdf_template = pdf_template

    def render(self, **kwargs):
        return self.env.get_template(self.pdf_template).render(**kwargs)


renderer = Renderer(template, path_to('res'))
