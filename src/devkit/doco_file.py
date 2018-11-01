""" Operations on/about docker-compose (or doco) files

"""
from os.path import exists
from pathlib import Path
from typing import Dict, Union

import yaml
import json

from .doco_merge import merge_docos
from .repo_explorer import get_doco_path



def load_from_name(doco_id: str) -> Dict:
    doco_path = get_doco_path(doco_id)
    return load_from_path(doco_path)

def load_from_path(doco_path: Path) -> Dict:
    loader = yaml.safe_load if doco_path.name.endswith(("yaml", "yml")) else json.load
    with doco_path.open() as f:
        doco = loader(f)
    return doco

def load(doco_id: Union[str, Path]) -> Dict:
    if isinstance(doco_id, Path) or exists(doco_id):
        doco_path = Path(doco_id)
        return load_from_path(doco_path)
    return load_from_name(doco_id)


def validate(doco: Dict):
    # TODO: is yaml or json!?
    raise NotImplementedError(str(doco))


def merge(*docos) -> Dict:
    """ Equivalent to

        -f docker-compose-1.yml -f docker-compose-2.yml ...
    """
    doco_dicts = []
    for doco in docos:
        if not isinstance(doco, dict):
            doco = load(doco)
        doco_dicts.append(doco)
    # TODO: validate
    # TODO: check compatibility, e.g. cannot combine docos of different versions?

    return merge_docos(doco_dicts)
