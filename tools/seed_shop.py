#!/usr/bin/env python3
"""Stock the shop with one booster pack per set, in release order.

Ordering matters because the client renders shop rows by `sort_order`, and the
auto-generated packs all defaulted to 0 -- which is why the shop looked shuffled.

Needs the server running (it uses the admin API):

    ./venv/bin/python tools/seed_shop.py --user brandon --password password

Prices default to 200 Trainer Tokens per pack; override with --price.
"""

import argparse
import json
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8000"
META_PATH = "spirit/database/json_data/set_meta.json"


def call(path, payload=None, cookie=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, method="POST" if data else "GET")
    req.add_header("Content-Type", "application/json")
    if cookie:
        req.add_header("Cookie", cookie)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            cookie_out = r.headers.get("Set-Cookie")
            return json.load(r), cookie_out
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{path}: {e.code} {e.read()[:200]!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="brandon")
    ap.add_argument("--password", default="password")
    ap.add_argument("--price", type=int, default=200)
    args = ap.parse_args()

    _, cookie_header = call("/admin/api/login", {"username": args.user, "password": args.password})
    cookie = cookie_header.split(";")[0] if cookie_header else ""

    products, _ = call("/admin/api/products", cookie=cookie)
    by_key = {}
    for product in products.get("products", []):
        key = product.get("key")
        if key:
            by_key[key.upper()] = product.get("guid")

    meta = json.load(open(META_PATH))
    ordered = sorted(meta.items(), key=lambda kv: kv[1].get("order", 999))

    added = 0
    for code, record in ordered:
        guid = by_key.get(code.upper())
        if not guid:
            print(f"  no booster product for {code}, skipped")
            continue
        call(
            "/admin/api/shop",
            {
                "product_guid": guid,
                "display_name": record["name"],
                "price": args.price,
                "enabled": True,
                "sort_order": record.get("order", 0),
            },
            cookie=cookie,
        )
        added += 1

    items, _ = call("/admin/api/shop", cookie=cookie)
    print(f"shop items seeded: {added} | in shop now: {len(items.get('items', []))}")
    for item in items.get("items", [])[:5]:
        print(f"  {item.get('sort_order'):>3}  {item.get('display_name')}")


if __name__ == "__main__":
    main()
