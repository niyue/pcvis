from pcvis.pcvis import parse_pps, sizeof_fmt
import json


def test_parse_pps():
    file_statuses = parse_pps(json.dumps([{"status": [True, False, True]}]))
    file_statuses = list(file_statuses)
    assert len(file_statuses) == 1
    assert file_statuses[0]["vis"] == "█░█"


def test_parse_pps_multi_files():
    file_statuses = parse_pps(json.dumps([
        {"status": [True, False, True]},
        {"status": [False, True, True]}
    ]))
    file_statuses = list(file_statuses)
    assert len(file_statuses) == 2
    assert file_statuses[0]["vis"] == "█░█"
    assert file_statuses[1]["vis"] == "░██"


def test_sizeof_fmt():
    assert sizeof_fmt(0) == "0B"
    assert sizeof_fmt(1) == "1B"
    assert sizeof_fmt(1024) == "1.0KiB"
    assert sizeof_fmt(10240) == "10.0KiB"
    assert sizeof_fmt(10 * 1024 + 100) == "10.1KiB"
    assert sizeof_fmt(10 * 1024 * 1024) == "10.0MiB"
