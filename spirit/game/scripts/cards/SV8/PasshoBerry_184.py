from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="cd78f22b-da75-5f9d-87da-25c8876359b3",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PasshoBerry.Name",
    display_name="Passho Berry",
    searchable_by=["Passho Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=184,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(60, None, attacker_of_types("water"))
)
