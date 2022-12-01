from pcvis.pcvis import parse_sys_args
from unittest import TestCase


def assert_dict_equal(d1, d2):
    TestCase().assertDictEqual(d1, d2)


def test_empty_args_should_use_default_style():
    args = parse_sys_args([])
    assert_dict_equal(
        args,
        {"style": 0},
    )


def test_custom_style():
    args = parse_sys_args(["--style", "1"])
    assert_dict_equal(
        args,
        {"style": 1},
    )
