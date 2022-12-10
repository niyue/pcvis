from pcvis.pcvis import parse_sys_args
from unittest import TestCase


def assert_dict_equal(d1, d2):
    TestCase().assertDictEqual(d1, d2)


def test_empty_args_should_use_default_style():
    args = parse_sys_args([])
    assert_dict_equal(
        args,
        {"style": 0, "file": None, "install_pcstat": False},
    )


def test_custom_style():
    args = parse_sys_args(["--style", "1"])
    assert_dict_equal(
        args,
        {"style": 1, "file": None, "install_pcstat": False},
    )


def test_given_file():
    args = parse_sys_args(["--style", "1", "--file", "/foo"])
    assert_dict_equal(
        args,
        {"style": 1, "file": "/foo", "install_pcstat": False},
    )


def test_given_both_file_and_install_pcstat():
    try:
        args = parse_sys_args(
            ["--style", "1", "--file", "/foo", "--install-pcstat"])
        assert False, "Should raise SystemExit due to conflicting arguments"
    except SystemExit:
        pass


def test_install_pcstat():
    args = parse_sys_args(["--install-pcstat"])
    assert_dict_equal(
        args,
        {"style": 0, "file": None, "install_pcstat": True},
    )
