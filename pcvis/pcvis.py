#!/usr/bin/env python3

import sys
import json
import argparse
import os


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
    summary = "NA"
    try:
        import importlib.metadata
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

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f",
        "--file",
        default=None,
        type=str,
        help="the path to the file you want to visualize its page cache status, e.g. `pcvis -f /path/to/my_file`. If you specify this argument, `pcvis` will launch `pcstat` automatically and visualize the result. If this argument is not specified, `pcvis` will read the output of `pcstat` from `stdin`, e.g. `pcstat -json -pps /path/to/my_file | pcvis`",
    )

    group.add_argument(
        "-i",
        "--install-pcstat",
        action='store_true',
        help="Install pcstat to /usr/local/bin. You can specify `PCVIS_PCSTAT_PATH` env var to alter the default install dir. e.g. `PCVIS_PCSTAT_PATH=/usr/bin pcvis -i`",
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
    for line in sys.stdin:
        lines += line
    return lines


def parse_pps(pps_json, style=0):
    pps = json.loads(pps_json)
    pps_status = pps[0]["status"]
    out_icon, in_icon = BAR_STYLES[style]
    pps_string = "".join(
        [in_icon if page else out_icon for page in pps_status])
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

# download pcstat package from github url according to the system platform,
# extract the binary from the package
def _downlad_pcstat(download_dir):
    import platform
    import urllib.request
    import os
    pcstat_version = os.environ.get("PCVIS_PCSTAT_VERSION", "0.0.1")
    system = os.environ.get("PCVIS_PCSTAT_SYSTEM", platform.system())
    arch = os.environ.get("PCVIS_PCSTAT_ARCH", platform.machine())
    download_url_base = "https://github.com/tobert/pcstat/releases/download"
    if system in ["Darwin", "Linux"] and arch in ["x86_64", "arm64"]:
        download_url = f"{download_url_base}/v{pcstat_version}/pcstat-{pcstat_version}-{system}-{arch}.tar.gz"
        # download pcstat package from download_url to temp folder
        print(f"[downloading pcstat] url={download_url} download_dir={download_dir}")
        urllib.request.urlretrieve(
            download_url, f"{download_dir}/pcstat.tar.gz")
    else:
        raise Exception(
            "Unsupported platform, only support x86_64 and arm64 macOS and Linux")


def install_pcstat_cmd(install_dir):
    if not os.path.exists(f"{install_dir}/pcstat"):
        import tempfile
        import tarfile
        import shutil

        download_dir = tempfile.gettempdir()
        _downlad_pcstat(download_dir)
        # extract the binary from the package
        tar = tarfile.open(f"{download_dir}/pcstat.tar.gz", "r:gz")
        tar.extractall(download_dir)
        os.makedirs(install_dir, 0o755, True)
        shutil.move(f"{download_dir}/pcstat", f"{install_dir}/pcstat")
        print(f"[pcstat installed] path={install_dir}/pcstat")
    else:
        print(f"[pcstat already installed] path={install_dir}/pcstat")


def main():
    args = parse_sys_args(sys.argv[1:])
    style = args["style"]
    file = args["file"]
    install_pcstat = args["install_pcstat"]
    if file:
        pps_json, stderr = launch_pcstat(file)
        if stderr:
            print(stderr)
            return
    elif install_pcstat:
        install_dir = os.environ.get("PCVIS_PCSTAT_PATH", "/usr/local/bin")
        install_pcstat_cmd(install_dir)
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
