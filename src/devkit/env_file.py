""" Tools to create/

"""
from pathlib import Path
from typing import Dict, MutableMapping, IO


def load(envpath: Path) -> Dict:
    """ Loads a .env type of file into a dict """
    env_vars = {}
    with envpath.open() as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=")
                env_vars[key] = value
    return env_vars


def dump(env_vars: MutableMapping, ostream: IO):
    for key, value in env_vars.items():
        ostream.write("{}={}\n".format(key, value))
