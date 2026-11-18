from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, is_pokemon_card, is_trainer_card, knocked_out_last_turn, search_one_of_each

card = SupporterCardDef(
    guid="e2e69de4-d96f-5c7c-bb49-5585d70bc83d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rosa.Name",
    display_name="Rosa",
    searchable_by=["Rosa", "Supporter"],
    subtypes=["Supporter"],
    collector_number=204,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    effect=search_one_of_each([is_pokemon_card, is_trainer_card, is_basic_energy_card]), condition=knocked_out_last_turn()
)
