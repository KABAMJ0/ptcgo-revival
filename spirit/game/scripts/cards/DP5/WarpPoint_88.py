from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_switch_then_self_switch

card = ItemCardDef(
    guid="db3b7b0e-8837-53a7-b762-aea55f1f4720",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=opponent_switch_then_self_switch()
)
