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
        help="the visualization style for rendering, there are 20+ styles to choose from. The default style is `0`, e.g. `pcvis -s 24`",
    )

    parser.add_argument(
        "-f",
        "--file",
        default=None,
        type=str,
        help="the path to the file you want to visualize its page cache status, e.g. `pcvis -f /path/to/my_file`. If you specify this argument, `pcvis` will launch `pcstat` automatically and visualize the result. If this argument is not specified, `pcvis` will read the output of `pcstat` from `stdin`, e.g. `pcstat -json -pps /path/to/my_file | pcvis`",
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


def launch_pcstat(file):
    import subprocess

    cmd = ["pcstat", "-json", "-pps", file]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout.decode("utf-8"), stderr.decode("utf-8")


def main():
    args = parse_sys_args(sys.argv[1:])
    style = args["style"]
    file = args["file"]
    if file:
        pps_json, stderr = launch_pcstat(file)
        if stderr:
            print(stderr)
            return
    else:
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
