""" functionality to create, edit, check and manage doco-files used to deploy a swarm


See https://docs.docker.com/compose/compose-file/#deploy
"""
import re
import os
from copy import deepcopy
from typing import Dict, List, Optional, MutableMapping

from .utils import dump_to_stdout

from .settings import get_constraints, DEBUG


PARAMETER_EXPANSION = re.compile(r'\$\{(\w+)+') # ${parameter}


def resolve_environs(service_environ: List[str], env_vars: Optional[MutableMapping]=None) -> Dict:
    """ Creates a dict with the environment variables
        inside of a webserver container
    """
    if env_vars is None:
        env_vars = os.environ

    container_environ = {
       # 'SIMCORE_WEB_OUTDIR': 'home/scu/services/web/client' # defined in Dockerfile
    }

    for item in service_environ:
        key, value = item.split("=")
        m = PARAMETER_EXPANSION.match(value)
        if m:
            envkey = m.groups()[0]
            value = env_vars[envkey]
        container_environ[key] = value

    return container_environ



def resolve(doco: Dict, exclude: Optional[List[str]]=None, env_vars: Optional[MutableMapping]=None ) -> Dict:
    """ Resolves input doco-file to produce a deployable doco-file

    """
    constraints = get_constraints()
    if exclude is None:
        exclude = []

    deployable_doco = deepcopy(doco)

    for name in doco["services"]:

        # removes some services
        service = deployable_doco["services"][name]
        if name in exclude:
            deployable_doco["services"].pop(name)
            continue

        # remove excluded services also from dependencis
        if any(n in exclude for n in service.get("depends_on", []) ):
            service["depends_on"][:] = [n for n in service["depends_on"] if n not in exclude]
            if not service["depends_on"]: # if empty
                service.pop("depends_on")

        # remove builds
        service.pop("build", None)

        # replace by image
        service.setdefault("image", "services_{}:latest".format(name))

        # add deploy info
        constraint = constraints.get(name, None)
        if constraint is not None:
            service["deploy"] = {
                "placement": {
                    "constraints": list(constraint)
                }
            }

        # resolve environs
        if "environment" in service:
            environs = resolve_environs(service["environment"], env_vars)
            service["environment"] = [ "{}={}".format(k,v) for k,v in environs.items()]


        if DEBUG:
            print("{:-^20}".format(name))
            dump_to_stdout(service)

    return deployable_doco
