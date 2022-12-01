#!/usr/bin/env python3
import sys
import json
from sys import stdin
import argparse

import importlib.metadata


BAR_STYLES = [
    "▁▇",
    "░█",
    "⣿▇",
    "□■",
    "⣀⣿",
    "□▩",
    "□▦",
    "▱▰",
    "▭◼",
    "▯▮",
    "◯⬤",
    "01",
    "_#",
    "⬜⬛",
    "⬜🟩",
    "⬜🟦",
    "⬜🟧",
    "🤍💚",
    "🤍💙",
    "🤍🧡",
    "⚪⚫",
    "⚪🟢",
    "⚪🔵",
    "⚪🟠",
    "🌑🌕",
    "❕❗",
    "🥚🐣",
    "❌✅",
]


def get_meta():
    version = "NA"
    summmary = "NA"
    try:
        package_metadada = importlib.metadata.metadata("pcvis")
        # info from pyproject.toml's `version` and `description`
        version = package_metadada.get("Version")
        summary = package_metadada.get("Summary")
    except:
        pass
    return version, summary


def _cli_parser():
    parser = argparse.ArgumentParser(prog="pcvis")
    parser.add_argument(
        "-s",
        "--style",
        default=0,
        type=int,
        help="the visualization style for rendering",
    )

    version, summary = get_meta()

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version} [{summary}]",
        help="show version number",
    )
    return parser


def read_pps():
    lines = ""
    for line in stdin:
        lines += line
    return lines


def parse_pps(pps_json, style=0):
    pps = json.loads(pps_json)
    pps_status = pps[0]["status"]
    out_icon, in_icon = BAR_STYLES[style]
    pps_string = "".join([in_icon if page else out_icon for page in pps_status])
    return pps_string


def parse_sys_args(sys_args):
    parser = _cli_parser()
    args = parser.parse_args(sys_args)
    return vars(args)


def main():
    args = parse_sys_args(sys.argv[1:])
    style = args["style"]
    pps_json = read_pps()
    try:
        pps_string = parse_pps(pps_json, style % len(BAR_STYLES))
        print(pps_string)
    except Exception as e:
        print(
            f"[failed to parse per page status from pcstat] pps_json='{pps_json}' error='{str(e)}'"
        )


if __name__ == "__main__":
    main()
