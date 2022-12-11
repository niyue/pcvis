from pcvis.pcvis import format_date_time
import json


def test_format_datetime():
    result = format_date_time("2022-12-11T12:49:08.563175+08:00")
    assert "ago" in result