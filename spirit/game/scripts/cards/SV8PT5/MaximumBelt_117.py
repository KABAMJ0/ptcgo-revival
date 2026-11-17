from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_damage_boost, is_pokemon_ex

card = PokemonToolCardDef(
    guid="b6c48e40-0b54-5a84-ad99-0a31417e515f",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaximumBelt.Name",
    display_name="Maximum Belt",
    searchable_by=["Maximum Belt", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=117,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    passive=gated_damage_boost(50, None, target=is_pokemon_ex)
)
