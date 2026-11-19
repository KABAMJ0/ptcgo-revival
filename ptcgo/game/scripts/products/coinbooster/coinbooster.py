"""Coin Booster: a pack of 10 different coins, drawn from every loaded coin product.

It carries the BASE1 set key so the client files it, renders it and opens it like any
booster (an unknown set key left it unopenable). Its contents still come from
product.assemble_coin_pack: BoosterPack.open branches on this product's GUID, never on
the set key, so a real Base Set booster is untouched. The art is base1_booster, which the
packs bundle already holds (it is built from assets/products/custom_packs).
"""
import json
import uuid

from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.data_utils import BoosterPackDef

product = BoosterPackDef(
    guid=str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:COINBOOSTER")),
    key="BASE1",
    name="Coin Booster",
    image_url="base1_booster",
    attributes={
        # The pack's info popup lists its slots; ten coins rather than card rarities.
        str(AttrID.PACK_RARITY_DATA.value): {"type": "json", "value": json.dumps([
            {"rarityIcon": Rarities.Common.value, "rarityName": {"id": "Coins"}, "count": 10},
        ])},
    },
)
