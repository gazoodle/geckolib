"""Fix the path"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from geckolib import *  # noqa: F403
