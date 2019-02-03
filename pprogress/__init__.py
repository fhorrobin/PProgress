"""
Imports for packaging.
"""

try:
    import builtins #  Doesn't work if Python not 3.x
except ImportError:
    raise Exception("This package only supports Python 3.")

from .progress import ProgressBar
from ._version import __version__, __version_info__


__all__ = ["__version__", "__version_info__", "ProgressBar"]
