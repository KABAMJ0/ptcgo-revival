from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw_per_prize

card = SupporterCardDef(
    guid="4f686f06-0402-59a7-a521-c4008fe8e7bb",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsAdmin.Name",
    display_name="Rocket's Admin.",
    searchable_by=["Rocket's Admin.", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="CEL25C",
    rarity=Rarities.Common,
    effect=each_player_shuffle_draw_per_prize()
)
