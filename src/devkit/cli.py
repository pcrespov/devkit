# TODO: redo with cookie-cutter
from pathlib import Path
from typing import List

import click

from . import doco_deploy, doco_file, env_file
from .repo_explorer import env_devel_path
from .settings import DEFAULT_OUTPUT_DIR
from .utils import dump_to_file


@click.group()
def doco():
    """ Docker-compose manager
    """
    click.echo("doco")


@doco.command()
@click.option("--output", default="docker-compose.yml", type=click.Path())
@click.argument("inputs", nargs=-1, type=click.Path(exists=True, file_okay=True, readable=True, resolve_path=True))
def merge(inputs: List[Path], output: Path):
    """ Merges multiple docker-compose files into an output docker-compose.yml

    """
    click.echo("merge_docker_compose_files with {} -> {}".format(inputs, output))


@doco.command()
@click.option("--outdir", default=DEFAULT_OUTPUT_DIR, help="Output directory")
def deploy(outdir: Path):
    """ Produces a docker-compose file for deployment. Specifically:
        a) all images versions are pinned
        b) all service constraints are defined
        c) unnecesary services (e.g. webclient) are not included
    """
    click.echo("Creating deploy to {}".format(outdir))

    prod = doco_file.load("main")
    tools = doco_file.load("tools")
    devel = doco_file.load("devel")

    EXCLUDE = ["webclient", "registry"]
    env_vars = env_file.load(env_devel_path()) # TODO: make this optional


    merged = doco_file.merge(prod, tools)
    dc_deploy = doco_deploy.resolve(merged, EXCLUDE, env_vars)
    dump_to_file(dc_deploy, outdir / "docker-compose.yml")


    merged = doco_file.merge(prod, devel, tools)
    dc_devel = doco_deploy.resolve(merged, EXCLUDE, env_vars)
    dump_to_file(dc_devel, outdir / "docker-compose.yml")



main = click.CommandCollection(sources=[doco, ])
