from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, look_top_take_rest_shuffle

card = SupporterCardDef(
    guid="2c00bb26-4cf3-52e2-9b1e-145382667863",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hassel.Name",
    display_name="Hassel",
    searchable_by=["Hassel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=look_top_take_rest_shuffle(8, 3), condition=knocked_out_last_turn()
)
