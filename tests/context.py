"""Fix the path."""  # noqa: INP001

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))  # noqa: PTH100, PTH118, PTH120

from geckolib import *  # noqa: F403
