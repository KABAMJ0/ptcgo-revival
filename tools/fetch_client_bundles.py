#!/usr/bin/env python3
"""Fetch the client-original asset bundles the server serves.

Card art is covered by tools/fetch_art.py, but a few bundles are the *original
game's* artwork -- the Pokemon logos and the landing-page carousel -- and the
server cannot generate those from card data. Without them the client logs in and
shows empty space where the logo and landing art should be.

They are small and live in the upstream repository this project forked from, so
this downloads them into ptcgo/assets/bundleCache/, where the server looks.

    ./venv/bin/python tools/fetch_client_bundles.py

Safe to re-run: existing files are left alone.
"""

import os
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST = os.path.join(ROOT, "ptcgo", "assets", "bundleCache")
UPSTREAM = "https://raw.githubusercontent.com/Bratah123/Spirit-PTCGO/main/spirit/assets/bundleCache"
INNER = "00000000000000000000000001000000"

# folder -> files to pull
BUNDLES = {
    "en_US_Logos": ["__data", "__info"],
    "en_US_LandingPage_CRR80_3": ["__data", "__info"],
    "en_US_LandingPage_CRR87_3": ["__data", "__info"],
}


def get(url, tries=4):
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ptcgo-fetch/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.2 * (attempt + 1))
    return None


def main():
    saved = skipped = failed = 0
    for bundle, files in BUNDLES.items():
        target_dir = os.path.join(DEST, bundle, INNER)
        os.makedirs(target_dir, exist_ok=True)
        for name in files:
            target = os.path.join(target_dir, name)
            if os.path.exists(target) and os.path.getsize(target) > 0:
                skipped += 1
                continue
            blob = get(f"{UPSTREAM}/{bundle}/{INNER}/{name}")
            if blob is None:
                print(f"  {bundle}/{name}: not published upstream, skipped")
                failed += 1
                continue
            with open(target, "wb") as f:
                f.write(blob)
            saved += 1
            print(f"  {bundle}/{name}: {len(blob)} bytes")
    print(f"client bundles: {saved} downloaded, {skipped} already present, {failed} unavailable")
    if saved:
        print("restart the server so its manifest picks them up: systemctl --user restart ptcgo")


if __name__ == "__main__":
    main()
