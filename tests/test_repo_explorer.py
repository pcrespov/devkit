from pathlib import Path

import pytest

from simcore_devtool import doco_file, env_file
from simcore_devtool.repo_explorer import (DOCO_FILENAMES, env_devel_path,
                                           get_doco_path, services_dir)


def test_env_files(tmpdir):
    assert env_devel_path().exists()
    env_vars = env_file.load(env_devel_path())
    assert env_vars

    other = tmpdir / ".env"
    with other.open('wt') as f:
        env_file.dump(env_vars, f)

    env_vars2 = env_file.load(other)
    assert env_vars == env_vars2


def test_skeleton():
    assert services_dir().exists()
    assert env_devel_path().exists()

    try:
        assert get_doco_path("main") == get_doco_path("prod")
        for name in DOCO_FILENAMES:
            assert isinstance(get_doco_path(name), Path)
    except ValueError as err:
        pytest.fail(err)


def test_docos():
    docos = { k:doco_file.load(k) for k,v in DOCO_FILENAMES.items() }

    main, devel, tools = [docos[k] for k in ("main", "devel", "tools")]

    assert all( isinstance(doco, dict) for doco in docos.values() )


    assert all( service in main["services"].keys() for service in devel["services"] )
    assert not any( service in list(main["services"].keys())+list(devel["services"].keys())
                    for service in tools["services"] )
