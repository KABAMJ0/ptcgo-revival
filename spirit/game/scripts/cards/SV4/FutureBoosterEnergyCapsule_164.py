from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import combined, gated_damage_boost, gated_retreat_free, pokemon_of_subtype

card = PokemonToolCardDef(
    guid="c3997836-3522-5fc5-9669-dfcbf0d4b1c7",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FutureBoosterEnergyCapsule.Name",
    display_name="Future Booster Energy Capsule",
    searchable_by=["Future Booster Energy Capsule", "Pok\u00e9mon Tool", "Future"],
    subtypes=["Pok\u00e9mon Tool", "Future"],
    collector_number=164,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    passive=combined(gated_retreat_free(pokemon_of_subtype("Future")), gated_damage_boost(20, pokemon_of_subtype("Future")))
)
