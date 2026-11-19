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

# Products that ship for sale.
DEFAULT_OFFERS = (
    {
        "guid": str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:deck:dragapult-ex-shop")),
        "name": "Dragapult ex",
        "price": 200,
        "sort_order": 10,
    },
    {
        # Coin Chest: a treasure box of two different coins for 1 Trainer Token.
        "guid": str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:COINBOOSTER")),
        "name": "Coin Chest",
        "price": 1,
        "sort_order": 20,
    },
    {
        # Charizard ex + Fusion Strike pack + gold Charizard coin + 1000 tokens back. Pays
        # out more tokens than it costs, so the bundle is one per account.
        "guid": str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:bundle:charizard-ex-collection")),
        "name": "Charizard ex Collection",
        "price": 500,
        # Rows still at a price we shipped earlier move to the new price; a price an admin
        # chose is left alone.
        "previous_prices": (1500,),
        "sort_order": 5,
    },
)


def ensure_default_shop_items():
    """Add the shipped shop rows that are missing; never overwrite an existing one."""
    from ptcgo.database.economy_data import list_shop_items

    try:
        existing = {row["product_guid"].lower(): row for row in list_shop_items()}
    except Exception as e:  # a missing table on a fresh database is not fatal here
        logging.warning(f"[Shop] Could not read shop items to seed defaults: {e}")
        return

    for offer in DEFAULT_OFFERS:
        if offer["guid"].lower() in existing:
            row = existing[offer["guid"].lower()]
            if row["price"] in offer.get("previous_prices", ()):
                try:
                    upsert_shop_item(offer["guid"], price=offer["price"], item_id=row["id"])
                    logging.info(f"[Shop] Repriced {offer['name']} from {row['price']} to {offer['price']} tokens")
                except Exception as e:
                    logging.warning(f"[Shop] Could not reprice {offer['name']}: {e}")
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
