from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="17463d28-8f3f-5726-ae41-c347cc8d3d81",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColburBerry.Name",
    display_name="Colbur Berry",
    searchable_by=["Colbur Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=168,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, None, attacker_of_types("darkness"))
)
