from simcore_devtool import doco_file


def test_merge_composes():
    main_doco = doco_file.load("main")
    assert isinstance(main_doco, dict)

    devel_doco = doco_file.load("devel")
    assert isinstance(devel_doco, dict)

    tools_doco = doco_file.load("tools")
    assert isinstance(tools_doco, dict)

    merged_doco = doco_file.merge(main_doco, devel_doco, tools_doco)
    assert merged_doco
    assert isinstance(merged_doco, dict)

    assert "portainer" in merged_doco["services"].keys()
    assert "portainer" not in devel_doco["services"].keys()
    assert "portainer" not in main_doco["services"].keys()
