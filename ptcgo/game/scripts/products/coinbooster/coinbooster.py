"""Coin Chest: a treasure box holding 2 different coins, drawn from every loaded coin product.

The client opens an archetype as a treasure box, not a booster, when its set is
`RewardItems` (`IsTreasureBox()`), and the treasure box sequence has two prize slots, so
the chest grants two coins. It stays typed as a pack because the shop only lists routed
product types; Packs files it under Booster Packs.

Its contents come from product.assemble_coin_pack: BoosterPack.open branches on this
product's GUID, never on the set key. The GUID is the one the earlier Coin Booster used,
so its shop row and every copy players already own become chests.
"""
import json
import uuid

from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.data_utils import BoosterPackDef

product = BoosterPackDef(
    guid=str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:COINBOOSTER")),
    key="RewardItems",
    name="Coin Chest",
    image_url="base1_booster",
    attributes={
        str(AttrID.PACK_RARITY_DATA.value): {"type": "json", "value": json.dumps([
            {"rarityIcon": Rarities.Common.value, "rarityName": {"id": "Coins"}, "count": 2},
        ])},
    },
)
