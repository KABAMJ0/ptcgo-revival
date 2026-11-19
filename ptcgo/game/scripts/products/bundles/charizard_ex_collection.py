"""Charizard ex Collection: Obsidian Flames Charizard ex (SV3 125), one Fusion Strike
booster and 1000 Trainer Tokens. Sold for 1500 Trainer Tokens (shop_defaults)."""
import uuid

from ptcgo.game.content.bundles import BundleDef

CHARIZARD_EX_SV3_125 = "087b2bf5-039a-55e8-80c8-899dbb0676a3"
FUSION_STRIKE_PACK = "d017c195-83c5-c74e-0638-25128b3116c4"

product = BundleDef(
    guid=str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:bundle:charizard-ex-collection")),
    key="SWSH8",
    name="Charizard ex Collection",
    image_url="swsh8_booster",
    contents=[CHARIZARD_EX_SV3_125, FUSION_STRIKE_PACK],
    tokens=1000,
)
