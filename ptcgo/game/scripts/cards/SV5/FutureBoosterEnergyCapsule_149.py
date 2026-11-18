from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import combined, gated_damage_boost, gated_retreat_free, pokemon_of_subtype

card = PokemonToolCardDef(
    guid="26ce9eed-2c87-5aac-8c4d-308d00cac054",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FutureBoosterEnergyCapsule.Name",
    display_name="Future Booster Energy Capsule",
    searchable_by=["Future Booster Energy Capsule", "Pok\u00e9mon Tool", "Future"],
    subtypes=["Pok\u00e9mon Tool", "Future"],
    collector_number=149,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=combined(gated_retreat_free(pokemon_of_subtype("Future")), gated_damage_boost(20, pokemon_of_subtype("Future")))
)
