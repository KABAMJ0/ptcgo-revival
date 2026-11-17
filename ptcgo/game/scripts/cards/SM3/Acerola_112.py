from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_damaged_pokemon, return_pokemon_to_hand

card = SupporterCardDef(
    guid="479eac05-4692-569c-aaff-d8f88dcf0b33",
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
