# graphviz - create dot, save, render, view

"""Assemble DOT source code and render it with Graphviz.

>>> import graphviz
>>> dot = graphviz.Digraph(comment='The Round Table')

>>> dot.node('A', 'King Arthur')
>>> dot.node('B', 'Sir Bedevere the Wise')
>>> dot.node('L', 'Sir Lancelot the Brave')

>>> dot.edges(['AB', 'AL'])

>>> dot.edge('B', 'L', constraint='false')

>>> print(dot)  #doctest: +NORMALIZE_WHITESPACE
// The Round Table
digraph {
    A [label="King Arthur"]
    B [label="Sir Bedevere the Wise"]
    L [label="Sir Lancelot the Brave"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
"""

from ._settings import set_default_engine, set_default_format, set_jupyter_format

from .backend import (DOT_BINARY, UNFLATTEN_BINARY,
                      render, pipe, pipe_string, pipe_lines, pipe_lines_string,
                      unflatten, version, view,
                      RequiredArgumentError,
                      ExecutableNotFound, CalledProcessError)
from .graphs import Graph, Digraph
from .jupyter_integration import SUPPORTED_JUPYTER_FORMATS
from .parameters import ENGINES, FORMATS, RENDERERS, FORMATTERS
from .quoting import escape, nohtml
from .sources import Source

__all__ = ['ENGINES', 'FORMATS', 'RENDERERS', 'FORMATTERS',
           'DOT_BINARY', 'UNFLATTEN_BINARY',
           'SUPPORTED_JUPYTER_FORMATS',
           'Graph', 'Digraph',
           'Source',
           'escape', 'nohtml',
           'render', 'pipe', 'pipe_string', 'pipe_lines', 'pipe_lines_string',
           'unflatten', 'version', 'view',
           'RequiredArgumentError',
           'ExecutableNotFound', 'CalledProcessError',
           'set_default_engine', 'set_default_format', 'set_jupyter_format']

__title__ = 'graphviz'
__version__ = '0.19.dev0'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'MIT, see LICENSE.txt'
__copyright__ = 'Copyright (c) 2013-2021 Sebastian Bank'

#: :class:`set` of known layout commands used for rendering
#: (``'dot'``, ``'neato'``, ...)
ENGINES = ENGINES

#: :class:`set` of known output formats for rendering
#: (``'pdf'``, ``'png'``, ...)
FORMATS = FORMATS

#: :class:`set` of known output renderers for rendering
#: (``'cairo'``, ``'gd'``, ...)
RENDERERS = RENDERERS

#: :class:`set` of known output formatters for rendering
#: (``'cairo'``, ``'gd'``, ...)
FORMATTERS = FORMATTERS

#: :class:`set` of supported formats for ``_repr_mimebundle_()``
#: (``'svg'``, ``'png'``, ...)
SUPPORTED_JUPYTER_FORMATS = SUPPORTED_JUPYTER_FORMATS

#: :class:`pathlib.Path` of rendering command
#: (``Path('dot')``)
DOT_BINARY = DOT_BINARY

#: :class:`pathlib.Path` of unflatten command
#: (``Path('unflatten')``)
UNFLATTEN_BINARY = UNFLATTEN_BINARY


RequiredArgumentError = RequiredArgumentError


ExecutableNotFound = ExecutableNotFound


CalledProcessError = CalledProcessError
