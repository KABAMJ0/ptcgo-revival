from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attacker_of_types, takes_less_from

card = PokemonToolCardDef(
    guid="bf58a012-a6aa-5f66-8787-249ef119c3aa",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HabanBerry.Name",
    display_name="Haban Berry",
    searchable_by=["Haban Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=111,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    passive=takes_less_from(60, None, attacker_of_types("dragon"))
)
