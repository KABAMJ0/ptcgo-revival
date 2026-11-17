from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attacker_of_types, pokemon_of, takes_less_from

card = PokemonToolCardDef(
    guid="cb29cdbd-6fc3-5402-b2d3-4a58351f626d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThickScale.Name",
    display_name="Thick Scale",
    searchable_by=["Thick Scale", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=211,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(50, pokemon_of("dragon"), attacker_of_types("grass", "fire", "water", "lightning"))
)
