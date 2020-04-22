# coding=utf8

"""Usage:
  md2pdf <filepath> [-s <stylesheet>] [-o <output>]
  md2pdf [-h|-v]

Options:
  -h --help         show help
  -v --version      show version
  -o <output>       output pdf/html path
  -s <stylesheet>   stylesheet path"""

import sys
from docopt import docopt

from . import __version__
from .generator import generator


def main():
    args = docopt(__doc__, version=__version__)

    filepath = args['<filepath>']
    stylesheet = args['-s']
    output = args['-o']

    if not filepath:
        sys.exit(__doc__)

    try:
        results = generator.generate(
            filepath, stylesheet=stylesheet, output=output)
    except Exception as e:
        sys.exit(e)

    message = 'output to %s (%.2fs)\n' % results
    sys.stdout.write(message)
    sys.stdout.flush()
    sys.exit(0)


if __name__ == '__main__':
    main()
