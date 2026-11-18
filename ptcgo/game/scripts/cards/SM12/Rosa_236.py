from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_pokemon_card, is_trainer_card, knocked_out_last_turn, search_one_of_each

card = SupporterCardDef(
    guid="24d620d6-8e86-54fe-a953-09d2af8d8672",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=236,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=search_one_of_each([is_pokemon_card, is_trainer_card, is_basic_energy_card]), condition=knocked_out_last_turn()
)
