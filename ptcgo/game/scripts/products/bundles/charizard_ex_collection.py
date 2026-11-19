"""Charizard ex Collection: Obsidian Flames Charizard ex (SV3 125), one Fusion Strike
booster, the ASRBL Gold Charizard coin and 1000 Trainer Tokens. Sold for 500 Trainer
Tokens (shop_defaults), so it pays back more tokens than it costs: it is limited to one
per account, enforced atomically at purchase."""
import uuid

from ptcgo.game.content.bundles import BundleDef

CHARIZARD_EX_SV3_125 = "087b2bf5-039a-55e8-80c8-899dbb0676a3"
FUSION_STRIKE_PACK = "d017c195-83c5-c74e-0638-25128b3116c4"
ASRBL_GOLD_CHARIZARD_COIN = "adb210c2-bca5-5b1a-8b24-c8bcdac41fb8"

product = BundleDef(
    guid=str(uuid.uuid5(uuid.NAMESPACE_URL, "ptcgo:product:bundle:charizard-ex-collection")),
    key="SWSH8",
    name="Charizard ex Collection",
    # assets/products/custom_packs/charizard_ex_collection.png; the packs bundle must be
    # rebuilt (server restart with the bundle scan on) before the client can draw it.
    image_url="charizard_ex_collection",
    contents=[CHARIZARD_EX_SV3_125, FUSION_STRIKE_PACK, ASRBL_GOLD_CHARIZARD_COIN],
    tokens=1000,
    once_per_account=True,
)
