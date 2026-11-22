import time
import urllib.request


def test_canary_gate_open():
    url = ("https://raw.githubusercontent.com/fredericowu/aw-app-template/"
           f"ci/canary-gate/gate.txt?t={time.time()}")
    assert urllib.request.urlopen(url, timeout=20).read().decode().strip() == "open"
