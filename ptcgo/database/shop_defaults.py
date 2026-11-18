"""Shop items every install ships with, seeded once at startup.

A shop row is what puts a product on sale: the shop lists admin-configured items
from the `shop_items` table and only falls back to automatic booster pricing for
packs. A deck product with no row would exist in the catalogue and be invisible
in the shop, so the ones we ship are seeded here.

Idempotent by product GUID: an admin who changes the price or disables a row keeps
their change, because the row is only created when it is missing.
"""

import logging
import uuid

from ptcgo.database.economy_data import upsert_shop_item
from ptcgo.game.attributes import AttrID

# Deck products that ship for sale. 200 Trainer Tokens, the same price as a pack.
DEFAULT_DECK_OFFERS = (
    {
        "guid": str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:deck:dragapult-ex-shop")),
        "name": "Dragapult ex",
        "price": 200,
        "sort_order": 10,
    },
)


def ensure_default_shop_items():
    """Add the shipped shop rows that are missing; never overwrite an existing one."""
    from ptcgo.database.economy_data import list_shop_items

    try:
        existing = {row["product_guid"].lower() for row in list_shop_items()}
    except Exception as e:  # a missing table on a fresh database is not fatal here
        logging.warning(f"[Shop] Could not read shop items to seed defaults: {e}")
        return

    for offer in DEFAULT_DECK_OFFERS:
        if offer["guid"].lower() in existing:
            continue
        try:
            upsert_shop_item(
                offer["guid"],
                display_name=offer["name"],
                currency=AttrID.TRAINER_TOKENS.value,
                price=offer["price"],
                enabled=True,
                featured=True,
                top_selling=True,
                sort_order=offer["sort_order"],
            )
            logging.info(f"[Shop] Seeded shop item {offer['name']} at {offer['price']} tokens")
        except Exception as e:
            logging.warning(f"[Shop] Could not seed shop item {offer['name']}: {e}")
