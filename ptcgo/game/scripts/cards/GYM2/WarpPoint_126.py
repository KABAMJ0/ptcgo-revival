from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_switch_then_self_switch

card = ItemCardDef(
    guid="7a2778a7-31ec-5e8c-b37b-418e1b4e2274",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point"],
    subtypes=[],
    collector_number=126,
    set_code="GYM2",
    rarity=Rarities.Common,
    effect=opponent_switch_then_self_switch()
)
