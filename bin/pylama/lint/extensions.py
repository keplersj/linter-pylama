"""Load extensions."""

import os
import sys

CURDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(CURDIR, '..', '..', 'deps'))


LINTERS = {}

try:
    from pylama.lint.pylama_mccabe import Linter
    LINTERS['mccabe'] = Linter()
except ImportError:
    pass

try:
    from pylama.lint.pylama_pydocstyle import Linter
    LINTERS['pep257'] = Linter()  # for compatibility
    LINTERS['pydocstyle'] = Linter()
except ImportError:
    pass

try:
    from pylama.lint.pylama_pycodestyle import Linter
    LINTERS['pycodestyle'] = Linter()  # for compability
    LINTERS['pep8'] = Linter()  # for compability
except ImportError:
    pass

try:
    from pylama.lint.pylama_pyflakes import Linter
    LINTERS['pyflakes'] = Linter()
except ImportError:
    pass

try:
    from pylama.lint.pylama_pylint import Linter
    LINTERS['pylint'] = Linter()
except ImportError:
    pass

#  pylama:ignore=E0611
