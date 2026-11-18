from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import knocked_out_last_turn, look_top_take_rest_shuffle

card = SupporterCardDef(
    guid="093fdb59-34d7-5225-a339-2eccd70df382",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hassel.Name",
    display_name="Hassel",
    searchable_by=["Hassel", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    effect=look_top_take_rest_shuffle(8, 3), condition=knocked_out_last_turn()
)
