""" Configuration and defaults


"""
from collections import defaultdict
from functools import lru_cache
from typing import Dict

from . import PACKAGE_DIR

DEFAULT_OUTPUT_DIR = (PACKAGE_DIR / "../../out").resolve()
DEBUG = False


# SWARM OPTIONS ------------
@lru_cache(None)
def get_constraints() -> Dict:
    # TODO: check that these constraints are correct
    _constraints = defaultdict.fromkeys(["director", "webserver"],
        ['node.platform.os == linux', "node.role == manager"])
    _constraints.default_factory = list

    _constraints["apihub"].append('node.platform.os == linux')
    return _constraints

#-------------------------------
