#!/usr/bin/env python3
import sys
import json
from sys import stdin

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


def main():
    try:
        style = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    except:
        style = 0
    pps_json = read_pps()
    try:
        pps_string = parse_pps(pps_json, style % len(BAR_STYLES))
        print(pps_string)
    except Exception as e:
        print(f"[failed to parse per page status from pcstat] pps_json='{pps_json}' error='{str(e)}'")


if __name__ == "__main__":
    main()
