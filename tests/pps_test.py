from pcvis.pcvis import parse_pps
import json

def test_parse_pps():
    pps_vis = parse_pps(json.dumps([{"status": [True, False, True]}]))
    assert pps_vis == "▇▁▇"