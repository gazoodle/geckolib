""" Library to communicate with Gecko Alliance products via the in.touch2 module """

import logging

from .const import GeckoConstants
from .automation import GeckoFacade
from .locator import GeckoLocator
from .driver import GeckoStructAccessor, GeckoSpaPack
from ._version import VERSION
from .utils import GeckoShell

# __all__ = ["GeckoManager"]

# Module logger, uses the library name (at this time it was geckolib) and it
# is silent unless required ...
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = VERSION
