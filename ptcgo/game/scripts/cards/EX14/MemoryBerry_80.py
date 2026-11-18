from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import previous_evolution_grant_passive

card = PokemonToolCardDef(
    guid="bb62c9e2-7d57-58e3-93b6-de161ebf1d8c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=previous_evolution_grant_passive()
)
