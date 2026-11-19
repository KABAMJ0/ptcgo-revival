"""Coin Booster: a pack of 10 different coins, drawn from every loaded coin product.

Its contents are assembled by product.assemble_coin_pack (BoosterPack.open branches on
COIN_BOOSTER_KEY), not by the set-based card slots. It reuses the generic booster art,
so no bundle has to be built for it.
"""
import json
import uuid

from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.data_utils import BoosterPackDef

product = BoosterPackDef(
    guid=str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:COINBOOSTER")),
    key="COINBOOSTER",
    name="Coin Booster",
    image_url="booster_generic",
    attributes={
        # The pack's info popup lists its slots; ten coins rather than card rarities.
        str(AttrID.PACK_RARITY_DATA.value): {"type": "json", "value": json.dumps([
            {"rarityIcon": Rarities.Common.value, "rarityName": {"id": "Coins"}, "count": 10},
        ])},
    },
)
