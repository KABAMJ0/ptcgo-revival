from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import combined, gated_hp_bonus, holder_condition_immunity, pokemon_of_subtype

card = PokemonToolCardDef(
    guid="9768ba4c-0a6e-5ade-9d27-d9a92d44b03b",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientBoosterEnergyCapsule.Name",
    display_name="Ancient Booster Energy Capsule",
    searchable_by=["Ancient Booster Energy Capsule", "Pok\u00e9mon Tool", "Ancient"],
    subtypes=["Pok\u00e9mon Tool", "Ancient"],
    collector_number=140,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=combined(gated_hp_bonus(60, pokemon_of_subtype("Ancient")), holder_condition_immunity(pokemon_of_subtype("Ancient")))
)
