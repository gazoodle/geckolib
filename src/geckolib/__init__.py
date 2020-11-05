""" Library to communicate with Gecko Alliance products via the in.touch2 module """

import logging

from .const import GeckoConstants
from .automation import GeckoFacade
from .manager import GeckoManager
from .driver import GeckoStructAccessor
from .utils import GeckoShell
from ._version import VERSION

# __all__ = ["GeckoManager"]

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION
