#!/usr/bin/env python
import sys
import json
from sys import stdin


def read_pps():
    lines = ""
    for line in stdin:
        lines += line
    return lines

def parse_pps():
    pps_json = read_pps()
    pps = json.loads(pps_json)
    pps_string = " ".join(["1" if page else "0" for page in pps])
    print(pps_string)


parse_pps()
