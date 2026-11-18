from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_damage_boost, is_pokemon_ex

card = PokemonToolCardDef(
    guid="b790ca93-d140-57fb-a007-491afe69d617",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaximumBelt.Name",
    display_name="Maximum Belt",
    searchable_by=["Maximum Belt", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=154,
    set_code="SV5",
    rarity=Rarities.Rare,
    passive=gated_damage_boost(50, None, target=is_pokemon_ex)
)
