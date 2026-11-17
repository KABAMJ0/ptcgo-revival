from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, holder_prize_shift, is_pokemon_card, owned_by

card = PokemonToolCardDef(
    guid="f2c517b6-f0d5-5886-9b0b-79fed97bd954",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPearl.Name",
    display_name="Lillie's Pearl",
    searchable_by=["Lillie's Pearl", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=151,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    passive=holder_prize_shift(-1, all_of(is_pokemon_card, owned_by("lillie")))
)
