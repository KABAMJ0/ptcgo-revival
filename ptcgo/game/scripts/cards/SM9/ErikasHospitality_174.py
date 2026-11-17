from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_opponent_pokemon, hand_at_most

card = SupporterCardDef(
    guid="3ab9af14-c5d5-5b86-8d07-acbc15d60217",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=draw_per_opponent_pokemon(1), condition=hand_at_most(4)
)
