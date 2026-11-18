from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_damaged_pokemon, return_pokemon_to_hand

card = SupporterCardDef(
    guid="14a0b888-bb49-5ec2-82c4-42948c835eb5",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(predicate=is_damaged_pokemon)
)
