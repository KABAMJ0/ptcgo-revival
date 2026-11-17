from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import excluding, gated_damage_boost, is_pokemon_EX

card = PokemonToolCardDef(
    guid="174a5d56-e1c1-5c76-bc16-1c72752c6bba",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilverBangle.Name",
    display_name="Silver Bangle",
    searchable_by=["Silver Bangle", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=88,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    passive=gated_damage_boost(30, excluding(is_pokemon_EX), target=is_pokemon_EX)
)
