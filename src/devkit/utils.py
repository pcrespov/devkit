""" Unclassified utilities/helpers


"""
import io
import os
from contextlib import closing
from pathlib import Path
from typing import Dict

import yaml


def dump_to_stdout(data: Dict):
    with closing(io.StringIO()) as ios:
        yaml.dump(data, ios, default_flow_style=False)
        print(ios.getvalue()) # pylint: disable=E1101


def dump_to_file(data: Dict, fpath: Path) -> Path:
    os.makedirs(fpath.parent, exist_ok=True)
    with fpath.open('wt') as fh:
        yaml.dump(data, fh, default_flow_style=False)
    return fpath
