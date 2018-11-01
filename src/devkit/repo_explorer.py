""" Repo explorer

    Knows about files and directory structure of osparce-simcore repository
"""
from collections import OrderedDict
from enum import Enum
from functools import lru_cache
from pathlib import Path
from typing import Optional

from . import PACKAGE_DIR


@lru_cache(None)
def osparc_simcore_root_dir() -> Path:
    """
    TODO: Assumes that installed somewhere below osparc root folder
    FIXME: check in some configuration file or environ ??
    """
    MAX_LEVELS = 6

    def _is_root(dirpath):
        return any(dirpath.glob("services/web/server"))

    root_dir = PACKAGE_DIR.parent.resolve()
    count = 1
    while not _is_root(root_dir) and count < MAX_LEVELS:
        root_dir = root_dir.parent.resolve()
        count +=1

    assert root_dir.exists(), "Is this service within osparc-simcore repo?"
    assert _is_root(root_dir), "%s not look like rootdir" % root_dir
    return root_dir


@lru_cache(None)
def env_devel_path(name: Optional[str]=None) -> Path:

    if name is None:
        name = ".env-devel"
    fpath = osparc_simcore_root_dir() / name

    assert name.startswith("."), name
    assert fpath.exists(), fpath
    return fpath


@lru_cache(None)
def services_dir():
    fpath = osparc_simcore_root_dir() / "services"
    assert fpath.exists(), fpath
    return fpath



# TODO: replace str by NamedDoco
class NamedDoco(Enum):
    main = 1
    prod = 1
    devel = 2
    tools = 3

# There are named-docos
DOCO_FILENAMES = OrderedDict([
        ('main',  "docker-compose.yml"), ('prod',  "docker-compose.yml"),
        ('devel', "docker-compose.devel.yml"),
        ('tools', "docker-compose.tools.yml") ] )


def get_doco_path(name: str) -> Path:
    """ Returns path to named-doco

    Raise ValueError
    """
    try:
        fpath = services_dir() / DOCO_FILENAMES[name]
        assert fpath.exists(), "Cannot find {} doco. Invalid path {}".format(name, fpath)
    except (AssertionError, KeyError) as err:
        raise ValueError(str(err))
    return fpath
