from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import any_of, holder_damage_boost, is_pokemon_ex, is_pokemon_gx

card = PokemonToolCardDef(
    guid="6b20d3a2-dbad-5db0-b917-83445ba707f0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name",
    display_name="Choice Band",
    searchable_by=["Choice Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=162,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    passive=holder_damage_boost(30, target_pred=any_of(is_pokemon_gx, is_pokemon_ex))
)
