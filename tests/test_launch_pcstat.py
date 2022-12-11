from pcvis.pcvis import launch_pcstat
import json


def test_launch_pcstat():
    output, error = launch_pcstat(["README.md", "LICENSE"])
    assert error == ""
    pps = json.loads(output)
    assert len(pps) == 2
    for attr in ["filename", "size", "percent", "status", "pages", "timestamp"]:
        assert attr in pps[0]
    assert pps[0]["filename"] == "README.md"
    assert pps[1]["filename"] == "LICENSE"
