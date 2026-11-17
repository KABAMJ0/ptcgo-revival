from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_switch_then_self_switch

card = ItemCardDef(
    guid="9fc2273e-5dd3-5c8c-9120-abcdc73c8831",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=opponent_switch_then_self_switch()
)
